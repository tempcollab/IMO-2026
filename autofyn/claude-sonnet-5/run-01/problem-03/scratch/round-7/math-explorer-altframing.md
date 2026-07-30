# math-explorer report — alternative framings (round 7)

**Lens:** scout for a genuinely different proof *shape* for imo-2026-03, distinct
from the shared "geometric superincreasing construction + odd-rank-sum /
alternating-sum invariant" framing that all live approaches
(`recursive-embedding-induction`, `geometric-dominance-construction`,
`universal-adversary-strategy`) and the already-dead/near-dead ones
(`potential-averaging-bound`, `majorization-smoothing`, `minimax-mixed-duality`,
`equalization-potential-bound`) all share.

**Problem recap (from `problems.jsonl`).** Liu Bang marks ≤n points on [0,1],
then Xiang Yu marks ≤n points; the stick is cut into pieces; players alternately
claim the largest remaining piece (Liu Bang first) — since pieces are distinct
"non-synergistic" items, greedy-take-largest is optimal for both sides, so the
value of a fixed cut sequence is `oddrank` = sum of pieces at odd rank (1st,
3rd, 5th, ... largest). Conjectured `c(n) = 2^n/(2^{n+1}-1)`. Two open gaps
per `current.md`:
1. **Lower bound**, general `0≤k<n` with Xiang Yu's tail *simultaneously*
   adversarially refined (Lemma PARITY-PAIR-GEN, Case B — the "odd tying-block"
   case — unworked).
2. **Upper bound**, arbitrary (non-geometric) Liu Bang configurations, general
   `n≥2`: the DOM/HALVE/TAIL-SNIP/SANDWICH menu only covers ~74% of a sampled
   `m=3` space; the "which tie-structure is globally best" matching/assignment
   question is open.

I searched `knowledge_base.md` (no game-theoretic dual/surrogate entries yet)
and the crux corpus (`combinatorics` domain, subtopics `games-and-strategy`,
`extremal-principle`, `invariants-and-monovariants`, `processes-and-algorithms`,
`bijections-and-encoding`) per `crux_moves_documentation.md`. Below are three
candidate framings, ranked by how directly they attack the two open gaps and
how far they sit from the current field's shared mechanism (a single
deterministic local move — split/peel/exchange one or two pieces at hand-picked
ratios — plus induction or vertex casework on the sorted composition, as
`minimax-mixed-duality`'s round-6 diagnosis names it).

---

## Candidate 1 (strongest, targets the upper-bound gap): surrogate/relaxed-adversary transfer

**Crux source:** `aimo-0560` (gardener–lumberjack majestic-trees game, ISL
2022 C7-ish). Its load-bearing move (`games-and-strategy`): *"Replace the
adversary with a strictly stronger surrogate whose reply is pointwise at
least as damaging, so a win against the surrogate transfers down and the
reply collapses to a finite per-region menu."* Concretely, to prove the
gardener CAN force `K` majestic trees, the solution plays a **harder
modified game** (the lumberjack gets extra power — he may decrement every
tree except those the gardener just grew, not just 4 of them) and proves the
gardener still wins that harder game via a clean closed-form move-counting
argument; since a gardener strategy that beats the *harder* lumberjack is a
fortiori a valid strategy against the *real, weaker* lumberjack, the result
transfers down without any casework on what the real lumberjack does.

**Why this is a genuinely different shape here.** Every current approach
attacks the upper bound by casework: enumerate Liu Bang's possible tie/vertex
structures, and for each, exhibit a specific menu item (DOM, HALVE, TAIL-SNIP,
SANDWICH, ...) that is a good-enough response. The menu keeps needing new
items because new configurations keep evading the existing ones. The surrogate
trick inverts this: instead of enumerating configurations and finding a
response for each, **relax the game itself so the existence question becomes
config-independent**, solve the relaxed game in closed form, then prove a
one-shot transfer/rounding lemma back to the real (harder-for-Xiang-Yu)
constrained game.

