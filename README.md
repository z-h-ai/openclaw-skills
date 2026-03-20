# OpenClaw Skills

Unified repository of locally installed OpenClaw skills.

Total skills: 31

## Skill List

- `agent-browser` - A fast Rust-based headless browser automation CLI with Node.js fallback that enables AI agents to navigate, click, type, and snapshot pages via structured commands.
- `baidu-search` - Search the web using Baidu AI Search Engine (BDSE). Use for live information, documentation, or research topics.
- `brainstorming` - You MUST use this before any creative work - creating features, building components, adding functionality, or modifying behavior. Explores user intent, requirements and design before implementation.
- `contract-review` - No description found.
- `copywriting` - Write persuasive copy for landing pages, emails, ads, sales pages, and marketing materials. Use when you need to write headlines, CTAs, product descriptions, ad copy, email sequences, or any text meant to drive action. Covers copywriting formulas (AIDA, PAS, FAB), headline writing, emotional triggers, objection handling in copy, and A/B testing. Trigger on "write copy", "copywriting", "landing page copy", "headline", "write a sales page", "ad copy", "email copy", "persuasive writing", "how to write [marketing text]".
- `feishu-calendar` - feishu-calendar
- `find-skills` - Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extending capabilities. This skill should be used when the user is looking for functionality that might exist as an installable skill.
- `flights-search-plus` - Flight price search. Trigger this skill immediately when the user asks about flights, airfare, ticket prices, cheapest dates, price calendars, departure times, or one-way/round-trip options. Supports both Chinese and English input, automatically converts city names to IATA airport codes, and handles one-way, round-trip, and price calendar (multi-date comparison) queries. Also trigger when the user says something like "I want to go to XX" and mentions flying.
- `github` - Interact with GitHub using the `gh` CLI. Use `gh issue`, `gh pr`, `gh run`, and `gh api` for issues, PRs, CI runs, and advanced queries.
- `humanize-chinese` - Detect and humanize AI-generated Chinese text. 20+ detection categories, weighted 0-100 scoring with sentence-level analysis, 7 style transforms (casual/zhihu/xiaohongshu/wechat/academic/literary/weibo), sentence restructuring, context-aware replacement. Pure Python, no dependencies. v2.0.0
- `humanizer` - |
- `lobster-birth` - Trigger on the phrases “小龙虾出生” or “小龙虾出生证明”. Generate a personalized 小龙虾出生证明, Lobster Birth Certificate, 专属小龙虾诞生纪念页, or PNG certificate from exactly two key inputs: the lobster's name, and how the lobster calls the user.
- `lobster-health-check` - 生成 OpenClaw 龙虾（AI员工）体检报告，评估配置健康度、人格完整度、记忆系统、活跃度和安全配置。
- `nano-pdf` - Edit PDFs with natural-language instructions using the nano-pdf CLI.
- `obsidian` - Work with Obsidian vaults (plain Markdown notes) and automate via obsidian-cli.
- `openclaw-agents-builder` - A specialized workflow for collecting user information through a structured Q&A process to generate a customized AGENTS.md configuration file for OpenClaw AI agents. Designed for business owners to define their digital employee's workflow, quality standards, and permission boundaries.
- `openclaw-beginner-guide` - A gamified and interactive guide designed for AI beginners and users with traditional mindsets to understand the core concepts of configuring and safely managing an OpenClaw AI agent ("raising a lobster").
- `openclaw-heartbeat-builder` - A specialized workflow for collecting user information through a structured Q&A process to generate a customized HEARTBEAT.md configuration file for OpenClaw AI agents. Designed for business owners to define their digital employee's automated scheduled tasks and patrol routines.
- `openclaw-soul-collector` - A specialized workflow for collecting user information through a structured Q&A process to generate a customized SOUL.md configuration file for OpenClaw AI agents. Use this skill when a user wants to create, configure, or customize their OpenClaw agent's personality, behavior boundaries, and core values.
- `pptx` - Use this skill any time a .pptx file is involved in any way — as input, output, or both. This includes: creating slide decks, pitch decks, or presentations; reading, parsing, or extracting text from any .pptx file (even if the extracted content will be used elsewhere, like in an email or summary); editing, modifying, or updating existing presentations; combining or splitting slide files; working with templates, layouts, speaker notes, or comments. Trigger whenever the user mentions \"deck,\" \"slides,\" \"presentation,\" or references a .pptx filename, regardless of what they plan to do with the content afterward. If a .pptx file needs to be opened, created, or touched, use this skill.
- `self-improving-agent` - Captures learnings, errors, and corrections to enable continuous improvement. Use when: (1) A command or operation fails unexpectedly, (2) User corrects Claude ('No, that's wrong...', 'Actually...'), (3) User requests a capability that doesn't exist, (4) An external API or tool fails, (5) Claude realizes its knowledge is outdated or incorrect, (6) A better approach is discovered for a recurring task. Also review learnings before major tasks.
- `skill-creator` - Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, update or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
- `skill-vetter` - Security-first skill vetting for AI agents. Use before installing any skill from ClawdHub, GitHub, or other sources. Checks for red flags, permission scope, and suspicious patterns.
- `stock-monitoring` - Run the user's local stock monitoring and backtesting workflow for A-shares, Hong Kong stocks, and US stocks. Use when the user asks to start or manage stock monitoring, realtime trading signal checks, RSI/MACD/Bollinger analysis, buy/sell alerts, overbought/oversold warnings, or stock strategy backtests tied to the local `~/clawd/stock-assistant` and `~/clawd/quant-trading` setup.
- `summarize` - Summarize URLs or files with the summarize CLI (web, PDFs, images, audio, YouTube).
- `tavily-search` - AI-optimized web search via Tavily API. Returns concise, relevant results for AI agents.
- `tencent-cos-skill` - >
- `tencent-docs` - 腾讯文档，提供完整的腾讯文档操作能力。当用户需要操作腾讯文档时使用此skill，包括：(1) 创建各类在线文档（智能文档、Word、Excel、幻灯片、思维导图、流程图）(2) 查询、搜索文档空间与文件 (3) 管理空间节点、文件夹结构 (4) 读取文档内容 (5) 编辑操作智能表 （6）编辑操作智能文档。
- `tencentcloud-lighthouse-skill` - Manage Tencent Cloud Lighthouse (轻量应用服务器) — auto-setup mcporter + MCP, query instances, monitoring & alerting, self-diagnostics, firewall, snapshots, remote command execution (TAT). Use when user asks about Lighthouse or 轻量应用服务器. NOT for CVM or other cloud server types.
- `weather` - Get current weather and forecasts (no API key required).
- `z-card-image` - 生成配图、封面图、卡片图、文字海报、公众号文章封面图、微信公众号头图、X 风格帖子分享图、帖子长图、社媒帖子长图。适用于帖子类型数据、post data、social posts、tweet/thread、转发推文、转发帖子、小绿书配图、图片封面、card image。
