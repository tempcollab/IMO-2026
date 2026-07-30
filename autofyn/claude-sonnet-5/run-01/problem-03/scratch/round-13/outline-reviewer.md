## Review of round-13 outline (imo-2026-03)

Context confirmed against `results/imo-2026-03/current.md`: the lower bound is
fully closed; `m=1,2,3` of the upper bound (Claim PTBI) are fully closed;
the sole remaining gap is Claim PTBI's Case C (`p_1<Sigma(A)/2`) for general
`m>=4`, currently reduced (per certified Lemma THRESHOLD-REDUCTION) to Lemma
HALF-BOUND: `solve_full(A)<=Sigma(A)/2`. Verified this reduction is correctly
cited (matches `lemmas/ptbi-threshold-reduction.md` and round-12's
certified Lemma WF-C5 for the `solve(A,budget)` recursion).

### universal-adversary-strategy (revise) — CHANGES REQUESTED

**Exhaustiveness of the case split.** The Case (a)/(b) dichotomy on
`tail(A)` — `p_2<Sigma(tail(A))/2` vs `p_2>=Sigma(tail(A))/2` — is a genuine
trichotomy-free total split (< vs >=), so it is exhaustive. Good.

**Well-foundedness / IH invoked at a smaller instance.** Verified directly
against the actual certified recursive definition of `solve(A,budget)` in
`approaches/universal-adversary-strategy.md`'s "Round 12 build" section
(Lemma WF-C5, measure `(budget,|A|)` lex, `budget` primary). Case (a)'s
Move-1 recursion into `tail(A)` at unchanged budget decreases `|A|`
strictly (`m-1<m`) — a legitimate smaller instance, consistent with WF-C5.
Case (b)'s Move-2 recursion into `leftover` (with `|L|<m` strictly, per the
already-proved `j*>=1` fact) is likewise a legitimate smaller instance. So
the strong induction is well-founded on `|A|`, reusing WF-C5 correctly —
no new well-foundedness issue here.

