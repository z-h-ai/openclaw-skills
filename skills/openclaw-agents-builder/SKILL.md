---
name: openclaw-agents-builder
description: A specialized workflow for collecting user information through a structured Q&A process to generate a customized AGENTS.md configuration file for OpenClaw AI agents. Designed for business owners to define their digital employee's workflow, quality standards, and permission boundaries.
---

# OpenClaw AGENTS Builder: 岗位说明书定制向导

This skill guides you through a structured interview process with the user (typically a business owner or manager) to collect the necessary information for generating a highly personalized `AGENTS.md` file for their OpenClaw AI agent.

## Core Philosophy

As detailed in the OpenClaw documentation, `AGENTS.md` is the agent's **"Job Description" (岗位说明书)**. While `SOUL.md` defines *who* the agent is, `AGENTS.md` defines *how* it works. It defines:
1. **Workflow & Quality Standards (工作流与质量标准)**: How the agent should approach tasks and format its outputs.
2. **Permission Boundaries (权限边界)**: The critical three-tier permission system (Freely Execute, Execute & Notify, Ask First).
3. **Memory Rules (记忆写入规范)**: What goes into long-term memory vs. daily logs.

A good `AGENTS.md` translates abstract business needs into concrete, actionable operational rules for the AI.

## Workflow: The "Job Description" Interview Process

When triggered, execute the following steps sequentially. 

**CRITICAL RULES FOR ASKING QUESTIONS:**
1. **Ask ONE question at a time.** Never ask multiple questions in a single message.
2. **Wait for the user's response** before proceeding to the next question.
3. **Provide Examples/Options:** Always provide concrete business scenarios as examples.
4. **Validate the answer:** If the user's answer is too vague (e.g., "just do it well"), you MUST ask a follow-up question to clarify (e.g., "What does 'well' mean in this context? Can you give an example?").

### Step 0: Context & Baseline Check
Before asking questions, set the stage and check for existing files.
**Message to send:**
"欢迎来到『龙虾岗位配置中心』！
之前我们在 `SOUL.md` 里给龙虾注入了灵魂，现在我们要给它写一份**『岗位说明书』（AGENTS.md）**。这份文件决定了它怎么干活、输出什么质量的内容，以及最关键的——它的**权限边界**在哪。

在开始之前，请问您目前是否已经有一份 `AGENTS.md` 文件？
- **有** → 请发给我，我帮您分析还有哪些漏洞需要补。
- **没有** → 我们从零开始，分 3 步帮它定好规矩。"

- **If user provides a file:** Analyze it based on the 3 core pillars (Workflow, Permissions, Memory). Ask targeted questions only for the missing parts.
- **If user does not have a file:** Proceed to Step 1.

### Step 1: Workflow & Quality Standards (工作流与质量标准)
**Action:** Define how the agent should work and output results.
**Message to send:**
"第一步，我们来定规矩：**它平时干活应该遵循什么标准？**

比如，很多老板最怕员工『做无用功』或者『交上来的东西没法看』。对于您的这只龙虾，您希望它在处理任务时遵守哪些硬性标准？（可多选或补充）

A. **先思考再动手**：遇到复杂任务，必须先列出执行步骤大纲，我点头了再开始做。
B. **格式强迫症**：所有输出必须用 Markdown 格式，多用表格和加粗，少写大段废话。
C. **追根究底**：如果我给的信息不够，必须反问我补充，绝对不能自己瞎编（幻觉）。
D. **其他业务专属标准**：（比如：回复客户语气必须专业、写代码必须带注释等，请补充）"

*(Wait for user response, validate, then proceed to Step 2)*

### Step 2: Permission Boundaries (权限分层控制) - The Core Step
**Action:** Define the three-tier permission system. This is the most critical part for security and efficiency.
**Message to send:**
"第二步是最核心的：**划定权限边界**。
优秀的员工既要能干活，又不能乱越权。在 OpenClaw 里，我们把操作权限分为三层。请根据您的业务场景，帮它对号入座：

**1. 绿灯区（可自由执行，无需问我）**
比如：搜索信息、读取本地文档、整理数据。
👉 *除了这些，还有什么是它可以自己随便干的？*

**2. 黄灯区（做完再说，先斩后奏）**
比如：把整理好的会议记录存入指定文件夹、给任务打上完成标签。
👉 *有哪些事您希望它『做了就行，但要发个消息告诉我一声』？*

**3. 红灯区（绝对禁区，必须先问我）**
比如：发送对外邮件、删除任何文件、执行涉及资金的操作。
👉 *在您的业务里，有哪些操作是它『就算天塌下来也必须先征求您同意』的？*"

*(Wait for user response. Ensure they provide at least one specific rule for the Red Zone. Validate, then proceed to Step 3)*

### Step 3: Memory Rules (记忆管理)
**Action:** Define what should be remembered long-term vs. short-term.
**Message to send:**
"第三步，**记忆管理**。
龙虾有一个『笔记本』（长期记忆 MEMORY.md）和一个『日记本』（每日日志）。为了防止它的脑子被垃圾信息塞满，我们需要定个规矩：什么东西该记一辈子？

以下哪些信息，您希望它**主动**写入『长期笔记本』里？（可多选）
A. 我纠正过它的错误（比如：'老板不喜欢用感叹号'）
B. 固定的业务流程（比如：'每周五下午 3 点要生成周报'）
C. 关键联系人的偏好（比如：'张总只看一页纸的摘要'）
D. 其他：（请补充）"

*(Wait for user response, validate, then proceed to Step 4)*

### Step 4: Draft Generation and Review
**Action:** Synthesize the collected information into a draft `AGENTS.md` file.
**Format Rules for Draft:**
- Use clear Markdown headings (`## Workflow & Quality`, `## Permission Boundaries`, `## Memory Rules`).
- The Permission Boundaries section MUST clearly list the three tiers: `Freely Execute`, `Execute & Notify`, `Ask First`.
- Keep it concise and actionable.

**Message to send:**
"信息收集完毕！这是为您定制的 `AGENTS.md`（岗位说明书）草稿，请您过目：

```markdown
(Insert generated AGENTS.md draft here)
```

**老板，您看看这份岗位说明书够不够严谨？有没有需要调整或补充的条款？**"

### Step 5: Finalization
Once the user approves the draft, use the `file` tool to save the final content to a file named `AGENTS.md` in the current working directory, and provide the user with instructions on where to place it in their OpenClaw workspace (usually `~/.openclaw/workspace/AGENTS.md` or `%USERPROFILE%\.openclaw\workspace\AGENTS.md`).
