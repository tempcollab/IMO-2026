## imo-2026-03 — scouting report: adaptive Case C construction

### Setup recap (from `universal-adversary-strategy.md` / lemma files)
Claim PTBI (strong induction on piece-count `m`): for sorted
`A=(p_1≥...≥p_m)`, Σ:=Σ(A), using ≤m-1 marks Xiang Yu can force
`oddrank(B) ≤ c(m-1)Σ`. Cases A (`p_1≥c(m-1)Σ`) and B (`Σ/2≤p_1<c(m-1)Σ`)
are fully closed (Lemma THRESHOLD-REDUCTION). **Case C is `p_1<Σ/2`,
general `m≥4`, and is the only remaining gap for the whole problem.**

Key reusable fact used throughout: **Lemma PAIR-VALUE** (`lemmas/pair-value.md`):
if `B = U ⊎ {v_1,v_1} ⊎ ... ⊎ {v_k,v_k}` (any number of tied pairs, anywhere
in sorted order, no domination/contiguity needed), then unconditionally
`oddrank(B) = oddrank(U) + Σv_i`. This means: any construction that
"matches" some pieces into tied pairs and leaves a residual `U` to be
handled recursively gets total value = (sum of matched pair values) +
(recursively-achieved value on `U`), regardless of how the matching is
laid out. This is the design principle behind every candidate below.

### Distinct openings / candidate adaptive rules tried

**Candidate 1 — pure "peel top, halve, recurse on tail" (Case A's
construction applied unconditionally, no adaptivity).**
`solve(A) = p_1/2 + solve(tail)`, base case `solve({x})=x`.
Uses Lemma DOUBLE-INSERT (unconditional halving via PAIR-VALUE, no
domination hypothesis). **Numerically REFUTED as a stand-alone rule**:
3600 random Case C trials (`m=4..15`), 2021 violations (56%), worst margin
`≈-0.228` at `m=4`, `A≈(0.741,0.667,0.638,0.635)` (near-uniform top-4) —
exactly the failure mode already on record (round 7): halving is wasteful
when all pieces are comparable in size; the correct move there is to pair
elements up, not repeatedly bisect the max.

**Candidate 2 — pure PARTIAL-DOM / BLOCK-RECURSE chain (maximal-prefix
match, recurse on leftover via the same rule).**
`solve(A)`: match `p_1` against the maximal tail-prefix it dominates
(`Lemma PARTIAL-DOM`/`BLOCK-RECURSE`), recurse on the leftover residual +
untouched tail-suffix. **Also REFUTED as a stand-alone rule**: 4800 trials,
3280 violations (68%), worst margin `≈-0.354` at `m=5`. Also fails the
near-uniform-tail family (`p_1=0.499`, uniform tail) for every `m` from 9
to 20 (small negative margins, e.g. `m=20`: `≈-0.0010`), and fails the
`m=5` hard witness `A=(1826,1563,1520,1514,765)/7188` (margin
`-2047/111414 <0`). Consistent with round-10/11's finding that greedy
largest-first-style matching alone is not universal.

**Candidate 3 — adaptive 3-way menu (the interesting one):**
```
solve12(A):                      # strategies 1 & 2 only, recursion always
                                  # strictly shrinks |A|, so well-defined
  if |A|==1: return A[0]
  p1, tail = A[0], A[1:]
  v1 = p1/2 + solve12(tail)                        # Strategy 1: peel+halve
  j* = max j with p1 >= S_j (S_j = prefix-sum of tail, S_0=0)
  r  = p1 - S_{j*}
  leftover = tail[j*:] + ({r} if r>0 else {})
  v2 = S_{j*} + solve12(sorted(leftover, desc))     # Strategy 2: PARTIAL-DOM
  return min(v1, v2)

solve_full(A):                   # top-level: adds a 3rd move when |A| odd
  base = solve12(A)
  if |A| is odd and |A|>=3:
      snip smallest element a_m into two copies of a_m/2 (1 mark,
        unconditional, via Lemma TAIL-SNIP / PAIR-VALUE — always LEGAL,
        decreases oddrank when |A| odd)
      v3 = solve12(new (|A|+1)-element list)   # continue with strategies 1,2 only
      return min(base, v3)
  else:
      return base
```
This is a genuine config-dependent rule: which of `v1`/`v2`/`v3` wins
differs by instance (verified explicitly below).

**Stress test results for Candidate 3 (exact `fractions.Fraction`
throughout):**
- 2700 random Case C trials, `m=4..12`: **0 violations.**
- 960 more random trials with a different skew distribution
  (`random()**3`), `m=4..15`: **0 violations.**
- `m=5` hard witness `A=(1826,1563,1520,1514,765)/7188`: margin
  `=1/62>0` ✓ (winning move: Strategy 2, PARTIAL-DOM).
