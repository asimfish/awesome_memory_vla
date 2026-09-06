# Learning Memory Mechanisms for Decision Making through Demonstrations

> **arXiv 2411.07954** · arXiv 2024 · 提交 2024-11-12 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *William Yue, Bo Liu, Peter Stone*
> [arXiv](https://arxiv.org/abs/2411.07954) · [PDF](https://arxiv.org/pdf/2411.07954)

## 一句话定位

把「第 p 步事件在第 q 步被回忆」作为记忆依赖对加入演示，AttentionTuner 用它监督 Transformer 的注意力。

## 与核心论文的关系

所属家族「latent 状态、循环与槽记忆（TRACE 一族）」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

In Partially Observable Markov Decision Processes, integrating an agent's history into memory poses a significant challenge for decision-making. Traditional imitation learning, relying on observation-action pairs for expert demonstrations, fails to capture the expert's memory mechanisms used in decision-making. To capture memory processes as demonstrations, we introduce the concept of memory dependency pairs $(p, q)$ indicating that events at time $p$ are recalled for decision-making at time $q$. We introduce AttentionTuner to leverage memory dependency pairs in Transformers and find significant improvements across several tasks compared to standard Transformers when evaluated on Memory Gym and the Long-term Memory Benchmark. Code is available at https://github.com/WilliamYue37/AttentionTuner.
