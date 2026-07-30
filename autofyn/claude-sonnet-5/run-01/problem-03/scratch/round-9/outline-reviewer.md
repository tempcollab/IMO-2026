# Outline-reviewer report — round 9 — imo-2026-03

## Summary of what was checked

Read `CLAUDE.md`, `results/imo-2026-03/current.md`, `/tmp/round-9/proof-outliner.md`
in full, and the actual on-disk approach files
(`recursive-embedding-induction.md`, `geometric-dominance-construction.md`,
`universal-adversary-strategy.md`, `minimax-mixed-duality.md`) — specifically
the "Round 9 plan" sections each was described as adding, verified directly
against the file text (not just the outliner's paraphrase), plus the
underlying scouting report `/tmp/round-9/math-explorer-ptbi.md` that
motivates the `universal-adversary-strategy` plan. No proof was written this
round (planning-only round, as the outliner itself states); this review
judges whether the plans are sound enough to hand to a builder.

## Per-approach verdicts

### `recursive-embedding-induction` — CHANGES REQUESTED (plan approved, proceed with the flagged check first)

The Round 9 plan (lines 1709–1765 of the file) targets gap (b)'s last
sub-case (minority-part, external-anchor residue) via a **domination**
claim: `D(residual config) ≥ D(virtually-split config)`, reducing to the
already-certified Sub-lemma ODD one recursion level deeper. This is the
right shape of argument (residual value `c = t_i - t_j` really is exactly
the sum of the missing anchors `t_{i+1},…,t_j`, so "what if it had been
fully split" is a legitimate comparison object, not an invented one).

**Adversarial check performed**: the plan itself explicitly flags — in its
own words — that "the direction of the domination inequality is not
obviously safe" and mandates the builder verify it on ≥2 concrete instances
before generalizing. This is exactly the right caution (per the standing
memory rule to take self-flagged circularity/validity risk seriously) and I
independently agree the direction is non-obvious: un-splitting simultaneously
changes (i) which ranks the leftover node occupies in the sorted merge and
(ii) the sign it contributes to the alternating sum, so a naive "splitting
only ever adds value" intuition (true for D-INSERT's *duplicated-pair*
insertion) does not obviously transfer to "a single un-split residual node
vs. its collapsed children," which is a different structural operation. This
is not a fatal flaw — it is an appropriately-scoped open risk with a
concrete verification gate attached (the file names two witnesses, `n=4`
symmetric tie and `n=6` external-anchor-snap, to test first). Requiring
the builder to check both directions numerically before writing the general
induction is the correct discipline; approve the plan on that condition.

**Issue to fix while building**: step 4's "Conclude" is currently written as
if steps 2–3 already establish the inequality — the builder must not
present the domination claim as proved until the concrete-instance check in
the "Honest risk flagged" paragraph has actually passed; if it fails on
either witness, this route must be reported as a negative result (mirroring
`geometric-dominance-construction`'s own explicit fallback), not silently
patched.

### `geometric-dominance-construction` — CHANGES REQUESTED (plan approved)

The Round 9 plan (lines 1544–1586) is a genuinely different mechanism from
its sibling — a direct two-term D-BOUND split at the endpoint value, rather
than a tree-reachability comparison — attacking the *same* residual
sub-case. This is legitimate parallel exploration under the standing memory
rule (distinct mechanisms, same target, positive evidence the target gap is
real and narrow), not the single-gap trap: each file is still a complete,
standalone attempt at the whole lower bound, differing only in how they
close the last narrow sub-case.

Good practice already baked into the plan: it explicitly names its own crude
step (D-BOUND only uses `max(Y)`, discarding structure) as the likely
failure point and commits to reporting "negative/inconclusive" and
deferring to the sibling route rather than forcing a false claim (step 4).
It also correctly mandates cross-checking the final inequality against the
sibling's numeric witnesses (step 3) — required reconciliation, not
optional. No issues beyond what the file already self-flags; approve as
written.

### `universal-adversary-strategy` — CHANGES REQUESTED (plan approved, both targets sound)

Verified the round-9 explorer's claimed falsifying witness directly:
`A=(12,6,5,4,2)/29`, `m=5`, budget 4. Reproduced the explorer's construction
by hand — halve `p_1` (24/58 → 12/58,12/58), halve `p_3` (10/58 → 5/58,5/58),
split `p_2` (12/58) into fragments exactly matching `p_4,p_5` (8/58,4/58 in
58ths) — giving sorted multiset `12,12,8,8,5,5,4,4` (units of 1/58),
`oddrank = 12+8+5+4 = 29`, i.e. exactly `1/2 < c(4)=16/31`, using only 3 of
the 4 available marks. This is a real, checkable construction the existing
certified menu (BLOCK-RECURSE restricted to sorted-prefix matches) cannot
express, since the leftover `{p_1,p_3}` is not dominated by
`min{p_4,p_5}=p_5` — confirms the plan's diagnosis is correct, not
overclaimed.

**Target 1** (finish `m=3`'s Case C residual region) is a bounded algebra
task on an already-identified two-candidate min, appropriately scoped as a
"quick win," and the explorer's own 20,000-trial + grid probe found zero
violations — reasonable to proceed.

**Target 2** (Lemma SUBSET-DOM via Hall's theorem) is the substantive new
direction. The plan is honest about the precise open risk: BLOCK-RECURSE's
rank-occupancy identity used sortedness of a *prefix* to get contiguity,
and this genuinely fails for an arbitrary subset `T` (confirmed above — the
witness's own leftover is not dominated by `T`'s minimum). The plan
correctly separates two distinct sub-tasks that must not be conflated: (i)
Hall's theorem proves *existence* of a valid assignment (a matching
problem), and (ii) the rank-occupancy identity for the resulting merged
multiset is a *separate* combinatorial fact that does not follow from Hall's
theorem and must be re-derived from scratch for non-contiguous `T` (step 3,
correctly flagged as "the load-bearing new content," with an honest
fallback to a narrower claim if the general identity fails). This is sound:
Hall's theorem is the right tool for existence, but the plan does not
mistake it for a proof of the harder rank-identity — no circular reasoning
here. Approve, with the requirement (already in the plan) that the builder
report a narrowed/failed claim honestly rather than assert the general
identity if step 3 does not go through.

### `minimax-mixed-duality` — retirement confirmed, RETHINK / drop from build set

Checked the file's own history directly: round 6 opened it as a genuinely
different proof shape (mixed-strategy/LP duality); round 6's honest result
was "no shortcut, but Lemma SANDWICH surfaced as a byproduct"; round 7's
gate check again converged to "no `A`-independent certificate, reduces to
`universal-adversary-strategy`'s casework" (`current.md` lines 210–228,
confirmed against the file's own "Round 7 update" section, lines 262+, and
its "Full proof" placeholder at line 428 restating the same conclusion);
round 8 had no build at all (confirmed: no round-8 entry exists in the
file's own "Approaches tried," and `current.md` records no round-8 activity
for this slug). None of this round's three scouting reports surfaced a new
dual object for it either. Two consecutive rounds of no independent
leverage, a third round with no revival, and a fourth round (this one) with
no new evidence — the retirement is justified exactly as claimed. Its
certified contributions (Lemma SANDWICH, cross-checks) remain reusable via
the shared `lemmas/` cache regardless of the slug's build status. Confirmed
RETHINK; drop from this round's build set (file kept, not deleted).

## Diversity check

The three build-set approaches are not a single-framing collapse:
`recursive-embedding-induction` and `geometric-dominance-construction`
target the *lower* bound's last sub-case via two independently-verified,
distinct mechanisms (tree-reachability/domination vs. direct D-BOUND split)
that both remain honest about their risk and have an explicit reconciliation
step; `universal-adversary-strategy` targets the entirely separate *upper*
bound (Claim PTBI, Case C) via a new matching/Hall's-theorem mechanism, not
previously used on this problem. This is a genuine two-halves split
(lower-bound vs. upper-bound), which the standing memory rule already
recognizes as legitimate structure, not the single-gap trap. No stalled
3+-round shared-wall pattern this round — the lower-bound sub-case has only
been convergently attacked for one round (round 8) plus this round's plans,
and the upper-bound side just got a genuinely new obstruction (the m=5
witness) and a genuinely new tool (Hall's theorem) rather than repeating a
stale mechanism.

## Ranking actions taken

- No new slugs registered (all three build-set approaches — plus
  `minimax-mixed-duality` — are already in the population from prior
  rounds; this round only added plan/skeleton text, no new approach).
- No `copy_approach` calls — the outliner did not request a branch, and I
  agree with its reasoning for not opening a 4th slug this round (a shared
  lemma belongs in `lemmas/`, not a new competing slug for terrain three
  existing approaches already cover).
- `update_ranking` called with 6 comparisons anchored to round-8 evidence
  (the last actual build outcomes, since this round was planning-only):
  `recursive-embedding-induction` vs `geometric-dominance-construction` —
  draw (both "advanced," consistent parallel routes to the same gap);
  `recursive-embedding-induction` and `geometric-dominance-construction`
  each beat `universal-adversary-strategy` (fuller/closer-to-closed gap-(a)
  and gap-(b) results vs. `universal-adversary-strategy`'s still-open
  Case C, now further complicated by this round's falsifying witness); all
  three live approaches beat `minimax-mixed-duality` (dead-end last
  outcome, per the standing anchoring rule). This clears the `stale` flags
  set by the round-8 review. Resulting Elo order: recursive-embedding-induction
  (1690) > geometric-dominance-construction (1638) > universal-adversary-strategy
  (1541) > minimax-mixed-duality (1445, dead-end, excluded from build set).

## Build set

All three live, non-retired approaches have sound, appropriately-hedged
plans for genuinely new content this round (not repeats of a dead end, not
circular, not overclaiming); dispatch one builder per slug.

build set: recursive-embedding-induction, geometric-dominance-construction, universal-adversary-strategy
