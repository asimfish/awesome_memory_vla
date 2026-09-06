# RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark

> **arXiv 2605.10921** · arXiv 2026 · 提交 2026-05-11 · 分类 `bench` / 记忆依赖操作的基准
> *Huashuo Lei, Wenxuan Song, Huarui Zhang, Jieyuan Pei, Jiayi Chen, Haodong Yan, Han Zhao, Pengxiang Ding, Zhipeng Zhang, Lida Huang, Donglin Wang, Yan Wang, Haoang Li*
> [arXiv](https://arxiv.org/abs/2605.10921) · [PDF](https://arxiv.org/pdf/2605.10921)

## 一句话定位

26 任务、平均 >1000 步、68.9% 子任务依赖记忆的大规模基准，VLM 生成子任务并自带关键帧标注；配套双系统策略 PrediMem（近期缓冲 + 关键帧缓冲 + 预测编码头）。

## 与核心论文的关系

所属家族「记忆依赖操作的基准」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Memory is a critical component of robotic intelligence, as robots must rely on past observations and actions to accomplish long-horizon tasks in partially observable environments. However, existing robotic memory benchmarks still lack multimodal annotations for memory formation, provide limited task coverage and structural complexity, and remain restricted to simulation without real-world evaluation. We address this gap with RoboMemArena, a large-scale benchmark of 26 tasks, with average trajectory lengths exceeding 1,000 steps per task and 68.9% of subtasks being memory-dependent. The generation pipeline leverages a vision-language model (VLM) to design and compose subtasks, generates full trajectories through atomic functions, and provides memory-related annotations, including subtask instructions and native keyframe annotations, while paired real-world memory tasks support physical evaluation. We further design PrediMem, a dual-system VLA in which a high-level VLM planner manages a memory bank with recent and keyframe buffers and uses a predictive coding head to improve sensitivity to task dynamics. Extensive experiments on RoboMemArena show that PrediMem outperforms all baselines and provides insights into memory management, model architecture, and scaling laws for complex memory systems.

*arXiv comment: Project website: https://robomemarena.github.io*
