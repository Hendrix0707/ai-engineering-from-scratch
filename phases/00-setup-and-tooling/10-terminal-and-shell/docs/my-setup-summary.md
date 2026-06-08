# Lesson 10 完成总结：Terminal & Shell

## 学了什么

这节课讲 AI 工程师必须会的终端操作：管道处理日志、tmux 多窗格跑训练、监控 GPU、SSH 传文件。

## 你现在能用的 vs 以后才能用的

### 现在就能用（Windows 上有对应方案）

| 操作 | Linux 命令 | 你的 Windows 方案 |
|------|-----------|------------------|
| GPU 状态 | `nvidia-smi` | `nvidia-smi`（一模一样） |
| 实时 GPU 监控 | `watch -n1 nvidia-smi` | `nvidia-smi -l 1`（你跑 benchmark 时用过） |
| SSH 连服务器 | `ssh user@host` | VS Code Remote SSH + Git Bash（已配好 3 台） |
| 传文件 | `scp` / `rsync` | VS Code Remote SSH 直接拖文件，或 Git Bash 里用 scp |
| 清屏 | `clear` / `Ctrl+L` | 同样有效 |
| 取消命令 | `Ctrl+C` | 同样有效 |

### 现在还不行，等上 Linux 服务器时

| 操作 | 为什么现在用不了 | 什么时候需要 |
|------|-----------------|-------------|
| **tmux** 多窗格 | Windows 不支持，需要 WSL 或 Linux | 远程服务器上跑长时间训练时（Phase 3+） |
| **管道 + grep** 过滤日志 | PowerShell 语法不同，但 Git Bash 可以跑 | 分析训练日志、找 error |
| **htop / nvtop** | Linux 专属工具 | 服务器上排查 OOM、内存泄漏 |
| **nohup** 后台保活 | Windows 有别的方案（Start-Process） | 暂时不需要，反正你目前在本地跑 |
| **Bash aliases** | PowerShell 不支持 bash 别名语法 | 配 `$PROFILE` 可以实现 PowerShell 版 |

### 核心概念（记住就行，以后天天用）

```
1. 管道 |  →  把前一个命令的输出喂给后一个命令
   cat train.log | grep "loss" | wc -l
   → 看日志 → 过滤"loss"行 → 统计行数

2. 重定向 >  →  把输出存到文件
   python train.py > output.log 2>&1
   → 正常输出 + 错误信息全存到文件里

3. tmux  →  创建"不死的终端"
   tmux new -s train   → 创建会话
   Ctrl+B, d           → 断开（训练继续跑）
   tmux attach -t train → 重新连上
   跑了 3 小时回来了，训练还在，日志可见

4. SSH 端口转发  →  本地浏览器访问远程服务
   ssh -L 8888:localhost:8888 user@gpu-box
   → 在本地打开 localhost:8888，实际是远程的 Jupyter
```

## 建议

**这节课现在不深入做练习。** 把核心概念（管道、重定向、tmux 是什么）看一遍，知道它们存在就行。等你第一次连 Linux 服务器跑训练时，回来速查这节课的命令——那时候 30 分钟就能掌握。
