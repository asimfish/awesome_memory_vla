# LongBench: Evaluating Robotic Manipulation Policies on Real-World Long-Horizon Tasks

> **arXiv 2604.16788** · arXiv 2026 · 提交 2026-04-18 · 分类 `bench` / 记忆依赖操作的基准
> *Xueyao Chen, Jingkai Jia, Tong Yang, Yibo Fu, Wei Li, Wenqiang Zhang*
> [arXiv](https://arxiv.org/abs/2604.16788) · [PDF](https://arxiv.org/pdf/2604.16788)

## 一句话定位

真机 1000+ 回合长时程基准，把任务分成全可观（考执行鲁棒性）与上下文依赖（考歧义推理）两类，发现记忆方法并不稳定地改善上下文难度。

## 与核心论文的关系

所属家族「记忆依赖操作的基准」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Robotic manipulation policies often degrade over extended horizons, yet existing benchmarks provide limited insight into why such failures occur. Most prior benchmarks are either simulation-based or report aggregate success, making it difficult to disentangle the distinct sources of temporal difficulty in real-world execution. We introduce LongBench, a real-world benchmark for evaluating long-horizon manipulation. LongBench consists of over 1,000 real-world episodes, covering two complementary regimes: Context-Independent (fully observable) and Context-Dependent (ambiguity-driven). By organizing tasks into capability- and ambiguity-specific subsets, LongBench enables mechanism-aware evaluation of execution robustness, temporal consistency, and context-dependent reasoning. Evaluating six state-of-the-art policies reveals that long-horizon performance is not governed by a single factor. We observe that performance in fully observable settings is more strongly associated with execution robustness, while contextual difficulty varies across tasks and is not consistently improved by memory-based methods. We hope that LongBench serves as a useful benchmark for studying long-horizon manipulation and for developing policies with stronger robustness across both execution and contextual challenges.
