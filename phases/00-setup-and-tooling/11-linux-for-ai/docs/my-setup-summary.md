# Lesson 11 完成总结：Linux for AI

## 这是什么

Linux 生存指南。只讲 AI 工程师在远程 GPU 机器上需要的命令行操作。

## 与你现状的关系

| 你现在 | Windows 11 + PowerShell |
|--------|------------------------|
| 你有 Linux 访问吗？ | **有** — SSH 配好了 Sdu-1、school_se、seetacloud（都是 Linux 服务器） |
| 你有 WSL2 吗？ | Windows 11 支持，一行命令可装：`wsl --install -d Ubuntu-24.04` |
| 这节课现在能用上吗？ | **SSH 连服务器时直接能用**，本地 Windows 用不上但连上去就是这套 |

## 核心速查（以后贴终端旁边）

```
目录导航    pwd / ls -la / cd ~ / cd .. / mkdir -p
文件操作    cp / mv / rm -rf（小心！不可逆）/ cat / head / tail -f
搜索        grep "关键词" 文件名 / find . -name "*.py"
权限        chmod +x 脚本.sh / sudo 命令
装软件      sudo apt update && sudo apt install -y 包名
进程        htop / ps aux | grep python / kill PID / nvidia-smi
磁盘        df -h / du -sh *
下载        wget URL / curl -O URL
传输        scp 文件 user@机器:路径 / rsync -avz --progress
保活        tmux new -s 名字 / Ctrl+B, d / tmux attach -t 名字
```

## 两个最重要的习惯

### 1. 长时间训练永远放在 tmux 里跑

```
SSH 连服务器 → tmux new -s train → python train.py → Ctrl+B, d 分离 → SSH 断开
3 小时后 → SSH 连回来 → tmux attach -t train → 训练还在跑，日志可见
```

不用 tmux：合上笔记本 → 训练没了，几小时白跑。

### 2. rm -rf 前再三确认

Linux 没有回收站。`rm -rf` 删了就没了。敲完路径检查一遍。

## Windows 用户的加分项：WSL2

你可以在本地装 WSL2，获得一个真实的 Linux 环境来练习这些命令：

```powershell
# PowerShell（管理员）
wsl --install -d Ubuntu-24.04
# 重启后从开始菜单打开 Ubuntu
sudo apt update && sudo apt upgrade -y
```

装完后你的 Windows 文件在 WSL 里路径为 `/mnt/c/`、`/mnt/f/` 等。GPU 也可透传（你已装了 Windows 版 NVIDIA 驱动）。

## 建议

**这节课当速查手册用。** 不需要背命令。当你第一次 SSH 进 Linux 服务器做事时，打开这节课翻——10 分钟就能上手。用几次就记住了。
