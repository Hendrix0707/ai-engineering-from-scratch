# data_utils.py — 数据加载和缓存工具
# 基于 Hugging Face datasets 库，封装了 AI 项目中最常用的数据操作

import os
import sys
import json
import hashlib
from pathlib import Path

try:
    from datasets import load_dataset, Dataset
except ImportError:
    print("Install the datasets library: pip install datasets")
    sys.exit(1)

try:
    from huggingface_hub import hf_hub_download
except ImportError:
    print("Install huggingface_hub: pip install huggingface_hub")
    sys.exit(1)

# HF 数据集默认缓存路径
CACHE_DIR = Path.home() / ".cache" / "huggingface" / "datasets"


def load_and_inspect(dataset_name: str, config: str = None, split: str = "train"):
    """加载数据集并查看基本信息（列名、特征类型、样本数、第一条数据）"""
    kwargs = {"path": dataset_name}
    if config:
        kwargs["name"] = config  # 有些数据集需要 config，如 glue/mrpc
    if split:
        kwargs["split"] = split  # 指定划分：train / test / validation

    ds = load_dataset(**kwargs)
    print(f"Dataset: {dataset_name}")
    print(f"  Split: {split}")
    print(f"  Rows: {len(ds)}")
    print(f"  Columns: {ds.column_names}")
    print(f"  Features: {ds.features}")
    print(f"  First row: {ds[0]}")
    return ds


def stream_dataset(dataset_name: str, config: str = None, max_rows: int = 5):
    """流式读取数据集 — 适合超大文件，逐行处理不占满内存"""
    kwargs = {"path": dataset_name, "split": "train", "streaming": True}
    if config:
        kwargs["name"] = config

    ds = load_dataset(**kwargs)
    rows = []
    for i, example in enumerate(ds):
        rows.append(example)
        if i >= max_rows - 1:
            break  # 只取指定行数，不会无限下载

    print(f"Streamed {len(rows)} rows from {dataset_name}")
    return rows


def convert_format(ds, output_dir: str, name: str):
    """将数据集导出为 CSV / JSON / Parquet 三种格式并对比文件大小"""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    csv_path = output_path / f"{name}.csv"
    json_path = output_path / f"{name}.json"
    parquet_path = output_path / f"{name}.parquet"

    ds.to_csv(str(csv_path))
    ds.to_json(str(json_path))
    ds.to_parquet(str(parquet_path))

    csv_size = csv_path.stat().st_size
    json_size = json_path.stat().st_size
    parquet_size = parquet_path.stat().st_size

    print(f"Format comparison for {name}:")
    print(f"  CSV:     {csv_size:>10,} bytes")
    print(f"  JSON:    {json_size:>10,} bytes")
    print(f"  Parquet: {parquet_size:>10,} bytes")
    print(f"  Parquet is {csv_size / parquet_size:.1f}x smaller than CSV")

    return {"csv": csv_path, "json": json_path, "parquet": parquet_path}


def make_splits(ds, train_ratio: float = 0.8, val_ratio: float = 0.1, seed: int = 42):
    """用固定 seed 划分训练/验证/测试集，保证每次结果一致"""
    test_ratio = 1.0 - train_ratio - val_ratio
    assert test_ratio > 0, "train_ratio + val_ratio must be less than 1.0"

    # 第一步：按 80%/20% 分出训练集和其余部分
    test_size = val_ratio + test_ratio
    split1 = ds.train_test_split(test_size=test_size, seed=seed)
    train_ds = split1["train"]

    # 第二步：把剩下的 20% 再分成验证集和测试集各半
    val_fraction = val_ratio / test_size  # 0.1 / 0.2 = 0.5，即验证集占剩余的一半
    split2 = split1["test"].train_test_split(test_size=(1.0 - val_fraction), seed=seed)
    val_ds = split2["train"]
    test_ds = split2["test"]

    total = len(train_ds) + len(val_ds) + len(test_ds)
    print(f"Splits (seed={seed}):")
    print(f"  Train: {len(train_ds):>6} ({len(train_ds)/total:.1%})")
    print(f"  Val:   {len(val_ds):>6} ({len(val_ds)/total:.1%})")
    print(f"  Test:  {len(test_ds):>6} ({len(test_ds)/total:.1%})")

    return {"train": train_ds, "val": val_ds, "test": test_ds}


