# Rethinking Bimanual Robotic Manipulation: Learning with Decoupled Interaction Framework

> **arXiv 2503.09186** · ICCV 2025 · 提交 2025-03-12 · 分类 `multi` / 多机器人协作与搭档记忆（SAI 一族）
> *Jian-Jian Jiang, Xiao-Ming Wu, Yi-Xiang He, Ling-An Zeng, Yi-Lin Wei, Dandan Zhang, Wei-Shi Zheng*
> [arXiv](https://arxiv.org/abs/2503.09186) · [PDF](https://arxiv.org/pdf/2503.09186)

## 一句话定位

每臂独立模型 + 选择性交互模块的解耦双臂框架，RoboTwin +23.5%，可扩展到多智能体；单机版的「去中心化 + 局部交互」。

## 与核心论文的关系

所属家族「多机器人协作与搭档记忆（SAI 一族）」，对照阅读：[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Bimanual robotic manipulation is an emerging and critical topic in the robotics community. Previous works primarily rely on integrated control models that take the perceptions and states of both arms as inputs to directly predict their actions. However, we think bimanual manipulation involves not only coordinated tasks but also various uncoordinated tasks that do not require explicit cooperation during execution, such as grasping objects with the closest hand, which integrated control frameworks ignore to consider due to their enforced cooperation in the early inputs. In this paper, we propose a novel decoupled interaction framework that considers the characteristics of different tasks in bimanual manipulation. The key insight of our framework is to assign an independent model to each arm to enhance the learning of uncoordinated tasks, while introducing a selective interaction module that adaptively learns weights from its own arm to improve the learning of coordinated tasks. Extensive experiments on seven tasks in the RoboTwin dataset demonstrate that: (1) Our framework achieves outstanding performance, with a 23.5% boost over the SOTA method. (2) Our framework is flexible and can be seamlessly integrated into existing methods. (3) Our framework can be effectively extended to multi-agent manipulation tasks, achieving a 28% boost over the integrated control SOTA. (4) The performance boost stems from the decoupled design itself, surpassing the SOTA by 16.5% in success rate with only 1/6 of the model size.

*arXiv comment: 15 pages, 8 figures*
