# TRACE, read closely: addressing memory by the path the robot took

> **Paper**: TRACE: Trajectory-Routed Causal Memory for Delayed-Evidence Visuomotor Imitation
> **Authors**: Zihao Li, Ranpeng Qiu, Yincong Chen, Guoqiang Ren, Weiming Zhi (Zhejiang University / Zhejiang University of Technology / University of Sydney)
> **arXiv**: [2606.14551](https://arxiv.org/abs/2606.14551) (2026-06-12, v3) · Project page: [jeong-zju.github.io/trace](https://jeong-zju.github.io/trace)
> **In this repo**: [English PDF](../papers/pdf/TRACE_2606.14551.pdf) · [Chinese PDF](../papers/zh/TRACE_2606.14551_zh.pdf) · [中文解读](02_trace_cn.md)

## 0. One sentence

TRACE bolts a fixed-capacity latent memory (K = 4 or 6 slots of 512 dimensions) onto ACT and Diffusion Policy and addresses it with **path signatures** of the robot-state trajectory: while a cue is visible, visual-and-state evidence is written into slots selected by "how the robot got here"; when the cue is gone and the robot reaches a visually ambiguous branch point, the same trajectory address reads it back. On five real delayed-evidence tasks, ACT rises from 25.50 to 69.23 mean stage progress and Diffusion Policy from 25.00 to 59.53, above π₀.₅ fine-tuned on the same data (50.47); reversing the history order drives route similarity down to 37.8%, showing the memory reads ordered history rather than the current frame.

## 1. The problem: delayed evidence

The paper isolates a task class: an early cue (object identity, origin shelf, which side a garment came from), a shared execution segment, then a **branch point** where observations under different histories look nearly identical but require different actions. Formally, for a short window `w` there exist histories with

```
x_{t-w+1:t} ≈ x'_{t-w+1:t}   but   a*_t(H_t) ≠ a*_t(H'_t),
```

so `π(a_t | x_t)` must assign one action distribution to two near-identical observations and is wrong at least half the time. What is needed is a compact causal history summary `m_t = m(H_t)` such that `π(a_t | x_t, m_t)` recovers the branch decision through a fixed-size interface.

The critique of the usual remedies is specific. Longer windows fail as soon as the cue leaves the window and force the policy to guess which early frames still matter. Recurrent policies can overwrite or dilute the branch cue, or entangle it with task-progress signals. Generic external memories do not tie writes and reads to the execution history that will be present at the branch point.

## 2. Method

### 2.1 Separate memory content from memory address

The central design decision: **the current image and state say what to remember; the executed trajectory decides where it is stored and later retrieved.**

- Content: `e_t = φ_x(x_t)`, pooled multi-view visual features plus a proprioceptive embedding.
- Address: the depth-`p = 3` path signature of the normalised 17-D robot-state path `S_t` (2 base planar velocities, 1 yaw rate, 7 + 7 arm joints),

```
Sig_{≤p}(S_t) = (1, ∫dS, ∫∫_{u1<u2} dS⊗dS, ∫∫∫ dS⊗dS⊗dS).
```

Dropping the scalar term gives `17 + 17² + 17³ = 5219` coordinates, plus a signature-space increment `δ_t = ξ_t − ξ_{t−1}`. Learned projections yield `g_t = φ_g(ξ_t)` and `Δg_t = φ_Δ(δ_t)`, combined into the trajectory key `q_t = φ_q([g_t, Δg_t])`.

Why signatures instead of time indices or another RNN state: signatures are invariant to monotone time reparameterisation (speed does not change the address) and to constant offsets (basepointed), yet sensitive to **order**: replaying the history backwards changes the key. They stream online at 0.52 ms per step. The signature stores no visual cue; it is only the key.

### 2.2 Signature-routed slot memory

`K` slots `M_t = {m_{t,1}, …, m_{t,K}}`, reset at the start of every episode. Each step:

1. **Route.** `ρ_t = φ_ρ(q_t)` is compared with the previous slot contents (optionally offset by fixed slot identities `η_k` to break symmetry); a softmax gives write weights `ω_{t,k}` (Eq. 6). Routing depends on the trajectory key and on current slot contents, so it is not a fixed hash.
2. **Gated write.** Write proposal `u_t = φ_w(e_t, q_t)`, candidate `m̃_{t,k} = tanh(φ_m(m̄_{t−1,k}, u_t, ρ_t))`, gate `β_{t,k} = ω_{t,k} · σ(φ_β(·))`, update `m_{t,k} = (1−β)m_{t−1,k} + β m̃_{t,k}` (Eqs. 7–8). Slots with small weight barely change; selected slots absorb the current evidence.
3. **Read.** A query from current evidence and routing state attends over the updated slots: `z_t^mem = Σ_k α_{t,k} W_V^r m_{t,k}` (Eq. 9).

The shared state `R_t = (M_t, z_t^mem, g_t, Δg_t)` goes to an adapter. Training and deployment use the same causal scan: only observations and states up to the current step, no cue labels, branch labels, future frames, or test-time demonstration retrieval.

### 2.3 Adapters translate; they do not change the policy

The updater is shared across policy families; only the policy-facing adapter differs.

- **Regression (ACT) adapter**: each slot becomes a 512-D memory token, `[z_t^mem, g_t, Δg_t]` becomes a summary token, both concatenated to ACT's attention memory. The action head still regresses the chunk with the unchanged L1 (+ optional KL) loss. 0.79 M parameters.
- **Diffusion adapter**: slots pooled by read weights, concatenated with `z_t^mem, g_t, Δg_t`, passed through a zero-initialised MLP into an additive global conditioning vector. Denoising and loss unchanged. 16.03 M parameters.

The shared updater has 11.91 M parameters: +24.6% over ACT (51.62 M), +10.3% over Diffusion Policy (270.96 M).

### 2.4 Three stabilisers

Finite-slot memories fail in three recognisable ways during training: **slot collapse** (most evidence written through a few slots), **diffuse writing** (one observation spread over all slots, so addresses stop meaning anything), **read–write mismatch** (stored in a form the readout cannot recover). TRACE adds one auxiliary loss for each: a balance loss `L_bal` on uneven average routing, an entropy loss `L_ent` on high-entropy per-step routing, and a consistency loss `L_cons` aligning readout with the write proposal (Eqs. 41–43). They act only on the memory; the imitation loss is untouched. Removing them lowers mean progress from 69.23 to 66.10.

## 3. Experimental setup

- **Tasks** (collected with the TriPilot-FF whole-body teleoperation system, 30 Hz, one overhead + two wrist cameras, 17-D state):

| Task | Early evidence → branch | Demos | Episode length | Subtasks / stages |
|---|---|---|---|---|
| Tool | Initial object identity → later tool sequence | 100 | 2910 frames (97 s) | 2/4 |
| Book | Origin shelf → route and placement | 150 | 1392 frames (46 s) | 3/4 |
| Laundry | Origin side → brush-and-basket vs fold-and-store | 60 | 2220 frames (74 s) | 2/4 |
| Cable | Origin side → matched device | 30 | 1770 frames (59 s) | 1/4 |
| Medicine | Tray origin → box selection and return | 60 | 1759 frames (59 s) | 2/4 |

- **Metric**: stage-level progress (%), 25 physical rollouts per task, task-balanced averages, bootstrap standard errors.
- **Baselines**: ACT and Diffusion Policy (TRACE's two bases); SmolVLA, π₀.₅, X-VLA, GR00T N1.6, each adapted for 180k updates on the same single-task demonstrations, with only a generic task prompt (no cue leakage through language).

## 4. Results

### 4.1 Main table

| Method | Tool | Book | Laundry | Cable | Medicine | Avg. |
|---|---|---|---|---|---|---|
| Diffusion Policy | 18.00 | 12.33 | 22.00 | 34.00 | 38.67 | 25.00 |
| ACT | 31.00 | 13.67 | 11.50 | 44.00 | 27.33 | 25.50 |
| π₀.₅ | 45.50 | 51.00 | 47.50 | 49.00 | 59.33 | 50.47 |
| GR00T N1.6 | 39.00 | 12.67 | 24.00 | 38.00 | 39.33 | 30.60 |
| SmolVLA | 25.00 | 20.00 | 12.00 | 50.00 | 34.67 | 28.33 |
| X-VLA | 5.50 | 47.00 | 41.00 | 36.00 | 40.00 | 33.90 |
| **TRACE (Regression)** | 54.50 ± 17.96 | **83.00** | **81.00** | **51.00** | **76.67** | **69.23** |
| **TRACE (Diffusion)** | **58.50** | 68.33 | 70.50 | 51.00 | 49.33 | 59.53 |

The largest gains are on Book, Laundry and Medicine, exactly the tasks where an origin cue determines a later branch. Cable gains only +7 because local device geometry near the branch still carries information. Tool has a standard error of 17.96; the authors report a leave-Tool-out check in which TRACE Regression still averages 72.92, 21.21 points above the strongest non-TRACE baseline.

### 4.2 Against generic memory modules (same ACT base)

| Memory module | Online | Fixed budget | Signature | Avg. |
|---|---|---|---|---|
| No memory | — | — | — | 25.50 |
| GRU recurrent memory | ✓ | ✓ | — | 45.83 |
| Transformer history context | — | — | — | 52.10 |
| LRU external memory | ✓ | ✓ | — | 53.93 |
| Retrieval-prompt memory (MAP-VLA style) | — | — | — | 56.30 |
| **TRACE signature-routed slots** | ✓ | ✓ | ✓ | **69.23** |

Any memory beats none (+20 to +30), but the four controls sit within 10 points of each other and TRACE adds 13 more. The authors' explanation: the controls retain history but do not bind the delayed cue to the trajectory address that will be read at the branch point.

### 4.3 Ablations and diagnostics

| Component ablation | Avg. |
|---|---|
| Current observation only | 25.50 |
| Signature only (no stored visual evidence) | 45.50 |
| Unrouted slot memory | 52.17 |
| No delta routing `Δg_t` | 61.43 |
| Mean readout (no attention) | 62.80 |
| No auxiliary losses | 66.10 |
| Full TRACE | 69.23 |

"Signature only" reaching 45.50 shows the trajectory shape itself carries some branch information (different shelves imply different paths); the remaining 24 points come from storing visual evidence.

The **history-transform diagnostics** are the most persuasive part of the paper. The state path of a recorded online rollout is transformed and the memory module re-run, measuring route similarity (does the pre-branch slot routing sequence match?) and branch consistency (does the branch-point readout and action match?).

| Transform | Property tested | Route similarity | Branch consistency |
|---|---|---|---|
| Time resampling | Time-reparameterisation invariance | 92.4 | 96.0 |
| Speed jitter | Same | 89.8 | 94.7 |
| State offset | Offset invariance | 91.2 | 95.1 |
| Sparse sampling | Sampling robustness | 86.5 | 92.3 |
| **Order reversal (negative control)** | Destroys causal order | **37.8** | **41.6** |

Order-preserving transforms stay around 90; reversing the history falls below 40. Same branch-point image, same weights, only the history order changed, and the readout changes with it. That is direct evidence that the memory depends on ordered history, rather than an inference from success rates.

### 4.4 Long-history stability

Extending online histories to 1.25× / 1.5× / 2.0× or inserting repeated distractor segments keeps slot churn at or below 0.05, with branch decision consistency no lower than 0.872 (repeated distractors). The authors state plainly that this is a diagnostic over the evaluated extensions, not a guarantee for arbitrary horizons.

### 4.5 Deployment overhead

| Path | Base forward | Signature | Slot update | Readout | Adapter | TRACE overhead | Share |
|---|---|---|---|---|---|---|---|
| Regression | 5.90 ms | 0.52 | 0.90 | 0.58 | 0.10 | 2.11 ms | 35.8% |
| Diffusion (100 denoising steps) | 118.00 ms | 0.52 | 0.90 | 0.58 | 0.14 | 2.15 ms | 1.8% |

RTX 5090, PyTorch 2.9.1. Memory is a small fixed cost inside one forward pass, not a second policy call or an offline retrieval.

## 5. Assessment

### 5.1 Three things worth remembering

1. **Separating address from content is a new answer to "how should memory be addressed?"** Frame stacking addresses by time, attention retrieval by content, TRACE by the geometry of the executed trajectory. For delayed-evidence tasks this is well-founded: the path the robot has travelled corresponds between cue time and branch time, whereas the images do not.
2. **Diagnostics rather than success rates alone.** Route similarity / branch consistency with an order-reversal negative control is a methodology any memory paper could adopt to answer "what is your memory actually using?". It complements the probing approach of *Present but Not Remembered*.
3. **A plug-in that leaves the backbone alone.** A shared updater and translate-only adapters lift both regression and diffusion families from the same memory state, which is the modularity claim made concrete.

### 5.2 Points to keep in mind

1. **Signature dimension grows exponentially.** A 17-D state at depth 3 is already 5219-D; depth 4 is 88,740-D. The authors name this the main limitation. Higher-dimensional states (humanoids, dexterous hands) need lower depth or log-signatures (1785-D, but streaming and normalisation are harder; not done here).
2. **Addresses need distinguishable trajectories.** Routing relies on different origins producing different paths. If two branches share identical motion before the branch point (the cue is only a colour, the action sequence identical), signature addresses coincide and routing degrades to content only. All five tasks have origins at different spatial locations, squarely inside TRACE's comfort zone.
3. **Writes happen every step; there is no "should I write?" decision.** Opposite to EventVLA, TRACE writes at every step and lets routing and gates decide how much and where. The stability diagnostics show readout consistency falling to 0.928 at 2× history and 0.907 under repeated distractors: finite slots do get diluted over long histories.
4. **Baseline fairness.** The VLA baselines are fine-tuned for 180k updates with generic prompts but carry no memory module; the only same-base memory comparison is ACT/DP with and without memory. "TRACE + π₀.₅" is not answered.
5. **Tool variance is large** (± 17.96). The leave-one-task-out analysis and failure taxonomy handle it honestly, but 25 real rollouts are thin for contact-heavy tasks.
6. **Single-task training.** Each task trains its own policy; there are no multi-task or cross-task memory-transfer results.

### 5.3 TRACE versus EventVLA

See [EventVLA §5.3](01_eventvla_en.md). In one line: EventVLA stores **many bits of visual detail** (raw frames) and controls sparsity with a learned write trigger; TRACE stores **few bits of branch variable** (latent slots) and controls read/write alignment with trajectory addresses. Both insist that memory be bounded; they are complementary on what to store and how to find it. The natural follow-up: use EventVLA's foresight trigger to decide when to write and TRACE's signatures to decide where, and test whether sparsity and addressability can be had together.

## 6. Related reading

- **Same group**: TriPilot-FF ([2602.09888](https://arxiv.org/abs/2602.09888), the data-collection system), SAI ([2606.16490](https://arxiv.org/abs/2606.16490), the third core paper here), AutoIntervene ([2608.07065](https://arxiv.org/abs/2608.07065), a visual-action support memory that decides when to hand control to the operator), Tri-Manual ([2607.25731](https://arxiv.org/abs/2607.25731)).
- **Other slot / fixed-budget latent memories**: ELMUR ([2510.07151](https://arxiv.org/abs/2510.07151), layer-local external memory with LRU updates, large gains on MIKASA-Robo), MANN ([1605.06065](https://arxiv.org/abs/1605.06065), the origin of content-addressed external memory), VPWEM ([2603.04910](https://arxiv.org/abs/2603.04910), out-of-window observations recursively compressed into a fixed number of episodic embeddings).
- **"History should be the policy's state"**: Chronos ([2606.30318](https://arxiv.org/abs/2606.30318), selective SSM over the full history, 73.6% on RMBench), TFP ([2607.08283](https://arxiv.org/abs/2607.08283), liquid time-constant belief whose write gain is about 6× larger near events), RB-VLA ([2602.20659](https://arxiv.org/abs/2602.20659)).
- **Path signatures**: Signatory ([2001.00706](https://arxiv.org/abs/2001.00706)), CILO ([2407.04856](https://arxiv.org/abs/2407.04856), signatures encoding trajectory constraints in imitation learning).
- **Source of the retrieval control**: MAP-VLA ([2511.09516](https://arxiv.org/abs/2511.09516)).
