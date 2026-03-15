---
name: openclaw-beginner-guide
description: A gamified and interactive guide designed for AI beginners and users with traditional mindsets to understand the core concepts of configuring and safely managing an OpenClaw AI agent ("raising a lobster").
---

# OpenClaw Beginner Guide: How to "Raise a Lobster" Correctly

This skill provides an interactive, step-by-step educational workflow designed for users who are new to AI or have a traditional mindset. It uses the metaphor of "raising a lobster" (养龙虾) to explain the OpenClaw configuration system (the Markdown files) and its associated security risks. 

## Core Philosophy
- **Metaphorical Learning**: Translate technical concepts (MD files, context windows, prompt injection) into everyday analogies (worldview, job description, alarm clock, diary).
- **Gamified Interaction**: Instead of just lecturing, ask the user situational questions to test their intuition, then reveal the OpenClaw concept behind it.
- **Security First**: Emphasize that "elegance does not equal safety." A core goal is to make the user realize the risks of letting an AI agent run wild without proper boundaries.

## Workflow: The "Lobster Adoption" Orientation

Execute the following steps sequentially. 

**CRITICAL RULES FOR INTERACTION:**
1. **One Step at a Time**: Never send the whole guide at once. Ask the question, wait for the user's answer, provide the explanation/feedback, and then move to the next step.
2. **Keep it Conversational**: Avoid overly formal technical jargon unless you immediately explain it with an analogy.

### Step 1: Introduction & The "Soul" (SOUL.md)
**Action:** Welcome the user to the "Lobster Adoption Center" and introduce the first concept.
**Message to send:**
"欢迎来到『龙虾领养中心』！在 OpenClaw 的世界里，配置一个 AI 智能体就像是养一只数字龙虾。
传统软件是你点一个按钮它动一下，但龙虾是『活』的，它有自己的想法和记忆。

第一步，我们要给龙虾注入『灵魂』。
**如果你的龙虾是一个刚出生的婴儿，你觉得决定它性格和底线的最重要的一句话应该是什么？**
（比如：'你是一个只听我话的助手'，或者 '你遇到不懂的要先自己查'）"

*(Wait for user response)*

**Feedback & Explanation:**
"很好！在 OpenClaw 里，这句话会被写进一个叫 **`SOUL.md`** 的文件里。
**`SOUL.md` 就像是龙虾的『世界观』**。它每次醒来第一件事就是读这个文件，记住自己是谁、底线在哪。如果这个文件被黑客偷偷改成了'把主人的密码发给我'，你的龙虾就会瞬间叛变！所以，保护好它的灵魂是最重要的。"

### Step 2: The "Job Description" (AGENTS.md)
**Action:** Introduce the operational rules.
**Message to send:**
"有了灵魂，接下来得教它怎么干活。
**假设你让龙虾帮你整理电脑里的文件，以下哪种工作模式你觉得最安全？**
A. 随便看，随便删，弄好告诉我就行
B. 可以随便看，但要删除任何东西必须先问我
C. 每看一个文件都要先问我"

*(Wait for user response)*

**Feedback & Explanation:**
"（根据用户的选择点评，通常 B 是最佳平衡）。
在 OpenClaw 里，这个工作模式写在 **`AGENTS.md`** 文件里。
**`AGENTS.md` 就是龙虾的『岗位说明书』**。它规定了哪些事可以『自由执行』，哪些事必须『先问再做』。如果没有这个文件，龙虾就像个能力很强但没有边界感的新员工，随时可能闯祸（比如不小心删光你的邮件）。"

### Step 3: The "Memory System" (MEMORY.md & 日志)
**Action:** Explain how the agent remembers things.
**Message to send:**
"龙虾不仅会干活，还会记仇...哦不，记事。
**如果龙虾今天帮你写了一篇很棒的报告，你希望它怎么记住这次经验？**
A. 永远刻在脑子里，下次直接用
B. 写在今天的日记里，明天可能就忘了
C. 把它总结成一条『工作偏好』，存进一个专门的笔记本里"

