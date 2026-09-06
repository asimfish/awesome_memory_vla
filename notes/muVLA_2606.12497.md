# $μ$VLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models

> **arXiv 2606.12497** · arXiv 2026 · 提交 2026-06-10 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Egor Cherepanov, Nikita Kachaev, Daniil Zelezetsky, Aydar Bulatov, Artem Pshenitsyn, Yuri Kuratov, Alexey Skrynnik, Aleksandr I. Panov, Alexey K. Kovalev*
> [arXiv](https://arxiv.org/abs/2606.12497) · [PDF](https://arxiv.org/pdf/2606.12497)

## 一句话定位

受控隔离研究：只在 OpenVLA-OFT 里加跨步携带的记忆 token（TBPTT 训练），不加任何辅助损失；MIKASA-Robo 0.42→0.84，标定了最小循环记忆的能力边界。

## 与核心论文的关系

所属家族「latent 状态、循环与槽记忆（TRACE 一族）」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Vision-language-action (VLA) models predict chunks of future actions from the current observation, an assumption that fails under partial observability, where decisions depend on information no longer visible. Existing memory-augmented VLAs simultaneously introduce recurrence, retrieval, compression modules, auxiliary objectives, hierarchical memory, or task-specific architectural changes, so the contribution of recurrence itself remains entangled with surrounding machinery. We present a controlled isolation study of recurrence in a strong pretrained VLA backbone. Our formulation augments the transformer with a small set of learnable memory tokens carried across timesteps and updated through self-attention, trained end to end with truncated backpropagation through time, with no auxiliary losses and no architectural changes. We instantiate this as $μ$VLA, a family of OpenVLA-OFT variants parameterized by memory width m, TBPTT length K, and the memory update rule (cross-step gradients or a detached EMA), so that recurrence is the only varying factor. On MIKASA-Robo, $μ$VLA improves average success rate on five training tasks from 0.42 to 0.84 at the strongest setting and reaches 0.23 on held-out tasks with the same memory structure versus 0.07 for the memoryless baseline. On tasks requiring different memory structure, performance remains near baseline. On LIBERO, the strongest recurrent variant achieves 96.2% average success, indicating no regression under full observability. We interpret these results as a calibration of the capability envelope of minimal in-backbone recurrence, identifying the regime in which it is sufficient and the regime where additional memory structure is required. Demos and videos can be found in https://avanturist322.github.io/mu-vla/.

*arXiv comment: 34 pages, 20 figures, 9 tables*
