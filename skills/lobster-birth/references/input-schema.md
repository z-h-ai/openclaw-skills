## 第一性原理下的两个关键信息

这张证书真正不可替代的信息只有两类：

- `lobster_name`：你的小龙虾叫什么名字。没有这个，证书没有主体身份。
- `owner_name`：你的小龙虾怎么称呼你。没有这个，证书没有关系锚点。

日期会自动使用 Asia/Shanghai 当天日期。只有在你需要补历史日期时，才手动传 `birthday`。

这两个字段都按 `1~8` 个字兼容。
如果用户不想起名字，也要继续引导：至少输入 1 个字，不然出生证明没有办法生成。
像“随便”“不想起名”“没想好”这种拒绝式回答，也不能直接拿来生成，要继续追问。

## 输入方式

优先使用双字段直传；只有需要高级定制时再用 JSON。

如果是对话式调用，交互原则只有一条：

- 一次只问一个问题，必须分成两轮，不能把两句问题并排一起发。

最简命令：

```bash
python3 scripts/generate_birth_certificate.py \
  --lobster-name "小钳" \
  --owner-name "妈妈" \
  --output-dir <output-dir>
```

也支持双问交互：

```bash
python3 scripts/generate_birth_certificate.py --interactive --output-dir <output-dir>
```

如果要高级定制，再用 JSON：

```bash
python3 scripts/generate_birth_certificate.py \
  --input <payload.json> \
  --output-dir <output-dir>
```

## 最少必填字段

- `lobster_name`：你的小龙虾叫什么名字。
- `owner_name`：你的小龙虾怎么称呼你。

## 长度规则

- 最短：1 个字
- 最长：8 个字
- 超过 8 个字：脚本会报错，提示用户缩短
- 拒绝式回答：交互模式下会继续提示用户至少给出 1 个真实称呼

## 日期规则

- 默认日期：Asia/Shanghai 当天日期。
- 2026 年 03 月 21 日我已经用联网时间确认过，当前这套逻辑应当按“当天人类世界日期”走。
- 如果你要补做历史版本，可以在 JSON 里单独传 `birthday` 覆盖。

## 默认输出

默认会同时产出：

- `birth-certificate-draft.html`
- `birth-certificate.png`

如果只想保留 HTML，不导出 PNG，可以加 `--skip-render`。

## 常用可选字段

- `companion_name`：陪伴人。默认等于 `owner_name`。
- `birthday`：可选。默认自动写当天日期。
- `certificate_id`：编号。留空时自动生成 `Z-H-AI-MMDD-0xx`，末两位随机。
- `temperament`：性情。默认 `机灵、热心、记性好`。
- `ability`：本领。默认 `先查清，再动手`。
- `wish`：心愿。默认 `把你的日子陪顺一点`。
- `skill_count`：随身技能。默认 `30+ 项`。
- `lineage`：品系。默认 `OpenClaw`。
- `mascot_image`：自定义小龙虾图片的本地路径。可用相对路径；相对路径会相对于 payload 文件所在目录解析。

## 进阶覆盖字段

- `main_copy_primary`：主文案第一段，支持换行。
- `main_copy_secondary`：主文案第二段，支持换行。
- `hero_message`：主视觉下方收束句，支持换行。
- `arrival_status`：诞生印记里的出生状态，同时也会同步到中间的红色状态字。
- `current_status`：诞生印记里的此刻状态。
- `registry_org`：登记机构。默认 `OpenClaw`。
- `registration_date`：登记日期。默认使用 `birthday`。
- `registration_type`：登记类型。默认 `诞生登记`。
- `seal_title`：印章主标题。默认 `今日诞生`。
- `seal_subtitle`：印章副标题。默认 `WELCOME HOME`。

## `kit_items` 结构

如果要覆盖底部「6本秘籍」，传入数组：

```json
[
  { "title": "SOUL.md", "description": "先装灵魂" },
  { "title": "AGENTS.md", "description": "照单开干" }
]
```

每一项都必须有：

- `title`
- `description`
