# MemoAct: Atkinson-Shiffrin-Inspired Hierarchical Memory-Augmented Policy for Robotic Manipulation

> **arXiv 2603.18494** · arXiv 2026 · 提交 2026-03-19 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Liufan Tan, Jiale Li, Gangshan Jing*
> [arXiv](https://arxiv.org/abs/2603.18494) · [PDF](https://arxiv.org/pdf/2603.18494)

## 一句话定位

Atkinson-Shiffrin 三层记忆：感觉记忆过滤、无损短期记忆精确追踪状态、压缩长期记忆长期保持；附 MemoryRTBench（RoboTwin 2.0，6 任务）。

## 与核心论文的关系

所属家族「latent 状态、循环与槽记忆（TRACE 一族）」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Memory-augmented robotic policies are essential in handling memory-dependent tasks. However, existing approaches typically rely on simply extending the observation window, struggling to simultaneously achieve precise task-state tracking and robust long-horizon retention. To overcome these challenges, inspired by the Atkinson--Shiffrin memory model, we propose MemoAct, a hierarchical memory-augmented policy that leverages distinct memory tiers to tackle specific bottlenecks. Specifically, sensory memory filters immediate perceptual inputs, lossless short-term memory supports precise task-state tracking, and compressed long-term memory facilitates robust long-horizon retention. To enrich the evaluation landscape, we construct MemoryRTBench based on RoboTwin 2.0, comprising 6 manipulation tasks that systematically evaluate policy memory capabilities across three dimensions: sequential, spatial, and episodic memory. Extensive experiments across simulated and real-world scenarios demonstrate that MemoAct achieves superior performance compared to both existing Markovian baselines and history-aware policies. The project page is available at https://tlf-tlf.github.io/MemoActPage/.