**Concrete adaptation sketch.**
- Define the **∞-mark relaxation**: same game, but Xiang Yu is allowed
  unboundedly many marks (or a continuum — split any piece at any ratio,
  arbitrarily many times). Solve this relaxed game exactly. This is plausibly
  *easier* than the n-mark game: with unlimited splits Xiang Yu can attack
  the oddrank sum via a clean continuous/greedy argument (e.g. repeatedly
  halving the current largest piece, or a symmetry/convexity argument pinning
  the relaxed optimum to a specific closed form) — likely provable directly,
  without per-configuration casework, since the extra freedom removes the
  discreteness that is forcing the current casework.
- Prove a **truncation/efficiency lemma**: the ∞-mark optimal response can
  always be realized (or approximated with zero loss, if piece values must
  land at "tie" boundaries — this is exactly where Lemma TIE-NECESSARY's
  disjunctive tie-structure already lives) using at most `n` marks. This is
  the "transfer down" step, structurally analogous to aimo-0560's "a gardener
  strategy that wins the harder game is legal in the real game."
- If the truncation lemma holds with *equality* (no loss from capping at `n`
  marks), the upper bound falls out in one shot, replacing the
  matching/assignment optimization entirely.

**Risk / what could go wrong (flag honestly for the outliner).** The
truncation step is exactly the kind of thing that could turn out to be as
hard as the current casework — if the ∞-mark optimum genuinely needs more
than `n` splits to approximate for *some* configurations, the relaxation
doesn't close the gap and this collapses into another rediscovery of the
existing menu (the risk `minimax-mixed-duality` flagged and hit for its LP
framing). The mandate should be: **do the cheap/exploratory half first**
(solve the ∞-mark relaxation in closed form on 2–3 concrete `n=2,3`
configurations, numerically) before committing to the truncation lemma —
mirrors the gate `minimax-mixed-duality` and `potential-averaging-bound` were
run under.

---

## Candidate 2 (targets the upper-bound gap; alternative to Candidate 1): explicit one-sequence majorization, not averaged-candidate majorization

