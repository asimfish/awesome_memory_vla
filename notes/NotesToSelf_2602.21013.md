# Notes-to-Self: Scratchpad Augmented VLAs for Memory Dependent Manipulation Tasks

> **arXiv 2602.21013** · arXiv 2026 · 提交 2026-02-24 · 分类 `agentic` / 双系统、智能体与符号记忆
> *Sanjay Haresh, Daniel Dijkman, Apratim Bhattacharyya, Roland Memisevic*
> [arXiv](https://arxiv.org/abs/2602.21013) · [PDF](https://arxiv.org/pdf/2602.21013)

## 一句话定位

语言草稿板给 VLA 空间与时间记忆：记物体位置、追踪计划与子目标进度；在 ClevrSkills / MemoryBench 上提升泛化。

## 与核心论文的关系

所属家族「双系统、智能体与符号记忆」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Many dexterous manipulation tasks are non-markovian in nature, yet little attention has been paid to this fact in the recent upsurge of the vision-language-action (VLA) paradigm. Although they are successful in bringing internet-scale semantic understanding to robotics, existing VLAs are primarily "stateless" and struggle with memory-dependent long horizon tasks. In this work, we explore a way to impart both spatial and temporal memory to a VLA by incorporating a language scratchpad. The scratchpad makes it possible to memorize task-specific information, such as object positions, and it allows the model to keep track of a plan and progress towards subgoals within that plan. We evaluate this approach on a split of memory-dependent tasks from the ClevrSkills environment, on MemoryBench, as well as on a challenging real-world pick-and-place task. We show that incorporating a language scratchpad significantly improves generalization on these tasks for both non-recurrent and recurrent models.

*arXiv comment: To appear at ICRA 2026*