def download_model_file(repo_id: str, filename: str):
    """从 Hugging Face Hub 下载单个模型文件并缓存到本地"""
    path = hf_hub_download(repo_id=repo_id, filename=filename)
    size = Path(path).stat().st_size
    print(f"Downloaded {filename} from {repo_id}")
    print(f"  Path: {path}")
    print(f"  Size: {size:,} bytes")
    return path


def cache_summary():
    """查看 HF 数据集缓存的磁盘占用情况"""
    cache_path = CACHE_DIR
    if not cache_path.exists():
        print("No HF cache found yet.")
        return

    total_size = 0
    file_count = 0
    for f in cache_path.rglob("*"):
        if f.is_file():
            total_size += f.stat().st_size
            file_count += 1

    print(f"HF Dataset Cache: {cache_path}")
    print(f"  Files: {file_count}")
    print(f"  Total size: {total_size / (1024 * 1024):.1f} MB")


def load_from_parquet(path: str):
    """从 Parquet 文件反向加载回 Dataset 对象"""
    ds = Dataset.from_parquet(path)
    print(f"Loaded {len(ds)} rows from {path}")
    return ds


def load_from_csv(path: str):
    """从 CSV 文件反向加载回 Dataset 对象"""
    ds = Dataset.from_csv(path)
    print(f"Loaded {len(ds)} rows from {path}")
    return ds


def load_from_json(path: str):
    """从 JSON 文件反向加载回 Dataset 对象"""
    ds = Dataset.from_json(path)
    print(f"Loaded {len(ds)} rows from {path}")
    return ds


def fingerprint(ds, num_rows: int = 100):
    """取数据集前 N 行的 SHA256 哈希作为"指纹" — 用来验证数据有没有变化"""
    sample = ds.select(range(min(num_rows, len(ds))))
    content = json.dumps([row for row in sample], default=str).encode()
    digest = hashlib.sha256(content).hexdigest()[:16]
    print(f"Dataset fingerprint (first {num_rows} rows): {digest}")
    return digest


# ========== 演示运行 ==========
if __name__ == "__main__":
    print("=" * 60)
    print("Data Management Utility / 数据管理工具")
    print("=" * 60)

    print("\n--- 1. Load and inspect a dataset / 加载并查看数据集 ---")
    ds = load_and_inspect("rotten_tomatoes", split="train")

    print("\n--- 2. Stream a dataset / 流式读取 ---")
    rows = stream_dataset("rotten_tomatoes", max_rows=3)
    for row in rows:
        print(f"  {row['text'][:80]}...")

    print("\n--- 3. Convert formats / 格式转换对比 ---")
    small_ds = ds.select(range(500))  # 只取前 500 条，演示用
    paths = convert_format(small_ds, "/tmp/data_utils_demo", "rotten_tomatoes_sample")

    print("\n--- 4. Create train/val/test splits / 数据划分 ---")
    splits = make_splits(small_ds, train_ratio=0.8, val_ratio=0.1, seed=42)

    print("\n--- 5. Reload from Parquet / 从 Parquet 重新加载 ---")
    reloaded = load_from_parquet(str(paths["parquet"]))
    print(f"  Columns: {reloaded.column_names}")

    print("\n--- 6. Download a model file / 下载模型文件 ---")
    download_model_file("sentence-transformers/all-MiniLM-L6-v2", "config.json")

    print("\n--- 7. Dataset fingerprint / 数据集指纹 ---")
    fingerprint(ds)

    print("\n--- 8. Cache summary / 缓存信息 ---")
    cache_summary()

    print("\n" + "=" * 60)
    print("All checks passed. Your data pipeline is ready.")
    print("=" * 60)
