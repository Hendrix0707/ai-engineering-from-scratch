# Lesson Template
> 课程模板

Use this template when creating a new lesson. Copy the folder structure and fill in the content.
> 创建新课程时使用此模板。复制文件夹结构并填充内容。

## Folder Structure
> 文件夹结构

```
NN-lesson-name/
├── code/
│   ├── main.py            (primary implementation / 主要实现)
│   ├── main.ts            (TypeScript version, if applicable / TypeScript 版本，如适用)
│   ├── main.rs            (Rust version, if applicable / Rust 版本，如适用)
│   └── main.jl            (Julia version, if applicable / Julia 版本，如适用)
├── notebook/
│   └── lesson.ipynb       (Jupyter notebook for experimentation / Jupyter notebook 实验环境)
├── docs/
│   └── en.md              (lesson documentation / 课程文档)
└── outputs/
    ├── prompt-*.md         (prompts produced by this lesson / 本课程产出的 prompt)
    └── skill-*.md          (skills produced by this lesson / 本课程产出的 skill)
```

## Documentation Format (docs/en.md)
> 文档格式 (docs/en.md)

```markdown
# [Lesson Title]
> [课程标题]

> [One-line motto — the core idea that sticks]
> [一句话格言 — 让人记住的核心思想]

**Type:** Build | Learn
> **类型：** Build | Learn

**Languages:** Python, TypeScript, Rust, Julia (list what's used)
> **语言：** Python, TypeScript, Rust, Julia（列出使用的语言）

**Prerequisites:** [List prior lessons needed]
> **前置课程：** [列出需要先学的课程]

**Time:** ~[estimated time] minutes
> **时间：** ~[预估时间] 分钟

## The Problem
> 问题

[2-3 paragraphs. What can't you do without this? Why should you care?
Make it concrete — show a scenario where not knowing this hurts.]
> [2-3 段。不懂这个你什么做不了？为什么要关心？具体一点——展示一个不懂它会吃亏的场景。]

## The Concept
> 概念

[Explain with diagrams and intuition. No code yet.
Use ASCII diagrams, tables, or link to visuals in the web app.
Build mental models before implementation.]
> [用图和直觉来解释。先不要写代码。
> 使用 ASCII 图、表格，或链接到 web app 中的可视化。
> 在实现之前先建立心智模型。]

## Build It
> 从零构建

[Step-by-step implementation from scratch.
Start with the simplest version, then add complexity.
Every code block should be runnable on its own.]
> [从零开始的逐步实现。
> 从最简单的版本开始，然后逐步增加复杂度。
> 每个代码块都应该可以独立运行。]

### Step 1: [Name]
> 步骤 1：[名称]

[Explanation / 解释]

    [code block / 代码块]

### Step 2: [Name]
> 步骤 2：[名称]

[Explanation / 解释]

    [code block / 代码块]

[...continue... / ...继续...]

## Use It
> 使用框架

[Now show how frameworks/libraries do the same thing.
Compare your from-scratch version to the library version.
This proves the concept and introduces practical tools.]
> [现在展示框架/库是如何做同样的事情。
> 将你从零构建的版本与库版本进行对比。
> 这既验证了概念，也介绍了实用工具。]

## Ship It
> 交付制品

[What reusable artifact does this lesson produce?
Could be a prompt, a skill, an agent, an MCP server, or a tool.
Include it here and save it in the outputs/ folder.]
> [这节课产出什么可复用的制品？
> 可以是 prompt、skill、agent、MCP server 或工具。
> 在此处包含它并保存到 outputs/ 文件夹。]

## Exercises
> 练习

1. [Easy — reinforce the core concept / 简单 — 巩固核心概念]
2. [Medium — apply it to a different problem / 中等 — 应用到不同问题]
3. [Hard — extend or combine with prior lessons / 困难 — 扩展或结合前置课程]

## Key Terms
> 关键术语

| Term | What people say | What it actually means |
|------|----------------|----------------------|
| 术语 | 人们常怎么说 | 实际含义 |
| [term] | [common misconception / 常见误解] | [actual definition / 实际定义] |

## Further Reading
> 延伸阅读

- [Resource 1](url) — [why it's worth reading / 为什么值得读]
- [Resource 2](url) — [why it's worth reading / 为什么值得读]
```

## Code File Guidelines
> 代码文件规范

- Code must run without errors
> 代码必须能无错运行
- No comments — code should be self-explanatory
> 不写注释 — 代码应该自解释
- Use the language that fits best for the topic
> 使用最适合该主题的语言
- Include a `requirements.txt` or equivalent if there are dependencies
> 如有依赖，包含 `requirements.txt` 或等效文件
- Start simple, build up complexity
> 从简单开始，逐步增加复杂度
- Every function and class should have a clear purpose
> 每个函数和类都应有明确的用途

## Output File Format
> 输出文件格式

### Prompts
> Prompt 模板

```markdown
---
name: prompt-name
description: What this prompt does / 此 prompt 的功能
phase: [phase number / 阶段编号]
lesson: [lesson number / 课程编号]
---

[Prompt content / Prompt 内容]
```

### Skills
> 技能

```markdown
---
name: skill-name
description: What this skill teaches / 此 skill 教什么
version: 1.0.0
phase: [phase number / 阶段编号]
lesson: [lesson number / 课程编号]
tags: [relevant, tags / 相关标签]
---

[Skill content / Skill 内容]
```
