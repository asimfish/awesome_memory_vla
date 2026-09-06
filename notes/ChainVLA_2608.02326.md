# ChainVLA: Chaining Vision-Language-Action Queries through a Unified Execution State for Long-Horizon Manipulation

> **arXiv 2608.02326** · arXiv 2026 · 提交 2026-08-03 · 分类 `agentic` / 双系统、智能体与符号记忆
> *Yuzhi Huang, Weijue Bu, Ziyi Xiong, Jie Wu, Fanding Huang, Jingyan Jiang, Zhi Wang*
> [arXiv](https://arxiv.org/abs/2608.02326) · [PDF](https://arxiv.org/pdf/2608.02326)

## 一句话定位

跨查询链接的执行状态：循环工作状态 + 稀疏事件记忆（Progress Context）与上一预测的未执行尾部（Motion Tail）；RMBench 62.8%，去掉两者分别掉到 3.0 / 11.2。

## 与核心论文的关系

所属家族「双系统、智能体与符号记忆」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Humans perform long-horizon manipulation by retaining knowledge of what earlier actions have established while continuously adapting the motion underway. By contrast, action-chunked vision-language-action (VLA) policies repeatedly replan from the current input at each query. Existing methods preserve either long-term task evidence through memory or short-term motion through action reuse and ensembling, leaving the cross-query handoff incomplete. We introduce ChainVLA, a 1.2B-parameter VLA policy that chains successive queries through a joint and revisable execution state. Progress Context combines a recurrent Working State with sparse event memory to carry observation-derived task progress, while Motion Tail feeds the preceding prediction's unexecuted continuation into state construction and action generation. Together, the two components condition a decoder that regenerates each action horizon under the latest observation, allowing the carried state to guide the next prediction without fixing it. ChainVLA reaches 62.8% average success on RMBench and 98.8% across four LIBERO suites, while removing Motion Tail or Progress Context reduces RMBench success to 11.2% and 3.0%, respectively. These asymmetric ablations are consistent with motion continuity helping preserve the observation stream from which task progress is inferred.

*arXiv comment: 13 pages (9 main + 4 appendix), 4 figures. Project page: https://muqy1818.github.io/chainvla-web/*
