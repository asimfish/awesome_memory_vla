# A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning

> **arXiv 1011.0686** · AISTATS 2011 · 提交 2010-11-02 · 分类 `background` / 背景：记忆机制与轨迹描述子
> *Stephane Ross, Geoffrey J. Gordon, J. Andrew Bagnell*
> [arXiv](https://arxiv.org/abs/1011.0686) · [PDF](https://arxiv.org/pdf/1011.0686)

## 一句话定位

交互式模仿学习的理论基础，SAI 阶段三与 AutoIntervene 的方法源头。

## 与核心论文的关系

所属家族「背景：记忆机制与轨迹描述子」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)、[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Sequential prediction problems such as imitation learning, where future observations depend on previous predictions (actions), violate the common i.i.d. assumptions made in statistical learning. This leads to poor performance in theory and often in practice. Some recent approaches provide stronger guarantees in this setting, but remain somewhat unsatisfactory as they train either non-stationary or stochastic policies and require a large number of iterations. In this paper, we propose a new iterative algorithm, which trains a stationary deterministic policy, that can be seen as a no regret algorithm in an online learning setting. We show that any such no regret algorithm, combined with additional reduction assumptions, must find a policy with good performance under the distribution of observations it induces in such sequential settings. We demonstrate that this new approach outperforms previous approaches on two challenging imitation learning problems and a benchmark sequence labeling problem.

*arXiv comment: Appearing in the 14th International Conference on Artificial Intelligence and Statistics (AISTATS 2011)*
