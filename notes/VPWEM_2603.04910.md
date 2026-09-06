# VPWEM: Non-Markovian Visuomotor Policy with Working and Episodic Memory

> **arXiv 2603.04910** · arXiv 2026 · 提交 2026-03-05 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Yuheng Lei, Zhixuan Liang, Hongyuan Zhang, Ping Luo*
> [arXiv](https://arxiv.org/abs/2603.04910) · [PDF](https://arxiv.org/pdf/2603.04910)

## 一句话定位

滑窗工作记忆 + Transformer 上下文压缩器把窗外观测递归压成固定数量情景嵌入，每步计算近似常数；MIKASA 上比 DP/VLA 高 20%+。

## 与核心论文的关系

所属家族「latent 状态、循环与槽记忆（TRACE 一族）」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Imitation learning from human demonstrations has achieved significant success in robotic control, yet most visuomotor policies still condition on single-step observations or short-context histories, making them struggle with non-Markovian tasks that require long-term memory. Simply enlarging the context window incurs substantial computational and memory costs and encourages overfitting to spurious correlations, leading to catastrophic failures under distribution shift and violating real-time constraints in robotic systems. By contrast, humans can compress important past experiences into long-term memories and exploit them to solve tasks throughout their lifetime. In this paper, we propose VPWEM, a non-Markovian visuomotor policy equipped with working and episodic memories. VPWEM retains a sliding window of recent observation embeddings as short-term working memory, and introduces a Transformer-based contextual memory compressor that recursively converts out-of-window observations into a fixed number of episodic memory embeddings. The compressor uses self-attention over a cache of past summary embeddings and cross-attention over a cache of historical observations, and is trained jointly with the policy. We instantiate VPWEM on diffusion policies to exploit both short-term and episode-wide information for action generation with nearly constant memory and computation per step. Experiments demonstrate that VPWEM outperforms state-of-the-art baselines including diffusion policies and vision-language-action (VLA) models by more than 20\% on the memory-intensive manipulation tasks in MIKASA and achieves an average 5\% improvement on the mobile manipulation benchmark MoMaRT. Code is available at https://github.com/HarryLui98/code_vpwem.

*arXiv comment: Accepted to IEEE Robotics and Automation Letters (RA-L). \textcopyright 2026 IEEE*
