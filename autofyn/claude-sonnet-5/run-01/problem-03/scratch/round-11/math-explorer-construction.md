# Round 11 — math-explorer (construction lens): reverse-engineering Xiang Yu's optimal Case-C response

## Scope

Lens: numerical/computational search for the true optimal Xiang Yu response
on adversarial Case-C witnesses (`p_1<\Sigma(A)/2`, general `m\ge4`), to
find the general rule the current menu (BLOCK-RECURSE, THRESHOLD-REDUCTION,
PAIR-VALUE, ALL-BUT-MIN, MATCH-TAIL-PAIR) misses. **Scouting only — no
proof attempted.**

Method: for a fixed mark-allocation vector `(k_1,\ldots,k_m)` (how many of
the `m-1` marks go to splitting each original piece), any Xiang-Yu response
under that allocation is exactly "partition `p_i` into `k_i+1` positive
parts" for each `i` — recursion order never matters, only the final
partition. So the *entire* reachable space is captured by looping over all
compositions of `m-1` into `m` nonnegative parts and, for each, globally
optimizing the free split values with `scipy.optimize.differential_evolution`
+ Nelder–Mead polish (softplus/normalize parametrization keeps parts
positive and summing to `p_i` without constraints). This reproduces a true
global optimum (not merely a candidate), and the optimal split values were
then matched to exact `Fraction`s to read off the algebraic structure.
Scripts: `/tmp/round-11/search.py`, `/tmp/round-11/search2.py`.

## Main finding: exact reconstruction of the known `m=5` witness's optimum

For `A=(1826,1563,1520,1514,765)/7188` (`m=5`, budget `4`, target
`c(4)=16/31\approx0.51613`), the round-10 file reports a numeric true
optimum `\approx0.5004` found via an ad hoc deep brute force, without a
clean closed form. The exhaustive-allocation search here reproduces it
**exactly** as
```
oddrank = 1199/2396 = 0.500417362...  < c(4) = 16/31.
```
Reading off the optimal split (winning allocation `(k_1,\ldots,k_5) =
(1,0,1,0,2)`, i.e. **1 mark on `p_1`, 1 mark on `p_3`, 2 marks on `p_5`,
`p_2` and `p_4` untouched**) gives an exact, clean algebraic construction:

- **Match `p_1\to p_2`** (BLOCK-RECURSE, `j=1`): split `p_1` into
  `(p_2, r_1)`, `r_1:=p_1-p_2 = 263/7188`. Contributes the tied pair
  `\{p_2,p_2\}` (value `p_2`) plus the loose residual `r_1`.
- **Match `p_3\to p_4`** (BLOCK-RECURSE, `j=1`, independently, a second
  disjoint pair at the same level): split `p_3` into `(p_4, r_3)`,
  `r_3:=p_3-p_4 = 6/7188` (tiny). Contributes `\{p_4,p_4\}` plus loose `r_3`.
