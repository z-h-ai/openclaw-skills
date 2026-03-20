---
name: lobster-birth
description: Trigger on the phrases “小龙虾出生” or “小龙虾出生证明”. Generate a personalized 小龙虾出生证明, Lobster Birth Certificate, 专属小龙虾诞生纪念页, or PNG certificate from exactly two key inputs: the lobster's name, and how the lobster calls the user. Use when a user says either trigger phrase and Codex should ask those two questions one at a time in separate turns, never in the same message, then use the real current Asia/Shanghai date and render the existing V3 design to HTML and PNG.
---

# Lobster Birth

默认沿用现有 V3 出生证明视觉，不要重新发明版式。目标是把用户提供的“小龙虾名字”和“小龙虾对主人的称呼”映射进模板，自动写入当天日期，稳定产出 HTML，并默认导出 PNG。

## Workflow

1. 当用户说“小龙虾出生”或“小龙虾出生证明”时，严格按两轮来问：
   - 第 1 轮只发这一句：`你的小龙虾叫什么名字`
   - 等用户回答后，第 2 轮只发这一句：`你的小龙虾怎么称呼你`
   - 绝对不要把这两个问题放在同一条消息里。
   - 绝对不要用 `1.` `2.` 这种并列编号一次性抛给用户。
   - 用户如果拒绝起名字，继续温和引导：这张出生证明至少要有 1 个字的名字才能生成。
   - 像“随便”“不想起名”“没想好”这类拒绝式回答，不要直接拿去生成，要继续追问。
   - 两个字段都按 1~8 个字设计，超过 8 个字要提醒用户缩短。

2. 在生成前，先确认 Asia/Shanghai 的真实当天日期，再把这一天写入 `birthday` 和 `registration_date`。

3. 优先用双字段直传模式，不要先让用户写 JSON。
   直接运行：

   ```bash
   python3 scripts/generate_birth_certificate.py \
     --lobster-name "<lobster_name>" \
     --owner-name "<owner_name>" \
     --output-dir <output-dir>
   ```

4. 如果你已经在终端里，可以用交互式双问：

   ```bash
   python3 scripts/generate_birth_certificate.py --interactive --output-dir <output-dir>
   ```

5. 检查输出。
   输出目录里会生成：
   - `birth-certificate-draft.html`
   - `birth-certificate.png`
   - `lobster-theme.css`
   - `lobster-selected.*`
   - `birth-certificate.payload.json`

6. 只有在高级定制时，才读取 `references/input-schema.md` 并改用 JSON 输入。

7. 迭代规则。
   - 只改字：改 payload 再重跑。
   - 想换默认视觉：改 `assets/birth-certificate.template.html` 或 `assets/lobster-theme.css`。
   - 想换默认小龙虾图：改 `assets/lobster-selected.png`，或者在 payload 里传 `mascot_image`。
   - 默认编号格式：`Z-H-AI-MMDD-0xx`，其中 `0xx` 的后两位随机。
   - 默认秘籍区：只显示一次 `6本秘籍` 标题，下面排 6 张卡片。
   - 名字兼容范围：`lobster_name` 和 `owner_name` 都要求 1~8 个字。
   - 版式校验范围：至少验证 `1`、`4`、`8` 个字三档输入，确保不会把正文、秘籍区和登记信息挤出内框。

## Output Convention

- 如果用户要覆盖现有草稿文件，就把 `--output-dir` 指向原来的 `outputs/HTML-Drafts/`。
- 如果只是做新版本，优先生成到一个新子目录，避免直接覆盖原草稿。

## Resources

- `scripts/generate_birth_certificate.py`：主脚本。
- `references/input-schema.md`：输入字段和默认值。
- `references/example-payload.json`：最小可用示例。
- `assets/birth-certificate.template.html`：参数化后的出生证明模板。
- `assets/lobster-theme.css`：默认样式。
- `assets/lobster-selected.png`：默认小龙虾素材。
