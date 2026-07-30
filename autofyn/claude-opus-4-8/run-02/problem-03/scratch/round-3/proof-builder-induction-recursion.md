# Build report — induction-recursion (imo-2026-03 / IMO 2026 P3), Round 3

Slug: **induction-recursion**. Owns **GAP L** (lower bound, Case B: Xiang cuts Liu's top dyadic piece).
Status remains **partial** — GAP-LB′ is not fully closed, but the closed region is enlarged and the
residual is sharpened. No overclaim.

## What I closed / advanced this round

Working in the certified integer-unit normalization (Liu = `{1,2,…,2^n}`, total `2^{n+1}−1`, bottom
block = literal `(n−1)`-dyadic, target `D̃ ≥ 1`), inside Case B (`a ≥ 1` cuts on the top piece `2^n`,
`b ≤ n−1` on the bottom block, final `F = Y ⊎ Z`):

- **Threshold-domination refinement (new, fully proved).** The top-descendants `Y` sum to exactly
  `2^n = 2θ` with `θ := 2^{n−1}`. Two parts each `> θ` would sum to `> 2θ`, impossible; so **at most
  one `Y`-part exceeds `θ`**. Since every bottom part is `≤ θ` (`N_Z = 0` on `(θ,∞)`), the level
  function `N = N_Y ∈ {0,1}` on `(θ,∞)`, and therefore
  `D_top^> = λ(O ∩ (θ,∞)) = (y₁ − θ)⁺` **exactly** (`y₁ = max Y`), giving the **cancellation-free
  bound `D̃ ≥ (y₁ − θ)⁺` (◇◇).**
- **Consequence:** Case B is now **fully settled on `{ y₁ ≥ 2^{n−1}+1 }`** with no cancellation term
  at all — a far weaker demand than the domination corollary C3 (which needs `y₁ ≥ 2^n`). Combined
  with the round-2 bound `D̃ ≥ D_top^> + |D_top^< − D_bot|` (★★), Case B is closed on
  `{ y₁ ≥ 2^{n−1}+1 } ∪ { |D_top^< − D_bot| ≥ 1 − D_top^> }`.
- **Eliminated a dead route.** The natural "strengthen the IH to *confine* `O_Z` (or `O`) to a high
  region" idea is **REFUTED**: already at n=1, cutting the `2` into `x, 2−x` yields odd-set
  `(1,2−x) ∪ (0,x)`, which reaches arbitrarily close to `0`. So `O` is never location-confined; only
  its measure `λ(O)=D̃` is controlled. This confirms the residual is intrinsically a *joint*
  interleaving fact, not a one-sided containment — removing a tempting but doomed line for next round.

All new claims numerically verified: 0 violations of "≤ 1 top-part > θ", of `λ(O∩(θ,∞)) = (y₁−θ)⁺`,
of `D̃ ≥ (y₁−θ)⁺`, and of `D̃ ≥ 1` over 2·10⁵ random Case-B configs, n = 2..6.

Also carried forward (already rigorous from round 2): base `P(0)`; Case A (`a=0`, `D̃ ≥ 2·2^n −
(2^{n+1}−1) = 1` by C3); the exact threshold identity
`D̃ = D_top^> + D_top^< + D_bot − 2λ(O_Y^< ∩ O_Z)` with `D_bot = λ(O_Z) ≥ 1` by the strong IH.

## What remains open (precise unproven claim)

**GAP-LB′.** In the *doubly-balanced* residual region
```
y₁ < 2^{n−1}+1   (so D_top^> = (y₁−θ)⁺ < 1)   AND   |D_top^< − D_bot| < 1 − D_top^> ,
```
prove
```
2 λ(O_Y^< ∩ O_Z) ≤ D_top^< + D_bot + D_top^> − 1        (equivalently D̃ ≥ 1).
```
This is a **joint** bound on the overlap of the bottom's odd-set `O_Z` with the top's low odd-set
`O_Y^<` inside `(0,θ)`; it does NOT follow from `D_bot ≥ 1` alone (which controls only `λ(O_Z)`, not
its location) and — as shown above — cannot come from any one-sided confinement of either set.
Recommended (still-unclosed) mechanism: the **rank-interleaving** reformulation — merge `Y` and `Z`
into one sorted list, track the T/B label string, and apply Lemma G's signed sum on the merged order,
working with `λ(O_Y^< △ O_Z)` directly rather than through the opaque `2λ(∩)` cancellation term.
Numerics: true `min D̃ = 1` exactly across 2·10⁵ samples in this region — the theorem holds; only the
overlap bound is unproven.

## Promotable lemmas (for reviewer certification)

- **Half-total single-crosser identity (new, fully proved, reusable).** If a multiset `Y` of positive
  parts has total `S` and `θ = S/2`, then at most one part of `Y` exceeds `θ`; hence for any disjoint
  `Z ⊆ (0,θ]`, the combined odd-set `O = O_Y △ O_Z` satisfies `λ(O ∩ (θ,∞)) = (y₁ − θ)⁺` and the
  discrepancy `D(Y⊎Z) ≥ (y₁ − θ)⁺`. Proved in §5B (◇),(◇◇). Sharp, cancellation-free.
- (carried) Threshold block-decomposition + (★★) bound (round 2). Both good `lemmas/` candidates.

## Spec concerns (issues with the planned mechanism itself)

- The reviewer's spec ("exact recurrence `V(n,k)=f(n−1,k−1)` closes via merged-order signed sum,
  GAP-LB.1") is sound as a target, but the **merged-order signed-sum invariant is not yet a proof** —
  it reorganizes the same joint quantity `λ(O_Y^< △ O_Z)` and I could not extract a monovariant that
  forces `≥ 1` in the doubly-balanced region. The budget-split decomposition (bottom `= σ·V(n−1,b)`)
  by itself is provably **insufficient**: it delivers `D_bot ≥ 1` but the top can partially cancel
  `O_Z` (the r2 memory note: `D̃ ≥ D_bot` is FALSE, ~38% of random Case-B configs violate it). So any
  spec that hopes to finish from `D_bot ≥ 1` plus separate top data alone will fail; the missing
  ingredient is genuinely the *relative location* of `O_Z` inside `O_Y^<`, which requires tracking the
  interleaving jointly. This is a real (not cosmetic) gap and the field should treat GAP-LB′ as still
  needing a new joint invariant, not a repackaging of the block split.
- Equality-robustness respected throughout: no strict domination `W(n−1,b) > u` reintroduced; every
  step (◇), (◇◇), (★), (★★) is an inequality/identity that holds with equality on the attained family.