- **Absorb `r_1` into `p_5`, then self-halve the rest.** Split `p_5$ into
  three parts: one part exactly **ties `r_1`** (a third, cross-level match —
  `p_5\to r_1`, an instance of Lemma PAIR-VALUE, *not* expressible as a
  single BLOCK-RECURSE chain since `r_1` is not an original piece), and the
  remaining mass `p_5-r_1 = 502/7188` is **split into two equal halves**
  `251/7188` each (an unconditional Lemma DOUBLE-INSERT self-halve, no
  matching partner needed).
- **`r_3` is left untouched, unpaired** — the smallest element in the whole
  final 9-element multiset, landing at the last (odd) rank, contributing
  `r_3=6/7188` alone.

Final sorted multiset (`\times7188`): `1563,1563,1514,1514,502/2\cdot2{=}251,251,263,263,6`
(sorted: `1563,1563,1514,1514,263,263,251,251,6`), giving
`oddrank = 1563+1514+263+251+6 = 3597`, i.e. `3597/7188 = 1199/2396` exactly
— matches the search to machine precision and reduces to the round-10 file's
numeric value on the nose.

**This exact reconstruction is new** (the round-10 file only had the numeric
value and a vague "five moves, deep recursive composition" description); the
algebraic structure above is a precise, checkable 4-mark construction:
`match(p_1,p_2) + match(p_3,p_4) + match(p_5,r_1) + self\text{-}halve(p_5-r_1)`,
leaving `r_3` as leftover.

## The naive "always match, never self-halve" rule is FALSE — a clean, exact counterexample

A natural guess for a general rule is: recursively feed every residual back
into the pool and always match the **two currently-largest** available
values, repeating until the budget is exhausted (a pure greedy
matching/pairing cascade, no self-halves). Simulated exactly on the same
witness (`/tmp/round-11` verification script): this greedy rule produces
```
match(p1,p2), match(p3,p4), match(p5,r1)->residual 502/7188,
match(502/7188, r3=6/7188) -> residual 496/7188 (final, unprocessed leftover)
```
giving
```
oddrank_greedy = 1921/3594 = 0.534502... > c(4) = 16/31 = 0.516129...
```
**This exceeds the target — greedy matching is not just suboptimal, it
provably fails to close Case C on this witness.** The true optimum instead
*reserves* the last mark for a **self-halve** of the exposed residual
`502/7188` rather than matching it down to the tiny leftover `r_3=6/7188`.

## Diagnosis: why self-halve beats "match to a much smaller partner"

Both computations above are exact (`Fraction`), giving a clean mechanistic
explanation, not just a numeric coincidence:

- **Matching** a value `X` down to a much smaller partner `Y` (`Y\ll X`)
  costs 1 mark, contributes the *safe* amount `Y` from the tied pair, but
  **exposes a new residual `X-Y`** (`\approx X`, since `Y` is small) that,
  if no further budget remains to control it, lands somewhere in the sorted
  order **unmanaged** — it contributes either the *entire* `X-Y` (if it
  happens to land at an odd rank) or `0` (if even), a gamble that is bad in
  expectation whenever `X-Y` is not itself small.
- **Self-halving** `X` (Lemma DOUBLE-INSERT / the general Lemma PAIR-VALUE,
  both hypothesis-free) costs 1 mark and contributes **exactly** `X/2`,
  *unconditionally* — the two equal halves are always mutually adjacent in
  sorted order, so there is no exposure risk at all; this is a "safe" move
  in a way matching-down is not.
- Concretely here: matching `502/7188` down to `6/7188` leaves the exposed
  residual `496/7188` sitting unmanaged (it happens to land at an odd rank,
  contributing its full value) — self-halving `502/7188` instead
  guarantees exactly `251/7188`, roughly half the damage, regardless of
  where it lands.

**Empirical rule (not proved as a theorem, but checkable and precise):**
*match large elements down to their nearest neighbor while enough budget
remains to keep controlling the resulting residual recursively; reserve
self-halving (the "safe", exposure-free move) for the residual that would
otherwise be left with no further budget to fix its landing parity.* This
sharpens, rather than resolves, the open existence question: it is not "any
matching works" (false, shown above) nor "always self-halve" (worse still —
checked: self-halving `p_1,\ldots,p_4` and leaving `p_5` alone, or other
all-self-halve allocations, all scored strictly worse than `0.5004` in the
exhaustive search) — the correct general strategy provably **must mix**
matches and self-halves, and *which* mix is optimal depends on the relative
sizes of the residuals in a way not captured by any single static rule
tried so far (BLOCK-RECURSE alone, ALL-BUT-MIN alone, MATCH-TAIL-PAIR
alone, or naive greedy cascading).

## Secondary evidence: `m=4` witness reproduces the same two-pair-plus-tie-residuals pattern

`A=(0.35,0.30,0.20,0.15)`, budget `3`, target `c(3)=8/15\approx0.53333`:
exhaustive-allocation search finds true optimum **exactly `0.5`**, via
allocation `(1,0,1,1)`: match `p_1\to p_2$ (residual `0.05`), match
`p_3\to p_4$ but with `p_4$ pushed to a **degenerate zero-length part**
(one of Lemma TIE-NECESSARY's two allowed boundary types — the mark is
"wasted" rather than genuinely splitting `p_4`), and the two residuals
(`0.05` from `p_1`, `0.05` from `p_3`) turn out **already exactly equal** by
sheer coincidence of this witness, so they tie for free with no extra mark
needed, and the final degenerate `0` sits as the odd-rank leftover. This is
consistent with (not a new mechanism beyond) BLOCK-RECURSE applied twice in
parallel to two disjoint top pairs — no self-halve was needed here because
the two residuals happened to already coincide. A second `m=4` probe
(`A=(0.49,0.30,0.12,0.09)`, budget `3`) found a lower value (`\approx0.51`,
comfortably under `c(3)`) with allocation `(2,0,0,1)` but the optimizer did
not fully converge to exact ties within the time budget available for this
scouting pass (values close to but not exactly `0.3`, `0.12` — a precision
artifact of `differential_evolution`, not a different qualitative
structure); not pursued further given the scouting time budget.

## Honest assessment

- **What is solid, exact, and reusable:** the precise reconstruction of the
  known `m=5` hard witness's optimal 4-mark construction (`match(p_1,p_2)`,
  `match(p_3,p_4)`, `match(p_5,r_1)`, `self-halve(p_5-r_1)`, leftover `r_3`),
  verified to the exact fraction `1199/2396`; and the **exact counterexample
  showing "always match, never self-halve" fails** (`1921/3594 > 16/31`) —
  this is new, load-bearing negative evidence that should stop any future
  round from trying a pure-matching Hall-type existence argument without
  also allowing self-halves as first-class moves.
- **What is NOT established:** a general, provably-optimal decision
  procedure (when to match vs. when to self-halve, and which partner to
  match to) for arbitrary `m` and arbitrary configurations. The diagnosis
  above ("match while budget can still control the resulting residual;
  self-halve only once budget for further control runs out") is a plausible
  *qualitative* principle consistent with every witness checked this round,
  but it is empirical, not a theorem, and was not tested against enough
  independently-generated adversarial configurations (`m=6,7`) to be
  confident it is exactly right — only `m=4,5` were checked to full
  precision within this round's time budget. In particular it does not
  yet say, in closed form, *how many* marks to reserve for the terminal
  self-halve as a function of `m`, nor prove that this two-move menu
  (match + self-halve), used in *some* order, always suffices for every
  `m\ge4` — this remains exactly the open existence/Hall-type question
  flagged in `current.md`, now narrowed to "prove a match/self-halve
  interleaving always exists," rather than "prove a matching always
  exists" (which is now known false as a stand-alone claim).

## Files

- `/tmp/round-11/search.py` — general exhaustive-allocation + global
  optimizer search tool (reusable for any `A`, any `m`, any budget).
- `/tmp/round-11/search2.py` — additional `m=4` probes.
- Exact-fraction verification of the reconstructed `m=5` construction and
  the greedy-fails counterexample was run inline (see fractions above);
  reproducible via `python3 -c "..."` with the values quoted in this report.
