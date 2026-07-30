# Proof-outliner field — Round 10 — imo-2026-03

SOLE open wall: GAP L (lower bound, Case B) = prove `D̃(F) ≥ 1` for every real feasible
refinement `F=⊎_{j=0}^n π_j`, `Σa_j≤n`. Upper bound DONE/certified (`lemmas/upper-bound.md`) —
NOT reopened. Two live far-apart routes (peel-induction on `n` = GAP-P1; integer-minimizer
reduction = GAP-IMR) plus certified `+1` injector (Parity Lemma). Field below advances both
live routes with the sharpened gap-plans the explorers pointed to, and opens ONE new slug that
runs a second, genuinely-distinct mechanism on the cleanest gap (GAP-IMR) via a certified tool.

Import freely (do NOT re-derive): `parity-odd-total.md` (Parity Lemma: integer parts + odd total
`2^{n+1}−1` ⇒ `D̃` odd ⇒ `D̃≥1`), `peel-difference-bound.md` (SD/(PEEL) identity, (DIFF), Case A,
Invariant I), `merged-order-layer.md`, `termwise-lattice.md`, `greedy-claim.md`, `cut-flip.md`.

---

## imo-2026-03

### peel-scale-rank-induction: revise (advance the same route, re-plan GAP-P1)
Target: `D̃(F) ≥ 1` for every feasible `F` (whole problem, with certified UB) — strong induction on `n`.
Technique: peel the top dyadic scale `F=π_0⊎F'`; certified SD/(PEEL)/(DIFF)/Case A already close
Case A + the region `{|D̃(π_0)−D̃(F')|≥1}` (80.8%). Re-plan the residual `{|D̃(π_0)−D̃(F')|<1}`
with a **LOADED, coupled multi-scale IH** — NOT the plain scalar `D̃(F')≥1` (proven insufficient,
§7a witness `D̃(F')=2.506`, `D̃(F)=0.146`), and NOT any static profile of `F'` (R8 meta).
Skeleton:
  1. Base `n≤1`, Case A, and `{|D̃(π_0)−D̃(F')|≥1}` — CLOSED (certified `peel-difference-bound.md`).
  2. Residual target (restated exactly): `2λ(O_{π_0}∩O_{F'}) ≤ D̃(π_0)+D̃(F') − 1` on `(0,θ)`,
     `θ=2^{n−1}` — by (PEEL), since above `θ`, `O_{F'}=∅`.
  3. Strong-induct NOT on `n` alone but on the **cut-budget** `b=Σ_{j≥1}a_j` (bounded integer,
     Invariant I already keys on `b`), carrying the **per-scale cut vector** `(a_1,…,a_n)` as loaded
     state — this fixes `F'`'s recursive granularity, the exact info a decoy multiset lacks (§7a).
  4. Co-induct a **coupled pair** (aimo-0377 shape): propagate down the SAME overlap object one
     scale further — with `F'=π_0'⊎F''`, carry `(P1: D̃(F')≥1)` AND `(P2: a cap on the top-overlap
     of `F'`)`, and prove the two claims close each other under one peel level (the way the naive
     scalar fails to close alone but the 3-claim system in aimo-0377 does).
  5. Loaded IH ⇒ residual bound (step 2) ⇒ `D̃(F)≥1`. With certified UB ⇒ `c(n)=2^n/(2^{n+1}−1)`.
Key lemmas (claim + mechanism):
  - Loaded IH `L(F')` = coupled pair `(D̃(F')≥1 ; overlap-cap P2(F'))`, indexed by `(a_1,…,a_n)`,
    inherited under one peel — because peeling `F'=π_0'⊎F''` reproduces the SAME (PEEL) identity one
    scale down, so `P2` at level `n` follows from `(P1,P2)` at level `n−1` exactly as aimo-0377's
    `f(3i)>0` follows from the shifted-residue triple. P2 must satisfy: strictly stronger than
    `D̃(F')≥0`, inherited, AND forces `2λ(O_{π_0}∩O_{F'}) ≤ D̃(π_0)+D̃(F')−1` for EVERY partition
    `π_0` of `2^n`.
Open gaps: pin the exact `P2` (the overlap-cap) that is both inherited under peel AND yields the
  residual inequality — the builder must state it and verify both (i) inheritance, (ii) sufficiency,
  each with an exact-`Fraction` numeric probe on genuine dyadic refinements before writing algebra.
Cases to cover: none new — Case A, `{|Δ|≥1}`, base cases already closed; only `{|Δ|<1}` remains.
Watch out for: (a) opening 2 (force `a_1=0` / two-level-peel alone) is REFUTED — residual only
  shrinks 89%→89%, does NOT collapse; do not resubmit. (b) Circularity: any `P2` derivable from a
  static merged-order profile of the FINAL multiset is R8-dead; `P2` must read `F'`'s recursive cut
  origin. (c) use exact `Fraction`, never `limit_denominator` (float artifact showed false `min≈1−ε`).

