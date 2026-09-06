# MemoryVAM: Integrating Memory into Video Action Model for Robot Manipulation

> **arXiv 2606.20679** · arXiv 2026 · 提交 2026-06-13 · 分类 `world` / 世界模型 / 视频动作模型中的记忆
> *Yuxin Jiang, Chang Yu, Yunuo Chen, Xiang Feng, Yin Yang, Nishank Gite, Chenfanfu Jiang*
> [arXiv](https://arxiv.org/abs/2606.20679) · [PDF](https://arxiv.org/pdf/2606.20679)

## 一句话定位

视频动作模型的情景记忆：Perceiver 压缩器把逐帧 CLIP 嵌入压成记忆 token，Cue Gate 估计任务完成度；LIBERO-Mem 5→42.5%。

## 与核心论文的关系

所属家族「世界模型 / 视频动作模型中的记忆」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Video-world-model policies learn action-relevant representations by predicting future observations. However, they condition on only a short observation window, which renders long-horizon manipulation non-Markovian when the correct action depends on earlier events that are no longer visible. We present MemoryVAM, an episodic memory mechanism for video-world-model policies. We employ a Recap-Cue (RC) module, in which a Perceiver-based Recap Compressor maps per-frame CLIP embeddings into compact memory tokens, and a lightweight Cue Gate estimates task completion from memory and language. These tokens are injected into both the video backbone and the action decoder, aligning policy imagination with episode progress and conditioning actions on history. Our model trains the memory module with video prediction, a delta-reconstruction auxiliary loss, and episode-boundary supervision, requiring no per-frame progress labels. The same mechanism applies to UNet and Diffusion Transformer (DiT) backbones by changing only the cross-attention injection interface. On LIBERO-Mem, our model improves average success from 5% to 42.5%. On real robots, it achieves 78.3% success on counting tasks, 80.0% on spatial recall, and 75.0% on sequential tracking. Project page: https://MemoryVAM.github.io/

*arXiv comment: Project page: https://MemoryVAM.github.io/*
