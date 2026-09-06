# TriPilot-FF: Coordinated Whole-Body Teleoperation with Force Feedback

> **arXiv 2602.09888** · arXiv 2026 · 提交 2026-02-10 · 分类 `multi` / 多机器人协作与搭档记忆（SAI 一族）
> *Zihao Li, Yanan Zhou, Ranpeng Qiu, Hangyu Wu, Guoqiang Ren, Weiming Zhi*
> [arXiv](https://arxiv.org/abs/2602.09888) · [PDF](https://arxiv.org/pdf/2602.09888)

## 一句话定位

TRACE 与 SAI 的数据采集系统：脚踏板 + lidar 触觉的全身遥操作，臂侧力反射，反馈信号并入 ACT 策略。

## 与核心论文的关系

所属家族「多机器人协作与搭档记忆（SAI 一族）」，对照阅读：[SAI 深读](../reports/03_sai_cn.md)；横向比较见[趋势与洞见](../reports/04_trends_insights_cn.md)与[设计空间矩阵](../insights/DESIGN_SPACE_MATRIX.md)。

## 摘要（原文）

Mobile manipulators broaden the operational envelope for robot manipulation. However, the whole-body teleoperation of such robots remains a problem: operators must coordinate a wheeled base and two arms while reasoning about obstacles and contact. Existing interfaces are predominantly hand-centric (e.g., VR controllers and joysticks), leaving foot-operated channels underexplored for continuous base control. We present TriPilot-FF, an open-source whole-body teleoperation system for a custom bimanual mobile manipulator that introduces a foot-operated pedal with lidar-driven pedal haptics, coupled with upper-body bimanual leader-follower teleoperation. Using only a low-cost base-mounted lidar, TriPilot-FF renders a resistive pedal cue from proximity-to-obstacle signals in the commanded direction, shaping operator commands toward collision-averse behaviour without an explicit collision-avoidance controller. The system also supports arm-side force reflection for contact awareness and provides real-time force and visual guidance of bimanual manipulability to prompt mobile base repositioning, thereby improving reach. We demonstrate the capability of TriPilot-FF to effectively ``co-pilot'' the human operator over long time-horizons and tasks requiring precise mobile base movement and coordination. Finally, we incorporate teleoperation feedback signals into an Action Chunking with Transformers (ACT) policy and demonstrate improved performance when the additional information is available. We release the pedal device design, full software stack, and conduct extensive real-world evaluations on a bimanual wheeled platform. The project page of TriPilot-FF is http://bit.ly/46H3ZJT.
