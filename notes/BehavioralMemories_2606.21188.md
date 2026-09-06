# Remember what you did?: Learning Behavioral Memories for Partially Observable Object Manipulation

> **arXiv 2606.21188** · arXiv 2026 · 提交 2026-06-19 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Kuancheng Wang, Seungho Yeom, Jinglin Cao, Yuheng Zhi, Nikhil Shinde, Michael Yip*
> [arXiv](https://arxiv.org/abs/2606.21188) · [PDF](https://arxiv.org/pdf/2606.21188)

## 一句话定位

CAMP：把机器人自己的动作历史压缩成行为记忆，自监督地追踪任务进度并从失败尝试中学习；附 Memory-T-Bench / Memory-Manip-Bench。

## 与核心论文的关系

所属家族「latent 状态、循环与槽记忆（TRACE 一族）」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Long horizon, contact-rich manipulation is inherently partially observable. This is as a single visual observation rarely captures a robot's full action context, including prior attempts, interactions, or progress. Consequently, standard visuomotor policies or vision-language-action models are prone to struggle in such tasks due to a lack of memory. To address this, we introduce Compressed Action Memory Policy (CAMP) based on the insight that a robot's own action history serves as a highly informative, self-supervised signal, enabling the policy to learn a robust, compact history representation. In our approach, we train a memory module to maintain a compressed representation of past actions, forcing it to encode a latent behavioral memory of all the robot's past interactions that can then be used to better contextualize future actions. This allows our approach to implicitly track generalized task progress and learn from failed attempts without any additional supervision, or external oversight. We evaluate CAMP across four real-robot setups and two novel simulation benchmarks: Memory-T-Bench and Memory-Manip-Bench. By demonstrating substantial gains over state-of-the-art baselines, CAMP is, to our knowledge, the first policy to demonstrate substantial success on contact-rich partially observable manipulation tasks purely through learned memory.

*arXiv comment: Project website: robo-camp.github.io*
