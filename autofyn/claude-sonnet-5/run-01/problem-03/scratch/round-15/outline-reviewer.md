# Outline review — round 15, imo-2026-03

## Context recap
Only one gap remains for the whole problem: Claim PTBI's Case C
(`p_1<Σ(A)/2`, general `m≥4`) — Lemma SLACK-COVER (a joint
covering-plus-recursive-value subset-match existence statement inside
the `(marks,|A|)` induction). The lower bound, `m=1..3`'s upper bound,
and `solve2`'s corrected mark-accounting (Lemma FREE-TIE-REDUCTION) are
all fully closed/certified and NOT reopened here. Three non-constructive
averaging/secondary-statistic routes to this same gap are already proven
dead (`minimax-mixed-duality`, `case-c-secondary-extremality`,
`case-c-slack-covering`).

## 1. `universal-adversary-strategy` (revision — "Round 15 plan" section)

**Verdict: APPROVE.**

This is a legitimate revision of the same live slug, still targeting the
whole problem via the same closed-form-recursion route, now attacking
the sole open gap by a genuinely constructive mechanism distinct from
the three refuted averaging attempts.

Checked:
- **Step 1 gate, Lemma MARKS-MONO** (`solve2(A,k)` non-increasing in
  `k`): I independently stress-tested this claim with a coarse
  from-scratch simulation (a simplified recursive splitting game, `k=1`
  vs `k=2`, 20 random `m=3,4` instances, coarse grid search over split
  ratios) — zero violations, consistent with the trivial argument the
  plan gives ("do nothing further" is always an available fallback, so
  the candidate set at budget `k+1` weakly dominates the set at `k`).
  This is a cheap, almost-certainly-true monotonicity fact and a sound
  thing to nail down first, since (per the plan) it would decouple the
  joint covering+value "AND" into two independent, separately-tractable
  statements. Good sequencing.
- **Choice of test witness**: the plan explicitly targets the small
  `m=4` witness `T=(0.20,0.15,0.12,0.08)` instead of the round-12 `m=8`
  witness for the hand-verification in Step 2. I read
  `/tmp/round-15/math-explorer-termination.md` in full — its diagnosis
  (the `m=8` stall is a branching-factor/complexity artifact of the
  newly-widened any-subset Move 2, and that witness's winning move was
  already shown in round 12 to be an ordinary contiguous match, so it
  tests nothing SLACK-COVER doesn't already get from the `m=4` witness)
  is sound and correctly distinguishes "scalability-only stall" from
  "mathematical necessity" — this is the right target to spend effort
  on, not a dodge.
- **Steps 2/3**: correctly scoped as gaps, not asserted as done. Step 2
  (the aimo-0292-style scalar covering induction) is honestly flagged as
  an adaptation, not a citation — consistent with the standing rule
  (memory rule 18) that aimo-0292's mesh argument does not transfer
  wholesale (bounded-mesh hypothesis false here) and must be re-derived.
  Step 3 (exchange-argument fallback) reuses only already-certified Fact
  0/Lemma TIE-NECESSARY machinery, not new unproven imports.
- **Explicit "out of scope" list** correctly excludes re-litigating the
  three already-dead averaging/pigeonhole mechanisms.

No circularity, no hand-waved lemma without a mechanism, no repeat of a
recorded dead end. Build as planned.

## 2. `defect-hall-deficiency` (new slug)

**Verdict: APPROVE (register), with one added caveat for the builder.**

This is a genuinely different proof shape from every live/dead approach
so far: existence via defect (König/Hall-deficiency) rather than a value
bound via averaging (the three already-refuted mechanisms) or an
inductive value construction (`universal-adversary-strategy`'s own
route). It targets the same whole problem end-to-end (Step 3 explicitly
reuses the already-proved lower bound + Lemma THRESHOLD-REDUCTION to
assemble the full two-sided theorem if Steps 1–2 close) — not a
disconnected slice, consistent with the established pattern (memory rule
19: multiple approaches attacking the same named lemma via genuinely
different proof shapes is legitimate, not the single-gap trap).

Checked crux `aimo-0341` directly (grepped
`past_crux_moves_database.json` rather than trusting the outline's
paraphrase, per memory rule 18): the crux's actual defect-Hall argument
is about covering a product grid by axis-fixing subgrids (peel
max-deficiency subgrid-set, match remainder to axes via Hall, build the
missing point coordinate-by-coordinate) — a **1-1 assignment/SDR**
structure. This problem's actual need is closer to **subset-sum /
subset-cover** (does some subset of the tail sum to/near a target `p_1`,
combined with a recursive value bound on the leftover), which is a
different combinatorial shape from a straightforward 1-1 bipartite
matching. The outline is aware this is an adaptation, not an import, and
correctly marks Steps 1–2 as unproved gaps rather than asserting the
Hall machinery applies as-is — but the mandatory Step 0 gate as
currently worded only checks that a chosen bipartite-graph *encoding* has
bounded deficiency; it should **also** explicitly verify that encoding
is representationally faithful (i.e., that a Hall-type matching in the
chosen graph actually *implies* the needed subset-match, and not just
that *some* graph can be drawn) before spending effort on a general
deficiency bound. This is CHANGES REQUESTED in spirit but folded into
Step 0 as an added item, not a reason to RETHINK the whole approach —
the plan's own gating discipline (mandatory numeric gate before general
proof effort, explicit "dead on arrival if the gate fails" instruction)
already matches the standard this run holds new approaches to
(`case-c-slack-covering`, `relaxed-adversary-transfer` precedent).

