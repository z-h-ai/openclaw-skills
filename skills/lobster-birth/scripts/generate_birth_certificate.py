#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import copy
import html
import json
import re
import secrets
import shutil
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    from playwright.async_api import async_playwright
except ModuleNotFoundError:
    async_playwright = None


SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
ASSETS_DIR = SKILL_DIR / "assets"
TEMPLATE_PATH = ASSETS_DIR / "birth-certificate.template.html"
THEME_PATH = ASSETS_DIR / "lobster-theme.css"
DEFAULT_MASCOT_PATH = ASSETS_DIR / "lobster-selected.png"

OUTPUT_HTML_NAME = "birth-certificate-draft.html"
OUTPUT_CSS_NAME = "lobster-theme.css"
OUTPUT_PAYLOAD_NAME = "birth-certificate.payload.json"
OUTPUT_PNG_NAME = "birth-certificate.png"
SHANGHAI_TZ = ZoneInfo("Asia/Shanghai")
DEFAULT_KIT_SECTION_TITLE = "6本秘籍"
MIN_NAME_LENGTH = 1
MAX_NAME_LENGTH = 8
REFUSAL_NAME_VALUES = {
    "不想起",
    "不想起名",
    "不想起名字",
    "不起名",
    "不起名字",
    "不取名",
    "不取名字",
    "没有名字",
    "没名字",
    "不知道",
    "没想好",
    "随便",
    "都行",
    "不填",
    "空着",
}

DEFAULT_KIT_ITEMS = [
    {"title": "SOUL.md", "description": "先装灵魂"},
    {"title": "AGENTS.md", "description": "照单开干"},
    {"title": "USER.md", "description": "懂你脾气"},
    {"title": "HEARTBEAT.md", "description": "自带闹钟"},
    {"title": "IDENTITY.md", "description": "先认工牌"},
    {"title": "MEMORY.md", "description": "越养越懂"},
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="根据两个称呼和当天日期生成专属小龙虾出生证明 HTML 和 PNG。"
    )
    parser.add_argument(
        "--input",
        type=Path,
        help="输入 JSON 路径。适合高级定制。",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="使用双称呼交互式收集信息。",
    )
    parser.add_argument(
        "--owner-name",
        help="你的小龙虾怎么称呼你。"
    )
    parser.add_argument(
        "--lobster-name",
        help="你的小龙虾叫什么名字。"
    )
    parser.add_argument(
        "--birthday",
        help="可选。手动覆盖生日；默认使用 Asia/Shanghai 当天日期。",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="输出目录。会生成 HTML、CSS、图片、PNG 和归档后的 payload。",
    )
    parser.add_argument(
        "--skip-render",
        action="store_true",
        help="只生成 HTML 及资源，不导出 PNG。",
    )
    parser.add_argument(
        "--scale",
        type=int,
        default=2,
        help="PNG 导出倍率，默认 2。",
    )
    args = parser.parse_args()

    direct_mode = any([args.owner_name, args.lobster_name, args.birthday])
    direct_mode_complete = all([args.owner_name, args.lobster_name])
    chosen_modes = sum([bool(args.input), bool(args.interactive), direct_mode])

    if chosen_modes != 1:
        parser.error("请在 `--input`、`--interactive`、三字段直传模式 中三选一。")
    if direct_mode and not direct_mode_complete:
        parser.error("直传模式下必须同时提供 `--owner-name` 和 `--lobster-name`。")

    return args


def load_payload(input_path: Path) -> dict:
    with input_path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError("输入 JSON 顶层必须是对象。")
    return payload


def prompt_value(label: str, default: str | None = None, required: bool = False) -> str:
    suffix = f" [{default}]" if default else ""
    while True:
        value = input(f"{label}{suffix}: ").strip()
        if value:
            return value
        if default is not None:
            return default
        if not required:
            return ""
        print("该字段不能为空，请重新输入。")


