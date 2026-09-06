# Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control

> **arXiv 2606.25136** · arXiv 2026 · 提交 2026-06-23 · 分类 `dense` / 稠密与压缩的视觉历史
> *Rutav Shah, Yisu Li, Femi Bello, Yuke Zhu, Roberto Martín-Martín*
> [arXiv](https://arxiv.org/abs/2606.25136) · [PDF](https://arxiv.org/pdf/2606.25136)

## 一句话定位

HALO：注意力式记忆检索长达八分钟，用 VLM 生成的记忆依赖问答蒸馏先验抑制虚假相关，稀疏注意力限制检索范围以减少误差累积。

## 与核心论文的关系

所属家族「稠密与压缩的视觉历史」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

General-purpose robots operating in partially observable environments, such as homes, require memory to support autonomy. They must recall diverse information from the past, such as where objects were placed, which tasks a human partner has completed, and when an appliance was turned on. Achieving this versatility requires a general memory retrieval mechanism. Transformer architectures that use attention over long contexts for memory retrieval provide a promising approach, as they learn retrieval from data rather than relying on task-specific or hand-designed rules. However, directly incorporating them into imitation learning from offline data introduces two key challenges: (1) the policy may learn spurious correlations between past information and predicted actions, and (2) errors accumulate in memory due to prediction inaccuracies and their compounding interactions with the environment, causing model drift and cascading failures. To address both challenges, we introduce HALO, a visuomotor policy with an attention-based memory retrieval mechanism for long-horizon control. First, to suppress spurious correlations, HALO distills vision-language model (VLM) priors into the policy. It generates memory-dependent question--answer pairs from demonstration trajectories and trains jointly with a video question--answering objective, steering retrieval toward task-relevant information. Second, to reduce the impact of accumulated errors in memory during closed-loop control, HALO uses sparse attention that restricts retrieval to only the most relevant parts of the history. Together, these components enable more reliable long-horizon control by guiding the policy to retrieve task-relevant information from up to eight minutes of past experience. Project website: https://robin-lab.cs.utexas.edu/HALO

*arXiv comment: 16 pages, 5 tables, 8 figures*
