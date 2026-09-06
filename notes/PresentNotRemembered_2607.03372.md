# Present but Not Remembered: Auditing How Frozen VLAs Encode, Deploy, and Steer Visual History

> **arXiv 2607.03372** · arXiv 2026 · 提交 2026-07-03 · 分类 `survey` / 综述与分析
> *Chih-Ting Liao, Xin Cao*
> [arXiv](https://arxiv.org/abs/2607.03372) · [PDF](https://arxiv.org/pdf/2607.03372)

## 一句话定位

对冻结 VLA 做逐层探针 + 因果干预：历史帧内容可解码，但「只属于过去」的信息几乎不存在，历史只在当前帧退化时才被使用；建议记忆增强应注入过去独有的信息——为稀疏事件记忆提供机理依据。

## 与核心论文的关系

所属家族「综述与分析」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)、[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

A frozen vision-language-action model (VLA) receives recent observations at every decision step, yet prior work has focused on adding memory rather than asking how existing history is represented and used. We study this temporal axis using layer-resolved linear probing and causal interchange interventions across three VLAs from two architecture families. We find a three-part dissociation. First, past-frame content remains linearly decodable throughout the network. Second, information unique to history beyond the current frame is nearly absent, indicating that stored history is largely a redundant copy of the present. Third, history is causally deployed only when the current frame is heavily degraded, while the action readout progressively loses dependence on history through the network. Although all models encode history similarly, their deployment strategies differ: under the same occlusion, one architecture increasingly relies on history as a fallback, whereas the other relies on it less. We further introduce a training-free temporal deployment audit that distinguishes these regimes. In the fallback regime, re-injecting history neither repairs occlusion nor disambiguates actions, confirming the redundancy of the stored representation. In the other regime, the same intervention reliably steers the predicted action toward the donor history. These results show that steerability depends on how history is deployed rather than whether it is encoded. VLAs do not forget the past; they largely fail to represent it as information distinct from the present. Our findings suggest that future memory augmentation should inject information unique to the past rather than simply more history.
