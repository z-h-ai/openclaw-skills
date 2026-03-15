---
name: openclaw-heartbeat-builder
description: A specialized workflow for collecting user information through a structured Q&A process to generate a customized HEARTBEAT.md configuration file for OpenClaw AI agents. Designed for business owners to define their digital employee's automated scheduled tasks and patrol routines.
---

# OpenClaw HEARTBEAT Builder: 自动巡检闹钟定制向导

This skill guides you through a structured interview process with the user (typically a business owner or manager) to collect the necessary information for generating a highly personalized `HEARTBEAT.md` file for their OpenClaw AI agent.

## Core Philosophy

As detailed in the OpenClaw documentation, `HEARTBEAT.md` is the agent's **"Alarm Clock & Patrol Checklist" (闹钟与巡检清单)**. It defines what the agent should proactively do when it "wakes up" on its own schedule (default is every 30 minutes).

A good `HEARTBEAT.md` turns a passive chatbot into a proactive digital employee that manages workflows, monitors communications, and anticipates needs.

## Workflow: The "Patrol Checklist" Interview Process

When triggered, execute the following steps sequentially. 

**CRITICAL RULES FOR ASKING QUESTIONS:**
1. **Ask ONE question at a time.** Never ask multiple questions in a single message.
2. **Wait for the user's response** before proceeding to the next question.
3. **Provide Examples/Options:** Always provide concrete business scenarios as examples.
4. **Validate the answer:** If the user's answer is too vague, you MUST ask a follow-up question to clarify.

### Step 0: Context & Baseline Check
Before asking questions, set the stage and check for existing files.
**Message to send:**
"欢迎来到『龙虾自动巡检配置中心』！⏰

之前我们给龙虾注入了灵魂（SOUL.md），也定好了岗位规矩（AGENTS.md）。现在，我们要给它定一个**『自动巡检闹钟』（HEARTBEAT.md）**。
普通 AI 是『你踢一脚它动一下』，但有了这个闹钟，龙虾就能每隔 30 分钟自己醒来，帮您巡视业务、主动汇报。

在开始之前，请问您目前是否已经有一份 `HEARTBEAT.md` 文件？
- **有** → 请发给我，我帮您看看还有哪些场景可以加上。
- **没有** → 我们从零开始，分 3 步帮它列好巡检清单。"

- **If user provides a file:** Analyze it and suggest new scenarios based on common business needs.
- **If user does not have a file:** Proceed to Step 1.

### Step 1: Communication & Message Monitoring (沟通与消息巡检)
**Action:** Define what communications the agent should monitor.
**Message to send:**
"第一步，我们来设置**消息巡检**。
老板每天最怕的就是漏掉重要信息。当龙虾每 30 分钟醒来时，您最希望它帮您盯住哪些渠道？（可多选或补充）

A. **盯客户**：检查有没有新的客户邮件/消息，有的话立刻通知我
B. **盯进度**：检查团队群聊，把大家讨论的结论和进度整理成一句话发给我
C. **盯异常**：扫描系统告警或客诉渠道，发现带『退款』『投诉』等字眼的消息，拉响最高级别警报
D. **其他业务专属渠道**：（比如：盯某个特定供应商的回复，请补充）"

*(Wait for user response, validate, then proceed to Step 2)*

### Step 2: Schedule & Task Management (日程与任务管理)
**Action:** Define how the agent should manage time and tasks.
**Message to send:**
"第二步，**日程与任务管理**。
除了盯消息，龙虾还能当您的贴身秘书。在时间管理上，您需要它帮您做什么？（可多选或补充）

A. **会前预警**：每次心跳检查日历，如果有 30 分钟内要开始的重要会议，提前把相关资料（如对方背景、上次会议纪要）发给我
B. **晨间简报**：每天早上 8:30 醒来时，生成今天的日程摘要和核心待办
C. **晚间复盘**：每天下午 5:30 醒来时，检查今天未完成的任务，顺延到明天并提醒我
D. **其他专属习惯**：（比如：每周五下午提醒提交周报，请补充）"

*(Wait for user response, validate, then proceed to Step 3)*

### Step 3: Security Warning & Constraints (安全警告与边界)
**Action:** Crucial step to ensure the user doesn't put sensitive info in HEARTBEAT.md.
**Message to send:**
"第三步，**安全红线确认**。
`HEARTBEAT.md` 是龙虾读取最频繁的文件，也是黑客最喜欢盯的目标。
为了您的安全，我必须和您确认：**在接下来的清单里，绝对不能包含任何密码、API 密钥或真实的客户隐私数据。** 所有的操作都必须通过调用本地工具（Tools）或环境变量来完成。

您可以接受这条红线吗？（回复『确认』即可，或者您有其他顾虑？）"

*(Wait for user response. If confirmed, proceed to Step 4. If they have concerns, explain that OpenClaw uses `.env` files for secrets, not markdown files.)*

### Step 4: Draft Generation and Review
**Action:** Synthesize the collected information into a draft `HEARTBEAT.md` file.
**Format Rules for Draft:**
- Use a clear Markdown list structure.
- Group tasks logically (e.g., `## Every Heartbeat (30 mins)`, `## Daily Routine`).
- Keep descriptions actionable for the AI.

**Message to send:**
"信息收集完毕！这是为您定制的 `HEARTBEAT.md`（自动巡检清单）草稿，请您过目：

```markdown
(Insert generated HEARTBEAT.md draft here)
```

**老板，您看看这份巡检清单是否覆盖了您的核心需求？有没有需要调整的频次或增加的场景？**"

### Step 5: Finalization
Once the user approves the draft, use the `file` tool to save the final content to a file named `HEARTBEAT.md` in the current working directory, and provide the user with instructions on where to place it in their OpenClaw workspace (usually `~/.openclaw/workspace/HEARTBEAT.md` or `%USERPROFILE%\.openclaw\workspace\HEARTBEAT.md`).
