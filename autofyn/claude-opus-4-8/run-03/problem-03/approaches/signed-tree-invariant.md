## Status
unsolved (NEW round 19 — UPPER wall, deep interior). Second, ANALYTIC framing (far from the
counting/divide-and-conquer route): extend certified Lemma WTC's two-sided partial-sum invariant
from a single caterpillar to a SUBSET-CHOICE statement, exploiting the deep gap `a₁ < L/2 − u_nL/2`
to force some subset's descending-differencing value ≤ u_nL by an exact interval-nesting invariant.

## Target
The whole IMO-2026-P3 upper bound (same as every UPPER approach): valley profile, Xiang forces
`D ≤ u_nL`, `u_n=1/(2^{n+1}−1)`; with the certified lower bound ⇒ `c(n)=2^n/(2^{n+1}−1)`.

## Technique (the spine — distinct route)
An EXACT two-sided interval invariant on the reachable value as pieces are folded in a CHOSEN
order, generalising certified WTC. WTC proved, for the full caterpillar, `a₁−P_k ≤ v_k ≤ |a₁−P_k|`,
giving `descKK(full) ≤ |2a₁−L|` — exact, tight, but too big in the deep interior. The new content:
instead of one fixed fold, track the invariant over an ADAPTIVELY CHOSEN inclusion order and show
the reachable interval `[lo_k, hi_k]` for the running value CONTAINS a target that shrinks to
`≤ u_nL`, driven by the deep condition. This is a single global monotone invariant (no averaging,
no covering radius, no anchored contraction past a crossing — it is a NESTED-INTERVAL argument, not
a walk that re-inflates).

## Skeleton
1. **Reduce to reachability.** By certified R-UV/R-COV', suffices to exhibit a nonempty tree value
   `≤ u_nL`. Boundary layer closed by WTC; work deep `a₁ < L/2 − u_nL/2`. — R-UV + WTC.
2. **Reachable-interval invariant.** For an inclusion order `π` of a chosen subset, let
   `[lo_k, hi_k]` be the tightest interval provably containing the fold value `v_k` from the WTC
   two-sided bound (`lo_k = a₁−P_k` clamped at 0, `hi_k = |a₁−P_k|`). Generalise: track the SET of
   simultaneously-reachable values (skip/include), an interval union whose lower envelope descends.
   — by induction extending WTC's `(I_k)`.
3. **Deep-gap contraction.** The deep condition `L−2a₁ > u_nL` means the whole-tail signed leftover
   `|2a₁−L|` overshoots `u_nL` by an amount `≥ u_nL`; show this overshoot can be absorbed EXACTLY by
   re-including one more piece near the crossing (band-landing BL gives the crossing subset `T` with
   residual `r=|a₁−Σ_T| ∈ [0, a_{k*})`), and that the residual interval NESTS: `r ≤ u_nL` OR the
   remaining pieces below the crossing scale form a strictly smaller sub-instance to which the same
   invariant applies with parameter `n−1` — telescoping via `1/u_n = 2/u_{n-1}+1`. — by BL + IH.
4. **Base + extract.** Base `n=1`; the terminal residual `≤ u_nL` is a tree value ⇒ `D ≤ u_nL`. —
   direct.
5. **Answer.** As in every UPPER approach: matches certified lower bound ⇒ `c(n)=2^n/(2^{n+1}−1)`.

## Key lemmas (claim + mechanism)
- **Two-sided invariant (certified WTC, imported)** — `a₁−P_k ≤ v_k ≤ |a₁−P_k|`; the analytic
  backbone. Its `d≥0` branch is EQUALITY, which is exactly why it is tight and margin-free.
- **Nested residual (GAP)** — after band-landing lands residual `r=Σ_T − a₁ ∈ [0,a_{k*})`, the
  sub-profile `{r} ∪ {pieces below scale k*}` is a valid smaller instance whose own reachable
  interval telescopes; the residual does NOT re-inflate (contrast the R18 dead anchored walk),
  BECAUSE we restart the invariant on a fresh disjoint sub-instance rather than continuing the same
  fold — the re-inflation in R18 came from folding the SAME anchor `a₁` into later pieces; here `a₁`
  is consumed into `r` and never re-touched.
- **Deep-gap absorption** — the overshoot `|2a₁−L| − u_nL ≥ 0` is bounded by the mass of pieces
  below the crossing scale, so one nested restart suffices per scale; `n` scales telescope to `u_nL`
  exactly (VALLEY-TIGHT met by the exact recursion `1/u_n = 2/u_{n-1}+1`).

## Open gaps
- Step 3 nested-residual telescope: prove the restart sub-instance genuinely has parameter `n−1`
  and its target `u_{n-1}·(mass)` composes to `u_nL` — the exact, no-margin heart.
- Confirm the restart is on a DISJOINT support (so residual `r` plus lower pieces never reuse `a₁`
  or the crossing block) — this is the precise property whose absence killed the anchored walk.

## Cases to cover
- Deep interior `a₁ < L/2 − u_nL/2` only. Base `n=1`. Exact-zero even cancellation (helps).

## Watch out for
- **This must NOT collapse to the R18 dead anchored walk.** The distinguishing feature is the
  DISJOINT RESTART after band-landing (a₁ consumed, never re-folded), not "continue the walk past
  the crossing." If the builder finds the restart still re-touches a₁ or re-inflates like the
  covering radius (minpost/u_n growing ~2^{n-1}), this collapses to the 9th dead mechanism — STOP.
- **VALLEY-TIGHT:** the telescope must be exact; any constant-factor residual is dead.
- Whether this is genuinely far from `tree-min-divide-conquer`: it is (analytic interval-nesting on
  a chosen fold vs. counting existence over disjoint blocks) — but both target `min R(A)` and both
  telescope by `1/u_n=2/u_{n-1}+1`, so if BOTH fail their gate the min-R(A) target itself is the
  shared wall and next round must reframe off it. Keep them as the two probes of that target.

## MANDATORY exact-Fraction pre-build gate (run FIRST, n=4,5,6, no floats)
Reuse the `treeVals`/`minR` gate from `tree-min-divide-conquer` for target soundness. Additionally,
for THIS mechanism, compute the band-landing crossing subset `T` (certified BL) and its residual
`r=Σ_T − a₁`, then RESTART: form `{r} ∪ {a_i : scale(a_i) < scale(a_{k*})}` and recursively compute
its `minR`; verify the composed value ≤ u_nL on the hard families (`A^{(n)}` inward-sliver,
`{1/3,13/40,13/40,1/120,1/120}`, `{30,25,20,15,10}/100`). **KILL CRITERION:** if the nested-restart
composed value / u_n grows with n (re-inflation, anchored-walk signature), the invariant does not
close — report and STOP. Use FGR dist-recursion for any μ computation (explorer finding 4).
