# EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies

> **arXiv 2606.20092** · arXiv 2026 · 提交 2026-06-18 · 分类 `core` / 核心论文（逐篇深读）
> *Ganlin Yang, Zhangzheng Tu, Yuqiang Yang, Sitong Mao, Junyi Dong, Tianxing Chen, Jiaqi Peng, Jing Xiong, Jiafei Cao, Jifeng Dai, Wengang Zhou, Yao Mu, Tai Wang*
> [arXiv](https://arxiv.org/abs/2606.20092) · [PDF](https://arxiv.org/pdf/2606.20092) · [仓库内英文 PDF](../papers/pdf/EventVLA_2606.20092.pdf) · [中文翻译 PDF](../papers/zh/EventVLA_2606.20092_zh.pdf)

## 一句话定位

核心论文之一：稀疏视觉证据记忆 = 初始/近期锚帧 + 学习的关键帧证据记忆（KEM），KEM 从 VLA 隐状态预测未来 50 步的关键帧概率，写入容量 5 的原图缓冲；RoboTwin-MeM 18.0→75.2%，RMBench 67.8%（仅锚帧）。

这是本仓库的核心论文之一，完整解读见 [EventVLA 深读](../reports/01_eventvla_cn.md)（[English](../reports/01_eventvla_en.md)）。

## 摘要（原文）

Memory remains a critical bottleneck for long-horizon robotic manipulation, as standard Vision-Language-Action (VLA) policies often fail when task-relevant cues become occluded or unobservable over time. While existing memory-augmented methods utilize historical context, they either suffer from severe information bottlenecks, incur high latency via decoupled dual systems, or rely on unselective buffers that accumulate massive visual redundancies. To address these limitations, we introduce EventVLA, an end-to-end framework founded on the concept of sparse visual evidence memory that comprises two core components: foundational visual anchors to retain initial and short-term contexts, and a dynamic Keyframe Evidence Memory (KEM) module. Specifically, KEM directly predicts future keyframe probabilities from the VLA's latent embeddings to autonomously capture and store sparse, task-critical visual events. This foresight-driven mechanism empowers the policy to dynamically evaluate the future causal utility of current observations, preserving transient visual evidence before it becomes unobservable. Furthermore, we propose RoboTwin-MeM, a diagnostic benchmark specifically designed to evaluate non-Markovian manipulation tasks with interactive visual evidence. Extensive evaluations show that across 17 memory-requiring simulation tasks and 4 real-world bimanual tasks, EventVLA achieves an average success rate improvement of +40% over state-of-the-art memory-augmented VLAs.
