# ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval

> **arXiv 2511.06202** · arXiv 2025 · 提交 2025-11-09 · 分类 `agentic` / 双系统、智能体与符号记忆
> *Shahram Najam Syed, Yatharth Ahuja, Arthur Jakobsson, Jeff Ichnowski*
> [arXiv](https://arxiv.org/abs/2511.06202) · [PDF](https://arxiv.org/pdf/2511.06202)

## 一句话定位

压缩经验回放 + 检索增强在设备上快速专精 VLA，存储省 97%，12 条演示 31 秒适应；偏「经验记忆」而非回合内记忆。

## 与核心论文的关系

所属家族「双系统、智能体与符号记忆」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Vision-Language-Action (VLA) models like OpenVLA demonstrate impressive zero-shot generalization across robotic manipulation tasks but struggle to adapt to specific deployment environments where consistent high performance on a limited set of tasks is more valuable than broad generalization. We present EXPierence replayed, REtrieval augmented, Specialized VLA (ExpReS-VLA), a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. Our approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs. During deployment, ExpReS-VLA retrieves the $k$ most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories. To leverage failed attempts, we introduce Thresholded Hybrid Contrastive Loss (THCL), enabling the model to learn from both successful and unsuccessful demonstrations. Experiments on the LIBERO benchmark show improvements from 82.6% to 93.1% on spatial reasoning and 61% to 72.3% on long-horizon tasks over base OpenVLA, with gains across architectures including $π_0$ (+3.2 points) and OpenVLA-OFT (+1.7 points). Physical robot experiments across five tasks demonstrate 98% success on both in-distribution and out-of-distribution conditions, improving from 84.7% and 32% respectively for naive fine-tuning. Adaptation completes in 31 seconds using 12 demonstrations on a single RTX 5090.

*arXiv comment: 8 pages, 4 figures, 3 tables, accepted to International Conference on Robotics and Automation (ICRA) 2026*
