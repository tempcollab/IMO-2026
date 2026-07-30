## imo-2026-03 — GAP-U super-balanced residual (Region B: ℓ₁<Σ/2) — numeric gates on the 3 candidate openings

All numerics use an exact recursive ground-truth solver (`/tmp/round-6/rt_search.py`, copy of
`/tmp/round-4/rt_search.py`'s `eval_f`) that computes the TRUE minimal effective total reachable
by Xiang's legal op-sequences (bisect/pin/free-delete) with budget k, given k+1 pieces summing to
Σ=1. This is not an approximate optimizer — it is an exact DP over the (finite, since op count is
bounded) search tree, so ratios reported are exact for the sampled instance. Scripts:
`/tmp/round-6/gate1_mesh.py`, `gate1b_mesh_focus.py`, `gate1c_adversarial.py`, `gate2_induction.py`,
`gate2b_diagnose.py`, `gate2c_pin_include.py`, `gate2d_residual_region.py`, `gate3_concavity.py`.

### Gate 1 — Opening 1 (mesh of reachable residuals)
Built the FULL reachable set `R(pieces,budget)` (not just the min) by exhaustive recursion over
all legal op-sequences up to budget k, allowing early stopping (Xiang need not use all ops).
- **Global/near-threshold mesh is NOT structurally bounded by u_kΣ.** In a window `[0, 2.5·u_kΣ]`
  the worst observed max-gap-between-consecutive-reachable-points was **1.96·u_k** (k=3) and
  **1.24·u_k** (k=4) over only 25 random region-B instances — i.e. gaps *larger* than the target
  threshold routinely occur just outside `[0,u_kΣ]`.
- Restricting strictly to `[0,u_kΣ]` itself, the mesh stayed **just under** u_k in 200 trials
  (worst 0.059 vs u_3=0.0667; worst 0.0276 vs u_4=0.0323) — but this is a much narrower, ad hoc
  fact ("gaps below the threshold happen to be small"), not the kind of *global* mesh bound the
  aimo-0292 template needs to argue "any target window is hit."
- Separately confirmed (not new, but re-verified with my own solver): **0 violations of
  min ≤ u_kΣ** over 200 random + 3000 adversarial (boundary-biased, skewed-Dirichlet) region-B
  trials for k=3,4,5. Worst-found ratio min/u_k: **0.76 (k=3), 0.67 (k=4), 0.52 (k=5)** — confirms
  genuine slack, consistent with R4's 12–28%+ finding (here even more slack found at k=3: ~24%).
- **Verdict: Opening 1 as literally described (bound the mesh, therefore guarantee coverage) DOES
  NOT structurally hold.** The achievable-set structure here (built from ± pin-cancellations and
  discretionary bisect-deletion, not simple increasing-subset sums) lacks the monotonicity property
  (`x_k ≤ prefix + gap`) that makes the aimo-0292 mesh argument work. Only the *specific* minimum
  happens to land close to 0; the mesh technique's generic machinery does not transplant.

### Gate 2 — Opening 2 (induction loading: peel largest / widen IH window / splice)
Tested three variants against the ground-truth solver, restricting last test to the TRUE open
residual (`ℓ₁<Σ/2 AND 2ℓ₂<c(k)Σ`, i.e. excluding the already-proven Case (ii)):

1. **"Exclude ℓ₁" alone** (bisect ℓ₁, 1 op, then TRUE-optimal RT(k−1) on the remaining k pieces,
   k−1 ops): **fails on real instances** — 26/399 (k=2), 4/399 (k=3), 1/399 (k=4) failures (ratio
   up to 1.37 at k=2). Confirms this branch is NOT independently sufficient (matches Opening 4's
   already-known overshoot, now confirmed with exact recursion, not just a crude bound).
2. **"Pin top-2" (merge ℓ₁,ℓ₂ → |ℓ₁−ℓ₂| in 1 op, then TRUE-optimal RT(k−1) on the resulting k
   pieces):** much stronger — **0 failures** across 300 broad-region-B trials each for k=2,3,4
   (worst ratio 0.71–0.95). But restricted to the TRUE residual region (excluding Case ii), a
   **near-miss appears at k=4: 1 failure in 758 instances, ratio 1.039** — i.e. even the exact
   optimal recursion on the remainder is not *quite* always enough after a single pin-top-2 step.
   k=2,3 had 0 failures in their residual subsets (54 and 305 instances respectively).
3. **Critical finding — the PLAIN IH bound fails everywhere.** Substituting the actual induction
   hypothesis bound `u_{k−1}·(remainder total)` (as a real induction must, not the true optimum)
   for step 2 gives **100% failure on the residual region** for k=2,3,4 (54/54, 305/305, 758/758
   instances fail; ratios up to 1.15, 1.37, 1.47). Algebraically: pin-top-2 leaves remainder total
   `Σ−2ℓ₂`, so the naive bound needs `ℓ₂/Σ ≥ c(k)/2` — **exactly Case (ii)'s condition**. So a
   plain one-level "pin-top-2 + IH-bound" induction only re-proves the already-known Case (ii); it
   contributes NOTHING new to the residual. The reason the TRUE-optimal recursion succeeds where
   the naive bound fails must be a genuine structural fact about the remainder after merging
   (e.g. the new largest remaining piece is itself provably large relative to the new total,
   pushing the remainder into its OWN Case (i)/(ii) sub-case) — this is precisely the "widened
   IH / extra parameter" opening 2 calls for, not yet identified explicitly.
- **Verdict: Opening 2 is the most promising of the three, but is NOT a free transplant.** The
  literal aimo-0292 mechanism (average-bound peel + naive widened-bound splice) is REFUTED (point
  3 above, 100% failure). What survives is a specific empirical fact — pin-top-2 + something
  stronger than the raw IH bound works in ~99.9% of the true residual — that still needs a real
  argument for why the remainder's structure improves, plus a fix for the k=4 near-miss (ratio
  1.039; candidates: pin-top-3 as an escape branch, or splice with an explicit second case).

