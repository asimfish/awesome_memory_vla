<!-- handwritten -->
# Chronos: A Physics-Informed Full-History Framework for Non-Markovian Long-Horizon Manipulation

> **arXiv 2606.30318** · arXiv 2026 · 提交 2026-06-29 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Yulin Zhou, Yimeng Wang, Nengyu Wang, Shaojia Xing, Shiyun Tu, Xiang Li, Jingkai Zhang, Ningbo Jiang, Yuankai Lin, Hua Yang, Xiangrui Zeng, Zhouping Yin*
> [arXiv](https://arxiv.org/abs/2606.30318) · [PDF](https://arxiv.org/pdf/2606.30318) · [仓库内英文 PDF](../papers/pdf/Chronos_2606.30318.pdf) · [中文翻译 PDF](../papers/zh/Chronos_2606.30318_zh.pdf)

## 一句话定位

Chronos 把整条观测历史当作策略的 latent 状态：每个物理控制步压成一个 state token，用 Mamba 型选择性 SSM 沿全轨迹因果传播，再以 IMLE 粗先验 + 预测加速度场的二阶 Schrödinger 桥生成动作块。0.3B 参数在 RMBench 七任务平均 73.6%，比 π0.5（11.2%）高 62.4 个百分点，比记忆 VLA Mem-0（50.8%）高 22.8 个百分点。

## 解决什么问题

观测混叠：杯子拿走再放回后，图像和点云与初始几乎一致，但任务阶段不同，正确动作也不同。Markov 策略 π(o_t, p_t) 与固定窗口 π(o_{t−K:t}) 只在条件变量是充分统计量时成立，RMBench 类任务正是构造成让这一前提失效。论文点名两类先前做法的短板：外挂记忆模块的 VLA（Mem-0 的 anchor + sliding、MemoryVLA）在历史需要连续调制低层动作、而非作为离散线索被检索时仍会失败；MTIL 虽是全历史 SSM 模仿，但 hidden state 被 detach，晚期损失无法修正早期阶段表征。

## 方法

- **存什么**：SSM 内部循环状态 h_t 与输出上下文 y_t。输入 token x_t = LN(W_x[g_t^obs; g_t^prop] + b_x)，观测特征来自可训练 PointNet 式点云编码器（RoboTwin 2.0、RMBench）或冻结 DINOv2 / ResNet18 + 可训练 adapter（ALOHA、真机）。token 序列长度等于示教轨迹长度 L。
- **何时写、如何读**：每步无门控写入，h_t = Ā_t h_{t−1} + B̄_t x_t，y_t = C_t h_t + D x_t，Δ_t、B_t、C_t 由当前 token 选择性生成；读出即 y_t 进动作条件 c_t = LN(W_c[y_t; x_t] + b_c)。没有槽、没有寻址，容量就是 SSM 状态维度。
- **动作头**：IMLE 生成器 G_φ(z, c_t) 采 K 个候选，只让离专家块最近者受拉（L_IMLE = E[min_k d(G(z^k, c), q*)]），得到粗先验 q_0。二阶桥再精化：参考路径 q_ref(s) = q_0 + α(s)(q_1 − q_0)，α(s) = 3s² − 2s³ 使端点速度为零；目标加速度 a_tar = a_spline(s) + K_p(q_ref − q) + K_d(v_ref − v)，由 Schrödinger → Madelung → Kostin 耗散势推出，落地是围绕三次样条的 PD 稳定器；噪声调度 σ(s) = 16σ_max s²(1−s)²，位置与速度扰动在两端同时为零。总损失 L = L_IMLE + λ_acc L_acc + λ_bc L_BC。
- **训练与推理**：感知按块编码后拼接、整体过一次 SSM，SSM 与动作头不 detach、全序列反传。推理为因果单步 SSM.step，IMLE 隐变量用时间相关采样保持连续，加速度场 symplectic Euler 积分 N 步，3–5 步最佳。只有模仿损失，无记忆专用辅助损失。

## 关键数字

| 基准 / 协议 | 对比项 | 数字 |
|---|---|---|
| RMBench 7 任务，50 demo，每任务 100 次；基线为论文报告值 | DP / ACT / π0.5 / X-VLA / Mem-0 / Chronos 平均 | 5.8 / 7.4 / 11.2 / 11.1 / 50.8 / **73.6%** |
| RMBench 分任务（Rearrange / Put Back / Swap Blocks / Swap T / Battery Try / Cover / Press Button） | Chronos | 98 / 98 / 99 / 93 / 29 / 96 / 2% |
| 同上 | Mem-0 | 89 / 90 / 67 / 14 / 28 / 68 / 0% |
| RoboTwin 2.0 Easy 8 任务，50 demo，100 次 | DP / ACT / RDT-1B / π0 / DP3 / Chronos 平均 | 35.1 / 30.6 / 35.8 / 48.8 / 59.5 / **70.0%**；Put Bottles Dustbin 输 DP3（54 vs 60） |
| ALOHA 双臂插入，50 demo，50 次；ACT、MTIL 为复现 | ACT / MTIL / 回归头（无 IMLE、无 SB）/ 换 diffusion / 换 flow / 无 SB / 无 IMLE / 一阶噪声调度 / 完整 | 50 / 76 / 76 / 66 / 72 / 86 / 84 / 72 / **90%** |
| ALOHA 推理积分步数 N = 1 / 3 / 5 / 15 | 同一模型 | 84 / 90 / 90 / 88% |
| 真机双 UR3 + 单 D435 RGB，每任务 50 次 | π0.5 vs Chronos：Put Back Blocks / Swap T（无记忆对照）/ Swap T-Mem / Cover Blocks | 0 vs 98、28 vs 96、0 vs 98、0 vs 20%；三个记忆任务合计 0/150 vs 108/150（72%） |
| 模型规模（论文表 I） | Mem-0 > 10B，π0.5 > 3.3B，DP3 264.4M，Chronos 0.3B | 仅作规模语境 |

## 局限与注意

- **基线不对等**：RMBench 与 RoboTwin 2.0 上除 Chronos 外全是 Reported 数字，作者明说未在同一 seed、硬件、编码器、代码库下重训。更关键的是 Chronos 在这两个基准用点云输入，π0.5、X-VLA、Mem-0 是 RGB VLA，"少 10 倍参数却高 62 点"混合了记忆机制与输入模态两个因素。真正受控的只有 ALOHA 上共享同一历史编码器的动作头消融，以及双方同一单目相机的真机对比。
- **缺记忆消融**：没有"去掉 SSM / 换短窗口"对照，也没有截断反传 vs 全序列反传的直接对比。MTIL 只在 ALOHA 出现且与 Chronos 回归头打平（76%），说明该任务瓶颈在动作头不在记忆。"历史应当是策略状态"来自 RMBench 大幅领先和 PCA 可视化（y_t 能分开 x_t 混叠的阶段），是间接证据。
- **物理推导的份量**：Schrödinger–Madelung–Kostin 链条最后落成 PD 稳定器 + 三次样条 + 四次噪声调度，作者自认"不是解一般桥问题，而是控制导向的投影"。真正有效的消融是一阶 vs 四次调度（72 → 90%）。
- **未评估**：延迟与吞吐未报告；训练显存只有大 O 分析；无跨 seed 方差。Press Button 2%、Battery Try 29% 说明 OCR 与接触精度仍是瓶颈；真机 Cover Blocks 20% 被归因为 ResNet18 弱化颜色–位置绑定。训练需要整条示教轨迹按物理时间对齐。

## 与核心论文的关系

- **最接近 TRACE**，同属 latent 状态记忆、都可挂在 compact 策略上，但设计相反：TRACE 是固定 K 槽（4 或 6 × 512-D）、按机器人状态轨迹的 path signature（深度 3，5219-D）寻址、门控写入、三项稳定器损失、适配器接入不改骨干与损失；Chronos 无槽无寻址，整个 SSM 状态就是记忆，每步无门控写入，只靠模仿损失，但把动作头整体换成 IMLE + 二阶桥。TRACE 用顺序反转负对照（37.8 路由相似度）检验记忆是否真依赖顺序，Chronos 没有等价负对照，只有真机 Swap T 与 Swap T-Mem 的任务级对照（π0.5 28% vs 0%，Chronos 96% vs 98%）。
- **与 EventVLA**：两篇都报 RMBench 但不能横向比。EventVLA 报 anchors-only 67.8%、Mem-0 42.0%、π0.5 10.4%；Chronos 报自身 73.6%、Mem-0 50.8%、π0.5 11.2%，同一基线在两篇里数字不同，任务子集或口径必然不同。机制上是对立设计：EventVLA 存稀疏原始关键帧（5 槽 FIFO，KEM 头预测 50 步 chunk 内的关键帧，阈值 0.55），事件触发写入、可视可查；Chronos 存稠密连续状态，每步写入、不可读。EventVLA 的隐式 latent bank 消融只有 24.9%，看似与 Chronos 矛盾，但那是挂在 VLA 上的外置库，Chronos 的 SSM 是全轨迹反传训练的策略主干。
- **与 SAI**：SAI 的 30 步 GRU 历史 token 是短窗口循环记忆（过早释放 64.5% → 16.1%），Chronos 是全历史循环；两者都表明循环状态不加记忆损失也能起作用。

## 关联阅读

- MTIL（arXiv 2505.12410）：Chronos 的直接前身，Mamba 全历史模仿但 detach hidden state，本文用它做截断信用分配的对照。
- RMBench（arXiv 2603.01229）：主实验基准及 Mem-0 基线的出处，anchor + sliding 记忆设计。
- IMLE Policy（arXiv 2502.12371）：粗先验所用的 IMLE 视觉运动策略，解释为何用最近样本匹配替代回归。
- MemoryVLA（arXiv 2508.19236）：感知–认知记忆库，代表 Chronos 所批评的外挂记忆模块路线。
- Mamba（arXiv 2312.00752）：选择性 SSM 原始论文，Chronos 的历史编码器。

