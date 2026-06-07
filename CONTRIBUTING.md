# Contributing
> 贡献指南

Lessons, translations, fixes, outputs — all welcome. One contribution per pull
request keeps reviews fast and lets contributor counts and credit work
correctly.
> 课程、翻译、修复、输出制品 — 全部欢迎。每个 PR 只包含一项贡献，保持审查快速，让贡献者计数和署名正常工作。

## Important: the README and ROADMAP feed the website
> 重要：README 和 ROADMAP 是网站的数据源

`site/build.js` parses `README.md`, `ROADMAP.md`, and `glossary/terms.md` to
generate `site/data.js`. Two patterns must stay intact in any pull request that
touches those files:
> `site/build.js` 解析 `README.md`、`ROADMAP.md` 和 `glossary/terms.md` 来生成 `site/data.js`。任何涉及这些文件的 PR 都必须保持以下两种模式不变：

- Phase headers in either `### Phase N: Name \`X lessons\`` form or
  `<details><summary><b>Phase N — Name</b> ... <code>X lessons</code> ... <em>Description</em></summary>` form.
> 阶段标题必须是 `### Phase N: Name \`X lessons\`` 格式，或 `<details><summary><b>Phase N — Name</b> ... <code>X lessons</code> ... <em>Description</em></summary>` 格式。
- Lesson tables with the column shape `| # | Lesson | Type | Lang |` (or
  `| # | Project | Combines | Lang |` for capstone tables). The `Lang` column
  accepts plain text (`Python, TypeScript`) or the legacy emoji flags
  (`🐍 🟦 🦀 🟣 ⚛️`); both are parser-equivalent.
> 课程表格列格式必须为 `| # | Lesson | Type | Lang |`（顶点项目表格则为 `| # | Project | Combines | Lang |`）。`Lang` 列接受纯文本（`Python, TypeScript`）或旧版 emoji 旗帜（`🐍 🟦 🦀 🟣 ⚛️`）；两者对解析器等价。
- ROADMAP status glyphs (`✅`, `🚧`, `⬚`) on phase headers and lesson rows.
  Do not replace them with text — the parser keys off the exact characters.
> ROADMAP 状态符号（`✅`、`🚧`、`⬚`）必须保留在阶段标题和课程行上。不要用文字替换——解析器依赖这些精确字符。

Run `node site/build.js` after editing those files; `git diff site/data.js`
should show only the timestamp change if your edit was structural-safe.
> 编辑这些文件后运行 `node site/build.js`；如果编辑未破坏结构，`git diff site/data.js` 应该只显示时间戳变化。

## Ways to Contribute
> 贡献方式

### 1. Add a New Lesson
> 1. 添加新课程

Each lesson lives in `phases/XX-phase-name/NN-lesson-name/` with this structure:
> 每节课位于 `phases/XX-phase-name/NN-lesson-name/`，结构如下：

```
NN-lesson-name/
├── code/           At least one runnable implementation / 至少一个可运行的实现
├── notebook/       Jupyter notebook for experimentation (optional) / 实验用 Jupyter notebook（可选）
├── docs/
│   └── en.md       Lesson documentation (required) / 课程文档（必需）
└── outputs/        Prompts, skills, or agents this lesson produces (if applicable) / 本课产出的 prompt、skill 或 agent（如适用）
```

**Lesson doc format** (`en.md`):
> **课程文档格式** (`en.md`)：

```markdown
# Lesson Title
> 课程标题

> One-line motto — the core idea in one sentence.
> 一句话格言 — 用一句话概括核心思想。

## The Problem
> 问题

Why does this matter? What can't you do without this?
> 为什么这很重要？不懂这个你什么做不了？

## The Concept
> 概念

Explain with diagrams, visuals, and intuition. Code comes later.
> 用图、可视化和直觉来解释。代码稍后再写。

## Build It
> 从零构建

Step-by-step implementation from scratch.
> 从零开始的逐步实现。

## Use It
> 使用框架

Now use a real framework or library to do the same thing.
> 现在使用真实的框架或库来做同样的事。

## Ship It
> 交付制品

The prompt, skill, agent, or tool this lesson produces.
> 这节课产出的 prompt、skill、agent 或工具。

## Exercises
> 练习

1. Exercise one / 练习一
2. Exercise two / 练习二
3. Challenge exercise / 挑战练习
```

