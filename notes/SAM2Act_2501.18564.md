# SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation

> **arXiv 2501.18564** · arXiv 2025 · 提交 2025-01-30 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Haoquan Fang, Markus Grotz, Wilbert Pumacay, Yi Ru Wang, Dieter Fox, Ranjay Krishna, Jiafei Duan*
> [arXiv](https://arxiv.org/abs/2501.18564) · [PDF](https://arxiv.org/pdf/2501.18564)

## 一句话定位

SAM2 式记忆库 + 编码器 + 注意力赋予多视角策略空间记忆；附 MemoryBench，记忆任务 94.3%。

## 与核心论文的关系

所属家族「latent 状态、循环与槽记忆（TRACE 一族）」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Robotic manipulation systems operating in diverse, dynamic environments must exhibit three critical abilities: multitask interaction, generalization to unseen scenarios, and spatial memory. While significant progress has been made in robotic manipulation, existing approaches often fall short in generalization to complex environmental variations and addressing memory-dependent tasks. To bridge this gap, we introduce SAM2Act, a multi-view robotic transformer-based policy that leverages multi-resolution upsampling with visual representations from large-scale foundation model. SAM2Act achieves a state-of-the-art average success rate of 86.8% across 18 tasks in the RLBench benchmark, and demonstrates robust generalization on The Colosseum benchmark, with only a 4.3% performance gap under diverse environmental perturbations. Building on this foundation, we propose SAM2Act+, a memory-based architecture inspired by SAM2, which incorporates a memory bank, an encoder, and an attention mechanism to enhance spatial memory. To address the need for evaluating memory-dependent tasks, we introduce MemoryBench, a novel benchmark designed to assess spatial memory and action recall in robotic manipulation. SAM2Act+ achieves an average success rate of 94.3% on memory-based tasks in MemoryBench, significantly outperforming existing approaches and pushing the boundaries of memory-based robotic systems. Project page: sam2act.github.io.

*arXiv comment: Including Appendix, Project Page: https://sam2act.github.io*
