# MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation

> **arXiv 2508.19236** · arXiv 2025 · 提交 2025-08-26 · 分类 `dense` / 稠密与压缩的视觉历史
> *Hao Shi, Bin Xie, Yingfei Liu, Lin Sun, Fengrong Liu, Tiancai Wang, Erjin Zhou, Haoqiang Fan, Xiangyu Zhang, Gao Huang*
> [arXiv](https://arxiv.org/abs/2508.19236) · [PDF](https://arxiv.org/pdf/2508.19236)

## 一句话定位

感知-认知记忆库 + 工作记忆检索融合 + 记忆条件扩散动作专家；150+ 任务，MIKASA-Robo 41.2%。EventVLA 把它当作帧缓冲范式的代表基线。

## 与核心论文的关系

所属家族「稠密与压缩的视觉历史」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Temporal context is essential for robotic manipulation because such tasks are inherently non-Markovian, yet mainstream VLA models typically overlook it and struggle with long-horizon, temporally dependent tasks. Cognitive science suggests that humans rely on working memory to buffer short-lived representations for immediate control, while the hippocampal system preserves verbatim episodic details and semantic gist of past experience for long-term memory. Inspired by these mechanisms, we propose MemoryVLA, a Cognition-Memory-Action framework for long-horizon robotic manipulation. A pretrained VLM encodes the observation into perceptual and cognitive tokens that form working memory, while a Perceptual-Cognitive Memory Bank stores low-level details and high-level semantics consolidated from it. Working memory retrieves decision-relevant entries from the bank, adaptively fuses them with current tokens, and updates the bank by merging redundancies. Using these tokens, a memory-conditioned diffusion action expert yields temporally aware action sequences. We evaluate MemoryVLA on 150+ simulation and real-world tasks across three robots. On SimplerEnv-Bridge, Fractal, LIBERO-5 suites and Mikasa-Robo, it achieves 71.9%, 72.7%, 96.5%, and 41.2% success rates, respectively, all outperforming state-of-the-art baselines CogACT and pi-0, with a notable +14.6 gain on Bridge and +11.8 gain on Mikasa-Robo. On 12 real-world tasks spanning general skills and long-horizon temporal dependencies, MemoryVLA achieves 84.0% success rate, with long-horizon tasks showing a +26 improvement over state-of-the-art baseline. Project Page: https://shihao1895.github.io/MemoryVLA

*arXiv comment: ICLR 2026 | The project is available at https://shihao1895.github.io/MemoryVLA*
