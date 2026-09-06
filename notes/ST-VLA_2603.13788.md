# ST-VLA: Enabling 4D-Aware Spatiotemporal Understanding for General Robot Manipulation

> **arXiv 2603.13788** · arXiv 2026 · 提交 2026-03-14 · 分类 `dense` / 稠密与压缩的视觉历史
> *You Wu, Zixuan Chen, Cunxu Ou, Wenxuan Wang, Wenbo Huang, Lin Cao, Yangtao Chen, Weichao Qiu, Xingyue Quan, Jieqi Shi, Jing Huo, Yang Gao*
> [arXiv](https://arxiv.org/abs/2603.13788) · [PDF](https://arxiv.org/pdf/2603.13788)

## 一句话定位

分层 VLA 用统一 3D-4D 表征（3D 轨迹 + 4D 时空掩码）桥接推理与控制；偏时空感知而非显式记忆。

## 与核心论文的关系

所属家族「稠密与压缩的视觉历史」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Robotic manipulation in open-world environments requires reasoning across semantics, geometry, and long-horizon action dynamics. Existing hierarchical Vision-Language-Action (VLA) frameworks typically use 2D representations to connect high-level reasoning with low-level control, but lack depth awareness and temporal consistency, limiting robustness in complex 3D scenes. We propose ST-VLA, a hierarchical VLA framework using a unified 3D-4D representation to bridge perception and action. ST-VLA converts 2D guidance into 3D trajectories and generates smooth spatial masks that capture 4D spatio-temporal context, providing a stable interface between semantic reasoning and continuous control. To enable effective learning of such representations, we introduce ST-Human, a large-scale human manipulation dataset with 14 tasks and 300k episodes, annotated with 2D, 3D, and 4D supervision via a semi-automated pipeline. Using ST-Human, we train ST-VLM, a spatio-temporal vision-language model that generates spatially grounded and temporally coherent 3D representations to guide policy execution. The smooth spatial masks focus on task-relevant geometry and stabilize latent representations, enabling online replanning and long-horizon reasoning. Experiments on RLBench and real-world manipulation tasks show that \method significantly outperforms state-of-the-art baselines, improving zero-shot success rates by 44.6% and 30.3%. These results demonstrate that offloading spatio-temporal reasoning to VLMs with unified 3D-4D representations substantially improves robustness and generalization for open-world robotic manipulation. Project website: https://oucx117.github.io/ST-VLA/.

*arXiv comment: 25 pages, under review*
