# Proof-review — imo-2026-03, round 9

Two isolated walls advanced. Both builders recorded `partial` honestly; I confirm both. Answer
`c(n)=2^n/(2^{n+1}−1)` unchanged and correct (brute-forced n=0,1,2 in prior rounds). No APPROVE.

---

## SLUG 1 (LOWER) — parity-measure-potential

**Verdict: CHANGES REQUESTED. True Status: partial. Recorded Status (partial) is correct.**

**Lemma ONE-REC (`recursed-dyadic-dichotomy`) — CERTIFIED.**
Re-derived independently:
- (i) Partition-of-cuts: fragments of pieces `2^0..2^ℓ` form a self-contained refinement of `C_ℓ`,
  cut count `Σ_{j≤ℓ}(|G_j|−1)`. No cut crosses two original pieces — correct.
- (ii) Two fragments of `G_j` each `>2^{j−1}` sum to `>2^j=ΣG_j` — impossible (superincreasing).
  Applying certified Lemma ONE (`top-scale-dichotomy`) to the refinement `B_{≤ℓ}` of `C_ℓ` (valid by
  (i)) gives ≤1 piece `>2^{ℓ−1}`; `N_B(τ)` additivity over disjoint `G_j` — correct.
The lemma claims ONLY (i),(ii) and genuinely reduces to certified Lemma ONE + a triviality; it does
NOT lean on any uncertified step. It does NOT close GAP MID-core (correctly disclaimed). The
ladder-litmus (excludes `F={½,½,½},B={½}`, since `{½}` is not a refinement of any `C_m`) is valid.
This is the shared structural dependency of both walls — certifying it de-risks both. Admitted.

**Residual identity — verified exact.** `μ{g odd}−1 = ∫_0^{2^{n−1}}φ(g)` with `φ(c)=1[c odd]−c`,
using Lemma MID (`D=μ{g odd}`, `∫g=1`). Checked `φ` over integer `c∈[−3,4]` (g is integer-valued):
`φ≥0 ⟺ c≤1`, `φ<0 ⟺ c≥2`, negative mass exactly on `{g≥2}`. Correct; not overclaimed.

**ρ_k reserve refutation — correctly recorded, not overclaimed.** The negative claim (nonnegative
cumulative-surplus reserve does not exist; walk-height-only `ψ(g(τ))` also impossible) is numerical/
diagnostic and used only to prune the lever, not inside a proof. Builder does not claim MID-core
closed. Honest.

**GAP MID-core is honestly still open** (`|F|≥3`, `{g≥2}` present; needs a whole-ladder
F-mass-tracking reserve, not a local surplus). Correctly `partial`, not `solved`.

Scores — Correctness 10/10 (ONE-REC + identity both exact); Completeness 5/10 (core gap open);
Progress: real — certified the field-wide structural dependency and pinned the residual to an exact
scalar integral, plus killed a whole reserve-class.

---

## SLUG 2 (UPPER) — breakpoint-vertex

**Verdict: CHANGES REQUESTED. True Status: partial. Recorded Status (partial) is correct.**

**Lemma BL (`band-landing`) — CERTIFIED.** Re-derived independently:
- (1) `P_0=0<P_1<…<P_n=L−a_1`; `a_1<L/2 ⇒ P_n>a_1`, `P_0≤a_1` ⇒ unique first index `k≤n` with
  `P_{k−1}≤a_1<P_k`. Finite strictly-increasing sequence ⇒ the flagged straddle case is genuinely
  vacuous (no boundary ambiguity). Correct.
- (2) `r=a_1−P_{k−1}∈[0,s_k)`, `s_k≤a_2<β_nL` (`β_n=2^{n−1}u_n`). Correct.
- (3) All running values `a_1−P_{j−1}≥r≥0` for `j≤k` ⇒ no abs-flip; caterpillar value `=r`, exactly
  certified Lemma ESF-1 with `T={2,…,k}`, `Σ_{i=2}^k a_i=P_{k−1}≤a_1`, `n` moves. Correct.
Verified on n=2 witness `{9/20,7/25,27/100}` with exact fractions: `a_1=0.45<0.5`, survivors
`0.28,0.27`, `P_1=7/25≤a_1<P_2=11/20`, `k=2`, `r=17/100∈[0,27/100)⊂[0,2/7)`. Admitted.

**Reachability/Covering reformulation — correct.** Via certified ESF-2, `Subset-KK ⟺ R_{n+1}` meets
`[0,u_nL]` (include/skip reachable set with two-sided abs-flip). A clean equivalent of the residual;
consistent with Lemma RL (not all `{0,±1}` patterns reachable, no raw pigeonhole) and Lemma VS
(≥2 coordinated cuts forced). Sound as a reformulation, not a claim of closure.

**Negative result (greedy recursion overshoots) — sound.** BL alone gives `r=17/100>u_2=1/7`;
greedy band-landing / flip-if-helps / drop-one all machine-verified to overshoot `u_nL`. Numerics
diagnostic only (prune the recursion class); no numeric statement enters a proof step. Correct
conclusion: the residual is a GLOBAL covering problem, not a per-step recursion.

**GAP U-cover is honestly still open** (cover the remaining factor `2^{n−1}` down to `u_nL`
globally). Correctly `partial`, not `solved`.

Scores — Correctness 10/10 (BL exact, reformulation valid); Completeness 5/10 (covering gap open);
Progress: real — closed step-2 (first landing) rigorously and rigorously killed the step-3 recursion
route, reframing the residual precisely.

---

## Goal Progress
- **parity-measure-potential:** Elo 1729.97 (leader), outcome `advanced`. Raw: +1 certified lemma
  (ONE-REC), shared structural dependency now available to both walls; residual pinned to exact
  `∫φ(g)≥0`; ρ_k reserve-class refuted. GAP MID-core unchanged-open.
- **breakpoint-vertex:** Elo 1577.51, outcome `advanced`. Raw: +1 certified lemma (BL, step-2
  closed); step-3 recursion route refuted; residual reframed as GAP U-cover (global covering).
- **Lemmas certified this round: 2** (ONE-REC, BL) → 15 total in `lemmas/`.
- No APPROVE. Both walls remain open; both are now aggregate whole-ladder / global-covering objects
  (mirrored structure), suggesting the outliner should target a single shared aggregate-reserve
  framing next round rather than local/recursive levers (both refuted).
