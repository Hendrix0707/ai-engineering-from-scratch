# GPU Setup & Cloud
> GPU 配置与云计算

> Training on CPU is fine for learning. Training for real needs a GPU.
> 在 CPU 上训练对学习来说是够用的。真要训练模型，你得有 GPU。

**Type:** Build
> **类型：** 构建

**Languages:** Python
> **语言：** Python

**Prerequisites:** Phase 0, Lesson 01
> **前置课程：** Phase 0, Lesson 01

**Time:** ~45 minutes
> **时间：** ~45 分钟

## Learning Objectives
> 学习目标

- Verify local GPU availability using `nvidia-smi` and PyTorch's CUDA API
> 使用 `nvidia-smi` 和 PyTorch 的 CUDA API 验证本地 GPU 是否可用
- Configure Google Colab with a T4 GPU for free cloud-based experiments
> 配置 Google Colab 使用 T4 GPU，免费进行云端实验
- Benchmark matrix multiplication on CPU vs GPU and measure the speedup
> 对 CPU 和 GPU 的矩阵乘法进行基准测试，测量加速比
- Estimate the largest model that fits in your VRAM using the fp16 rule of thumb
> 用 fp16 经验法则估算你的显存能装下的最大模型

## The Problem
> 问题

Most lessons in phases 1-3 run fine on CPU. But once you start training CNNs, transformers, or LLMs (phases 4+), you need GPU acceleration. A training run that takes 8 hours on CPU takes 10 minutes on GPU.
> Phase 1-3 的大部分课程在 CPU 上就能跑。但一旦你开始训练 CNN、Transformer 或 LLM（Phase 4+），就需要 GPU 加速。CPU 上跑 8 小时的训练，GPU 上只需要 10 分钟。

You have three options: local GPU, cloud GPU, or Google Colab (free).
> 你有三种选择：本地 GPU、云 GPU、或者 Google Colab（免费）。

## The Concept
> 概念

```
Your options:
> 你的选择：

1. Local NVIDIA GPU
   Cost: $0 (you already have it)
   Setup: Install CUDA + cuDNN
   Best for: Regular use, large datasets
> 1. 本地 NVIDIA GPU
>    费用：$0（你已经有了）
>    配置：安装 CUDA + cuDNN
>    最适合：日常使用、大数据集

2. Google Colab (free tier)
   Cost: $0
   Setup: None
   Best for: Quick experiments, no GPU at home
> 2. Google Colab（免费版）
>    费用：$0
>    配置：无需配置
>    最适合：快速实验、家里没 GPU

3. Cloud GPU (Lambda, RunPod, Vast.ai)
   Cost: $0.20-2.00/hr
   Setup: SSH + install
   Best for: Serious training, large models
> 3. 云 GPU（Lambda, RunPod, Vast.ai）
>    费用：$0.20-2.00/小时
>    配置：SSH + 安装
>    最适合：大规模训练、大模型
```

## Build It
> 从零构建

### Option 1: Local NVIDIA GPU
> 方案 1：本地 NVIDIA GPU

Check if you have one:
> 检查你有没有：

```bash
nvidia-smi
```

Install PyTorch with CUDA:
> 安装带 CUDA 的 PyTorch：

```python
import torch

print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
```

### Option 2: Google Colab
> 方案 2：Google Colab

1. Go to [colab.research.google.com](https://colab.research.google.com)
> 打开 [colab.research.google.com](https://colab.research.google.com)
2. Runtime > Change runtime type > T4 GPU
> 运行时 > 更改运行时类型 > T4 GPU
3. Run `!nvidia-smi` to verify
> 运行 `!nvidia-smi` 验证

Upload notebooks from this course directly to Colab.
> 把本课程的 notebook 直接上传到 Colab 即可运行。

### Option 3: Cloud GPU
> 方案 3：云 GPU

For Lambda Labs, RunPod, or Vast.ai:
> 适用于 Lambda Labs、RunPod 或 Vast.ai：

```bash
ssh user@your-gpu-instance

pip install torch torchvision torchaudio
python -c "import torch; print(torch.cuda.get_device_name(0))"
```

### No GPU? No problem.
> 没 GPU？没问题。

Most lessons work on CPU. The ones that need GPU will say so and include Colab links.
> 大多数课程在 CPU 上就能跑。需要 GPU 的课程会明确说明，并提供 Colab 链接。

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using: {device}")
```

## Build It: GPU vs CPU benchmark
> 从零构建：GPU vs CPU 基准测试

```python
import torch
import time

size = 5000

a_cpu = torch.randn(size, size)
b_cpu = torch.randn(size, size)

start = time.time()
c_cpu = a_cpu @ b_cpu
cpu_time = time.time() - start
print(f"CPU: {cpu_time:.3f}s")

if torch.cuda.is_available():
    a_gpu = a_cpu.to("cuda")
    b_gpu = b_cpu.to("cuda")

    torch.cuda.synchronize()  # 等 GPU 算完再计时
    start = time.time()
    c_gpu = a_gpu @ b_gpu
    torch.cuda.synchronize()
    gpu_time = time.time() - start
    print(f"GPU: {gpu_time:.3f}s")
    print(f"Speedup: {cpu_time / gpu_time:.0f}x")
```

## Exercises
> 练习

1. Run the benchmark above and compare CPU vs GPU times
> 运行上面的基准测试，比较 CPU 和 GPU 的时间
2. If you don't have a GPU, run it on Google Colab and compare
> 如果没有 GPU，在 Google Colab 上跑并比较
3. Check how much GPU memory you have and estimate the largest model you can fit (rule of thumb: 2 bytes per parameter for fp16)
> 查看你有多少 GPU 显存，估算能装下多大的模型（经验法则：fp16 下每参数 2 字节）

## Key Terms
> 关键术语

| Term | What people say | What it actually means |
> | 术语 | 人们常怎么说 | 实际含义 |
|------|----------------|----------------------|
| CUDA | "GPU programming" | NVIDIA's parallel computing platform that lets you run code on the GPU |
> | CUDA | "GPU 编程" | NVIDIA 的并行计算平台，让你能在 GPU 上运行代码 |
| VRAM | "GPU memory" | Video RAM on the GPU, separate from system RAM. Limits model size. |
> | VRAM | "GPU 显存" | GPU 上的专用内存，和系统内存是分开的。限制了模型大小 |
| fp16 | "Half precision" | 16-bit floating point, uses half the memory of fp32 with minimal accuracy loss |
> | fp16 | "半精度" | 16 位浮点数，内存占用是 fp32 的一半，精度损失很小 |
| Tensor Core | "Fast matrix hardware" | Specialized GPU cores for matrix multiplication, 4-8x faster than regular cores |
> | Tensor Core | "快速矩阵硬件" | GPU 中专用于矩阵乘法的核心，比普通核心快 4-8 倍 |
