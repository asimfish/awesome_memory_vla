# Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation

> **arXiv 2401.02117** · CoRL 2024 · 提交 2024-01-04 · 分类 `multi` / 多机器人协作与搭档记忆（SAI 一族）
> *Zipeng Fu, Tony Z. Zhao, Chelsea Finn*
> [arXiv](https://arxiv.org/abs/2401.02117) · [PDF](https://arxiv.org/pdf/2401.02117)

## 一句话定位

低成本全身遥操作的双臂移动操作系统，静态 ALOHA 数据协同训练；SAI 的硬件与任务范式源头之一。

## 与核心论文的关系

所属家族「多机器人协作与搭档记忆（SAI 一族）」，对照阅读：[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Imitation learning from human demonstrations has shown impressive performance in robotics. However, most results focus on table-top manipulation, lacking the mobility and dexterity necessary for generally useful tasks. In this work, we develop a system for imitating mobile manipulation tasks that are bimanual and require whole-body control. We first present Mobile ALOHA, a low-cost and whole-body teleoperation system for data collection. It augments the ALOHA system with a mobile base, and a whole-body teleoperation interface. Using data collected with Mobile ALOHA, we then perform supervised behavior cloning and find that co-training with existing static ALOHA datasets boosts performance on mobile manipulation tasks. With 50 demonstrations for each task, co-training can increase success rates by up to 90%, allowing Mobile ALOHA to autonomously complete complex mobile manipulation tasks such as sauteing and serving a piece of shrimp, opening a two-door wall cabinet to store heavy cooking pots, calling and entering an elevator, and lightly rinsing a used pan using a kitchen faucet. Project website: https://mobile-aloha.github.io

*arXiv comment: Project website: https://mobile-aloha.github.io (Zipeng Fu and Tony Z. Zhao are project co-leads, Chelsea Finn is the advisor)*
