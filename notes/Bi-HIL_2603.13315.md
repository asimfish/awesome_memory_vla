# Bi-HIL: Bilateral Control-Based Multimodal Hierarchical Imitation Learning via Subtask-Level Progress Rate and Keyframe Memory for Long-Horizon Contact-Rich Robotic Manipulation

> **arXiv 2603.13315** · arXiv 2026 · 提交 2026-03-04 · 分类 `event` / 事件与关键帧记忆（EventVLA 一族）
> *Thanpimon Buamanee, Masato Kobayashi, Yuki Uranishi*
> [arXiv](https://arxiv.org/abs/2603.13315) · [PDF](https://arxiv.org/pdf/2603.13315)

## 一句话定位

双边控制 + 分层模仿：关键帧记忆与子任务级进度率同时条件高低层策略，面向接触丰富的长时程任务。

## 与核心论文的关系

所属家族「事件与关键帧记忆（EventVLA 一族）」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Long-horizon contact-rich robotic manipulation remains challenging due to partial observability and unstable subtask transitions under contact uncertainty. While hierarchical architectures improve temporal reasoning and bilateral imitation learning enables force-aware control, existing approaches often rely on flat policies that struggle with long-horizon coordination. We propose Bi-HIL, a bilateral control-based multimodal hierarchical imitation learning framework for long-horizon manipulation. Bi-HIL stabilizes hierarchical coordination by integrating keyframe memory with subtask-level progress rate that models phase progression within the active subtask and conditions both high- and low-level policies. We evaluate Bi-HIL on unimanual and bimanual real-robot tasks, demonstrating consistent improvements over flat and ablated variants. The results highlight the importance of explicitly modeling subtask progression together with force-aware control for robust long-horizon manipulation. For additional material, please check: https://mertcookimg.github.io/bi-hil
