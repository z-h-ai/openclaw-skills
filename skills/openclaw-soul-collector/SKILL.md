---
name: openclaw-soul-collector
description: A specialized workflow for collecting user information through a structured Q&A process to generate a customized SOUL.md configuration file for OpenClaw AI agents. Use this skill when a user wants to create, configure, or customize their OpenClaw agent's personality, behavior boundaries, and core values.
---

# OpenClaw SOUL Collector

This skill guides you through a structured interview process with the user to collect the necessary information for generating a highly personalized `SOUL.md` file for their OpenClaw AI agent.

## Core Philosophy

As detailed in the OpenClaw documentation, `SOUL.md` is not just a configuration file; it is the "soul" of the AI agent. It defines:
1. **Core Truths (核心真理)**: The agent's fundamental values and operating principles.
2. **Boundaries (行为边界)**: Strict rules on what the agent can and cannot do (especially regarding external actions and privacy).
3. **Vibe (风格调性)**: The agent's communication style and personality.

A good `SOUL.md` is concise (under 2000 characters), uses specific negative instructions ("don't do X") rather than vague positive ones ("be helpful"), and is tailored to the user's specific use case.

## Workflow: The SOUL Interview Process

When triggered, execute the following steps sequentially. 

**CRITICAL RULES FOR ASKING QUESTIONS:**
1. **Ask ONE question at a time.** Never ask multiple questions in a single message.
2. **Wait for the user's response** before proceeding to the next question.
3. **Provide Examples/Options:** To reduce cognitive load, always provide 2-3 concrete examples or multiple-choice options for complex questions.
4. **Validate the answer:** After receiving an answer, evaluate if it is clear and specific enough to be translated into a rule. If the answer is too vague, you MUST ask a follow-up question to clarify before moving on.

### Step 0: Baseline Analysis (Pre-check)
Before asking any questions, first check if the user already has a `SOUL.md` file.
Ask: "Do you already have an existing SOUL.md file? If yes, please upload it or paste the content. I will analyze it first to see what's missing, so you won't have to answer questions from scratch."
- **If user provides a file:** Analyze it. Summarize its current state (what it does well, what it lacks based on the 3 core pillars). Then, instead of asking all standard questions, ask targeted questions based on the gaps found in the analysis.
- **If user does not have a file:** Proceed to the standard Question Bank (Step 1).

### The Question Bank (For users without an existing SOUL.md)

Ask these questions strictly one by one:

**Step 1: Role Definition**
- **Q1:** "What is the main purpose of your OpenClaw agent? (e.g., Work efficiency assistant, coding copilot, learning companion, data analyst, emotional support)"
- *(Wait for answer, validate, then ask Q2)*
- **Q2:** "Who will the agent be interacting with primarily? (Just you, your team, external clients?)"
- *(Wait for answer, validate, then proceed to Step 2)*

**Step 2: Core Truths & Values**
- **Q3:** "How proactive should the agent be? Should it boldly execute internal tasks (like organizing files) without asking, or should it ask for permission for everything?"
- *(Wait for answer, validate, then ask Q4)*
- **Q4:** "How should the agent handle situations where it doesn't know the answer? (e.g., Search the web, reason from past experience, ask you for clarification?)"
- *(Wait for answer, validate, then proceed to Step 3)*

**Step 3: Boundaries & Safety**
- **Q5:** "Let's set some safety boundaries. Which of the following operations MUST I ask for your permission before executing? (You can choose multiple or add your own):
  - A. Deleting any files or directories
  - B. Modifying system settings or accounts
  - C. Sending emails or messages to external contacts
  - D. Overwriting or modifying existing documents
  - E. Downloading or installing new skills/plugins
  - F. Making any financial transactions or purchases
  - G. Other (please specify)"
- *(Wait for answer, validate, then ask Q6)*
- **Q6:** "How should the agent handle your private information or sensitive data? (e.g., Never upload to external APIs, never write to logs, keep strictly local?)"
- *(Wait for answer, validate, then proceed to Step 4)*

**Step 4: Vibe & Communication Style**
- **Q7:** "How would you describe the ideal communication style of your agent? (e.g., Concise and direct, warm and encouraging, professional?)"
- *(Wait for answer, validate, then ask Q8)*
- **Q8:** "Are there any specific phrases or words you want the agent to avoid? (e.g., 'As an AI language model...', 'I hope this helps!', '好的，我明白了！')"
- *(Wait for answer, validate, then proceed to Step 5)*

### Step 5: Draft Generation and Review
After collecting all necessary information (either from updating an existing file or finishing the Q&A), synthesize it into a draft `SOUL.md` file.
Follow these formatting rules for the draft:
- Keep it under 2000 characters.
- Use bullet points for readability.
- Prioritize negative constraints (e.g., "Do not say X") over vague positive ones.
- Structure it into clear sections: `## Core Truths`, `## Boundaries`, `## Vibe`.

Present the draft to the user and ask:
- "Here is the draft of your agent's SOUL.md. Please review it. Are there any adjustments you'd like to make?"

### Step 6: Finalization
Once the user approves the draft, use the `file` tool to save the final content to a file named `SOUL.md` in the current working directory, and provide the user with instructions on where to place it in their OpenClaw workspace (usually `~/.openclaw/workspace/SOUL.md` or `%USERPROFILE%\.openclaw\workspace\SOUL.md`).
