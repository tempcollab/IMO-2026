# Outline review — Round 10 — imo-2026-03

Sole open wall: GAP L (lower bound, Case B) = prove `D̃(F) ≥ 1` for every real feasible
refinement. UB certified/closed, not reopened. Three approaches proposed; all screened
against the run's recorded dead ends (per-group rounding, TU/integral-vertex,
two-level-peel-alone, parity-through-peel, all merged-order/measure/sequential/genfn framings).
No proposal repeats a refuted line; the one refuted synergy (Parity-Lemma-through-peel) was
correctly NOT seeded. Certified block-contribution formula independently re-verified
(0 mismatches on 20k random exact-Fraction multisets), so the smoothing slope reasoning in
approach 2 rests on solid ground.

---

## 1. peel-scale-rank-induction — revise/advance — APPROVE
Route: direct real-valued strong induction (peel top scale), close near-balance residual
`{|D̃(π_0)−D̃(F')|<1}` with a LOADED coupled multi-scale IH (aimo-0377-shape co-induction of
a pair `(P1: D̃(F')≥1, P2: overlap-cap)` indexed by the per-scale cut vector).

- Technique is sound and olympiad-standard (loaded/coupled induction), and is NOT in any
  refuted family. This is the only route that proves the real-valued bound directly, with no
  detour through integrality — the most solution-shaped line in the field (imr explorer:
  induction/peel is the olympiad route; GAP-IMR is unusually LP-flavored, no corpus support).
- Refuted-line hygiene is correct: the outline explicitly BANS resubmitting opening-2
  (force `a_1=0` / two-level-peel alone) — the p1 explorer's exact-Fraction cheap-kill showed
  the residual only shrinks 89%→89%, no collapse. It also bans any `P2` derivable from a static
  merged-order profile of the final multiset (R8-dead) — `P2` must read `F'`'s recursive cut
  origin. Both bans are load-bearing; keep them.
- Genuine open gap (not fatal, this is an advance-with-gap): the exact `P2` is NOT yet pinned.
  The mechanism IS stated (peeling `F'=π_0'⊎F''` reproduces the SAME (PEEL) identity one scale
  down, so `P2` at level `n` inherits from `(P1,P2)` at level `n−1`, as aimo-0377's `f(3i)`
  follows from the shifted triple) — a real mechanism, not a bare label. Builder MUST: state `P2`
  explicitly and verify (i) inheritance under peel and (ii) sufficiency (forces
  `2λ(O_{π_0}∩O_{F'}) ≤ D̃(π_0)+D̃(F')−1`) with an exact-`Fraction` probe on genuine dyadic
  refinements BEFORE writing algebra. Circularity guard: `P2` must be strictly stronger than
  `D̃(F')≥0` yet not equal the target itself — flag this in the build.

## 2. vertex-integrality-parity — revise/advance — APPROVE
Route: GAP-IMR via order-aware minimality smoothing at the GLOBAL optimum (kb piecewise-concavity
smoothing / exchange) — kill odd fractional tie-blocks ⇒ integer minimizer ⇒ Parity Lemma ⇒ `≥1`.

- Correctly replaces the R9-refuted independent per-group rounding (7847/18900 violations) and
  does NOT reassert per-cell TU / integral vertices (refuted R9). The argument is explicitly
  global-minimality-driven, not cell-geometry — the right diagnosis.
- Mechanism is concrete and rests on the certified §3.2 block-contribution formula (re-verified
  here): even tie-blocks contribute 0, only ODD fractional blocks obstruct; perturb `v→v±ε` with
  joint order-aware compensation into an adjacent even/free block of the SAME group (keeps every
  group-sum fixed AND the merged order — the exact failure mode of the naive version). `D̃` is
  then affine in `ε` with slope ±1 from the odd block; minimality blocks the decreasing direction
  ⇒ collision at ε=0 ⇒ fractionality monovariant `Φ` strictly drops with `D̃` non-increasing.
