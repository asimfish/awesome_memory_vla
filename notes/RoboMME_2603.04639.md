<!-- handwritten -->
# RoboMME: Benchmarking and Understanding Memory for Robotic Generalist Policies

> **arXiv 2603.04639** · arXiv 2026 · 提交 2026-03-04 · 分类 `bench` / 记忆依赖操作的基准
> *Yinpei Dai, Hongze Fu, Jayjun Lee, Yuejiang Liu, Haoran Zhang, Jianing Yang, Chelsea Finn, Nima Fazeli, Joyce Chai*
> [arXiv](https://arxiv.org/abs/2603.04639) · [PDF](https://arxiv.org/pdf/2603.04639) · [仓库内英文 PDF](../papers/pdf/RoboMME_2603.04639.pdf)

## 一句话定位

RoboMME 把记忆拆成时间/空间/物体/过程四类，各 4 个任务共 16 个、1,600 条演示、77 万步，并在同一 π₀.₅ 骨干上受控比较 14 种记忆变体与 4 个已有方法。要记的结论：没有一种表征通吃，感知记忆 + 调制器注入（FrameSamp+Modul）总分最高 44.51%，符号记忆在计数类领先；真值子目标的 GroundSG+Oracle 84.08%，人类 90.5%。

## 解决什么问题

已有记忆型 VLA（MemoryVLA、MemER、ContextVLA 等）各用不同骨干、各评自设任务，回答不了「哪种记忆表征对哪类任务有效」；已有基准也不够：MemoryBench 只有 3 个近乎解决的任务，MIKASA-Robo 面向 RL、平均仅 72 步、演示不足。RoboMME 同时提供显式非马尔可夫、覆盖四类记忆的测试床，和固定骨干、固定记忆预算的模型族，把表征与注入方式拆开比较。

## 方法

**任务。** ManiSkill 中 7 自由度 Franka Panda 桌面，前视 + 腕部 256×256。Counting（时间）：PickXTimes、BinFill、SwingXTimes、StopCube；Permanence（空间）：VideoUnmask、ButtonUnmask 及各自的 Swap 版；Reference（物体）：PickHighlight、VideoRepick、VideoPlaceButton、VideoPlaceOrder；Imitation（过程）：MoveCube、InsertPeg、PatternLock、RouteStick。带 Video 前缀的任务和 Imitation 套件在初始步给一段视频，其余任务的证据在执行中出现（按按钮期间方块被短暂高亮或盖住）。平均 481 步（PatternLock 208 到 VideoPlaceOrder 1,134），评测上限 1,300 步。演示由关键路点回放生成并加 5% 噪声再恢复以注入纠错，分易/中/难，每任务 100 条，附子目标与关键帧标注。

**模型族 MME-VLA。** 三种表征：符号（SimpleSG / GroundSG 子目标，由 Gemini-2.5-Pro 提示、微调 Qwen3-VL-4B 或仿真真值 Oracle 生成）、感知（TokenDrop 按 RGB 差异保留变化区块并完整保留首帧；FrameSamp 均匀采 32 帧各池化到 4×4）、循环（TTT 快权重、RMT 记忆槽）。三种注入：Context（拼进 VLM 输入）、Modul（动作专家每层交叉注意记忆后做 AdaLN 调制，约 80M 参数）、Expert（独立 18 层记忆专家，约 190M）。记忆预算统一 512 token。

**协议。** 16 任务联合训练 80k 步，动作块 20 执行 16，冻结 SigLIP；每任务 50 个固定种子回合，取最后 3 个 checkpoint × 3 个随机种子共 9 次平均。对比 π₀.₅、π₀.₅+过去动作、SAM2Act+、MemER。人类研究把任务改为在线 VideoQA 加 oracle 规划器，18 人 800 回合。

## 关键数字

| 方法（成功率 %） | Counting | Permanence | Reference | Imitation | 平均 |
|---|---|---|---|---|---|
| π₀.₅（无记忆） | 28.78 | 17.00 | 17.17 | 8.78 | 17.93 |
| π₀.₅ + 过去动作 | — | — | — | — | 19.73 |
| SAM2Act+ | 35.33 | 26.00 | 16.83 | 7.33 | 21.37 |
| MemER | 48.83 | 53.17 | 38.00 | 29.50 | 42.38 |
| GroundSG+QwenVL（符号最佳） | 38.00 | 39.34 | 31.56 | 21.89 | 32.70 |
| FrameSamp+Modul（感知最佳） | 65.22 | 25.11 | 36.33 | 51.39 | 44.51 |
| TTT+Expert（循环最佳） | 36.00 | 22.95 | 19.67 | 10.78 | 22.35 |
| GroundSG+Oracle（上界） | 83.86 | 93.31 | 95.17 | 63.98 | 84.08 |
| 人类（oracle 规划器） | — | — | — | — | 90.50 |

其他：记忆预算从 64 增到 1024，FrameSamp+Modul 从 30.42 升到 45.87，512 之后增益变小；动作 token 对记忆 token 的平均注意力只有 0.7–4.8%，峰值可到 21.8%，记忆使用稀疏；GroundSG+QwenVL 计算量约为 π₀.₅ 的 3 倍，MemER 约 5 倍。真机 4 任务各 10 次：π₀.₅ 4/40，GroundSG+QwenVL 19/40，FrameSamp+Modul 25/40。附录中 DP 与 MemoryVLA 总分均低于 10%。

## 局限与注意

- 论文自述：桌面单臂、固定资产、几乎只测 π₀.₅ 一个骨干；同样的记忆设计搬到 OpenVLA-OFT 收益很小（最高 21.6%）。
- 「初始帧 + 近期窗」能否解题：论文没有这一基线，最接近的是完整保留首帧的 TokenDrop，它在三种注入下都低于均匀采样全程的 FrameSamp。按任务结构，9 个任务的证据在初始视频这段静态前缀里，但 VideoPlaceOrder、PatternLock 需要前缀内部的顺序而非单帧；ButtonUnmask、ButtonUnmaskSwap、PickHighlight 的证据只在按按钮期间出现，是瞬态证据；4 个计数任务需要事件累积。EventVLA「RoboMME 可被静态锚帧解决」的判断在本文内部找不到直接支持，也未被检验。
- 真值子目标能到 84.08%，而人类在 StopCube、SwingXTimes 只有 78 / 80，部分任务的困难来自时序精度与低层控制，不全是记忆。
- 符号记忆变体依赖子目标标注（仿真自动生成，真机需人工标注接地子目标），这项成本应计入比较。
- 多任务联合训练、512 token 预算、冻结视觉编码器，与 RMBench 单任务从零训练的设定不同，数字不能横比。

## 与核心论文的关系

- **EventVLA**（2606.20092）未在 RoboMME 上报告结果，却认为其可由锚帧解决。RoboMME 的 Button 系列与 PickHighlight 恰是 KEM 针对的瞬态证据：在高亮出现时判断「这帧将来有用」并存原图。RoboMME 发现保留关键帧原图的 MemER 在动态场景变化类任务上最强（54.67），支持存原图关键帧的路线；Counting 套件对应 EventVLA 的 Press Button Keyframe（n=2–5）。
- **TRACE**（2606.14551）的路径签名是机器人状态轨迹的有序特征，天然适合 Imitation 套件里 PatternLock、RouteStick 这类复现轨迹与绕行方向的过程记忆；RoboMME 在这两项上符号记忆几乎为零（6.67 / 6.00），FrameSamp+Modul 为 53.56 / 66.67，过程记忆需要低层运动信息。其顺序反转负对照可搬到 VideoPlaceOrder 这类要求顺序的任务上。
- **SAI**（2606.16490）是双移动机械臂的协同问题，RoboMME 把移动操作留作未来工作；SAI 靶向的过早释放属于时间记忆里的阶段判断，与 Counting 套件「何时按停止按钮」同类。三篇核心论文合起来覆盖时间（EventVLA 计数、SAI 阶段）、空间/物体（EventVLA 遮挡证据、TRACE 目标选择）与过程（EventVLA Reproduce Route）记忆，但都没有 RoboMME 数字。

## 关联阅读

- MemER（2510.20328）：本文最强的外部基线，关键帧图像 + 语言子目标的混合记忆。
- SAM2Act（2501.18564）：MemoryBench 的提出者，本文以其记忆库 + 离散路点动作为基线。
- ContextVLA（2510.04246）：历史视觉 token 直接拼入输入，本文 Perceptual+Context 一族的代表。
- Mem（2603.03596）：多尺度具身记忆，本文的符号记忆刻意去掉了其推理链以便标准化。
- MIKASA-Robo（2502.10550）：被本文批评为步长短、演示不足的 RL 取向记忆基准。
