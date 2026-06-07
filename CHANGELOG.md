# Changelog
> 更新日志

What's new in the curriculum. Most recent first.
> 课程的新增内容。最近的排在最前。

Format loosely follows [Keep a Changelog](https://keepachangelog.com/). Each entry names the phase, lesson, and what changed, so learners can jump straight to the delta.
> 格式大致遵循 [Keep a Changelog](https://keepachangelog.com/)。每个条目注明了阶段、课程和变更内容，方便学习者直接跳转到改动处。

## [Unreleased]
> [未发布]

### Added
> 新增

- `scripts/scaffold-lesson.sh` — scaffolder that creates `phases/NN-phase/NN-lesson/` with the full folder structure and a `docs/en.md` skeleton prefilled from `LESSON_TEMPLATE.md`.
> `scripts/scaffold-lesson.sh` — 脚手架脚本，创建 `phases/NN-phase/NN-lesson/` 完整目录结构，并从 `LESSON_TEMPLATE.md` 预填充 `docs/en.md` 骨架。
- `.github/PULL_REQUEST_TEMPLATE.md` — contributor checklist (code runs, no code comments, built-from-scratch-first, atomic per-lesson commit, markdown-link ROADMAP row).
> `.github/PULL_REQUEST_TEMPLATE.md` — 贡献者检查清单（代码可运行、代码无注释、先构建再框架、每课原子提交、ROADMAP 行使用 markdown 链接）。
- `.github/ISSUE_TEMPLATE/bug_report.md` and `new_lesson_proposal.md` — structured intake for bug reports and lesson pitches.
> `.github/ISSUE_TEMPLATE/bug_report.md` 和 `new_lesson_proposal.md` — 结构化的 bug 报告和新课提案模板。
- This `CHANGELOG.md`.
> 本 `CHANGELOG.md`。

## 2026-04 — Phase 4: Computer Vision complete
> 2026-04 — Phase 4：计算机视觉 完成

### Added
> 新增

- All 28 Phase 4 lessons, covering image fundamentals through multi-modal vision (VLMs, 3D, video, self-supervised).
> Phase 4 全部 28 节课完成，覆盖从图像基础到多模态视觉（VLM、3D、视频、自监督）。
- Phase 4 rows in `ROADMAP.md` linked as markdown to the lesson folders, so the website surfaces them.
> `ROADMAP.md` 中的 Phase 4 行以 markdown 链接指向课程文件夹，网站可正常展示。

### Fixed
> 修复

- Phase 4 precision pass across 15+ lessons:
> Phase 4 精确性审查，覆盖 15+ 节课：
  - `phase-4/02`: shape calculator specifies RF/stride handling for adaptive pool, flatten, and linear.
  > `phase-4/02`：shape calculator 明确了自适应池化、展平和线性层的感受野/步长处理。
  - `phase-4/03`: backbone selector description lists all covered families; head guidance added for OCR, medical, industrial.
  > `phase-4/03`：backbone selector 描述列出了所有覆盖的模型家族；为 OCR、医疗、工业场景添加了 head 选择指南。
  - `phase-4/04`: classification diagnostics use quantitative thresholds per failure mode; `n/a` declared for undefined metrics; guard for fewer than 3 classes.
  > `phase-4/04`：分类诊断对每种失败模式使用量化阈值；未定义指标声明为 `n/a`；增加了少于 3 类的防护。
  - `phase-4/06`: detection metric reader uses `AP@0.5` (not `mAP@0.5`); per-class recall declared optional; anchor designer clarifies stride truncation and single-anchor-per-level path.
  > `phase-4/06`：检测指标读取器使用 `AP@0.5`（而非 `mAP@0.5`）；逐类召回率声明为可选；anchor designer 明确了步长截断和单锚点路径。
  - `phase-4/10`: sampler picker declares `unet_forward_ms` as an input; ControlNet guard promoted to rule 0.
  > `phase-4/10`：sampler picker 将 `unet_forward_ms` 声明为输入；ControlNet 防护提升为规则 0。
  - `phase-4/14`: ViT inspector aligned with refusal rule — port attempts are audited, not endorsed.
  > `phase-4/14`：ViT inspector 与拒绝规则对齐 — 端口尝试被审计而非认可。
  - `phase-4/24`: open-vocab stack picker has explicit rule precedence and license-filter semantics; concept designer resolves step-5/rule-80 conflict.
  > `phase-4/24`：开放词汇栈选择器具有明确的规则优先级和许可证过滤语义；concept designer 解决了步骤 5/规则 80 冲突。
  - `phase-4/25`: VLM docs `_merge` raises descriptive `ValueError` on placeholder mismatch; CMER normalises internally.
  > `phase-4/25`：VLM 文档 `_merge` 在占位符不匹配时抛出描述性 `ValueError`；CMER 内部进行归一化。
  - `phase-4/27`: `synthetic_frames` clips GT boxes to frame H/W.
  > `phase-4/27`：`synthetic_frames` 将 GT 框裁剪到帧高/宽范围内。
  - `phase-4/28`: `rope_3d` validates dim split; dropped unused `F` import from DiT block example.
  > `phase-4/28`：`rope_3d` 验证维度分割；从 DiT block 示例中删除了未使用的 `F` 导入。

## 2026-Q1 and earlier
> 2026年第一季度及更早

### Added
> 新增

- Phase 0 (Setup & Tooling): all 12 lessons.
> Phase 0（环境搭建与工具）：全部 12 节课。
- Phase 1 (Math Foundations): all 22 lessons.
> Phase 1（数学基础）：全部 22 节课。
- Phase 2 (ML Fundamentals): all 18 lessons.
> Phase 2（机器学习基础）：全部 18 节课。
- Phase 3 (Deep Learning Core): core lessons through perceptron, backprop, optimizers.
> Phase 3（深度学习核心）：核心课程，含感知机、反向传播、优化器。
- Built-in Claude Code skills: `find-your-level` (placement quiz) and `check-understanding` (per-phase quiz).
> 内置 Claude Code 技能：`find-your-level`（分班测验）和 `check-understanding`（逐阶段测验）。
- Website at `aiengineeringfromscratch.com`: catalog, per-lesson pages, roadmap, 277-term glossary.
> 网站 `aiengineeringfromscratch.com`：课程目录、逐课页面、路线图、277 条术语表。
- Initial scaffolding for all 20 phases (`phases/00-*` through `phases/19-*`).
> 全部 20 个阶段的初始脚手架（`phases/00-*` 到 `phases/19-*`）。
- `LESSON_TEMPLATE.md`, `CONTRIBUTING.md`, `ROADMAP.md`, `README.md`.
> `LESSON_TEMPLATE.md`、`CONTRIBUTING.md`、`ROADMAP.md`、`README.md`。

[Unreleased]: https://github.com/rohitg00/ai-engineering-from-scratch/compare/HEAD...HEAD
