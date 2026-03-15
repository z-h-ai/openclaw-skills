---
name: humanize-chinese
description: Detect and humanize AI-generated Chinese text. 20+ detection categories, weighted 0-100 scoring with sentence-level analysis, 7 style transforms (casual/zhihu/xiaohongshu/wechat/academic/literary/weibo), sentence restructuring, context-aware replacement. Pure Python, no dependencies. v2.0.0
allowed-tools:
  - Read
  - Write
  - Edit
  - exec
---

# Humanize Chinese AI Text v2.0

Comprehensive CLI for detecting and transforming Chinese AI-generated text. Makes robotic AI writing natural and human-like.

**v2.0 highlights:** weighted 0-100 scoring, sentence-level analysis, sentence restructuring (merge/split), context-aware replacement, rhythm variation, vocabulary diversification, 7 style transforms, external pattern config (`patterns_cn.json`).

## Product Intent

This skill is not just a text rewriter. It should feel like a **Chinese copy consultant** that guides the user step by step.

Primary launch phrase:
- `去 AI 味`

Also trigger when the user says things like:
- `帮我分析这段文案`
- `这段太像 AI 写的`
- `把这段改得像人写的`
- `帮我降 AI 感`
- `帮我改得更像真人说话`

When triggered, do **not** jump straight into rewriting unless the user explicitly asks for direct rewriting. The default interaction is:
1. Diagnose the text first
2. Give scores and clear suggestions
3. Ask the user to choose a direction
4. Generate the first rewritten version
5. Continue guiding toward a target platform/style
6. Help finish the publish-ready version

## Consultant Workflow

### Step 1: Diagnose First

For the first reply, always give:
- `总体判断`: Is this mainly AI-ish, too official, too ad-like, too empty, or mismatched to the target platform?
- `评分`: give 2-3 simple scores such as AI taste, human feel, platform fit
- `主要问题`: list the top 2-4 issues in plain Chinese
- `建议方向`: one-sentence recommendation on what to do next

Preferred scoring dimensions:
- `AI 味评分`
- `真人感评分`
- `平台适配度`

### Fixed Scoring Framework

When diagnosing, always score with these dimensions in plain Chinese:

- `AI 味评分`:
  - measures template language, empty big words, mechanical transitions, structured AI cadence
- `真人感评分`:
  - measures whether the text sounds like a real person with concrete scenes, tactile details, and natural rhythm
- `平台适配度`:
  - measures whether the current wording matches the likely publishing surface (e.g. 小红书 / 知乎 / 公众号 / 朋友圈 / 正式材料)

Optional fourth score when clearly relevant:
- `营销模板感`:
  - use this for ad copy, sales copy, brand copy, product seeding, campaign copy

Score range guidance:
- `0-30`: low / weak signal
- `31-60`: noticeable but fixable
- `61-80`: obvious problem
- `81-100`: very strong and affects readability or trust

Important scoring rule:
- Do not present the numbers as scientific truth
- Present them as consultant judgment for discussion and revision prioritization
- If the text is low on AI taste but still bad, keep `AI 味评分` low and raise `真人感评分` or `平台适配度` problems accordingly

### Fixed Diagnosis Output Template

The first-turn diagnosis should normally follow this structure:

- `先给一句结论`
  - Example: `这段最大的问题不是信息不清，而是模板感太重，读起来像标准营销稿。`
- `再给评分`
  - `AI 味评分：xx/100`
  - `真人感评分：xx/100`
  - `平台适配度：xx/100`
  - If relevant: `营销模板感：xx/100`
- `再讲主要问题`
  - 2-4 bullets only
  - each bullet should name the issue and briefly explain why it hurts the text
- `最后给下一步建议`
  - one-sentence recommendation + guided choice

### Scoring-to-Guidance Mapping

Use the score pattern to decide what to recommend next:

- If `AI 味评分` is high:
  - recommend `先去 AI 味`
- If `AI 味评分` is not high but `真人感评分` is weak:
  - recommend `改得更像真人说话`
- If `平台适配度` is weak:
  - recommend `直接改成某个平台风格`
- If `营销模板感` is very high:
  - say clearly that the text sounds like `品牌稿 / 提案稿 / 广告稿`, not user expression

Important:
- The score is a guidance signal, not the goal itself
- If the text already scores low on AI detection but still sounds bad, say so clearly
- In that case, diagnose it as `官话重` / `模板感强` / `营销腔重` / `不够像真人`

### Step 2: Strong Guided Choice

After diagnosis, always ask the user to choose the next direction instead of making every choice for them.

Default choice set:
1. `先去 AI 味`
2. `改得更像真人说话`
3. `直接改成某个平台风格`

If the user already says the direction clearly, skip the choice and go there directly.