def normalize_name(value: str, field_label: str) -> str:
    normalized = str(value).strip()
    length = len(normalized)
    if length < MIN_NAME_LENGTH:
        raise ValueError(f"{field_label}至少要有 1 个字。")
    if length > MAX_NAME_LENGTH:
        raise ValueError(f"{field_label}最多支持 8 个字，当前是 {length} 个字。")
    return normalized


def looks_like_refusal_name(value: str) -> bool:
    normalized = re.sub(r"\s+", "", str(value).strip())
    return normalized in REFUSAL_NAME_VALUES


def prompt_name(label: str, field_label: str) -> str:
    while True:
        raw = input(f"{label}: ").strip()
        if looks_like_refusal_name(raw):
            print(f"{field_label}至少要有 1 个字。先给它起个小名也可以。")
            continue
        try:
            return normalize_name(raw, field_label)
        except ValueError as exc:
            print(str(exc))


def prompt_payload() -> dict:
    print("开始创建专属小龙虾出生证明。只需要两个称呼，当天日期会自动写入。")
    lobster_name = prompt_name("1. 你的小龙虾叫什么名字", "小龙虾名字")
    owner_name = prompt_name("2. 你的小龙虾怎么称呼你", "小龙虾对你的称呼")
    return build_minimal_payload(owner_name, lobster_name)


def current_human_date() -> str:
    today = datetime.now(SHANGHAI_TZ)
    return f"{today.year:04d} 年 {today.month:02d} 月 {today.day:02d} 日"


def build_minimal_payload(
    owner_name: str,
    lobster_name: str,
    birthday: str | None = None,
) -> dict:
    payload = {
        "owner_name": owner_name,
        "lobster_name": lobster_name,
    }
    if birthday:
        payload["birthday"] = birthday
    return payload


def ensure_non_empty(payload: dict, field: str) -> None:
    if not str(payload.get(field, "")).strip():
        raise ValueError(f"字段 `{field}` 为必填。")


def derive_certificate_id(birthday: str) -> str:
    digits = re.sub(r"\D", "", birthday)
    if len(digits) >= 8:
        month_day = digits[4:8]
    elif len(digits) >= 4:
        month_day = digits[-4:]
    else:
        month_day = "0000"

    serial = secrets.randbelow(99) + 1
    return f"Z-H-AI-{month_day}-0{serial:02d}"


def normalize_payload(raw: dict) -> dict:
    payload = copy.deepcopy(raw)

    ensure_non_empty(payload, "owner_name")
    ensure_non_empty(payload, "lobster_name")
    payload["owner_name"] = normalize_name(payload["owner_name"], "小龙虾对你的称呼")
    payload["lobster_name"] = normalize_name(payload["lobster_name"], "小龙虾名字")
    payload.setdefault("birthday", current_human_date())

    payload.setdefault("title_cn", "小龙虾出生证明")
    payload.setdefault("title_en", "Lobster Birth Certificate")
    payload.setdefault("companion_name", payload["owner_name"])
    payload.setdefault("lineage", "OpenClaw")
    payload.setdefault(
        "main_copy_primary",
        "{owner_name}的一只小龙虾，\n今日诞生。",
    )
    payload.setdefault("main_copy_secondary", "从今天起，会帮你干活，也会慢慢懂你。")
    payload.setdefault("temperament", "机灵、热心、记性好")
    payload.setdefault("ability", "先查清，再动手")
    payload.setdefault("wish", "帮你省心、省力、省钱")
    payload.setdefault("arrival_status", "已出生")
    payload.setdefault("skill_count", "34个skill，8大能力模块")
    payload.setdefault("current_status", "等待培养")
    payload.setdefault("hero_message", "今天到家。\n以后陪你一起长大。")
    payload.setdefault("registry_org", "智回科技")
    payload.setdefault("registration_date", payload["birthday"])
    payload.setdefault("registration_type", "诞生登记")
    payload.setdefault("seal_title", "今日诞生")
    payload.setdefault("seal_subtitle", "WELCOME HOME")
    payload.setdefault("mascot_alt", "选定的小龙虾")
    payload.setdefault("kit_section_title", DEFAULT_KIT_SECTION_TITLE)

    if not payload.get("certificate_id"):
        payload["certificate_id"] = derive_certificate_id(payload["birthday"])

    kit_items = payload.get("kit_items")
    if kit_items is None:
        payload["kit_items"] = copy.deepcopy(DEFAULT_KIT_ITEMS)
    elif not isinstance(kit_items, list) or not kit_items:
        raise ValueError("字段 `kit_items` 必须是非空数组。")

    payload["page_title"] = payload.get(
        "page_title",
        f"{payload['title_cn']} - {payload['lobster_name']}",
    )
    return payload


