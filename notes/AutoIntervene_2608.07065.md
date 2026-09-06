# AutoIntervene: Calibrated Intervention for Action-Chunking Imitation Learning Policies

> **arXiv 2608.07065** · arXiv 2026 · 提交 2026-08-07 · 分类 `multi` / 多机器人协作与搭档记忆（SAI 一族）
> *Jinhe Tang, Weiming Zhi*
> [arXiv](https://arxiv.org/abs/2608.07065) · [PDF](https://arxiv.org/pdf/2608.07065)

## 一句话定位

用成功执行构建视觉-动作支持记忆，按分位数校准双向切换阈值决定策略↔操作者交接；SAI 阶段三「何时干预」的自动化答案。

## 与核心论文的关系

所属家族「多机器人协作与搭档记忆（SAI 一族）」，对照阅读：[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Action-chunking visuomotor policies learn from demonstrations and improve temporal consistency by predicting short action sequences rather than single-step commands. Yet perception errors and execution drift can move the robot outside the demonstration distribution, while the policy continues to produce smooth action chunks that are inconsistent with the observed state. We present AutoIntervene, an online framework that selectively transfers control between an action-chunking policy and an operator during deployment. AutoIntervene evaluates proposed chunks against a visual-action support memory built from successful task executions, combining visual similarity with consistency between proposed and reference actions. Phase-local support governs policy-to-operator transfer within the current task phase, whereas global support governs the return to policy control after operator recovery. We calibrate separate switching thresholds for the two directions from empirical quantiles of evaluation-level scores on held-out expert demonstrations, avoiding direct manual tuning of score cutoffs. Intervention segments retained from successful rollouts target learner-induced states and provide corrective supervision for subsequent policy updates. Experiments on real-world bimanual manipulation tasks show higher post-adaptation task success and lower operator-control time than manual intervention. Videos and additional results are available at https://aus.bot/research/autointervene/.

*arXiv comment: 9 pages, 7 figures*
