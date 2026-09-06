# IntervenGen: Interventional Data Generation for Robust and Data-Efficient Robot Imitation Learning

> **arXiv 2405.01472** · IROS 2024 · 提交 2024-05-02 · 分类 `multi` / 多机器人协作与搭档记忆（SAI 一族）
> *Ryan Hoque, Ajay Mandlekar, Caelan Garrett, Ken Goldberg, Dieter Fox*
> [arXiv](https://arxiv.org/abs/2405.01472) · [PDF](https://arxiv.org/pdf/2405.01472)

## 一句话定位

从少量人类干预自动生成大量纠正数据，鲁棒性提升至 39 倍；直接可补 SAI 阶段三的干预覆盖不足。

## 与核心论文的关系

所属家族「多机器人协作与搭档记忆（SAI 一族）」，对照阅读：[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Imitation learning is a promising paradigm for training robot control policies, but these policies can suffer from distribution shift, where the conditions at evaluation time differ from those in the training data. A popular approach for increasing policy robustness to distribution shift is interactive imitation learning (i.e., DAgger and variants), where a human operator provides corrective interventions during policy rollouts. However, collecting a sufficient amount of interventions to cover the distribution of policy mistakes can be burdensome for human operators. We propose IntervenGen (I-Gen), a novel data generation system that can autonomously produce a large set of corrective interventions with rich coverage of the state space from a small number of human interventions. We apply I-Gen to 4 simulated environments and 1 physical environment with object pose estimation error and show that it can increase policy robustness by up to 39x with only 10 human interventions. Videos and more results are available at https://sites.google.com/view/intervengen2024.
