# Making two action heads agree: coordination mechanisms and a runtime collapse certificate for flow-matching policies

> **arXiv 2608.15748** · arXiv 2026 · 提交 2026-08-16 · 分类 `multi` / 多机器人协作与搭档记忆（SAI 一族）
> *Jinhui Sun, Wei Zhou, Bowen Yang, Xinliang Xiao, Li Yang*
> [arXiv](https://arxiv.org/abs/2608.15748) · [PDF](https://arxiv.org/pdf/2608.15748)

## 一句话定位

双表征流匹配策略两分支的协调机制与运行时塌缩证书；「两个动作头选到不同模态」的形式化。

## 与核心论文的关系

所属家族「多机器人协作与搭档记忆（SAI 一族）」，对照阅读：[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

A dual-representation flow-matching policy decodes each predicted motion into joint and end-effector spaces, and the residual between the two kinematically equivalent decodings provides a physically interpretable runtime signal. On multimodal tasks, however, independently sampled branches may choose different valid modes, causing false alarms. We study how to coordinate the two branches and at what cost. Across two robot environments and a non-robotic testbed, the tested mechanisms fall into four classes. An auxiliary latent shared by both branches but absent from the flow-matching construction is erased at the population optimum, a provable dead end confirmed within a prespecified 2% equivalence band. Sharing source noise can coordinate or anti-coordinate: its effect changes sign with the representation map and tracks the alignment of decoder mode basins. Consistency regularization gives intermediate coordination but reduces the valid-pair rate, while training-supported discrete partitions achieve near-ceiling coordination robustly. We further derive a chance-corrected coordination bound based only on each branch's Gini-Simpson diversity, yielding an attainable region and a label-free certificate that separates coordination from collapse when zero mismatch is ambiguous. On LIBERO-Plus, benign multimodality adds 1.57 percentage points of false alarms to the residual, which remains the strongest evaluated failure signal; the preregistered token intervention does not meet its false-alarm criterion or produce a seed-robust detection change. Code, models, and per-run configurations are available at https://github.com/kimo423/dual-head-coordination.
