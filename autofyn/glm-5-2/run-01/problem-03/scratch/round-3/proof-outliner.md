# proof-outliner — IMO 2026 P3 (imo-2026-03), round 3

Target (the whole problem, end to end): prove `c(n) = 2^n / (2^{n+1} - 1)`.
Both bounds, all n. Lower bound = Liu plays the tower `T_n`, prove `D >= 1`
(tower units) for every Xiang refinement. Upper bound = for every Liu config,
Xiang has <= n marks forcing `D <= 1/D_n`. Two load-bearing walls remain:
**G1-lower** (non-dyadic multi-split: `D >= 1` at every non-dyadic breakpoint)
and **G1-upper/G2** (general-n upper bound: the Max-bound `D* <= M/2^n` unifying
the below-threshold non-dominant case).

State of the field (6 registered slugs): tail-count (Elo 1603, leader, stale),
tower-induction (1530, stale), majorization-upper (1529, stale), d-potential
(1519, not stale), self-similar (1438), balanced-configs (1382, retired). 13
certified lemmas importable from `results/imo-2026-03/lemmas/`.

Three round-3 explorer reports folded in:
- **lower-nondyadic**: pair-cancellation+spine (even-group strong bps CLOSE
  clean; odd-group MINIMIZERS exist so pair-cancellation alone is INSUFFICIENT);
  2-split sub-case cleanly closable (min `D = D(T_{n-2}) >= 1`, highest-confidence
  concrete progress); plateau-connectivity/global-exchange is the deepest lead
  but LOCAL rebalancing FAILS (V-shape, `8->5+3` then `5->4+1` gives D=1, rebalanced
  `5->2.5+2.5` gives D=3) — the exchange must be GLOBAL.
- **upper-exchange**: majorization/Schur-convexity DEAD (decisive counterexamples:
  single piece `(1)` is most-majorizing yet `D*=0`; `D*` is not Schur-convex).
  Max-bound conjecture `D* <= M/2^n` (M = largest piece) unifies G1+G2, 0 violations
  over 2860+ configs, tight uniquely at the tower. Dominant case is a one-line
  halving induction; the hard step is the non-dyadic `a_3 > a_1/2` sub-case (adaptive
  optimal move, needs a two-variable IH `D* <= f(M, M_2, n)`).
- **alt-framing**: the genuinely-new lower-bound framing is **gaps+leftover**
  (`D = sum(p_{2k-1} - p_{2k}) + p_{2n+1}`, a charging/matching proof vs the target
  "1" = smallest tower piece), third-party to PL-integral and block-formula
  machinery; F3 (convexity/plateau) IS G1-lower reframed (no escape, keep as
  fallback inside an existing slug); F4 (LP saddle) subsumes G1-upper (no escape);
  F1 (self-similar recurrence) folds into the upper-bound induction as narrative.

Per the orchestrator's explicit constraints: (1) OPEN gaps-leftover as a NEW
lower-bound slug (far from PL/block machinery); advance the 2-split sub-case
closure and pair-cancellation+spine (fold into tail-count/tower-induction);
nominate plateau-connectivity (global exchange) as the ADVANCE target inside
the lower-bound slug most likely to carry it, flagging LOCAL-rebalancing-fails
as the hard step. (2) REVISE majorization-upper to center on the Max-bound (ONE
upper-bound slug, single-gap-trap rule); drop majorization/Schur; new engine =
Max-bound halving induction + two-variable IH. (3) Each slug targets the whole
claim. (4) Record imported lemmas.

---

## imo-2026-03

