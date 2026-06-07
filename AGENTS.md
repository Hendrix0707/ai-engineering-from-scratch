# AGENTS.md
> 操作手册

Operating manual for contributors and AI agents touching this repo. Read it before opening a PR.
> 面向贡献者和 AI Agent 的操作手册。提交 PR 前请阅读。

The repo is a curriculum, not a SaaS app. The lessons are the product. Every rule below keeps 435 lessons coherent over time.
> 本仓库是一个课程体系，而非 SaaS 应用。课程本身就是产品。以下每条规则都是为了保持 435 节课长期一致。

---

## Philosophy
> 核心理念

435 lessons. 20 phases. Every algorithm built from raw math before a single framework gets imported. You write backprop, the tokenizer, the attention mechanism, and the agent loop by hand in Python, TypeScript, Rust, or Julia. Then you run the same operation through the production library so the framework stops being a black box. The "Build It / Use It" split is the spine. Each lesson ships a reusable artifact you can plug into your daily workflow.
> 435 节课。20 个阶段。每个算法在导入任何框架之前，都从原始数学开始构建。你用手写的方式实现反向传播、分词器、注意力机制和 agent 循环——用 Python、TypeScript、Rust 或 Julia。然后再用生产库跑同样的操作，让框架不再是一个黑盒。"Build It / Use It"（先构建再使用）的分割是课程的脊梁。每节课都产出一个可复用的制品，你可以直接接入日常工作流。

---

## Repo layout
> 仓库布局

```
phases/
  NN-phase-slug/
    NN-lesson-slug/
      docs/en.md              # lesson explainer / 课程讲解
      code/                   # implementation + tests / 实现 + 测试
      quiz.json               # 6 questions / 6 道题
      outputs/                # reusable artifact (skill / prompt / agent / MCP server) / 可复用制品（skill/prompt/agent/MCP server）
README.md                     # public face; lesson counts auto-synced / 对外主页；课程计数自动同步
ROADMAP.md                    # phase/lesson status / 阶段/课程状态
glossary/terms.md             # canonical term definitions / 规范术语定义
site/
  build.js                    # parses README + ROADMAP + glossary -> data.js / 解析 README + ROADMAP + glossary → data.js
  data.js                     # generated; rebuilt by CI on main push / 生成文件；CI 在 main 推送时重建
scripts/                      # automation / 自动化脚本
.github/workflows/
  curriculum.yml              # invariant + auto-sync workflow / 不变量检查 + 自动同步工作流
```

---

## Hard rules
> 硬性规则

1. **One commit per lesson directory.** Never batch multiple lessons into one commit. A 10-lesson PR has 10 commits.
> **每课目录一次提交。** 绝不将多节课合并为一次提交。10 节课的 PR 应有 10 次提交。
2. **Conventional commit subjects** ≤72 chars: `feat(phase-NN/MM): <slug>`. Body explains why, not what.
> **Conventional Commits 主题** ≤72 字符：`feat(phase-NN/MM): <slug>`。正文解释为什么，而非做了什么。
3. **Mermaid or SVG only** for diagrams. No ASCII / Unicode box-drawing.
> 图表**仅使用 Mermaid 或 SVG**。不使用 ASCII/Unicode 字符画。
4. **Every fenced code block needs a language tag.** Use `text`, `json`, `python`, `typescript`, `rust`, `julia`, `bash`, `console`, `mermaid`, `yaml` as appropriate.
> **每个代码块必须标注语言。** 使用 `text`、`json`、`python`、`typescript`、`rust`、`julia`、`bash`、`console`、`mermaid`、`yaml` 等。
5. **Original implementations only.** Don't cite external curriculum repos in docs, code comments, or commit text. Cite RFCs, official specs, and academic papers when they are the canonical source.
> **仅原创实现。** 不在文档、代码注释或提交文本中引用外部课程仓库。引用 RFC、官方规范和学术论文作为规范来源。
6. **Dependency allowlist** (see `Dependencies` below). Stdlib-first.
> **依赖白名单**（见下方 `Dependencies`）。标准库优先。
7. **Never commit generated files**: `catalog.json` is gitignored, `site/data.js` is rebuilt by CI, `package-lock.json` is never tracked.
> **绝不提交生成文件**：`catalog.json` 已被 gitignore，`site/data.js` 由 CI 重建，`package-lock.json` 从不追踪。

---

## Dependencies
> 依赖