def resolve_local_asset(path_value: str, base_dir: Path | None) -> Path:
    source_path = Path(path_value)
    if not source_path.is_absolute():
        anchor = base_dir if base_dir is not None else Path.cwd()
        source_path = (anchor / source_path).resolve()
    if not source_path.exists():
        raise FileNotFoundError(f"找不到图片素材：{path_value}")
    return source_path


def escape_text(value: str) -> str:
    return html.escape(str(value), quote=True)


def multiline_to_html(value: str) -> str:
    escaped = escape_text(value)
    return escaped.replace("\n", "<br />")


def compact_display_date(value: str) -> str:
    return re.sub(r"\s+", "", str(value).strip())


def render_main_copy_primary(template: str, owner_name: str) -> str:
    token = "{owner_name}"
    underline_width = min(10.4, max(3.6, len(owner_name) + 1.8))
    owner_html = (
        f'<span class="fill-line" style="min-width:{underline_width:.1f}em">'
        f"{escape_text(owner_name)}"
        "</span>"
    )

    if token not in template:
        return multiline_to_html(template)

    chunks = template.split(token)
    rendered: list[str] = []
    for index, chunk in enumerate(chunks):
        if chunk:
            rendered.append(multiline_to_html(chunk))
        if index < len(chunks) - 1:
            rendered.append(owner_html)
    return "".join(rendered)


def render_info_pairs(pairs: list[tuple[str, str]]) -> str:
    return "\n".join(
        (
            f'<div class="info-pair"><span class="k">{escape_text(key)}</span>'
            f'<span class="v">{escape_text(value)}</span></div>'
        )
        for key, value in pairs
    )


def render_trait_cards(items: list[tuple[str, str]]) -> str:
    return "\n".join(
        (
            '<div class="trait-card">'
            f"<h3>{escape_text(title)}</h3>"
            f"<p>{multiline_to_html(value)}</p>"
            "</div>"
        )
        for title, value in items
    )


def render_kit_cards(items: list[dict]) -> str:
    cards: list[str] = []
    for item in items:
        title = item.get("title")
        description = item.get("description")
        if not title or not description:
            raise ValueError("每个 `kit_items` 元素都需要 `title` 和 `description`。")
        cards.append(
            '<article class="mini-card kit-card">'
            f"<h4>{escape_text(title)}</h4>"
            f"<p>{multiline_to_html(description)}</p>"
            "</article>"
        )
    return "\n".join(cards)