### tail-count: ADVANCE
Target: prove `c(n) = 2^n / (2^{n+1} - 1)` (whole claim), lower-bound spine.
Technique: PL/variational (D = integral of N(t) mod 2) + plateau connectivity
(GLOBAL exchange), the PL/variational route to G1-lower.
Framing (one sentence): the lower bound `D >= 1` for every Xiang refinement of
`T_n` via the piecewise-linear + breakpoint reduction, advancing now to (a) certify
the 2-split sub-case as a lemma, (b) fold in the pair-cancellation+spine even-group
sub-result, and (c) attack the plateau-connectivity global exchange as the deep
G1-closing step.
Skeleton:
  1. Import Lemma 0 (`claim-game-odd-index`), `D-equals-parity-integral`,
     `tower-top-unsplit` (case a), `single-split-top-lower-bound` (case b-i),
     `dyadic-refinement-lower-bound` (case b-ii-dyadic), `pl-breakpoint-minimum`,
     `frontier-recursion` — all certified.
  2. Case (a) top-unsplit: `D >= 1` — certified (`tower-top-unsplit`).
  3. Case (b-i) single-split: `D >= D(T_{n-1}) >= 1` — certified
     (`single-split-top-lower-bound`, PL slope {0,-2}, min at plateau).
  4. Case (b-ii-dyadic) all-balanced-splits: `D >= 1` — certified
     (`dyadic-refinement-lower-bound`, level-block dominance).
  5. NEW THIS ROUND — 2-split sub-case (G1 partial): prove `D >= D(T_{n-2}) >= 1`
     for every 2-mark refinement of `T_n`, all n. Mechanism: the two structural
     types (split-smaller-fragment, split-larger-fragment) each give D as explicit
     PL in the two cut points; the min plateau touches the dyadic cascade
     `{2^{n-1},2^{n-1},2^{n-2},2^{n-2},...}` where `dyadic-refinement-lower-bound`
     applies. Candidate lemma `two-split-lower-bound`.
  6. NEW THIS ROUND — pair-cancellation + spine (even-group sub-result, from
     explorer 1 §S1/S2): at a strong breakpoint, equal-adjacent pairs cancel (S1);
     non-dyadic fragments form adjacent-equal groups, EVEN-count groups fully
     cancel (S2); if all non-dyadic groups are even, the spine = distinct powers
     of 2, and the largest exceeds the sum of all smaller (geometric bound,
     `2^{k_1} > 2^{k_2+1}-1`), with the spine nonempty (total mass D_n is ODD,
     pairs contribute EVEN mass, so the unpaired mass is odd => 1 is in the spine),
     giving `D(spine) >= 1`. Closes G1 for even-group strong breakpoints.
  7. G1 DEEP ADVANCE — plateau connectivity (GLOBAL exchange): prove the min-level
     set `{D = D*}` always contains a DYADIC config, so `dyadic-refinement-lower-bound`
     gives `D* >= 1`. The PL-vertex iteration slides along ZERO-gradient directions
     (plateaus) until reaching a vertex where ALL coordinates are pinned; the target
     is to show this terminal vertex can be chosen dyadic by routing the slide
     through dyadic-friendly directions. HARD STEP (flagged): LOCAL rebalancing
     FAILS — the V-shape (`8->5+3` then `5->4+1` gives D=1; rebalanced
     `5->2.5+2.5` gives D=3, an INCREASE) kills any per-split "replace unbalanced
     by balanced" exchange. The exchange must be a multi-coordinate GLOBAL
     deformation keeping `D = D*`, not a sequence of local rebalancings. This is
     the research-prize step; if closed it unifies the whole lower bound.
  8. Upper bound: cite `majorization-upper` (the upper-bound slug owns this); n=1
     imported from `n1-base-both-bounds`.
Key lemmas (claim + mechanism):
  - `D >= D(T_{n-2}) >= 1` for every 2-split refinement — because the two
    structural types each give D as explicit PL in the cut points, and the min
    plateau touches the dyadic cascade where `dyadic-refinement-lower-bound`
    applies.
  - Even-group strong breakpoints have `D >= 1` — because equal-adjacent pairs
    cancel (S1), even-count non-dyadic groups cancel (S2), the spine is distinct
    powers of 2, and the largest power exceeds the sum of all smaller (geometric
    dominance), with the spine nonempty (odd-total mass forces an unpaired 1).
  - The min-level set contains a dyadic config — because the PL-vertex slide
    along zero-gradient directions reaches a terminal vertex choosable dyadic
    (GLOBAL exchange, NOT local rebalancing). [GAP — the hard step]
