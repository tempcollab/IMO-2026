# Proof-outliner report — round 9 — imo-2026-03

## Status
partial

## What changed this round

Read `current.md`, all 8 approach files, and the three round-9 scouting
reports (`math-explorer-crosstie.md`, `math-explorer-ptbi.md`,
`math-explorer-altframing.md`). No new proof was written this round (that
is the builders' job); this round's outliner work is: (1) revise the three
live approaches with concrete, skeletoned next-step plans grounded in the
explorers' findings, (2) formally recommend retiring the stalled
`minimax-mixed-duality` slug, (3) decide **not** to open a new approach
slug (rationale below).

### Revisions made (skeletons appended, no proof claims)

- **`recursive-embedding-induction`** — appended "Round 9 plan: extend
  Lemma TREE-BOUND to forced-residual (non-anchor) leaves," targeting
  gap (b)'s last sub-case (minority-part, deep-bracket residue). Skeleton:
  reinterpret the residual companion value `c = t_i-t_j =
  \sum_{l=i+1}^j t_l` as a partially-collapsed subtree, generalize
  Sub-lemma ODD's forest induction to admit one "forced-residual" node
  standing in for its own virtual sub-forest, and prove a **domination**
  inequality (`D(\text{residual config}) \ge D(\text{virtually-split
  config})`) rather than a fresh bound — reusing D-BOUND/D-INSERT. Flagged
  the honest risk explicitly: the direction of the domination inequality
  is not obviously safe and must be checked on concrete instances before
  generalizing. This directly follows both explorers' top recommendation
  (extend TREE-BOUND's mechanism rather than retry the confirmed-dead
  perturbation/exchange route).
- **`geometric-dominance-construction`** — appended "Round 9 plan: second,
  independent route to the minority-part residue sub-case," a genuinely
  different mechanism (direct two-term D-BOUND split at the winning
  endpoint) from `recursive-embedding-induction`'s forest-extension, per
  CLAUDE.md's standing reconciliation requirement for this shared gap.
  Includes an explicit fallback: if the crude D-BOUND estimate is too
  weak, report inconclusive and defer to the sibling approach's finer
  argument rather than force a false claim.
- **`universal-adversary-strategy`** — appended "Round 9 plan: two
  targets." Target 1 (quick win): finish `m=3`'s Case C residual region
  `p_1<\Sigma/2 \wedge p_3>\Sigma/7` as a bounded 2-parameter
  piecewise-affine optimization — the explorer's 20,000-trial + grid probe
  found zero violations of the existing menu there, so this is genuinely
  mechanical, not a new construction. Target 2 (the real obstruction):
  formalize **Lemma SUBSET-DOM**, generalizing BLOCK-RECURSE from
  prefix-matching to arbitrary-subset matching via **Hall's marriage
  theorem** (already in `knowledge_base.md`), motivated by the concrete
  `m=5` witness `A=(12,6,5,4,2)/29` that **falsifies** the current
  certified menu by exactly `1/899` — recorded as the sharp new
  obstruction (gap-widening, not narrowing) per the explorer's finding.
  Flagged the load-bearing open technical risk precisely: BLOCK-RECURSE's
  contiguous-rank-occupancy step used sortedness of a prefix, which does
  **not** hold for an arbitrary subset `T` (the witness's own leftover
  `\{p_1,p_3\}` is not dominated by `\min(T)`), so the rank-occupancy
  identity must be re-derived, not assumed, for general `T`.
- **`minimax-mixed-duality`** — Status changed to `RETHINK (recommended
  for retirement, round 9)`. Two consecutive rounds (6, 7) with no
  independent proof leverage, not revived in round 8, and none of this
  round's three scouting reports found a new dual object for it. Its two
  certified contributions (Lemma SANDWICH, witness cross-checks) remain
  available in the shared lemma cache to `universal-adversary-strategy`
  regardless of this slug's fate. Recommend the outline-reviewer drop it
  from the build set this round (not delete the file); revivable later if
  a genuinely new `A`-independent certificate object surfaces.

### Decision: no new approach opened this round

Considered opening a new slug for the "unified forced-residual" idea the
alt-framing explorer flagged (structural kinship between gap (b) and PTBI
Case C — both are "value forced by pinned siblings" obstructions). Decided
**against** a new slug: per CLAUDE.md, a slug must be a whole rival attempt
at the problem, and a unifying *lemma* is exactly the kind of object that
belongs in the shared `lemmas/` cache, reusable by whichever of
`recursive-embedding-induction` or `universal-adversary-strategy` proves it
first — opening a fourth slug for the same terrain the other three already
cover would violate the "don't split a proof, don't duplicate a wall"
principle, not satisfy it. Instead, both relevant approach files' Round 9
plans above are written so that if either builder notices the technique
transfers to the other gap, they should say so explicitly and propose the
lemma be extracted to `lemmas/` for cross-approach reuse — flagging this
for the outline-reviewer and next round's builders rather than
pre-committing to a new slug.

Also considered: is `m=3`'s Case C task big enough to deserve its own
slug? No — it is a sub-task inside `universal-adversary-strategy`'s
existing target (Claim PTBI), not a distinct route to the whole problem;
keeping it inside that approach avoids a single-gap-trap slug that would
die if `universal-adversary-strategy`'s general framing turns out to be
wrong.

## Field of approaches (for the outline-reviewer)

- `recursive-embedding-induction` — **advance** (revised: forest-extension
  plan for gap (b)'s last sub-case).
- `geometric-dominance-construction` — **advance** (revised: independent
  D-BOUND-split route to the same sub-case, for reconciliation).
- `universal-adversary-strategy` — **advance** (revised: `m=3` quick win +
  Lemma SUBSET-DOM/Hall's-theorem plan for the newly-widened general-`m`
  gap).
- `minimax-mixed-duality` — **retire from build set this round**
  (RETHINK, recommended retirement; lemmas already extracted/reusable).
- `relaxed-adversary-transfer` — no change (confirmed clean dead end,
  round 7; not re-attempted).
- `potential-averaging-bound` — no change (partial negative-progress
  record; not touched this round).
- `majorization-smoothing` — no change (confirmed dead end; kept as
  negative-result record only).
- `equalization-potential-bound` — no change (stagnant since round 1; not
  touched this round).

build set: recursive-embedding-induction, geometric-dominance-construction, universal-adversary-strategy
