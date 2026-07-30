# Build report — parity-measure-potential (round 7)

Status: **partial** (advanced; lower gap re-reduced, not closed).

## Spec concerns
- **The outliner's specific structural invariant is FALSE.** Step 3 of my assigned skeleton asked
  to prove "`O_B` meets each dyadic gap of `C_{n−1}` in a single interval." This is numerically
  refuted by a **budget-respecting** witness: `B = {1, 1.865, 2, 2.135, 2.915, 5.085}` (a `c_B=2`
  refinement of `{1,2,4,8}`, so within budget `≤ n−1 = 3`) has
  `O_B ∩ (2,4) = (2, 2.135) ∪ (2.915, 4)` — TWO intervals. The interval count is budget-dependent
  (each cut landing a fragment in a gap can add a toggle), so the per-gap single-interval
  accounting in step 4 has no foundation. I did not force the false invariant; I re-derived the
  correct upstream object instead (see below).

## What I closed / advanced
- **Lemma MID (mass-difference reduction) — NEW, FULLY PROVED.** For an admissible `a=0`
  refinement `S = F ⊔ B`, with `g := N_F − N_B` on `(0, 2^{n−1})`:
  - (a) `D(S) = μ{ t : g(t) odd }` (Lemma M + `N_S = N_F + N_B`, and `N_S = 0` for `t ≥ 2^{n−1}`);
  - (b) `∫_0^{2^{n−1}} g = Σ F − Σ B = 2^n − (2^n−1) = 1` (layer-cake / Fubini).
  Hence L2 (`D(S) ≥ 1`) `⟺` **MID-core**: `μ{g odd} ≥ ∫g = 1`.
  This **eliminates the cross term** `μ(O_F∩O_B)` entirely — no `D(F)`, `D(B)`, min-cap, or
  balanced/unbalanced dichotomy remain. The unexplained `−1` deficit of the old GAP L2-exch is now
  exactly the mass identity `ΣF − ΣB = 1` (the ladder's superincreasing signature). This is the
  honest realisation of "the fix is upstream." Verified on `3·10^4` budget-respecting `n=4`
  refinements: `∫g=1`, `μ{g odd}=D(S)`, `D(S)≥1` in every case.
- Closed **within MID**: the `|F|=2` case (`N_F` even ⇒ `μ{g odd}=D(B)≥1` by IH LB(n−1)) and the
  `0≤g≤1` exact-floor case (`D(S)=1`). Residual is strictly `|F|≥3`.
- Showed the **pure-integral** version is false (`g≡2` on measure `1/2`), so the ladder structure
  of `B` (Lemma ONE recursed) is genuinely required — but now isolated to one clean scalar claim.

## What remains
- **GAP MID-core** (open): for `|F|≥3`, prove the integer step function `g = N_F − N_B` with
  `∫g=1` has `μ{g odd} ≥ 1`. Needs a monovariant/exchange using Lemma ONE recursed (at each
  scale `2^j`, `≤1` B-piece exceeds `2^j`). This is the same combinatorial content as
  induction-peel's exchange and merge-interleave's reachable-word minimisation, now cross-term-free.

## Lemmas proposed for certification
- **Lemma MID** (statement + full proof above; self-contained on certified Lemma M). Reusable in
  every measure-based lower-bound approach; cleaner replacement for the SPLIT cross-term route.
- **Negative record:** the "≤1 `O_B`-interval per dyadic gap" invariant is false (witness above) —
  record so no future round re-attempts the per-gap single-interval accounting.

Written to results/imo-2026-03/approaches/parity-measure-potential.md.