Open gaps:
  - G1 (non-dyadic multi-split, k >= 3): the plateau-connectivity global exchange
    is unproved; the V-shape is the obstruction to the natural local induction.
    Even-group strong bps closed; odd-group MINIMIZERS exist (e.g.
    `{4.75,4,2,2,1,1,0.25}`, D=1) so the pair-cancellation sub-result is a partial,
    not a full close.
  - Upper bound general n: deferred to `majorization-upper`.
Cases to cover: single-split (closed), 2-split (closeable this round), k-split
k>=3 (G1 open); even-group vs odd-group strong breakpoints; PL-vertex vs strong
breakpoint (lone larger-fragment configs).
Watch out for:
  - The V-shape: NEVER assume "balancing a later split weakly decreases D after
    an unbalanced first split" — it is FALSE (round-2 rule). The exchange must be
    global.
  - Odd-group MINIMIZERS exist (321 of them for T_3 3-split at D=1); the
    pair-cancellation argument is INSUFFICIENT alone — it closes even-group bps
    but odd-group non-strong (PL-vertex) configs reach D*=1 with a non-dyadic
    spine.
  - PL-vertex != strong breakpoint: the lone larger-fragment requires sliding a
    DIFFERENT coordinate to eliminate, and the V-shape shows this is not always a
    local decrease.
Imports: `claim-game-odd-index`, `D-equals-parity-integral`, `layer-cake-odd-index`,
`tower-top-unsplit`, `single-split-top-lower-bound`, `dyadic-refinement-lower-bound`,
`pl-breakpoint-minimum`, `frontier-recursion`, `n1-base-both-bounds`,
`closed-form-answer`.
Note for reviewer: leader, stale (round-2 outcome unprocessed). Advancing with
the 2-split lemma (highest-confidence concrete progress) + pair-cancellation
even-group sub-result + the plateau-connectivity deep advance. The 2-split
lemma and the even-group sub-result are certifiable independently regardless of
whether the global exchange closes.

### tower-induction: ADVANCE
Target: prove `c(n) = 2^n / (2^{n+1} - 1)` (whole claim), lower-bound spine.
Technique: block-contribution formula + frontier recursion (block/parity
machinery), pushed toward a NON-dyadic generalization via spine sign-bookkeeping.
Framing (one sentence): the lower bound via the block/parity formula
`D = sum_k 2^k (-1)^{C_k} (n_k mod 2)` for dyadic refinements, advancing now to
generalize the block-tracking to non-dyadic fragments by tracking fragment values
mod the tower skeleton and attempting a sign-bookkeeping bound on the spine
(explorer 1 Route D), the genuinely different machinery on the same G1 wall.
Skeleton:
  1. Import Lemma 0, `tower-top-unsplit` (case a), `frontier-recursion`,
     `block-contribution-formula`, `dyadic-refinement-lower-bound`,
     `pl-breakpoint-minimum`, `single-split-top-lower-bound`, `n1-base-both-bounds`.
  2. Case (a) + balanced (b-ii-dyadic): `D >= 1` — certified
     (`tower-top-unsplit`, `dyadic-refinement-lower-bound` via F-block + F-rec +
     F-min).
  3. Case (b-i) single-split: cite `single-split-top-lower-bound`.
  4. NEW THIS ROUND — non-dyadic spine generalization (Route D): for a non-dyadic
    refinement, remove all adjacent-equal pairs (S1, from explorer 1) to form the
    spine (strictly-decreasing distinct values: powers of 2 + non-dyadic
    leftovers, one per odd-count non-dyadic group). The block formula does not
    apply directly, but track each non-dyadic leftover's sign (position parity in
    the spine) and value relative to the flanking tower pieces. Sub-targets:
    (i) even-count non-dyadic groups fully cancel (clean, closes even-group bps —
    same sub-result as tail-count step 6, derived here from the block viewpoint);
    (ii) for odd-count leftovers, characterize where they sit relative to the
    flanking tower pieces and prove the net contribution keeps `D(spine) >= 1`.
  5. G1 HARD STEP — the sign of a non-dyadic leftover depends on global parity
    (its position in the spine): e.g. `4.75 @ +` and `0.25 @ +` in
    `{4.75,4,0.25}` give D=1; `7/3 @ -` in `{4,7/3,2}` gives D=11/3. No uniform
    "leftover contributes +" rule. A sign-bookkeeping argument tied to the
    splitting tree (which fragment spawned which leftover) is needed but not
    evident. This is the block/parity counterpart of tail-count's plateau wall.
  6. Upper bound: cite `majorization-upper`; n=1 from `n1-base-both-bounds`.
