# Outline review — round 10 (imo-2026-03)

Reviewed: `/tmp/round-10/proof-outliner.md` (3 revisions, no new slug opened this
round). Cross-checked against `results/imo-2026-03/current.md` (Status:
partial, round-9 state) and the three approach files
(`recursive-embedding-induction.md`, `geometric-dominance-construction.md`,
`universal-adversary-strategy.md`) plus the certified lemma this round's plans
build on (`lemmas/tree-bound-residual.md`, `lemmas/two-block-residue-close.md`,
`lemmas/ptbi-threshold-reduction.md`, `lemmas/pair-value.md`).

## recursive-embedding-induction — revise — APPROVE (to build)

Target: generalize Lemma TREE-BOUND-RESIDUAL / Sub-lemma ODD from "at most one
impure node in the whole forest" to "any finite number of impure nodes,
anywhere." This is the correct next target — it is precisely the multi-cluster
gap the round-9 reviewer flagged as the last unclosed piece of gap (b), and
the plan builds strictly on already-certified machinery (Lemma D-BOUND,
Lemma D-INSERT), not new atomic tools.

Checked the case enumeration against the actual proof structure in
`tree-bound-residual.md`: the existing induction peels the top level and
splits into "impurity strictly below top level" vs. "impurity at top level"
(Case C). With the IH restated to allow arbitrarily many impurities in the
remainder (step 1), a single top-level impurity plus arbitrarily many buried
deeper reduces immediately to the existing recursion — no new case needed
there. The one genuinely new combinatorial configuration not reachable by
peeling is **p ≥ 2 impurities landing simultaneously at the current top level
of the same forest pass** (two or more of the `r` trees rooted at τ_1 are each
independently impure at once) — this is exactly what the outline's step 3
isolates as the new case, and I could not find a missing sub-case (single
impurity anywhere else composes correctly with the restated IH; mixed
top+below-level impurities reduce to "one impurity at top, IH handles the
rest" since the IH no longer restricts the remainder's own impurity count).

Soundness of the proposed mechanism (multi-pair insertion, largest-companion-
first): this is flagged, correctly, as NOT yet proved — only numerically
evidenced (21,875+ configs, zero violations per round-9). The plan is honest
about this being the one open piece, not hand-waved as "then it follows." I
did not find an obvious flaw in the induction-on-p framing (base case p=1 is
already the certified Case C; each step p→p+1 is one fresh D-INSERT
application on the next-largest surviving companion), but the boundary case
where companions tie (c_(i) = c_(i+1)) genuinely needs to be checked in the
written proof, not asserted from numerics — the outline correctly flags this
as a case to cover, not skips it.

One thing to insist on for the build: **step 2 ("no hidden use of the ≤1
restriction") must actually be verified line-by-line in the written proof**,
not merely asserted from the explorer's read — the outline correctly labels
this an open gap needing rigorous verification, but the builder must not
skip it and treat it as already discharged.

Watch-out is correctly stated: do not resurrect the round-9 "virtual fully
split domination" mechanism (proven false, 159/600 violations) — the
plan's chosen route (direct re-induction via Case C's own toolkit) is the
right fix, not that shortcut.

No circularity, no skipped case, no recorded dead end repeated. APPROVE.

## geometric-dominance-construction — revise — APPROVE (to build, scoped as cross-check)

Target: same multi-cluster generalization via K-fold nested TWO-BLOCK
(threshold at decreasing tie-values v_1 > ... > v_K, recurse on the
remainder). Technically this mirrors the sibling's peeling structure at one
remove (threshold instead of forest-level) and reuses only the
already-certified Lemma TWO-BLOCK and Structural Lemma — no new atomic
machinery, consistent with how this approach has operated since round 8
(independent verification route, not independent theory).

The outline's own instruction is the right call: **use this round primarily
as a cross-check against recursive-embedding-induction's general theorem
rather than re-deriving a third independent full proof from scratch** — this
avoids duplicated effort on the identical target while still preserving the
value of two independently-agreeing mechanisms (which has been useful every
round since 8; no regression risk here). The K=2 first-then-generalize plan
is a reasonable scoping; the "cluster ownership of the two globally-largest
pieces" 2^K-ish casework is flagged honestly as bookkeeping, not new content,
which matches the K=1 Structural Lemma's actual proof shape.

No fatal flaw. APPROVE, with the explicit condition (already in the outline)
that this round's builder effort should be weighted toward verification of
recursive-embedding-induction's construction on the shared witnesses rather
than a full from-scratch K-fold proof, unless the sibling stalls.

## universal-adversary-strategy — revise — APPROVE (to build)

Target: close Claim PTBI's Case C (p_1 < Σ(A)/2) for general m ≥ 4 — the sole
remaining upper-bound gap. Two candidate routes offered: (1) the Fact-0
evensum-maximization reformulation, (2) a Hall-deficient-set-deletion
existence argument adapted from crux aimo-0063. Both are genuinely untested
this round, honestly marked as open, not overclaimed.

This is the correct target (matches current.md's stated single remaining
upper-bound gap) and correctly avoids the round-9-falsified "greedy
largest-first subset selection" mechanism (74% violation rate) — explicitly
called out as a watch-out, good.

The plan's own gating discipline is sound and matches the standing rule
("always numerically test a claim before trusting it as a lemma mechanism"):
step 2 explicitly says to test the Fact-0 reformulation numerically *before*
committing further proof effort, and step 3's Hall's-theorem route correctly
flags the caveat that the underlying object may be a subset-sum/hyperedge
structure rather than a literal 1-1 matching (this was the PTBI explorer's
finding this round, not assumed) — so classical Hall's theorem must not be
cited without first verifying the formalization is actually a bipartite 1-1
matching problem. This flags a real risk correctly rather than glossing over
it.

No circularity, no case skipped (m=4 hand-worked first, general m by
induction, simultaneous-donor-action boundary explicitly named as a case to
handle rather than special-case away). APPROVE.

## Cross-approach diversity check

The two lower-bound approaches (recursive-embedding-induction,
geometric-dominance-construction) still target the identical residual
sub-case (multi-cluster generalization of gap (b)) via genuinely distinct
mechanisms (forest/tree induction vs. two-block threshold recursion) — this
is legitimate cross-verification per the standing rule (round 5), not the
single-gap trap, since both mechanisms are independently plausible and any
disagreement between them would be a real signal. universal-adversary-strategy
attacks the wholly separate upper-bound half, so overall field diversity
across the run remains adequate (one shared-technique-pair for the lower
bound, one independent line for the upper bound) — no new framing needed this
round; the field has not stalled on one wall for 3+ rounds on the *same*
gap (the lower-bound gap has narrowed every round since round 7, the
upper-bound gap narrowed as recently as round 9 with m=3 fully closed).

## Ranking

Registered: no new slugs this round (all three revisions keep existing
slugs, already in the population).

Ranked the three revised approaches head-to-head, anchored to round-9
outcomes: universal-adversary-strategy fully closed a complete sub-case
(m=3's general upper bound, unconditionally) this round, a more decisive
result than the siblings' still-caveated single-cluster closures (both still
carry the same open multi-cluster gap) — ranked universal-adversary-strategy
above both siblings. recursive-embedding-induction and
geometric-dominance-construction are ranked as a draw — identical scope,
independently cross-verified, same open caveat, genuinely different
mechanisms.

```
update_ranking(imo-2026-03, [
  {winner: universal-adversary-strategy, loser: recursive-embedding-induction},
  {winner: universal-adversary-strategy, loser: geometric-dominance-construction},
  {winner: recursive-embedding-induction, loser: geometric-dominance-construction, draw: true}
])
```

Resulting Elo (stale cleared on all three): recursive-embedding-induction
1662.1, geometric-dominance-construction 1624.2, universal-adversary-strategy
1582.8 — geometric-dominance-construction and recursive-embedding-induction
remain the two highest-rated approaches overall (this round's single win for
universal-adversary-strategy narrowed the gap but did not overtake, consistent
with the sibling pair's larger cumulative track record: 8-9 rounds of
progress vs. universal-adversary-strategy's still-open general-m Case C).

## Build set

All three approaches pass review; no RETHINK this round, no cuts. Build all
three, with geometric-dominance-construction's effort explicitly weighted
toward cross-checking recursive-embedding-induction's general multi-cluster
theorem rather than an independent full K-fold derivation, per the outline's
own instruction.

build set: recursive-embedding-induction, geometric-dominance-construction, universal-adversary-strategy
