# Proof-builder report — breakpoint-vertex (UPPER), Round 15

**Status: partial (genuine advance).** Slug: breakpoint-vertex. Verdict recommendation: CHANGES REQUESTED
(real progress, boundary closed, deep interior remains open).

## Mandatory exact gate — RESULT

Ran the exact `sympy`/`Fraction` gate (adversarial + structured, NOT random-only) BEFORE any prose,
per the binding precondition. Scripts: `/tmp/gate2.py`, `/tmp/verify.py`.

**Load-bearing definitional fix.** The residual is `Φ = min over NONEMPTY subsets` of the
descending-KK caterpillar value (0 admissible via a nonempty even cancellation), NOT `min positive`.
Witness: `{30,25,20,15,10}/100` (valley, n=4) has min-positive reachable value `1/20 = 1.55·u₄`
(would spuriously refute the target) but `Φ=0` via the nonempty subset `{30,25,20,15}`. Matches R13.

- **G1 (deep margin):** deep region `a₁ ≤ L/2 − c·u_n` has adversarial worst `Φ/u_n = 0.72/0.67/0.58`
  at `n=3/4/5` (c=1/2 and c=1); the margin (~0.3) does NOT shrink to 0 with n and does not improve
  past c≈1/2. **BUT** the deep minimiser needs unbounded-order cancellation (the 4-element
  `{30,25,20,15}` on `{30,25,20,15,10}/100`; min pairwise there is `1.55·u₄`), so NO bounded (1–2
  move) analytic mechanism realises it. G1 = numeric margin exists, but the required *provable*
  mechanism does NOT. Deep region NOT closeable this round.
- **G2 (boundary continuation of `D=2a₁−L`):** PASS, and upgraded to a THEOREM. `Φ(A) ≤ |2a₁−L|`
  holds universally (0 fails, >100k exact profiles, valley + general); already witnessed by the
  full-profile caterpillar (`descKK(fullset) ≤ |2a₁−L|`, 0 fails). EQUALITY on the VALLEY-TIGHT
  family `A^{(n)}` (`n=2..6`, ratios 0.778→0.985) and on the R14 maximiser `{16,8,4,3,2}/33`
  (`Φ=|2a₁−L|=1/33`). Exact/tight, not a margin bound.
- **G3 (cover):** trivial — dominant `a₁≥L/2` ∪ boundary `(L−u_nL)/2 ≤ a₁ < L/2` ∪ deep
  `a₁ < (L−u_nL)/2` partitions all `a₁`.

## What was PROVEN (rigorous, in the approach file)

**Lemma WTC (whole-tail continuation).** For `a₁≥…≥a_m>0`, `Σ=L`, the largest-first differencing value
`K=descKK(a₁,…,a_m)` satisfies `K ≤ |2a₁−L|`. Proof by the two-sided invariant
`a₁−P_k ≤ v_k ≤ |a₁−P_k|` (`P_k=a₂+…+a_k`), induction with a clean sign-split; at `k=m`, `P_m=L−a₁`.
Verified 0 violations / 300k adversarial profiles; equality on `A^{(n)}`.

**Corollary (boundary + dominant closed).** Full profile is a nonempty subset, so `Φ(A) ≤ K ≤ |2a₁−L|`.
For valley `a₁ ≥ (L−u_nL)/2` (⇒ `|2a₁−L|=L−2a₁ ≤ u_nL`), `Φ ≤ u_nL`, and certified R-COV'
(sufficiency) forces `D ≤ u_nL`. This is the exact continuation of certified whole-tail-peel across
`a₁=L/2` (that lemma is the `d≥0`/equality branch of WTC). Region `a₁ ≥ (L−u_nL)/2` closed rigorously.

## Residual (open crux, honestly surfaced)

Deep interior `a₁ < (L−u_nL)/2` (i.e. `|2a₁−L| > u_nL`). WTC gives only `Φ ≤ |2a₁−L| > u_nL`;
`Φ ≤ u_nL` there needs genuine multi-piece cancellation with margin — no analytic mechanism known,
bounded moves provably insufficient. Same first-gap / Subset-KK pigeonhole open since R7, now strictly
confined to the deep interior. This is a real reduction of the open region (from `a₁<L/2` to
`a₁<(L−u_nL)/2`), and the region VALLEY-TIGHT protected (boundary, where `A^{(n)}` lives) is closed.

## Promotable lemma for certification

**Lemma WTC** (`K ≤ |2a₁−L|` for largest-first differencing) — game-independent, fully proven, 0-fail
verified, tight on the extremal family. Ready to certify.

## Spec concerns

- The R14 conclusion "no margin ⇒ margin route dead" was correct only for a UNIFORM bound; the fix is
  the REGION SPLIT, and it works because the no-margin phenomenon is entirely boundary-layer.
- The certified R-COV' target `Φ` must be read as `min over NONEMPTY subsets` (0 allowed); the
  reachable-set "min positive" reading is a red herring (R13 already noted; re-confirmed decisive here).
- Next round: the DEEP interior is the whole remaining upper crux. WTC does not touch it. A deep lever
  must produce `Φ ≤ u_n` via unbounded cancellation — likely the same object as the LOWER wall's
  Gap-Interleaving exchange (flagged by the outline-reviewer's diversity note).