Key lemmas (claim + mechanism):
  - Even-count non-dyadic groups fully cancel in the spine — because adjacent-equal
    pairs cancel (sign-agnostic), and an even-count group is a union of pairs.
  - The spine of an even-group breakpoint is distinct powers of 2 with `D >= 1`
    — because the largest power exceeds the sum of all smaller (geometric
    dominance) and the spine is nonempty (odd-total-mass forces an unpaired 1).
  - For odd-count leftovers, `D(spine) >= 1` — because [GAP: the sign-bookkeeping
    tied to the splitting tree]. The leftovers come from splitting-tree "ends"
    (top fragment and cascading-residual fragment); in `{4.75,4,0.25}` the two
    leftovers `4.75+0.25=5` straddle tower 4 and `D = 5-4 = 1`.
Open gaps:
  - G1 (non-dyadic multi-split, odd-count leftovers): the sign-bookkeeping bound
    on the spine is unproved. Odd-group MINIMIZERS exist (D=1) so a clean bound
    must account for the global parity of each leftover's position.
  - Upper bound general n: deferred to `majorization-upper`.
Cases to cover: even-group vs odd-count non-dyadic groups; leftover position
(above all tower pieces / between two tower pieces / below all); splitting-tree
origin of each leftover (top fragment vs cascading residual).
Watch out for:
  - The block formula `D = sum_k 2^k (-1)^{C_k} (n_k mod 2)` applies ONLY to
    dyadic refinements (all fragments powers of 2); non-dyadic fragments do not
    group into 2^k-blocks, so within-block pair-cancellation fails. The
    generalization must track fragment values mod the tower skeleton, not mod 2^k.
  - The sign of a leftover is NOT uniformly +; it depends on global parity. Do
    not assume "leftover contributes +" without proving the position-parity
    bookkeeping.
  - Odd-group MINIMIZERS exist (D=1), so any bound must be tight enough to reach
    1, not just > 1.
