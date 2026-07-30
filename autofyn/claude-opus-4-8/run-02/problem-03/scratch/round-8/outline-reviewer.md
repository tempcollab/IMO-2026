# Outline review — imo-2026-03 (Round 8)

Sole open wall: GAP L (lower-bound Case B), certified-reduced to the NON-STRICT bounded-mass
count-parity inequality (△⋆) `λ_{(0,θ)}{M odd} ≥ 1−β` ⇔ (♠≥0) ⇔ self-contained `E(F) ≤ 2^n−1`.
Upper bound is DONE (certified, not touched). No approach reviewed here targets the upper bound.

Independent check I ran: brute-forced the self-contained target `E(F) ≤ 2^n−1` over ALL integer
refinements of the dyadic weights {2^0,…,2^n} with split budget Σa_j ≤ n, for n=2,3,4
(7 / 62 / 1497 configs). Result: 0 violations, maxE = 2^n−1 exactly (tight). The shared target of
approaches A and C is correct and tight — the wall is a MISSING MECHANISM, not a false claim.

---

## induction-recursion-telescope (A) — advance — CHANGES REQUESTED

Technique sound. Builds only on certified machinery ((♦) `D̃−1=Σψ(c_i)Δw_i`, ψ(c)=1[c odd]−c with
ψ≥0 ⇔ c≤1 — verified the sign table by hand; Structure Lemma; Lemma T closing maxc≤1). The NEW
mechanism (greedy bounded-window nonnegative-block TILING, crux aimo-0626) is a genuine many-to-one
NET block-sum domination, explicitly NOT the refuted 1-1 value/width injection (§10) — the
distinction is real and correctly stated. Does not resurrect any refuted route (scalar summary,
top-down reserve, budget-count are all avoided; compensation kept global/bottom-inclusive).

- Load-bearing gap (Steps 3–4, correctly flagged as the ONE hard step): proving a valid
  nonneg-block tiling ALWAYS exists, with (i) a two-sided/budget-bounded window and (ii) the
  budget bound Σa_j≤n capping excursion tokens. Both sub-claims have a stated mechanism
  (excursion-token charging to the split budget via Structure Lemma §5; net-block domination
  surviving §10). Acceptable as an explicit gap for a build.
- Direction trap is correctly internalized: the probe shows one-directional left→right greedy
  fails on slack witness W3 (surplus precedes deficit). The builder MUST deliver a two-sided /
  budget-bounded window, not a one-pass greedy — this is the make-or-break of Step 3. Do not let
  the build quietly assume a single-direction tiling.
- Watch: the "budget-bounded window length" claim (a T-run to c=k charges k−1 tokens, ≤n total)
  is the load-bearing quantitative lemma. It must be proved, not asserted — bound the window
  length a priori before claiming the tiling terminates with nonneg blocks.

This is the leader on the wall and owns the certified machinery. Build it.

## cut-sequence-potential (B) — new — CHANGES REQUESTED (build with early-RETHINK flag)

Register + build. Genuinely different framing per the plateau rule: an amortized monovariant over
Xiang's ORDERED cut sequence using the EXACT Cut-Flip toggle-set geometry (certified), structurally
orthogonal to the merged-order/fragment-origin machinery. Explorer (bypass-strategy opening 2,
aimo-0019) supports the proof-shape. Steps 1–3 rest on certified facts (base D̃(F_0)=(2^{n+1}+(−1)^n)/3
≥1 by exact geometric alt-sum; per-cut ΔD̃ = ±2·exact toggled measure, |ΔD̃|≤2min(x,L−x)).

- Load-bearing gap (Step 4, the whole content): CONSTRUCTING the reserve r_k so Φ_k = D̃−1−r_k is
  monovariant with r_0=D̃(F_0)−1 and r→0 at the tie extremum. Mechanism stated (charge each cut's
  drop against reserve released by the SAME cut, via the exact toggle set — not the summed-magnitude
  bound).