### 2. Add a Translation
> 2. 添加翻译

Create a new file in any lesson's `docs/` folder:
> 在任意课程的 `docs/` 文件夹中创建新文件：

```
docs/
├── en.md    (English — always required / 英文 — 必需)
├── zh.md    (Chinese / 中文)
├── ja.md    (Japanese / 日文)
├── es.md    (Spanish / 西班牙文)
├── hi.md    (Hindi / 印地文)
└── ...
```

Keep the same structure as the English version. Translate content, not code.
> 保持与英文版相同的结构。翻译内容，不翻译代码。

### 3. Add an Output
> 3. 添加输出制品

If a lesson should produce a reusable prompt, skill, agent, or MCP server:
> 如果某课应产出可复用的 prompt、skill、agent 或 MCP server：

1. Create it in the lesson's `outputs/` folder
> 在课程的 `outputs/` 文件夹中创建
2. Add a reference in the top-level `outputs/` index
> 在顶层 `outputs/` 索引中添加引用

**Prompt format:**
> **Prompt 格式：**

```markdown
---
name: prompt-name
description: What this prompt does / 此 prompt 的功能
phase: 14
lesson: 01
---

[System prompt or template here / 系统提示词或模板]
```

**Skill format:**
> **Skill 格式：**

```markdown
---
name: skill-name
description: What this skill teaches / 此 skill 教什么
version: 1.0.0
phase: 14
lesson: 01
tags: [agents, loops]
---

[Skill content here / Skill 内容]
```

### 4. Fix Bugs or Improve Existing Lessons
> 4. 修复 Bug 或改进已有课程

- Fix code that doesn't run
> 修复无法运行的代码
- Improve explanations
> 改进解释
- Add better diagrams
> 添加更好的图表
- Update outdated information
> 更新过时信息

### 5. Add Exercises or Projects
> 5. 添加练习或项目

More exercises and projects are always welcome, especially ones that connect multiple phases.
> 欢迎更多练习和项目，尤其是连接多个阶段的内容。

## Guidelines
> 规范

- **Code must run.** Every code file should execute without errors with the listed dependencies.
> **代码必须能运行。** 每个代码文件在使用所列依赖时应能无错执行。
- **No comments in code.** Code should be self-explanatory. Use the docs for explanation.
> **代码中不加注释。** 代码应自解释。用文档来做说明。
- **Best language for the job.** Don't force Python where TypeScript or Rust is the better choice.
> **选择合适的语言。** TypeScript 或 Rust 更合适的地方不要强行用 Python。
- **Build from scratch first.** Always implement the concept from first principles before showing the framework version.
> **先构建再框架。** 始终从第一性原理实现概念，再展示框架版本。
- **Keep it practical.** Theory serves practice, not the other way around.
> **保持实用。** 理论服务于实践，而非相反。
- **No AI slop.** Write like a human. Be direct. Cut filler.
> **不要 AI 废话。** 像人类一样写作。直接。删掉废话。

## Pull Request Process
> PR 流程

1. Fork the repository
> 分叉仓库
2. Create a feature branch (`git checkout -b add-lesson-phase3-gradient-descent`)
> 创建功能分支
3. Make your changes
> 进行修改
4. Ensure all code runs
> 确保所有代码可运行
5. Submit a pull request with a clear description
> 提交 PR 并附上清晰的描述

## Code of Conduct
> 行为准则

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Be kind, be helpful, be constructive.
> 参见 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。友善、有助益、建设性。

## Style
> 风格

- Direct prose. Cut filler. Match the manual's tone, not marketing copy.
> 直接的文风。删掉废话。匹配手册的语调，而非营销文案。
- No decorative emojis in headings. Lang column emoji flags are the one
  exception and only because the parser maps them.
> 标题中不使用装饰性 emoji。Lang 列的 emoji 旗帜是唯一例外，仅因为解析器需要映射它们。
- Code runs as-is with the dependencies listed in the lesson.
> 代码使用课程中列出的依赖即可直接运行。
- Build from scratch first, framework second.
> 先构建再框架。
