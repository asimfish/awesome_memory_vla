# Efficient Long-Horizon Vision-Language-Action Models via Static-Dynamic Disentanglement

> **arXiv 2602.03983** · arXiv 2026 · 提交 2026-02-03 · 分类 `dense` / 稠密与压缩的视觉历史
> *Weikang Qiu, Huashuo Lei, Tinglin Huang, Rex Ying*
> [arXiv](https://arxiv.org/abs/2602.03983) · [PDF](https://arxiv.org/pdf/2602.03983)

## 一句话定位

DySta：把视觉 token 拆成静态/动态，跨帧只保留一份静态 token 并复用其 KV 缓存；多帧整合 +24.5%，推理 2 倍加速。

## 与核心论文的关系

所属家族「稠密与压缩的视觉历史」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Vision-Language-Action (VLA) models have recently emerged as a promising paradigm for generalist robotic control. Built upon vision-language model (VLM) architectures, VLAs predict actions conditioned on visual observations and language instructions, achieving strong performance and generalization across tasks. However, VLAs face two major challenges: a limited context window for input frames and inefficient inference due to the quadratic attention complexity and large parameter counts. To this end, we propose DySta, a framework that disentangles visual inputs into multi-level static and dynamic tokens, which enables (1) retaining a single copy of static tokens across frames to significantly reduce context length, and (2) reusing the key-value (KV) cache of static tokens through a lightweight recache gate that updates only when necessary. This design enables efficient multi-frame integration and efficient inference. In addition, we introduce a new benchmark that more effectively evaluates the multi-frame integration ability of VLAs. Experiments show that Dysta improves multi-frame integration by 24.5% across metrics on our benchmark and 23.3% in absolute success rate on real-world memory-dependent tasks, while accelerating inference by 2.0x (with +2.3% success rate) on simulation benchmarks and 2.2x (with +10.6% success rate) on real-world general tasks.
