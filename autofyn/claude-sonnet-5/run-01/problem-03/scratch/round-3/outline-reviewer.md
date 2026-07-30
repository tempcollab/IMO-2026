# Outline review — imo-2026-03, round 3

Reviewed against `results/imo-2026-03/current.md`, all `approaches/*.md`, all
`lemmas/*.md`, `knowledge_base.md`, and `/tmp/round-3/proof-outliner.md`
(4 candidates: geometric-dominance-construction, recursive-embedding-induction,
universal-adversary-strategy, majorization-smoothing).

I independently re-ran a numeric concavity check (exact `Fraction` arithmetic,
sorted-descending simplex, true game-value `V(p) = min_B oddrank(B)` computed
by brute-force enumeration of Xiang Yu's mark distributions and a fine grid
over continuous split ratios) for `n=1` (closed form, by hand) and `n=2`
(script, 150+ random pairs plus targeted points including the certified
geometric optimum `A_2=(4/7,2/7,1/7)`, which correctly returned `V=4/7`).
Result: **zero concavity violations found** — every tested midpoint had
`V(mid) ≥ avg(V(endpoints))`, including near-degenerate and highly skewed
configurations. This is new, independent evidence (not just the explorer's)
that the round-1 falsification does not reproduce under the correct
sorted-descending domain and exact game value.

---

## 1. geometric-dominance-construction — advance

**Verdict: CHANGES REQUESTED.**

Sound continuation of certified round-2 work (Lemma 1, Prop A, Lemma F1,
Lemma S all reused correctly, no re-litigation). The new mechanism (Lemma V:
LP vertex-extremality reducing a continuum of split ratios to finitely many
degenerate/tie configurations; Lemma W: wasted-mark domination) is a
legitimate, standard technique — "a piecewise-linear function on a compact
convex polytope attains its extremum at a boundary/tie-breakpoint" is correct
and matches the KB's piecewise-concavity family of arguments. Not circular:
Lemma V does not assume the conclusion, it only reduces the search space.

Issues:
- Lemma V's "extreme point" characterization needs to explicitly include
  interior tie-hyperplanes (rank-order ties between original and split
  pieces), not just the polytope's geometric vertices (piece degenerating to
  0) — the outline states this but the builder must not silently drop the
  tie-hyperplane case, since that's exactly where the harder configurations
  (the "doubling family") live.
- Lemma W is only sketched for "smallest piece → top piece"; the outline
  itself flags (correctly, in Watch out for) that it must be proved for a
  mark on ANY piece, and that "current smallest" is not fixed across the
  induction as pieces split. This is a real, not yet closed, gap — keep as
  open gap, do not let the builder assume it by analogy to Lemma F1's
  one-case argument.
- The "doubling family dominates" claim remains numeric-only (n≤5); the
  peel-induction's case split by rank-of-injected-piece `r` is unworked.

No case-coverage omission: k=0,1 closed already; the outline's plan reaches
k≥2 and simultaneous tail-splitting, i.e. all remaining cases, not a subset.

## 2. recursive-embedding-induction — advance

**Verdict: CHANGES REQUESTED.**

Also sound continuation (Lemma 1, G0, G1, Lemma 3 correctly imported).
Genuinely distinct mechanism from #1 — direct recursive induction with an
enriched (value, rank-position) invariant, no LP-vertex step — legitimately
respects the certified negative result (merge-by-sums counterexample): every
step is required to track `r`'s rank, not just its value.

Issues:
- Lemma R's three regimes (dominates / interior / negligible) are stated but
  none of the three rank-shift computations are done — this is the entire
  content of the approach and is still 100% open.
- Multiple simultaneous injected pieces (more than one "foreign" mark off
  the self-similar chain) is explicitly unreduced to the single-injection
  case — flag this as still open, not implicitly assumed away.

Overlap watch: this approach and #1 now both target the identical residual
gap (k≥2 lower bound with tail-splitting) using structurally similar
"peel one mark, carry position" machinery (as the outline itself admits).
This is the shared-gap-plateau risk CLAUDE.md calls out. I am NOT cutting
either yet — real technique divergence exists (LP-extremality vertex
reduction vs. direct case-split induction) and both made independent,
verified progress in rounds 1–2 (closing k=0, k=1 by different routes) —
but if BOTH stall on the same doubling-family/Lemma-R-case-(b) computation
again next round with no new lemma closed, that will be the "stuck 3+
rounds" trigger and the next outliner must replace one of them with a
genuinely different framing for the lower bound (not another peel variant).

