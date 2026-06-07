# Git 实操手册

> 你需要掌握的 Git 操作 —— 本项目、进组、上班三种场景

---

## 一、核心概念：4 区域模型

```
工作目录 ──git add──► 暂存区 ──git commit──► 本地仓库 ──git push──► 远程仓库
   │                     │                       │                      │
   │              git reset                  git reset --soft        git pull
   │◄────────────────────┤◄──────────────────────┤◄─────────────────────│
```

- **工作目录** = 你实际看到的文件
- **暂存区** = 选中哪些改动放进下一次快照
- **本地仓库** = 一连串带注释的快照（commit 历史）
- **远程仓库** = GitHub / GitLab 上的副本

**核心心智模型**：Git 不是网盘同步，是一连串完整快照。每次 commit 都是整个项目的备份，随时可以穿越回去。

---

## 二、日常命令速查

| 命令 | 作用 | 频率 |
|------|------|------|
| `git status` | 看看改了什么 | 每5分钟 |
| `git diff` | 看具体改动内容 | 提交前 |
| `git add <file>` | 选中要提交的文件 | 若干次 |
| `git commit -m "..."` | 保存快照 | 每完成一个小改动 |
| `git push origin <branch>` | 推到 GitHub | 每次 commit 后 |
| `git log --oneline` | 看历史 | 需要回顾时 |
| `git checkout -b <name>` | 创建新分支 | 开始新任务时 |
| `git checkout <branch>` | 切换分支 | 切换任务时 |
| `git merge <branch>` | 合并分支 | 任务完成后 |

---

## 三、本项目的使用方式

### 你的仓库结构

```
upstream (rohitg00/ai-engineering-from-scratch) ← 原仓库，只拉取
origin   (Hendrix0707/ai-engineering-from-scratch) ← 你的 fork，可推送
```

### 每次学习的流程

```bash
# 1. 同步上游最新课程内容
git checkout main
git fetch upstream
git merge upstream/main
git push origin main

# 2. 合并到你的进度分支
git checkout my-progress
git merge main

# 3. 学习、写代码、提交
git add <文件>
git commit -m "完成 Phase X Lesson Y"
git push origin my-progress
```

### 原则

- `main` 永远保持干净，只跟踪上游
- 所有自己的改动都在 `my-progress` 上
- 不做 PR（不需要，你的 fork 自己用）
- 生成文件冲突 → 重新运行生成命令（如 `node site/build.js`）

---

## 四、进组后的使用方式（Lab）

### 典型场景：导师给你一个任务

```bash
# 1. 从最新的 main 拉分支
git checkout main
git pull origin main
git checkout -b feat/task-name

# 2. 写代码，小步频繁提交
git add src/xxx.py
git commit -m "feat: 完成 xxx 模块"

# 3. 推送到远程备份
git push origin feat/task-name
```

### Pull Request 流程

```
你写完代码 → 创建 PR → 师兄/导师 Review → 修改 → 通过 → Merge 到 main
```

```bash
# Review 后需要修改
git add src/xxx.py
git commit -m "fix: 根据 review 意见修改 xxx"
git push origin feat/task-name    # PR 自动更新
```

### 分支策略

```
main ────●────●────●────●────●  ← 永远是稳定的
          \         /
feat-a     ●──●──●─┘             ← 每个人一个功能分支
                       \
feat-b                  ●──●──●  ← 互不干扰
```

### 铁律

- **绝不直接 commit 到 main**
- **每次开始工作前先 pull 最新代码**
- **同一个功能在一个分支上做，别混**
- **commit message 要有意义，别写 "update"**

---

## 五、上班后的使用方式（Company）

### 和 Lab 的关键区别

| | Lab | Company |
|---|---|---|
| 分支策略 | 简单 feature branch | 可能有 Git Flow / Trunk-based |
| Code Review | 师兄看 | 必做，可能有 CI 自动检查 |
| Commit 格式 | 随意 | Conventional Commits 强制 |
| 合并方式 | 普通 merge | 可能要求 squash / rebase |
| 发布节奏 | 没有 | 有版本号、有 CHANGELOG |

### Conventional Commits（约定式提交）

```
<type>: <简短描述>

feat: 添加水龙头抓取策略
fix: 修复 IK 求解器数值不稳定问题
docs: 更新 GR00T 部署文档
refactor: 提取通用机器人工具函数
test: 为抓取规划器添加回归测试
chore: 更新依赖版本
```

### Merge Conflict 处理

```bash
# 1. 冲突发生了，别慌
git merge main
# CONFLICT ... 正常的

# 2. 看哪些文件冲突
git status

# 3. 打开冲突文件，找到标记
<<<<<<< HEAD
你的改动
=======
别人的改动
>>>>>>> main

# 4. 手动编辑，保留正确的，删掉标记
# 5. 标记已解决
git add <冲突文件>

# 6. 完成合并
git commit -m "Merge main into feat/xxx"
```

### 自救命令

```bash
# "我改错了，想回到上次提交的状态"
git checkout -- file.py           # 丢弃单个文件的修改
git reset --hard HEAD             # 丢弃所有未提交的修改（不可恢复！）

# "我提交了但后悔了，还没 push"
git reset --soft HEAD~1            # 撤销 commit，改动保留在暂存区
git reset HEAD~1                   # 撤销 commit 和 add，改动回到工作目录

# "我想暂存当前改动，切去干别的事"
git stash                         # 暂存
git stash pop                     # 恢复

# "这行代码是谁写的、什么时候写的"
git blame file.py
```

---

## 六、你只需要这些

你不需要 `rebase`、`cherry-pick`、`submodule`、`reflog` 这些高级操作。上面列的就是你日常 99% 会用到的。

用到高级操作时再查，别提前学。
