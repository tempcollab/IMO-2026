## imo-2026-03 — LENS: the b-lift after single-cut descent's death

### Summary verdict up front
The peel §11.5 proposal ("adopt (WM) as a LOADED IH for general F', close via peel-inheritance")
is **numerically REFUTED as literally stated**: full weak-majorization (WM), and even the much
weaker "majorize only at dyadic-rung-boundary thresholds" version of (HLP), are FALSE for general
(non-ladder) F'. Only the exact TOTAL identity (★-id)/(FLOOR) generalizes to arbitrary F' — and
that generalization is a tautological restatement of the whole theorem (D̃(F)≥1 ⟺ Σ_{F'-odd} ≥
Σ_{π_0-even}), giving zero new leverage. So (WM) as proposed does **not** subsume the b-lift; it
cannot even survive as a stated hypothesis off the ladder. This is a clean, useful negative for
the outliner: retire (WM)-as-loaded-IH, but keep looking for a *different* invariant that (a) is
true for general F', (b) is strictly weaker than the target itself, and (c) is provably inherited
under one peel.

### Distinct openings
1. **Diagnose why (WM) fails off the ladder, and mine the failure for the missing ingredient.**
   The concrete n=2 counterexample below shows the failure mode precisely: prefix-1 majorization
   fails (top BO value 1.3292 < top RE value 1.9836) while the FULL sum (★) still holds (BO sum
   2.0 ≥ RE sum 1.9836). This says the ladder's special property (DOM: each rung strictly exceeds
   the sum of every lower rung, §11.3) is doing real, load-bearing work that the loose "top-k
   prefix" majorization overclaims once F' is not the ladder — general F' has NO such per-part
   dominance (a split rung's individual parts can be small). A candidate opening: replace (WM)'s
   value-sorted prefix with a **π_0-indexed** or **rank-indexed** partial-sum invariant that only
   claims dominance at the SPECIFIC breakpoints forced by π_0's own even-rank positions (not every
   k, and not every dyadic rung boundary — both refuted below), i.e. a charge tailored exactly to
   §10.6/§11.4's rank-parity formula rather than a blind HLP family.
2. **Multi-cut / global re-choice b-lift (untried, and NOT the same as the refuted single-cut
   move).** coupled-cut-descent's Prop REFUTE only rules out ONE move class: a single within-scale
   `F'`-merge + a completely free repartition of `π_0` into `a_0+2` parts. It explicitly verified
   (its own §"why the whole b-descent framing is a mirage") that a config *does* exist in the
   target slice with `D̃(F*)≤D̃(F)` — reachability isn't the obstacle, *locality* of the move is.
   A genuinely different framing: a **specific, structured** multi-cut move (e.g. simultaneously
   re-cutting ALL scales of F' back toward the ladder shape while co-moving π_0 along a matched
   schedule, rather than one arbitrary repartition) might be provable as non-increasing even though
   an unrestricted single-cut move is not. This is speculative and should be scoped carefully
   before committing a slug (the coupled-cut-descent post-mortem already flags this direction as
   "not obviously simpler than the theorem" — treat as a stretch opening, not a safe bet).
