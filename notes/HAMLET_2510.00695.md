# HAMLET: Switch your Vision-Language-Action Model into a History-Aware Policy

> **arXiv 2510.00695** · arXiv 2025 · 提交 2025-10-01 · 分类 `dense` / 稠密与压缩的视觉历史
> *Myungkyu Koo, Daewon Choi, Taeyoung Kim, Kyungmin Lee, Changyeon Kim, Younggyo Seo, Jinwoo Shin*
> [arXiv](https://arxiv.org/abs/2510.00695) · [PDF](https://arxiv.org/pdf/2510.00695)

## 一句话定位

moment token（时间对比初始化）+ 轻量记忆模块，把 GR00T N1.5 变成历史感知策略；真机历史依赖任务 76.4%（+47.2）。

## 与核心论文的关系

所属家族「稠密与压缩的视觉历史」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Inherently, robotic manipulation tasks are history-dependent: leveraging past context could be beneficial. However, most existing Vision-Language-Action models (VLAs) have been designed without considering this aspect, i.e., they rely solely on the current observation, ignoring preceding context. In this paper, we propose HAMLET, a scalable framework to adapt VLAs to attend to the historical context during action prediction. Specifically, we introduce moment tokens that compactly encode perceptual information at each timestep. Their representations are initialized with time-contrastive learning, allowing them to better capture temporally distinctive aspects. Next, we employ a lightweight memory module that integrates the moment tokens across past timesteps into memory features, which are then leveraged for action prediction. Through empirical evaluation, we show that HAMLET successfully transforms a state-of-the-art VLA into a history-aware policy, especially demonstrating significant improvements on long-horizon tasks that require historical context. In particular, on top of GR00T N1.5, HAMLET achieves an average success rate of 76.4% on history-dependent real-world tasks, surpassing the baseline performance by 47.2%. Furthermore, HAMLET pushes prior art performance from 64.1% to 66.4% on RoboCasa Kitchen (100-demo setup) and from 95.6% to 97.7% on LIBERO, highlighting its effectiveness even under generic robot-manipulation benchmarks.

*arXiv comment: ICLR 2026. Project page: https://myungkyukoo.github.io/hamlet/*
