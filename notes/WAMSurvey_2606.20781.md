# World Action Models: A Survey

> **arXiv 2606.20781** · arXiv 2026 · 提交 2026-06-18 · 分类 `survey` / 综述与分析
> *Qiuhong Shen, Shihua Zhang, Yue Liao, Qi Li, Zhenxiong Tan, Shizun Wang, Shuicheng Yan, Xinchao Wang*
> [arXiv](https://arxiv.org/abs/2606.20781) · [PDF](https://arxiv.org/pdf/2606.20781)

## 一句话定位

世界动作模型综述，讨论持久性（persistence）与记忆在预测-动作耦合中的位置，指出趋势是「生成更少的未来、保留控制所需的部分」。

## 与核心论文的关系

所属家族「综述与分析」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)、[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

World Action Models (WAMs) are embodied predictive-action models that make a forecast of the future available to action. Recent WAMs repurpose large video generation models, and a parallel line relies on language or vision-language backbones without a video-generation core. This rapid expansion has blurred the boundary among broad world models, video generation models, action-grounded video world models, Vision-Language-Action policies, and WAMs. This survey gives the field a common account. It first clarifies these boundaries, then organizes existing works through two complementary views. The first view asks what each method is required to generate, spanning rendered futures, latent futures, and video-generation-free action reasoning. The second view decomposes each method by predictive substrate, backbone, action coupling, and deployment regime. This anatomy supports a unified discussion of interactability, causality, persistence, physical plausibility, and generalization, followed by data, evaluation, and open challenges. Across these axes, a consistent design pattern emerges: WAMs are not simply video generators with action heads, but predictive-action methods whose design choices trade representational richness against compute, memory, latency, and action-label cost. The field is moving toward methods that generate less of the future while preserving what control requires. The survey homepage is available at https://world-action-models.github.io/.

*arXiv comment: 57 pages, 6 figures*
