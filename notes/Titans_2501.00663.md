# Titans: Learning to Memorize at Test Time

> **arXiv 2501.00663** · arXiv 2025 · 提交 2024-12-31 · 分类 `background` / 背景：记忆机制与轨迹描述子
> *Ali Behrouz, Peilin Zhong, Vahab Mirrokni*
> [arXiv](https://arxiv.org/abs/2501.00663) · [PDF](https://arxiv.org/pdf/2501.00663)

## 一句话定位

测试时学习记忆的神经长期记忆模块，注意力为短期、神经记忆为长期；latent 记忆的 LLM 侧最新参照。

## 与核心论文的关系

所属家族「背景：记忆机制与轨迹描述子」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)、[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Over more than a decade there has been an extensive research effort on how to effectively utilize recurrent models and attention. While recurrent models aim to compress the data into a fixed-size memory (called hidden state), attention allows attending to the entire context window, capturing the direct dependencies of all tokens. This more accurate modeling of dependencies, however, comes with a quadratic cost, limiting the model to a fixed-length context. We present a new neural long-term memory module that learns to memorize historical context and helps attention to attend to the current context while utilizing long past information. We show that this neural memory has the advantage of fast parallelizable training while maintaining a fast inference. From a memory perspective, we argue that attention due to its limited context but accurate dependency modeling performs as a short-term memory, while neural memory due to its ability to memorize the data, acts as a long-term, more persistent, memory. Based on these two modules, we introduce a new family of architectures, called Titans, and present three variants to address how one can effectively incorporate memory into this architecture. Our experimental results on language modeling, common-sense reasoning, genomics, and time series tasks show that Titans are more effective than Transformers and recent modern linear recurrent models. They further can effectively scale to larger than 2M context window size with higher accuracy in needle-in-haystack tasks compared to baselines.
