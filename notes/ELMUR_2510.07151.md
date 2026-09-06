# ELMUR: External Layer Memory with Update/Rewrite for Long-Horizon RL Problems

> **arXiv 2510.07151** · arXiv 2025 · 提交 2025-10-08 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Egor Cherepanov, Alexey K. Kovalev, Aleksandr I. Panov*
> [arXiv](https://arxiv.org/abs/2510.07151) · [PDF](https://arxiv.org/pdf/2510.07151)

## 一句话定位

层内外部记忆 + LRU 更新/重写，有效时程扩展到注意力窗口的 10 万倍；MIKASA-Robo 23 任务中 21 个最好。

## 与核心论文的关系

所属家族「latent 状态、循环与槽记忆（TRACE 一族）」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Real-world robotic agents must act under partial observability and long horizons, where key cues may appear long before they affect decision making. However, most modern approaches rely solely on instantaneous information, without incorporating insights from the past. Standard recurrent or transformer models struggle with retaining and leveraging long-term dependencies: context windows truncate history, while naive memory extensions fail under scale and sparsity. We propose ELMUR (External Layer Memory with Update/Rewrite), a transformer architecture with structured external memory. Each layer maintains memory embeddings, interacts with them via bidirectional cross-attention, and updates them through an Least Recently Used (LRU) memory module using replacement or convex blending. ELMUR extends effective horizons up to 100,000 times beyond the attention window and achieves a 100% success rate on a synthetic T-Maze task with corridors up to one million steps. In POPGym, it outperforms baselines on more than half of the tasks. On MIKASA-Robo sparse-reward manipulation tasks with visual observations, it nearly doubles the performance of strong baselines, achieving the best success rate on 21 out of 23 tasks and improving the aggregate success rate across all tasks by about 70% over the previous best baseline. These results demonstrate that structured, layer-local external memory offers a simple and scalable approach to decision making under partial observability. Code and project page: https://elmur-paper.github.io/.

*arXiv comment: 31 pages, 15 figures, 8 tables*
