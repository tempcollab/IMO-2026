# Proof-reviewer — imo-2026-03, Round 15

Two built slugs, routed independently. Both builder-recorded statuses are ACCURATE (no overclaim).

---

## Slug 1: breakpoint-vertex (UPPER)

**Verdict: CHANGES REQUESTED. True Status: partial (genuine advance).**
Builder recorded `partial` — correct.

### (a) Is Lemma WTC rigorously proven? YES — certified.
Claim: for descending `a₁≥…≥a_m>0`, sum `L`, `K = descKK ≤ |2a₁−L|`.
I re-derived the two-sided invariant `(I_k): a₁−P_k ≤ v_k ≤ |a₁−P_k|` (`P_k=a₂+…+a_k`) from
scratch, independently of the write-up:
- Base `k=1` both sides `=a₁`. ✓
- Lower bound `v_k ≥ v_{k−1}−a_k ≥ d−a_k = a₁−P_k` uses only `v_{k−1}≥d` (lower half of the IH),
  valid for either sign of `d`. ✓
- Upper bound, `d≥0` branch: `|d|=d` pins `v_{k−1}=d`, giving equality `v_k=|a₁−P_k|`. ✓
- Upper bound, `d<0` branch: `t=v_{k−1}∈[0,−d]`, `|t−a_k|` maximised at an endpoint;
  both endpoints `≤ a_k+(−d)=|a₁−P_k|` (one by monotonicity, one by triangle inequality). ✓
Every step is justified; no hand-waving, no hidden case. `k=m` gives `K ≤ |a₁−(L−a₁)| = |2a₁−L|`.
Independent numeric check: **0 violations / 200 000 exact-`Fraction` adversarial profiles** (`m=1..7`),
and **equality** `K=|2a₁−L|` on `A^{(n)}={2^n,…,4,3,2}/(2^{n+1}+1)` for `n=2..6`.
→ **CERTIFIED as `lemmas/whole-tail-continuation.md`** (30 lemmas total).

### (b) Does the boundary closure respect VALLEY-TIGHT? YES.
The corollary chain is sound: `Φ(A)=min_{∅≠T}descKK(T) ≤ descKK(full) ≤ |2a₁−L|` (full profile is a
nonempty subset). For `a₁ ≥ (L−u_nL)/2` with `a₁<L/2`: `|2a₁−L|=L−2a₁ ≤ u_nL` (verified:
`2a₁≥L−u_nL ⟺ L−2a₁≤u_nL`), so `Φ ≤ u_nL`, and certified R-COV' (sufficiency) forces `D ≤ u_nL`.
This is NOT a margin bound — it is EXACT, with equality on `A^{(n)}` (whose `a₁=2^n/(2^{n+1}+1)` sits
`~u_n/2` below `L/2`, i.e. inside this boundary layer). It is the literal continuation of certified
whole-tail-peel (`a₁≥L/2 ⇒ D=2a₁−L`, the `d≥0`/equality branch of the invariant) across `a₁=L/2`.
VALLEY-TIGHT forbids margin bounds because `A^{(n)}` drives `Φ/u_n→1`; WTC is compliant precisely
because it is tight on exactly that family. No hidden margin.

### (c) Is the deep interior honestly surfaced as open? YES.
Deep region `a₁<(L−u_nL)/2` ⟺ `|2a₁−L|>u_nL`, so WTC gives only `Φ ≤ |2a₁−L| > u_nL` — vacuous.
Builder states this plainly and does not overclaim; the `{30,25,20,15,10}/100` witness (deep, needs a
4-element cancellation to reach `Φ=0`) shows bounded moves are insufficient. This is the same
first-gap/Subset-KK pigeonhole open since R7, now strictly confined to the deep interior — a real
reduction of the open region, not a repackaging.

**Scoring.** Correctness 10/10 (WTC proof valid, corollary logic valid). Rigor 9/10 (deep interior
honestly left open). Progress: real — the open valley shrinks `a₁<L/2 → a₁<(L−u_nL)/2`, and the
VALLEY-TIGHT-protected boundary layer is closed EXACTLY.

**Gap that remains (for next round):** the DEEP interior `a₁<(L−u_nL)/2` — prove
`Φ(A)=min_{∅≠T}descKK(T) ≤ u_nL` there via genuine unbounded multi-piece cancellation (NOT a bounded
move, NOT a covering radius, NOT a margin/mass-telescope — all dead). WTC does not touch it.

---

## Slug 2: gen-func-transform (LOWER)

**Verdict: RETHINK. True Status: unsolved (decisive negative — genuine 7th dead lower lever).**
Builder recorded `unsolved` — correct.

### Is the refutation sound and decisive? YES — reviewer-reproduced.
The identity `Z(−1)=L−2μ{g odd}` (MID-core ⟺ `Z(−1)≤L−2`) is certified-MID repackaged and closes
nothing — builder states this. The slug's only non-repackaging content is the two-band recursion, and
it is refuted:
- The deviation `Z_n(−1) − [TopBand + Z_{n−1}(−1)] = −2∫_{O_F∩(0,L/2)}(−1)^{g'}` is exactly `−2×` the
  certified DEAD SPLIT cross-term `μ(O_F∩O_B)`.
- **Collision reproduced exactly** (my independent computation of `Z(−1)=∫₀^8(-1)^{N_F−N_B}` on the
  three multisets): fixed top-data `F={8,5,3}`, `F_B={4,4}`, three admissible `B_B` refinements of
  `C_2={4,2,1}` (each sum 7, each with `Z_{n−1}(−1)=0`) give `Z_4(−1) = −4, −2, 0` respectively.
  So `Z_n(−1)` is NOT a function of `(F, F_B, Z_{n−1}(−1))` — no scalar-IH-carrying recursion exists.

Evaluating the transform at `z=−1` re-imports precisely the overlap object `μ(O_F∩O_B)` that Lemma MID
was built to eliminate — a reframing, not a reduction, same fate as vertex-polytope (R14) and LP-dual.
This is a HONEST negative: no fake proof shipped, gate run first in exact arithmetic on structured +
adversarial + cut-budget-respecting witnesses.

**Scoring.** Correctness 10/10 (refutation exact, reproduced). Progress: none toward the wall, but a
clean decisive dead-end that removes a whole object family — valuable for the ranking. **7th dead lower
lever (Z-transform / generating-function recursion on the static parity-measure).** Recorded so no
agent retries it. The LOWER wall still has NO live vehicle → back to the outliner for a genuinely
different global object (the shared Gap-Interleaving `O_F∩O_B` exchange, or a 2-scale self-similar
recursion — NOT another transform/potential/vertex/matching variant).

**Promotable lemmas:** none proposed; none certifiable (the two-band identity is a re-expression of
certified TB + split-cross-term, diagnostic only). Agreed.

---

## Summary
- breakpoint-vertex → **CHANGES REQUESTED** (partial). Lemma WTC CERTIFIED; UPPER boundary layer closed
  exactly; deep interior `a₁<(L−u_nL)/2` is the remaining gap.
- gen-func-transform → **RETHINK** (unsolved). Decisive 7th dead lower lever; LOWER wall needs a new object.
