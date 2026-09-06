# MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models

> **arXiv 2606.09827** · arXiv 2026 · 提交 2026-06-08 · 分类 `dense` / 稠密与压缩的视觉历史
> *Hao Shi, Weiye Li, Bin Xie, Yulin Wang, Renping Zhou, Tiancai Wang, Xiangyu Zhang, Ping Luo, Gao Huang*
> [arXiv](https://arxiv.org/abs/2606.09827) · [PDF](https://arxiv.org/pdf/2606.09827)

## 一句话定位

MemoryVLA 加上潜空间世界模型「想象」未来，记忆与想象共同形成时间感知 token；真机记忆依赖任务 +26%、想象依赖任务 +28%。

## 与核心论文的关系

所属家族「稠密与压缩的视觉历史」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Temporal modeling is essential for robotic manipulation, as effective control requires both memory of past interactions and imagination of future states. However, most VLA models rely primarily on the current observation and therefore struggle with long-horizon, temporally dependent tasks. Cognitive science suggests that humans rely on working memory to buffer short-lived context, the hippocampal system to preserve episodic memory of past experience, and internal models to imagine possible future state evolution. Inspired by these mechanisms, we propose MemoryVLA++, a full temporal modeling framework that equips VLA models with memory and imagination for robotic manipulation. A pretrained VLM encodes the current observation into perceptual and cognitive tokens, forming working memory. These tokens query a Perceptual-Cognitive Memory Bank to retrieve relevant historical context. This bank stores low-level details and high-level semantics from past interactions, and is updated through redundancy-aware consolidation. A world model imagines future states in a denoising latent space, and the imagined latents are integrated under memory guidance to form full temporal-aware tokens. The resulting tokens condition a diffusion action expert to predict temporally consistent action sequences. We conduct extensive experiments on 5 simulation benchmarks and 3 categories of real-robot tasks across 3 robots, covering general manipulation, long-horizon temporal tasks, robustness, and generalization. Our method achieves strong performance across Libero, SimplerEnv, Mikasa-Robo, Calvin, Libero-Plus, and diverse real-robot tasks, validating the effectiveness of full temporal modeling with memory and imagination. For example, on real robots, it achieves +9%, +26%, +28% gains on general, memory-dependent, and imagination-dependent tasks. Project Page: https://shihao1895.github.io/MemoryVLA-PP-Web

*arXiv comment: The project is available at https://shihao1895.github.io/MemoryVLA-PP-Web*