Also confirmed per memory rule 13 (Hall existence ≠ numeric identity):
the skeleton's Step 2 explicitly separates "bounded deficiency"
(cardinality fact) from "value bound on the leftover" (the load-bearing
new content), calling it out as "the crux of the whole approach and not
yet done" — this is exactly the right decomposition, not a conflation.

Register this slug.

## Field-wide notes

- `recursive-embedding-induction` (Elo 1675) and
  `geometric-dominance-construction` (Elo 1634): both fully served their
  purpose (lower bound closed, `verified-milestone` / narrower
  cross-check respectively) — no further work needed or requested this
  round; kept in the population for ranking continuity, not in the build
  set.
- `case-c-slack-covering`, `universal-adversary-strategy-exact-tie`,
  `minimax-mixed-duality`, `case-c-secondary-extremality`,
  `relaxed-adversary-transfer`, `majorization-smoothing`: all dead/retired,
  correctly not rebuilt.
- `equalization-potential-bound`, `potential-averaging-bound`: stale
  partials with no active leverage; not competitive for the build set.
- **Diversity check**: with `defect-hall-deficiency` added, the field now
  has two genuinely distinct live mechanisms on the sole open gap
  (constructive joint-induction vs. matching/deficiency existence) plus
  a designated fallback (exchange argument) inside the first — this
  satisfies the plateau-break mandate without fragmenting the proof into
  disconnected slices.

## Ranking actions taken
- Registered `defect-hall-deficiency` (new).
- Ran `update_ranking` with:
  - `universal-adversary-strategy` beat `defect-hall-deficiency` (established, concrete progress this round vs. untested skeleton)
  - `defect-hall-deficiency` beat `case-c-slack-covering` (live novel mechanism vs. proven dead-end)
  - `universal-adversary-strategy` drew `recursive-embedding-induction` (both top-tier: one owns the only remaining gap, the other fully closed its own half)
  - `defect-hall-deficiency` beat `universal-adversary-strategy-exact-tie` (fresh distinct mechanism vs. retired/duplicative)

This clears `stale` on `universal-adversary-strategy` and anchors the
newcomer against both an established leader and a dead sibling, per the
standing anchoring rule.

## Build set

build set: universal-adversary-strategy, defect-hall-deficiency
