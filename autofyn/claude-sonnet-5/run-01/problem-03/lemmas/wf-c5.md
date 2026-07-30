# Lemma WF-C5 — well-foundedness of the Candidate-5 recursion

**Certified round 12** (from `universal-adversary-strategy`, "Round 12
build", Step 0). Independently re-verified by the proof-reviewer.

## Statement

Define, for a sorted descending tuple `A = (p_1 ≥ ... ≥ p_m)` and an
integer `budget ≥ 0`:

```
solve(A, budget):
  if |A| <= 1: return sum(A)   # 0 or A[0]
  # Move 1 (halve): p1/2 + solve(tail(A), budget)
  # Move 2 (partial-dom): S_{j*} + solve(leftover, max(budget-1,0))
  #   where j* = max{ j : S_j <= p1 }, S_j = prefix sum of tail(A),
  #   leftover = tail(A)[j*:] plus the residual r = p1 - S_{j*} if r>0
  # Move 3 (tail-snip, only if |A| odd, |A|>=3, budget>0):
  #   split smallest element into two halves, recurse with budget-1
  return min of whichever moves are legal

solve_full(A) := solve(A, budget=1)
```

Then every call sequence reachable from a top-level call `solve_full(A)`
terminates in finitely many recursive calls, for every finite input `A`.

## Proof

Order `(budget, |A|) ∈ Z_{≥0} × Z_{≥1}` lexicographically with `budget`
primary. This is a well-order (both coordinates bounded below; standard
lexicographic product of two well-orders on `Z_{≥0}`). It suffices to
show every recursive call made by a non-base-case invocation (`|A| ≥ 2`)
strictly decreases this measure.

- **Move 1 (halve)**: recurses as `solve(tail(A), budget)`. `budget` is
  unchanged and `|tail(A)| = |A|-1 < |A|`; primary coordinate ties,
  secondary strictly decreases. Measure strictly decreases.

- **Move 2 (partial-dom)**: recurses as `solve(leftover, max(budget-1,0))`.
  The new budget is `≤ budget` always. *Sub-claim `j* ≥ 1` whenever
  `|A| ≥ 2`*: since `A` is sorted descending, `S_1 = p_2 ≤ p_1`, so `j=1`
  always satisfies `p_1 ≥ S_j`; hence the maximal such `j` satisfies
  `j* ≥ 1`. Consequently `|leftover| = |A| - 1 - j* + 1[r>0] ≤ |A|-1-1+1
  = |A|-1 < |A|`. So: if `budget = 0` (ties before/after, since
  `max(-1,0)=0`), the secondary coordinate strictly decreases by the
  `j*≥1` fact; if `budget ≥ 1`, the primary coordinate strictly decreases.
  Either way the measure strictly decreases.

- **Move 3 (tail-snip)**, only reachable when `budget > 0`: recurses as
  `solve(A', budget-1)`. The primary coordinate strictly decreases
  (`budget - 1 < budget`), regardless of `|A'| = |A|+1 > |A|` increasing.
  This is why `budget` must be the *primary*, not secondary, coordinate:
  under the naive `(|A|, budget)` ordering (`|A|` primary) this move does
  **not** decrease the measure, since the primary coordinate goes up.

Since every recursive call strictly decreases a well-founded measure, and
`solve` returns immediately without recursion whenever `|A| ≤ 1`, every
call sequence from `solve_full(A)` reaches a base case in finitely many
steps. ∎

## Independent verification (proof-reviewer, round 12)

- Re-implemented `solve`/`solve_full` from scratch in Python with exact
  `fractions.Fraction` arithmetic. Confirmed the `j*≥1` sub-claim
  algebraically (immediate from `A` sorted descending, one line) and
  confirmed empirically: thousands of random instances (`m=2..12`,
  `budget∈{0,1}`) all terminate, each call count small (linear-ish in
  `m`, no blow-up), consistent with the well-founded measure decreasing
  by at least 1 in either coordinate at every step.
- Traced the specific bug the well-foundedness proof fixes: under the
  outline's original `(|A|,budget)`-primary ordering, `tail-snip`
  increases `|A|` while decreasing `budget`, so it does not decrease that
  measure — confirmed this is a genuine defect in the earlier draft, and
  that `(budget,|A|)` with `budget` primary is the correct fix.

## Scope

Narrow: specific to this one recursive construction (Candidate 5,
`universal-adversary-strategy`'s round-12 attempt at Case C). Fully
general within that scope (any `m`, any `A`, any reachable `budget`).
Does **not** by itself establish any inequality about the *value*
`solve_full(A)` — only that the recursion is well-defined (terminates).
Reusable if Candidate 5 (or a variant threading the same budget
parameter) is picked up again in a future round.