## 3. universal-adversary-strategy — advance

**Verdict: CHANGES REQUESTED.**

Sole approach on the upper-bound-for-arbitrary-configs half, essential for
ever reaching `solved`. Lemma PEEL's proof sketch is correct and easy: since
`A` is sorted, `p_1,p_2` unconditionally dominate any refinement of the tail
(no extra hypothesis needed), so they occupy global ranks 1,2 and the tail's
ranks all shift by the same even amount (2), preserving parity — this is the
same mechanism as the certified DOM/HALVE lemmas, correctly specialized.

Issues (both explicitly self-flagged by the outline, good sign):
- The exhaustiveness argument for the 3-way case split (`p_1≥S`; `p_1<S,
  p_1≥2p_2`; `p_1<2p_2`) is correctly total (`p_1<S and p_1≥2p_2` can
  coexist, `p_1<2p_2` is the complement) but needs the boundary ties
  (`p_1=S`, `p_1=2p_2`) explicitly assigned to one branch, not silently
  dropped.
- The termination argument has a real bug risk the outline itself catches:
  the PEEL branch decreases `m` but leaves `r` fixed, so a naive induction
  "on `n`" or "on `r`" alone does NOT terminate — it must be nested
  (induct on `m` first, with `r` fixed, inside an outer induction on `r`,
  or a genuine well-founded combined order). This is correctly flagged as
  an open gap to fix, not swept under "it follows" — good, but it is not
  yet fixed, so this stays CHANGES REQUESTED, not APPROVE.
- Step 5's homogeneity/rescaling argument (`C(r') = c(r')`) is asserted by
  analogy to DOM/HALVE/PEEL being linear, but the precise induction
  structure combining it with the (m,r) termination fix is not spelled out.

## 4. majorization-smoothing — revise

**Verdict: CHANGES REQUESTED (not RETHINK), conditional on Step 0 being
executed for real.**

This is the approach I scrutinized hardest per the dispatch instruction,
since round 1 falsified an earlier "Lemma C" (`V(mid)=0.52 < avg 0.525`) and
round 2's outliner tried to resubmit that exact falsified version unchanged
(correctly re-killed).

Diff check: the on-disk file `approaches/majorization-smoothing.md` is
byte-identical to the round-1 commit (`git diff` empty) — but this is
because it was never built (killed both round 1 and round 2 before any
builder touched it), not because this round's outliner is silently
resubmitting the same content: the outliner's actual proposed skeleton (in
`/tmp/round-3/proof-outliner.md`) is materially different from the old
Lemma C:
- Old Lemma C: bare assertion "Xiang Yu's optimal use of his n splits is to
  perform them all on the single largest piece," offered without resolving
  the inner continuous-optimization-per-type step — this is exactly the
  gap that likely caused the false concavity claim.
- New Lemma C': explicitly requires solving the INNER minimization over
  continuous split ratios FIRST, for each fixed discrete type, and only
  then checking whether the resulting function of `p` is genuinely affine
  (not just piecewise-affine with hidden internal kinks) — with an explicit
  instruction to refine the type further if it isn't. This directly targets
  the subtlety a bare "V is concave because it's a min of linear things"
  claim would have glossed over.

I independently ran the Step 0 reconciliation myself (not just relying on
the explorer): exact-`Fraction`, sorted-descending domain, true brute-force
game value, `n=1` (closed form: slope 1 on `[1/2,2/3]`, slope −1/2 on
`[2/3,1]`, single downward kink at the certified optimum `2/3` — matches
`c(1)`) and `n=2` (150+ random pairs, zero violations, plus the certified
optimum point returning exactly `4/7 = c(2)`). The round-1 falsification does
NOT reproduce under the correct domain/exact value — strong evidence it was
an artifact of an unsorted or approximate computation, not a genuine
counterexample to the corrected claim. This is a genuinely different
mechanism this time, not a relabeled resubmission — approve for building,
but:

Mandatory condition (must be enforced, not optional): the builder MUST
perform and WRITE UP Step 0 explicitly in the approach file — show the
reconciliation numbers, state precisely what was different about round 1's
falsifying computation (domain/sortedness/exactness), before writing any
later step as if concavity is established. If the builder's own Step-0
check reproduces a violation, the correct action is to stop and report
RETHINK immediately, not to keep building around it.

Other issues: Step 2's type-refinement procedure (showing it terminates in
finitely many genuinely-affine pieces) and Step 4's general-`n` kink system
are both fully open — this is a large, unstarted amount of work; realistic
expectation is partial progress this round, likely at most n=1–2 closed
formally, not a full solve.

Since this file was never registered (previously RETHINK'd both rounds),
register it now.

---

## Diversity assessment

Four live approaches, two genuinely distinct half-proofs (lower bound:
geometric-dominance-construction + recursive-embedding-induction, sharing a
gap but differing in mechanism; upper bound: universal-adversary-strategy,
sole owner) plus one attempt at a unifying alternative framing that could
close both halves at once (majorization-smoothing). This matches CLAUDE.md's
guidance to add a genuinely different framing when the lower-bound field
risks a shared-gap plateau. No approach here is a fragment of another split
across slugs — each targets a whole, well-defined half (or, for
majorization-smoothing, the whole) of the true minimax value; this
bifurcation is inherent to a minimax problem, not an artificial split.

Watch (carried forward + new): if geometric-dominance-construction and
recursive-embedding-induction both fail to close a new lemma next round
(i.e., stall again on the same doubling-family/Lemma-R computation), that is
the trigger to drop one and replace it with a different lower-bound framing.

---

## Ranking

`equalization-potential-bound` remains registered from round 1 (not in this
round's build set, kept in the population as a diversity/negative-result
anchor per round 1 decision). Registering `majorization-smoothing` as new.
Anchoring comparisons: the three advancing approaches all made verified,
non-overlapping progress last round (narrowed gaps, zero regressions) so
rank them above the untouched equalization-potential-bound anchor; among the
three, universal-adversary-strategy is the sole owner of an entire
un-substituted half of the problem (higher marginal value per unit of
future progress) and its two certified lemmas (DOM, HALVE) are more general
(arbitrary tail shape) than the k=0/1-only progress of the other two, so it
edges ahead; geometric-dominance-construction (Elo 1542, LP-vertex
mechanism, slightly further specified case machinery) edges recursive-
embedding-induction (Elo 1520, same gap, negative result is valuable but is
a "ruled out a wrong path" contribution rather than new positive ground);
majorization-smoothing is a fresh entrant with real but preliminary evidence
(my own reproduction), so it's compared as a strong newcomer against the
weakest anchor (equalization-potential-bound, stale, untouched two rounds)
and against the established field, landing mid-pack pending its own
concrete lemma closure next round.

I called `register_approach` for `majorization-smoothing` and
`update_ranking` with the following comparisons:
- universal-adversary-strategy beats equalization-potential-bound (opened
  and closed a whole new half of the problem; the anchor is stale/untouched
  two rounds)
- geometric-dominance-construction beats equalization-potential-bound (two
  rounds of verified case closures vs. a stale conditional negative result)
- recursive-embedding-induction beats equalization-potential-bound (same
  reasoning)
- geometric-dominance-construction vs recursive-embedding-induction: draw
  (identical remaining gap, comparable rigor, genuinely different but
  equally-progressed mechanisms)
- universal-adversary-strategy beats geometric-dominance-construction (sole
  owner of an entire unaddressed half of the problem; its certified lemmas
  are more general — arbitrary tail shape vs. geometric-only)
- majorization-smoothing beats equalization-potential-bound (fresh,
  independently-reproduced positive evidence vs. a stale conditional
  negative result)
- geometric-dominance-construction beats majorization-smoothing (established,
  multi-round verified progress vs. majorization-smoothing's still-unstarted
  Step 2/4 work, despite the promising Step-0 reconciliation)

---

build set: universal-adversary-strategy, geometric-dominance-construction, recursive-embedding-induction, majorization-smoothing