Imports: `claim-game-odd-index`, `tower-top-unsplit`, `frontier-recursion`,
`block-contribution-formula`, `dyadic-refinement-lower-bound`,
`pl-breakpoint-minimum`, `single-split-top-lower-bound`, `n1-base-both-bounds`,
`closed-form-answer`.
Note for reviewer: the genuinely different machinery (block/parity vs PL) on the
same G1 wall — keep diverse within, do NOT retire. The even-group sub-result is
certifiable independently. The odd-count spine bound is the open hard step
(counterpart to tail-count's plateau wall).

### gaps-leftover: NEW (OPEN)
Target: prove `c(n) = 2^n / (2^{n+1} - 1)` (whole claim), lower-bound spine.
Technique: charging/matching — a per-pair gap + leftover charging argument,
third-party to both the PL-integral (tail-count) and block/formula (tower-induction)
machinery.
Framing (one sentence): after Xiang's n marks the refined config has exactly
`m = 2n+1` pieces (Liu's n marks -> n+1 pieces; Xiang's n marks -> n more), and
`D = sum_{k=1}^{n} (p_{2k-1} - p_{2k}) + p_{2n+1}` (per-pair gaps + the leftover
smallest piece), so `D >= 1` is "the n per-turn advantages plus one leftover piece
cover the target 1 (= smallest tower piece, unnormalized)" — a charging/matching
proof against the tower's self-similar sizes, not a parity-integral or block formula.
Skeleton:
  1. Import Lemma 0, `tower-top-unsplit` (case a), `pl-breakpoint-minimum`,
     `dyadic-refinement-lower-bound`, `single-split-top-lower-bound`,
     `n1-base-both-bounds`, `closed-form-answer`.
  2. Identity (verified, explorer 3 /tmp/round-3/gaps.py): for sorted-desc
    `p_1 >= ... >= p_{2n+1}`,
    `D = sum_{k=1}^{n} (p_{2k-1} - p_{2k}) + p_{2n+1}`. Each gap `>= 0` (sorted).
    So `D >= 1` iff `sum(gaps) + leftover >= 1`.
  3. Case (a) top-unsplit: `D >= 1` — cite `tower-top-unsplit` (the intact top
    piece `2^n` is the largest, Liu claims it first, trivially `>= 1`).
  4. Case (b-i) single-split: cite `single-split-top-lower-bound`.
  5. Case (b-ii-dyadic): cite `dyadic-refinement-lower-bound`.
  6. G1-lower via charging/matching (the NEW route): prove
    `sum_{k}(p_{2k-1} - p_{2k}) + p_{2n+1} >= 1` for every n-mark refinement of
    `T_n`. The target "1" is the smallest tower piece (unnormalized). The
    charging argument: charge each per-pair gap and the leftover to the tower's
    self-similar sizes `{2^n, 2^{n-1}, ..., 2, 1}`. Intuition from numerics
    (explorer 3): for n=2 minimizers at D=1, the "1" is DISTRIBUTED — halving
    `{2,2,1,1,1}` -> gaps 0+0, leftover 1 (leftover carries it all); all-cuts-on-
    big-piece `{2.85,2,1.1,1,0.05}` -> gaps 0.85+0.1, leftover 0.05 (the "1" is
    split as 0.85+0.1+0.05). The "1" is a conserved quantity flowing into either
    the leftover or the gaps.
  7. G1 HARD STEP — the charging/matching proof. No clean induction is visible
    (interleaving of big-fragment pieces and sub-stick pieces in the sorted order
    is the obstruction, same as the PL/block routes hit), BUT the proof object is
    genuinely third-party: a charging argument that pushes the "1" into the
    gaps+leftover using only the tower's self-similar sizes, not a parity-integral
    or block-formula decomposition. Candidate mechanism: a matching between the
    `2n` paired pieces and the tower skeleton `{2^n, ..., 2, 1}` such that each
    pair's gap is charged to a tower level, with the leftover charged to the
    smallest level. The matching must be adaptive (depends on which tower pieces
    Xiang split), but the tower's dyadic sizes force the total charge to be `>= 1`.
  8. Upper bound: cite `majorization-upper`; n=1 from `n1-base-both-bounds`.
Key lemmas (claim + mechanism):
  - `D = sum(gaps) + leftover` — because the alternating sum of `2n+1` sorted
    pieces telescopes into n per-pair differences plus the last (odd-position)
    piece. (Identity, verified.)
  - `sum(gaps) + leftover >= 1` — because [GAP: a charging/matching argument
    pushes the "1" (smallest tower piece) into the gaps+leftover using the tower's
    self-similar dyadic sizes]. The "1" is a conserved quantity (numerics: it
    flows into either the leftover or the gaps).
Open gaps:
  - G1-lower (the charging/matching proof): `sum(gaps) + leftover >= 1` for
    every n-mark refinement of `T_n`. The interleaving obstruction means no clean
    induction, but the charging object is independent of PL/block machinery — if
    the lower-bound wall is a wrong-shape problem (V-shaped second-split defeating
    monotonicity), this is the framing most likely to see around it.
  - Upper bound general n: deferred to `majorization-upper`.
Cases to cover: which tower pieces Xiang split (top piece / interior / bottom);
the matching between paired pieces and tower levels; the distribution of the "1"
into gaps vs leftover (leftover-carries-all vs split).
Watch out for:
  - The identity `D = sum(gaps) + leftover` is ALGEBRAICALLY `D >= 1` (same
    inequality as the PL/block routes) — the diversity is in the PROOF OBJECT
    (charging/matching vs parity-integral/block-formula), not the statement. Do
    not re-label the same inequality as progress; the charging argument must be a
    genuinely different mechanism.
  - The interleaving obstruction: big-fragment pieces and sub-stick pieces
    INTERLEAVE in the sorted order, so the per-pair gaps are not simply
    "tower-level gaps." The matching must account for interleaving.
  - The "1" is a conserved quantity (numerics), but this is CONJECTURE, not proof.
    The charging argument must prove the conservation, not assume it.
Imports: `claim-game-odd-index`, `tower-top-unsplit`, `pl-breakpoint-minimum`,
`dyadic-refinement-lower-bound`, `single-split-top-lower-bound`,
`n1-base-both-bounds`, `closed-form-answer`.
Note for reviewer: genuinely new framing (charging/matching), far from PL/block
machinery — the diversity-of-thought slug the orchestrator asked for. Its proof
object is third-party; if the lower-bound wall is a wrong-shape problem, this is
the framing most likely to break through. The identity is verified; the
charging argument is the open GAP. High value as a rival even if it does not
close G1 this round — it keeps the field from collapsing to one framing.

### majorization-upper: REVISE
Target: prove `c(n) = 2^n / (2^{n+1} - 1)` (whole claim), upper-bound spine.
Technique: Max-bound halving induction `D* <= M/2^n` (piece-count-free
strengthened IH) + two-variable IH `D* <= f(M, M_2, n)` for the non-dominant
`a_3 > a_1/2` sub-case. Majorization/Schur-convexity DROPPED (dead per explorer 2).
Framing (one sentence): the upper bound via the Max-bound conjecture `D* <= M/2^n`
(M = largest Liu piece), which unifies G1 and G2 (the non-dominant below-threshold
wall) and is tight uniquely at the tower — the dominant case is a one-line halving
induction, the non-dominant `a_3 > a_1/2` sub-case is the crux, attacked via a
two-variable IH tracking `(max, second-max)`.
Skeleton:
  1. Import Lemma 0, `n1-base-both-bounds` (n=1 base), `n2-upper-bound-complete`
     (n=2 base, the averaging-bound mechanism), `parallel-halving-saturates-tower`
     (U1, the equality witness `D(T_n) = 1/D_n`), `pl-breakpoint-minimum` (B1,
     Xiang optimum at a tie/breakpoint), `D-equals-parity-integral`,
     `closed-form-answer`, `tower-top-unsplit` (lower bound, cited).
  2. Lower bound: cite `tower-top-unsplit` + the advancing `tail-count` /
     `tower-induction` / `gaps-leftover` slugs. (This slug owns the UPPER bound.)
  3. n=1 base: certified (`n1-base-both-bounds`).
  4. n=2 base: certified (`n2-upper-bound-complete`, all m <= 3, all four regimes,
     tower T_2 unique equality). The n=2 mechanism extracted (explorer 2): the
     load-bearing step is the AVERAGING bound `min(b_1-b_2, 2b_2-b_1) <= b_2/2`
     on the 2-piece rest, NOT a Robin-Hood/majorization move. Non-tower
     arithmetic forces `b_2 < 2/7` strictly, giving strict inequality. The tower
     is unique worst because it is the unique config where `b_2` lands exactly at
     the threshold `2/7` (= n=1 worst `T_1`).
  5. NEW SPINE — the Max-bound conjecture `D*(L) <= M/2^n` (M = a_1, any piece
     count, total 1). Verified 0 violations over 2860+ configs (n=2,3,4), tight
     uniquely at the tower (`M = 2^n/D_n` => `M/2^n = 1/D_n`). If proven, it
     closes G2 (below-threshold `M < 2^n/D_n` => `D* < 1/D_n` strictly) in one
     stroke; combined with the certified dominant factorization (regimes A/B1),
     it closes the full upper bound.
  6. Max-bound induction — DOMINANT case (one-line, proven at scout level): base
     `n=0`: `D <= a_1 = M` (alternating sum of sorted-desc <= first term). Step
     `W(n-1) => W(n)`: dominant `a_1 >= 2 a_2`, halve `a_1 -> {a_1/2, a_1/2}`,
     new max `= a_1/2 = M/2` (since `a_1/2 >= a_2`), the two halves cancel
     (positions 1,2), by `W(n-1)` on the new multiset (piece-count-free):
     `D <= (M/2)/2^{n-1} = M/2^n`. [CLOSED]
  7. Max-bound induction — NON-DOMINANT case `a_1 < 2 a_2` (the CRUX): halving
     `a_1` puts halves at positions 3,4 (after `a_2`); they cancel, giving
     `D = D({a_2, a_3, ...})` with new max `a_2`. By IH: `D <= a_2/2^{n-1}`, but
     we need `<= a_1/2^n`, i.e. `a_2 <= a_1/2` — CONTRADICTS non-dominant
     (`a_2 > a_1/2`). Pairing `a_1 -> {a_2, a_1-a_2}` leaves rest'-max `= a_3`
     (when `a_3 > a_1-a_2`), and `a_3` can exceed `a_1/2` (witness
     `(0.4,0.35,0.25)`, `a_3=0.25 > 0.20`). The simple induction BREAKS here.
  8. G1/G2 HARD STEP — the two-variable IH `D* <= f(M, M_2, n)` tracking both
     the max `M = a_1` and the second-max `M_2 = a_2`. The pairing move removes
     `a_1, a_2` together, so a bound in `(M, M_2)` can tighten. Concrete
     sub-target: prove `D* <= M/2^n` for non-dominant configs by induction where
     the IH tracks `(max, second-max)`. The optimal move is ADAPTIVE (trace:
     pair `a_1 <-> a_2` leaving fragment `a_1-a_2`, then halve `a_3`; OR halve
     `a_1` to land mid-list when `a_1/2` sits between `a_2` and `a_3`; no single
     rule). The two-variable IH must handle both sub-cases. Base n=2 is certified
     (`n2-upper-bound-complete`). Fallback (explorer 2 Route b): a residual-integral
     characterization `D = integral(N(t) mod 2) dt`, proving the residual
     (measure of the unpaired-interval set) `<= M/2^n`.
  9. Self-similar recurrence narrative (explplorer 3 F1, fold in): the answer
     satisfies `v_n = 2 v_{n-1} / (1 + 2 v_{n-1})`, `1/v_n = 1 + 1/(2 v_{n-1})`,
     verified n=2..6. The tower factors as `T_n = {big piece 2^n} + {scaled
     T_{n-1}, total D_{n-1}}`. Xiang's "halve the big piece + recurse on the
     sub-stick" gives `Liu <= v_n/2 + v_{n-1}(1-v_n) = v_n` by the recurrence —
     a clean self-similar re-derivation of `parallel-halving-saturates-tower`
     that organizes the upper-bound induction more cleanly than the
     exchange/majorization narrative. (Does NOT by itself close G1-upper — it
     only covers the tower config — but it diversifies the upper-bound
     induction's shape, reducing single-gap risk.)
  10. Answer verification: `c(n) = 2^n / (2^{n+1} - 1)`, verified n=1..4 by
      substitution (`(1 + 1/D_n)/2 = 2^n/D_n`).
Key lemmas (claim + mechanism):
  - `D* <= M/2^n` for dominant configs — because halving `a_1` gives new max
    `M/2`, the halves cancel (positions 1,2), and `W(n-1)` applies piece-count-free.
  - `D* <= M/2^n` for non-dominant configs — because [GAP: a two-variable IH
    `D* <= f(M, M_2, n)` tracking (max, second-max) tightens the bound when the
    pairing move removes `a_1, a_2` together]. The optimal move is adaptive
    (pair-then-halve or halve-to-mid-list); the IH must handle both.
  - The Max-bound is tight uniquely at the tower — because `M = 2^n/D_n` =>
    `M/2^n = 1/D_n = D*(T_n)` (ratio exactly 1.000 at n=2,3,4); the worst non-tower
    ratio is 0.987 (near-tower), so the bound cannot be improved.
Open gaps:
  - G1/G2 (non-dominant `a_3 > a_1/2`): the two-variable IH is unproved. The
    Max-bound is a CONJECTURE (strongly verified, not proved). The non-dominant
    case is where it could still fail in general (holds in all 2860+ tests). Mark
    as explicit GAP; fallback = residual-integral characterization.
  - The dominant case + factorization (regimes A/B1) is certifiable independently
    as proven scaffolding regardless of whether the non-dominant sub-step closes.
Cases to cover: dominant (`a_1 >= 2 a_2`) vs non-dominant (`a_1 < 2 a_2`); within
non-dominant, `a_3 > a_1/2` (pairing leaves large rest'-max) vs `a_3 <= a_1/2`
(halving suffices); the optimal move (pair-then-halve vs halve-to-mid-list).
Watch out for:
  - Majorization/Schur-convexity/Karamata is DEAD — `D*` is not Schur-convex
    (single piece `(1)` is most-majorizing yet `D*=0`; `(0.6,0.25,0.1,0.05)`
    majorizes `T_3` yet `D*=0.05 < 0.0667`). Do NOT frame the induction as
    "tower is the most-spread / most-majorizing config." The right
    characterization is the dyadic self-similar structure, NOT "most spread."
  - The Max-bound is a CONJECTURE — do not present it as proven. Mark the
    non-dominant sub-step as an explicit GAP.
  - The averaging bound `min(...) <= b_2/2` does NOT generalize to n >= 3 (the
    rest after one mark has >= 3 pieces, no 3-piece analog). The n=2 base is a
    base, not a template.
  - One upper-bound slug only (single-gap-trap rule, round 2): the Max-bound
    unifies G1 and G2 — do NOT open a second upper-bound slug.
Imports: `claim-game-odd-index`, `n1-base-both-bounds`, `n2-upper-bound-complete`,
`parallel-halving-saturates-tower`, `pl-breakpoint-minimum`,
`D-equals-parity-integral`, `closed-form-answer`, `tower-top-unsplit` (lower
bound, cited).
Note for reviewer: REVISED — the majorization/Schur route is DEAD (decisive
counterexamples, explorer 2), dropped. New spine = the Max-bound `D* <= M/2^n`
(piece-count-free strengthened IH), which unifies G1 and G2 (single-gap-trap
rule). Dominant case is a one-line halving induction (proven at scout level);
the non-dominant `a_3 > a_1/2` sub-case is the crux, attacked via a two-variable
IH. Certified scaffolding (U1, B1, n=2) stays. The Max-bound is a CONJECTURE
(strongly verified, not proved) — mark the non-dominant sub-step as explicit GAP.
The self-similar recurrence narrative (F1) is folded in as an inductive
organizer, reducing single-gap risk.

### d-potential: HOLD
Target: prove `c(n) = 2^n / (2^{n+1} - 1)` (whole claim).
Technique: potential/weight-function Phi >= D with a per-mark decay.
Framing (one sentence): the potential programme Phi >= D with a per-mark decay
`1/Phi' >= 2/Phi + 1` would yield the answer, but the natural candidate Phi = D
is circular (T_1 witness: D stays 1/3 under the optimal mark, but `2/D + 1 = 7`);
no concrete Phi exists.
Action: HOLD (not in the build set this round). The potential programme is
shown circular; its certified outputs (Lemma 0, closed-form recursion, n=1 base,
case-A) are already in the shared cache and imported by the other slugs. No new
machinery to advance this round; keep live in the population for diversity (it
is NOT stale — last outcome round 1).
Note for reviewer: HOLD — no builder dispatched. Certified outputs already
harvested. Keep in the population for ranker diversity; revisit only if a concrete
Phi candidate emerges.

---

## build set

build set: tail-count, tower-induction, gaps-leftover, majorization-upper

(4 slugs: 2 advances [tail-count, tower-induction] + 1 new [gaps-leftover] + 1
revised [majorization-upper]. d-potential HELD, self-similar HELD,
balanced-configs RETIRED. The 3 lower-bound slugs diversify in FRAMING/route
[PL-variational, block/parity, charging/matching] on the same G1 wall — not
technique variations on one idea. The 1 upper-bound slug [Max-bound halving
induction] unifies G1+G2 per the single-gap-trap rule. Each slug targets the
whole claim `c(n) = 2^n/(2^{n+1}-1)` end to end.)