def build_context(payload: dict, mascot_filename: str) -> dict[str, str]:
    record_pairs = [
        ("姓名", payload["lobster_name"]),
        ("生日", compact_display_date(payload["birthday"])),
        ("陪伴人", payload["companion_name"]),
        ("编号", payload["certificate_id"]),
        ("品系", payload["lineage"]),
    ]
    left_traits = [
        ("性情", payload["temperament"]),
        ("本领", payload["ability"]),
        ("心愿", payload["wish"]),
    ]
    right_traits = [
        ("出生状态", payload["arrival_status"]),
        ("随身技能", payload["skill_count"]),
        ("此刻状态", payload["current_status"]),
    ]
    registry_pairs = [
        ("机构", payload["registry_org"]),
        ("日期", compact_display_date(payload["registration_date"])),
        ("类型", payload["registration_type"]),
    ]

    return {
        "page_title": escape_text(payload["page_title"]),
        "title_cn": escape_text(payload["title_cn"]),
        "title_en": escape_text(payload["title_en"]),
        "main_copy_primary_html": render_main_copy_primary(
            payload["main_copy_primary"],
            payload["owner_name"],
        ),
        "main_copy_secondary_html": multiline_to_html(payload["main_copy_secondary"]),
        "record_info_html": render_info_pairs(record_pairs),
        "left_traits_html": render_trait_cards(left_traits),
        "right_traits_html": render_trait_cards(right_traits),
        "mascot_alt": escape_text(payload["mascot_alt"]),
        "mascot_image_src": escape_text(f"./{mascot_filename}"),
        "arrival_note": escape_text(payload["arrival_status"]),
        "hero_message_html": multiline_to_html(payload["hero_message"]),
        "kit_section_title": escape_text(payload["kit_section_title"]),
        "kit_cards_html": render_kit_cards(payload["kit_items"]),
        "registry_info_html": render_info_pairs(registry_pairs),
        "seal_title": escape_text(payload["seal_title"]),
        "seal_subtitle": escape_text(payload["seal_subtitle"]),
    }


def render_template(template_text: str, context: dict[str, str]) -> str:
    rendered = template_text
    for key, value in context.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)

    unresolved = sorted(set(re.findall(r"{{[a-zA-Z0-9_]+}}", rendered)))
    if unresolved:
        raise ValueError(f"模板仍有未替换占位符：{', '.join(unresolved)}")
    return rendered


async def render_png(html_path: Path, output_path: Path, scale: int) -> None:
    if async_playwright is None:
        raise RuntimeError(
            "Playwright 未安装。请先安装 playwright，或先使用 `--skip-render` 只生成 HTML。"
        )

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1000, "height": 1400, "device_scale_factor": scale}
        )
        await page.goto(html_path.as_uri())
        await page.wait_for_timeout(1200)
        await page.locator(".poster").screenshot(path=str(output_path), type="png")
        await browser.close()


def main() -> None:
    args = parse_args()

    if args.interactive:
        raw_payload = prompt_payload()
    elif args.input:
        raw_payload = load_payload(args.input.resolve())
    else:
        raw_payload = build_minimal_payload(
            args.owner_name,
            args.lobster_name,
            args.birthday,
        )

    payload = normalize_payload(raw_payload)

    base_dir = args.input.resolve().parent if args.input else Path.cwd()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    mascot_source = DEFAULT_MASCOT_PATH
    custom_mascot = str(payload.get("mascot_image", "")).strip()
    if custom_mascot:
        mascot_source = resolve_local_asset(custom_mascot, base_dir)

    mascot_extension = mascot_source.suffix.lower() or ".png"
    mascot_filename = f"lobster-selected{mascot_extension}"
    shutil.copy2(THEME_PATH, output_dir / OUTPUT_CSS_NAME)
    shutil.copy2(mascot_source, output_dir / mascot_filename)

    template_text = TEMPLATE_PATH.read_text(encoding="utf-8")
    context = build_context(payload, mascot_filename)
    html_output = render_template(template_text, context)

    html_path = output_dir / OUTPUT_HTML_NAME
    payload_path = output_dir / OUTPUT_PAYLOAD_NAME
    png_path = output_dir / OUTPUT_PNG_NAME

    html_path.write_text(html_output, encoding="utf-8")
    payload_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    if not args.skip_render:
        try:
            asyncio.run(render_png(html_path, png_path, args.scale))
        except Exception as exc:
            raise RuntimeError(
                "PNG 导出失败。HTML 已生成，但当前环境可能缺少 Chromium，"
                "或者浏览器启动受限。可先用 `--skip-render` 保留 HTML。"
            ) from exc

    print(f"HTML: {html_path}")
    print(f"CSS: {output_dir / OUTPUT_CSS_NAME}")
    print(f"Mascot: {output_dir / mascot_filename}")
    print(f"Payload: {payload_path}")
    if not args.skip_render:
        print(f"PNG: {png_path}")


if __name__ == "__main__":
    main()
