# Explorative Imitation Learning: A Path Signature Approach for Continuous Environments

> **arXiv 2407.04856** · arXiv 2024 · 提交 2024-07-05 · 分类 `background` / 背景：记忆机制与轨迹描述子
> *Nathan Gavenski, Juarez Monteiro, Felipe Meneguzzi, Michael Luck, Odinaldo Rodrigues*
> [arXiv](https://arxiv.org/abs/2407.04856) · [PDF](https://arxiv.org/pdf/2407.04856)

## 一句话定位

CILO：模仿学习中用路径签名做轨迹的非参数表征以自动编码约束；签名进入模仿学习的先例。

## 与核心论文的关系

所属家族「背景：记忆机制与轨迹描述子」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)、[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Some imitation learning methods combine behavioural cloning with self-supervision to infer actions from state pairs. However, most rely on a large number of expert trajectories to increase generalisation and human intervention to capture key aspects of the problem, such as domain constraints. In this paper, we propose Continuous Imitation Learning from Observation (CILO), a new method augmenting imitation learning with two important features: (i) exploration, allowing for more diverse state transitions, requiring less expert trajectories and resulting in fewer training iterations; and (ii) path signatures, allowing for automatic encoding of constraints, through the creation of non-parametric representations of agents and expert trajectories. We compared CILO with a baseline and two leading imitation learning methods in five environments. It had the best overall performance of all methods in all environments, outperforming the expert in two of them.

*arXiv comment: This paper has been accepted in the 27th European Conference on Artificial Intelligence (ECAI) 2024*
