# Chronos: A Physics-Informed Full-History Framework for Non-Markovian Long-Horizon Manipulation

> **arXiv 2606.30318** · arXiv 2026 · 提交 2026-06-29 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Yulin Zhou, Yimeng Wang, Nengyu Wang, Shaojia Xing, Shiyun Tu, Xiang Li, Jingkai Zhang, Ningbo Jiang, Yuankai Lin, Hua Yang, Xiangrui Zeng, Zhouping Yin*
> [arXiv](https://arxiv.org/abs/2606.30318) · [PDF](https://arxiv.org/pdf/2606.30318)

## 一句话定位

把观测历史提升为策略动力学的 latent 状态：每个控制步一个状态 token，选择性 SSM 传播，IMLE 粗先验 + 二阶薛定谔桥精化；RMBench 73.6%（π₀.₅ +62.4），参数少 10 倍。

## 与核心论文的关系

所属家族「latent 状态、循环与槽记忆（TRACE 一族）」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

General-purpose robot policies should be modeled as dynamical systems, yet many VLA and generative imitation policies still rely on present observations or short windows. This Markovian shortcut fails in memory-dependent manipulation: identical observations can demand different actions after different histories. We present Chronos, a physics-informed full-history framework for non-Markovian long-horizon manipulation. The key idea is to elevate observation history from auxiliary context to the latent state of the policy dynamics. At each physical control step, Chronos forms one state-representative token by fusing observation and proprioception, so the token sequence is aligned one-to-one with physical time. A selective state space model propagates this causal historical state, which conditions a multimodal coarse action prior through implicit maximum likelihood estimation (IMLE). This prior is then refined by a second-order Schrodinger-inspired bridge that predicts acceleration fields, yielding smoother and more physically grounded robot motion. Across 16 simulated tasks and 4 real-world experiments, Chronos is evaluated on precision insertion, general manipulation, and memory-dependent long-horizon control. On RMBench, where success requires remembering task phase, Chronos achieves 73.6% average success, outperforming Markovian VLA baseline pi0.5 by +62.4 percentage points, a 6.6x relative gain, while using 10x fewer parameters. It also surpasses the memory VLA Mem-0 by 22.8 points while using over 30x fewer parameters. In real-world dual-arm experiments using a single RGB camera, Chronos achieves 78% average success over four tasks, including 72% on the three memory-dependent tasks, whereas pi0.5 achieves 7% overall and 0% on the memory-dependent subset. These results suggest that history should not be treated as auxiliary context, but as the latent state of the manipulation policy.

*arXiv comment: 20 pages, 10 figures. Submitted to IEEE Transactions on Robotics*