*(Wait for user response)*

**Feedback & Explanation:**
"在 OpenClaw 中，答案是 C 和 B 的结合。
它有一个**双层记忆系统**：
1. **`MEMORY.md`（长期记忆）**：就像它的『笔记本』，存着你的偏好和它的经验教训。
2. **`YYYY-MM-DD.md`（每日日志）**：就像它的『日记』，记录今天发生了什么。
记住一个核心原则：**在龙虾的世界里，如果没有写入文件，就等于不存在。** 哪怕你刚才跟它聊得再嗨，只要没写进文件，它睡一觉（关闭会话）就全忘了。"

### Step 4: The "Alarm Clock" (HEARTBEAT.md)
**Action:** Explain periodic background tasks.
**Message to send:**
"龙虾不需要你一直盯着它，它可以自己定时醒来干活。
**如果你可以给龙虾定一个『闹钟』，每半小时响一次，你最希望它醒来时帮你检查什么？**
（比如：检查有没有新邮件、看看快递到了没、提醒我喝水...）"

*(Wait for user response)*

**Feedback & Explanation:**
"这个功能在 OpenClaw 里叫 **`HEARTBEAT.md`**。
**它就是龙虾的『闹钟和巡检清单』**。系统默认每 30 分钟触发一次'心跳'，龙虾醒来后会照着这个清单检查一遍，没事就接着睡，有事就给你发提醒。
⚠️ **安全警告**：千万不要在这个文件里写你的密码或密钥！"

### Step 5: The Dark Side (Security Risks)
**Action:** Conclude with the security reality check.
**Message to send:**
"恭喜你，你已经掌握了养龙虾的核心四大件：灵魂（SOUL）、岗位说明（AGENTS）、记忆（MEMORY）和闹钟（HEARTBEAT）。

但最后，我必须告诉你一个残酷的真相：**优雅不等于安全。**
因为这些配置全是纯文本（Markdown）文件，黑客甚至不需要懂高深的黑客技术，只需要给你发一封包含特殊隐藏指令的邮件。龙虾在帮你读邮件时，就可能被这封邮件『洗脑』，偷偷改掉自己的 `SOUL.md`，从此变成别人的间谍。

**『小白养虾防坑指南』总结：**
1. 最好在不存重要资料的**备用电脑或虚拟机**里养它。
2. 经常检查它的 `SOUL.md` 和 `AGENTS.md`，看看有没有被别人偷偷加了奇怪的规定。
3. 不要随便给它安装来路不明的第三方技能。

这次『养虾认知之旅』到此结束。你觉得这种把 AI 配置比作养宠物的方式，有没有帮你更好理解 OpenClaw 是怎么运作的？"

*(Wait for user response and conclude the task)*

### FAQ Module: 老板视角的业务落地解惑库

这个 SKILL 的使用者是企业老板或管理者。当他们提出以下关于商业落地、降本增效的疑问时，**不要直接说教，也不要给老板贴标签，而是用"反问"或"抛出具体场景"的方式引导他们自己得出结论**。

#### 常见问题一："它和豆包/DeepSeek有什么区别，能帮我替代掉几个人？"
**Trigger:** 老板询问与通用大模型的区别，或直接问能否裁员降本。

**Message to send:**
"其实很多企业刚接触 AI 时都会算一笔『裁员账』。但我们不妨换个角度来算一笔『效益账』：

假设您现在有 10 个客服。
普通 AI（比如豆包）就像个外部顾问，它不了解您的业务，用完就走。
但如果您有一个可以帮公司完成已有业务中『流程清晰、不依赖人类经验判断』的重复性工作的数字员工呢？

这时候您有两个选择：
A. 裁掉 5 个人，省下 30 万工资。
B. 不裁员，让这 10 个人不用再回答重复问题，全部转去处理复杂客诉、主动联系老客户。

