# ContextVLA: Vision-Language-Action Model with Amortized Multi-Frame Context

> **arXiv 2510.04246** · arXiv 2025 · 提交 2025-10-05 · 分类 `dense` / 稠密与压缩的视觉历史
> *Huiwon Jang, Sihyun Yu, Heeseung Kwon, Hojin Jeon, Younggyo Seo, Jinwoo Shin*
> [arXiv](https://arxiv.org/abs/2510.04246) · [PDF](https://arxiv.org/pdf/2510.04246)

## 一句话定位

把过去多帧压成单个上下文 token，以低成本获得多帧训练的收益；观察到 VLM 骨干比普通 BC 更能利用多帧。

## 与核心论文的关系

所属家族「稠密与压缩的视觉历史」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Leveraging temporal context is crucial for success in partially observable robotic tasks. However, prior work in behavior cloning has demonstrated inconsistent performance gains when using multi-frame observations. In this paper, we introduce ContextVLA, a policy model that robustly improves robotic task performance by effectively leveraging multi-frame observations. Our approach is motivated by the key observation that Vision-Language-Action models (VLA), i.e., policy models built upon a Vision-Language Model (VLM), more effectively utilize multi-frame observations for action generation. This suggests that VLMs' inherent temporal understanding capability enables them to extract more meaningful context from multi-frame observations. However, the high dimensionality of video inputs introduces significant computational overhead, making VLA training and inference inefficient. To address this, ContextVLA compresses past observations into a single context token, allowing the policy to efficiently leverage temporal context for action generation. Our experiments show that ContextVLA consistently improves over single-frame VLAs and achieves the benefits of full multi-frame training but with reduced training and inference times.

*arXiv comment: Project page: https://huiwon-jang.github.io/contextvla*
