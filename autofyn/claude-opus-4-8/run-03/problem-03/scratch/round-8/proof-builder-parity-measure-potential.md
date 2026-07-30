# Proof-builder report — parity-measure-potential, round 8

**Slug:** parity-measure-potential. **Status: PARTIAL** (advanced; the assigned GAP MID-core is NOT
fully closed, but a new sub-case is closed and the residual is sharpened + structurally pinned).

## What I did this round (target: LOWER GAP MID-core, `μ{g odd} ≥ 1` for `|F| ≥ 3`)

1. **Clean order-statistic reformulation (Lemma OSR — FULLY RIGOROUS, promotable).**
   Merging `S = F ⊔ B` in strictly-descending order `v_1 > ⋯ > v_m` with signs `e_i = ±1`,
   certified Lemma R gives `D(S) = Σ_i(−1)^{i+1}v_i`, and the ladder mass identity gives
   `Σ_i e_i v_i = ΣF − ΣB = 2^n − (2^n−1) = 1`. Subtracting:
   `D(S) − 1 = Σ_i((−1)^{i+1} − e_i)v_i`. Hence
   **`D(S) ≥ 1 ⟺ Σ_{B at odd rank} v_i ≥ Σ_{F at even rank} v_i`.**
   This is the explorer's `Σc_iw_i ≥ 0` walk inequality, but derived without any integral or Lemma
   MID(a) — only certified Lemma R + the superincreasing signature. Verified exact on 20000
   admissible refinements (`n=2..6`).

2. **NEW closed sub-case (Lemma OSR-cap — FULLY RIGOROUS, promotable).**
   If the merge walk never leads by two (`S_k ≤ 1` for all `k`, i.e. `N_F ≤ N_B + 1` pointwise,
   `g ≤ 1`), then the partial coefficient sums `P_k = 1[k odd] − S_k ≥ 0` (parity check), so Abel
   summation `Σ_i d_i v_i = Σ_k P_k(v_k − v_{k+1}) ≥ 0` gives `D(S) ≥ 1`. This **strictly generalizes**
   the previously-closed `0 ≤ g ≤ 1` floor case (drops the lower bound on `g`).

3. **Residual pinned by two verified structural facts.**
   - **(F1)** The global inequality `Σ_{B odd}v ≥ Σ_{F even}v` holds in **all 30000** sampled cases,
     but its **prefix form fails ~27%** (8043/30000). So NO prefix/running-deficit monovariant on
     the merge order can prove GAP MID-core — the compensation is irreducibly aggregate. This
     rigorously kills the naive `P_k ≥ 0` route outside sub-case R8.2 and confirms the
     outline-reviewer's "aggregate, never termwise" mandate.
   - **(F2)** `S_m = |F| − |B| ≤ 0` (from `|B| = n + c_B`, `|F| = 1 + c_F`, `c_F + c_B ≤ n`), so
     credit-ranks outnumber debit-ranks in COUNT (necessary but not value-sufficient).

## Honest gap (NOT closed)

The aggregate overshoot-repayment inequality in the regime `max_k S_k ≥ 2`, `|F| ≥ 3` — a
value-weighted transport routing each `F`-even debit to smaller-or-equal `B`-odd credits summing to
at least it, feasible via the ladder (Lemma ONE recursed at each dyadic scale). This is exactly the
outline-reviewer's step-4 aggregate-compensation induction. I could not build the transport/induction
rigorously in the time available. The pure-integral version stays false (`g ≡ 2` on measure ½), so
the ladder must genuinely enter — as established, but not carried through to a proof.

## Spec concerns
None. The reduction (Lemma R + `ΣF−ΣB=1`) and the sub-case are fully rigorous; the residual is a
genuine open aggregate inequality, not a bookkeeping gap. Note (F1) formally rules out the
prefix-monovariant framing, so next round's attack on this wall should be a transport/matching
certificate (ballot-matching reserve) or a strong induction abstracting the ladder — not another
running-deficit variant.

## Verdict I expect
CHANGES REQUESTED (real progress: new sub-case closed, reformulation cleaner than MID, residual
sharpened and monovariant-route refuted; core inequality still open). Approach stays live/partial.

## Promotable lemmas (for reviewer certification)
- **Lemma OSR** (order-statistic reformulation): `D(S) ≥ 1 ⟺ Σ_{B odd rank}v_i ≥ Σ_{F even rank}v_i`.
- **Lemma OSR-cap**: `S_k ≤ 1 ∀k` (`g ≤ 1`) ⇒ `D(S) ≥ 1` (Abel, `P_k ≥ 0`).
- **Negative result**: prefix form fails ~27%; compensation is irreducibly aggregate.

File written: /home/agentuser/repo/results/imo-2026-03/approaches/parity-measure-potential.md
