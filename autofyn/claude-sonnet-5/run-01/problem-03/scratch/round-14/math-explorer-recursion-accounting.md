## imo-2026-03

### Focus of this lens (round 14, priority 1)
Rebuild a genuinely mark-faithful recursion `solve2(A, marks)` — ONE shared
real-mark counter (`marks = |A|-1`, the true Xiang-Yu budget), every move
(halve / contiguous-prefix-match / tail-snip / non-contiguous subset-match)
charged against it — and report what a corrected numeric adversarial gate
would show. I built and ran this from scratch (script logic below,
independent of the round-13 builders' own code) and traced actual winning
move sequences, not just top-level values.

### The corrected recursion `solve2(A, marks)` — what it must look like

```
solve2(A, marks):
  if |A| <= 1: return sum(A)
  p1 = A[0]; tail = A[1:]
  best = +infinity
  # Move 1 (halve p1): cost 1
  if marks >= 1:
      best = min(best, p1/2 + solve2(sorted({p1/2,p1/2} + tail), marks-1))
  # Move 2 (subset-match p1 against a subset S of tail, contiguous OR not):
  #   for every S subseteq tail with sum(S) <= p1:
  #     r = p1 - sum(S);  cost = |S| if r>0 else |S|-1   (Lemma DOM-boundary-slack)
  #     leftover = (tail \ S) union {r if r>0}
  #     candidate = sum(S) + solve2(leftover, marks-cost)   [only if cost<=marks]
  #   best = min(best, min over all affordable S of candidate)
  # Move 3 (tail-snip smallest element): cost 1, requires |A| odd, |A|>=3
  if marks >= 1 and |A| odd and |A| >= 3:
      best = min(best, solve2(A with smallest element -> two halves, marks-1))
  return best
```

The key fix versus the retracted round-12/13 `solve(A,budget)`: **there is
exactly one counter, `marks`, and it equals the true `m-1` at the top level
and is decremented by the ACTUAL number of physical cuts every move
performs** (halve=1; a subset-match producing `|S|` matched pieces plus one
residual piece costs `|S|`, or `|S|-1` if the residual is exactly `0`,
exactly per the already-certified Lemma DOM-boundary-slack; tail-snip=1).
This removes both defects round 13 found: (a) Move 1/2 no longer get "free"
uncounted marks, (b) Move 3 (tail-snip, which *increases* `|A|` by one) is
now charged against the *same* pool, not a separate nested-only counter, so
it cannot manufacture a phantom extra mark.

I implemented and ran exactly this (`fractions.Fraction`, memoized on
`(A, marks)`, exhaustive over ALL subsets `S` of the tail — not just
prefixes — when the "subset" move is enabled) as `/tmp/recursion_check.py`
and a tracing variant `/tmp/trace_check2.py`.

### Results on the three key witnesses (numeric, exact `Fraction` where stated)

**Witness A = (26,21,10), m=3, true budget = 2 marks** (the round-13
exact-tie witness). `solve2` with contiguous-only menu: **31** exactly
(matches round 13's independently-confirmed true value, both via
menu-restricted DP and unrestricted `scipy` continuous search). With the
subset-match move added: **still exactly 31** — subset matching gives NO
improvement here (only 3 pieces, no non-contiguous subset exists other than
the trivial prefix). `31 > Σ/2=28.5` but `31 < c(2)Σ=228/7≈32.57`: Claim
PTBI's real target holds with room to spare; the sharper Σ/2 identity is
correctly refuted (confirms round 13's finding under the *correctly
constructed* solve2, independent re-derivation).

**Witness T = (20,15,12,8), m=4, true budget = 3 marks** (round 13's Case-(a)
witness). Contiguous-only menu: `solve2 = 28 > Σ/2 = 27.5` — reproduces
round 13's finding exactly under my independent implementation. **With the
subset-match move added: `solve2 = 27.5 = Σ/2` exactly** — matching the true
optimum round 13 found via `scipy` (split `p_1=20` into `(12,8)`, an exact
non-contiguous tie against the tail's own `{12,8}`, skipping `15`, while
independently halving `p_2=15`). This *confirms*, under a properly
mark-capped shared-counter recursion (not the retracted one), that
non-contiguous subset matching is genuinely load-bearing here, not an
artifact of bad accounting.

**Witness m=8 = (0.2117,0.1588,0.1410,0.1319,0.1232,0.0881,0.0748,0.0705)**
(round 12's flagged Candidate-3/5 counterexample; `c(7)Σ≈0.50196078`). This
is the most informative test, because round 12 had claimed (under the
OLD, now-retracted accounting) that the winning donor subset here was
`{p_2}` — i.e. that ordinary contiguous PARTIAL-DOM already sufficed and
subset-matching added nothing on this witness; the real defect was thought
to be recursion depth/budget, not subset choice (see math-explorer's
per-role rule #25). **Under the corrected, real-mark-capped `solve2` with
`marks = m-1 = 7`:**
- Contiguous-only menu: `solve2 ≈ 0.5021 > c(7)Σ ≈ 0.50196` — **fails**
  (this witness is a genuine counterexample to contiguous-only matching
  even after fixing the accounting bug, not just under the old buggy
  recursion).
- Subset-match menu enabled: `solve2 = 0.5 = Σ/2` **exactly** — passes with
  margin (`0.5 < 0.50196...`).
- I traced the actual winning move sequence (not just the value): it is
  `CONTIGMATCH(p1 vs prefix {p2}, cost 1) → SUBSETMATCH(the residual's own
  p1 vs a NON-adjacent single tail element, skipping two larger elements,
  cost 1) → four more halvings → two free contiguous ties → leaf`. The
  subset-match step genuinely skips over larger tail elements to reach a
  smaller one it can exactly afford — this is a real non-contiguous
  matching, not an artifact.

**Conclusion, this round's central finding:** under the corrected
single-real-mark-counter recursion, the round-12 diagnosis "the m=8
counterexample only needed recursion depth, not subset choice" **does not
survive re-accounting** — once marks are charged correctly to every move
(so contiguous PARTIAL-DOM's leftover can no longer silently borrow
recursion depth it hasn't paid for), the m=8 witness needs genuine
non-contiguous subset matching too, at a DIFFERENT point in the recursion
(one level down, on the leftover after the first contiguous match, not at
the top level). This suggests the earlier "subset choice was never the
problem" finding (round 12, math-explorer-subsetmatch) was itself
contaminated by the same accounting bug the whole population later found —
it is worth flagging as possibly needing re-examination, not just the
round-12 "gate PASS".

### What move-menu actually suffices (this round's terrain answer)

On all three known hard witnesses, **contiguous-only matching (cheap,
existence trivial — just take the maximal affordable prefix) is
insufficient** under correct mark accounting; **full non-contiguous
subset-matching (Lemma PAIR-VALUE / SUBSET-DOM's general form) is required**
and, where tested, sufficient to reach the target (with margin, not just
equality) in all three cases. This strengthens (not weakens) the standing
diagnosis, echoed across rounds 9–13: **the load-bearing missing piece is
a general existence theorem** — for any tail and any target value `p_1`
(with `p_1 < Σ(tail)`, Case C), does there always exist a subset `S` of the
tail (possibly with residual `r=p_1-Σ(S)`, cost `|S|` or `|S|-1`) whose use,
combined with recursing on the leftover with the reduced budget, drives the
whole recursion down to `≤ c(m-1)Σ(A)`? This is NOT a bare Hall's-theorem
SDR question (no bipartite 1-1 matching structure is given up front — it's
a subset-sum/exact-cover-flavored existence claim, consistent with
per-role rule #24) — it needs either (a) a genuinely different existence
argument (e.g. an averaging/greedy-with-backtrack argument tailored to
this specific recursive value function, since plain greedy subset-sum
is already known to fail — rule #23), or (b) reformulating the whole
induction to avoid needing an unrestricted subset-match oracle at all
(e.g. bounding the recursion's value directly via an inequality that
doesn't require identifying which subset is optimal, in the spirit of the
"average of two candidate strategies" idea flagged in rule #19 but never
carried through for this specific recursion).

### Termination / feasibility of the corrected recursion

The corrected `solve2(A, marks)` with subset-match included is well-founded
by the SAME lexicographic argument as Lemma WF-C5, with one adjustment:
now there is only ONE parameter (`marks`), and it strictly decreases on
every move (halve: `marks-1`; subset-match: `marks-cost` with `cost>=1` in
general, EXCEPT the boundary `r=0` case where `cost=|S|-1` could in
principle be `0` if `|S|=1` — but a `1`-element exact-tie match costs `0`
marks only if the match already exists in `A` with no split at all, which
is a genuinely free move and must be handled as a separate "recognize an
existing tie, no split needed" base case, not a decrementing recursive
call — this is a small but real corner that needs explicit treatment in
any formal write-up, distinct from Move 2's degenerate `j=1,r=0` case
already handled by the certified DOM-boundary-slack fact). Tail-snip:
`marks-1`. So termination is on `marks` alone (strictly decreasing, bounded
below by 0), simpler than WF-C5's two-coordinate argument, PROVIDED the
`cost=0` free-tie corner is excluded from ever recursing again on the SAME
size or larger (it should immediately return a value, not call `solve2`
again) — this is a one-line addition to WF-C5's proof, not a new
difficulty, but must be stated explicitly since the retracted recursion's
bug was exactly a mishandled boundary/cost accounting issue.

### Computational cost of a full adversarial gate with subset-match included

The subset-match move is `2^k` per node (`k`=tail size), so a full
`differential_evolution`-style continuous adversarial gate over `m=4..14`
with the FULL subset-match menu at every recursive level is exponential in
`m` and will not scale past roughly `m~14-16` even with memoization
(consistent with round-12's own finding that letting the leftover recurse
through the unrestricted full menu without any cap "did not terminate" —
though that was a different, non-terminating bug; here it terminates but
is simply slow). A trustworthy numeric gate at `m` up to ~12-14 (matching
prior rounds' own tested range) is feasible; going meaningfully higher
would need either restricting the subset search heuristically (risky —
greedy subset selection is already known to fail, rule #23) or accepting
a coarser/randomized subset sample for large `m` and treating it as weaker
evidence than the small-`m` exhaustive checks.

### Cheap-kill checks before heavy computation
- Re-verify contiguous-only ALWAYS fails the correctly-capped gate at at
  least one `m` for every `m>=4` tested (this round only checked `m=8`
  explicitly plus the two small witnesses; a cheap next step is to rerun
  the exact same `m=8`-style `differential_evolution` search but against
  `solve2`-contiguous-only with the corrected single-counter budget, for
  `m=4..12`, to see whether contiguous-only fails at MORE than just `m=8`,
  or whether `m=8` was already the worst case under the old buggy
  accounting and remains so).
- Parity/mark-count sanity check: for any proposed construction, count
  physical cuts directly (as round 13's exact-tie build did) and confirm
  the total never exceeds `|A|-1` — this single check would have caught
  the round-12/13 bug in one line, and should be a mandatory assertion in
  any future recursion implementation.

### Candidate technique(s)
- Corrected budget-capped recursion as above (single real-mark counter).
- The genuine open mathematical content is a **subset-sum/exact-cover
  existence theorem** for Lemma PAIR-VALUE / SUBSET-DOM (not literal Hall's
  marriage/SDR, despite the superficial resemblance — no natural bipartite
  structure is given), possibly provable by strong induction jointly on
  `(|A|, marks)` using the SAME measure as the corrected WF-C5.

### Knowledge-base entries to use
- Hall's marriage theorem / SDR (`knowledge_base.md` line ~122) — candidate
  but likely needs reformulation per rule #24; a straight citation will not
  suffice since the structure is subset-sum, not 1-1 bipartite matching.
- Invariants & monovariants (for re-deriving termination of the corrected
  recursion — the single-counter `marks` measure is a clean monovariant).
- Double counting / extremal-style pigeonhole — not obviously applicable
  yet, but worth checking against the subset-sum existence question if a
  direct construction stalls (no lemma from the KB currently targets
  subset-sum existence directly; this may be the deepest gap in the whole
  KB relative to this problem).

### Analogous past problems (cruxes)
Not independently re-queried this round (out of time budget after the
recursion-accounting build) — prior rounds (9, 10) already searched the
games-and-strategy / subset-sum subtopics for Hall's-theorem-style cruxes
(see per-role rules #6, #24) without finding an exact drop-in existence
theorem for a subset-sum matching structure; I did not find anything
different in `knowledge_base.md` itself worth adding beyond what is
already flagged.

### Prior progress
See "Current best" throughout; the whole lower bound and `m=3` upper bound
remain fully closed and untouched by this round. Case C for general `m>=4`
remains the sole open gap. This round's contribution: a from-scratch,
independently-built, correctly single-counter-budgeted `solve2` recursion
that reproduces every round-13 finding exactly and ADDITIONALLY shows the
`m=8` witness (previously believed to need no subset-matching once
accounting is fixed, per round-12's `math-explorer-subsetmatch` finding)
DOES need subset-matching under correct accounting, one level down in the
recursion from where round 12 looked (round 12 checked the TOP-level
donor-subset choice only; the real need appears in a nested sub-call after
one contiguous match has already been applied).

### Dead ends (do not retry)
- Trusting round-12's `math-explorer-subsetmatch` "the winning subset here
  is exactly the contiguous prefix, subset choice was never the problem"
  finding as still valid — it was computed under the retracted
  `solve(A,budget)` accounting (see round-13 findings); this round shows it
  does NOT survive re-accounting on the same `m=8` witness. Flag for the
  outliner: any claim in the population sourced to the pre-round-13
  `solve(A,budget)` recursion's traced move sequences (not just its final
  values) should be treated as unverified until re-traced under `solve2`.
- Greedy subset selection (largest-fitting-first) for the subset-match
  move — already shown to fail 74% of random trials in round 10 (rule #23);
  do not propose it again as a shortcut for the existence question.

### Small-case / intuition notes (all labeled conjecture except where an
exact computation is cited above)
- Conjecture (strong numeric support, 3 witnesses, all exact/near-exact):
  the corrected `solve2` with the FULL subset-match menu never exceeds
  `c(m-1)Σ(A)` in Case C — consistent with, but not proof of, Claim PTBI.
- Conjecture (weaker numeric support, 1 witness so far): contiguous-only
  matching is insufficient at multiple `m`, not just `m=8` — needs a
  broader sweep (`m=4..14`) under `solve2`'s corrected accounting to
  confirm before treating as established terrain.
- The `m=8` witness's winning subset-match is NOT at the top level but one
  level into the recursion (after an ordinary contiguous match already
  fired) — this suggests any inductive proof attempt should allow the
  subset-match existence question to be invoked at EVERY recursive level,
  not just checked once at the top of the induction step, which is a
  meaningfully different (harder) proof obligation than a single top-level
  existence check.
