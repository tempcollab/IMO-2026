## Status
partial

(This slug dead-ends: the load-bearing per-cell cap it was built on is numerically REFUTED by its
own make-or-break gate. It contributes a decisive NEGATIVE — the 10th dead lower lever — not a proof.
The overall problem remains `partial`; the certified reduction chain is untouched.)

## Approaches tried
- **scale-origin-layercake (LOWER, NEW R17) — DEAD (10th dead lower lever).** Value-side layer-cake
  (co-area slicing of `g` by g-VALUE) paired with a per-cell cap indexed by ONE-REC dyadic
  *scale-of-origin* `j` (aimo-0009 "index-into-itself" flavor). Target: the certified cross-scale
  residual `(★) Σ_{i≥1} μ{g≥2i} ≤ Σ_{i≥1} μ{g≤1−2i}` (⟺ `∫⌊g/2⌋≤0` ⟺ MID-core `μ{g odd}≥1`,
  `|F|≥3`). **Make-or-break GATE RESULT: the cap is FALSE (~50% exceptions), so the lever fails
  (failure mode (1) of the dispatch).** Details below. The kill is structural, not a boundary
  artifact: deficits reach the full scale mass `2^j`, and 113/122 of the i=1-termwise-failing
  witnesses are among the failures — the credit that repays a scale-`j` super-level deficit is
  generated at OTHER scales, so NO cap local to the scale-of-origin index can capture (★). The only
  structural B-tagging available is loss-free (it reproduces (★) exactly) but its scale-local
  aggregate is the very inequality that fails. Do NOT re-propose any per-(g-level, dyadic-scale)
  LOCAL cell cap: the cross-scale lending is real at the coarsest granularity.
- (prior lower levers 1–9 and the upper leader are recorded in `current.md`; not restated here.)

## Current best
No new positive progress on the lower wall. The furthest rigorous progress remains the certified
reduction chain (unchanged this round):

- Lemma **MID** (`mass-difference-reduction`, certified): with `g = N_F − N_B` on `(0,2^{n−1})`,
  `D(S) = μ{g odd}` and `∫ g = 1`; so the `a=0` lower bound `D(S) ≥ 1` for `|F| ≥ 3` is exactly
  **MID-core** `μ{g odd} ≥ 1`.
- Rescaling CLIP's `τ=0` face (Lemma **CLIP**, certified) by `−½` gives the identity
  `D(S) = 1 − 2∫_0^{2^{n−1}} ⌊g/2⌋`, hence MID-core ⟺ `∫⌊g/2⌋ ≤ 0`. The standard layer-cake split
  `⌊g/2⌋ = Σ_{i≥1} 1[g≥2i] − Σ_{i≥1} 1[g≤1−2i]` (valid for integer-valued `g`, since
  `⌊g/2⌋≥i ⟺ g≥2i` and `⌊g/2⌋≤−i ⟺ g≤1−2i`) integrates to
  `∫⌊g/2⌋ = Σ_i μ{g≥2i} − Σ_i μ{g≤1−2i}`, so `∫⌊g/2⌋ ≤ 0 ⟺ (★)`.
