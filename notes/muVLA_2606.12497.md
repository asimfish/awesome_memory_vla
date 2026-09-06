<!-- handwritten -->
# $μ$VLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models

> **arXiv 2606.12497** · arXiv 2026 · 提交 2026-06-10 · 分类 `latent` / latent 状态、循环与槽记忆（TRACE 一族）
> *Egor Cherepanov, Nikita Kachaev, Daniil Zelezetsky, Aydar Bulatov, Artem Pshenitsyn, Yuri Kuratov, Alexey Skrynnik, Aleksandr I. Panov, Alexey K. Kovalev*
> [arXiv](https://arxiv.org/abs/2606.12497) · [PDF](https://arxiv.org/pdf/2606.12497) · [仓库内英文 PDF](../papers/pdf/muVLA_2606.12497.pdf)

## 一句话定位

μVLA 是一项受控隔离研究：在 OpenVLA-OFT 里只加 m 个跨步携带的可学习记忆 token，用 TBPTT 端到端训练，无辅助损失、无结构改动，让循环成为唯一变量。MIKASA-Robo 五个训练任务平均成功率 0.42 → 0.84（m=64，K=2）。最值得记住的是 TBPTT 长度的 U 形曲线：K=2 在 RememberColor5 达 0.93，K=1 与 K=8 只有 0.40 / 0.35。

## 解决什么问题

VLA 从当前观测预测动作块，部分可观测下决策所需的信息已不可见。已有记忆 VLA 同时引入循环、检索、压缩、辅助目标、层级记忆或专用结构改动（ReMem-VLA 的 EMA 更新加过去观测预测损失、AVA-VLA 的信念状态加额外损失、MemoryVLA 的记忆库），循环本身的贡献无法从这些机械中剥离。论文回答四个问题：能否在微调阶段给无记忆预训练 VLA 加循环；跨步梯度是否必要、截断多长合适；记忆语义迁移时表现如何；全可观测任务是否退化。

## 方法

- **存什么**：m 个 d=4096 维记忆 token M_t，插在 OpenVLA-OFT 输入序列的 PROPRIO 与 TEXT 之间。M_0 = M^init 为共享可学习参数；t ≥ 1 时 M_t 取上一步前向中记忆位置的隐藏状态，一次前向同时完成读与写。m=64 为主设定，m=1 为带宽探针。
- **注意力掩码守卫**：OpenVLA-OFT 是双向注意力，记忆若能看动作 token，会退化为 M_t = φ(ACTION_t) 的自指解，什么环境信息都不存。把 context→action 块置零，只让动作 token 读全上下文。去掉守卫后 RememberColor5 0.44 → 0.25，而运动主导的 ShellGamePush 0.77 → 0.94，记忆转向编码动作轨迹。
- **数据管线**：round-robin 分集加载器，B 条独立流各自逐步走完一条 episode，is_first 标志按流重置到 M^init，取代原 RLDS 打乱单步采样。
- **写入规则**：TBPTT 累积 K 步 L1 chunk 损失后一次反传，仅在截断边界 detach；EMA 变体 M_{t+1} = α M'_t.detach() + (1−α) M_t.detach()，α=0.1，反传限于单步。
- **训练**：从 OpenVLA 权重起，LoRA r=32 加记忆位置嵌入与 M^init，AdamW lr 5e-4，8×H100，最多 150k 步，H=8，两视角 224×224。
- **推理**：receding-horizon，每个环境步重查询、只执行 chunk 首动作，使记忆更新节奏与训练一致。同一 K=8 检查点改成 H=8 开环执行，LIBERO Long-10 从 95.8 跌到 5.4，Goal 从 96.6 跌到 35.8。
- **监督**：只有动作 L1 损失。

## 关键数字

| 基准 / 协议 | 对比项 | 数字 |
|---|---|---|
| MIKASA-Robo-VLA 5 个训练任务，每环境 100 个固定 seed 回合 | π0.5 / OpenVLA-OFT / OFT 分集加载器 / m=1,K=8 / m=64,K=8 / K=1 / EMA / **K=2** / 首帧 oracle | 0.46 / 0.42 / 0.48 / 0.54 / 0.57 / 0.57 / 0.57 / **0.84** / 0.85 |
| RememberColor5 | OFT / OFT 分集 / K=1 / K=8 / EMA / K=2 / 首帧 oracle | 0.04 / 0.09 / 0.40 / 0.35 / 0.44 / **0.93** / 0.96 |
| TakeItBack（线索不在首帧） | OFT 分集 / 首帧 oracle / K=2 | 0.87 / 0.94 / **0.99** |
| 11 个同记忆语义留出任务平均 | OFT / OFT 分集 / K=2 / 首帧 oracle | 0.01 / 0.07 / **0.23** / 0.24 |
| 7 个新记忆语义留出任务平均 | OFT 分集 / 其余循环变体 / K=2 / 首帧 oracle | 0.07 / 0.09–0.11 / 0.16 / 0.19 |
| LIBERO 四套件平均（每子任务 50 回合） | OpenVLA-OFT / MemoryVLA / CronusVLA / μVLA K=8 / μVLA EMA | 97.1 / 96.5 / 86.2 / 96.2 / 44.8% |
| 因果干预（K=2，100 回合） | 记忆换高斯噪声：RC5 / TakeItBack；冻结首步记忆：RC5 / InterceptMedium | 0.94 → 0.09 / 0.99 → 0.21；0.36 / 0.07 |
| 阶段长度外推 RC5（训练 N ≤ 5） | K=2 在 N=3 / N=20；K=8 全程；EMA N ≥ 20 | 0.93 / 丢约 75%；0.31–0.38；< 0.15 |
| 代价（RC5 评测） | OFT 开环 vs μVLA：前向延迟 / 闭环吞吐 | 61.3 vs 66.7–68.3 ms / 20.9 vs 9.1–9.3 Hz |
| 训练时长（8×H100） | OFT 分集 / K=1 / EMA / K=2 / K=8 | 22h41m / 1d3h / 1d2h / 2d18h / 12d0h |

## 局限与注意

- **正确基线是分集加载器版 OFT（0.48）而非原始 OFT（0.42）**，作者自己指出数据顺序就贡献 6 点；记忆带宽 m 从 0 到 1 加 6 点、1 到 64 只加 3 点，主要杠杆是 K。
- **K=2 的优势是分布内的**：阶段长度超出训练范围后 K=2 掉得最快，K=8 低而平，论文明说 TBPTT 不面向任意长程记忆。首帧 oracle 在线索位于首帧的任务上与 K=2 持平或更好（RC5 0.96 vs 0.93），只有 TakeItBack 这类线索不在首帧的任务证明循环是必要的。
- **新记忆语义几乎不迁移**：Rotate 家族全部接近零，RememberShape 只有部分迁移。"能力包络"的措辞诚实，但也意味着 m=64 单一循环状态不是通用记忆。
- **成本**：receding-horizon 让闭环吞吐减半以上；K=8 训练 12 天，K=2 近 3 天，是无记忆基线的近 3 倍。7B 骨干加 LoRA r=32，可训练参数量未单独给出。
- **未评估**：仅仿真、脚本 oracle 示教，无真机；LIBERO 只报 K=8 而未报最强的 K=2；与 MemoryVLA、CronusVLA 的对比取自他人论文数字，训练配方不同，不能当作严格胜出。

## 与核心论文的关系

- **与 TRACE 同属 latent 循环记忆但更极简**：TRACE 用固定 K 槽、path signature 寻址、门控写入、三项稳定器损失、适配器外挂在 ACT / DP；μVLA 把记忆放进 7B 骨干的自注意力，无寻址（记忆 token 经注意力自行读写）、每步无门控写入、容量 m×4096、零辅助损失。两者都表明训练信号决定成败：TRACE 靠稳定器损失，μVLA 靠跨步梯度（K=1 detach 后只有 0.57）。μVLA 的 EMA 变体（0.57）与 ReMem-VLA 的 detached EMA 更新同类，被判定不足以精确保持线索。
- **与 EventVLA 是两个极端**：EventVLA 存 5 槽原始关键帧、KEM 头显式预测何时写、吞吐 2.91 → 0.94 Hz；μVLA 存不可读的连续 token、每步写，吞吐 20.9 → 9.1 Hz 主要来自 receding-horizon 而非记忆本身（前向延迟只增 5–7 ms）。μVLA 观察到记忆 token 的余弦变化在阶段转换处出现尖峰，并提出可作为学到的关键帧信号，与 KEM 思路呼应。EventVLA 的隐式 latent bank 消融（24.9%）与 μVLA 的正面结果不矛盾：μVLA 的循环状态经 TBPTT 端到端训练且有动作拷贝守卫。
- **与 SAI**：SAI 的 30 步 GRU 历史 token 也是不加辅助损失的最小循环；μVLA 的隔离结论（跨步梯度加训练/推理节奏对齐）为这类设计给出可迁移的经验规则。

## 关联阅读

- Recurrent Memory Transformer（arXiv 2207.06881）：μVLA 的原型，记忆 token 跨段携带；本文把它降到环境步级并加动作守卫。
- MIKASA-Robo（arXiv 2502.10550）：主基准，按线索回忆 / 遮挡 / 序列预测三类记忆结构组织任务。
- ReMem-VLA（arXiv 2603.12942）：帧级与 chunk 级循环 query 加 EMA 更新与辅助损失，本文 EMA 变体的对照原型。
- CronusVLA（arXiv 2506.19816）：多帧后训练的压缩上下文路线，LIBERO 与 MIKASA 表中的语境对比。
- RoboMME（arXiv 2603.04639）：14 种 π0.5 记忆变体的受控研究，与本文同属隔离记忆机制的方法学。

