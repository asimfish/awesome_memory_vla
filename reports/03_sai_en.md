# SAI, read closely: the partner is only partly visible, so history and the curriculum have to fill in

> **Paper**: Robots that Collaborate: Sequential Asymmetric Imitation for Learning Coupled Robot Policies
> **Authors**: Yincong Chen, Ranpeng Qiu, Zihao Li, Yanan Zhou, Guoqiang Ren, Weiming Zhi (Zhejiang University / Zhejiang University of Technology / University of Sydney)
> **arXiv**: [2606.16490](https://arxiv.org/abs/2606.16490) (2026-06-15, v2) · Project page: [cyc0429.github.io/sai-project-page](http://cyc0429.github.io/sai-project-page/)
> **In this repo**: [English PDF](../papers/pdf/SAI_2606.16490.pdf) · [Chinese PDF](../papers/zh/SAI_2606.16490_zh.pdf) · [中文解读](03_sai_cn.md)

## 0. One sentence

Two bimanual mobile manipulators carry a painting, spread a bed throw and a tablecloth, and collect laundry together, without communicating and without seeing each other fully. SAI collects data with a single teleoperator in three stages: Robot A first learns the task with a compliant human partner; A is then frozen while a human teleoperates B against A's actual behaviour; finally both run together and the operator intervenes on A only where coordination starts to fail. Across four real tasks, success rises from 23–50% (independent imitation) to 53–70%, and the Yield/Wait metric ("wait when the partner is late") from 27–47% to 68–72%. The policy is just an ACT with a 30-step history token and a cascaded base-then-arm head; the coordination comes from the data curriculum, not the architecture.

## 1. Why this paper belongs in a memory-VLA list

SAI looks like multi-robot imitation learning, but the problem underneath is the same non-Markovian one: **the partner's state is partially observed**. Robot A can only infer from its own cameras and from forces on the shared object which phase B is in, whether B is delayed, whether B is stuck. That inference has to come from history. Two pieces of evidence in the paper say so directly:

- The 30-step history token (12 log-sampled frames → GRU) cuts premature release in Laundry from 64.5% to 16.1%, because the policy must use history to tell "mid-transport" from "time to release": a single frame looks the same in both.
- Stage-three interventions specifically teach A to slow, wait and recover when "B is not there yet", and whether B is there yet is a latent variable read off a time series.

So SAI is the multi-agent version of memory VLA: what must be remembered is not an occluded object but where a partly visible partner has got to. It comes from the same group as TRACE, shares the policy backbone (ACT with history encoding) and the data-collection system (TriPilot-FF).

## 2. Problem setting

- Decentralised partially observable control: each robot `i ∈ {A, B}` receives only its local observation `o_i^t = O_i(s_t)` and acts by its own policy `a_i^t ~ π_i(·|o_i^t)`; no messages, partner states, actions or latents are exchanged. Coordination can only arise from local observation of the shared workspace and physical coupling through the shared object.
- Three failure classes: **temporal phase coupling** (grasp, lift, lower, release must align), **partner-contingent yielding** (slow down when the partner is delayed or stuck), **interaction conflict** (excess internal force, deformation, opposing motion, collisions).
- Single-teleoperator constraint: one robot at a time. Supervision is split into three asymmetric datasets: `D_A^solo` (A with a compliant human partner), `D_B^A` (B while A's learned policy runs), `D_A^int` (interventions on A during joint deployment).

The question: are these sequential, asymmetric datasets enough to learn coupled policies that approach what synchronised two-operator demonstrations would give?

## 3. Method: a three-stage curriculum

### 3.1 Stage 1: bootstrap A with a human partner

A human supports the other end of the shared object while A is teleoperated. A learns grasping, pulling and aligning. Because the training partner is human and the deployment partner is a robot, naive training lets A shortcut on human appearance (clothes, skin, body shape). The fix is offline **partner-region randomisation**: segment the human, dilate the mask, and at data-loading time replace the region with random RGB noise, heavy Gaussian blur or Stable Diffusion inpainting (Appendix B). The aim is not to erase interaction evidence but to make human appearance unreliable, so the policy attends to object geometry, deformation and contact progress.

### 3.2 Stage 2: train B against the deployed A

`π_A^(1)` is frozen and deployed; a human teleoperates B. A is run with bounded deployment variation (speed scaling, action noise, timing offsets, perturbed initial object states), so B sees realistic partner deviations and learns to wait, yield, recover and resume. The stage is asymmetric by design: B trains against A's actual learned behaviour rather than an ideal or manually synchronised partner, so it compensates for A's timing, motion profile and residual errors.

### 3.3 Stage 3: DAgger-style intervention fine-tuning of A

The largest remaining mismatch is on A, which has only ever seen a compliant human. Both policies are deployed together and the operator supplies corrective actions on A only near states where coordination begins to fail (pulling too early, not yielding, continuing while B is delayed, poor recovery after phase mismatch). The interventions are aggregated with the original A demonstrations:

```
π_A^(3) = BC(D_A^solo ∪ D_A^int)
```

Intervention samples are upweighted relative to nominal replay; when only part of the action is corrected, a binary action-dimension mask (e.g., correct the base, keep the arms) prevents sparse labels from overwriting unaffected dimensions. The intervention set is about 30% of the baseline dataset size.

### 3.4 Policy instantiation

One ACT-style policy per robot: frozen DINOv3-80M (ViT-B) vision, top-view plus wrist cameras, 17-D proprioception (3 base + 14 arm/gripper), arm torque feedback. History window `H = 30` steps, 12 log-sampled frames, pooled multi-view features fused with a 64-D state embedding, a single-layer GRU (hidden 512) whose final state is the history token. The action head is cascaded: an MLP predicts the base action `a_base ∈ R³ = (v_x, v_y, ω)`, which is concatenated with the decoder query to predict the 14-D arm/gripper action. Chunk length 100, temporal ensembling coefficient 0.01.

## 4. Experiments

### 4.1 Four real tasks, three training pipelines

Tasks: Bed-throw Spreading and Tablecloth Spreading (deformable alignment), Laundry Collection (asynchronous coordination in a shared workspace), Painting Transport (contact-rich rigid transport). Three pipelines share one architecture: Independent Imitation (each robot from its own unilateral demos), Partner-Conditioned Imitation (stage 2 without stage 3), full SAI. 30 rollouts per task-method pair; Phase Sync counts predefined checkpoints (Painting: 5 × 30 = 150), Yield/Wait counts partner-delay opportunities.

| Task | Method | Success | Phase Sync | Yield/Wait |
|---|---|---|---|---|
| Bed-throw | Independent / Partner-cond. / **SAI** | 23.3 / 36.7 / **53.3** | 30.8 / 60.8 / **62.5** | 26.7 / 35.0 / **68.3** |
| Tablecloth | Independent / Partner-cond. / **SAI** | 43.3 / 60.0 / **66.7** | 54.4 / 67.8 / **68.9** | 46.7 / 61.7 / **70.0** |
| Laundry | Independent / Partner-cond. / **SAI** | 50.0 / 63.3 / **70.0** | 51.7 / 68.3 / **73.3** | 31.7 / 48.3 / **71.7** |
| Painting | Independent / Partner-cond. / **SAI** | 33.3 / 46.7 / **56.7** | 42.7 / 67.3 / **74.7** | 34.4 / 48.9 / **68.9** |

How to read it: stage 2 mainly lifts Phase Sync (Bed-throw 30.8→60.8) because B learns A's rhythm; stage 3 mainly lifts Yield/Wait (Bed-throw 35.0→68.3) because A finally learns to wait when B falls behind. Success is the sum of the two.

### 4.2 Controlled partner delay

In Tablecloth, B is manually paused. Independent-imitation A keeps pulling on its nominal trajectory, the cloth misaligns and B loses its grasp; SAI's A sees that B has not advanced, slows and waits, then resumes when B recovers. That is the behaviour behind the Yield/Wait number.

### 4.3 Architecture ablations: history and cascade

| Failure mode | Variant | Rate |
|---|---|---|
| Premature release (Laundry delivery phase) | without / with history | 64.5% / **16.1%** |
| Premature lowering (transport→place transition) | without / with cascade | 51.6% / **9.7%** |

The history token lets the policy separate mid-transport from terminal release; the cascaded head conditions arm commands on base intent so the arm does not lower before the base arrives. The authors stress that these components improve local execution reliability and **do not** explain the collaborative gains: the three pipelines in Table 1 share the architecture and independent imitation still fails under partner delay.

### 4.4 Backbone independence

On Painting Transport with a Diffusion Policy head: Independent 23.5 / 35.2 / 30.7 → SAI 52.9 / 62.2 / 76.9 (Success / Phase Sync / Yield/Wait, 34 rollouts). With ACT: 33.3 / 42.7 / 34.4 → 56.7 / 74.7 / 68.9. The curriculum's effect does not depend on the action decoder.

## 5. Assessment

### 5.1 Worth remembering

1. **Coordination is a function of the partner distribution, not the architecture.** The experimental design fixes the architecture and changes only the data curriculum, so the gains are cleanly attributable to what partners the policy saw during training. It is the same experimental discipline as TRACE's plug-in memory with an untouched backbone.
2. **Asymmetry is a feature.** B learns against the real A; A then patches against the real B. Each stage fixes the currently largest distribution mismatch. Synchronised two-operator data is expensive and not obviously better, since it trains against a perfect partner.
3. **History's role in multi-robot control is quantified.** Premature release 64.5% → 16.1% is a direct instance of history disambiguating visually identical states, structurally the same as TRACE's delayed-evidence setting.

### 5.2 Points to keep in mind

1. **Intervention coverage is thin.** Stage-3 data is about 30% of the baseline set and the authors say recovery "has not saturated"; too much correction could bias the policy toward needless waiting. How many interventions and where remains a human judgement. The group's follow-up AutoIntervene ([2608.07065](https://arxiv.org/abs/2608.07065)) addresses exactly this with a visual-action support memory and quantile-calibrated switching thresholds.
2. **A-centric.** Only A is corrected. Tasks needing simultaneous correction of both robots do not fit; B is never updated after stage 2, although the distribution it faces changes once A changes. There is no stage 4.
3. **History is 30 steps, about a second.** Enough to separate adjacent phases, not enough to know what B did two minutes ago. Partner phase over longer tasks may need TRACE-style explicit slots, which is the most natural fusion of the two papers.
4. **Descriptive metrics.** Phase Sync and Yield/Wait denominators are event counts, not independent trials (Painting's 150 checkpoints come from 30 rollouts), so they cannot be treated as independent samples; the appendix says so.
5. **Homogeneous robots** (two identical bimanual mobile manipulators with TriPilot-FF). Whether human-appearance randomisation suffices with heterogeneous partners (humanoid plus wheeled, as in Duet) is untested.
6. **No comparison to policies trained on synchronised two-operator demonstrations**, the very target SAI is meant to replace; the cost of collecting them is the reason, so "approaches synchronised demonstrations" remains a hypothesis.

### 5.3 Relation to the other two papers

| | EventVLA | TRACE | SAI |
|---|---|---|---|
| What is unobservable | Occluded or vanished object evidence | An early branch cue | The partner's internal phase |
| What fills the gap | Sparse raw-frame buffer | Trajectory-addressed latent slots | 30-step GRU history + training-distribution coverage |
| Where the intervention sits | Architecture (KEM head) | Module (plug-in adapter) | Data (curriculum + DAgger) |
| Shared stance | All three reject "just lengthen the window" and use a bounded history representation | | |

## 6. Related reading

- **Same group**: TRACE, TriPilot-FF, AutoIntervene, Tri-Manual ([2607.25731](https://arxiv.org/abs/2607.25731): one operator demonstrates for three arms; demonstrations are re-timed offline under dependency constraints).
- **Multi-robot data collection**: HATS ([2606.16491](https://arxiv.org/abs/2606.16491), the adjacent arXiv number: one human plus an MLLM agent controlling four arms), Duet ([2606.20990](https://arxiv.org/abs/2606.20990), human–human demonstrations for pretraining plus a few dual-robot teleoperation trajectories, Unitree G1 + Vega1 heterogeneous partners), Mobile ALOHA ([2401.02117](https://arxiv.org/abs/2401.02117)).
- **Interventional imitation**: DAgger ([1011.0686](https://arxiv.org/abs/1011.0686)), IntervenGen ([2405.01472](https://arxiv.org/abs/2405.01472), generating many corrective interventions from few human ones; a direct remedy for SAI's stage-3 coverage).
- **Decoupled bimanual control**: Decoupled Interaction Framework ([2503.09186](https://arxiv.org/abs/2503.09186), one model per arm plus a selective interaction module, +23.5% on RoboTwin), the single-robot version of "decentralised with local interaction".
- **Making two action heads agree** ([2608.15748](https://arxiv.org/abs/2608.15748)): coordination mechanisms and a runtime collapse certificate for dual-branch flow-matching policies; a formal reference for the failure where two robots pick different modes.
