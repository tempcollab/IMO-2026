## Status
unsolved

## Approaches tried
- Round 11 build: ran the mandated cheap feasibility gate on the hard `m=5`
  witness `A=(1826,1563,1520,1514,765)/7188` before attempting any exchange
  machinery. **Result: the gate exposes a genuine structural obstruction to
  this proof shape — recommend RETHINK.** See "Round 11: feasibility-gate
  findings" below for full detail. Summary: the global-minimum value on this
  witness is achieved not by an essentially-unique tie-structure (as the
  `aimo-0438` technique presupposes) but by a large, structurally diverse
  family of distinct Xiang-Yu responses — including combinatorially
  unrelated construction types (a matching/residual/self-halve chain vs. a
  pure Lemma-MULTI-HALVE cascade) — that turn out to coincide *exactly* only
  because of a hidden **algebraic identity** between their value formulas
  (`p_2+p_4+r_1+(p_5-r_1)/2+r_3 \equiv p_1/2+p_2/2+p_3+p_5/2` whenever both
  constructions' rank orderings hold — verified exactly with `Fraction`
  arithmetic, not a numeric coincidence). The candidate secondary statistic
  (number of exactly-tied Lemma PAIR-VALUE pairs) does narrowly prefer the
  "correct" branch (4 tied pairs vs. 3) on this one test, but only *because*
  we already independently know which branch is correct from the
  construction-lens explorer's hand reconstruction — the statistic itself
  supplies no new leverage for identifying that formula in general. This
  confirms, rather than refutes, the risk flagged in the original "Honest
  risk assessment" section below: the second layer of extremality re-derives
  what the direct-construction routes already need to derive, it does not
  bypass them.

## Current best
(empty — no correct progress established yet; the round-11 build produced
a negative/obstruction finding, not forward proof progress)

## Round 11: feasibility-gate findings (full detail)

### What was tested

Per the mandate, before building any exchange-argument machinery, tested
whether the true optimal Xiang-Yu response on the hard `m=5` witness
`A=(1826,1563,1520,1514,765)/7188` (budget `4`, target `c(4)=16/31`) is
itself distinguished among *all* global-minimum responses by a candidate
secondary statistic — **number of exactly-tied Lemma PAIR-VALUE pairs**
(a response's final `9`-element multiset partitioned into tied pairs plus
at most one unpaired singleton; max possible is `4` pairs `+1` single, since
`9` is odd).

Method: exhaustively searched all `\binom{4+4}{4}=70` mark-allocation
vectors `(k_1,\ldots,k_5)` with `\sum k_i=4` (compositions of the budget
among the `5` pieces), globally optimizing the free split ratios within each
allocation (`scipy.optimize.differential_evolution` + Nelder–Mead polish,
per-allocation), matching every candidate near-optimal split back to exact
`Fraction`s and verifying algebraically. Scripts: `/tmp/round-11/gate_check.py`,
inline exact-`Fraction` verification (below).

### Finding 1 — the global optimum is NOT achieved by an essentially-unique
response; it is achieved by a large, discrete family of combinatorially
distinct allocations

The numeric scan found **at least 17 distinct mark-allocation vectors**
(out of 70) achieving the exact same global-minimum value
`\approx 0.50041736`, not merely a handful of trivial relabelings. Two of
these were verified **exactly** with `Fraction` arithmetic to both equal
`1199/2396`:

- **Construction A (the one hand-reconstructed by this round's
  construction-lens explorer):** `match(p_1,p_2)` (residual `r_1=p_1-p_2`),
  `match(p_3,p_4)` (residual `r_3=p_3-p_4`), `match(p_5\text{-part}, r_1)`,
  `self-halve(p_5-r_1)`. Final multiset (`\times 7188`):
  `1563,1563,1514,1514,263,263,251,251,6`. **4 tied pairs + 1 single
  (`r_3=6`).** `oddrank = 1199/2396` exactly.
- **Construction B (allocation `(1,1,0,0,2)`, a totally different
  mechanism):** `self-halve(p_1)`, `self-halve(p_2)`, `self-halve(p_5)` (2
  marks, one wasted on a degenerate `0` part), leaving `p_3,p_4` **completely
  untouched**. Final multiset: `913,913,\,781.5,781.5,\,1520,1514,\,
  382.5,382.5,\,0`. **3 tied pairs + 3 singles (`p_3,p_4,0`).**
  `oddrank = 1199/2396` **exactly the same value**, verified with `Fraction`.