3. **Direct structural induction on n via the peel, but WITHOUT a majorization-shaped loaded IH —
   use (POS)/(Q) layer bookkeeping instead.** `positive-layer-localization.md` already bounds the
   positive layers `P ≤ Σ_{k≤K0} y_{2k}` purely from π_0. The missing half `Q ≥ P` is about `F''`s
   negative layers, i.e. about `N_{F'}` alone (no dependence on π_0's fine shape beyond its even
   parts). A genuinely different loaded IH: carry a NUMERIC bound on `Q` (not a majorization
   relation) as the induction hypothesis on `F'`, e.g. `Q(F') ≥ (something explicit in a_0, the
   y_{2k})`, and show it's inherited when peeling `F' = π_1 ⊎ F''` — this sidesteps majorization
   entirely and stays inside the already-certified (POS) machinery, closer to home.
4. **Global exchange/smoothing to the certified tie family (genuinely far framing, not induction on
   n or b at all).** Since the tie set `{D̃=1}` is exactly known and small — the `n+1` "ladder with
   one unit bumped onto a rung (or appended)" configs (banked round-12 memory rule 36) — a
   Karamata/aimo-0146-style smoothing argument could show every feasible `(π_0,F')` can be pushed,
   by a sequence of feasibility-preserving moves that are `D̃`-non-increasing, to one of these `n+1`
   points, without induction on `n` or `b` as separate variables. CAUTION: R11 rule 34 already
   proved the **π_0-fixed** single-move version of this is FALSE (~30% of trials raise `I_n`), and
   coupled-cut-descent's Prop REFUTE shows the natural **co-varying single-cut** version is also
   FALSE at n=5. So a smoothing move here would need to be genuinely global (not local single-cut)
   — same caution as opening 2. Worth flagging as an orthogonal target for the outliner, but do not
   under-scope it as "just redo coupled-cut-descent with a different repartition rule."

### Candidate technique(s)
- Charge/dominance argument tailored to π_0's rank-parity structure (§10.6/§11.4 machinery),
  generalized scale-by-scale rather than via blind majorization.
- (POS)/(Q) layer bookkeeping as the loaded IH object (numeric bound, not majorization relation).
- Karamata-style smoothing to the explicit tie family, IF a genuinely global (not single-cut) move
  can be found — high risk, flagged speculative.

### Cheap-kill candidates
- None new beyond what's banked. The obvious cheap kills (scalar b-cutoff, π_0-fixed monovariant,
  single within-scale-merge coupled move, full/threshold-restricted majorization) are now ALL
  refuted (see Dead ends). Before committing new machinery, cheaply test any proposed invariant on
  the SAME n=2 counterexample below (2 lines of Fraction arithmetic) — it already breaks WM and the
  dyadic-breakpoint HLP relaxation, so it's a fast filter for future candidate invariants.

### Knowledge-base entries to use
- `lemmas/floor-half-reduction.md` (FLOOR identity, fully general in F', already imported).
- `lemmas/ladder-interleaving-identity.md` (★-id, ALSO fully general in F' — its proof only used
  `Σπ_0−ΣF'=1`, true for every feasible F', not just the ladder; this generality was already
  correctly noted in §11.5 but conflated with (WM) generalizing too, which it does not).
- `lemmas/positive-layer-localization.md` ((POS): `P ≤ Σ_{k≤K0} y_{2k}`, π_0-only, still the
  cleanest half-result; opening 3 tries to build its missing partner directly instead of via WM).
- knowledge_base.md's majorization/HLP and exchange-argument entries (generic technique pointers,
  not specific to this problem) — worth a fresh read for a formal HLP inheritance lemma template if
  opening 1 is pursued (does majorization admit a natural "peel-one-scale" inheritance theorem in
  the literature that could be adapted to a restricted breakpoint set rather than all k?).

