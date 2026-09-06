<!-- handwritten -->
# MemER: Scaling Up Memory for Robot Control via Experience Retrieval

> **arXiv 2510.20328** · arXiv 2025 · 提交 2025-10-23 · 分类 `agentic` / 双系统、智能体与符号记忆
> *Ajay Sridhar, Jennifer Pan, Satvik Sharma, Chelsea Finn*
> [arXiv](https://arxiv.org/abs/2510.20328) · [PDF](https://arxiv.org/pdf/2510.20328) · [仓库内英文 PDF](../papers/pdf/MemER_2510.20328.pdf) · [中文翻译 PDF](../papers/zh/MemER_2510.20328_zh.pdf)

## 一句话定位

MemER（ICLR 2026）是双系统记忆：高层 Qwen2.5-VL-7B 以约 1 Hz 看最近 8 帧（2 Hz 采样，约 4 s）加至多 8 张已选关键帧，输出低层 π₀.₅ 要执行的文本子任务，同时从近期帧里提名值得记住的帧；提名索引经 1D 单链接聚类（d = 5）取中位数固化为关键帧，只增不删。三个需要数分钟记忆的 DROID 真机任务、每任务 20 trials，全部 >90%，与人类给子任务的上界持平。最该记的数字：Counting 任务错误舀取次数 MemER 1，No History 61，Long History（32 帧）12。

## 解决什么问题

给通用 VLA 加分钟级视觉记忆。直接拉长历史有两个代价：算力——32 帧（约 16 s）就要 1 s 推理，已到闭环可容忍的上限；脆弱——长上下文与专家动作之间的伪相关在策略自身的状态分布下失效，误差随历史变长复合。无差别下采样则塞进无关或重复的帧。已有的上下文扩展（Past-Token Prediction、SAM2Act）最多两打帧或 N = 10 最近帧，MemER 要从上千帧的整段 episode 里挑任务相关帧，且必须微调开源 VLM：API VLM 延迟 10–15 s，零样本也挑不出机器人相关的关键帧。

## 方法

**分解**：π(A_t | o_0:t) = π_l(A_t | I_t, q_t, l'_t) · π_h(l'_t, J_t | I_{t−N+1:t}, K_t)（Eq. 3）。记忆只存在于高层。

**高层**：Qwen2.5-VL-7B-Instruct，冻结视觉编码器与投影层只训 LLM，4500 步、batch 256、96 H200 GPU 时，三任务合训一个模型。输入：任务指令 + 已选关键帧 K_t（实践 |K_t| ≤ 8）+ 最近 N = 8 帧视频（第三人称 + 腕部两路相机）；输出 JSON，含 current_subtask 与 keyframe_positions（1–8 的索引）。

**写入与固化**：每步提名的候选帧索引 J_t 汇入有序列表（保留重复），相邻索引距离 ≤ d = 5 的归为一簇，每簇取中位数为代表帧，代表帧集合即 K_t。重复提名让中位数偏向被多次选中的帧；早于 t − N + 1 − d 的簇不再重算。没有删除机制。

**低层**：π₀.₅ 的 DROID 检查点微调，条件于子任务文本 + 当前图像 + 关节状态，马尔可夫；三任务共用一个策略，每任务 50 条长程演示 + 10–15 条干预演示（从常见失败状态遥操作回到分布内），18000 步、batch 128、48 H200 GPU 时；输出 15 步动作 chunk（15 Hz），开环执行 8 步。

**标注**：子任务由操作员采集时按键切分。关键帧半自动：取子任务边界帧为候选，每类子任务人工定一条规则（取首帧、末帧或不取，如 "look inside the bin" 取末帧，"reset scooper position" 不取），每段至多一帧。

**模型合并**：θ = 0.2 θ_pre + 0.8 θ_ft（α = 0.8），找回微调后丢掉的对低层卡顿、重试的鲁棒性（Fig. 6 右）。

**部署**：π_h 约 1 Hz、π_l 约 2 Hz，各在独立服务器异步运行；图像 320×180，15 Hz 流按 2 Hz 入队。

## 关键数字

Franka + 平行夹爪，ZED 第三人称 + miniZED 腕相机；每任务 20 trials。Object Search 每 trial 找三个物体，每列满分 60；Dust & Replace 每列满分 20。

| 指标 | MemER | No History | Short History (8 帧) | Long History (32 帧) | Human HL |
|---|---|---|---|---|---|
| Object Search 取回次数 ↑ | 59 | 32 | 38 | 47 | 58 |
| Object Search 最优路径次数 ↑ | 57 | 25 | 31 | 41 | 58 |
| Counting 错误舀取数 ↓ | 1 | 61 | 26 | 12 | 0 |
| Dust & Replace 擦下层 / 擦上层 ↑ | 20 / 19 | 5 / 4 | 14 / 14 | 11 / 11 | 19 / 19 |
| Dust & Replace 放回下层 / 上层 ↑ | 18 / 20 | 5 / 7 | 11 / 12 | 12 / 12 | 18 / 17 |

模态消融（同协议）：Short History + Text 取回 40 / 最优 28 / 错舀 10 / 擦 16, 16 / 放回 7, 10；MemER + Text 59 / 49 / 13 / 20, 18 / 17, 20。加文本反而更差，尤其 Counting。

离线子任务预测（轨迹准确率 / 边界准确率，Object Search、Counting、Dust & Replace）：MemER 0.80/0.76、0.67/0.65、0.87/0.86；GPT-5 0.15/0.16、0.43/0.47、0.67/0.63；Gemini Robotics-ER 1.5 0.21/0.23、0.13/0.14、0.19/0.22。API 模型在线部署因 10–15 s 延迟全部失败。

## 局限与注意

论文自述：关键帧只增不删，小时级任务会撑爆；吞吐受 VLM 与 1 Hz / 2 Hz 调度限制，反应慢；记忆只有视觉；单一本体。

我的读法：
- 记忆只在高层，低层 π₀.₅ 马尔可夫、只收文本子任务，凡是子任务词表表达不了的信息（物体的精确位置）都到不了执行器。UniMem 正是攻这一点：TableClean 13%、TapScoopPour 7%；EventVLA 的复现里 RMBench 8.7%（低于无记忆 π₀.₅ 的 10.4%）、RoboTwin-MeM 10.5%。
- 子任务词表封闭且逐任务写死，高层实际是在一个小动作列表上做选择；关键帧规则也是逐子任务手定的首帧/末帧。监督是子任务级的，KEMO 批评的就是这个。
- 所有基线共用同一低层、同一分层结构，只改高层输入；没有端到端记忆 VLA 基线，没有公开基准，三个任务自建、各 20 trials，59 vs 58 在噪声内。
- Dust & Replace 测试用训练 17 个物体中低层能抓的 9 个，Object Search 训练测试同 15 个物体，数字略偏乐观。
- 「文本有害」与 UniMem 的结论相反，但两者存的文本不同：MemER 存高层自己预测、可能出错的子任务，UniMem 存分类器判定的事件名。
- 成本：7B VLM 独占一台服务器以 1 Hz 运行，每次查询 2 路 × 8 帧 + ≤ 8 张关键帧；训练 96 + 48 H200 GPU 时。

## 与核心论文的关系

EventVLA 把 MemER 当双系统基线：RMBench 8.7%（π₀.₅ 无记忆 10.4%，EventVLA 仅锚帧 67.8%），RoboTwin-MeM 10.5%（EventVLA 75.2%）。这与 MemER 自报的 >90% 不矛盾，是基准性质不同：RoboTwin-MeM 要求低层看到瞬态证据（哪只杯子），文本子任务带不动这种信息，除非词表预先编码了它。存什么：两者都存原图关键帧，但 MemER 只给 VLM 规划器看，EventVLA 把帧拼进执行 VLA 的视觉编码器；容量 MemER ≤ 8 张 + 每相机 8 张近期帧且不删，EventVLA 5 槽 FIFO + 锚帧。何时写：MemER 由 VLM 从刚滑出 8 帧窗口的帧里回顾式提名，再用 d = 5 单链接聚类 + 中位数去抖；EventVLA 的 KEM 头前瞻式预测未来 50 步哪些会成为关键帧，用 1-D NMS + 冷却去抖。监督：MemER 是子任务边界上的首帧/末帧规则，EventVLA 是 Qwen3-VL-235B 软标签。

与 TRACE 处于两个极端：TRACE 是 latent、无标签、每步门控写入 4/6 槽、挂在 ACT/DP 上，路径签名提供「我在轨迹哪一段」的进度信号；MemER 是显式图像 + 文本、1 Hz、7B VLM，进度靠近期帧加关键帧推断。与 SAI：SAI 的层级在两个智能体（两臂）之间而非抽象层级之间，其 30 步 GRU 历史 token 相当于 MemER 证明不够用的 Short History（错舀 26 次）；MemER 每任务 10–15 条从失败状态出发的干预演示，与 SAI 第三阶段的 DAgger 干预是同一类数据。

## 关联阅读

- Hi Robot（2502.19417）：MemER 直接沿用的分层 VLA 模板，No History 基线即此。
- Past-Token Prediction（2505.09561）：Counting 任务的出处，也是「长上下文引入伪相关」论证的来源。
- SAM2Act（2501.18564）：N = 10 最近帧的记忆架构，MemER 对比的短上下文代表。
- UniMem（2608.22869）：把记忆直接给低层，真机 80.0 vs MemER 43.5。
- EventVLA（2606.20092）：把 MemER 当双系统基线，RoboTwin-MeM 10.5%。