Both were confirmed exactly (not approximately) with the following Python
session (`fractions.Fraction`, exact arithmetic throughout):
```
leaves_match = [p2, r1, p2, p4, r3, p4, r1, half, half]   # sum = 1 exactly
leaves_halve = [p1/2,p1/2, p2/2,p2/2, p3, p4, p5/2,p5/2, 0]  # sum = 1 exactly
oddrank(leaves_match) == oddrank(leaves_halve) == Fraction(1199,2396) == c4=16/31? no, < c4
```
(both `\le c(4)=16/31`, confirming both are valid Case-C responses meeting
the target on this witness, not just tied with each other).

### Finding 2 — the tie is not numerology, it is a provable algebraic
identity between the two constructions' value formulas

Simplifying Construction A's value symbolically (before plugging in numbers):
```
oddrank_A = p_2 + p_4 + r_1 + (p_5-r_1)/2 + r_3,  r_1=p_1-p_2,\ r_3=p_3-p_4
          = p_2+p_4+(p_1-p_2)+(p_5-(p_1-p_2))/2+(p_3-p_4)
          = p_1/2 + p_2/2 + p_3 + p_5/2.
```
Construction B's value is, by direct inspection (both halves of `p_1,p_2,p_5`
land below `p_3,p_4` in sorted order, so `p_3,p_4` occupy ranks `1,2`
untouched):
```
oddrank_B = p_3 + p_1/2 + p_2/2 + p_5/2.
```
**These are the identical algebraic expression**, `p_1/2+p_2/2+p_3+p_5/2` —
not a coincidence of this witness's specific numbers, but an unconditional
identity that holds *whenever both constructions' rank orderings are valid
simultaneously* (i.e. whenever `p_4 \ge p_1/2`, `p_4\ge p_2/2`, `p_2\ge r_1`,
etc., the exact hypotheses each construction needs). Verified exactly with
`Fraction` arithmetic on the witness (both reduce to `1199/2396`) and
independently re-derived symbolically above.

### Finding 3 — what this means for the secondary-statistic mechanism

- **Narrowly, the gate "passes":** among the two verified competing
  responses, Construction A (the "correct" one, matching the construction-
  lens explorer's report) has strictly more tied pairs (`4` vs. `3`), so
  maximizing "number of tied PAIR-VALUE pairs" over the argmin set *would*
  select Construction A over Construction B on this specific test.
- **But this is not real leverage.** The reason Construction A wins on this
  statistic is a *fact about this specific witness's numbers* (which
  ordering makes `p_3,p_4` fall differently relative to the halved pieces),
  not a *provable general property* of "the tied-pair-maximal response."
  Crucially, **the reason the two constructions tie at all is that their
  value formulas are algebraically identical** — i.e. the secondary
  statistic is trying to distinguish between two responses that a *direct
  computation of each one's closed-form value* already shows are
  interchangeable. Any proof that "the max-tied-pair response always meets
  the target" would have to establish, for every `m` and every Case-C
  configuration, a closed-form value bound on whichever construction the
  tie-count picks out — which is **exactly** the same closed-form-bound
  problem `universal-adversary-strategy`'s Route A/B are already attacking
  (deriving `p_1/2+p_2/2+p_3+p_5/2 \le c(4)\Sigma` in general, or its
  `m`-piece analogue), not a shortcut around it. The "second layer of
  extremality" does not supply any information not already needed by the
  direct-construction approach; it only re-poses the same question with an
  extra selection step on top.
- **A further complication, not fully resolved:** the discrete family of
  tied optima found (`\ge17` distinct allocations) plus internal flat
  directions within some of them (e.g. allocation `(1,0,1,0,2)`'s own
  optimum has a flat interval in how `p_3` is split, since both resulting
  fragments can land at *odd* global ranks simultaneously and so contribute
  their full combined value `p_3` regardless of the exact split point —
  this is not a "tie" in the PAIR-VALUE sense at all, just two fragments
  both landing at odd positions) means the very notion of "the maximal-
  secondary-statistic response" is not even well-posed without first fixing
  which representative of a flat cell to count ties in. This is a genuine,
  unresolved technical obstacle on top of Finding 3's conceptual one.

