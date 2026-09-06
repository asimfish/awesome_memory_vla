# Gated Memory Policy: In-Context Memorization and Adaptation

> **arXiv 2604.18933** · arXiv 2026 · 提交 2026-04-21 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Yihuai Gao, Jeff Jinyun Liu, Shuang Li, Shuran Song*
> [arXiv](https://arxiv.org/abs/2604.18933) · [PDF](https://arxiv.org/pdf/2604.18933)

## 一句话定位

学习「何时回忆」（记忆门）与「回忆什么」（轻量交叉注意力），对历史动作注入扩散噪声防过拟合；MemMimic 上比长历史基线 +30.1。

## 与核心论文的关系

所属家族「latent 状态、循环与槽记忆（TRACE 一族）」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Robotic manipulation tasks exhibit varying memory requirements, ranging from Markovian tasks that require no memory to non-Markovian tasks that demand in-context memorization of historical information within a single trial or in-context adaptation based on the outcomes of multiple past trials. Surprisingly, simply extending observation histories of a visuomotor policy often leads to a significant performance drop due to distribution shift and overfitting. To address these issues, we propose Gated Memory Policy (GMP), a visuomotor policy that learns both when to recall memory and what to recall. To learn when to recall memory, GMP employs a learned memory gate mechanism that selectively activates history context only when necessary, improving robustness and reactivity. To learn what to recall efficiently, GMP introduces a lightweight cross-attention module that constructs effective latent memory representations. To further enhance robustness, GMP injects diffusion noise into historical actions, mitigating sensitivity to noisy or inaccurate histories during both training and inference. On our proposed non-Markovian benchmark MemMimic, GMP achieves a 30.1% average success rate improvement over long-history baselines, while maintaining competitive performance on Markovian tasks in RoboMimic. All code, data and in-the-wild deployment instructions are available on our project website https://gated-memory-policy.github.io/.
