# Build report — breakpoint-vertex (UPPER), round 13

**Status: partial. The mandated exact-fraction gate FAILED; no fake proof shipped (per directive).**

## What I was asked to build
Advance the first-gap pigeonhole `μ_{n+1} = min_i dist(a_i, R_{i-1}) ≤ u_n` via the seeded strong
induction **SEED(p)** + **mass-telescope discrepancy (GAP-TELE)** that charges "far" pieces against
`Σa_i = L` and both caps `a_1<L/2`, `a_2<β_nL`. Mandatory: run the exact-fraction numeric gate on the
SEED(p) scaling and the GAP-TELE constant BEFORE prose; if it fails, report honestly and stop.

## Gate outcome: BOTH steps refuted (exact fractions)

**Residual reconciliation (cleared a definitional red herring first).** The certified target is
`min_{∅≠T} descKK(T) ≤ u_n` — the min over *nonempty* subsets of the descending-KK caterpillar value,
where value `0` (nonempty even cancellation) is admissible; only `T=∅` is excluded. With this correct
reading: 0 exact fails, worst ratio 0.75, tight at the dyadic ladder — matching the reported claim. (An
initial `min positive reachable value` reading spuriously "failed" 128/442 at n=3 because it wrongly
discards the admissible 0. Cleared.)

**GATE 1 — SEED(p) scaling: REFUTED.** Descending fold-from-seed `r` over pieces `b_1≥…≥b_p`, target
`≤ u_p·M` (`M=r+Σb`):
- seed domination `r≤b_1` only: worst ratio 2.24/4.21/6.20/8.17/9.77 at p=2..6.
- + valley caps inherited on the combined (p+1)-instance: still fails, 1.67/3.44/4.85/7.47 at p=3..6.
- reverse domination `r≥` all pieces: 7.5/15.5/31.5/63.5 at p=3..6.
Worst overshoot GROWS with p in every parametrization ⇒ `u_p·M` is not an inductively stable threshold;
the seed-domination invariant that would make SEED(p−2) a legal IH does not exist. (Exactly the reviewer's
flagged "12 rounds failed on this parametrization," now a concrete refutation.)

**GATE 2 — GAP-TELE: STRUCTURALLY IMPOSSIBLE.** Charging `n+1` far pieces against `Σa_i=1` cannot work:
1. `(n+1)u_n = (n+1)/(2^{n+1}-1) → 0` (0.43 at n=2 down to 0.01 at n=9): the far-pieces reservoir is
   exponentially too small — linearly many pieces, an exponentially small threshold.
2. The distance-sum is provably bounded **above** by `<1`, the WRONG direction:
   `dist(a_i,R_{i-1}) ≤ a_1·2^{-(i-1)}` (covering radius halves per reflection) ⇒
   `Σ_i dist(a_i,R_{i-1}) ≤ a_1(2-2^{-n}) < 2a_1 < 1`. Exact-fraction check confirms the constant
   `2-2^{-n}` is tight (1.75, 1.875, 1.9375, 1.96875, … for n=2..5).
So GAP-TELE cannot force `Σa_i>L`. Dead at the structural level, not a loose constant.

## Deliverables recorded in the approach file
- Honest refutation of SEED(p) + GAP-TELE, written into Status / Approaches tried / Current best.
- New certifiable structural fact **Lemma DSUM**: `Σ_i dist(a_i,R_{i-1}) ≤ a_1(2-2^{-n}) < 2a_1`, a
  clean NO-GO that certifies no per-piece mass-charging lever can ever reach the total mass.
- Residual definition corrected/clarified: `min_{∅≠T} descKK(T) ≤ u_n` (0 admissible).

## Signal for the orchestrator
The mass-telescope-discrepancy lever is the FIFTH exhausted upper-wall family (joining covering-radius
R10/R12, density/COUNT R11, greedy recursion R9, bounded-depth escape R10). Both this round's proposed
levers on the upper wall are now refuted by gate. Per the outline-reviewer's own diversity note, this is
the escalation trigger: put ≥1 explorer on a **potential-free / LP-duality extremal re-derivation of the
minimax attacking both walls at once**, rather than a sixth variant on the reachable-set object. The
honest open crux (`min_{∅≠T} descKK(T) ≤ u_n`, true and tight at the dyadic ladder) is unchanged.

## Files
- results/imo-2026-03/approaches/breakpoint-vertex.md (updated: Status, Approaches tried, Current best,
  Promotable lemmas — Lemma DSUM added).