### Verdict

**Do not build the exchange-argument machinery on this statistic (or,
almost certainly, on any single scalar tie-count statistic) — the gate
reveals the mechanism converges to the same open closed-form question
Route A/B already own, exactly the outcome CLAUDE.md's diversity rule and
this file's own "Honest risk assessment" section flagged as the failure
mode to watch for.** This is reported as an honest, verified negative
result (in the style of `majorization-smoothing` and
`potential-averaging-bound`), not forced into false progress. **Recommend
RETHINK / retirement of this slug** unless a future round can identify a
genuinely different secondary statistic that does *not* reduce to "already
know the closed-form value" — no such statistic was found this round, and
the algebraic-identity finding above suggests any scalar tie-count is
likely to face the same issue (multiple mechanistically different
constructions that are value-equivalent by algebra, not by any structural
tie the secondary statistic could reward without first computing the
values).

## Scope (read this before building)

**This is a narrow, backup approach, not a full restart.** It targets
**only** the single remaining gap for the whole problem: Claim PTBI's
Case C (`p_1 < \Sigma(A)/2`) in `universal-adversary-strategy`'s general
upper-bound induction, for general piece-count `m \ge 4`. It does **not**
re-attempt or duplicate:
- the lower bound (`A_n` achieves `c(n)`) — fully closed, do not touch;
- Cases A/B of Claim PTBI (`p_1 \ge \Sigma(A)/2`) — already closed by
  `universal-adversary-strategy`'s Lemma THRESHOLD-REDUCTION and Lemma DOM;
- `m \le 3` — already fully closed;
- any of the already-certified constructive lemmas (DOM, HALVE,
  MULTI-HALVE, BLOCK-RECURSE, TAIL-SNIP, DOUBLE-INSERT, PAIR-VALUE and its
  SUBSET-DOM/ALL-BUT-MIN/MATCH-TAIL-PAIR corollaries) — these are imported
  as already-proved background facts, reusable without re-derivation.

If this approach's proof shape does not pan out, it should be RETHINK'd or
retired on its own — it must not be allowed to duplicate
`universal-adversary-strategy`'s own Case C work (see that file's Round 11
plan, which pursues two different routes: reusing
`recursive-embedding-induction`'s TREE-BOUND-MULTICLUSTER machinery, and an
aimo-0292-style peel-and-reattach induction). This approach is a
**genuinely distinct proof shape** relative to both of those: a
contradiction argument via a *second layer of extremality*, rather than an
explicit construction or a direct induction.

## Background: why this proof shape, and what it needs to do

