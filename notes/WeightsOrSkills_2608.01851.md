# Weights or Skills? A Survey of Robot-Learning Techniques: from Action-Predicting Weights to Robots that Write their Own Skills

> **arXiv 2608.01851** · arXiv 2026 · 提交 2026-08-03 · 分类 `survey` / 综述与分析
> *Gaytri Jena, Kapil Wanaskar, Vinija Jain, Aman Chadha, Vasu Sharma, Amitava Das*
> [arXiv](https://arxiv.org/abs/2608.01851) · [PDF](https://arxiv.org/pdf/2608.01851)

## 一句话定位

「权重 vs 技能（代码）」的机器人学习综述，梳理持久技能记忆与自我改进闭环；与 HyMeS「技能在权重、记忆在代码」同一坐标。

## 与核心论文的关系

所属家族「综述与分析」，对照阅读：[EventVLA 深读](../reports/01_eventvla_cn.md)、[TRACE 深读](../reports/02_trace_cn.md)、[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Robot learning is splitting into two bets: policies that bake competence into frozen weights (vision-language-action, or VLA, models), and agents that write and refine their own executable skills as code. This survey organises the field around that axis of weights versus skills. Its central analytical contribution is a deep-dive that arranges code-as-policy methods by their degree of self-improvement, from zero-shot program synthesis, through closed-loop self-repair and persistent skill memory, to the sparsely populated cell in which execution feedback, skill memory, and evolutionary search combine into one open-ended loop; only a few very recent systems (for example ASPIRE, ENPIRE, and RoboClaw) occupy that cell. We map the complementary "skills" pole, from unsupervised reinforcement-learning skill discovery to large-language-model skill libraries, and show that the word "skill" is used in at least five distinct senses, of which only the code sense self-improves without gradient updates. We then connect the taxonomy to the emerging skill economy: commercial robot-skill marketplaces now distribute one-tap skills across robots but ship only static playback, which surfaces open problems of adaptation, cross-embodiment portability, provenance, safety verification, composition, and standardisation. This is a deliberately focused survey. Rather than cataloguing the field exhaustively, it examines 77 representative systems across six technique families through one taxonomy and a set of contrast tables, and it supplies operational definitions of the self-improvement mechanisms together with a statement of what each family cannot do.

*arXiv comment: 40 pages, 11 figures, 11 tables*