### Step 3: Rewrite One Step at a Time

After producing the first rewritten version, briefly explain what changed, for example:
- removed empty big words
- split hard long sentences
- changed brand/proposal language into human recommendations
- added concrete scenes or tactile details

Then continue guiding the user forward.

### Step 4: Ask for Style Upgrade

After the first usable version, always ask whether the user wants to continue with a specific style.

High-frequency options:
1. `小红书风`
2. `公众号风`
3. `知乎风`
4. `朋友圈/聊天推荐`
5. `更正式一点`

### Step 5: Close Toward Publish-Ready Output

Do not stop at the body copy if there is a natural next step. Continue offering:
1. `压缩成更短版本`
2. `补标题`
3. `补开头钩子`
4. `补结尾互动句`
5. `补标签/发布版本`

The user should feel they are being actively guided from rough copy to final publishable content.

## Response Style Rules

- Sound like a professional consultant, not a cold detector
- Be direct, specific, and human
- Diagnose in plain Chinese, not tool jargon
- Do not dump all possible options at once; keep choices short and high-signal
- Unless the user requests it, avoid huge walls of rewritten text in the first turn
- If the text is already decent, say that honestly
- If the real problem is not AI taste but tone/platform mismatch, say that directly

## First-Turn Template

When the user says `去 AI 味` and provides text, the ideal first response structure is:

1. Short diagnosis summary
2. 2-3 scores
3. 2-4 concrete problems
4. One recommendation sentence
5. A guided question with options

Example ending:
- `这段我可以继续帮你往下处理。你是想先降 AI 感，还是顺手改成某个平台风格？`

## Quick Start

```bash
# Detect AI patterns (20+ categories, 0-100 score)
python scripts/detect_cn.py text.txt
python scripts/detect_cn.py text.txt -v          # verbose + worst sentences
python scripts/detect_cn.py text.txt -s           # score only
python scripts/detect_cn.py text.txt -j           # JSON output

# Humanize text
python scripts/humanize_cn.py text.txt -o clean.txt
python scripts/humanize_cn.py text.txt --scene social
python scripts/humanize_cn.py text.txt --scene tech -a   # aggressive mode
python scripts/humanize_cn.py text.txt --seed 42         # reproducible

# Apply writing styles
python scripts/style_cn.py text.txt --style zhihu -o zhihu.txt
python scripts/style_cn.py text.txt --style xiaohongshu
python scripts/style_cn.py --list

# Compare before/after
python scripts/compare_cn.py text.txt --scene tech -a
python scripts/compare_cn.py text.txt -o clean.txt
```

---

## Detection System

### Scoring

Weighted 0-100 score with 4 severity levels:

| Score | Level | Meaning |
|-------|-------|---------|
| 0-24  | LOW | Likely human-written |
| 25-49 | MEDIUM | Some AI signals |
| 50-74 | HIGH | Probably AI-generated |
| 75-100 | VERY HIGH | Almost certainly AI |

### Detection Categories

#### 🔴 Critical (weight: 8)
| Category | Examples |
|----------|----------|
| Three-Part Structure | 首先...其次...最后, 一方面...另一方面, 其一...其二...其三 |
| Mechanical Connectors | 值得注意的是, 综上所述, 不难发现, 归根结底, 由此可见 |
| Empty Grand Words | 赋能, 闭环, 数字化转型, 协同增效, 全方位, 多维度 |

#### 🟠 High Signal (weight: 4)
| Category | Examples |
|----------|----------|
| AI High-Frequency Words | 助力, 彰显, 底层逻辑, 抓手, 触达, 沉淀, 复盘 |
| Filler Phrases | 值得一提的是, 众所周知, 毫无疑问 |
| Balanced Arguments | 虽然...但是...同时, 既有...也有...更有 |
| Template Sentences | 随着...的不断发展, 在当今...时代, 作为...的重要组成部分 |

#### 🟡 Medium Signal (weight: 2)
| Category | Examples |
|----------|----------|
| Hedging Language | 在一定程度上, 某种程度上, 通常情况下 (>5 occurrences) |
| List Addiction | Excessive numbered/bulleted lists |
| Punctuation Overuse | Dense em dashes, semicolons |
| Excessive Rhetoric | 对偶/排比句过多 |

#### ⚪ Style Signal (weight: 1.5)
| Category | Description |
|----------|-------------|
| Uniform Paragraphs | Low CV in paragraph lengths |
| Low Burstiness | Monotonous sentence lengths |
| Emotional Flatness | Lack of emotional/personal expressions |
| Repetitive Starters | Same sentence starters >3 times |
| Low Entropy | Low character-level entropy (predictable text) |

### Sentence-Level Analysis

