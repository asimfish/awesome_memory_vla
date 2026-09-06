# MemER: Scaling Up Memory for Robot Control via Experience Retrieval

> **arXiv 2510.20328** · arXiv 2025 · 提交 2025-10-23 · 分类 `agentic` / 双系统、智能体与符号记忆
> *Ajay Sridhar, Jennifer Pan, Satvik Sharma, Chelsea Finn*
> [arXiv](https://arxiv.org/abs/2510.20328) · [PDF](https://arxiv.org/pdf/2510.20328)

## 一句话定位

双系统：高层 VLM（Qwen2.5-VL-7B）选择并追踪相关关键帧、生成文本指令给低层 π₀.₅；EventVLA 把它作为双系统基线（RoboTwin-MeM 10.5%）。

## 与核心论文的关系

所属家族「双系统、智能体与符号记忆」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Humans routinely rely on memory to perform tasks, yet most robot policies lack this capability; our goal is to endow robot policies with the same ability. Naively conditioning on long observation histories is computationally expensive and brittle under covariate shift, while indiscriminate subsampling of history leads to irrelevant or redundant information. We propose a hierarchical policy framework, where the high-level policy is trained to select and track previous relevant keyframes from its experience. The high-level policy uses selected keyframes and the most recent frames when generating text instructions for a low-level policy to execute. This design is compatible with existing vision-language-action (VLA) models and enables the system to efficiently reason over long-horizon dependencies. In our experiments, we finetune Qwen2.5-VL-7B-Instruct and $π_{0.5}$ as the high-level and low-level policies respectively, using demonstrations supplemented with minimal language annotations. Our approach, MemER, outperforms prior methods on three real-world long-horizon robotic manipulation tasks that require minutes of memory. Videos and code can be found at https://jen-pan.github.io/memer/.

*arXiv comment: Project page: https://jen-pan.github.io/memer/*