| Language / 语言  | Allowed / 允许使用                                                                |
|------------------|-----------------------------------------------------------------------------------|
| Python           | `numpy`, `torch`, `h5py`, `zstandard`, `safetensors`, stdlib                      |
| TypeScript       | `hono`, `zod`, `ws` (only when WebSockets needed / 仅在需要 WebSocket 时), `@hono/node-server`, Node 20+ stdlib |
| Rust             | stdlib only (single-file `rustc --edition 2021`) / 仅标准库                        |
| Julia            | `Random`, `Statistics`, `LinearAlgebra`, `Printf` (Julia stdlib)                   |

If a finding suggests a banned dep, skip it with the reason "stays stdlib-first for educational clarity."
> 如果某发现建议使用被禁依赖，跳过它，理由为"出于教育清晰性保持标准库优先"。

---

## Lesson contract
> 课程规约

### docs/en.md frontmatter
> docs/en.md 前置元数据

```markdown
# <Title>
> <标题>

> <One-line hook>
> <一句话钩子>

**Type:** <Learn | Build | Reference>
> **类型：** <Learn | Build | Reference>

**Languages:** <comma-list matching the main.* files in code/>
> **语言：** <逗号分隔列表，与 code/ 中的 main.* 文件匹配>

**Prerequisites:** <comma-list of upstream lessons, or "None">
> **前置课程：** <逗号分隔的上游课程列表，或 "None">

**Time:** ~<estimate in minutes>
> **时间：** ~<预估分钟数>

## Learning Objectives
> 学习目标
- <4-6 bullet points starting with a verb>
> <4-6 条以动词开头的要点>
```

The `**Languages:**` field must match the languages with a `main.*` file in `code/`.
> `**Languages:**` 字段必须与 `code/` 中拥有 `main.*` 文件的语言匹配。

### quiz.json schema
> quiz.json 模式

```json
{
  "lesson": "<dir-slug>",
  "title": "<Lesson Title> / <课程标题>",
  "questions": [
    {"stage": "pre",   "question": "...", "options": ["a","b","c","d"], "correct": 0, "explanation": ""},
    {"stage": "check", "question": "...", "options": ["a","b","c","d"], "correct": 1, "explanation": ""},
    {"stage": "check", "question": "...", "options": ["a","b","c","d"], "correct": 2, "explanation": ""},
    {"stage": "check", "question": "...", "options": ["a","b","c","d"], "correct": 1, "explanation": ""},
    {"stage": "post",  "question": "...", "options": ["a","b","c","d"], "correct": 3, "explanation": ""},
    {"stage": "post",  "question": "...", "options": ["a","b","c","d"], "correct": 0, "explanation": ""}
  ]
}
```

Exactly 6 questions: 1 pre + 3 check + 2 post. `correct` is zero-indexed. The site renderer only understands this shape — legacy `q/choices/answer` schemas crash silently.
> 恰好 6 道题：1 道学前 + 3 道检查 + 2 道学后。`correct` 从 0 开始索引。网站渲染器只理解这种格式——旧的 `q/choices/answer` 模式会静默崩溃。

### code/
> 代码

- Runs end-to-end and exits 0 on the canonical command for the language.
> 端到端运行，并以该语言规范命令退出码 0。
- Self-terminating demo. No infinite stdin loops, no hangs on missing API keys.
> 自终止演示。无无限 stdin 循环，不因缺少 API key 而挂起。
- 4-6 line header comment citing the lesson's `docs/en.md` path and any spec or RFC sources.
> 4-6 行头部注释，引用课程的 `docs/en.md` 路径及任何规范或 RFC 来源。

### code/tests/
> 代码测试

- 5+ unit tests minimum.
> 至少 5 个单元测试。
- Runs via the language's stdlib runner (`python3 -m unittest discover`, `npx tsx --test`, Rust/Julia inline).
> 通过语言的标准库测试运行器运行（`python3 -m unittest discover`、`npx tsx --test`、Rust/Julia 内联）。

---

## Per-PR validation
> 每次 PR 的验证

Run locally before pushing:
> 推送前本地运行：

```bash
python3 scripts/audit_lessons.py
python3 scripts/check_readme_counts.py        # advisory — CI fixes on merge / 建议性 — CI 在合并时修复

# For each lesson touched: / 对每个涉及的课程：
cd phases/NN-phase/MM-lesson/code
python3 main.py && python3 -m unittest discover tests -v   # or the lang equivalent / 或语言等效命令
```

CI gates (`.github/workflows/curriculum.yml`):
> CI 门控 (`.github/workflows/curriculum.yml`)：

