# FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation

> **arXiv 2607.18231** · arXiv 2026 · 提交 2026-07-20 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Ruicheng Li, Qixiu Li, Ruichun Ma, Yu Deng, Lin Luo, Zhiying Du, Jianfeng Xiang, Huizhi Liang, Ruicheng Wang, Jiaolong Yang, Baining Guo*
> [arXiv](https://arxiv.org/abs/2607.18231) · [PDF](https://arxiv.org/pdf/2607.18231)

## 一句话定位

力历史经 VAE 压成力记忆 token 条件动作专家：视觉分不清的重复接触事件（按几次按钮、擦几次盘子）靠力记住，成功率 80%+。

## 与核心论文的关系

所属家族「latent 状态、循环与槽记忆（TRACE 一族）」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Vision-language-action (VLA) models have achieved impressive generalization in robotic manipulation, and recent memory-augmented VLAs have relaxed the Markovian assumption by conditioning on past images or language summaries. Vision-based memory approaches address this by conditioning on sampled past image frames, but they are computationally expensive and fundamentally limited when temporal events are visually ambiguous, e.g., pushing a button multiple times with small movements. We propose FM-VLA, a VLA model with force-based memory, enabling temporal context reasoning for non-Markovian, contact-rich manipulation. We encode force histories into compact force memory tokens with a variational autoencoder (VAE) pretrained with force time series reconstruction. By projecting force latent representations and short state history as additional conditioning tokens to the action expert module, we enable VLAs to leverage accumulated contact event history to guide manipulation. We evaluate FM-VLA on three memory-dependent tasks, including finding a hidden block, pressing a button, and wiping a dish for a specific number of times. Our lightweight force memory achieves over 80% success rate with minimal inference overhead, significantly outperforming baseline approaches. Project page: https://qft-333.github.io/FM-VLA-Page/
