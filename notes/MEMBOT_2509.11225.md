# MEMBOT: Memory-Based Robot in Intermittent POMDP

> **arXiv 2509.11225** · arXiv 2025 · 提交 2025-09-14 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Youzhi Liang, Eyan Noronha*
> [arXiv](https://arxiv.org/abs/2509.11225) · [PDF](https://arxiv.org/pdf/2509.11225)

## 一句话定位

解耦信念推断与策略学习：SSM/LSTM 信念编码器在观测间歇缺失下维持 latent 状态，50% 观测可用时保持 80% 性能。

## 与核心论文的关系

所属家族「latent 状态、循环与槽记忆（TRACE 一族）」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Robotic systems deployed in real-world environments often operate under conditions of partial and often intermittent observability, where sensor inputs may be noisy, occluded, or entirely unavailable due to failures or environmental constraints. Traditional reinforcement learning (RL) approaches that assume full state observability are ill-equipped for such challenges. In this work, we introduce MEMBOT, a modular memory-based architecture designed to address intermittent partial observability in robotic control tasks. MEMBOT decouples belief inference from policy learning through a two-phase training process: an offline multi-task learning pretraining stage that learns a robust task-agnostic latent belief encoder using a reconstruction losses, followed by fine-tuning of task-specific policies using behavior cloning. The belief encoder, implemented as a state-space model (SSM) and a LSTM, integrates temporal sequences of observations and actions to infer latent state representations that persist even when observations are dropped. We train and evaluate MEMBOT on 10 robotic manipulation benchmark tasks from MetaWorld and Robomimic under varying rates of observation dropout. Results show that MEMBOT consistently outperforms both memoryless and naively recurrent baselines, maintaining up to 80% of peak performance under 50% observation availability. These findings highlight the effectiveness of explicit belief modeling in achieving robust, transferable, and data-efficient policies for real-world partially observable robotic systems.