- `(★)` is CERTIFIED-TRUE and tight (0 failures / 21000 exact-`Fraction` adversarial `a=0`
  refinements at `n=4,5,6` this round + explorer's 0/900; worst margin ≈0.0093). The TERMWISE
  per-level reduction is FALSE (always at `i=1`) — (★) genuinely needs cross-level cancellation.

**The open gap (unchanged, now with one more mechanism ruled out):** (★) needs a genuinely
cross-scale mechanism. This round proves that the mechanism is NOT scale-local in the ONE-REC
scale-of-origin index (see below). The lower wall still has no live vehicle.

### Why the scale-of-origin cap is dead — the gate, in full

**Objects.** `F` = fragments of the top `2^n` (each `≤ L:=2^{n−1}`, `ΣF=2^n`, `|F|≥3`);
`B = ⊔_{j=0}^{n−1} G_j`, `G_j` = fragments of ladder piece `2^j`, `ΣG_j = 2^j` (Lemma ONE-REC).
`g = N_F − N_B` on `(0,L)`. Note `g(0+) = |F|−|B| ≤ 1` (budget `|F|+|B| ≤ 2n+1`, `|B|≥n`), so for
every `i≥1` neither `{g≥2i}` nor `{g≤1−2i}` touches `t=0+`.

**The only structural B-tagging (scale-of-origin).** As `t` increases, `g` jumps UP exactly at
B-values (where `N_B` drops) and DOWN at F-values (where `N_F` drops). Hence:
- every maximal interval of `{g≥2i}` is *opened* (left endpoint) at a B-value — assign it the scale
  `j` of that B-fragment: `α_{i,j}` := total measure of level-`i` super-intervals opened by `G_j`;
- every maximal interval of `{g≤1−2i}` is *closed* (right endpoint) at a B-value — assign it that
  scale: `β_{i,j}` := total measure of level-`i` sub-intervals closed by `G_j`.

This is the *unique* scale-of-origin tagging (B is the only multiset with a scale decomposition; F is
a single scale `n`). It is loss-free: verified exact over 9000 refinements,
`Σ_{i,j} α_{i,j} = Σ_i μ{g≥2i} = LHS(★)` and `Σ_{i,j} β_{i,j} = Σ_i μ{g≤1−2i} = RHS(★)`, 0 mismatches;
and `α` is never assigned to a non-B endpoint (0/12000), confirming super-levels are always opened by
a genuine `G_j` fragment.

**The cap that any local decomposition forces.** A per-cell cap `C(i,j)` is *scale-local* iff it
relates only scale-`j` quantities (`α_{·,j}`, `β_{·,j}`). If a family of scale-local caps sums to
(★), then summing over the level index `i` at fixed `j` yields the **per-scale statement**
`Σ_i α_{i,j} ≤ Σ_i β_{i,j}` for every `j`. (Any level shift `α_{i,j} ≤ β_{i+s,j}` implies this by
telescoping; the aimo-0009 self-referential form pairs `α` with `β` at a *shifted level but the same
scale*, so it too implies the per-scale statement.) **This per-scale statement is exactly the
make-or-break cap `C(i,j)` for the lever.**

**Gate result (exact `Fraction`, sympy-free rationals, `n=4,5,6`).**
| scale-pick rule | per-scale cap `Σ_iα_{i,j} ≤ Σ_iβ_{i,j}` | on i=1-failing witnesses |
|---|---|---|
| `max`-scale at coincident values | **4529 / 9000 FAIL** | 113/122 fail |
| `min`-scale at coincident values | **4569 / 9000 FAIL** | (same order) |

Worst per-scale deficit `Σ_iα_{i,j} − Σ_iβ_{i,j} ≈ 15.92`, i.e. `deficit/2^j ≈ 0.995` — nearly the
**entire** scale mass `2^j`. Meanwhile (★) itself holds 9000/9000 in the same runs. So a scale-`j`
super-level deficit of order `2^j` is genuinely repaid by credit produced at DIFFERENT scales; the
repayment is non-local at the coarsest granularity the scale-of-origin index offers.

**Conclusion (the kill).** The bookkeeping is faithful, yet the *only* local cap it can support is
numerically false by ~50%, including on the i=1-termwise-failing witnesses the dispatch flagged as the
discriminator. Therefore **no per-`(i,j)` cap local to the ONE-REC scale-of-origin index establishes
(★).** The aimo-0009 hope — a self-referential per-cell `a_i+b_i ≤ f(2^j,i)` pairing an excess
against a *same-scale* shifted credit — fails here precisely because excess and matching credit sit at
*different* scales. This is failure mode (1) of the dispatch's mandatory gate: the cap is FALSE on the
witnesses, so the lever fails. It is the **10th dead lower lever**. (It is not failure mode (2), a
dressed tautology: the tagging is loss-free but its local aggregate is a *strictly false* strengthening
of (★), not a reframing of it — that is what refutes it rather than trivializes it.)

## Full proof
(Not present — Status is `partial`. This slug established a decisive NEGATIVE, not a proof.)

## Promotable lemmas
None new for certification. One reusable NEGATIVE fact for the record (a dead-end, not a lemma):

- **NO-SCALE-LOCAL-CAP (negative).** With the unique scale-of-origin tagging (`α_{i,j}` = super-level
  measure of `{g≥2i}` opened by a scale-`j` B-fragment; `β_{i,j}` = sub-level measure of `{g≤1−2i}`
  closed by a scale-`j` B-fragment), the tagging is loss-free (`Σα=LHS(★)`, `Σβ=RHS(★)` exact) but the
  scale-local aggregate `Σ_i α_{i,j} ≤ Σ_i β_{i,j}` is FALSE (~50%, deficits up to `≈2^j`, exact
  `Fraction`, `n=4,5,6`). Hence any per-`(g-level i, dyadic-scale-of-origin j)` LOCAL cell cap
  summing to (★) is impossible; the cross-scale lending is real at the scale granularity. Records
  the layer-cake × scale-of-origin lever as the 10th dead lower lever; do not re-open.
