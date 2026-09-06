# RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies

> **arXiv 2607.04434** · arXiv 2026 · 提交 2026-07-05 · 分类 `bench` / 记忆依赖操作的基准
> *Tianxing Chen, Yue Chen, Zixuan Li, Junyuan Tang, Kailun Su, Haoran Lu, Weijie Wan, Baijun Chen, Songling Liu, Haowen Yan, Honghao Su, Zhiyang Dou, Kaixuan Wang, Dandan Zhang, Yunze Liu, Yan Qin, Qiwei Liang, Qiwei Wu, Zijian Lin, Wenwei Lin, Yuran Wang, Minghua He, Tianshu Wu, Ruihai Wu, Jingquan Zhou, Kai-Chong Lei, Haibao Yu, Yuanfeng Ji, Weiyang Jin, Guanyu Lin, Xiaofan Li, Qi Xiong, Renjing Xu, Zhongyu Li, Wenhao Chai, Enze Xie, Ziwei Wang, Yao Mu, Hao Dong, Wojciech Matusik, Mingyu Ding, Wenbo Ding, Ping Luo, Masayoshi Tomizuka*
> [arXiv](https://arxiv.org/abs/2607.04434) · [PDF](https://arxiv.org/pdf/2607.04434)

## 一句话定位

统一仿真+真机基准（42 仿真 + 18 真机任务），记忆是五个评测维度之一；提供公共榜单与 XPolicyLab 集成。

## 与核心论文的关系

所属家族「记忆依赖操作的基准」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Generalist robot manipulation policies have advanced rapidly, yet existing benchmarks remain limited in systematically evaluating their capabilities. Many rely on simple, short-horizon, or skill-narrow tasks with limited capability coverage, and are often conducted only in simulation or only in the real world. Simulation enables scalable feedback but misses physical deployment challenges, while real-world evaluation is costly, time-consuming, and difficult to reproduce. We introduce RoboDojo, a unified sim-and-real benchmark for comprehensive evaluation of generalist robot manipulation policies. RoboDojo includes 42 simulation tasks and 18 real-world tasks covering diverse and complementary manipulation capabilities. The simulation benchmark evaluates five dimensions: generalization, memory, precision, long-horizon execution, and open-vocabulary instruction following, while the real-world benchmark exposes policies to challenging physical-world deployment conditions. RoboDojo supports scalable evaluation through heterogeneous parallel simulation in Isaac Sim and provides RoboDojo-RealEval, a reproducible real-world evaluation system with remote cloud access, standardized hardware, scene reset, evaluation protocol, and deployment interface. Together with XPolicyLab, policies can be integrated once and evaluated across simulation and real-world settings with minimal adaptation. We integrate 30 policies into XPolicyLab and evaluate them on RoboDojo, establishing a public leaderboard and systematic analysis of current policy performance. The website is available at http://robodojo-benchmark.com/.

*arXiv comment: Website: https://robodojo-benchmark.com/, Code: https://github.com/RoboDojo-Benchmark/RoboDojo, Leaderboard: https://robodojo-benchmark.com/leaderboard*
