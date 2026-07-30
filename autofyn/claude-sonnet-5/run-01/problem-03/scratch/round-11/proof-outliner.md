# Round 11 — proof-outliner report

## Status
partial

## Recap: where the whole problem stands

The lower bound (`A_n` achieves `c(n) = 2^n/(2^{n+1}-1)`) is **fully
closed** (round 10) and must not be re-opened or re-attempted. The
**entire remaining gap for the whole problem** is
`universal-adversary-strategy`'s Claim PTBI Case C
(`p_1 < \Sigma(A)/2`), general piece-count `m \ge 4`, in the general upper
bound over arbitrary (non-geometric) Liu Bang configurations. `m\le3` is
fully closed. This round's three explorers
(`/tmp/round-11/math-explorer-hall.md`,
`/tmp/round-11/math-explorer-construction.md`,
`/tmp/round-11/math-explorer-altframing.md`) all scouted this single gap
from different lenses, per the assignment.

## Field of approaches this round

### 1. `universal-adversary-strategy` — REVISED (primary approach, live)

Appended a new "Round 11 plan" section to
`results/imo-2026-03/approaches/universal-adversary-strategy.md` with a
precise sub-goal, **Lemma MATCH-HALVE-EXISTS**, replacing the vaguer
"prove a Hall-type existence theorem" framing left over from round 10.

Key findings baked into the revision (full detail in the file, all sourced
from this round's explorers):

- The round-10 hard witness's true optimum
  (`A=(1826,1563,1520,1514,765)/7188`, `m=5`) is now **exactly
  reconstructed**: `match(p_1,p_2) + match(p_3,p_4) + match(p_5,r_1) +
  self-halve(p_5-r_1)`, giving `1199/2396` exactly, matching the round-10
  file's numeric value on the nose.
- **A clean, exact counterexample proves "always greedily match the two
  largest available values, never self-halve" is FALSE** — greedy matching
  alone gives `1921/3594 > c(4)`. Self-halving is a necessary, distinct
  move, not a fallback. Any Hall's-marriage-only existence argument (pure
  matching, no self-halve) is refuted before it's attempted.
- A literal transplant of `aimo-0063`'s Hall-deficient-set-deletion crux
  does **not** fit (fixed 0/1 compatibility graph + SDR existence vs. our
  continuous exact-value subset/fragment-matching problem with no natural
  graph) — both the Hall-lens and altframing-lens explorers independently
  reached this conclusion. Flagged in the revision: do not spend a round
  building "the" Hall graph.
- `aimo-0292` (peel-largest-block, solve smaller instance, reattach with
  additive slack) is the closest structural analogue, but needs new work
  adapting additive slack to the multiplicative target `c(m-1)\Sigma`.
- Round 10's own Step 3 fact (`g(v)` always `>c(m-1)\Sigma` at `v=0`) rules
  out any single-peel-then-bare-IH shape — the sub-goal explicitly warns
  against re-deriving that dead end.

**New sub-goal given to the next builder, with two concrete routes:**
- **Route A (primary, cheap to check first):** the round-11 explorer's
  reconstructed `m=5` construction (top-level pairs, with residuals fed
  recursively into deeper pairs/self-halves) is structurally similar to
  `recursive-embedding-induction`'s already-certified
  **Lemma TREE-BOUND-MULTICLUSTER** forest recursion (proved for the
  *lower*-bound side). The next builder's first task: state Case C's
  existence claim in the same forest/tree language and check whether the
  already-proved multiplier bound (or its dual) directly forces
  `oddrank(B)\le c(m-1)` — potentially closing Case C by reuse rather than
  a new proof. If the quantifier direction is wrong (adversary-minimum vs.
  response-achieves), report exactly where and fall back to Route B.
- **Route B (fallback):** an aimo-0292-style peel-two-elements-and-reattach
  induction (`match(p_1,p_2)`, reinsert the residual `r`, invoke the
  **same-strength** `c(m-1)` IH — not the weaker `c(m-2)` — on the
  resulting `(m-1)`-element instance), with a precise algebraic inequality
  to check against the known hard witness, spelled out in the file.

This is a revision, not a new slug — same approach, sharpened target.

### 2. `case-c-secondary-extremality` — NEW (backup, narrowly scoped)

New file: `results/imo-2026-03/approaches/case-c-secondary-extremality.md`.
Status `unsolved` (not yet attempted). Scoped **only** to Case C — does not
touch the lower bound, Cases A/B, or `m\le3`, and explicitly says so, to
avoid duplicating work already done elsewhere.

Rationale: the alternative-framing explorer identified this
(`aimo-0438`-style "extremal principle with a secondary maximality
criterion, forcing canonical structure via contradiction") as the one
genuinely distinct proof shape found in the crux corpus — a contradiction/
second-layer-extremality argument, rather than an explicit construction or
direct induction, which is what both `universal-adversary-strategy`'s
Route A and Route B are. This makes it a legitimately different framing
from the current live field, per CLAUDE.md's diversity rule, without
being a revival of the two already-retired framings
(`minimax-mixed-duality`, `relaxed-adversary-transfer` — explicitly NOT
touched, per instructions).

The file states a precise sub-goal (select, among Xiang-Yu's optimal
responses — which Lemma TIE-NECESSARY already shows exist at a tie
point — the one maximizing a secondary statistic, e.g. number of
Lemma PAIR-VALUE pairs; derive a contradiction if the maximal-statistic
response still fails the target) and mandates a **cheap feasibility gate
first**: test whether the just-reconstructed true optimal response on the
round-10/11 hard witness is itself distinguished by the candidate
secondary statistic, before investing in the full exchange-argument
machinery. If no statistic distinguishes it, this should report as a
clean negative result (in the style of `majorization-smoothing` /
`potential-averaging-bound`), not be forced into false progress.

### 3. Approaches NOT touched this round (per instructions / no scope)

- `geometric-dominance-construction`, `recursive-embedding-induction` — no
  remaining scope on the (closed) lower bound; not given new targets. (Note:
  `recursive-embedding-induction`'s certified TREE-BOUND-MULTICLUSTER is
  *referenced* by `universal-adversary-strategy`'s Route A as a possible
  reusable tool, but that approach itself is not re-opened or asked to do
  new work.)
- `minimax-mixed-duality`, `relaxed-adversary-transfer` — both
  retired/RETHINK'd, not revived.
- `majorization-smoothing`, `potential-averaging-bound`,
  `equalization-potential-bound` — unchanged, stagnant/dead, not touched.

## Recommended build set

`universal-adversary-strategy` (the revised Round 11 plan — dispatch a
builder to attempt Route A first, falling back to Route B if Route A's
structural check fails) and `case-c-secondary-extremality` (the new
backup angle, dispatch a builder to run the mandated feasibility gate
before any full proof attempt).

**build set: universal-adversary-strategy, case-c-secondary-extremality**
