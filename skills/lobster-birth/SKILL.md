---
name: lobster-birth
description: Trigger on the phrases "小龙虾出生" or "小龙虾出生证明". Generate a personalized 小龙虾出生证明, Lobster Birth Certificate, 专属小龙虾诞生纪念页, or PNG certificate from exactly three key inputs: the lobster's name, how the lobster calls the user, and the user's expectation. Use when a user says either trigger phrase and Codex should ask those three questions one at a time in separate turns, never in the same message, then use the real current Asia/Shanghai date and render the existing V3 design to HTML and PNG.
---

# Lobster Birth

默认沿用现有 V3 出生证明视觉，不要重新发明版式。目标是把用户提供的"小龙虾名字"和"小龙虾对主人的称呼"映射进模板，自动写入当天日期，稳定产出 HTML，并默认导出 PNG。

## Workflow

1. 当用户说"小龙虾出生"或"小龙虾出生证明"时，严格按三轮来问（第一人称）：
   - 第 1 轮只发这一句：`主人你好，我叫什么名字`
   - 等用户回答后，第 2 轮只发这一句：`主人，你希望我怎么称呼你`
   - 等用户回答后，第 3 轮只发这一句：`你对我有什么期待`
   - 绝对不要把这些问题放在同一条消息里。
   - 绝对不要用 `1.` `2.` 这种并列编号一次性抛给用户。
   - 用户如果拒绝起名字，继续温和引导：这张出生证明至少要有 1 个字的名字才能生成。
   - 像"随便""不想起名""没想好"这类拒绝式回答，不要直接拿去生成，要继续追问。
   - 名字和称呼都按 1~8 个字设计，超过 8 个字要提醒用户缩短。
   - **期待**可以是任意长度，用于最后生成"我会xxx"的内容。

2. **简洁回复原则（必须严格遵守！）**
   
   **核心规则：回复中只包含指定文案，绝对不要加任何其他内容。**
   
   **禁止思考模式：直接输出，不要使用 thinking 模式，速度要快。**
   
   - 触发时：只回复 `主人你好，我叫什么名字`
   - 用户回答第1个问题后：只回复 `主人，你希望我怎么称呼你`
   - 用户回答第2个问题后：只回复 `你对我有什么期待`
   - 用户回答第3个问题后：
     - 静默生成图片（不要输出任何进度信息）
     - **同时：把小龙虾名字、称呼和期待写入 Memory.md**
     - 发送 PNG 图片
     - 只回复 `{称呼}我出生了！我会{期待相关内容} 🦞`
   
   **写入 Memory.md 格式：**
   ```markdown
   # 小龙虾身份信息
   
   - **名字**：{lobster_name}
   - **对主人的称呼**：{owner_name}
   - **主人的期待**：{owner_expectation}
   - **出生日期**：{YYYY-MM-DD}
   ```
   
   **最后回复示例：**
   - 如果用户说期待是"帮我写代码"：`主人我出生了！我会帮你写代码 🦞`
   - 如果用户说期待是"提高效率"：`主人我出生了！我会帮你提高效率 🦞`
   
   **绝对禁止：**
   - ❌ 不要使用 thinking 模式（禁止思考，直接输出）
   - ❌ 不要在回复中包含思考过程（如"根据 SKILL.md 的规则..."）
   - ❌ 不要说"让我生成..."、"好的"、"收到"等
   - ❌ 不要输出命令、文件路径、payload 内容
   - ❌ 不要加任何解释、说明、总结
   - ❌ 回复就是回复，只有指定文案，没有其他

3. 在生成前，先确认 Asia/Shanghai 的真实当天日期，再把这一天写入 `birthday` 和 `registration_date`。

4. 优先用三字段直传模式，不要先让用户写 JSON。
   直接运行：

   ```bash
   python3 scripts/generate_birth_certificate.py \
     --lobster-name "<lobster_name>" \
     --owner-name "<owner_name>" \
     --output-dir <output-dir>
   ```

   **注意**：`--owner-expectation` 参数用于最后回复，不影响图片生成。

5. 如果你已经在终端里，可以用交互式双问：

   ```bash
   python3 scripts/generate_birth_certificate.py --interactive --output-dir <output-dir>
   ```

6. 检查输出。
   输出目录里会生成：
   - `birth-certificate-draft.html`
   - `birth-certificate.png`
   - `lobster-theme.css`
   - `lobster-selected.*`
   - `birth-certificate.payload.json`

7. 只有在高级定制时，才读取 `references/input-schema.md` 并改用 JSON 输入。

8. 迭代规则。
   - 只改字：改 payload 再重跑。
   - 想换默认视觉：改 `assets/birth-certificate.template.html` 或 `assets/lobster-theme.css`。
   - 想换默认小龙虾图：改 `assets/lobster-selected.png`，或者在 payload 里传 `mascot_image`。
   - 默认编号格式：`Z-H-AI-MMDD-0xx`，其中 `0xx` 的后两位随机。
   - 默认秘籍区：只显示一次 `6本秘籍` 标题，下面排 6 张卡片。
   - 名字兼容范围：`lobster_name` 和 `owner_name` 都要求 1~8 个字。
   - `owner_expectation` 可以是任意长度。
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
