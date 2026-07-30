## imo-2026-03 — fresh-framing scout (assessing 4 candidate "escape the two walls" routes)

Read: current.md, all 4 approach files (parity-measure-potential, induction-peel,
two-box-balancing, explicit-pairing-strategy), lemmas/*, round-2 outline-reviewer.md and
math-explorer-unified.md. Confirmed the problem statement directly (problems.jsonl): Liu
marks ≤n points, Xiang marks ≤n points (seeing Liu's), stick is cut at all marks, then Liu
and Xiang alternately claim unclaimed pieces (Liu first), each maximizing his own total.
Lemma R (already certified) reduces this to: greedy-claim is optimal ⇒ Liu gets the
odd-sorted-rank sum, D = Σ(−1)^{i+1}b_i, target minimax D = u_n = 1/(2^{n+1}−1).

### Verdict up front
None of the four candidate framings genuinely escapes GAP U / GAP L as currently posed —
they either (a) restate the existing measure/recursion machinery in new notation
(candidates 1 and 3), or (b) are not actually formalizable as a clean LP with the tools at
hand (candidate 2). Candidate 4 (crux corpus) surfaces one technique — **surrogate-opponent
domination** — that is genuinely unused by the current field and gives a concrete new angle
on GAP L specifically (not a full alternate framing, but a load-bearing move worth trying).
I also found one clean, previously-unstated *inequality* (not from the four candidates,
but relevant): the two-sided sandwich `2b_1 − 1 ≤ D ≤ b_1` in terms of the single largest
final piece `b_1` — but on checking, the upper half is already implicit in the certified
Lemma M/I ("odd-set ⊆ [0,b_1)"), so it is not new; flagged below only as a sanity note.

### Candidate-by-candidate assessment

**(1) Single Lyapunov potential Φ covering both bounds at once.**
NOT genuinely new, and I don't think it's real as stated. The obstruction: D's "weight" on a
piece (its sign, ±1) is determined by its *sorted rank relative to all other final pieces* —
a global/relational quantity, not a per-piece attribute. Any additive potential
`Φ = Σ f(length_i)` over pieces in isolation cannot see this relational structure, so it
cannot certify D directly; the only way to make a potential "see" rank is to build it from
`N(t) = #{pieces > t}` (parity of coverage) exactly as parity-measure-potential already
does (Lemma M/I), or from the explicit recursive value function `f(A,k)` (which is just the
minimax itself, restated — proving anything about it *is* the problem, not a shortcut past
it). So candidate 1 collapses into either the already-tried measure framing or a tautology.
**Rank: not viable as a distinct route.**

**(2) LP / continuous-optimization duality with an explicit dual certificate.**
Checked concretely whether D, as a function of the *final* multiset, has an LP structure
useful for Xiang's move selection. `D(b)` for a *fixed sorted* multiset is just the forced
alternating sum (no optimization there — the greedy sort already happened, Lemma R). The
actual hard optimization is Xiang choosing WHICH cuts to make on Liu's committed multiset,
which is a **discrete combinatorial choice of a tree of splits**, not a continuous LP: cut
choices change which pieces exist, which changes the sort order globally, so the feasible
region is not convex and "cut a piece" is not a linear operator on the relevant D functional
(this matches the round-2 outline-reviewer's own verdict on the parked `lp-dual-weight`
approach — I independently confirm it, not just repeat it: no natural linear relaxation of
"pick ≤n cut points, one of which resorts the whole multiset" presents itself). A genuine
dual-certificate proof would need to be built lemma-by-lemma from the measure identity
(Lemma M) anyway, i.e. it reduces to framing B in disguise.
**Rank: not viable as stated; matches prior round's "weakest-supported" verdict, now
independently re-derived rather than just trusted.**

**(3) Self-similar renormalization giving `u_n = u_{n−1}/(2+u_{n−1})` for BOTH players
transparently.**
This is **not new** — it is exactly induction-peel's existing engine (Lemma P peel +
the recursion), and its failure mode is exactly why GAP U/GAP L are open: the recursion is
only transparent on the *extremal dyadic path* (Liu plays 𝒟_n, Xiang bisects the top piece,
giving a clean scaled copy of 𝒟_{n−1}). For an **arbitrary** Liu profile or an **imperfect**
Xiang cut, the residual after "peeling the top scale" is NOT a clean order-(n−1) instance —
its extra/leftover mass and its interaction with the global sort is precisely GAP L (lower)
and the reason a single peel is provably insufficient is precisely GAP U (upper). Two-box-
balancing's Sub-lemma SL section states this explicitly: "SL Case A... degenerates as
p_1 ↓ 2^{n−1}" and "GAP L: for general p_1 ≠ p_2 we need D(Π) ≥ 1... the shadow-coupling
claim remains to be constructed" — i.e. the self-similarity IS the open gap, not a route
around it. Re-proposing "the game is literally self-similar for both players" without a
mechanism to force it under imperfect play is not a new opening.
**Rank: identical to the already-stuck framing; do not re-dispatch as if new.**

**(4) Crux corpus: alternating-claim / cut-and-choose games.**
Filtered `combinatorics / games-and-strategy` (39 cruxes) and `invariants-and-monovariants`.
- **aimo-0117** (two-box constructor/corrector, dyadic sequence, superincreasing dominance)
  — already adopted (two-box-balancing approach); no further juice left in it beyond what's
  used.
- **aimo-0560** ("Replace the adversary with a strictly stronger surrogate whose reply is
  pointwise at least as damaging, so a win against the surrogate transfers down") — THIS is
  a genuinely unused technique. Concretely for **GAP L** (lower bound, top-scale cut case):
  instead of building the shadow-coupling map φ that directly compares the actual residual
  to `𝒟_{n−1}`, consider a *stronger surrogate Xiang* who, in addition to his real ≤n−1
  remaining cuts on `Π = {p_1,p_2,2^{n−1},…,1}`, is granted an extra costless power (e.g.
  the ability to also freely re-merge/re-split the `p_1,p_2` fragment pair at no cut cost
  before continuing). If one can show `D(Π under real Xiang) ≥ D(Π under surrogate Xiang)`
  (the surrogate is only more dangerous, i.e. can only make D smaller-or-equal) AND that even
  the surrogate cannot beat `u_n`, the real bound follows for free — this could sidestep
  the exact `p_1 ≠ p_2` bookkeeping that's stalling SL, by folding the imperfection into the
  surrogate's "extra move" rather than tracking it through the sort order. This is
  speculative and unverified (I did not attempt to construct the surrogate map — that is
  outline/build work, not scouting), but it is a load-bearing move genuinely absent from all
  three live approaches.
- **aimo-0236** (two-phase "before/after opponent" invariant, self-restoring induction;
  regime split by whether a valuation threshold has been crossed) — structurally similar
  flavor to what SL's Case A / perfect-bisection split already does; not obviously new
  leverage beyond what two-box-balancing already has.
- No other `games-and-strategy` crux (aimo-0066, 0077, 0115, 0196, 0225, 0262, 0445, 0461,
  0521, 0596, 0631, 0653, 0663, 0746, 0766, 0854, …) matches the two-phase
  commit-then-refine, continuous-length, alternating-claim structure of this problem closely
  enough to transplant a full strategy; most are discrete pairing/parity games on finite sets
  or combinatorial blocking games, not analogous at the level needed.
**Rank: the one genuinely fresh, concrete, unused idea in this batch — the surrogate-
opponent domination trick (aimo-0560) applied to GAP L.**

### A note (not a new framing, a sanity check worth recording)
`D ≤ b_1` (the alternating sum never exceeds the single largest final piece) is **already
implicit** in the certified Lemma M/I ("the odd-set ⊆ [0,b_1)" ⇒ its measure ≤ b_1); I
re-verified it numerically (200k random multisets, both `D ≤ b_1` and the companion
`D ≥ 2b_1 − Σrest` hold with no violation) and by direct algebraic grouping
`D = b_1 − (b_2−b_3) − (b_4−b_5) − …` (each bracket ≥ 0 by sortedness). This is not new
content for the outliner — flagging only so no builder "discovers" it and burns time
re-deriving what Lemma M/I already gives; the useful direction (`D = 2a_1−1` when `a_1`
dominates) is already used in two-box-balancing §1.

## Distinct openings (summary for the outliner)
- None of the three dispatched candidates (potential/Lyapunov, LP-duality, transparent
  self-similarity) is a genuinely new route; two of them (1, 3) collapse into the existing
  measure/recursion machinery and the third (2) is not formalizable as an LP with current
  tools — this independently confirms, rather than just trusts, the round-2 outline-
  reviewer's skepticism of `lp-dual-weight`.
- The one concrete new lever found this round: **surrogate-opponent domination** (crux
  aimo-0560) as a candidate mechanism for closing GAP L — grant Xiang a costless extra
  power in the top-scale-cut branch, show domination (real ≥ surrogate is false direction;
  need surrogate D ≤ real D, i.e. surrogate is at least as damaging/minimizing, so a lower
  bound on the surrogate's value implies the same lower bound for the real player), and
  show the surrogate still can't beat `u_n`. This has NOT been attempted by any live
  approach and is worth one build slot as an explicit named sub-route inside/alongside
  induction-peel or two-box-balancing's GAP L, rather than as a wholly separate slug (it
  targets the same wall with new machinery, which is legitimate per CLAUDE.md's guidance to
  route around a shared gap with a genuinely different mechanism — just not a different
  top-level target, so frame it as a revision to an existing approach's GAP L step, not a
  new competing slug, unless the outliner wants a 4th slug specifically to isolate it).

## Candidate technique(s)
Surrogate/domination argument (crux aimo-0560) for GAP L. Everything else in the dispatched
lens (potential/Lyapunov, LP duality, transparent self-similarity) is assessed as either a
restatement or infeasible — do not spend a build slot on them as framed.

## Cheap-kill candidates
None beyond what's certified (Lemma U0 already discharges all m≤n profiles; `D ≤ b_1` /
`D ≥ 2a_1−1` already used). No new pruning found.

## Knowledge-base entries to use
"Invariants & monovariants" (generic pointer only — not load-bearing here beyond what's
already used); no new KB entry surfaced as directly applicable beyond what the live
approaches already cite (Lemma R/M/T/P derivations use the general backward-induction value
recursion and measure/parity ideas already in the KB's Combinatorics section).

## Analogous past problems (cruxes)
- **aimo-0560** (combinatorics, games-and-strategy) — crux move "replace the adversary with
  a strictly stronger surrogate whose reply is pointwise at least as damaging, so a win
  against the surrogate transfers down" — genuinely unused technique, candidate for GAP L.
- **aimo-0117** — already fully absorbed into two-box-balancing; no further new leverage.
- **aimo-0236** — same invariant flavor as existing SL case split; not independently useful.
- No other crux in `games-and-strategy` or `invariants-and-monovariants` (both domains
  checked) is a close enough structural match to the two-phase continuous claiming game to
  be worth citing.

## Prior progress
See current.md: Lemmas R, M/I, T, P certified; Lemma U0 (new, certified-quality, in
two-box-balancing) discharges all m≤n profiles to D=0. Both bounds reduced to GAP U
(adaptive subset-match upper strategy, m=n+1 full budget) and GAP L (shadow-coupling lower
bound under imperfect top-scale cuts). All three live approaches independently converge on
these same two walls, confirmed again this round by re-reading (not just trusting) all
three approach files.

## Dead ends (do not retry)
- Greedy top-two matching / bisect-the-max as Xiang's universal upper strategy — proven
  insufficient for n≥3 (counterexample (0.5,0.28,0.22)), confirmed independently by round-2
  explorer brute force; re-confirmed structurally here (not re-tested numerically this
  round, but the algebraic reason — a1=a2+a3 exactly needs a whole-profile subset-copy, not
  a pairwise match — still holds).
- Naive "Xiang forces max final piece ≤ u_n" as a full upper strategy (my own check this
  round): infeasible on budget — cutting Liu's dyadic top piece 2^n·u_n down to all pieces
  ≤u_n needs ~2^n−1 cuts, vastly exceeding the n-cut budget, so `D≤b_1` alone cannot be
  turned into a universal strategy; it is only a background inequality, not a route.
- Framing candidates 1 (naive additive potential) and 2 (LP duality) from this round's
  dispatch: assessed and rejected as not viable / not new (see above) — do not re-dispatch
  as distinct slugs without a genuinely new mechanism attached.

## Small-case / intuition notes
- Numerically re-verified (200k random trials) the sandwich `2b_1−1 ≤ D ≤ b_1` for any
  sorted nonnegative multiset — a true inequality, already implicit in certified Lemma M/I,
  offered here only as a confirmed sanity fact, not a new result.
- No new small-case computation changed the picture on GAP U / GAP L; the counterexamples
  and base cases already documented in current.md / two-box-balancing.md stand.
