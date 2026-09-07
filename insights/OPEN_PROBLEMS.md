# 研究机会清单：记忆 VLA 里还没人占的 14 个位置

每条按「为什么重要 / 最小可行实验（MVE）/ 相关解读」组织。MVE 的标准是：一个人、一块 GPU、两周内能拿到第一个能证伪的数字。编号按 README 的家族顺序排列；只做一件事就做第 1 条。所有数字只取自原文，见[数字口径账本](NUMBERS_LEDGER.md)。

## A. 写入与寻址（EventVLA × TRACE 的中间地带）

### 1. 前瞻写入 × 轨迹寻址

**为什么重要**：EventVLA 学"何时写"但按时间拼接、靠注意力自己找（RoboTwin-MeM 18.0 → 75.2）；TRACE 按轨迹签名寻址但每步都写（ACT 25.5 → 69.2）。两者各占一个极端，"既学写入时机、又学寻址"的组合没人做过。稀疏写入解决容量（EventVLA 的 5 帧 FIFO 在 >10 分钟任务上会饱和），轨迹寻址解决读写对齐（TRACE 的每步写入在 2× 历史下一致性降到 0.928）。

**MVE**：在 TRACE 的 ACT 基座上加一个 KEM 式的写入门（用 EventVLA 的软标签监督，标签可用 Qwen3-VL 或 KEMO 的运动学规则生成），只在门打开时执行签名路由写入。在 TRACE 的 Book / Laundry 两个任务上比较：完整 TRACE、门控 TRACE 的阶段进度，以及 2× / 4× 延长历史下的分支一致性。预期：成功率持平、长历史一致性提升；若门控反而掉点，说明分支线索出现的时刻并不稀疏。

**相关解读**：[EventVLA](../reports/01_eventvla_cn.md) §5.3、[TRACE](../reports/02_trace_cn.md) §5.3、[KEMO](../notes/KEMO_2606.23589.md)。

### 2. 写入触发的跨任务迁移

**为什么重要**：现有触发器各有监督来源——EventVLA 用 235B 模型离线标注，KEMO 用运动学 + DINOv2 去重的规则并逐任务手调窗口（w 10–40、冷却 8–60），UniMem 训练事件分类器，OnEvoMemory 从 rollout 结果学。没有任何对照告诉我们哪种触发在未见任务上还能工作。

**MVE**：在同一个 π₀.₅ 骨干上实现三种触发（学习 / 规则 / 分类器），在 RoboTwin-MeM 的 4 个任务上训练、在另外 4 个任务上零样本测触发质量：以物理引擎真值关键帧为参照报告触发的精确率 / 召回率和时间误差，再报告下游成功率。三种触发的排序若在训练任务和留出任务上颠倒，就说明写入时机是任务特定的。

**相关解读**：[KEMO](../notes/KEMO_2606.23589.md)、[UniMem](../notes/UniMem_2608.22869.md)、[EventVLA](../reports/01_eventvla_cn.md) §2.3。

### 3. 轨迹地址的可区分性边界

**为什么重要**：TRACE 的寻址靠"不同来源走过来的路不同"。当两条分支在分岔点之前动作完全一致（线索只是颜色差异），签名地址重合，只能退化为内容路由。TRACE 的五个任务里来源都对应不同空间位置，正好落在舒适区，边界没被测过。

**MVE**：构造一个"同轨迹、异线索"任务（掀同一个盖子，颜色决定后续分支），对照 TRACE、去掉签名的无路由槽记忆（TRACE 表 3 中为 52.17）、EventVLA 式原图缓冲。预期 TRACE 掉到无路由水平，原图缓冲保持——这会把"何时用轨迹寻址、何时用内容寻址"变成可查表的结论。

**相关解读**：[TRACE](../reports/02_trace_cn.md) §5.2、[设计空间矩阵](DESIGN_SPACE_MATRIX.md)。

### 4. 高维状态下的签名

**为什么重要**：17 维状态、深度 3 的签名已是 5219 维，深度 4 为 88,740 维；人形或灵巧手的状态维数翻倍后标准签名不可用。log-signature（深度 3 为 1785 维）是论文自己点出但没做的替代。

**MVE**：在 TRACE 的公开任务数据上替换为 log-signature 与"学习的低维轨迹键"（对状态路径做 1D 卷积 + 池化），比较路由相似度、分支一致性和每步延迟（当前签名 0.52 ms）。目标是在 40 维以上状态下把地址维度压到 2000 以内且保持顺序反转负对照低于 50。

