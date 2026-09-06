# Scaling Short-Term Memory of Visuomotor Policies for Long-Horizon Tasks

> **arXiv 2606.16178** · arXiv 2026 · 提交 2026-06-15 · 分类 `dense` / 稠密与压缩的视觉历史
> *Rutav Shah, Rajat Kumar Jenamani, Xiaohan Zhang, Lingfeng Sun, Roberto Martín-Martín, Yuke Zhu, Deva Ramanan, Karl Schmeckpeper*
> [arXiv](https://arxiv.org/abs/2606.16178) · [PDF](https://arxiv.org/pdf/2606.16178)

## 一句话定位

PRISM：门控注意力过滤检索信息 + 分层压缩，把视觉运动策略的短期记忆扩展到两分钟；附 ReMemBench（8 任务、4 类短期记忆）。

## 与核心论文的关系

所属家族「稠密与压缩的视觉历史」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Many robotic tasks require short-term memory, whether it's retrieving an object that's no longer visible or turning off an appliance after a set period. Yet, most visuomotor policies trained via imitation learning rely only on immediate sensory input without using past experiences to guide decisions. We present PRISM, a transformer-based architecture for visuomotor policies to effectively use short-term memory via two key components: (i) gated attention, which filters retrieved information to suppress irrelevant details, improving performance by reducing the spurious correlations between the history and current action prediction, (ii) a hierarchical architecture that first compresses local information into compact tokens and then integrates them to capture temporally extended dependencies, improving its compute and memory footprint. Together, these mechanisms enable us to scale short-term memory in visuomotor policies for up to two minutes. To systematically evaluate memory in visuomotor control, we introduce ReMemBench -- a benchmark of eight diverse household manipulation tasks spanning four categories of short-term memory -- designed to foster general memory mechanisms rather than siloed, task-specific solutions. PRISM consistently outperforms prior works, including recurrent architectures, transformers, and their variants -- achieving an absolute improvement of 5%--12% over the strongest baseline. On the RoboCasa and LIBERO benchmarks, it achieves absolute improvements of 11%--15% over its no-memory variant and fine-tuned Vision-Language-Action baselines such as GR00T-N1-3B and OpenVLA, despite not leveraging any large-scale pretraining. Together, PRISM and ReMemBench establish a foundation for developing and evaluating short-term memory-augmented visuomotor policies that scale to long-horizon tasks. Additional materials are available at https://shahrutav.github.io/short-term-memory

*arXiv comment: 14 pages, 9 Figures, 8 Tables*