### Gate 3 — Opening 3 (region-restricted concavity/LP)
Ran the same midpoint-concavity check as R2's refuted global test, but restricted to pairs (and
midpoints) both lying strictly in region B (ℓ₁<Σ/2). Result: **37.0% violation rate at k=3
(74/200 pairs), 42.0% at k=4 (84/200 pairs)** — i.e. restricting to region B makes the
non-concavity WORSE, not better, than the already-refuted global 20% (12/60) rate.
- **Verdict: Opening 3 is DEAD.** No LP/KKT/concavity certificate is possible even on this
  narrower affine slice. Do not build; this closes off the one previously-untested opening from R5.

### Ranking for the outliner (builder-readiness)
1. **Opening 2 (pin-top-2 + strengthened/widened IH)** — the only opening with real empirical
   legs: near-zero failure rate (0/1058 broad trials, 1/1117 in the tight residual subset), and a
   sharp, provable reason the naive version is insufficient (100% fail ⟹ literally reduces to
   Case ii algebraically) — this tells the builder exactly what extra structural fact must be
   supplied (why true-optimal-on-remainder beats the naive bound). Ready for a builder, WITH the
   explicit warning: do not submit the literal aimo-0292 average-peel-and-splice as-is (refuted);
   must identify/prove the remainder-improves-after-merge fact, and must separately handle the
   k=4 near-miss instance (ratio 1.039, found at `parts=[0.483,0.168,0.151,0.117,0.081]`,
   `k=4`) — reproduce via `gate2d_residual_region.py`.
2. **Opening 1 (mesh)** — structurally refuted as stated (no global mesh bound below u_kΣ, gaps
   up to 2× u_k just outside the target window). Not ready for a builder in its literal form;
   would need a from-scratch reframing (e.g. a LOCAL pigeonhole near 0 specific to this problem's
   op semantics, not a transplanted generic mesh bound) — deprioritize unless Opening 2 stalls.
3. **Opening 3 (region-restricted concavity)** — DEAD, do not build (worse violation rate than
   the already-refuted global test).
4. **Opening 4 (crude 2-op bisect-top-2 fallback)** — SUPERSEDED: the 1-op pin-top-2 mechanism
   (tested in Gate 2) uses budget more efficiently (1 op vs 2) and empirically outperforms the
   bisect-2 fallback; fold Opening 4 into Opening 2's pin-top-2 as its base construction rather
   than treating it as a separate weaker opening.

