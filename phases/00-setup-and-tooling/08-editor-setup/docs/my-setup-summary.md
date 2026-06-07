# Lesson 08 完成总结：Editor Setup

## 做了什么

### 扩展安装（8 个）

| 扩展 | 状态 | 作用 |
|------|:--:|------|
| Python | 已有 | Python 语言支持、虚拟环境检测、运行/调试 |
| Pylance | 已有 | 快速类型检查、自动补全、import 解析 |
| Jupyter | 新装 | 在 Cursor 内运行 `.ipynb` notebook |
| GitLens | 新装 | 每行代码旁显示 git 作者和时间 |
| Remote SSH | 已有 | 远程连接 GPU 服务器（Sdu-1、seetacloud） |
| Debugpy | 已有 | Python 单步调试 |
| Black Formatter | 新装 | 保存时自动格式化代码 |
| Ruff | 新装 | 实时 linting，不规范处标波浪线 |

### 设置更改（settings.json）

| 设置 | 效果 |
|------|------|
| `python.analysis.typeCheckingMode: "basic"` | 参数类型不对 → 黄色波浪线 |
| `editor.formatOnSave: true` + Black | `Ctrl+S` → 代码自动对齐 |
| `editor.rulers: [88, 120]` | 编辑器显示 88 和 120 字符竖线 |
| `notebook.output.scrolling: true` | Jupyter 长输出可滚动 |
| `files.autoSave: "afterDelay"` | 1 秒后自动保存 |
| `files.exclude` / `search.exclude` | 隐藏 `__pycache__`、`.venv` 等垃圾文件 |

### 个人配置保留不变

主题（One Dark Pro）、壁纸、LeetCode、SSH 主机列表（Sdu-1、school_se、seetacloud）、终端配置、代理设置等全部保留。

---

## 实际效果

- 写 Python → Pylance 实时检查类型错误 + Ruff 实时检查代码规范
- `Ctrl+S` → Black 自动格式化
- 打开 `.ipynb` → Cursor 内直接运行 Jupyter notebook
- 文件树 → 不再被 `__pycache__`、`.venv` 等干扰
- Git 操作 → GitLens 显示每行代码历史
- 远程开发 → `Ctrl+Shift+P` → Remote-SSH 连服务器（已有）

## 配置文件位置

- 全局设置：`C:\Users\84070\AppData\Roaming\Cursor\User\settings.json`
- 项目推荐扩展：`phases/00-setup-and-tooling/08-editor-setup/code/vscode/extensions.json`
- 项目推荐设置：`phases/00-setup-and-tooling/08-editor-setup/code/vscode/settings.json`
