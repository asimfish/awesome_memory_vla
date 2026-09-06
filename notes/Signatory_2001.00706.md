# Signatory: differentiable computations of the signature and logsignature transforms, on both CPU and GPU

> **arXiv 2001.00706** · ICLR 2021 · 提交 2020-01-03 · 分类 `background` / 背景：记忆机制与轨迹描述子
> *Patrick Kidger, Terry Lyons*
> [arXiv](https://arxiv.org/abs/2001.00706) · [PDF](https://arxiv.org/pdf/2001.00706)

## 一句话定位

路径签名 / 对数签名的 GPU 可微计算库，TRACE 轨迹键的计算基础。

## 与核心论文的关系

所属家族「背景：记忆机制与轨迹描述子」，对照阅读：[TRACE 深读](../reports/02_trace_cn.md)、[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Signatory is a library for calculating and performing functionality related to the signature and logsignature transforms. The focus is on machine learning, and as such includes features such as CPU parallelism, GPU support, and backpropagation. To our knowledge it is the first GPU-capable library for these operations. Signatory implements new features not available in previous libraries, such as efficient precomputation strategies. Furthermore, several novel algorithmic improvements are introduced, producing substantial real-world speedups even on the CPU without parallelism. The library operates as a Python wrapper around C++, and is compatible with the PyTorch ecosystem. It may be installed directly via \texttt{pip}. Source code, documentation, examples, benchmarks and tests may be found at \texttt{\url{https://github.com/patrick-kidger/signatory}}. The license is Apache-2.0.

*arXiv comment: Published at ICLR 2021*