**相关解读**：[TRACE](../reports/02_trace_cn.md) §5.2、Signatory（[2001.00706](https://arxiv.org/abs/2001.00706)）。

## B. 容量、纪律与安全

### 5. 缓冲区饱和后的记忆分层

**为什么重要**：EventVLA 的 N_max = 5 + FIFO 会在事件密集的长任务上挤掉早期证据（n=5 的任务只有 48%）；MemoryWAM 的"近期帧 + 事件边界锚帧 + gist token"三层是目前的折中，但没有在同一基准上和平面记忆正面比过。

**MVE**：把 RoboTwin-MeM 的 Press Button Keyframe 扩到 n = 8、12（更多数字卡），对照 EventVLA 原版、N_max = 12 的平面缓冲、以及"事件帧满时压成一个 gist token 而非丢弃"的分层版本。报告成功率随 n 的曲线和吞吐。

**相关解读**：[EventVLA](../reports/01_eventvla_cn.md) §5.2、MemoryWAM 笔记（[notes](../notes/MemoryWAM_2606.20562.md)）。

### 6. 把"验证后才推进"搬进端到端记忆

**为什么重要**：AGM 的结论是可靠记忆靠有纪律的状态更新而非容量——进度指针只在物理证据验证子目标后推进，否则"尝试过"会被当成"完成了"。端到端方法里对应的机制只有 EventVLA 的 NMS + 冷却和 TRACE 的门控，都不检查写入内容是否被后续观测证实。

**MVE**：给 EventVLA 的事件缓冲加一个"回读验证"：写入后 k 步内若当前观测与写入帧的预测状态矛盾（用 KEM 头的下一块预测做代理），撤销写入。在 Pick-X-Times 类计数任务上对照写入撤销率与成功率。

**相关解读**：[AGM](../notes/AGM_2608.29537.md)、[HyMeS](../notes/SkillsWeightsMemoryCode_2608.09410.md)、[趋势与洞见](../reports/04_trends_insights_cn.md) 洞见 6。

### 7. 错误记忆的恢复

**为什么重要**：AGM 指出未经验证的记忆会把局部错误固化为持久的任务状态错误。EventVLA 若把一帧错误观测（遮挡、误触发）写进缓冲，论文没有讨论如何恢复；TRACE 的槽会被后续写入慢慢冲淡但没有主动纠错。

**MVE**：在 RoboTwin-MeM 上做注入实验——在推理时强制写入一帧随机历史帧，测成功率下降幅度与随后能否自恢复；对照"允许覆盖同槽"与"只追加"两种策略。这给出记忆机制的"错误容忍度"这一新指标。

**相关解读**：[AGM](../notes/AGM_2608.29537.md)、[EventVLA](../reports/01_eventvla_cn.md) §5.2。

### 8. 记忆与动作块长度的联合设计

**为什么重要**：EventVLA 的前瞻能力是动作块长度的函数：块从 50 缩到 15，成功率 75.2 → 13.6，低于不用 KEM 的 18.0。WhyChunking 又指出动作块的收益之一正是非马尔可夫表达力。需要短块高频响应的接触任务目前无法享受前瞻写入。

**MVE**：把 KEM 的预测窗口与执行窗口解耦——预测未来 50 步的关键帧概率，但每次只执行 10 步再重预测。对照原版（预测 = 执行 = 50）和短块原版（15/15），在 RoboTwin-MeM 与一个接触丰富任务上同时报告成功率与反应延迟。

**相关解读**：[EventVLA](../reports/01_eventvla_cn.md) §4.3、WhyChunking（[2608.02547](https://arxiv.org/abs/2608.02547)）。

## C. 评测与诊断

### 9. 标准化的记忆诊断

**为什么重要**：成功率不能区分"记忆在用历史"和"碰巧对了"。TRACE 的路由相似度 / 分支一致性 + 顺序反转负对照，Present-but-Not-Remembered 的探针 + 因果干预，TFP 的隐状态干预，是三套独立的诊断，但都只在各自论文里用过一次。

**MVE**：给 RoboMME 的四类任务（时间 / 空间 / 物体 / 过程）各配保序 / 破序两组历史变换，对 π₀.₅ + 帧堆叠、MemoryVLA、EventVLA、μVLA 四种记忆报告"破序后成功率下降幅度"。下降为零的记忆就是没用历史的记忆。

**相关解读**：[TRACE](../reports/02_trace_cn.md) §4.3、[Present but Not Remembered](../notes/PresentNotRemembered_2607.03372.md)、[RoboMME](../notes/RoboMME_2603.04639.md)。

### 10. 跨基准的统一报告模板

**为什么重要**：一年内出现至少 12 套记忆基准，口径互不相通：RMBench 上锚帧就能到 67.8，RoboMemArena 68.9% 子任务依赖记忆，RoboTwin-MeM 用 n 参数化瞬态证据数，TRACE 用阶段进度而非成功率。跨论文的数字目前只能分块列表，不能比较。

**MVE**：定义一个最小报告模板——任务的记忆类型（RoboMME 四类）、必须记住的中间事件数 n、证据出现与使用的时间间隔、指标类型（成功 / 阶段进度）、试验数——并为本仓库 17 篇有译文的论文回填这张表（见[数字口径账本](NUMBERS_LEDGER.md)的雏形）。

**相关解读**：[RoboMME](../notes/RoboMME_2603.04639.md)、[RoboMemArena](../notes/RoboMemArena_2605.10921.md)、[RMBench](../notes/RMBench_2603.01229.md)。

### 11. RMBench 到底测了什么

**为什么重要**：EventVLA 只用初始帧 + 近期帧就在 RMBench 拿到 67.8%，Chronos 用全历史 SSM 拿到 73.6%——两者都不需要事件记忆。如果 RMBench 的 9 个任务大多能被静态锚帧解决，那它测的是"能否保留初始布局"而不是"能否记住中间事件"。

**MVE**：在 RMBench 上跑三个退化基线：只加初始帧、只加近 2 帧、两者都加，逐任务报告。哪些任务只靠初始帧就能过 80%，就把它们标为"布局记忆"而非"事件记忆"；剩下的（Observe and Pick Up 21%、Press Button 3%）才是记忆基准的硬核。

**相关解读**：[RMBench](../notes/RMBench_2603.01229.md)、[EventVLA](../reports/01_eventvla_cn.md) §4.1、[Chronos](../notes/Chronos_2606.30318.md)。

## D. 路线之争与成本

### 12. 计数与过程记忆能否端到端

**为什么重要**：RoboMME 与 RoboMemArena 的榜首（PonderPounce、HyMeS、BATON）都是高层管符号状态的方案；端到端事件记忆在瞬态视觉证据上最强，但在"按 3 次、跳过已完成子任务"上还没有正面胜过符号进度指针。FM-VLA 用力历史记计数（80%+）提示了另一条端到端路径。

**MVE**：在 RoboMME 的 Counting 子集上对照 AGM（符号指针）、EventVLA（事件帧计数）、FM-VLA 式力记忆、WeaveLA（子目标完成事件），同时报告成功率与每步延迟。回答"符号状态的优势是表征上的还是只是验证机制上的"。

**相关解读**：[AGM](../notes/AGM_2608.29537.md)、[HyMeS](../notes/SkillsWeightsMemoryCode_2608.09410.md)、[MEM](../notes/Mem_2603.03596.md)、[MemER](../notes/MemER_2510.20328.md)。

### 13. 免训练记忆的失效边界

**为什么重要**：TempoFit 不训练、不加 token，只复用中间层 K/V 就在 LIBERO-LONG 上 +4.0；StreamPI 零新增参数；NativeMEM 每帧 1 token。如果免训练记忆够用，EventVLA 三倍的延迟和 235B 标注就没有必要。但它们没有在 RoboTwin-MeM 这类瞬态证据任务上测过。

**MVE**：把 TempoFit 与 StreamPI 直接接到 EventVLA 的 QwenOFT 基座，在 RoboTwin-MeM 的 n=1 与 n=4 任务上对照 EventVLA。若免训练方法在 n=1 持平、n=4 崩塌，就给出"何时必须学习写入"的边界。

**相关解读**：[趋势与洞见](../reports/04_trends_insights_cn.md) 洞见 8、TempoFit / StreamPI / NativeMEM 笔记（[notes](../notes/)）。

## E. 多机器人

### 14. 搭档相位的显式记忆

**为什么重要**：SAI 只用 30 步 GRU 历史（约 1 秒）区分"搬运中"与"该松手"（提前松手 64.5% → 16.1%），但搭档两分钟前做过什么它记不住。搭档相位是一个只能从历史推断的隐变量，与 TRACE 的延迟证据设定同构，却没有人用显式记忆模块做搭档状态估计。

**MVE**：在 SAI 的 Tablecloth 受控延迟实验上，把 A 的 GRU 换成 TRACE 式签名槽记忆（键 = A 自己的轨迹，内容 = 对 B 的观测），把 B 的暂停时长从 2 秒逐步拉到 30 秒，报告 Yield/Wait 随延迟时长的曲线。GRU 版应随时长下降，槽记忆版应保持。

**相关解读**：[SAI](../reports/03_sai_cn.md) §5.2、[TRACE](../reports/02_trace_cn.md)、[AutoIntervene](../notes/AutoIntervene_2608.07065.md)。
