## imo-2026-03 — alt-framing lens (round 3)

Scouting genuinely different framings (NO proof attempted). All numerics below are
evidence/conjecture, not proof. Unnormalized units (total = D_n = 2^{n+1}-1) throughout
unless "frac" is written; target D=1 (unnormalized) ⟺ Liu fraction v_n = 2^n/D_n.

## Terrain (what the current framings share / where they hit walls)

The three live approaches — `tail-count` (PL/variational via the D-parity integral),
`tower-induction` (block-contribution / frontier recursion), `majorization-upper`
(exchange/pairing for the upper bound) — all converge on the *same two objects*:

- **Lower bound object:** D := ∫(N(t) mod 2) dt = 2·(Liu's odd-index) − total
  (= parity integral / layer-cake). Proving Liu ≥ v_n ⟺ D ≥ 1.
- **Upper bound object:** "the tower T_n is the unique worst Liu config" (exchange
  monotonicity / majorization), with Xiang's parallel-halving the saturating witness.

**Two shared walls:**
- **G1-lower (non-dyadic multi-split):** prove D ≥ 1 at every NON-dyadic breakpoint
  refinement of T_n. Dyadic + single-split breakpoints are closed (Lemmas 9,10);
  multi-split is grid-verified n≤6, OPEN. The certified PL-reduction
  (`pl-breakpoint-minimum`) lands the global min at a breakpoint, but the
  multi-split non-dyadic breakpoints are not settled. The failed sub-claim:
  "balancing a later split weakly decreases D after an unbalanced first split" is
  FALSE (T_3 8→5+3 witness, second-split D is V-shaped) — so single-split
  monotonicity does NOT compose. This is the structural reason the wall stands.
- **G1-upper (exchange monotonicity, n≥3):** "tower is unique worst Liu config" is a
  CONJECTURE verified n=1..4, OPEN n≥3. Below-threshold regimes C/B2 (G2) also open.

The framings are NOT independent: all three reduce the lower bound to D ≥ 1 and the
upper bound to a "tower-is-worst" exchange claim. Per the orchestrator's guidance,
the fix is a genuinely different framing — not another lens on D.

## Framings

### F1. Self-similar recurrence of the ANSWER (verified, clean upper-bound induction)
**The recurrence.** Let v_n := 2^n/(2^{n+1}-1). Then
  v_n = 2·v_{n-1} / (1 + 2·v_{n-1}),  equivalently  1/v_n = 1 + 1/(2·v_{n-1}).
VERIFIED exactly for n=2..6 (script /tmp/round-3/explore.py): v_1=2/3, v_2=4/7, v_3=8/15, … .

**Game decomposition (the recurrence's source).** The tower factors as
  T_n  =  {big piece of size 2^n}  ⊎  {scaled copy of T_{n-1}, total D_{n-1}=2^n-1}.
Normalized: big piece has fraction v_n; the sub-stick has total 1−v_n and IS a scaled T_{n-1}.

**Upper bound for the TOWER config by induction (clean, NEW narrative).** If Liu plays
T_n, Xiang's response "halve the big piece (→ two pieces v_n/2 each) and play optimally
on the sub-stick (≤ n−1 marks)" gives, by the inductive hypothesis on the sub-stick,
  Liu ≤ v_n/2  +  v_{n-1}·(1 − v_n).
The recurrence v_n/2 + v_{n-1}(1−v_n) = v_n then yields Liu ≤ v_n.
This is a clean inductive *re-derivation* of the parallel-halving saturation (Lemma 11),
organized self-similarly. It is logically equivalent to Lemma 11 for the tower upper
bound, but supplies the inductive scaffold the upper-bound induction needs.

**Why it does NOT escape the walls.** (a) The full upper bound needs Xiang to force ≤ v_n
against EVERY Liu config, not only the tower — that is exactly G1-upper (tower-is-worst).
(b) The LOWER bound by this decomposition hits the merge/interleaving wall: when Xiang
splits the big piece (≥1 mark), the sub-stick gets ≤ n−1 marks (so IH gives sub-stick
odd-index ≥ 2^{n-1}), BUT the global odd-index ≠ sub-stick odd-index + big-fragment
odd-index, because big-fragment pieces and sub-stick pieces INTERLEAVE in the sorted
order. This interleaving is precisely G1-lower. So the recurrence gives a clean upper
induction and a clean lower *case A* (big piece untouched → Liu ≥ v_n trivially, since
the intact big piece is the largest and Liu claims it first), but case B (big piece cut)
is G1-lower in disguise.

**Likelihood:** Medium as an upper-bound PROOF ORGANIZER (self-similar induction around
the recurrence, instead of the majorization/exchange narrative) — but it does NOT by
itself close either wall. Worth opening as a rival upper-bound *narrative* so the
upper-bound induction is not pinched into the single-gap majorization framing.

### F2. Gaps + leftover pairing (genuinely different proof object for G1-lower)
**Reformulation.** After Xiang's n marks (all distinct from Liu's), the refined config
has exactly m = 2n+1 pieces (Liu's n marks → n+1 pieces; Xiang's n marks → n more). With
pieces sorted descending p_1 ≥ … ≥ p_{2n+1},
  D = Σ_{k=1}^{n} (p_{2k-1} − p_{2k})  +  p_{2n+1}.
IDENTITY verified (/tmp/round-3/gaps.py): D = (sum of per-pair gaps) + (the leftover
smallest piece, since m is odd). Each gap ≥ 0 (sorted). So
  Liu ≥ v_n  ⟺  Σ_{k}(p_{2k-1}−p_{2k}) + p_{2n+1} ≥ 1.
This is algebraically D ≥ 1 (same inequality) BUT the proof object is different: a sum
of n per-turn advantages plus one leftover piece, against the target "1" = the smallest
tower piece (unnormalized). It invites a charging/matching/majorization proof rather than
a parity-integral or block-formula proof.

**Intuition from numerics (conjecture, not proof).** For n=2 minimizers achieving D=1
(grid-80): the "1" is DISTRIBUTED across gaps + leftover.
  - halving: pieces {2,2,1,1,1} → gaps 0+0, leftover 1 → the leftover carries it all.
  - all-cuts-on-big-piece (e.g. 4 → {0.05,1.1,2.85}, with {1,2} intact): sorted
    {2.85,2,1.1,1,0.05} → gaps (0.85)+(0.1), leftover 0.05 → the "1" is split as
    0.85+0.1+0.05.
So the "1" is a conserved quantity that flows into either the leftover or the gaps.

**Hard step.** Prove Σ gaps + leftover ≥ 1 from the tower structure under arbitrary
n-mark refinement. No clean induction is visible (interleaving again), but the object is
genuinely third-party to the PL-integral and block-formula machinery, so it is a real
rival framing for G1-lower.

**Likelihood:** Medium-low to actually close G1, but HIGH value as a DIVERSE rival
framing — a charging/pairing proof here is independent of the PL/block framings, so if
they are stuck on the wrong shape, this is the one that could break through. Recommend
the outliner open it.

### F3. Continuous relaxation + convexity/plateau (attacks G1-lower directly)
**Reformulation.** Relax Xiang's marks to a continuous "splitting measure" on the tower
pieces; D becomes a function of the cut-position vector. If D is concave (or
"PL with min at a plateau touching the dyadic point"), the global min is attained at the
dyadic halving config (already closed, Lemma 9), settling G1-lower without per-breakpoint
casework.

**Numerics (conjecture, NOT a proof — and a correction to a naive hope).** For n=2
(grid-80) the min D = 1 is attained on a LARGE PLATEAU, not uniquely at the dyadic
halving: 1418/27966 configs lie within 0.05 of the min; many non-dyadic configs (e.g.
both cuts on the big piece at non-half fractions) attain D=1 exactly. For n=3 (grid-30,
3 cuts) the min D=1 is likewise attained at non-dyadic breakpoints (e.g. all 3 cuts on
the piece of size 8). So:
  - "min UNIQUELY at dyadic" is FALSE.
  - The right statement is "D ≥ 1 with equality on a plateau that INCLUDES the dyadic
    config." This matches the existing PL-plateau observations in `tail-count`.

**Why it may help / may not.** The large plateau is encouraging (lots of flexibility,
so a coarse convexity/monotonicity argument might reach it) and it suggests the clean
target: "every non-dyadic breakpoint's D ≥ the D of an adjacent dyadic breakpoint" (the
"plateau lead" the approaches already flagged but did not prove for multi-split). But
the V-shaped second-split (the FALSE composition lemma, round 2) shows D is NOT
monotone in cut positions in general — so a naive convexity is false. A genuine proof
must exploit the TOWER structure (the self-similar sizes 1,2,4,…,2^n), not generic
convexity.

**Likelihood:** Low-medium. This is the SAME wall reframed (it IS G1-lower), but the
plateau-lead statement is a cleaner target than "prove D≥1 at every breakpoint," and
the numerics show the equality set is large (so the inequality is not tight-ish and
fragile — there is room). Recommend keeping as a fallback target within an existing
lower-bound slug, NOT as a new approach.

### F4. LP dual / saddle point for the full minimax (attacks BOTH bounds at once)
**Claim-game dual (verified for m=2,3,4 by hand).** For sorted-desc pieces p_1≥…≥p_m,
  odd-index sum = min{ Σ_i w_i p_i : w_1 ≥ 1,  w_i + w_{i+1} ≥ 1 ∀i,  w_i ≥ 0 }.
This is the LP dual of the greedy alternate-pick game. It certifies UPPER bounds
naturally (exhibit a feasible w with small Σw_i p_i). For the tower+halving refinement,
w = (1,0,1,0,1,…) is feasible and tight, giving v_n.

**Saddle confirmation (n=2, the load-bearing numerics).** Full minimax on grid-56
(grid = 8·7, so the tower is ON-grid and Xiang can halve at 1/(2·D_n) = 1/14 points)
(/tmp/round-3/gaps.py):
  - max over Liu configs (≤2 marks) of [min over Xiang (≤2 marks) of odd-index] = 4/7 EXACTLY.
  - The UNIQUE best Liu config is the tower T_2 = {1,2,4}/7 (next configs give 9/16 < 4/7).
  - Tower's Xiang-best = 4/7 exactly.
So (Liu=T_2, Xiang=halving) is a confirmed saddle for n=2 — strong independent
evidence for the "tower is unique worst" upper-bound conjecture (G1-upper).

**Why it does NOT cleanly sidestep both walls.** (a) The full minimax is NOT a clean LP:
the sorting makes odd-index piecewise-linear (not linear), and "≤ n marks" is a
cardinality constraint with a likely integrality gap in any LP relaxation. (b) For the
LOWER bound, the dual is circular: odd-index = min_w Σw_i p_i, so "every feasible w
gives Σw_i p_i ≥ v_n" IS "odd-index ≥ v_n" — no non-circular lower-bound certificate
flows from this dual. (c) For the UPPER bound, proving the saddle is a saddle for
general n *requires proving the tower is Liu's best response to halving* — which is
exactly G1-upper. So the saddle approach SUBSUMES G1-upper rather than bypassing it.

**What the dual IS good for.** Clean upper-bound certificates for a FIXED Liu config
(exhibit a feasible w). This could reorganize the upper-bound casework (majorization
regimes) into a single dual-feasibility check per regime. But it does not escape G1-upper.

**Likelihood:** Low to escape the walls, but the n=2 saddle numerics are valuable
evidence (tower unique best). Recommend NOT opening a new slug on this; instead feed
the saddle confirmation into the existing `majorization-upper` approach as corroboration
that "tower is unique worst" is the right conjecture, and note the dual-w certificate
machinery as an optional re-derivation of the upper bound for fixed configs.

## Numerics

- **Recurrence** (/tmp/round-3/explore.py): v_n = 2v_{n-1}/(1+2v_{n-1}) and
  1/v_n = 1 + 1/(2v_{n-1}) verified exactly n=2..6.
- **n=2 minimizer plateau** (/tmp/round-3/convexity.py): min D=1 (target); 1418 configs
  within 0.05; minimizers include many non-dyadic configs (both cuts on the big piece).
  Max D=4. Min NOT unique to dyadic halving — it is a plateau.
- **n=3 minimizer** (/tmp/round-3/convexity.py, grid-30): min D=1.000, attained at
  non-dyadic breakpoint (all 3 cuts on the size-8 piece); 240 configs within 0.02 of min.
- **Gaps+leftover identity** (/tmp/round-3/gaps.py): D = Σ(p_{2k-1}−p_{2k}) + p_{2n+1}
  (m=2n+1 odd) verified.
- **n=2 full minimax = saddle** (/tmp/round-3/gaps.py, grid-56): max-min = 4/7 EXACTLY,
  tower T_2 UNIQUE best Liu config, tower's Xiang-best = 4/7. (Earlier coarse/non-multiple
  grids — grid-30/50 — placed the tower OFF-grid and falsely reported c(2) > 4/7; only
  grids that are multiples of D_n are trustworthy. This is a recurring explorer pitfall.)
