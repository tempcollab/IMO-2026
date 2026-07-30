# Build report — breakpoint-vertex (UPPER wall), round 12

**Slug:** breakpoint-vertex — imo-2026-03 upper bound, balanced valley.
**Status:** partial (unchanged solve state; mechanism GATE FAILED, honest negative + two new proven lemmas).

## Mandated gate result: GAP TWO-CAP is REFUTED

I ran the mandated numeric gate FIRST, before any prose (exact rationals, valley profiles n=3..7).
The proposed two-cap covering-radius contraction toward u_n **does not exist**:

- Covering radius `c_i = ½·max-gap(R_i)` over `[0,a_1]`: `max-gap/u_n` worst = 3.24 / 6.12 / 8.94 /
  15.76 / 24.63 (n=3..7), fails 96–100%. Level-by-level it contracts geometrically but **saturates at
  ≈3–5·u_n** and never reaches u_n — the exact R10 saturation, NOT removed by the second cap `a_i<β_n`.
- Windowed `sup_{[0,β_n]} dist(·,R_n) ≤ u_n`: fails 37–100% (worst 1.85×–19.46×).
- Exact-point `dist(a_{n+1},R_n) ≤ u_n`: fails a few % (worst 1.39×–2.59×).

Per the directive ("If it fails, report honestly rather than shipping a fake proof"), I did not write a
covering-radius proof. Recorded the refutation to prune the covering-radius family (R10 one-cap + R12
two-cap) permanently.

## Root cause identified (rigorous)

The true target is the **first gap** `μ_{n+1} = min{v>0 : v∈R_{n+1}}` ≤ u_n, which holds robustly
(0 fails, worst 0.70; tiny ~5e-4·u_n on near-all-equal exact profiles; TIGHT `=u_n` at the dyadic
boundary `a_i=2^{n+1-i}/(2^{n+1}-1)`, verified n=2..6). The first gap is FAR below the max gap (reachable
set is dense near 0, sparse near a_1), so a worst-gap covering radius is incomparable to it and can never
certify it. This is precisely why every covering-radius variant saturates.

## Rigorous positive deliverables (proven in full, §4B.8)

1. **First-gap recursion (Lemma FGR):** `μ_i = min(μ_{i-1}, dist(a_i,R_{i-1}))`, hence
   `μ_{n+1} = min_i dist(a_i, R_{i-1})`. The residual is thus the **first-gap pigeonhole**: some a_i
   approaches R_{i-1} within u_n. Global + adaptive; no single level i works (verified), so no per-level
   covering surrogate can exist — matches the gate failure structurally.
2. **Reduction R-COV' (T=∅-safe):** upper bound in valley ⟺ μ_{n+1} ≤ u_n, with the T=∅ exclusion
   handled exactly (nonempty T = n cuts via ESF-2; ∅ = n+1 cuts, infeasible; produced value is always a
   nonempty-T leftover). This fixes the explorer's naive-inclusion bug (which falsely gave min=0 on 100%).

Both are certifiable this round (listed under Promotable lemmas).

## Directive compliance

- Numeric gate FIRST: done; decisive failure reported honestly. ✅
- T=∅ exclusion handled explicitly in the conversion. ✅
- Did NOT lean on forced collisions / exact-0 as a mechanism (the 0-value is folded in only as the
  even-cancellation boundary case inside R-COV'). ✅
- Did NOT reuse dead upper families (dispersion/density/COUNT, fixed-depth moves). The covering-radius
  family is now added to the dead list with a rigorous negative. ✅

## Spec concerns / routing recommendation

- **The covering-radius framing (the defining mechanism of this slug's R9–R12 arc) is now exhausted.**
  Both one-cap (R10) and two-cap (R12) are refuted with the same saturation cause. Recommend RETHINK for
  the *mechanism*: the residual GAP U-first-gap is correctly stated but needs a genuinely different lever
  — a discrepancy/pigeonhole on the coupled sequence (a_i, R_{i-1}), e.g. an Abel/telescope identity on
  the sorted subset-value multiset M_{n+1} pairing values whose *difference* is reachable (the RL
  tree-realizability being the obstruction to a naive pigeonhole). Not a covering radius, not a fixed
  level.
- The two new lemmas (FGR, R-COV') are clean and reusable and give the upper wall its sharpest, correct
  reduction — worth certifying regardless of the mechanism pivot.

## Verdict suggestion
CHANGES REQUESTED (partial; real reduction progress + rigorous negative, gap remains) — but flag that the
covering-radius vehicle itself should be retired and the first-gap pigeonhole handed to the outliner for a
new mechanism next round.