**Crux source:** `aimo-0718` (Elisa's treasure chests, ISL 2023 C-ish),
`invariants-and-monovariants`. Crux move: *"Bound a greedy actor against an
adversary that can block at most r objects, pigeonhole on the r+1 smallest
objects."* Its solution builds **one explicit reference sequence**
`b_i^t = b_i^0 + floor((t-i)/n) + 1` and proves by induction on `t` (turn
count) that the real gem-count sequence `a_i^t` is majorized by `b_i^t` at
every turn — not by averaging two candidate strategies (which is what the
already-dead `majorization-smoothing` and `potential-averaging-bound` tried
and disproved on `A=(1/3,1/3,1/3)`, `n=2`).

**Why this is different from the dead attempts.** The dead approaches
averaged the *outputs* of 2–3 simply-defined candidate strategies and showed
the average still fails a witness. `aimo-0718`'s technique instead
majorizes the *state trajectory itself* by one hand-built sequence via
step-by-step induction on time, using a pigeonhole fact (rank `j` above the
`r`-th is never blocked, since only `r` objects can be locked/blocked at
once) — a genuinely different mechanism: an induction on **turn number**
(the claiming phase's `t`), not on `n` (number of marks) or on configuration
vertex type.

**Concrete adaptation sketch.** Target Lemma PARITY-PAIR-GEN's unworked Case
B (the odd tying-block case, general `k<n` with tail simultaneously
refined). Recast the claiming phase as Elisa's chest-filling process: at
each of the `m` claiming turns, the "locked chests" are the pieces already
claimed; build an explicit majorizing sequence for Liu Bang's running total
using the fact that Xiang Yu's marks can "block" (tie/dominate) at most
some bounded number of pieces per rank-band — directly mirroring the
`r+1`-smallest pigeonhole argument — and show this majorization alone forces
the oddrank sum above/below the target `c(n)` threshold in the tying-block
case without enumerating which specific pieces tie.

**Risk.** This needs the "at most `r` blocked objects" structure to have a
clean analogue in the piece-claiming game (what plays the role of "locked
chest" here); this isn't yet verified and should be treated as an open
question for the outline, not an established reduction.

---

## Candidate 3 (targets the lower-bound gap specifically): component-counting pigeonhole for "always a good untied reply"

**Crux source:** `aimo-0663`, `games-and-strategy`. Crux move: *"To prove a
player never gets stuck (liveness), count the contiguous components the
opponent's chosen positions cut the remaining space into and show that count
exceeds the number of positions the responder has used, so some component
holds a free legal reply by pigeonhole."*

**Why this is different.** The current lower-bound work (Lemma L, Lemma
PARITY-PAIR, Lemma FC) proves the `k=n` tail-untouched case by an exact
parity/pairing identity verified case-by-case on vertex type. The unworked
Case B of PARITY-PAIR-GEN is exactly a "does Liu Bang always have a
non-degenerate (non-tied) good move available, given Xiang Yu has refined
the tail" question — which is structurally a **liveness/pigeonhole**
question (does a good untied reply always exist), not an
identity-verification question. `aimo-0663`'s technique — count how many
components/gaps the opponent's already-placed marks split the space into,
and note this count exceeds the marks the responder has used, so a fresh
component always remains — could give an existence argument for Case B
directly, sidestepping the need to classify every tying-block shape.

**Concrete adaptation sketch.** In the tail-refined case, Xiang Yu's marks
partition (part of) the stick into `≤ n+1` intervals ("components"); Liu
Bang has used only `k<n` marks so far in the case under scrutiny. If the
number of components exceeds the number of "committed" choices Liu Bang
still owes, pigeonhole guarantees at least one component gives Liu Bang a
reply that avoids the specific tie Xiang Yu is trying to force — turning
Case B from "verify every odd tying-block shape individually" into "count
components vs. moves used, done." This is speculative (not yet checked
against the actual PARITY-PAIR-GEN statement) but worth a skeleton attempt
since it is a *liveness/counting* argument, orthogonal to every mechanism
currently in the field.

---

## What NOT to re-open (already explored / dead)

- **LP/minimax duality over Xiang Yu's mixed strategy space** —
  `minimax-mixed-duality` tried this directly (not via a surrogate/relaxed
  game, but by seeking mixing weights for the *existing* menu) and its
  round-6 honest diagnosis was that "find good mixing weights" reduces to
  the same casework `universal-adversary-strategy` is already doing. Do not
  re-open plain LP duality as a "new" framing; Candidate 1 above is
  different in mechanism (relax-then-round-down, not mix-the-known-menu) and
  should be pitched that way if used, to avoid the outline-reviewer flagging
  it as a duplicate.
- **Averaging simply-defined candidate strategies** (`potential-averaging-bound`,
  `majorization-smoothing`) — proven dead on `A=(1/3,1/3,1/3)`, `n=2`, and
  `majorization-smoothing` has a genuine structural non-concavity
  obstruction (min of affine + convex piece). Candidate 2 above majorizes the
  *state trajectory*, not strategy outputs — different enough to not be a
  retry of this, but should be framed carefully to avoid the same trap.
- `aimo-0198`'s "bound a greedy minimizer by the average of its two options,
  `min(A,B)≤(A+B)/2`" is the same averaging idea already dead here; not
  worth re-trying.

## Suggested next step for the outliner

Open **at most one** new slug this round per the diversity rule, and make it
**Candidate 1** (surrogate/relaxed-adversary transfer) — it is the furthest
in mechanism from the current field (relax-and-round vs.
casework-on-configuration) and targets the upper-bound gap, which is
currently the harder of the two open gaps (the lower-bound gap is narrowed
to one specific sub-case, Case B, while the upper bound has no clean
sub-case boundary at all — "which tie-structure is globally best" is open in
general). Task it explicitly with the cheap/exploratory gate first (solve
the ∞-mark relaxation on 2–3 concrete small configurations before attempting
the general truncation lemma), matching the pattern that worked for
`minimax-mixed-duality` (which didn't solve the main gap but did surface
Lemma SANDWICH from its mandated exploratory phase). Candidates 2 and 3 are
lower-cost, narrower options — Candidate 3 in particular could be handed to
whichever approach owns Lemma PARITY-PAIR-GEN
(`recursive-embedding-induction`) as an alternative *tactic* within its
existing slug for closing Case B, rather than a whole new approach slug, if
the outliner prefers not to open two new fronts in one round.
