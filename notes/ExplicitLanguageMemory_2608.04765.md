# Explicit Language Memory for Long-Horizon Planning in Vision-Language-Action Models

> **arXiv 2608.04765** · arXiv 2026 · 提交 2026-08-05 · 分类 `agentic` / 双系统、智能体与符号记忆
> *Houze Xu, Jizhong Li, Ziyi Ye*
> [arXiv](https://arxiv.org/abs/2608.04765) · [PDF](https://arxiv.org/pdf/2608.04765)

## 一句话定位

高层 VLM 把离散观测递归写成带时间逻辑的文本记忆并更新子任务指令，低层 VLA 执行；可解释的语义决策记录。

## 与核心论文的关系

所属家族「双系统、智能体与符号记忆」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Vision-language-action (VLA) models provide a unified paradigm for connecting visual perception, language understanding, and robotic control. However, existing VLA models still face major challenges in long-horizon tasks: sparse expert demonstrations constrain cross-task compositional generalization; the non-Markovian nature of long-horizon tasks makes it difficult for policies conditioned only on current observations to maintain temporal consistency; limited closed-loop error correction allows execution errors to accumulate; and end-to-end action fine-tuning may weaken the high-level semantic representations of vision-language model (VLM) backbones. To address these issues, we propose a hierarchical long-horizon VLA architecture with an explicit language-memory module. The central idea is to convert discrete temporal observations into a coherent textual memory sequence with temporal logic. The system is decoupled into a high-level VLM and a low-level VLA: the high-level VLM performs semantic reasoning through a visual question answering training paradigm, while the low-level VLA executes precise continuous control conditioned on subtask instructions and visual observations. The high-level VLM recursively updates both language memory and subtask instructions using the previous memory as a contextual anchor, enabling persistent temporal tracking and dynamic correction during long-horizon execution. We evaluate the proposed method in multiple simulation environments and conduct sim-to-real experiments on a real robotic platform. The results demonstrate that explicit language memory improves the success rate and robustness of VLA models on complex long-horizon tasks while providing an interpretable semantic account of the decision process.

*arXiv comment: 11 pages, 4 figures*
