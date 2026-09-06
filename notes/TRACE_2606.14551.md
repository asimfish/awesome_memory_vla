# TRACE: Trajectory-Routed Causal Memory for Delayed-Evidence Visuomotor Imitation

> **arXiv 2606.14551** · arXiv 2026 · 提交 2026-06-12 · 分类 `core` / 核心论文（逐篇深读）
> *Zihao Li, Ranpeng Qiu, Yincong Chen, Guoqiang Ren, Weiming Zhi*
> [arXiv](https://arxiv.org/abs/2606.14551) · [PDF](https://arxiv.org/pdf/2606.14551) · [仓库内英文 PDF](../papers/pdf/TRACE_2606.14551.pdf) · [中文翻译 PDF](../papers/zh/TRACE_2606.14551_zh.pdf)

## 一句话定位

核心论文之一：固定 K 槽 latent 记忆，用机器人状态轨迹的路径签名做读写地址，适配器外挂到 ACT/DP；五个真机延迟证据任务 ACT 25.5→69.2，顺序反转负对照把路由相似度打到 37.8。

这是本仓库的核心论文之一，完整解读见 [TRACE 深读](../reports/02_trace_cn.md)（[English](../reports/02_trace_en.md)）。

## 摘要（原文）

Robots under autonomous operation may require decisions based on evidence that is no longer visible. We study delayed-evidence tasks, where an early cue disappears before a later decision point, so visually similar observations can require different actions. In these settings, the current observation is not a sufficient state for control. We introduce TRAjectory-routed Causal Evidence (TRACE), a memory framework for visuomotor imitation policies. TRACE stores task-relevant visual and robot-state evidence, such as object identity, target choice, or route-dependent state, in a fixed-size latent memory that remains bounded over long episodes. Instead of indexing memory by raw time or manually provided task labels, TRACE uses path signatures: compact, order-sensitive features of the executed robot-state trajectory. These signatures do not store the visual cue itself; rather, they provide trajectory-conditioned keys for writing and retrieving the evidence stored when the cue was visible. When the robot later reaches an ambiguous observation, the policy conditions on TRACE memory to recover the missing context and choose the correct branch. TRACE attaches through lightweight adapters to policies, without changing the policy backbone, action head, or imitation objective. Across real-world long-horizon manipulation tasks with visually ambiguous branch points, TRACE improves branch selection and task success over alternative baselines, including short-history and recurrent memory. Project page: https://jeong-zju.github.io/trace
