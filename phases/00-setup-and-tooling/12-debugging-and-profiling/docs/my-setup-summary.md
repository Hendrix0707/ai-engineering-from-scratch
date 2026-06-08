# Lesson 12 完成总结：Debugging and Profiling

## 学了什么

AI 代码的 bug 和普通代码不同——训练跑了 8 小时不报错，但模型什么都没学到。这节课给了你一套工具箱来提前发现这些问题。

## 工具箱速查

### 10 个演示，跑一遍就懂

```bash
python phases/00-setup-and-tooling/12-debugging-and-profiling/code/debug_tools.py
```

| # | 工具 | 干什么用 |
|---|------|---------|
| 1 | `debug_print()` | 一次看清张量的形状、类型、设备、数值范围、有没有 NaN |
| 2 | `Timer` | 用 `with Timer("名字"):` 包裹代码，自动计时 |
| 3 | `tracemalloc` | 追踪 CPU 内存分配，找出哪行代码吃内存最多 |
| 4 | `check_shapes()` | 遍历模型每层，打印输入→输出形状，揪出维度不匹配 |
| 5 | `detect_nan()` | 发现 NaN loss 后，进一步找哪个参数梯度出了 NaN/Inf |
| 6 | `check_devices()` | 检查张量是否和模型在同一设备（CPU/GPU），揪出混放 |
| 7 | `check_gradient_health()` | 梯度总范数 + 异常大的梯度 + 零梯度警告 |
| 8 | GPU memory | 查看已分配 vs 缓存的显存，演示创建/清理大张量 |
| 9 | `logging` | 替代 print，有时间戳、级别、写文件（凌晨 3 点训练挂了你需要日志） |
| 10 | `breakpoint()` | 条件断点：`if loss > 100: breakpoint()`，只在出问题时停 |

### 调试流程（5 步）

```
训练前 → check_shapes() 验证维度
前 10 步 → debug_print() 确认没 NaN
训练中 → logger + TensorBoard 看曲线
出问题 → breakpoint() 交互检查
性能问题 → Timer 对比数据加载/前向/反向
```

## 四大常见 AI Bug

| Bug | 现象 | 第一招 |
|-----|------|--------|
| **形状不匹配** | RuntimeError | `check_shapes()` 跑一遍 |
| **NaN Loss** | loss = nan | 学习率降 10 倍 + 加梯度裁剪 |
| **数据泄漏** | 测试集 99% 第一 epoch | 检查 train/test 是否有重叠 ID |
| **设备错误** | 报错或慢得异常 | `check_devices()` 揪出放错地方的量 |

## OOM 处理顺序（你的 RTX 3060 只有 6GB 显存）

```
1. batch size 减半（永远先试这个）
2. torch.cuda.empty_cache() 清缓存
3. del 大张量 + empty_cache()
4. 开混合精度 torch.cuda.amp（显存减半）
5. 梯度检查点（非常深的模型才用）
```

## 你现在能用吗？

**大部分工具现在就能用。** `debug_print`、`check_shapes`、`detect_nan`、`Timer` 这些是你写任何 PyTorch 代码的标配。TensorBoard 和 VS Code 调试器等实际跑训练时再配。

## 建议

**跑一遍 `debug_tools.py`**，看 10 个演示的输出。然后把 `check_shapes`、`debug_print`、`detect_nan` 这三个函数复制到你写训练代码的项目里——它们是你在训练中第一个小时就能用上的东西。