By the already-certified **Lemma TIE-NECESSARY**
(`universal-adversary-strategy`'s own `lemmas/tie-necessary.md`), any
global minimizer of Xiang Yu's response
`oddrank(B)` over a fixed budget can be taken at a point where either some
split piece has zero length, or two adjacent-rank resulting pieces are
exactly tied. This already converts the continuous optimization into a
discrete search over tie-structures. What Case C still lacks is a theorem
that *some* tie-structure reachable with `\le m-1` marks achieves
`oddrank(B) \le c(m-1)\Sigma(A)`.

This round's `math-explorer-altframing` report
(`/tmp/round-11/math-explorer-altframing.md`, candidate 3) identifies a
genuinely different proof shape from the crux corpus, drawn from
**`aimo-0438`** (`combinatorics`, `extremal-principle`): among all globally
optimal configurations for a fixed extremal problem, select one that
*additionally* maximizes a secondary alignment statistic; then show any
local deviation admits an edge-count-preserving exchange that strictly
increases the secondary statistic, contradicting maximality — forcing a
canonical structural property on every optimum, without ever exhibiting an
explicit construction.

**This has not been tried on Case C.** Every approach so far (DOM, HALVE,
BLOCK-RECURSE, PAIR-VALUE, ALL-BUT-MIN, MATCH-TAIL-PAIR, and the round-11
plan's Routes A/B) works by *exhibiting* a construction and checking its
value. This approach instead works by contradiction: assume a
counterexample `A` (Case C, `m\ge4`) exists where **no** response with
`\le m-1` marks achieves `\le c(m-1)\Sigma(A)`; among all such
counterexamples (if any), and among all of a fixed counterexample's own
*optimal* Xiang-Yu responses (Lemma TIE-NECESSARY says these exist at a
tie/degeneracy point), select one maximizing a secondary statistic — e.g.
**the number of exactly-tied pairs** in the response, or **the total mass
moved into tied pairs** (`\sum v_i` over Lemma PAIR-VALUE pairs) — and
attempt to derive a contradiction: show that if this maximal-secondary-
statistic optimal response does not already meet the target, some
structure-preserving exchange (splitting a piece differently, or
re-pairing two already-tied pairs) exists that strictly increases the
secondary statistic while not increasing `oddrank(B)` above its optimal
value, contradicting maximality of the chosen response.

## Precise sub-goal for the first builder pass

> **Attempt.** Fix `m\ge4` and a Case-C configuration `A` (sorted,
> `\Sigma=1`, `p_1<1/2`). Let `v^*(A) := \min_{B} oddrank(B)` over all
> `\le(m-1)`-mark Xiang-Yu responses. By Lemma TIE-NECESSARY, the set of
> minimizers is nonempty and every minimizer has a tie/degeneracy point;
> among minimizers, let `\mathcal{M}(A)` be those maximizing (candidate
> statistic, to be chosen and justified by the builder — e.g. number of
> Lemma PAIR-VALUE pairs in the response's PAIR-VALUE decomposition).
> **Task 1**: prove `\mathcal{M}(A)` is well-defined (finite candidate set,
> attained maximum — should follow directly from Lemma TIE-NECESSARY's own
> finiteness argument, applied one level deeper).
> **Task 2 (the real content)**: show that any response in `\mathcal{M}(A)`
> already satisfies `v^*(A) \le c(m-1)\Sigma(A)`, by deriving a structural
> exchange contradiction if it does not — i.e. exhibit the exchange move
> and show it strictly increases the secondary statistic without
> increasing `oddrank`, for every possible way the maximal response could
> fail to meet the target.

**This is unsolved and speculative — the builder's first job is a cheap
feasibility gate, not a full proof attempt:** before investing in the full
exchange-argument machinery, test the *candidate secondary statistic* on
the two known hard witnesses (round 10's
`A=(1826,1563,1520,1514,765)/7188`, and any other Case-C witness recorded
in `universal-adversary-strategy.md`) to check whether the **known true
optimal response** (already reconstructed exactly by this round's
construction-lens explorer, see
`/tmp/round-11/math-explorer-construction.md`) is *itself* the unique
secondary-statistic maximizer among all global minimizers, or whether a
different, non-optimal-for-the-target tie-structure ties or beats it on
the candidate statistic. **If the known optimal response is not
distinguished by the chosen statistic, that statistic is the wrong choice
and a different one must be found before any exchange argument is
attempted** — do not build the exchange machinery on an unvalidated
statistic. If no secondary statistic within a reasonable search
distinguishes the true optimum on the hard witness, report this as a
structural obstruction (analogous to how `majorization-smoothing` and
`potential-averaging-bound` found and reported clean negative results for
their respective mechanisms) rather than forcing progress.

## Honest risk assessment (stated up front, not discovered later)

- No crux in the corpus was found with a *directly transplantable* lemma
  for this exact payoff shape (a weighted alternating sum over a
  combinatorial-cell structure) — `aimo-0438`'s proof shape is the only
  thing being borrowed, not any specific lemma statement or computation.
  Every step below Task 1 must be proved from scratch for this problem.
- This proof shape is close in *spirit* to Lemma TIE-NECESSARY (already a
  "select a boundary point" argument) — the genuine new content is the
  **second layer** of maximality, and it is not obvious in advance that a
  second layer adds real leverage rather than just re-deriving what
  TIE-NECESSARY already gives. The first builder pass should treat this as
  an open question, not an assumed win.
- If this approach also converges to "reduces to the same casework
  `universal-adversary-strategy` already does" (the fate of
  `minimax-mixed-duality`, RETHINK'd for exactly this reason after two
  rounds), it should be retired promptly per CLAUDE.md's diversity rule —
  do not keep it alive as a nominal duplicate.

## Full proof
(Not present — Status is `unsolved`, no proof attempted yet.)
