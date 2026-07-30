# Proof-reviewer — imo-2026-03, round 8

Two slugs built this round; both self-reported PARTIAL. I confirm both. No APPROVE.

Answer under review is unchanged and correct: `c(n) = 2^n/(2^{n+1}−1)`, minimax `D = u_n =
1/(2^{n+1}−1)` (previously reviewer-verified). Neither slug closes its assigned gap, so `current.md`
Status stays **partial**.

---

## Slug 1: parity-measure-potential — target LOWER GAP MID-core (`μ{g odd} ≥ 1`, `|F| ≥ 3`)

**Verdict: CHANGES REQUESTED. Status: partial (honest — matches builder's self-report).**

### What I checked

- **Lemma OSR (order-statistic reformulation) — CORRECT, certified.** Re-derived independently:
  `D(S) = Σ(−1)^{i+1}v_i` is exactly certified Lemma R; `Σ e_i v_i = ΣF − ΣB = 2^n − (2^n−1) = 1`;
  subtracting gives `D−1 = Σ d_i v_i` with `d_i = (−1)^{i+1} − e_i`. Coefficient sign analysis
  (`d_i = +2` iff B at odd rank, `−2` iff F at even rank, else 0) is correct, so
  `D(S) ≥ 1 ⟺ Σ_{B odd rank}v ≥ Σ_{F even rank}v`. Verified computationally on 20000 admissible
  a=0 refinements (n=2..6): the three identities hold exactly, aggregate inequality holds in all
  cases (0 violations), `min D = 1.0003 > 1`.
- **Lemma OSR-cap (one-sided walk sub-case) — CORRECT, certified.** Re-derived: `P_k = Σ_{i≤k}d_i =
  1[k odd] − S_k`; `S_k ≤ 1` + parity forces `P_k ≥ 0` (k odd: `1−S_k≥0`; k even: `S_k≤0` so
  `−S_k≥0`); Abel summation `Σ d_iv_i = Σ P_k(v_k−v_{k+1}) ≥ 0` since `w_k ≥ 0`. Hence `D ≥ 1`.
  Computationally: 0 violations among sampled refinements with `max_k S_k ≤ 1`. Strictly generalizes
  the old `0≤g≤1` case — genuine new content.
- **Negative fact F1 (prefix form fails ~27%)** — plausible and consistent with the aggregate
  nature of the inequality; not load-bearing for any claimed theorem, recorded as a route-eliminator.
  **F2** (`S_m = |F|−|B| ≤ 0` from `|B|=n+c_B`, `|F|=1+c_F`, `c_F+c_B≤n`) is correct arithmetic.

### The gap (honestly open, NOT hand-waved)

The assigned GAP MID-core is **not** closed. The residual — the aggregate overshoot-repayment
inequality in the regime `max_k S_k ≥ 2`, `|F| ≥ 3` — is explicitly left as an open aggregate
transport/induction. The builder did NOT paper over it: it is flagged as unbuilt, and F1 rigorously
kills the naive prefix-monovariant route. This is exactly the outline-reviewer's step-4 aggregate
compensation, still open. Status `partial` is correct and honest.

**Certified this round:** `lemmas/order-statistic-reformulation.md`, `lemmas/one-sided-walk-cap.md`.

**Scores:** Correctness 10/10 (what's written is valid). Rigor 9/10 (gap cleanly isolated, no
overclaim). Progress: real — a cleaner cross-term-free reformulation of the whole lower-bound
residual plus a strictly larger closed sub-case.

---

## Slug 2: breakpoint-vertex — target UPPER Prop UV (leftover bound over VERT)

**Verdict: CHANGES REQUESTED. Status: partial (honest — matches builder's self-report).**

### What I checked

- **Lemma ESF-1 (subtraction-from-top subfamily) — CORRECT, certified.** For `T⊆{2,…,n+1}` with
  `Σ_T a_i ≤ a_1`: the MATCH legality `r_{j−1} = a_1 − (a_{i_1}+…+a_{i_{j−1}}) ≥ a_{i_j}` follows
  because every partial sum `≤ Σ_T ≤ a_1`. Budget exact: `k` MATCHes + `n−k` DELETEs = `n` moves.
  Rests only on certified Lemmas P and DM. Sound.
- **Lemma ESF-2 (subset-caterpillar / descending-KK) — CORRECT, certified.** Both abs-flip branches
  handled with explicit legality (flip branch `v_{j−1} < t_j` cuts the resident `t_j ≥ v_{j−1}`).
  Budget exact: `k−1` MATCHes + `n+1−k` DELETEs = `n`. ESF-1 is the no-flip special case; ESF-2 is
  strictly larger. Rests only on certified P/DM. Sound.
- **n=2 negative result — CORRECT, verified by exact rational arithmetic.**
  `A = {9/20, 7/25, 27/100}`: sum = 1, `a_1 = 9/20 < 1/2`, `a_2 = 7/25 < β_2 = 2/7` (valley ✓).
  ESF-1 admissible subsets `{∅,{2},{3}}` give values `{9/20, 17/100, 9/50}`, min `17/100 > u_2 =
  1/7` (`{2,3}` excluded, sum `55/100 > a_1`). Abs-flip subset `{a_2,a_3}` gives `1/100 ≤ 1/7`. So
  ESF-1 alone is provably insufficient; the two-sided abs-flip is mandatory. This is a genuine
  theorem (rational counterexample), not a spot-check.
- **Reduction UV'** correctly reduces Prop UV to the **Subset-KK claim** via ESF-2 + certified
  Reduction R-UV. The reduction direction is valid (existence of one small realizable value suffices
  for the upper bound).

### The gap (honestly open, NOT overclaimed)

Prop UV is **not** closed. The residual Subset-KK claim (every full-budget balanced-valley profile
has a subset whose descending-KK value `≤ u_nL`) is left open and explicitly labelled a genuine
restricted-discrepancy statement needing scale recursion; the builder documents that no
single-pass deterministic policy works (overshoots up to ~7.5×). Numerical evidence (387 profiles)
is used only to confirm the target is true, never as a proof step. No overclaim. Status `partial`
is correct.

**Certified this round:** `lemmas/subtraction-from-top-subfamily.md`,
`lemmas/subset-caterpillar-subfamily.md`.

**Scores:** Correctness 10/10. Rigor 9/10 (residual cleanly isolated, negative result rigorous).
Progress: real — converts Prop UV from an abstract min over `𝓡(A)` into a bound over an explicit
constructive family, and rigorously eliminates the one-sided route so the field won't waste a round
on it.

---

## Verdicts

- **parity-measure-potential — CHANGES REQUESTED — Status: partial.** Gap: aggregate
  overshoot-repayment inequality (`max_k S_k ≥ 2`, `|F| ≥ 3`); needs a value-weighted transport /
  ladder-recursion, prefix monovariant provably dead (F1).
- **breakpoint-vertex — CHANGES REQUESTED — Status: partial.** Gap: the Subset-KK claim (some
  subset's descending-KK caterpillar value `≤ u_nL` on every valley profile) — a restricted-
  discrepancy statement requiring the scale recursion.
