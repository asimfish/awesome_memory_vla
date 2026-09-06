# UniMem: Unifying Multimodal Memory and Control for Vision-Language-Action Models

> **arXiv 2608.22869** · arXiv 2026 · 提交 2026-08-24 · 分类 `event` / 事件与关键帧记忆（EventVLA 一族）
> *Lars Osterberg, Maggie Wang, Mac Schwager*
> [arXiv](https://arxiv.org/abs/2608.22869) · [PDF](https://arxiv.org/pdf/2608.22869)

## 一句话定位

单骨干统一多模态记忆与控制：事件分类器决定何时更新、关键帧编码器做密集空间记忆、关键帧缓存降开销；仿真 93.4 vs 固定间隔采样 68.2，真机 80.0 vs 分层基线 43.5。

## 与核心论文的关系

所属家族「事件与关键帧记忆（EventVLA 一族）」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

While Vision-Language-Action (VLA) models have leveraged internet-scale pretraining and task-focused finetuning to achieve strong performance on long-horizon tasks, they often struggle with non-Markovian tasks that require memory. Existing approaches to memory typically involve additional Vision-Language-Models (VLMs) for long-term memory management, introducing a memory bottleneck and a fractured training pipeline. Conditioning on multiple historical frames can provide the VLA with access to more descriptive features of past scenes, but can degrade performance if frames are chosen at arbitrary, fixed intervals. To address these limitations, we present UniMem, a framework that unifies high-level, multimodal memory and low-level control under one backbone. UniMem employs an event classifier for memory updates, a keyframe encoder for dense spatial memory, and a keyframe caching technique to minimize overhead during policy rollouts. We evaluate UniMem across five simulation and four hardware tasks targeting sequential and spatial memory, demonstrating that our unified, single-model system outperforms fixed-interval image sampling baselines (93.4% vs. 68.2%) in simulation and hierarchical baselines (80.0% vs. 43.5%) in hardware, while offering faster inference and a simple training pipeline for easy adoption. Project website: https://losterberg3.github.io/unimem-vla/
