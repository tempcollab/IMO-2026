# Outline review — imo-2026-06, round 4 (reviewing round-3's interrupted outliner output)

Read: `/tmp/round-3/proof-outliner.md`, `/tmp/round-3/math-explorer-absorption-recurrence.md`,
`/tmp/round-3/math-explorer-fresh-framing.md`, `results/imo-2026-06/current.md`, the full
`.ranking.json`, and all four proposed approach files on disk (they were already written as
skeletons by round 3's outliner before the interruption; population registration/copies had
also already been executed — `absorption-recurrence-even-case` and `self-closing-pair-density-
odd-case` were already `copy_approach`'d from `antichain-signature-closure`, and
`per-prime-divisor-chain-decomposition` was already `register_approach`'d at cold-start 1500).
I refreshed all four summaries via `register_approach` (idempotent, no-op on existing slugs) and
ran the head-to-head ranking below.

## 1. `absorption-recurrence-even-case` — APPROVE (with caveats)

Copy of `antichain-signature-closure`, scoped to $2\in S=\mathrm{primes}(a_1)$. Reduction is
sound: cites the already-certified `lemmas/absorption-lemma.md` verbatim and correctly isolates
the residual claim as a precise, falsifiable **Trigger Claim** ("some term is eventually a pure
power of 2" — or, hedged appropriately, a pure power of some $q\in S$). The file is honest that
this is wide open with only empirical support (11/11 in the round-3 sim) and explicitly rules out
re-using the dead $O(\log a_n)$ charging shape. No circular reasoning, no hidden hand-off — the
mechanism gap is named precisely, not glossed as "then it follows."

**Caveats to pass to the builder:**
- Flag but do not require fixing: the inherited citation-hygiene gap in Lemma 3 ($P^*\supseteq
  \mathrm{primes}(a_1)$ not verified when citing `periodicity-given-no-escape.md`). Cheap to patch
  (verify directly or re-derive generic in $P$) — ask the builder to take the one-line fix if time
  allows, since it currently makes "zero residual gap in steps 4–6" technically unproven as stated.
- **Diversity note (important):** this is not an independent rival to `self-closing-pair-density-
  odd-case` — it is one half of an exhaustive case split of the *same* parent reduction
  (`antichain-signature-closure`). Casework by parity of $S$ is a legitimate proof strategy (the
  split is genuinely exhaustive and disjoint, and the round-3 explorer found a real empirical
  dichotomy in *which* certified lemma applies to each half), so this is not the CLAUDE.md
  "single-gap trap" (splitting one proof's steps across sibling slugs to be ranked as if
  independent) — but it should be tracked as a **case-pair**, not two independent framings: the
  parent claim (Antichain Stabilization) is only fully resolved once *both* halves close. Do not
  let the population double-count this as two orthogonal mechanisms when assessing field
  diversity.

## 2. `self-closing-pair-density-odd-case` — APPROVE (with caveats)

Sibling case split ($2\notin S$). Correctly cites `lemmas/self-closing-antichain-sufficiency.md`
and gives a genuine worked example ($a_1=15$) plus an honestly-reported counterexample to the
naive "all pairs" pattern ($a_1=255255$, final antichain size 7 not $\binom{6}{2}=15$) — this is
exactly the kind of small-case sanity check that should gate an outline, and it's already done
correctly here, not glossed over. Two clearly delineated sub-targets (characterization vs.
existence fallback), with the fallback honestly flagged as possibly no easier than the sibling
`dilworth-antichain-bound`'s PC target (a real risk, correctly disclosed rather than hidden).

**Same case-pair caveat as above** applies — not an independent rival to approach 1, structurally.

## 3. `dilworth-antichain-bound` — APPROVE

The PC$\Rightarrow$theorem reduction (Steps A–D) is the population's cleanest fully-verified
result: I re-checked Steps A–C's logic (finite-poset minimal-element argument, the $\pi(x)\cap D$
reduction, the $D_i\subseteq P\Rightarrow \pi(x)\cap D_i=\mathrm{primes}(x)\cap D_i$ step) and find
no gap — it is a genuinely different (single-hypothesis, no truncation-hygiene issue) proof shape
from `antichain-signature-closure`'s route, not a restatement. On disk the file is still the round-2
version; the round-3 outliner's *new* content for this round (the $\mu_n$ refutation — correctly
diagnosed as non-monotone via the $a_1=2310$ collapse counterexample, must be recorded not
re-discovered — and the $\nu_n$ cumulative "primes ever used" candidate) has not yet been written
into the file. This is fine; it's the builder's job this round. One thing to insist on: the builder
must not silently claim $\nu_n$'s eventual constancy *solves* PC — the outliner's own analysis shows
this is likely only "free" bookkeeping, not sufficient by itself, and the file must state precisely
what (if anything) beyond boundedness is missing before it would close PC.

