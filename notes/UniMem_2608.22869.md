<!-- handwritten -->
# UniMem: Unifying Multimodal Memory and Control for Vision-Language-Action Models

> **arXiv 2608.22869** · arXiv 2026 · 提交 2026-08-24 · 分类 `event` / 事件与关键帧记忆（EventVLA 一族）
> *Lars Osterberg, Maggie Wang, Mac Schwager*
> [arXiv](https://arxiv.org/abs/2608.22869) · [PDF](https://arxiv.org/pdf/2608.22869) · [仓库内英文 PDF](../papers/pdf/UniMem_2608.22869.pdf) · [中文翻译 PDF](../papers/zh/UniMem_2608.22869_zh.pdf)

## 一句话定位

UniMem 把「何时记」和「记什么」都放进 π₀.₅ 单一骨干：最后一层 latent 上的 MLP 事件头一旦预测出非 null 事件，就把事件名追加进文本历史、把当前多视角原图存入关键帧集合（3 张历史 + 当前帧），再经加了时间注意力的 SigLIP 读回。仿真五任务平均 93.4%（固定 6 s 间隔采帧的 π₀.₅+V.E. 为 68.2%），真机四任务 80.0%（MemER 43.5%）；靠缓存关键帧 hidden state，推理保持约 90 ms 的单帧速度。

## 解决什么问题

Perceptual aliasing：观测几乎相同、正确动作却取决于历史（拿起再放回、数第几勺）。作者批评两条路线：分层方案（MemER、MEM、Hi Robot）让额外的 VLM 管记忆、只给 VLA 发文本子任务，执行器拿不到过去画面里的空间细节，流水线割裂、延迟高；多帧输入若按固定间隔取帧则引入与动作无关的伪相关，反而拉低成绩。UniMem 要事件驱动、文本 + 视觉双模态、单模型端到端。

## 方法

**存什么**：文本记忆 M_t 是事件词表 E 中的离散事件名，以自然语言追加到指令上（"History: human tap, grabbed spoon, …"），起始为空。视觉记忆 H_t 是事件时刻的多视角原图 {I_wrist, I_ext}，起始只含初始场景帧；受训练算力限制容量为 3 个历史里程碑 + 当前帧（|K| ≤ 4，仿真用 3、真机用 4），超出丢最旧。

**何时写**：事件头 f_φ（MLP）读 backbone 最后一层本应生成文本 token 的 latent z_t，输出 E ∪ {null} 上的分布，argmax 非 null 即触发写入（Eq. 1），文本与视觉同时写。z_t 已注意过 M_t 与 H_t，分类器因此条件于全部历史，构成递归回路。记忆只增不删：漏检下一步还能补，误检则永久污染两种记忆，因此 null 类不屏蔽而是降权 w_null = 0.02。

**如何读**：改 π₀.₅ 的 SigLIP，每隔几层在空间注意力之间插入因果时间自注意力，复用该层自身的 QKV 与 LayerNorm 权重（配置取自 MEM 与 TimeSformer）。缓存：历史关键帧在时间注意力之前的 hidden state 被缓存，新帧到来只平移位置嵌入、不重算空间注意力，当前帧独自作 query。

**监督**：L = L_a + λ L_e，λ = 0.1；L_a 是不变的 flow-matching 损失，L_e 是类别加权交叉熵，梯度回传到共享 LM trunk。标签由 Claude Sonnet 5.0 生成的脚本按本体感知动作签名（gripper 闭合、roll/pitch 模式）自动打，事件窗口取检测点前 5 帧到后 20 帧，人工抽查后改脚本；M_t 只在事件窗口结束后才更新以防泄漏。训练时从每个过去事件窗口均匀采一帧组成 H_t。全部模型 LoRA 微调；BeanScoop、TapScoopPour 上把决策时刻的采样概率上调约 4×。

## 关键数字

仿真 robosuite Franka Panda，每任务 N = 25；真机 xArm6，每任务 N = 15，人工判定子任务二值成功，real-time chunking 约 10 Hz。UpDown3Times 报子任务平均成功率，UpDownSpatial 报放回位置精度分。

| 仿真任务 | π₀.₅+V.E.（6 s 定间隔，同编码器） | No Memory | Text Only | Keyframe Only | UniMem |
|---|---|---|---|---|---|
| UpDown | 84 | 52 | 96 | 92 | 100 |
| UpDown3Times | 16 | 22 | 93 | 23 | 96 |
| OccludedTap | 96 | 60 | 88 | 100 | 96 |
| UpDownSpatial | 49 | 6 | 30 | 52 | 79 |
| PlateRecall | 96 | 8 | 20 | 96 | 96 |
| 平均 | 68.2 | 29.6 | 65.4 | 72.6 | 93.4 |

| 真机任务 | MemER | No Memory | Text Only | Keyframe Only | UniMem |
|---|---|---|---|---|---|
| HammerMeasure | 87 | 13 | 53 | 53 | 87 |
| BeanScoop | 67 | 0 | 27 | 20 | 93 |
| TableClean | 13 | 0 | 0 | 47 | 80 |
| TapScoopPour | 7 | 7 | 7 | 27 | 60 |
| 平均 | 43.5 | 5.0 | 21.8 | 36.8 | 80.0 |

延迟（RTX 4090）：四路相机、16 个关键帧的上下文只比双相机单帧基座多约 25 ms；正文称比分层记忆基线快 6×。

## 局限与注意

论文自述：未在数十分钟到小时级任务上验证；没有记忆编辑（剪枝、整合）；关键帧标注依赖离线自动脚本和预定义事件词表；只有一条几分钟的时间上下文，不分短期长期。

我的读法：
- 事件词表逐任务预定义、标签来自人工核对的规则脚本，TapScoopPour 的人类敲击还是采集时手动打标：这是子任务级监督，「统一」指架构而非去掉标注。
- 容量只有 3 张历史帧：Keyframe Only 在 UpDown3Times 只有 23%，部分是容量装不下三次循环，靠文本记忆补。
- 所有消融都带事件头辅助损失训练，No Memory 不是原版 π₀.₅，辅助损失本身对骨干的影响没被拆出来。
- 真机 MemER 基线由作者自己 LoRA 微调低层 π₀.₅（附录 B），高层如何训练、用多少演示未交代；N = 15，一次 trial 值 6.7 个点。
- 仿真基线 π₀.₅+V.E. 用 UniMem 自己的编码器、只换取帧规则，是选帧规则的消融，不是与 MemoryVLA、EventVLA 类方法的比较；九个任务全是自建，没用 RMBench、MIKASA-Robo 等公开基准。
- 93.4 的平均混合了二值成功、子任务平均、空间精度三种度量；正文里 Keyframe Only 在 TableClean 的 53% 与表 II 的 47% 不一致，前者应是阶段成功率。
- 决策时刻 4× 过采样是与 KEMO 损失加权同类的训练技巧，是否也用于基线未说明。

## 与核心论文的关系

与 EventVLA 最近：都在 VLA 最后一层 hidden state 上接头决定关键帧，都存原图（EventVLA 5 槽 FIFO，UniMem 3 张历史 + 当前帧、丢最旧），都以初始帧作锚，都把帧送回 VLM 的视觉编码器。四点不同。预测目标：EventVLA 的 KEM 头对未来 50 步中每一步输出「将成为关键帧」的概率（前瞻式，阈值 0.55 + NMS + 冷却），标签是 Qwen3-VL-235B 的软标签；UniMem 的头对当前步做离散语义事件分类（回顾式，argmax），标签是 Claude 写的本体感知规则脚本。记忆模态：EventVLA 纯视觉；UniMem 把事件名写进指令，且发现计数任务离不开它（UpDown3Times 文本 93 vs 关键帧 23）。读出成本：EventVLA 把帧当额外视觉 token 拼接，吞吐 2.91→0.94 Hz；UniMem 改 SigLIP 加时间注意力并缓存 hidden state，保持约 90 ms，补的正是 EventVLA 付出的代价。短期窗：EventVLA 保留，UniMem 没有。

与 TRACE：TRACE 每步门控写入 4/6 个 512 维 latent 槽、以路径签名寻址、无需标签；UniMem 只在事件时写显式图像 + 文本、按时间顺序寻址、需要事件标签。与 SAI 的 30 步 GRU 历史 token 没有机制重叠，只有 TapScoopPour「等人敲杯再动」与 SAI 的伙伴条件时序问题相似。UniMem 未被任何核心论文用作基线（2026-08，晚于 EventVLA）；它和 EventVLA 用了同一个双系统基线 MemER，数字分别是真机 43.5% vs 80.0% 与 RoboTwin-MeM 10.5% vs 75.2%，协议不同。

## 关联阅读

- EventVLA（2606.20092）：设计最接近的对照，学习式未来关键帧头 vs 事件分类头。
- MemER（2510.20328）：被 UniMem 在真机上击败的分层基线（43.5 vs 80.0）。
- MEM（2603.03596）：VLM 文本摘要 + 固定间隔帧，UniMem 的时间注意力 SigLIP 配置取自它。
- KEMO（2606.23589）：规则式事件检测的同族方案，没有文本记忆。
- Past-Token Prediction（2505.09561）：长上下文带来伪相关的论证来源，是 UniMem 事件驱动选帧的动机。
