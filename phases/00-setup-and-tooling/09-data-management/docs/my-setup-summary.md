# Lesson 09 完成总结：Data Management

## 学了什么

Lesson 09 教的是 AI 项目中数据的标准处理方式——从加载、转换、划分到版本管理。

### 核心工具：Hugging Face `datasets` 库

| 操作 | 代码 | 用途 |
|------|------|------|
| 加载数据集 | `load_dataset("imdb")` | 从 HF Hub 下载/缓存数据集，一行搞定 |
| 流式读取 | `load_dataset("...", streaming=True)` | 数据集太大装不进硬盘时，逐行处理 |
| 格式转换 | `.to_csv()` / `.to_parquet()` | 导出为不同格式 |
| 数据划分 | `.train_test_split(test_size=0.2, seed=42)` | 可复现的训练/验证/测试集划分 |

### 格式对比（记住就行）

- **Parquet** — 存储最优，文件小、读取快 → 存硬盘用这个
- **Arrow** — 内存中处理，datasets 库默认用这个 → 不用管
- **CSV / JSON** — 人类可读、API 交换用 → 仅用于查看和分享

### 大文件管理三方案

| 方案 | 你现在需要吗？ |
|------|:--:|
| `.gitignore` | **用这个**。模型文件和数据加进 gitignore 就行 |
| Git LFS | 不需要。团队共享模型权重时才用 |
| DVC | 不需要。跨机器精确复现实验时才用 |

### 代码产出

- `code/data_utils.py` — 封装了 7 个常用函数（加载、流式、转换、划分、下载模型、缓存信息、数据集指纹），可直接复用

---

## 实际判断：现在需要深入学吗？

**需要学 `datasets` 库的基本用法**（load、split、stream），因为后续课程训练模型都要用它加载数据。但 DVC、Git LFS、云存储目前不需要——你是单人单机，`.gitignore` 够了。

**建议现在做的：**
1. 跑一下 `python code/data_utils.py` 看效果
2. 了解 `load_dataset()` 和 `train_test_split()` 的基本写法
3. 知道 Parquet 比 CSV 好就行

**可以跳过/以后再说：**
- DVC（等到需要多台机器复现实验时）
- Git LFS（等到团队协作共享模型时）
- 云存储 S3/GCS（等到在远程 GPU 上微调时）