| Job / 作业                         | Trigger / 触发条件   | Behavior / 行为                                         |
|------------------------------------|----------------------|---------------------------------------------------------|
| `audit`                            | push + PR            | Runs `audit_lessons.py`. Blocking. / 运行 `audit_lessons.py`。阻塞性。 |
| `readme-counts-sync` (main only)   | push to main         | Rebuilds catalog + auto-fixes README counts. / 重建目录 + 自动修复 README 计数。 |
| `site-rebuild` (main only)         | push to main         | Re-runs `node site/build.js`, commits `site/data.js`. / 重新运行 `node site/build.js`，提交 `site/data.js`。 |
| `readme-counts-drift`              | PR                   | Advisory only — main self-heals on merge. / 仅建议 — main 在合并时自愈。 |

---

## Automation contract
> 自动化契约

**CI handles automatically — do not touch in your PR:**
> **CI 自动处理 — 不要在 PR 中手动修改：**

| Surface / 表面           | Bot / 机器人                   | When / 何时             |
|--------------------------|--------------------------------|-------------------------|
| `catalog.json`           | rebuilt on demand (gitignored) / 按需重建（已 gitignore） | every CI job / 每次 CI 任务 |
| `README.md` counts       | `readme-counts-sync`           | on push to main / push 到 main 时 |
| `site/data.js`           | `site-rebuild`                 | on push to main / push 到 main 时 |

**You handle:**
> **你负责：**

| Surface / 表面              | When / 何时                                                          |
|-----------------------------|----------------------------------------------------------------------|
| `README.md` lesson-link rows | when adding a new lesson — link `[Title](phases/NN-phase/MM-lesson/)` / 添加新课时 |
| `ROADMAP.md` status          | when marking a lesson complete or WIP / 标记课程完成或进行中时       |
| `glossary/terms.md`          | when introducing a term used by more than one lesson / 引入多课使用的术语时 |

**Common bug**: if `grep -c 'tree/main/phases/NN-' site/data.js` is 0 after merge, the Phase NN README rows are plain text and missing the `[Title](phases/NN-...)` markdown link. `site/build.js` derives the URL from that link.
> **常见 bug**：如果合并后 `grep -c 'tree/main/phases/NN-' site/data.js` 为 0，说明 Phase NN 的 README 行是纯文本，缺少 `[Title](phases/NN-...)` markdown 链接。`site/build.js` 从该链接提取 URL。

---

## Conflict resolution
> 冲突解决

```bash
git fetch origin main
git merge --no-edit origin main

# Catalog conflict (legacy branches only — catalog.json is gitignored now):
# 目录冲突（仅旧分支 — catalog.json 现已 gitignore）：
git rm catalog.json
git commit --no-edit

# README count conflict:
# README 计数冲突：
git checkout --theirs README.md
python3 scripts/build_catalog.py
python3 scripts/check_readme_counts.py --fix
git add README.md && git commit --no-edit

# site/data.js conflict:
# site/data.js 冲突：
git checkout --theirs site/data.js
node site/build.js
git add site/data.js && git commit --no-edit

git push origin <your-branch>
```

Avoid `git push --force` to a branch with open review comments. Force-push detaches them.
> 避免对有未关闭 review 评论的分支使用 `git push --force`。强制推送会使评论脱离上下文。

---

## New-lesson onboarding
> 新课程上手指南

```bash
mkdir -p phases/NN-phase-slug/MM-new-lesson/{docs,code/tests,outputs}

# 1. Write docs/en.md with the frontmatter above.
#    按上述 frontmatter 编写 docs/en.md。
# 2. Write code/main.<lang> with the 4-6 line header.
#    编写带 4-6 行头部注释的 code/main.<lang>。
# 3. Write code/tests/test_main.* with 5+ tests.
#    编写 code/tests/test_main.*，包含 5+ 个测试。
# 4. Write quiz.json with the schema above.
#    按上述 schema 编写 quiz.json。
# 5. (Optional) Add outputs/skill-<slug>.md if the lesson ships a skill.
#    （可选）如果课程产出 skill，添加 outputs/skill-<slug>.md。

# 6. Add to README.md:
#    添加到 README.md：
#    | MM | [Lesson Title](phases/NN-phase-slug/MM-new-lesson/) | Type | Lang |

# 7. Update ROADMAP.md status row.
#    更新 ROADMAP.md 状态行。

# 8. Validate locally.
#    本地验证。

# 9. Atomic commit:
#    原子提交：
git add phases/NN-phase-slug/MM-new-lesson README.md ROADMAP.md
git commit -m "feat(phase-NN/MM): add <slug>"
git push -u origin <your-branch>
gh pr create --title "feat(phase-NN/MM): add <slug>" --body "<5-line summary>"
```

`site/data.js` regenerates on merge — leave it for CI.
> `site/data.js` 在合并时重新生成——留给 CI 处理。

---

Last reviewed: 2026-05-27.
> 最后审阅：2026-05-27。
