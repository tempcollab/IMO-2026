# Proof-outliner report — round 6 — imo-2026-03

Read: `results/imo-2026-03/current.md`, all six existing approach files, and
the three round-6 explorer reports (`math-explorer-ktail.md`,
`math-explorer-coordsplit.md`, `math-explorer-newframing.md`).

## Field this round

### 1. `recursive-embedding-induction` — ADVANCE
Edited in place. New "Round 6 target" section adds a skeleton for **Lemma
PARITY-PAIR-GEN**, the direct generalization of the already-certified
Lemma PARITY-PAIR to a variable, adversarially-refined tail $T$ (not a
fixed constant list), per `math-explorer-ktail`'s concrete recommendation
— explicitly **not** a further abstraction of Claim ★ (certified dead past
$s=2$). Proof skeleton: strong induction on $n$, Case A (even tying block)
hands off cleanly to the $n-1$ instance (already worked out concretely for
$k=1$ by the explorer — not new content, just repositioned), Case B (odd
tying block) is the genuinely open step, using Lemma D-BOUND on the merged
remainder. **Scoped narrowly to $k=2$ tail-refined first**, per the
explorer's de-risking recommendation, before attempting general $k$. This
approach cedes the "one free coordinate" Lemma V' vertex gap to
`geometric-dominance-construction` this round (see below) to avoid two
approaches chasing the same narrow item while a bigger one (PARITY-PAIR-GEN)
is open.

### 2. `universal-adversary-strategy` — ADVANCE
Edited in place. Two changes:
- **Corrected the record**, per `math-explorer-coordsplit`: the round-5
  witness does NOT require a coordinated 2-piece move — a single non-half
  tie-split closes it with a mark to spare. Flagged so future rounds don't
  build on the "2 marks required" framing.
- Added skeletons for **Lemma TIE-NECESSARY** (any optimum lies at a cell
  boundary — degenerate split or an exact tie — via the already-certified
  interior-point linear obstruction; converts continuous optimization to a
  finite discrete search) and **Lemma PARTIAL-DOM** (Lemma DOM generalized
  to prefix ties, same duplicate-pair proof technique, already confirmed
  numerically against a real optimum). Both are assessed as low-risk,
  mechanical extensions of already-certified material — good build-set
  candidates this round.
- Flagged, but **not** assigned as this round's target: the even-$m$
  "two independent non-adjacent ties" phenomenon, recommended as a
  matching/assignment framing, with an explicit note to check whether
  `recursive-embedding-induction`'s certified Lemma PARITY-PAIR transfers
  to this upper-bound object (a cross-approach reuse opportunity, not
  duplication — flagged for after TIE-NECESSARY/PARTIAL-DOM land).

### 3. `geometric-dominance-construction` — RE-SCOPE (not merged, not retired)
Edited in place. Its round-5 exchange-move mechanism for $k\ge2$ is a
confirmed dead end (move-traps, bounded-width impossible), and its only
remaining scope ("$k<n$, tail refined") is now the *same target*
`recursive-embedding-induction` is attacking via PARITY-PAIR-GEN — pursuing
it here via the falsified exchange mechanism would be both a dead end and a
duplication. **Decision: keep the slug alive** (it still carries unique
certified content — Lemma I, rank-shift-by-$s$, Claim ★ $s\le2$, Lemma
X/move-trap negative result) but **re-scope its live target** to the one
genuinely open, genuinely its-own item: the **"one free coordinate" vertex
case of Lemma V'** (closing Proposition K fully for the tail-untouched
case), explicitly ceded by `recursive-embedding-induction` this round.
Skeleton sketched: adapt Lemma D-INSERT to the one-parameter sweep of the
free coordinate, first settling the concrete feasibility sub-question (is
that vertex configuration reachable under the sum constraint) flagged since
round 5.

### 4. NEW — `minimax-mixed-duality` — OPEN
New slug, new file, attacking the **whole problem** (both bounds, primary
focus on the upper bound) via minimax/LP duality over the full mixed
(randomized) Xiang-Yu strategy space — genuinely distinct proof *shape*
from every live and dead approach, per `math-explorer-newframing`'s
Framing 1 (judged the strongest of four candidate new framings; Framing 3
judged too weak against the existing hard witness, Framings 2/4 judged
low-priority/speculative and not adopted). Explicitly distinguished in the
file from `equalization-potential-bound` (global $A$-independent rank
functional, proved impossible — this is per-$A$, response-space weights,
a different object) and from `potential-averaging-bound` (2–3 fixed
$A$-independent deterministic candidates, refuted — this is an
$A$-dependent mixture, directly targeting that diagnosed weakness).
Skeleton: 4 gaps in dependency order (formalize finite-type decomposition,
reusing `universal-adversary-strategy`'s new Lemma TIE-NECESSARY; empirically
find the weight formula on the two known hard witnesses; prove the
expectation inequality in general — honestly flagged as possibly as hard as
direct casework; assess the lower-bound side separately, likely scoping
this approach to upper-bound-only). First build pass should attempt Gaps 1
and 2 (largely exploratory/computational) before Gap 3.

### 5. `potential-averaging-bound` — RECOMMEND RETIREMENT
Edited in place with a round-6 note. Per its own round-5 flag: no
budget-aware third candidate was attempted this round, and its diagnosed
fix is structurally the same content `universal-adversary-strategy` is now
proving directly (Lemma TIE-NECESSARY/PARTIAL-DOM). Its diversity role
(a genuinely different upper-bound proof shape) is now better filled by
`minimax-mixed-duality`, an actual expectation/probabilistic argument
rather than 2–3 fixed candidates. **Recommend the outline-reviewer retire
this approach (RETHINK) this round** — flagging, not unilaterally deciding,
since retirement is the outline-reviewer's call per the ranking-hub role.

### 6. `majorization-smoothing` — unchanged, stays dead
Not touched, per the orchestrator's explicit instruction. Structural
non-concavity obstruction remains a confirmed, documented negative result.

### 7. `equalization-potential-bound` — unchanged, stagnant
Not touched this round; still the round-1 dead-end record (LP/rank-weight
functional proved impossible). No new work targets it.

## Build-set recommendation (for outline-reviewer to confirm/adjust)

Suggested slugs for this round's build set, in priority order:
1. `recursive-embedding-induction` — attempt PARITY-PAIR-GEN, scoped to
   $k=2$.
2. `universal-adversary-strategy` — prove Lemma TIE-NECESSARY and Lemma
   PARTIAL-DOM (both assessed low-risk/mechanical).
3. `minimax-mixed-duality` — first exploratory pass (Gaps 1–2).
4. `geometric-dominance-construction` — attempt the free-coordinate vertex
   case of Lemma V'.

`potential-averaging-bound` not recommended for a build slot (retirement
candidate). `majorization-smoothing` and `equalization-potential-bound`
correctly excluded (dead/stagnant, per standing instructions).

build set: recursive-embedding-induction, universal-adversary-strategy, minimax-mixed-duality, geometric-dominance-construction
