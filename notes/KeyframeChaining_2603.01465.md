# Non-Markovian Long-Horizon Robot Manipulation via Keyframe Chaining

> **arXiv 2603.01465** · arXiv 2026 · 提交 2026-03-02 · 分类 `event` / 事件与关键帧记忆（EventVLA 一族）
> *Yipeng Chen, Wentao Tan, Lei Zhu, Fengling Li, Jingjing Li, Guoli Yang, Heng Tao Shen*
> [arXiv](https://arxiv.org/abs/2603.01465) · [PDF](https://arxiv.org/pdf/2603.01465)

## 一句话定位

学习判别式嵌入空间自动选关键帧，用进度感知查询按当前阶段检索历史帧并作为交错视觉 token 输入；ManiSkill 上四个非马尔可夫任务。

## 与核心论文的关系

所属家族「事件与关键帧记忆（EventVLA 一族）」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Existing Vision-Language-Action (VLA) models often struggle to generalize to long-horizon tasks due to their heavy reliance on immediate observations. While recent studies incorporate retrieval mechanisms or extend context windows to handle procedural tasks, they often struggle to capture Non-Markovian dependencies, where optimal actions rely solely on specific past states rather than the current observation. To address this, we introduce Keyframe-Chaining VLA, a framework that extracts and links key historical frames to model long-horizon dependencies. Specifically, we propose an automatic keyframe selector that learns a discriminative embedding space, effectively identifying distinct state transitions. To capture task-critical information, we design a progress-aware query mechanism that dynamically retrieves historical frames based on their temporal relevance to the current execution phase. These selected keyframes are integrated into the VLA as interleaved visual tokens, explicitly grounding the policy in the long-horizon temporal context. Finally, we introduce a suite of four Non-Markovian manipulation tasks built upon the ManiSkill simulator to measure task success rates. Experimental results demonstrate that our method achieves superior performance, effectively tackling robot manipulation tasks characterized by long-horizon temporal dependencies. Code is available at https://github.com/cytoplastm/KC-VLA.
