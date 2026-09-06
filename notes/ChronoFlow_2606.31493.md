# ChronoFlow-Policy: Unifying Past-Current-Future Interaction Flow in Visuomotor Policy Learning

> **arXiv 2606.31493** · arXiv 2026 · 提交 2026-06-30 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Bokai Lin, Yifu Xu, Xinyu Zhan, Hongjie Fang, Jialin Tian, Fu-Cheng Zhang, Yong-Lu Li, Cewu Lu, Lixin Yang*
> [arXiv](https://arxiv.org/abs/2606.31493) · [PDF](https://arxiv.org/pdf/2606.31493)

## 一句话定位

用物体与夹爪的稀疏 3D 关键点统一表示过去-当前-未来交互流，与动作共同训练的扩散策略。

## 与核心论文的关系

所属家族「latent 状态、循环与槽记忆（TRACE 一族）」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Visual signals play a crucial role in policy learning by enabling models to capture object motion and interaction dynamics. Just as humans reason about actions using both past experience and anticipated outcomes, effective policies should integrate past interactions with future predictions. However, existing visuomotor policies typically model either historical context or future dynamics in isolation, lacking a unified temporal representation of interaction dynamics. In this work, we introduce ChronoFlow, a temporally unified representation that captures past, current, and future interaction dynamics through sparse 3D keypoints of both objects and the gripper. Based on this representation, we propose ChronoFlow-Policy, a diffusion-based visuomotor policy that jointly learns ChronoFlow and action sequences through a co-training objective. Experiments on 14 simulated tasks and 5 real-world manipulation tasks demonstrate that ChronoFlow-Policy consistently outperforms strong diffusion-policy baselines and improves robustness in long-horizon and non-Markovian manipulation scenarios. Our project page is available at https://the-kamisato-sii.github.io/ChronoFlow-Policy-project-page/.