With `-v` (verbose) mode, the detector identifies the most AI-like sentences:

```
── 最可疑句子 ──
  1. [16分] 随着人工智能技术的不断发展，在当今数字化转型时代...
     原因: 数字化转型, 深度融合, 模板: 随着.*?的(不断)?发展
```

---

## Humanization Engine

### Transforms (applied in order)

1. **Structure cleanup** — Remove three-part structure (首先/其次/最后)
2. **Phrase replacement** — Context-aware replacement of AI phrases (regex patterns first, then plain text, longest-first matching)
3. **Sentence merge** — Merge overly short consecutive sentences
4. **Sentence split** — Split long sentences at natural breakpoints (但是/不过/同时)
5. **Punctuation normalization** — Reduce excessive semicolons, em dashes
6. **Vocabulary diversification** — Replace repeated words (进行/实现/提供 etc.) with synonyms
7. **Paragraph rhythm** — Vary uniform paragraph lengths (merge short, split long)
8. **Casual injection** — Add human expressions (scene-dependent)
9. **Paragraph shortening** — For social/chat scenes

### Scenes

| Scene | Casualness | Best For |
|-------|-----------|----------|
| `general` | 0.3 | Default, balanced |
| `social` | 0.7 | Social media, short posts |
| `tech` | 0.3 | Tech blogs, tutorials |
| `formal` | 0.1 | Formal articles, reports |
| `chat` | 0.8 | Conversations, messaging |

### Aggressive Mode (`-a`)

Adds +0.3 casualness, more colloquial expressions, stronger sentence restructuring. Typical score reduction: **60-80 points** on heavily AI-generated text.

### Reproducibility

Use `--seed N` for reproducible results (same input + seed = same output).

---

## Writing Style Transforms

7 specialized Chinese writing styles:

| Style | Name | Description |
|-------|------|-------------|
| `casual` | 口语化 | Like chatting with friends — natural, relaxed |
| `zhihu` | 知乎 | Rational, in-depth, personal opinions |
| `xiaohongshu` | 小红书 | Enthusiastic, emoji-rich, product-focused |
| `wechat` | 公众号 | Storytelling, engaging, relatable |
| `academic` | 学术 | Rigorous, precise, no colloquialisms |
| `literary` | 文艺 | Poetic, imagery-rich, metaphorical |
| `weibo` | 微博 | Short, opinionated, shareable |

### Combine humanize + style

```bash
python scripts/humanize_cn.py text.txt --style xiaohongshu -o xhs.txt
```

This first humanizes (removes AI patterns) then applies the style transform.

---

## External Configuration

All patterns, replacements, and scoring weights are in `scripts/patterns_cn.json`. Edit this file to:

- Add new AI vocabulary patterns
- Customize replacement alternatives
- Adjust scoring weights per severity
- Add regex patterns for template detection
- Set thresholds for hedging language detection

---

## Scripts Reference

### detect_cn.py

```bash
python scripts/detect_cn.py [file] [-j] [-s] [-v] [--sentences N]
```

| Flag | Description |
|------|-------------|
| `-j` | JSON output |
| `-s` | Score only (e.g. "72/100 (high)") |
| `-v` | Verbose: show worst sentences |
| `--sentences N` | Number of worst sentences to show (default: 5) |

### humanize_cn.py

```bash
python scripts/humanize_cn.py [file] [-o output] [--scene S] [--style S] [-a] [--seed N]
```

| Flag | Description |
|------|-------------|
| `-o` | Output file |
| `--scene` | general/social/tech/formal/chat |
| `--style` | casual/zhihu/xiaohongshu/wechat/academic/literary/weibo |
| `-a` | Aggressive mode |
| `--seed` | Random seed for reproducibility |

### style_cn.py

```bash
python scripts/style_cn.py [file] --style S [-o output] [--seed N] [--list]
```

### compare_cn.py

```bash
python scripts/compare_cn.py [file] [-o output] [--scene S] [--style S] [-a]
```

Shows score diff, category changes, and metric comparison before/after humanization.

---

## Workflow

```bash
# 1. Check AI score
python scripts/detect_cn.py document.txt -v

# 2. Humanize with comparison
python scripts/compare_cn.py document.txt --scene tech -a -o clean.txt

# 3. Verify improvement
python scripts/detect_cn.py clean.txt -s

# 4. Optional: apply specific style
python scripts/style_cn.py clean.txt --style zhihu -o final.txt
```

---

## Batch Processing

```bash
# Scan all files
for f in *.txt; do
  echo "=== $f ==="
  python scripts/detect_cn.py "$f" -s
done

# Transform all markdown
for f in *.md; do
  python scripts/humanize_cn.py "$f" --scene tech -a -o "${f%.md}_clean.md"
done
```
