# Recursive Belief Vision Language Action Models

> **arXiv 2602.20659** · arXiv 2026 · 提交 2026-02-24 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Vaidehi Bagaria, Bijo Sebastian, Nirav Kumar Patel*
> [arXiv](https://arxiv.org/abs/2602.20659) · [PDF](https://arxiv.org/pdf/2602.20659)

## 一句话定位

RB-VLA：自监督世界模型目标训练紧凑信念状态，VLM 每任务只查询一次给意图；无信念 32.5%→有信念 77.5%，延迟降至 1/5。

## 与核心论文的关系

所属家族「latent 状态、循环与槽记忆（TRACE 一族）」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Vision-language-action models must enable agents to execute long-horizon tasks under partial observability. However, most existing approaches remain observation-driven, relying on short context windows or repeated queries to vision-language models (VLMs). This leads to loss of task progress, action repetition under perceptual aliasing, and high inference latency. While semantic grounding is important, long-horizon manipulation fundamentally requires persistent, action-conditioned state representations. Current VLAs lack such representations and exhibit limited temporal and physical reasoning, making them ill-suited for multi-stage control. This paper introduces RB-VLA, a belief-centric architecture trained with self-supervised world-model objectives that maintains a compact latent state encoding task-relevant history, dynamics, and object interactions. Queried once per task, the VLM provides high-level intent, while the belief tracks task progress and enables phase-aware, causally grounded control under partial observability without storing raw observations or scaling memory with time. The belief and intent jointly condition a diffusion policy for robust closed-loop execution. RB-VLA outperforms prior VLAs on long-horizon benchmarks, achieving 52.5 percent and 37.5 percent higher success rates on multi-stage pick-and-place and stacking tasks, respectively, compared to pi_0. It also reduces inference latency by up to five times relative to baselines and eliminates memory growth across timesteps observed in existing VLAs. Ablations show the belief module is the primary driver of performance, increasing success rates from 32.5 percent without belief to 77.5 percent with belief.