- CRITICAL guardrail: a crude Σ|ΔD̃|≤2Σmin(x,L−x) bound is REFUTED (it is the dead budget-count;
  D̃ can legitimately fall all the way to 1). The reserve MUST use the exact toggle-set geometry
  cut-by-cut. Per the outliner's own note and my role rule: if after ONE build the reserve cannot
  be made monovariant without collapsing to a summed-magnitude budget-count, this slug is RETHINK
  (that would confirm the whole sequential-count family is dead). Flag early — do not grind a
  second round on a collapsed reserve.

## even-rank-doublecount (C) — new — CHANGES REQUESTED (build behind the n≤3 cheap-kill gate)

Register + build, but the cheap-kill runs FIRST. Genuinely different framing: pure combinatorial
double-count / bivariate generating function on the self-contained `E(F)≤2^n−1`, no game / no
cutting / no measure language (bypass-strategy opening 4; genfn-dyadic opening 3). Step 1 (the §9
equivalence) is certified; I independently confirmed the target holds and is tight.

- Load-bearing gap (Steps 2–3): the scale-graded even-rank identity/bound. The stated mechanism is
  a per-scale defect controlled by a_j with Σa_j≤n forcing the total ≤0, read via a roots-of-unity
  filter at x=−1 plus a SECOND grading variable q marking dyadic scale.
- MANDATORY gate, before any prose: the "(♣) not pointwise" obstruction (1[M odd]≤M fails
  pointwise, only after integration) will kill any SINGLE-variable coefficient argument — the
  second (scale) grading must be genuinely load-bearing. Per the outliner's cheap-kill: hand/sympy
  compute the n=2 and n=3 bivariate genfn on the worked examples (§4,§6); if no clean identity
  falls out in ~30 min, DOWNGRADE this slug rather than invest a full build. This is the most
  speculative of the three — the gate is not optional.
- Do NOT reintroduce a scalar summary of Z (refuted); the scale grading must keep each scale's parts.

## induction-recursion — RETIRE (do not build) — RETHINK stands

Budget-count route (O_B≥E_A termwise, |A_2j|≤|B_2j−1|) is REFUTED with an explicit witness (R7);
its sequential intent is now carried in a genuinely different (amortized, exact-toggle) form by
cut-sequence-potential. Keep the file as a recorded dead end; dispatch no builder. Correctly
ranked as `dead-end`.

---

## Field / diversity assessment

Three framings, well separated: A = merged-order block-decomposition (measure/tiling), B =
ordered-cut amortized monovariant (sequential, orthogonal to merged-order), C = static
double-count/generating-function (no measure). Per the plateau rule (GAP L is the wall R3–R7),
the field retains ≥1 genuinely different framing from the plateaued merged-order machinery — in
fact TWO (B and C). Good.

One honesty note for the orchestrator (role rule): A and C, though mechanistically far apart,
share the SAME target inequality `E(F)≤2^n−1`. That is acceptable here only because the target is
proven-true and tight (my brute check + certified §9 equivalence) — the diversity we need is in
MECHANISM (which A/B/C have), not in the target. B is the sole slug on a genuinely different object
(sequential D̃ over cuts, never routing through E(F)≤2^n−1). If BOTH A and C stall on their
mechanism next round while B collapses to budget-count, that is the signal to escalate to a fourth
framing that does not go through the merged-order reduction OR the static inequality at all.

Ranking (post-update, Elo): dyadic-discrepancy 1656 and dyadic-discrepancy-euclid 1540 lead on the
verified UB milestone but are PARKED (UB reference — do not rebuild); among the live GAP-L field,
induction-recursion-telescope 1538 leads, cut-sequence-potential 1526, even-rank-doublecount 1495,
with induction-recursion 1444 (dead-end) and potential-certificate 1360 (retired) at the floor. The
build set is the three live GAP-L slugs (the top-Elo pair are terminal for their purpose).

build set: induction-recursion-telescope, cut-sequence-potential, even-rank-doublecount
