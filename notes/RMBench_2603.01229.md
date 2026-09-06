<!-- handwritten -->
# RMBench: Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design

> **arXiv 2603.01229** · arXiv 2026 · 提交 2026-03-01 · 分类 `bench` / 记忆依赖操作的基准
> *Tianxing Chen, Yuran Wang, Mingleyang Li, Yan Qin, Hao Shi, Zixuan Li, Yifan Hu, Yingsheng Zhang, Kaixuan Wang, Yue Chen, Hongcheng Wang, Junjie Wang, Tianhang Yang, Renjing Xu, Ruihai Wu, Yao Mu, Yaodong Yang, Hao Dong, Ping Luo*
> [arXiv](https://arxiv.org/abs/2603.01229) · [PDF](https://arxiv.org/pdf/2603.01229) · [仓库内英文 PDF](../papers/pdf/RMBench_2603.01229.pdf) · [中文翻译 PDF](../papers/zh/RMBench_2603.01229_zh.pdf)

## 一句话定位

RMBench 用「任务记忆复杂度」M(n) 把 9 个 RoboTwin 2.0 双臂任务分成 5 个 M(1) 和 4 个 M(n)，并配套模块化记忆策略 Mem-0 做受控消融。要记的数字：Mem-0 平均 42.0%，对比 π₀.₅ 10.4%、X-VLA 9.8%；消融里去掉锚帧记忆使 M(1) 平均从 52.8% 掉到 26.8%，去掉子任务关键记忆使 M(n) 从 28.5% 掉到 4.8%。

## 解决什么问题

现有策略默认马尔可夫假设，只看固定长度的近期窗；已有记忆基准要么可复现任务少（MemoryBench 7 个任务仅 3 个可稳定复现）、要么面向 RL（MIKASA）、要么信息全程可见（LIBERO-Long）。RMBench 给出任务侧的记忆需求刻度 TMC：最优策略所需保留的任务相关历史观测的最小数量 m，M(0) 无需记忆，M(1) 需一帧，M(n) 需多帧。另一目标是拆出哪些架构组件真正贡献记忆能力。

## 方法

**任务。** M(1)：Observe and Pick Up、Rearrange Blocks、Put Back Block、Swap Blocks、Swap T，依赖一帧或固定少量历史帧；M(n)：Battery Try、Blocks Ranking Try、Cover Blocks、Press Button，需要试错、按外部反馈重复、按数字卡计数。基于 SAPIEN，另有 Isaac Lab-Arena 实现；每个动作-观测对附细粒度语言标注。论文未报告各任务的平均步长。

**协议。** 每任务 50 条合成演示训练，100 次 rollout；基线 DP、ACT（无预训练）、π₀.₅、X-VLA（预训练），均不做子任务分解。Mem-0 在 M(1) 任务只用执行模块，在 M(n) 任务启用子任务分解。

**Mem-0。** 双系统：规划模块（Qwen3-VL-8B-Instruct，LoRA）以初始帧 o₀、任务指令和「关键记忆窗」（已完成子任务文本 + 各子任务结束帧）预测下一个子任务；执行模块把当前帧与子任务经 VLM 编码后均值池化，分别与锚帧记忆（子任务起始帧 latent）和滑动窗记忆（最近 K 帧 latent）做交叉注意力，送入 H=30 的 DiT；子任务结束分类器（MLP）连续 8 步判定结束才切换并清空两个缓冲。规划只在子任务边界触发。执行模块每任务从零训练，无预训练。

## 关键数字

| 设置（成功率 %） | DP | ACT | π₀.₅ | X-VLA | Mem-0 |
|---|---|---|---|---|---|
| M(1) 平均 | 6.4 | 6.8 | 14.4 | 11.8 | 52.8 |
| M(n) 平均 | 5.0 | 4.8 | 5.5 | 7.3 | 28.5 |
| 总平均 | 5.8 | 5.9 | 10.4 | 9.8 | 42.0 |
| Press Button | 0 | 0 | 0 | 0 | 0 |
| Observe and Pick Up | 1 | 1 | 9 | 9 | 4 |
| 真机平均（3 任务，各 40 次） | — | 0.0 | 5.83 | — | 22.50 |

Mem-0 消融：M(1) 去锚帧 26.8、去滑动窗 40.4；M(n) 去关键记忆 4.8、去锚帧 26.8、去滑动窗 25.3、用仿真真值替代结束分类器 45.3。Swap T 去滑动窗反而从 14 升到 20；Cover Blocks 去锚帧 92、去滑动窗 84，都高于完整版 68。Press Button 用真值分类器也只有 14。

## 局限与注意

- 主结果全部在仿真；真机只有 3 个任务、Mem-0 22.5%，失败多为低层抓放精度而非规划。
- 「初始帧 + 近期窗」能否解题：Mem-0 的锚帧就是子任务起始帧、滑动窗就是近期帧，M(1) 任务不分解时锚帧即整局初始帧。消融说明这两项是 M(1) 成绩的主体（52.8 对比无锚帧 26.8），与 EventVLA 仅用锚帧在 RMBench 拿到 67.8% 方向一致（骨干与训练配置不同，数字不能直接对齐）。真正抵抗静态锚帧的是计数与试错类：Press Button 所有方法为 0，Blocks Ranking Try 最高 18。
- 协议不对称：Mem-0 在 M(n) 任务额外使用子任务标注和结束分类器，基线则端到端无分解；真值分类器带来 28.5→45.3 的提升说明结果里相当一部分来自分解本身。
- TMC 标注为人工给定，M(1) 定义里「固定少量历史帧」与「一帧」并未严格区分。
- 标注成本：逐帧语言标注、子任务边界与结束信号都来自合成管线；真机每任务需 100 条人工演示。

## 与核心论文的关系

- **EventVLA**（2606.20092）在 RMBench 上只部署锚帧版本（初始帧 + 短期窗）得 67.8%，并据此认为 RMBench 大多依赖持久空间布局、可被静态锚帧解决；RMBench 自己的锚帧消融支持这一判断。EventVLA 报告的两个低分任务 Observe and Pick Up、Press Button 也正是 Mem-0 的短板，说明 RMBench 的剩余难度在语义辨识与计数，而非瞬态证据。EventVLA 因此在同一平台另建 RoboTwin-MeM，用 n 参数化「中途出现又消失」的关键帧数量。RMBench 一作也在 EventVLA 作者列表中。
- **TRACE**（2606.14551）针对的延迟证据任务属于 M(1) 型，但它用机器人状态轨迹的路径签名寻址 latent 记忆而非存原图；RMBench 指出 Swap T 的目标朝向无法用语言可靠表达，正是符号化子任务记忆失效、需要 latent 记忆的场景。M(n) 的试错任务要求有序历史，TRACE 的顺序反转负对照可借来检验记忆是否真的用到了顺序。
- **SAI**（2606.16490）的历史 token 解决的是过早释放；RMBench 附录里 Swap Blocks 的典型失败同样是子任务过早或过晚终止，两者都指向「阶段判断」这一时间记忆问题。按 RoboMME 的分类，RMBench 主要覆盖空间记忆（M(1)）和时间/计数记忆（M(n)），不含物体指代与过程模仿。

## 关联阅读

- SAM2Act / MemoryBench（2501.18564）：RMBench 批评其 7 个任务仅 3 个可稳定复现。
- MIKASA-Robo（2502.10550）：32 个记忆任务但面向 RL 形式化。
- MemER（2510.20328）：逐帧推理子任务的双系统，RMBench 用结束分类器把规划降到边界触发。
- RoboMME（2603.04639）：同期基准，按时间/空间/物体/过程四类记忆设计 16 任务。
- RoboMemArena（2605.10921）：后续基准，认为 RMBench 任务覆盖偏少，把平均步长推到 1,076。