- All numerics are CONJECTURE/evidence, not proof (rigor rule).

## Recommendation

Open **ONE** genuinely new approach: **F2 (gaps + leftover pairing)** as a fresh
lower-bound slug, attacking G1-lower with charging/matching/majorization machinery that
is independent of both the PL-parity-integral (`tail-count`) and the block/frontier
(`tower-induction`) framings. Its proof object — "Σ per-pair gaps + the leftover piece
≥ 1" — is third-party to the current machinery; if the lower-bound wall is a wrong-shape
problem (V-shaped second-split defeating monotonicity), this is the framing most likely
to see around it. Concretely the outliner should ask: can a charging argument push the
"1" (the smallest tower piece, unnormalized) into the gaps+leftover for every n-mark
refinement of T_n, using only the tower's self-similar sizes?

Do NOT open F3 (convexity/plateau) or F4 (LP saddle) as new slugs:
- F3 IS G1-lower reframed (no escape); keep it as a fallback target *inside* an existing
  lower-bound slug, sharpened to the "plateau-lead" statement (every non-dyadic
  breakpoint's D ≥ an adjacent dyadic breakpoint's D), which the plateau numerics support.
- F4 subsumes G1-upper (proving the saddle needs "tower-is-worst"); feed its n=2 saddle
  numerics into `majorization-upper` as corroboration, and offer the dual-w certificate
  as an optional re-derivation of the upper bound for fixed Liu configs (regimes A/B1).

Fold **F1 (recurrence + self-similar induction)** into the upper-bound slug
(`majorization-upper`) as the inductive *narrative*: it gives a clean self-similar
recurrence v_n = 2v_{n-1}/(1+2v_{n-1}) and a "halve-the-big-piece + recurse" induction
that may organize the upper-bound induction more cleanly than the exchange/majorization
narrative, and it makes the case-A lower-bound step (big piece untouched → Liu ≥ v_n
trivially) explicit. It does NOT by itself close a wall, but it diversifies the
upper-bound induction's shape, reducing single-gap risk.

**Could any framing close BOTH bounds at once?** No clean candidate found. F4 (saddle)
is the only one that would in principle do both, but it subsumes G1-upper rather than
bypassing it, and the LP relaxation has a likely integrality gap from the cardinality
(≤n marks) constraint. The honest assessment: G1-lower and G1-upper remain genuinely
open; the best this round can do is diversify the lower-bound machinery (F2) and
reorganize the upper-bound induction (F1), so the field is no longer three lenses on
the same D-integral / same exchange claim.