### Candidate technique(s)
- Opening 2: pin-top-2 (accumulator-style single pin) as the FIRST reduction step, composed with
  a genuine strengthened IH (not the raw `u_{k−1}·total` bound) — the missing piece is a structural
  claim about the post-merge remainder (candidate: after merging ℓ₁,ℓ₂→|ℓ₁−ℓ₂|, the new largest
  piece relative to the new total provably lands in Case (i) or (ii) recursively, which would
  explain the gap between "true optimal" and "naive bound" empirically found here).

### Knowledge-base entries to use
- `knowledge_base.md` "induction loading / strengthening the hypothesis" (lines ~227–228) — still
  the right generic label for Opening 2, but per Gate 2 point 3, the naive splice literally
  collapses to Case (ii); the outliner must design a genuinely stronger IH statement, not just cite
  the technique name.
- Certified `lemmas/pivot-lemma.md` (closes Case iii-a, Σ/2≤ℓ₁<c(k)Σ) — reusable machinery for the
  "remainder lands in Case i/ii" sub-argument the builder will need for Opening 2.

### Analogous past problems (cruxes)
No update from R5's assessment (aimo-0292 solutions 1 & 2 remain the two live analogies for
Openings 2 and 1 respectively) — but Gate 2 shows the aimo-0292 Solution 1 mechanism does NOT
transplant literally (100% failure of the naive splice bound); it is a starting scaffold only, not
a ready-made proof. aimo-0340 remains refuted (per run_state, do not re-attempt 1-parameter
version).

### Prior progress
Unchanged: RT reduces GAP U to Case (iii); Cases (i), (ii), (iii-a) proven ∀n (Pivot Lemma,
certified). Region B (`ℓ₁<Σ/2`) open. This round adds: exact numeric confirmation of 0 min≤u_kΣ
violations (k=3,4,5, 3000+ adversarial trials); identification of pin-top-2 as a strong empirical
single-step reduction (0/1058 broad failures) with ONE precise near-miss at k=4 to resolve; proof
that the naive "IH-bound" version of any peel-based induction reduces algebraically to Case (ii)
and is NOT new information — the real content must come from the remainder's post-merge structure.

### Dead ends (do not retry)
- Opening 1 (generic mesh-coverage bound) as a top-level proof template — mesh is not globally
  bounded by u_kΣ (up to 2× overshoot just outside the target window); only the ad hoc near-zero
  region happens to be tight, which is not a transplantable mechanism.
- Opening 3 (region-B-restricted concavity/LP) — 37–42% violation rate, worse than the already-
  refuted global 20%. Fully dead, do not revisit at any restriction of region B.
- "Exclude ℓ₁ only" (bisect largest + recurse) as a standalone sufficient mechanism — fails on
  real instances even with TRUE-optimal recursion on the remainder (up to 1.37× overshoot at k=2).
- Plain "pin-top-2 + naive IH bound (u_{k−1}·remainder-total)" — proven algebraically to reduce
  exactly to Case (ii)'s hypothesis (`2ℓ₂≥c(k)Σ`) and FAILS 100% of the time on the true residual
  (all of 54/305/758 tested instances for k=2/3/4); do not let a builder submit this as the closing
  argument — it contributes nothing beyond the already-certified Pivot Lemma / Case (ii).

### Small-case / intuition notes (all numerical/conjectural)
- Region B slack (min/u_k found by adversarial search): k=3 up to 0.76, k=4 up to 0.67, k=5 up to
  0.52 — slack appears to GROW with k (consistent with R4's prior finding), reinforcing that an
  exact tight closed-form match is not needed for region B, only a sufficient bound with comfortable
  margin (favors Opening 2's approach: prove *some* sufficient structural gain, not chase equality).
- The k=4 near-miss (ratio 1.039, essentially borderline) suggests the true worst-case in the
  TRUE residual region may sit very close to u_kΣ for k=4 specifically after a single pin-top-2 —
  worth having the builder explicitly search near
  `parts≈[0.483,0.168,0.151,0.117,0.081]` (k=4) with a local optimizer (Nelder-Mead) to see if a
  strictly worse instance exists (i.e. is single pin-top-2 truly insufficient at k=4, requiring a
  genuine second branch, or is 1.039 the actual supremum and a slightly different single-step
  reduction closes it)? This is the one loose thread before committing fully to Opening 2's
  single-pin-top-2 base step.
