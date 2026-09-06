# Tri-Manual Visuomotor Imitation Learning of Robot Policies

> **arXiv 2607.25731** · arXiv 2026 · 提交 2026-07-28 · 分类 `multi` / 多机器人协作与搭档记忆（SAI 一族）
> *James Zhao, Mingyuan Ba, Weiming Zhi*
> [arXiv](https://arxiv.org/abs/2607.25731) · [PDF](https://arxiv.org/pdf/2607.25731)

## 一句话定位

单操作者为三臂系统演示：DATS 按任务顺序与手臂使用约束离线重排演示时序，训练单一同步三臂策略。

## 与核心论文的关系

所属家族「多机器人协作与搭档记忆（SAI 一族）」，对照阅读：[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Bimanual teleoperation provides an effective way to collect robot demonstrations, but it assumes that the operator and robot have matching numbers of simultaneous control channels. This assumption breaks for tri-manual systems: the robot can coordinate three arms concurrently, whereas a single operator can continuously control only two. Pairwise mode switching may therefore record otherwise independent motions sequentially, causing behaviour cloning to reproduce delays imposed by the interface rather than required by the task. We present TriManPolicy, a tri-manual imitation learning system that allows one operator to demonstrate behaviours for three arms. Its central component is Dependency-Aware Tri-Arm Scheduling (DATS). The key idea is to preserve the demonstrated arm motions while reconsidering when they occur. DATS retimes demonstrations offline by preserving local sensorimotor segments of fixed duration and repositioning them according to constraints on task order and arm usage that are reviewed by a human. The resulting data train a single synchronous policy for all three arms, while deployment requires neither the dependency graph nor the scheduler. Across six challenging tasks performed in the real world, policies trained on demonstrations retimed by DATS exhibit more efficient coordination while maintaining comparable observed task success. Offline analysis further shows that DATS changes the supervision across arms rather than merely removing idle periods. Project videos and additional material are available at https://aus.bot/trimanpolicy/.

*arXiv comment: 9 pages, 9 figures. Project page: https://aus.bot/research/trimanpolicy/ . Equal contribution by James Zhao and Mingyuan Ba. Added the project website and clarified the qualitative figure captions*
