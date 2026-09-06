# OnEvoMemory: Evolving Memory through Online Robot Rollouts for Pretrained Robot Policies

> **arXiv 2608.08749** · arXiv 2026 · 提交 2026-08-09 · 分类 `agentic` / 双系统、智能体与符号记忆
> *Zhongxi Chen, Shenqi Zong*
> [arXiv](https://arxiv.org/abs/2608.08749) · [PDF](https://arxiv.org/pdf/2608.08749)

## 一句话定位

价值引导的记忆模块：从离线演示初始化、由在线 rollout 成败学习该保留哪些经验与转移。

## 与核心论文的关系

所属家族「双系统、智能体与符号记忆」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Long-horizon robot manipulation requires policies to track completed subtasks and critical interaction events. However, existing memory mechanisms heavily rely on external models or predefined update rules. To address this, we propose OnEvoMemory, a value-guided memory module for pretrained robot policies. It maintains recent context, high-value experiences, and salient transitions, while learning which experiences should be retained from trajectory outcomes. Offline demonstrations initialize the memory prior, whereas successful and unsuccessful online rollouts refine memory selection, helping the policy recognize task-stage transitions and avoid repeating completed subtasks. Experiments on long-horizon manipulation benchmarks show that OnEvoMemory improves the performance of the base VLA policy through both offline initialization and online memory evolution.

*arXiv comment: 6 pages, 1 figure. Accepted as a poster at the ECCV 2026 Workshop on Embodied Multimodal Reasoning in Physical Environments (EMR)*
