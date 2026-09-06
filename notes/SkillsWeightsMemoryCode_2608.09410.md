# Skills in Weights, Memory in Code: Hybrid Learning for Memory-Dependent Robot Manipulation

> **arXiv 2608.09410** · arXiv 2026 · 提交 2026-08-10 · 分类 `agentic` / 双系统、智能体与符号记忆
> *Yunhao Zhao, Zhenyang Ni, Haoyang Chen, Ruohan Zhang, Qi Zhu*
> [arXiv](https://arxiv.org/abs/2608.09410) · [PDF](https://arxiv.org/pdf/2608.09410)

## 一句话定位

HyMeS：技能在权重（模仿学习）、记忆在代码（编码智能体从 rollout 反馈迭代启发式），多模态阶段完成验证更新记忆；RoboMemArena 累计成功 52.5→66.2。

## 与核心论文的关系

所属家族「双系统、智能体与符号记忆」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Modern vision-language-action (VLA) policies have acquired broad manipulation skills, but typically generate each action chunk from the current observation or a short fixed-length history. However, real-world manipulation is often non-Markovian, requiring robots to retain and reason over task-relevant information from long-horizon interaction histories to determine the next action. To address this challenge, we propose HyMeS, a hybrid learning framework that leverages the reasoning and memory-management capabilities of coding agents to steer a Markovian VLA for memory-dependent manipulation. Specifically, HyMeS learns low-level motor skills through gradient-based imitation learning, while a coding agent acquires high-level memory-management strategies through heuristic learning by iteratively updating an executable heuristic system from rollout feedback. Furthermore, we close the loop between steering and execution through multimodal stage-completion verification, which updates memory using proprioceptive signals and multi-frame VLM judgments. Compared with end-to-end memory-augmented VLAs, HyMeS requires demonstrations only for reusable motor skills rather than for every history-dependent task configuration, enabling data-efficient compositional generalization. On RoboMemArena, HyMeS improves mean cumulative success from 52.5% to 66.2% and mean task success from 41.3% to 60.1% over pi0.5, while outperforming PrediMem by 4.5 points in cumulative success and 14.5 points in task success.

*arXiv comment: 9 pages, 4 figures, and 3 tables*