**A genuine inconsistency in the Case (b) mechanism (must be fixed before/while
building).** I re-implemented the exact certified `solve(A,budget)` recursion
in Python (`fractions.Fraction`) and traced budget bookkeeping precisely.
Per the certified definition, Move 2 (`partial-dom`) *always* decrements the
recursive call's budget by one (`solve(leftover, max(budget-1,0))`) — at the
top level (`budget=1`), invoking Move 2 sends `leftover` into recursion at
`budget=0`. But the outline's Case (b) text then proposes to "spend the
single Move-3 tail-snip mark ... before invoking the budget-0 IH on the
tail-snipped `L'`" — under the certified semantics, Move 3 requires
`budget>0` in the very call being made, and `budget` is already `0` for
`L`'s call by construction. **There is no spare Move-3 mark available on
`L` under WF-C5's actual budget accounting; the outline's proposed fix
does not correspond to a legal move in the certified recursion as written.**
This is exactly the class of bug flagged in my per-role memory (verify
every recursive branch's effect on the measure/budget directly, don't trust
the outline's prose). The builder must resolve this before claiming CASE-B-MATCH:
either (i) show Move 1/Move 2 alone (no extra snip) already close case (b)
at budget 0 — my own numeric check below suggests this may in fact be the
easier and correct path — or (ii) if a genuine extra snip is needed,
re-derive well-foundedness for a modified budget scheme (e.g., budget=2 at
top) rather than silently assuming a mark that isn't there.

**Numeric evidence bearing on this (worth handing to the builder).** I
independently reimplemented `solve(A,1)` exactly per the certified
definition and ran two checks:
1. Confirmed HALF-BOUND holds as an exact identity for all sampled
   Case-C `A`, `m=4..11` (0 violations / 3116 trials, min margin exactly 0)
   — consistent with round-12's gate.
2. Isolated "case (b)" instances (tail non-Case-C-for-itself, `p_2>=Sigma(tail)/2`,
   1729 samples `m=4..9`) and tested whether **plain Move 1** (`p_1/2 +
   solve(tail(A),1)`, i.e. passing the *unchanged* budget=1 into the tail,
   not spending anything on Move 2) already suffices: **0 failures** — Move 1
   alone (with the tail's own full recursive solve, budget still 1) already
   achieves `<=Sigma(A)/2` in every sampled case-(b) instance, even though
   `tail(A)` is not literally "Case-C for itself." This suggests the
   outline's stated necessary condition for invoking the IH ("tail(A) is
   Case-C relative to itself") may be stronger than actually needed, and
   that the elaborate Move-2/Move-3 CASE-B-MATCH machinery may be avoidable
   entirely if a slightly broader IH statement (covering some non-Case-C
   tails arising specifically as tails of Case-C parents) can be found and
   proved. This is a real lead, not a proof — flag it to the builder as the
   first cheap thing to test/try before building the harder CASE-B-MATCH
   lemma as currently specified.

**CASE-B-MATCH's own honesty.** The outline itself flags (twice, in the key
lemma text and in "Cases to cover") that the `j* in {0,1}` sub-claim and the
further `p_1` vs `p_2` split are NOT worked out — this is correctly
surfaced as an open gap rather than hand-waved, consistent with CLAUDE.md's
rigor rules. Combined with the budget inconsistency above, Lemma
CASE-B-MATCH is not yet a precisely stated lemma with a verified mechanism;
it is a plan for one. That is acceptable for an outline (not a proof) but
the builder must not paper over either gap.

**Verdict: CHANGES REQUESTED**, not RETHINK — the overall strong-induction
technique, the case split, and the well-foundedness argument are sound and
correctly reuse certified prior lemmas (WF-C5, BLOCK-RECURSE, PAIR-VALUE,
THRESHOLD-REDUCTION). The concrete required fixes: (1) resolve the Move-3
budget inconsistency in case (b) — test the cheaper Move-1-suffices lead
first; (2) complete the `j*` / `p_1` vs `p_2` sub-split the outline itself
flags as open; (3) validate any final CASE-B-MATCH argument against the
cascading extremal family `p_i=(1/2-eps)R_i` as the outline mandates.

### universal-adversary-strategy-exact-tie (copy) — CHANGES REQUESTED (build, hedged)

Genuinely different mechanism from the primary slug: an existence/Hall-style
exact-cover reachability claim (Lemma EXACT-TIE-EXISTS) rather than an
inequality-based case-split induction — not a relabeling. The outline
itself honestly flags this is likely false for generic reals in the
unrelaxed form and commits to either completing the "one designated element
may be bisected" relaxed-Hall bridge or producing a clean negative result,
per the standing rule against silent convergence with the primary slug
(round 11's `minimax-mixed-duality`/`case-c-secondary-extremality`
precedent). This satisfies CLAUDE.md's diversity requirement and the
copy-approach rationale (parallel bet on the same gap, distinct technique).
Approve to build with the outline's own mandated discipline: if the
builder's "exact tie" construction turns out to just be the primary slug's
Move-2 leftover argument restated, merge rather than duplicate — do not let
this silently converge a third time.

Housekeeping note: I registered this slug directly (cold-start Elo 1500)
rather than via `copy_approach` from `universal-adversary-strategy`, since
the tool call had already fired before I found the dispatch's "copy" framing
more precisely matched `copy_approach`'s inherit-Elo semantics; the slug
now exists so a retroactive copy isn't possible without clobbering. Ranking
was anchored via `update_ranking` this round instead (see below) — no
action needed, flagging only for the record.

### recursive-embedding-induction / geometric-dominance-construction — advance, no build

Confirmed both targets are fully discharged (lower bound closed in full,
round 10, independently reviewer-verified in `current.md`). Correctly not
nominated for build this round; no new gap in their scope. No issue.

### Ranking

Registered `universal-adversary-strategy-exact-tie` (new). Ran
`update_ranking` anchoring the newcomer against an established dead-end
(`case-c-secondary-extremality`) as well as against the primary live slug,
and reaffirming the primary slug's lead over the confirmed dead-ends
(`minimax-mixed-duality`, `relaxed-adversary-transfer`,
`case-c-secondary-extremality`) — reflecting round-12's certified progress
(WF-C5) and the sharpened-but-still-open HALF-BOUND gap. Post-update Elo:
`universal-adversary-strategy` 1648.8 (top), `recursive-embedding-induction`
1675.1 (untouched, closed-scope milestone), `geometric-dominance-construction`
1634.0 (untouched), `universal-adversary-strategy-exact-tie` 1503.8 (newcomer,
anchored above the confirmed dead-ends, below the established live slug),
dead-ends (`case-c-secondary-extremality` 1449.3, `minimax-mixed-duality`
1427.4, `relaxed-adversary-transfer` 1486.4) correctly below both live slugs.

build set: universal-adversary-strategy, universal-adversary-strategy-exact-tie
