# RMBench: Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design

> **arXiv 2603.01229** · arXiv 2026 · 提交 2026-03-01 · 分类 `bench` / 记忆依赖操作的基准
> *Tianxing Chen, Yuran Wang, Mingleyang Li, Yan Qin, Hao Shi, Zixuan Li, Yifan Hu, Yingsheng Zhang, Kaixuan Wang, Yue Chen, Hongcheng Wang, Junjie Wang, Tianhang Yang, Renjing Xu, Ruihai Wu, Yao Mu, Yaodong Yang, Hao Dong, Ping Luo*
> [arXiv](https://arxiv.org/abs/2603.01229) · [PDF](https://arxiv.org/pdf/2603.01229)

## 一句话定位

9 任务记忆依赖操作基准（RoboTwin 2.0）+ 模块化记忆策略 Mem-0；EventVLA 仅锚帧即 67.8%，说明其记忆需求偏浅。

## 与核心论文的关系

所属家族「记忆依赖操作的基准」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Robotic manipulation policies have made rapid progress in recent years, yet most existing approaches give limited consideration to memory capabilities. Consequently, they struggle to solve tasks that require reasoning over historical observations and maintaining task-relevant information over time, which are common requirements in real-world manipulation scenarios. Although several memory-aware policies have been proposed, systematic evaluation of memory-dependent manipulation remains underexplored, and the relationship between architectural design choices and memory performance is still not well understood. To address this gap, we introduce RMBench, a simulation benchmark comprising 9 manipulation tasks that span multiple levels of memory complexity, enabling systematic evaluation of policy memory capabilities. We further propose Mem-0, a modular manipulation policy with explicit memory components designed to support controlled ablation studies. Through extensive simulation and real-world experiments, we identify memory-related limitations in existing policies and provide empirical insights into how architectural design choices influence memory performance. The website is available at https://rmbench.github.io/.

*arXiv comment: website: https://rmbench.github.io/*