### Analogous past problems (cruxes)
- Already banked in `/tmp/memory/math-explorer.md` (round 12): **aimo-0146** ("smooth a sorted
  weighted sum to a few extremal profiles") as the template for opening 4's exchange target, and
  **aimo-0388** (coin 50-50 split, alternating signed sum over sorted merge, parity forces
  `|diff|≥1`) as a structurally analogous "baby-P3" for the Abel/pairing route underlying (★-id).
  I did not find further new analogues this round beyond what's already banked; did not re-query
  the corpus exhaustively given the time budget — the prior rounds' crux search on this exact wall
  (rounds 4–12) has been thorough and these two remain the best matches.

### Prior progress
- FLOOR + (★-id) fully reduce Case B to one scalar inequality `I_n≤0`, both identities GENERAL in
  F' (not ladder-specific) — this was already true before this round, just under-exploited.
- Base slice (b=0, F'=L): GAP-P1′-a open (cross-block tail-cancellation charge for the ladder only,
  via (DOM)); (WM) proven TRUE there (0/1.8e5 + 280k fractional, `n≤8`) — this remains a valid,
  live, closed-domain claim; only its GENERALIZATION to arbitrary F' is refuted this round.
- GAP-P1′-b (b-lift): single-cut coupled descent REFUTED rigorously at n=5 (Prop REFUTE, R12); (WM)
  proposed as a unifying loaded IH — REFUTED this round (numerically, both full-WM and the weaker
  dyadic-breakpoint HLP fail for general F').

### Dead ends (do not retry)
- **(WM) generalized to arbitrary F' as the loaded IH (§11.5's proposal, literally as stated):
  REFUTED this round.** Concrete witness (`n=2`): `π_0={4959/2500, 5041/2500}` (partition of `4`),
  `F'={3323/2500, 1677/2500, 1}` (rung `2^1` split into `{3323/2500,1677/2500}`, rung `2^0={1}`
  uncut). Descending merge: `2.0164(R), 1.9836(R), 1.3292(B), 1.0(B), 0.6708(B)`. `BO =
  {1.3292, 0.6708}` (sum `2.0`), `RE = {1.9836}`. Prefix-`1` majorization FAILS: top-`BO`
  `1.3292 < 1.9836` top-`RE`, even though the FULL sum `2.0 ≥ 1.9836` holds ((★) itself is fine —
  it's equivalent to the true theorem `D̃≥1`, verified `0/24000` separately). Scaled probe: `477`
  WM failures / `12000` random feasible `(π_0,F')` trials, `n=2..5`, both tie-break conventions.
  **Even the weaker relaxation — majorization tested only at the `n` dyadic rung-boundary
  thresholds `t=1,2,4,…,2^{n−1}` instead of every prefix — also FAILS**: `1321` failures / `60000`
  trials, `n=2..6`. So NO threshold-family strictly between "total sum" and "every prefix" that I
  tested survives generalization off the ladder. Do not re-seed (WM) or any HLP-threshold variant
  as a general-F' invariant; it is a ladder-only fact (proven true there, false elsewhere).
- Single-cut coupled b-descent (all variants: `π_0`-fixed merge, co-varying merge+repartition,
  broadened repartition to `a_0+1`-or-`a_0+2` parts): REFUTED R11/R12 (see run_state Rules 30, 33,
  34 and coupled-cut-descent.md Prop REFUTE, explicit `n=5` witness `π_0={16,16}`, `D̃(F)=3` but
  best-reachable `D̃(F*)=5`).
- Scalar b-cutoff / φ(b) pruning: DEAD (R11, exact ties at b=2,3).
- GAP-IMR integer-minimizer / TU framing: DEAD (R9–R10, proven equivalent-to-or-stronger-than
  target; cross-scale mass transfer blocked by hard scale sums).

### Small-case / intuition notes (conjectural / numeric evidence only)
- The n=2 counterexample above is a genuine, minimal, hand-verifiable witness that majorization
  (in the strong "every prefix" or even "every dyadic threshold" sense) is not the right structural
  invariant once F' departs from the ladder — the ladder's per-rung dominance (DOM) is doing
  irreplaceable work, and no simple relaxation of it survives naively. This strongly suggests
  (opening 3) that whatever DOES generalize must reference π_0's rank/parity structure directly
  (as in §10.6/§11.4's tail-charge), not a value-sorted threshold family — i.e. the correct loaded
  invariant is likely *rank-aware*, not *value-aware*.
- All `24000` general `(π_0,F')` trials (both integer and fractional, `n≤6`) confirm `D̃≥1` with
  `min=1` exactly — the theorem itself remains numerically airtight; only the proposed proof
  mechanism (WM) is wrong, not the target.
