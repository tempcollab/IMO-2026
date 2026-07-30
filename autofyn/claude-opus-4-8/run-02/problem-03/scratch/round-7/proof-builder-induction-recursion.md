# Build report — induction-recursion (imo-2026-03), round 7

Slug: `induction-recursion` (GAP L lower-bound residual `maxc≥2`, budget-count mechanism).
Status: **partial** (no gap closed; one natural sub-route provably killed; wall confirmed shared).

## What I did
Pushed the assigned budget-count mechanism on the residual target `(GOAL)`:
`O_B = Σ_j|B_{2j−1}| ≥ Σ_j|A_{2j}| = E_A` (equivalent to `D̃≥1` in Case B, via the certified
identity `D̃−1 = 2(O_B−E_A)`). Wrote up in §5E of the approach file.

## What I closed / confirmed rigorously
- Re-verified the round-6 rigorous parts: `(B1)` identity `D̃−1=2(O_B−E_A)` (error `3·10⁻¹⁵`
  over `5·10⁴` configs, n=3..5), `(B2)` deficit budget `E_A≤Σy_{2j}` (0 violations), and the
  tie config `n=4,Y=(8,3,3,2),Z=(8,2,2,2,1)` gives `D̃=O_B=E_A`-boundary `D̃=1` exactly.
- **NEW negative result (E1), rigorous:** the natural **term-by-term** super-level pairing
  `|A_{2j}| ≤ |B_{2j−1}|` is **FALSE**. Explicit witness (Case B, n=4, a=2, b=2):
  `Y=(7.9362,7.1735,0.8903)`, `Z=(4,3.4776,2.7687,2,1.7536,1)` — `|A_2|≈3.17 > |B_1|≈2.77`,
  yet `O_B≈4.52 ≥ E_A≈3.17`. Hundreds of witnesses for `b≥2`; aggregate `O_B≥E_A` holds in
  every one. So `(GOAL)` is irreducibly aggregate — no monotone super-level / level-matched
  pairing can prove it. This kills the most natural budget-count sub-route (and is a useful
  dead-end to bank: a "super-level pairing" would be a wasted third mechanism).
- **NEW localization (E2):** the `b=0` slice (all budget on top, `Z` = uncut dyadic) has genuine
  slack over `maxc≥2`: `min D̃ ≥ 1.029` (n=3,a=2) up to `1.486` (n=5,a=5), 8·10⁴ draws each,
  0 violations. So the tight `maxc≥2` infimum-`1` boundary lives ONLY at `b≥1` near-tie configs
  (near-equality between `y₁` and a `Z`-anchor). The hard slice is thus precisely `b≥1` with a
  `Z`-cut-fragment tie — not "many top fragments."

## What remains open (the gap)
`(GOAL)` `O_B ≥ E_A` itself — the width-weighted anchor lower bound on `O_B` through `Z`'s
cut-tree. This is the SAME inequality as the telescope twin's Step-5 (as the outline-reviewer
predicted). I could not close it, nor the `b=0` special case cleanly (the dyadic gives only
upper bounds `a_ℓ≤y_ℓ`, `b_ℓ≤z_ℓ`; `O_B` needs a *lower* bound on `b_odd` coupling `N_Z` to
where `N_Y` is small — the coupling is the wall).

## Spec / escalation concern (important for the orchestrator)
Both GAP-L slugs (this one and telescope) now sit on the identical inequality `(GOAL)`, and this
round proves the termwise closure of it is impossible. Per the outline-reviewer's explicit
short-leash note ("if BOTH GAP-L mechanisms stall on the width-weighted domination, escalate —
the field has collapsed; GAP L needs a genuinely different framing, not a third mechanism for the
same inequality"), the trigger is met. Recommend next round the outliner seed a genuinely
different top-level framing for the lower bound — candidates I'd suggest: (a) LP/minimax duality
certificate on the reduced discrepancy game (a dual feasible weighting rather than a primal
count), or (b) an amortized potential over Xiang's cut *sequence* (dynamic) rather than the static
final multiset. A fourth attack on `O_B≥E_A` should be avoided.

## Lemma proposed for certification
None new this round worth certifying as a positive lemma. The round-6 candidate
`super-level-reduction.md` (the `(B1)` identity `D(F)−(sumY−sumZ)=2(Σ|B_{2j−1}|−Σ|A_{2j}|)`)
remains a valid, fully-proved, reusable identity — still recommended for promotion. The (E1)
refutation of termwise pairing should be recorded as a banked dead-end (not a certified lemma).
