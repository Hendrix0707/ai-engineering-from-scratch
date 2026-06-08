# AI 项目环境与依赖管理

## 1. 你现在的状态

| 项目 | 当前 |
|------|------|
| 本地机器 | Windows 11，RTX 3060 Laptop |
| Python | D:\Python312（全局安装） |
| 包管理 | `pip install` 直接装到全局 |
| 包列表 | 没有记录文件，装了啥自己记不住 |
| 远程服务器 | Sdu-1、school_se、seetacloud（已配 SSH） |

## 2. 拿到新服务器第一件事（检查清单）

按顺序执行，约 10 分钟：

### 2.1 基础检查

```bash
# 系统信息
uname -a
cat /etc/os-release

# GPU 是否存在
nvidia-smi

# CUDA 版本
nvcc --version

# Python 版本
python3 --version
```

### 2.2 装 Python 和 uv

```bash
# 装 uv（比 pip 快 10-100x，自带虚拟环境管理）
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc   # 或 source ~/.zshrc

# uv 也可以帮你装 Python！！
uv python install 3.12
```

### 2.3 配置 Git 和 SSH

```bash
git config --global user.name "dogdogw"
git config --global user.email "你的邮箱"

# 生成 SSH key（如果没有）
ssh-keygen -t ed25519 -C "你的邮箱"
cat ~/.ssh/id_ed25519.pub   # 复制到 GitHub Settings > SSH Keys

# 测试
ssh -T git@github.com
```

### 2.4 克隆项目并装依赖

```bash
git clone https://github.com/Hendrix0707/ai-engineering-from-scratch.git
cd ai-engineering-from-scratch
uv venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

### 2.5 验证 GPU 可用

```bash
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}, GPU: {torch.cuda.get_device_name(0)}')"
```

---

## 3. 常用 AI 依赖分类

### 必装（几乎所有项目都要）

```txt
torch              # PyTorch 深度学习框架
numpy              # 数值计算
pandas             # 数据处理
transformers       # Hugging Face 模型库
datasets           # Hugging Face 数据集库
huggingface_hub    # 下载模型/数据集
accelerate         # 多 GPU / 混合精度训练
safetensors        # 安全的模型权重格式
```

### 按项目类型加装

**文本分类 / NLP：**
```txt
tokenizers         # 快速分词
scikit-learn       # 传统 ML 评估指标
```

**训练/微调：**
```txt
peft               # LoRA / QLoRA 微调
bitsandbytes       # 4-bit / 8-bit 量化
trl                # Transformer 强化学习
deepspeed          # 大模型分布式训练
```

**RAG（检索增强生成）：**
```txt
qdrant-client      # 向量数据库客户端
chromadb           # 另一个向量数据库
langchain          # RAG 框架
sentence-transformers  # 嵌入模型
```

**API / Web 服务：**
```txt
fastapi            # Web API 框架
uvicorn            # ASGI 服务器
gradio             # 快速搭建 demo 界面
```

**数据处理：**
```txt
pillow             # 图像处理
opencv-python      # 计算机视觉
pyarrow            # 列式数据格式
```

**开发/调试：**
```txt
jupyter            # Notebook
ipykernel          # Jupyter 内核
wandb              # 实验追踪（可选）
```

---

## 4. requirements.txt 模板

你的项目根目录放一个 `requirements.txt`：

```txt
# === 必装 ===
torch>=2.3.0
numpy>=1.26.0
pandas>=2.2.0
transformers>=4.40.0
datasets>=2.19.0
huggingface_hub>=0.23.0
accelerate>=0.30.0
safetensors>=0.4.0

# === 训练 ===
peft>=0.10.0
# bitsandbytes  # 需要 CUDA 工具链，在服务器上单独装

# === 分词 ===
tokenizers>=0.19.0

# === NLP 评估 ===
scikit-learn>=1.5.0

# === RAG ===
# qdrant-client>=1.9.0
# sentence-transformers>=3.0.0

# === API ===
# fastapi>=0.111.0
# uvicorn>=0.30.0

# === 开发 ===
jupyter>=1.0.0
ipykernel>=6.29.0
```

用 `#` 注释掉暂时不用的行，需要时取消注释。

---

## 5. 本地 Windows vs 远程 Linux 的区别

| | 本地 Windows | 远程 Linux |
|---|---|---|
| Python 安装 | 官网下载 exe | `uv python install 3.12` |
| GPU 支持 | 自动（NVIDIA 驱动已装） | 需要 CUDA toolkit 和驱动 |
| 路径分隔符 | `\` | `/` |
| 虚拟环境激活 | `.venv\Scripts\activate` | `source .venv/bin/activate` |
| 代理 | 可能需要（Clash） | 一般不需要 |
| 文件传输 | — | `scp` / `rsync` / VS Code Remote SSH |

---

## 6. Docker 方案（一步到位）

如果服务器装了 Docker + NVIDIA Container Toolkit，你可以完全跳过手动装依赖：

```bash
# 本地写好 Dockerfile → 推到服务器 → 一条命令跑起来
docker compose up -d
```

Dockerfile 里已经锁死了 Python 版本、CUDA 版本、PyTorch 版本，不需要每次重装。详见 Lesson 07。

---

## 7. 快速参考

```bash
# --- 新机器初始化（一次性） ---
curl -LsSf https://astral.sh/uv/install.sh | sh   # 装 uv
uv python install 3.12                              # 装 Python
git config --global user.name "dogdogw"              # 配 git
ssh-keygen -t ed25519                                # 配 SSH

# --- 每个项目（每次 clone 后） ---
git clone <repo>
cd <repo>
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# --- 日常 ---
uv pip install <新包>              # 装新包
uv pip install -r requirements.txt # 同步依赖
python -c "import torch; print(torch.cuda.is_available())"  # 检查 GPU
```
