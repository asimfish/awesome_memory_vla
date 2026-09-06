# AnchorVLA4D: an Anchor-Based Spatial-Temporal Vision-Language-Action Model for Robotic Manipulation

> **arXiv 2603.12730** · arXiv 2026 · 提交 2026-03-13 · 分类 `dense` / 稠密与压缩的视觉历史
> *Juan Zhu, Zhanying Shao, Xiaoqi Li, Ethan Morgan, Jiadong Xu, Hongwei Fan, Hao Dong*
> [arXiv](https://arxiv.org/abs/2603.12730) · [PDF](https://arxiv.org/pdf/2603.12730)

## 一句话定位

最简的空间-时间锚：把初始帧作为锚图像与当前帧一起输入，加轻量空间编码器；对应 EventVLA 的「初始帧锚」组件。

## 与核心论文的关系

所属家族「稠密与压缩的视觉历史」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Since current Vision-Language-Action (VLA) systems suffer from limited spatial perception and the absence of memory throughout manipulation, we investigate visual anchors as a means to enhance spatial and temporal reasoning within VLA policies for robotic manipulation. Conventional VLAs generate actions by conditioning on a single current frame together with a language instruction. However, since the frame is encoded as a 2D image, it does not contain detailed spatial information, and the VLA similarly lacks any means to incorporate past context. As a result, it frequently forgets objects under occlusion and becomes spatially disoriented during the manipulation process. Thus, we propose AnchorVLA4D, a simple spatial-temporal VLA that augments the visual input with an anchor image to preserve the initial scene context throughout execution, and adds a lightweight spatial encoder that jointly processes the anchor and current frames to expose geometric relationships within an episode. Built on a Qwen2.5-VL backbone with a diffusion-based action head, AnchorVLA4D requires no additional sensing modalities (e.g., depth or point clouds) and introduces negligible inference overhead. Combining anchoring with a frozen pretrained spatial encoder yields further gains, realizing a 13.6% improvement on the Simpler WidowX benchmark and confirming the approach on real-world tasks, where it achieved an average success rate of 80%.