- Non-circular: references only "is `v*` integer," never the value `1`. Good.
- Genuine open gap (advance-with-gap): builder must (i) prove an adjacent same-group companion
  block always exists to absorb the compensating mass (else route through the group's other
  parts), and (ii) prove the collision at a true minimizer strictly reduces `Φ` while `D̃` is
  non-increasing — the descent's load-bearing step. Do this with an exact-Fraction probe first;
  a single `D̃`-increase kills the scheme (this is how per-group rounding died in minutes).
  Do NOT reintroduce cross-group order inversion.

## 3. peel-integral-exchange — NEW (copy-of vertex-integrality-parity) — APPROVE
Route: SAME target (GAP-IMR ⇒ Parity Lemma) but a genuinely DIFFERENT tool — the certified peel
SD/(PEEL)/(DIFF) identity as a CROSS-SCALE integral-rounding engine on a global minimizer
(round scale-by-scale, `D̃` non-increasing, terminate at an integer config).

- This is EXACTLY the cross explorer's one endorsed synergy ("retarget the certified peel identity
  as the cross-block mass-transfer tool GAP-IMR's §3.3 needs"), and is explicitly DISTINCT from
  the refuted, circular "push the Parity Lemma directly through the peel step" — which the cross
  explorer proved circular and the outliner correctly did NOT seed. This approach uses the peel
  identity as an EXCHANGE tool for GAP-IMR, not as an induction finisher, so the circularity does
  not apply.
- Diverges from its twin on a real axis: within-group same-value smoothing (twin) vs cross-scale
  mass transfer (this). The §3.2 obstruction (`n_g·v∉ℤ`) has two halves — mass within a scale vs
  spanning scales — and the two approaches attack different halves, so they will not die together.
  Copy justified; twin inherits Elo/counts, they diverge on outcome.
- Genuine open gap: step-2 choice of `π_0^Z` with BOTH monotonicities (`λ(O_{π_0}∩O_{F'})` not
  decreasing, `D̃(π_0)` not increasing), and that scale-recursive rounding terminates integer with
  `D̃` never increasing — the scale-spanning tie-block is the crux. Builder MUST verify numerically
  on the documented witnesses (`n=4` Y=(8,3,3,2) Z=(8,2,2,2,1), fractional cell `(4,2,½,½)`) with
  exact `Fraction` BEFORE algebra. Watch: if the builder ends up moving mass only within a scale it
  collapses into the twin — keep the cross-scale exchange the load-bearing step.

---

## Field diversity note (for the orchestrator)
The plateau broke in R9; the field is now three concrete cruxes, but 2 of 3
(vertex-integrality-parity, peel-integral-exchange) route through the SAME reduction target
(GAP-IMR) and the SAME finishing device (Parity Lemma). They are legitimately distinct
MECHANISMS to reach GAP-IMR (within-group smoothing vs cross-scale peel exchange) — an approved
branch, not a single-gap trap — but they share the risk that GAP-IMR is unreachable by any
mass-transfer. peel-scale-rank-induction is the ONLY route independent of integrality (proves the
real-valued bound directly). WATCH: if all three stall in R11, do NOT add a fourth GAP-IMR
variant — seed the reserved far framing that avoids the odd-total-parity route entirely
(2-adic valuation split `N=N_++N_-`, crux aimo-0917; or the canonical-minimizer monovariant
descent to `{2^{n−1},…,3,2,1,1}` the outliner reserved).

## Ranking (folded this round; stale flags on both R9 advances cleared)
peel-scale-rank-induction 1595 (live LB leader, olympiad-shape route) > induction-recursion-telescope
1580 (parked machinery, framing R8-exhausted) > vertex-integrality-parity 1546 (advance) >
peel-integral-exchange 1540 (new, twin of vertex-parity) > even-rank-doublecount 1438 (RETHINK) >
cut-sequence-potential 1427 (dead-end) > induction-recursion 1380 (dead) > potential-certificate 1337
(retired). dyadic-discrepancy 1673 & dyadic-discrepancy-euclid 1552 untouched (parked UB reference,
verified-milestone — not on the open wall). Build set below is the strongest LIVE slugs on GAP L,
not the top Elo (the top-Elo pair is parked UB work).

build set: peel-scale-rank-induction, vertex-integrality-parity, peel-integral-exchange
