# Build report — peel-scale-rank-induction — Round 10 — imo-2026-03

## Outcome: partial (CHANGES REQUESTED expected). GAP L Case B sharpened, not closed.

## What I did
Target was GAP-P1: prove `D̃(F)≥1` on the near-balance residual `{|D̃(π_0)−D̃(F')|<1}` via a loaded
coupled IH. I did NOT find the loaded IH; instead I found a strictly sharper, exact reduction of the
WHOLE of Case B, and isolated the precise role of every hypothesis.

### New, fully-proven exact identity `(FLOOR)` (§9.1 of the approach file)
With the top-scale peel `F=π_0⊎F'`, `θ=2^{n−1}`, `M=N_{π_0}−N_{F'}` on `(0,θ)`:
```
D̃(F) = 1 − 2 ∫_{(0,θ)} ⌊M(t)/2⌋ dt.
```
Proof self-contained from the certified peel identity (`lemmas/peel-difference-bound.md`) + the
elementary `1[m odd] = m − 2⌊m/2⌋` + the mass computation `∫_{(0,θ)}M = 1−β`. Hence **Case B `⟺`
`I_n := ∫_{(0,θ)}⌊M/2⌋ ≤ 0`**, tie-attained (`D̃=1 ⟺ I_n=0`). Verified: `0` mismatches / `3·10³`
random dyadic configs; `I_n≤0` with max `=0` over `6·10⁴` feasible fractional Case-B configs (`n≤6`),
exact `Fraction`, `0` violations.

### Layer form (§9.2) and structural bound
`I_n = Σ_{k≥1}(λ{M≥2k} − λ{M≤−(2k−1)})` (verified `0` mismatches). Target `⟺
Σ_kλ{M≥2k} ≤ Σ_kλ{M≤−(2k−1)}`. The even-vs-odd threshold asymmetry is the exact source of the
missing `½`. Proven structural bound `Σ_kλ{M≥2k} ≤ E(π_0)=(2^n−D̃(π_0))/2` (from
`{M≥2k}⊆(0,x_{2k}(π_0))`) — correct but too weak alone (loose by a factor at the tie).

### Two decisive findings on which hypothesis does what (§9.3)
1. The joint budget `Σa_j≤n` enters the whole reduction ONLY through `M(0⁺)≤1` (Invariant I,
   `M(0⁺)=(a_0+1)−|F'|`, `≤1 ⟺ a_0+b≤n`). An exact-Fraction probe over *infeasible* configs
   (`F'` given its own budget `n−1` while `π_0` is also cut, so `a_0+b>n`) produces many `I_n>0`.
   This reconfirms at the sharp-inequality level that the `+1` is the single unit of budget slack
   `n−(n−1)` — a genuinely non-local quantity (matches R8/R9 meta).
2. `M(0⁺)≤1` ALONE is insufficient: the §7a decoy `F'` has `M(0⁺)=0` yet `I_n>0`. So the loaded IH
   must read `F'`'s genuine dyadic-refinement shape (its count function `g=N_{F'}`), not merely its
   part-count — exactly the "cut-tree origin" direction the meta demands.

## Where it stalled (honest gap, GAP-P1′)
Prove `I_n = ∫_{(0,θ)}⌊M/2⌋ ≤ 0`. The reduction is unconditional; the open content is a loaded
shape-property `P2(g)` of `g=N_{F'}` that (i) inherits under one further peel and (ii) forces
`(LAYER≤)` for every partition `π_0` of `2^n`. Tested and NOT closed: the scalar even-rank bound
(too weak); induction on the budget `b` from base `b=0` (base clean — `F'` forced to be the uncut
ladder — but the step of adding one cut to `F'` while lowering allowed `a_0` was not shown
`I_n`-monotone).

## Value banked
- Promotable: the `(FLOOR)` identity + layer form (cleanest restatement of GAP L to date; supersedes
  `(△⋆)`). Recommend certifying into `lemmas/`.
- The reduction is now a single scalar inequality with explicit integrand `⌊M/2⌋`, with every
  hypothesis's role isolated — a much better launch point for the loaded IH next round.

## Spec concerns
- None on the problem statement / target. The reduction target `I_n≤0` is provably equivalent to the
  problem's Case B (exact identity, not a heuristic), so no scope drift.
- Cross-approach note (not a concern, an opportunity): `(FLOOR)`'s finding that the residual's
  infimum is `0` and tie-attained, together with the sibling GAP-IMR/Parity-Lemma route, suggests
  `I_n≤0` might be closeable by showing the max of `I_n` (a piecewise-linear function of part
  positions) is attained where `M` is "integer-like" — but that is the sibling's integrality route,
  deliberately kept out of this (integrality-free) lane.