### vertex-integrality-parity: revise (advance the same route, re-plan GAP-IMR — order-aware smoothing)
Target: GAP-IMR `min_{Φ_n}D̃ = min{D̃(F):F integer}`; then Parity Lemma ⇒ `D̃≥1` (whole problem).
Technique: **minimality-driven smoothing at the GLOBAL optimum** (kb "piecewise-concavity
smoothing" / exchange), replacing the refuted independent per-group rounding (7847/18900 violations,
cross-group order inversions). Use the certified block-contribution structure (§3.2): even tie-blocks
contribute `0` to `D̃` and are freely resplittable; only ODD fractional tie-blocks obstruct.
Skeleton:
  1. `μ=min_{Φ_n}D̃` attained at a rational vertex `v*` of a merged order-type cell (certified §3.1).
  2. If `v*` integer ⇒ Parity Lemma ⇒ `μ≥1`, done. So assume `v*` fractional; pick the minimizer
     minimizing a fractionality monovariant `Φ` (e.g. #distinct non-integer values, or total denom).
  3. KEY: at a GLOBAL minimizer no ODD fractional tie-block survives. Mechanism: an odd block `B`
     (value `v`, groups `g` with counts `n_g`) contributes `±v` (§3.2). Perturb `v→v±ε` with a
     **joint, order-aware compensation** — move the `n_g·ε` mass into an ADJACENT even/free block of
     the SAME group `g` (this keeps every group-sum `2^{n−j}` fixed AND preserves the merged order,
     the exact failure mode of independent rounding). `D̃` is affine in `ε` with slope `±1·(#odd
     blocks net)`; minimality forces BOTH directions blocked ⇒ the perturbation is stopped by a
     collision (two adjacent blocks merge, or a coordinate hits `0`/a group face) ⇒ `Φ` strictly
     drops with `D̃` non-increasing.
  4. Descend on `Φ` ⇒ contradiction with `v*` minimal, OR reach an integer minimizer ⇒ `μ≥1`.
Key lemmas (claim + mechanism):
  - Block-contribution formula (certified §3.2): a tie-block of size `r`, value `v`, first rank `i`
    contributes `(−1)^{i−1}v·1[r odd]` — because consecutive equal terms in the alternating sum
    cancel in pairs, leaving one `±v` iff `r` odd. This is why even blocks are free and only odd
    fractional blocks matter.
  - Order-aware compensating perturbation stays feasible (group sums fixed) AND `D̃`-affine —
    because moving mass within one group between an odd block and an adjacent same-group block keeps
    `Σπ_j` and the merged order, so `D̃(ε)` is linear until a collision.
Open gaps: prove the perturbation is `D̃`-non-increasing in at least one direction while strictly
  reducing `Φ` at a true minimizer (the descent/monovariant), and that an adjacent same-group
  companion block always exists to absorb the mass (else handle by moving across the group's other
  parts). Must NOT reintroduce cross-group order inversion — that killed the naive version.
Cases to cover: odd fractional block with vs without an even same-group neighbor; the boundary
  collision types (block-merge, coordinate→0, coordinate→group-face).
Watch out for: (a) do NOT round per-group independently (REFUTED). (b) do NOT claim per-cell TU /
  integral vertices (REFUTED R9 — fractional vertices exist at non-optimal cells; the argument MUST
  use global minimality, not cell geometry). (c) non-circular: the smoothing references only "is `v*`
  integer," never the value `1`.

### peel-integral-exchange: new  (copy-of vertex-integrality-parity)
Target: GAP-IMR (integer minimizer) ⇒ Parity Lemma ⇒ whole problem — SAME gap as
vertex-integrality-parity, but a genuinely DIFFERENT tool (the certified peel identity as a
**cross-SCALE** mass-transfer engine, vs the twin's within-group same-value smoothing). Justifies a
copy: two viable, distinct mechanisms on the cleanest gap; they cannot die together (one moves mass
within a scale, the other across scales — the two halves of §3.2's obstruction).
Technique: certified SD/(PEEL) `D̃(F)=D̃(π_0)+D̃(F')−2λ(O_{π_0}∩O_{F'})` + (DIFF), used as an
exchange/rounding tool on a GLOBAL minimizer (the cross explorer's one surviving synergy).
Skeleton:
  1. Take a global minimizer `F*`; peel top scale `F*=π_0⊎F'`. `Σπ_0=2^n` is an INTEGER group-sum
     ⇒ π_0 CAN be integralized to a partition `π_0^Z` of `2^n` (the §3.2 obstruction — fractional
     group-block-sum `n_g·v∉ℤ` — bites only for a tie-block SPANNING scales, handled in step 3).
  2. KEY: choose `π_0^Z` so that `λ(O_{π_0}∩O_{F'})` does not decrease and `D̃(π_0)` does not
     increase, hence by (PEEL) `D̃(π_0^Z⊎F') ≤ D̃(F*)`; bound the change with (DIFF) applied on the
     interval `(0,θ)` where the two odd-level sets interact.
  3. Recurse the same integral rounding down the scales `j=1,…,n` (each `Σπ_j=2^{n−j}` integer),
     controlling the cross-scale overlap change with (PEEL) restricted to each scale's sub-interval.
     For a tie-block that SPANS scales (the true §3.2 obstruction, `n_g·v∉ℤ` within a group), move
     the compensating mass ACROSS the scales it touches — precisely what the peel identity is built
     to track — instead of within one group.
  4. Terminate at an integer `F^Z∈Φ_n` with `D̃(F^Z) ≤ D̃(F*)=μ`. Since `μ` is the min,
     `D̃(F^Z)=μ`, so `μ` is attained at an integer config ⇒ Parity Lemma ⇒ `μ≥1`. Whole problem done.
Key lemmas (claim + mechanism):
  - Scale-local integral rounding is `D̃`-non-increasing — because (PEEL) makes `D̃` a sum of
    `D̃(π_j)` terms minus overlaps, and rounding one scale to integers (its group-sum being integer)
    while preserving the odd-level-set nesting keeps every overlap `λ(O_{π_i}∩O_{π_j})` from growing;
    (DIFF) caps the residual change.
  - Cross-scale transfer resolves the `n_g·v∉ℤ` obstruction — because the missing integer mass in a
    scale-spanning tie-block is supplied from an adjacent scale of the same value-neighborhood, a move
    (PEEL) tracks exactly (it is scale-additive), which the within-group twin cannot do.
Open gaps: prove step 2's choice of `π_0^Z` exists with both monotonicities, and that the
  scale-recursive rounding terminates integer with `D̃` never increasing (the scale-spanning
  tie-block case is the crux — verify numerically on the documented tie witness `n=4` Y=(8,3,3,2)
  Z=(8,2,2,2,1) and fractional cell `(4,2,½,½)` BEFORE writing algebra).
Cases to cover: integer vs fractional `π_0`; tie-block confined to one scale vs spanning ≥2 scales.
Watch out for: (a) do NOT use per-cell TU (REFUTED). (b) The advantage claim over the twin is
  cross-scale mass movement — if the builder ends up moving mass only within a scale, it collapses
  into the twin; keep the cross-scale exchange as the load-bearing step. (c) exact `Fraction` only.

---

## Not opened this round (documented, not padding)
- **aimo-0917 2-adic valuation split `N=N_+ + N_-`** (dispatch item 3): I judge it NOT viable as a
  standalone slug. A valuation-of-a-count still requires integer structure to have a `v_2`, so it does
  NOT actually avoid the integrality wall the parity route hits — it dresses the SAME "the extremal
  config must be integer" obstruction in valuation language, without supplying a concrete count whose
  `v_2` is forced independent of integrality. Opening it would pad the field with a vague skeleton.
  Reserve it (and aimo-0663 shadow/position-map to the canonical `D̃=1` family) as the fallback IF all
  three approaches above stall next round — at which point a monovariant descent to the explicit
  canonical minimizer `{2^{n−1},2^{n−1},…,3,2,1,1}` (transport every `F` to it by budget-preserving,
  `D̃`-non-increasing moves) is the more concrete far framing to seed.
- The cross explorer PROVED that pushing the Parity Lemma directly through the peel step is
  structurally CIRCULAR (needs GAP-IMR on the residual first). Do NOT seed "parity-through-peel."

## Proposed field (to the outline-reviewer)
- **peel-scale-rank-induction** (revise/advance): loaded coupled multi-scale IH (aimo-0377 pair +
  per-scale cut vector) closing the near-balance residual `{|D̃(π_0)−D̃(F')|<1}`. [induction framing]
- **vertex-integrality-parity** (revise/advance): order-aware minimality smoothing kills odd
  fractional tie-blocks at the global optimum ⇒ integer minimizer ⇒ Parity Lemma. [minimizer, within-scale]
- **peel-integral-exchange** (new, copy-of vertex-integrality-parity): certified peel SD/(DIFF) as a
  cross-SCALE integral rounding of a global minimizer ⇒ integer minimizer ⇒ Parity Lemma. [minimizer, cross-scale]
