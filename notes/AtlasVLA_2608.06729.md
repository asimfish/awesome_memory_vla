# AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models

> **arXiv 2608.06729** · arXiv 2026 · 提交 2026-08-07 · 分类 `dense` / 稠密与压缩的视觉历史
> *Guiyu Zhao, Longteng Guo, Yanghong Mei, Zilin Zhu, Yu Zhang, Bin Cao, Mingming Yu, Xingjian He, Jie Jiang, Jing Liu*
> [arXiv](https://arxiv.org/abs/2608.06729) · [PDF](https://arxiv.org/pdf/2608.06729)

## 一句话定位

持久世界-自我状态：4D 体素哈希空间记忆解决单腕相机的视野盲区 + 自我工作状态追踪任务进度；仅腕相机即超多视角基线（LIBERO-Long +9.4，真机 +17.5）。

## 与核心论文的关系

所属家族「稠密与压缩的视觉历史」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

While Vision-Language-Action (VLA) models have advanced embodied AI, their fundamentally reactive paradigm severely limits performance in partially observable and long-horizon tasks. When restricted to a single wrist-mounted camera, they inevitably suffer from perception forgetting as objects exit the field of view, and temporal task-progress forgetting} during multi-step execution. To overcome these bottlenecks, we propose AtlasVLA, a novel framework that transitions from direct reactive manipulation to proactive reasoning through a persistent world-ego state. AtlasVLA features a dual-memory architecture: a 4D Persistent World State Memory that lifts transient 2D observations into a globally updated, voxel-hashed spatial state to resolve visual blind spots, and an Ego-Working State Memory that tracks historical ego state and task progress. By conditioning a diffusion transformer (DiT) on this joint World-Ego state, AtlasVLA enables robust spatial reasoning. Extensive evaluations across LIBERO, RLBench, and real-world benchmarks demonstrate that AtlasVLA achieves state-of-the-art performance using solely a wrist camera. Remarkably, it decisively outperforms multi-view baselines, yielding absolute success rate improvements of 9.4% on LIBERO-Long and 17.5% in real-world long-horizon tasks.