- Near-uniform-tail family (`p_1=0.499`, tail uniform), `m=4..40`: **all
  positive**, margin shrinking toward 0 as `m→∞` (e.g. `m=20`:
  `+4.77e-7`; `m=40`: `+4.5e-13`) — consistent with the family being an
  asymptotically-tight (not violating) sequence.
- Near-tied-top-two family (`p_1=p_2=0.5-ε`, tail uniform), `m=4..20`:
  all positive, same decaying pattern.
- Boundary geometric-tail family (`p_1=0.5-ε`, tail geometric ratio 1/2),
  `m=4..20`: all positive.

**However — Candidate 3 is NOT universal.** A `scipy.optimize.
differential_evolution` search (minimizing the margin `target-value`
directly over the simplex, restricted to `p_1<Σ/2`) found a genuine
violation at **`m=8`** (even `m`, so Strategy 3 / TAIL-SNIP is
unavailable — the failure is confined to the even-`m`, 2-strategy-only
regime):
```
A ≈ (0.2117, 0.1588, 0.1410, 0.1319, 0.1232, 0.0881, 0.0748, 0.0705)
```
Re-verified **exactly** with `fractions.Fraction` (rational approximation
of the optimizer's output, denominators up to ~10^7):
```
target = c(7)·Σ  ≈ 0.5019607843...
value  = solve_full(A) ≈ 0.5021141315...
margin = target - value ≈ -0.0001533  (exact rational value negative,
                                        confirmed, not floating-point noise)
```
i.e. Candidate 3 loses by a small but genuine margin. Adding a 4th
candidate move — halving the top-`K` pieces simultaneously for `K=2,3`
(also legal unconditionally via Lemma PAIR-VALUE / a generalized
DOUBLE-INSERT, no domination hypothesis needed) — was tested against this
exact counterexample and **did not help** (identical margin; that move is
never the arg-min here). Trying *every* prefix length `j` (not just the
maximal PARTIAL-DOM prefix) as a separate PARTIAL-DOM candidate also
**did not help** (identical margin) — so the missing move is not a
"try more prefixes" refinement of Strategy 2.

### What this narrows the search to

The `m=8` counterexample is a clean, reproducible falsifier (exact
rational, in the repo's test-witness style — should be added to the
"hard witness" list alongside the `m=5` witness and the near-uniform-tail
family). Its defining feature: **even `m`, no piece anywhere near
dominating even a short prefix of the tail** (all 8 pieces are within a
factor of ~3 of each other), so neither peel+halve, prefix-matching, nor
top-K-halving is a good move — this is exactly the "near-uniform,
neither DOM nor HALVE fires" regime flagged as unsolved since round 5
(`universal-adversary-strategy`'s Lemma TAIL-SNIP dead-end note), except
here it recurs at even `m` where TAIL-SNIP itself is structurally
unavailable (it *increases* `oddrank` for even `m`). The missing move for
this regime is very likely a **non-prefix / non-contiguous subset match**
(Lemma PAIR-VALUE's general SUBSET-DOM corollary allows matching an
arbitrary subset `T` of tail values to a split piece, not just a prefix)
or a **jointly-optimized non-half two-piece split** (as found in round
2/5's near-tied-top-two witness) — both are legal moves the current
3-strategy menu does not try. A 4th candidate worth testing next round:
for even `m`, additionally try "split `p_1` to match some *non-prefix*
subset `T` of the tail (not necessarily the top-`j` elements) chosen
greedily to minimize the recursive residual," or "recursively apply the
whole `solve_full` rule (not just `solve12`) inside Strategy 2's leftover
recursion" (Candidate 3 restricts recursive calls inside PARTIAL-DOM to
`solve12` only, to avoid the infinite-recursion trap TAIL-SNIP creates
when nested unboundedly — but this restriction may itself be why `m=8`
is missed; a version that allows one bounded level of nested TAIL-SNIP,
or alternates it correctly with depth-limiting, is untested).

### Cheap-kill candidates
- None obvious as a pure structural pruning (parity/pigeonhole) that
  would settle Case C outright; the problem is genuinely a "find the
  right adaptive selection rule" existence question, not a counting
  argument.

### Knowledge-base / lemma entries to use
- `lemmas/pair-value.md` (Lemma PAIR-VALUE) — the unifying tool: any
  matching-into-tied-pairs decomposition has value = Σ(matched values) +
  oddrank(unmatched), unconditionally. This is the right lens for
  designing the adaptive rule (a matching/partition problem), not a
  case-by-case algebra problem.
- `lemmas/block-recurse.md`, `lemmas/partial-dom.md`,
  `lemmas/partial-dom-residual.md` — the PARTIAL-DOM/BLOCK-RECURSE chain
  (Strategy 2 above).
- `lemmas/double-insert.md` — unconditional halving (Strategy 1's
  building block, no domination hypothesis needed).
- `lemmas/split-and-tail-snip.md` (Lemma TAIL-SNIP) — Strategy 3's
  building block, only legal/beneficial for odd `m`.
- `lemmas/multi-halve.md` — top-K simultaneous halve (tested as Strategy
  4, did not help on the `m=8` counterexample, but may help elsewhere;
  keep in the menu).
- `lemmas/ptbi-threshold-reduction.md` — the surrounding Case A/B closure
  this gap sits inside.
- Hall's marriage theorem (cited in `knowledge_base.md`, per
  `pair-value.md`'s own note) — the natural tool if the eventual
  construction needs *simultaneous, non-conflicting* multi-donor
  subset matches (several pieces each matching disjoint tail subsets at
  once) rather than one greedy sequential match.

### Analogous past problems (crux corpus)
Did not query the crux corpus this pass (scope was numeric algorithm
stress-testing per dispatch); round 10/11 explorers already searched
combinatorics/matching subtopics and found the closest analogue was
Hall's-theorem / exact-cover flavored (no problem_id reproduced verbatim
here — see round 10 math-explorer report for the citation trail). No new
crux search performed this round; recommend a future explorer specifically
search the "non-contiguous subset-sum matching to close a residual gap"
pattern (the `m=8` counterexample's likely fix) rather than re-searching
Hall's theorem generically.

### Prior progress
Case A, Case B fully closed (Lemma THRESHOLD-REDUCTION). Case C: `m=3`
fully closed (round 9). `m≥4` open. Round 10/11 established no *fixed*
small template (fixed pair-count, fixed threshold switch) is universal.
This round's Candidate 3 (adaptive 3-way min, described above) is
**strictly stronger** than everything on record — it survives every
random/adversarial family previously used to falsify constructions,
including the round-11 near-uniform-tail family (all `m` up to 40) and
the `m=5` hard witness — but is **not fully universal**: a genuine,
exactly-verified counterexample exists at `m=8`, margin `≈-1.53×10^-4`.

### Dead ends (do not retry without modification)
- Candidate 1 (pure peel+halve, no adaptivity) — refuted, 56% violation
  rate, matches round-7's diagnosis exactly.
- Candidate 2 (pure PARTIAL-DOM maximal-prefix chain, no adaptivity) —
  refuted, 68% violation rate; also fails the `m=5` hard witness and the
  near-uniform-tail family for `m≥9` — do not treat PARTIAL-DOM alone as
  sufficient even though it looks like the "right" mechanism for
  matching-heavy configs.
- Adding top-K-halve (`K=2,3`) as a 4th menu item to Candidate 3 — tested
  against the `m=8` counterexample specifically, made no difference
  (never the arg-min there); don't expect it alone to close the gap.
- Trying every PARTIAL-DOM prefix length (not just the maximal one) as
  separate candidates — tested against the `m=8` counterexample, no
  improvement; the missing move is not "a better prefix," it's a
  genuinely different (non-prefix) structure.

### Small-case / intuition notes (conjectural, not proven)
- The menu needed for Case C appears to require **at least one
  non-contiguous / non-prefix matching move** (SUBSET-DOM with an
  arbitrary tail subset, not just a prefix) for the even-`m`,
  near-uniform regime — this is a conjecture based on one counterexample,
  not a proof that such a move suffices.
- The margin at the `m=8` counterexample is very small (`-1.5×10^-4`
  relative to values `≈0.502`), suggesting the true construction is
  "close" to what Candidate 3 already does — a small enhancement (one
  more move type, or relaxing the "prefix" restriction in Strategy 2 to
  "any subset with the right sum," genuinely tested with a real subset-
  sum search rather than the greedy maximal prefix) is plausibly enough,
  rather than requiring an entirely new proof technique.
- Recommend next round's builder: (a) formally verify the `m=8`
  counterexample (exact Fraction, reproduced above — safe to hard-code
  as a new regression witness), (b) add a genuine non-prefix subset-match
  candidate (e.g. small subset-sum search over tail subsets summing to
  ≤p_1, not just the greedy prefix) to Candidate 3's menu and re-run the
  same optimizer-based adversarial search (differential_evolution over
  the simplex) for `m=6..10` to check whether the enhanced menu survives;
  (c) if a proof is attempted, structure it as strong induction on `m`
  with the case split "some prefix/subset match helps" vs. "no subset
  match helps, but near-uniformity itself bounds oddrank directly" (the
  latter may need a separate, dedicated near-uniform-case lemma, since
  Candidate 3's failure at `m=8` occurs exactly where no single move in
  the current menu is a strict enough contraction).