## 4. `per-prime-divisor-chain-decomposition` — APPROVE (plateau-breaker slot)

This is the required genuinely-different decomposition axis (per-prime vs. per-antichain-subset) —
correctly distinguished from Lead 3 (finite-automaton reframing), which both round-3 explorers
independently found to just restate PC with no new content, and which the outliner correctly
declined to promote to a slug. The three candidate quantities ($\sigma_p$, $\tau_p$, an
aimo-0477-style transplant) are stated as genuinely untried, with an explicit honesty checkpoint
requiring a documented negative result (in the style of `dense-signature-vanishing`) if none pan
out. No overclaiming, no circular step. Speculative by design — acceptable per the orchestrator's
explicit plateau-breaking instruction.

## Cross-cutting diversity assessment

The four candidates are **not** four independent framings: approaches 1–2 are a case-pair on one
parent reduction (antichain machinery), approach 3 is the sibling PC reduction (same underlying
antichain-of-subsets object, different packaging — already correctly identified in prior rounds as
"the same wall, cleaner form"), and only approach 4 attacks from a structurally different
decomposition axis. **Net new independent mechanism this round: exactly one** (per-prime). This
matches the orchestrator's plateau-breaking requirement (≥1 approach from a genuinely different
framing) but the orchestrator/next round's outliner should be aware the field is still narrow: three
of four slots are variations on the antichain-of-minimal-prime-sets object. If per-prime-divisor-
chain-decomposition also stalls this round, round 5 should prioritize a second, unrelated
plateau-breaking mechanism rather than another antichain dressing.

No approach here repeats a recorded dead end (`dense-signature-vanishing`'s aimo-0680 transplant,
`monovariant-telescoping`'s $|Q|<\infty$, the raw $\mu_n$ candidate, the Dilworth chain-covering
mechanism, any $O(\log a_n)$ charging shape) — all correctly excluded or explicitly flagged as
refuted-and-not-to-retry within the skeletons.

## Ranking

Ran `update_ranking` anchoring the four new/revised candidates against established population
members (core-signature-pigeonhole as a partial-but-weaker baseline; dense-signature-vanishing and
monovariant-telescoping as confirmed dead-ends) and against each other. Result (best-first, approx):
`dilworth-antichain-bound` (1575) > `antichain-signature-closure` (1559, stale cleared, not
building — superseded by its two children this round) > `self-closing-pair-density-odd-case` (1558)
≈ `absorption-recurrence-even-case` (1555) > `growth-bound-density` (1538) > `dense-signature-
vanishing` (1492, dead-end) > `per-prime-divisor-chain-decomposition` (1489) > `core-signature-
pigeonhole` (1477, superseded reduction) > `monovariant-telescoping` (1392, dead-end).
`covering-construction-induction` untouched this round (elo 1457, not competitive, not re-nominated
by the outliner — correctly).

## Build set

All four candidates are sound, non-overlapping in their open-gap claims (even though 1–2 share a
parent), and each makes the population's next round of evidence more informative (a resolved
Trigger Claim, a resolved odd-case existence/characterization, progress or a clean negative on
$\nu_n$, and either a new monovariant or a documented negative result for the per-prime axis).
Build all four in parallel.

build set: absorption-recurrence-even-case, self-closing-pair-density-odd-case, dilworth-antichain-bound, per-prime-divisor-chain-decomposition
