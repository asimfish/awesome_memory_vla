# BridgeVLA++: A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework for 3D Manipulation

> **arXiv 2608.05042** · arXiv 2026 · 提交 2026-08-05 · 分类 `dense` / 稠密与压缩的视觉历史
> *Peiyan Li, Yuze Zhu, Yixiang Chen, Qisen Ma, Yuan Xu, Jiabing Yang, He Guan, Yan Huang, Hongtao Wu, Xiao Ma, Tao Kong, Liang Wang, Tieniu Tan*
> [arXiv](https://arxiv.org/abs/2608.05042) · [PDF](https://arxiv.org/pdf/2608.05042)

## 一句话定位

3D VLA（点云→多视角热图）加统一时空记忆，在两个记忆依赖基准上取得 SOTA 且不损数据效率。

## 与核心论文的关系

所属家族「稠密与压缩的视觉历史」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Leveraging pre-trained vision-language models (VLMs) to construct vision-language-action (VLA) models has emerged as a promising paradigm for 3D robot manipulation. However, existing 3D VLA methods remain data-hungry, exhibit limited generalization under distribution shifts, and lack explicit memory of past observations. These limitations hinder their application to data-scarce, open-world, and memory-dependent manipulation scenarios. Our previous work, BridgeVLA, improves data efficiency and generalization by preserving the input--output alignment of a pre-trained VLM during 3D action learning: raw point clouds are projected into multi-view images, and intermediate heatmaps are predicted before generating robot actions. In this work, we develop BridgeVLA++ by equipping BridgeVLA with a unified spatio-temporal memory architecture that models persistent spatial context and temporal interaction history. The resulting memory-augmented framework can reason over observation histories while preserving BridgeVLA's data efficiency and generalization capabilities. Extensive experiments show that our framework achieves strong performance on spatial manipulation tasks while exhibiting robust generalization. BridgeVLA++ further achieves state-of-the-art performance on two challenging memory-dependent manipulation benchmarks without sacrificing the data efficiency and generalization of the original BridgeVLA. In addition, BridgeVLA++ performs effectively in bimanual manipulation settings and is validated on an additional real-world robotic platform, demonstrating its scalability across tasks, environments, and robotic platforms. These results establish BridgeVLA++ as a unified 3D vision-language-action framework that simultaneously supports data-efficient learning, robust generalization, and effective memory-aware robot manipulation. Project website: https://bridgevla-plus.github.io/.

*arXiv comment: This work has been submitted to the IEEE TPAMI for possible publication. Copyright may be transferred without notice, after which this version may no longer be accessible*
