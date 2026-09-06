# WeaveLA: Event Driven Cross-Subtask Latent Memory Weaving for Repetitive Robot Manipulation

> **arXiv 2606.17463** · arXiv 2026 · 提交 2026-06-16 · 分类 `event` / 事件与关键帧记忆（EventVLA 一族）
> *Shoujing Zhu, Zhenyang Liu, Fungmiu Wang, Jiafeng Wang, Bo Yue, Guiliang Liu, Simo Wu, Xiangyang Xue, Taiping Zeng*
> [arXiv](https://arxiv.org/abs/2606.17463) · [PDF](https://arxiv.org/pdf/2606.17463)

## 一句话定位

以「子目标完成事件」为跨子任务记忆交接的时间单位：把完成段压成 latent token 直接路由进下一子任务的动作生成；RoboMME 最难重复切片 0→47.8%，单次执行任务不变。

## 与核心论文的关系

所属家族「事件与关键帧记忆（EventVLA 一族）」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Vision-Language-Action (VLA) policies have achieved remarkable single-step manipulation, yet they remain brittle precisely where each stage depends on what was just completed. The core issue is structural: short-window VLAs lack an explicit channel for rouxting information across sub-task boundaries, and existing memory-augmented variants either write at every frame, retrieve from demonstration-time stages, or fire at sub-goal events without performing an explicit sub-task-to-sub-task hand-off into the action expert. We identify the sub-goal completion event as the natural temporal unit for cross-subtask memory hand-off, and present WeaveLA (Weave Latent memory for Vision-Language-Action policies), a cross-subtask memory interface that, on top of a frozen VLA backbone, compresses each completed segment into latent tokens via query-driven attention pooling and routes them directly into the action-generation path of the next sub-task. This event-triggered, action-side design preserves the base policy's short-window interface while adding a lightweight cross-subtask channel. Through stratified evaluation on RoboMME with a $π_{0.5}$ backbone, WeaveLA's gains land exactly where the channel is needed: on the hardest repetition slice (SwingXtimes, $N{=}3$), success rises from $0\%$ to $47.8\%$, while single-execution episodes remain unchanged. Per-episode paired analysis confirms the gains are confined to tasks whose causal structure requires cross-subtask information.
