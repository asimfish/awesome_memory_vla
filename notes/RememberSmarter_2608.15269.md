# Remember Smarter: Visual History Compressor and Hyperbolic Experience Space for Robotic Memory

> **arXiv 2608.15269** · arXiv 2026 · 提交 2026-08-15 · 分类 `dense` / 稠密与压缩的视觉历史
> *Dai Zhou, Jiexi Yan, Tong Li, Yuxuan Wang, Cheng Deng*
> [arXiv](https://arxiv.org/abs/2608.15269) · [PDF](https://arxiv.org/pdf/2608.15269)

## 一句话定位

视觉历史压缩（空间双向 Mamba + 时间因果 Mamba）+ 双曲空间经验记忆（Poincaré VAE），异步转成测地线提示 token；LIBERO-Plus 53.6→70.6。

## 与核心论文的关系

所属家族「稠密与压缩的视觉历史」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Long-horizon robot policies require compact access to recent observations and reusable experience without expanding the vision-language-action (VLA) context. We introduce Remember Smarter (RS), a plug-and-play module with complementary visual-history and hyperbolic experience-memory branches. Its visual branch compresses multi-view patch histories using bidirectional spatial Mamba and causal temporal Mamba, then exposes the resulting memory to action-facing hidden states through residual cross-attention while leaving the VLM visual-token stream unchanged. Its experience branch stores successful final-layer VLM states in a Poincare VAE space, organizes them hierarchically, and asynchronously converts retrieved experience into geodesic prompt tokens without blocking action inference. When adapted to pi0, RS increases total success on LIBERO-Plus from 53.6% to 70.6% and achieves substantial performance gains in real-robot experiments designed to evaluate memory retention and experience utilization.

*arXiv comment: 19 pages, 7 pages*