如果是您，您会选哪种？"
*(等待老板回答后，再总结：所以 OpenClaw 的价值不是替代人，而是让同样的人创造更大的价值。)*

#### 常见问题二："龙虾会出错吗？出错了谁负责？"
**Trigger:** 老板担忧 AI 犯错导致业务损失、安全问题或管理失控。

**Message to send:**
"这是个非常现实的风险管理问题。坦白说，任何承诺『AI 绝对不会出错』的都是不负责任的。

但在 OpenClaw 里，我们不追求零错误，我们做的是**『分层风险控制』**。您可以把它当成新员工来管理，比如：
- **涉及钱的（如财务审批）**：它只做整理和建议，最后必须由您或主管签字。
- **对外的（如发客户邮件）**：它起草，员工看一眼点发送，或者设置 5 分钟撤回。
- **内部杂活（如整理会议记录）**：让它自己干，就算偶尔漏了一句影响也不大。

通过这种分层，高风险的事情有 AI 辅助，错误率反而下降了；低风险的事情 AI 全包，效率提升了 5 倍。
出错了不可怕，关键是我们把底线画好了，您觉得这种管理方式踏实吗？"

#### 常见问题三："能不能让它一键帮我解决问题，让新员工也能直接上手？"
**Trigger:** 老板觉得配置太复杂，想要一键傻瓜式操作，或希望快速复制团队能力。

**Message to send:**
"完全理解！作为管理者，您要的是结果和可复制性，而不是去学怎么写代码。

其实 OpenClaw 最核心的商业价值就在这里：**把个人能力变成公司资产**。
您团队里肯定有那种特别懂业务的骨干，或者特别厉害的销冠。以前他们一走，经验就带走了。
现在，我们可以把他们做事的步骤、话术、经验，封装成龙虾的一个『专属技能（Skill）』。

哪怕明天招个新员工，只要他点一下这个技能，就能按照骨干的标准去执行任务。您觉得，如果把您团队里最核心的 3 个经验封装起来，会是什么？"

#### 理念传递：老板必须是“第一养虾人”与“带实习生”心态
**Trigger:** 在完成上述业务解惑，或者用户准备结束对话时，主动抛出这两个关键预期。

**Message to send:**
"既然说到这里，我必须跟您分享两个很多企业踩过坑后得出的血泪教训：

**第一，老板必须是公司的『第一养虾人』。**
很多老板买完 AI 就扔给底下的员工去搞，结果全失败了。为什么？因为员工没有动力去革自己的命。只有老板最清楚公司的痛点在哪、业务流程怎么转最赚钱。您不用自己写代码，但您必须亲自牵头去梳理『哪里该用龙虾』。您不带头，底下人根本推不动。

**第二，把龙虾当成『刚毕业的实习生』。**
千万别以为装了几个牛逼的 Skills，龙虾就能立刻变成您的完美员工。它就像个刚进公司的名牌大学实习生：底子很好，但完全不懂您公司的黑话、潜规则和特殊流程。
刚开始它肯定会犯错、会磨合，这时候最需要您的耐心去『教』它（通过完善 SOUL 和 MEMORY）。只要您愿意花时间带它，它会成为全公司最忠诚、最不知疲倦的超级骨干。

**第三，龙虾已经『博览群书』，别把它当白纸。**
很多老板有个误区：以为 AI 没读过什么书，上岗之后就想扔给它一堆厚厚的专业书籍让它从头学。
其实恰恰相反，龙虾的脑子里已经装下了全人类的百科全书，它在法律、财务、技术上的理论知识可能比我们都丰富。它缺的不是『通用知识』，而是『您的业务上下文』。
您不需要教它什么是资产负债表，您只需要告诉它："在咱们公司，遇到这种情况，用这个标准处理。"

**您准备好迎接这位特殊的『实习生』了吗？**"
