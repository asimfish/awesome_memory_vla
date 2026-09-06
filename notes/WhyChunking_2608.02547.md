# Why Does Action Chunking Improve Behavioral Cloning Performance in Robotic Control?

> **arXiv 2608.02547** · arXiv 2026 · 提交 2026-08-03 · 分类 `survey` / 综述与分析
> *Filippo Lazzati, Kyle Stachowicz, William Chen, Alberto Maria Metelli, Andrew Wagenmaker, Sergey Levine*
> [arXiv](https://arxiv.org/abs/2608.02547) · [PDF](https://arxiv.org/pdf/2608.02547)

## 一句话定位

动作块之所以有效，是因为更强的非马尔可夫表达力、更少的复合误差与隐式集成，而非时间一致性等旧假说；解释了 EventVLA 的 KEM 为何依赖长动作块。

## 与核心论文的关系

所属家族「综述与分析」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)、[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Action chunking---predicting and executing multiple actions instead of a single action---has proven to be a critical component for learning effective robotic control policies. However, our precise understanding of why action chunking improves performance has remained limited. In this work we seek to close this gap. Through rigorous experimental evaluations in both simulated and real-world settings, we show that existing hypotheses for the success of action chunking---temporal consistency, horizon reduction, and representation learning---fail to explain the success of action chunking. Instead, we find that action chunking benefits from greater non-Markovian expressivity and reduced compounding error compared to Markovian policies, but, in many settings of interest, these effects can be fully captured by delayed policies, which at each step predict a single action based on the observation $k$ steps in the past. We then show that there exists an additional benefit of action chunking that we refer to as implicit ensembling. In particular, by learning a diversity of temporal relationships (that is, $a_t | o_t, a_t | o_{t-1}, \ldots$), action-chunked policies exhibit behavior matching that of a model ensemble, increasing their robustness and generalization ability over policies that only learn a single temporal relationship. Building on these insights, we show that in simulated and real-world robotic control settings, we can match the performance of action chunking without action chunking---by deploying an action chunking policy as an ensemble of policies with randomized delays. Furthermore, we propose a policy class that amplifies the benefits of action chunking by explicitly instantiating an ensemble, and which we show significantly improves over the performance of action chunking in many domains.
