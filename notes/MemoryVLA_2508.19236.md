<!-- handwritten -->
# MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation

> **arXiv 2508.19236** · arXiv 2025 · 提交 2025-08-26 · 分类 `dense` / 稠密与压缩的视觉历史
> *Hao Shi, Bin Xie, Yingfei Liu, Lin Sun, Fengrong Liu, Tiancai Wang, Erjin Zhou, Haoqiang Fan, Xiangyu Zhang, Gao Huang*
> [arXiv](https://arxiv.org/abs/2508.19236) · [PDF](https://arxiv.org/pdf/2508.19236) · [仓库内英文 PDF](../papers/pdf/MemoryVLA_2508.19236.pdf) · [中文翻译 PDF](../papers/zh/MemoryVLA_2508.19236_zh.pdf)

## 一句话定位

MemoryVLA（ICLR 2026）在 CogACT 式的「7B Prismatic VLM + DiT 扩散动作专家」外挂一个每步写入的双流记忆库 PCMB：感知流每条 256 个压缩视觉 token，认知流每条 1 个 LLM EOS token，交叉注意力检索、门控融合，满了就合并最相似的相邻两条。只用单张第三人称 RGB：SimplerEnv-Bridge 71.9%（比 CogACT-Large +14.6）、Fractal 72.7%、LIBERO 五套 96.5%、MIKASA-Robo 41.2%（比 π₀ +11.8）、真机 12 任务 84.0%，长程时序任务比 CogACT +26；推理延迟只比无记忆基座多 3.6%（0.187→0.194 s）。

## 解决什么问题

主流 VLA（OpenVLA、π₀）只看当前帧，而操作任务非马尔可夫：Push Buttons 按前按后画面几乎一样，单帧无法判断是否已按过。直接把多帧拼给 VLM 有两个问题：自注意力二次复杂度限制上下文；多帧输入偏离 VLM 单帧机器人预训练分布。已有时序建模各有代价：Octo、RoboVLMs 的交错视频格式实现复杂、算力大；RoboFlamingo 用 LSTM 传一个粗 latent，丢掉细粒度感知；TraceVLA 把轨迹画到图上，丢掉语义；UniVLA 把历史动作放进 prompt，只是 CoT。MemoryVLA 主张同时保留细粒度感知与高层语义，放在 VLM 之外的库里按需检索。

## 方法

**骨干**：Prismatic 7B VLM（DINOv2 + SigLIP 并联 → LLaMA-7B），OXE 预训练；输入单张 224×224 第三人称 RGB + 指令。视觉 token 经 SE-bottleneck 压成 N_p = 256 个感知 token p；LLM 的 EOS 位置输出作为 1 个 4096 维认知 token c。二者合称工作记忆。

**存什么、何时写**：PCMB 有感知、认知两条流，每流最多 L 条。每一步都写，写入的是门控融合之后的 p̃、c̃——库里存的是已含检索结果的特征，不是原图。

**如何读**：以当前 p、c 分别为 query，对本流 L 条记忆做 scaled dot-product 注意力，key 加按 episode 时间步的正弦编码 TE(t_i)，value 不加（Eq. 5–6）；接 FFN 成一层 Transformer，堆两层得 H^p、H^c。融合 g^x = σ(MLP([x; H^x]))，x̃ = g^x ⊙ H^x + (1 − g^x) ⊙ x（Eq. 7–8）。

**容量**：超过 L 时在每流内算相邻条目余弦相似度，把最相似的一对取平均合并（Eq. 9），不是 FIFO。仿真与真机通用任务 L = 16，真机长程时序任务 L = 256。

**动作头**：约 300M 参数 DiT，DDIM 10 步、CFG 1.5，预测 T = 16 步 7-DoF 动作（Δ平移、Δ欧拉角、gripper）。每个去噪步先与 c̃ 拼接过 cognition-attention，再对 p̃ 做 perception-attention；只有动作 MSE 损失，没有记忆专属损失。

**训练**：8×A100 FSDP，全局 batch 256，lr 2×10⁻⁵。dataloader 必须保持 episode 内时序：Bridge/Fractal 流式加载连续帧；LIBERO/MIKASA 每次在单个 episode 内采 16 帧并保持顺序，与 L 对齐。真机数据按末端位移 > 0.01 m 或转角 > 0.4 rad 稀疏取帧，最大间隔 120 帧。

## 关键数字

| 基准（协议） | MemoryVLA | 对照 | 备注 |
|---|---|---|---|
| SimplerEnv-Bridge，WidowX，每任务 24 trials | 71.9 | CogACT-Large 57.3；π₀-Beta* 68.4 | * open-pi-zero 复现，用本体状态 |
| SimplerEnv-Fractal 总体（VM 77.7 / VA 67.7），336 变体 | 72.7 | CogACT 68.1（74.8 / 61.3） | Open/Close Drawer VA +24.9 |
| LIBERO 五套均值，每任务 50 trials | 96.5 | CogACT 93.2（复现）；π₀* 94.2 | Long-10 93.4，Long-90 95.6 |
| MIKASA-Robo 五任务，每任务 100 episodes | 41.2 | π₀ 29.4；CronusVLA 18.0（复现） | ShellGameTouch 88 vs 33；Intercept 24 低于 π₀ 42 |
| 真机 General 六任务，15 trials | 85 | CogACT 76 | |
| 真机 Long-horizon 六任务，10–15 trials，分步计分 | 83 | CogACT 57；π₀ 52 | Seq. Push Buttons 58 vs 15 |
| 推理，RTX 4090，bf16，300 次 | 0.194 s / 16.6 GB | 基座 0.187 s / 15.8 GB | HGX H20 上 0.246 vs 0.236 s |

Bridge 消融（4 任务 × 24 trials 均值）：

| 因素 | 变体 → 成功率 |
|---|---|
| 记忆类型 | 仅认知 63.5 / 仅感知 64.6 / 双流 71.9 |
| 记忆长度 L | 4: 67.7 / 16: 71.9 / 64: 67.7 |
| 检索时间编码 | 无 69.8 / 有 71.9 |
| 融合 | 相加 67.7 / 门控 71.9 |
| 整合 | FIFO 66.7 / 相邻合并 71.9 |
| 真机 Clean Table & Count 的 L | 64: 78 / 256: 84 / 512: 81 |

## 局限与注意

论文没有单列局限，结论只给未来方向（把长期记忆对齐到 LLM 输入空间做 embedding 级 CoT；终身记忆整合）。附录 B 承认相机视角变化下掉得厉害：Pick Coke Can 92.0 → 42.0。

我的读法：
- 这是稠密记忆：每步都写、没有事件选择，压缩靠合并相邻相似项，而且写入的是融合后的特征，库内容递归地包含自身检索结果。EventVLA 对「冗余淹没稀疏证据」的批评针对的正是这类设计。
- 消融差距很小：Bridge 96 次 trial 上 69.8 vs 71.9 差 2 个点约等于 2 次 trial；Bridge、LIBERO、MIKASA 都是每隔若干步验证并报告最佳验证步，等于在评测集上选 checkpoint。
- 基线处理总体公平且对自己不利：π₀ 在 Bridge 用本体状态、在 LIBERO 用腕相机 + 本体，MemoryVLA 只用第三人称 RGB；CogACT 重新复现。
- MIKASA-Robo 均值领先，但 Intercept Medium 24 低于 π₀ 的 42，RememberColor9 只有 20；增益主要来自 ShellGameTouch。
- 真机长程任务分步给分（30/30/30 + 10 奖励之类）、每任务 10 次，83 是分数不是二值成功率；L 在长程任务上改成 256，逐套调。
- LIBERO/MIKASA 训练时记忆一次只见同一 episode 内采出的 16 帧，测试时 episode 长达 505 步、记忆持续累积合并，训练/测试记忆跨度不一致，论文未讨论。
- 表 15 的 82.5 Hz 是按 16 步 chunk 折算的动作吞吐，不是控制频率。

## 与核心论文的关系

在写入策略上与 EventVLA 处于两端：EventVLA 只把预测为关键帧的原图写进 5 槽 FIFO，MemoryVLA 每步写融合特征再靠合并压缩。EventVLA 把它当帧缓冲范式的代表基线：RMBench 41.7%（QwenOFT 骨干）/ 19.4%（OpenVLA 骨干），对比 EventVLA 仅锚帧 67.8%；RoboTwin-MeM 10.8% 对比 75.2%。KEMO 也拿它当记忆基线，六个真机双臂任务聚合 TSR 1.4% 对比 KEMO 51.4%，但那是单相机 Prismatic 骨干对三相机 π₀.₅。两处复现都换了骨干和输入，测的不只是记忆机制。

机制上最接近 TRACE：都是挂在骨干之外、注意力读出、带门的 latent 记忆。差别在：TRACE 固定 K = 4/6 个 512 维槽，用机器人状态轨迹的路径签名寻址，每步门控写入，配三个稳定损失；MemoryVLA 每流 L = 16（或 256）条，寻址靠内容相似度（当前 token 作 query）加正弦时间编码，写入无条件、门在读端，没有记忆专属损失，溢出靠合并而非覆盖。容量：MemoryVLA 16 × (256 + 1) ≈ 4112 个 token，TRACE 4–6 个向量，EventVLA 5 张原图。成本：MemoryVLA 报 +3.6% 延迟，EventVLA 报 2.91→0.94 Hz，硬件和模型都不同，只能说 MemoryVLA 落在便宜的一端。SAI 的 30 步 GRU 历史 token 与 MemoryVLA 的认知流（每步 1 个 token）同为单向量摘要，一个递归、一个检索。

## 关联阅读

- CogACT（2411.19650）：MemoryVLA 的基座架构与主要对照。
- CronusVLA（2506.19816）：滑窗聚合多帧 VLM 特征，MemoryVLA 在 MIKASA-Robo 上复现的时序基线（18.0）。
- MIKASA-Robo（2502.10550）：唯一用到的公开记忆基准。
- EventVLA（2606.20092）：把 MemoryVLA 当帧缓冲基线，RMBench 41.7%。
- KEMO（2606.23589）：真机双臂任务上把 MemoryVLA 当记忆基线，聚合 TSR 1.4%。
