# CycleManip: Enabling Cyclic Task Manipulation via Effective Historical Perception and Understanding

> **arXiv 2512.01022** · arXiv 2025 · 提交 2025-11-30 · 分类 `dense` / 稠密与压缩的视觉历史
> *Yi-Lin Wei, Haoran Liao, Yuhao Lin, Pengyue Wang, Zhizhao Liang, Guiliang Liu, Wei-Shi Zheng*
> [arXiv](https://arxiv.org/abs/2512.01022) · [PDF](https://arxiv.org/pdf/2512.01022)

## 一句话定位

周期性任务（摇瓶、敲钉）需要知道做了几次：代价感知的历史采样 + 多任务学习，附周期任务基准。

## 与核心论文的关系

所属家族「稠密与压缩的视觉历史」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

In this paper, we explore an important yet underexplored task in robot manipulation: cycle-based manipulation, where robots need to perform cyclic or repetitive actions with an expected terminal time. These tasks are crucial in daily life, such as shaking a bottle or knocking a nail. However, few prior works have explored this task, leading to two main challenges: 1) the imitation methods often fail to complete these tasks within the expected terminal time due to the ineffective utilization of history; 2) the absence of a benchmark with sufficient data and automatic evaluation tools hinders development of effective solutions in this area. To address these challenges, we first propose the CycleManip framework to achieve cycle-based task manipulation in an end-to-end imitation manner without requiring any extra models, hierarchical structure or significant computational overhead. The core insight is to enhance effective history perception by a cost-aware sampling strategy and to improve historical understanding by multi-task learning. Second, we introduce a cycle-based task manipulation benchmark, which provides diverse cycle-based tasks, and an automatic evaluation method. Extensive experiments conducted in both simulation and real-world settings demonstrate that our method achieves high success rates in cycle-based task manipulation. The results further show strong adaptability performance in general manipulation, and the plug-and-play ability on imitation policies such as Vision-Language-Action (VLA) models. Moreover, the results show that our approach can be applied across diverse robotic platforms, including bi-arm grippers, dexterous hands, and humanoid robots.

*arXiv comment: Accepted by CVPR2026. Project page: https://isee-laboratory.github.io/CycleManip/*
