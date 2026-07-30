# Lemma NONNEG-EXCESS — the uncapped Round-12 recursion's excess over Σ/2 is never negative

**Certified round 13** (from `universal-adversary-strategy-exact-tie`).
Independently re-derived and stress-tested by the proof-reviewer.

## IMPORTANT SCOPE WARNING (read first)

This lemma is a fact about the **abstract, uncapped `solve(A,budget)`
recursion certified in round 12 (Lemma WF-C5)** — the same recursion
that round 13 discovered does **NOT** faithfully model Xiang Yu's true
mark-capped game (its `budget` parameter tracks only nested Move-3 uses,
not real marks; Move 1/2 never decrement it, and Move 3 grants an
uncounted extra mark). This lemma says nothing about the true game
value, and must not be cited as evidence for or against Claim PTBI or
HALF-BOUND. Its only certified use is as a sanity-check fact about the
recursion itself (e.g. to catch further bugs in reimplementations of
`solve`).

## Statement

Define `e(A,budget) := solve(A,budget) - Σ(A)/2` for the certified
`solve(A,budget)` recursion (Round 12 / Lemma WF-C5). Then for every
finite sorted-descending tuple `A` of positive reals (any `m=|A|≥1`,
Case C or not) and every integer `budget≥0`:
```
e(A,budget) ≥ 0.
```

## Proof

Strong induction on the well-founded lexicographic order `(budget,|A|)`
(`budget` primary) established by the certified Lemma WF-C5.

Base case `|A|≤1`: `solve(singleton)=A[0]`, so `e=A[0]/2>0`; the empty
list contributes excess `0` by convention. Both `≥0`.

Inductive step (`|A|≥2`): `solve(A,budget)` is the minimum over the
available moves of:
- Move 1: `p_1/2 + solve(tail(A),budget)`, i.e. excess
  `e(tail(A),budget)` after subtracting `Σ(A)/2 = p_1/2+Σ(tail(A))/2`.
- Move 2: `S_{j*}+solve(leftover,budget')`. If `leftover` is empty this
  forces `S_{j*}=p_1` exactly (an exact tie), giving excess exactly `0`.
  Otherwise the excess is `e(leftover,budget')`.
- Move 3 (if available): `solve(A',budget-1)`, excess `e(A',budget-1)`.

Each of `(tail(A),budget)`, `(leftover,budget')`, `(A',budget-1)` is
strictly smaller than `(A,budget)` in the WF-C5 order (this is exactly
what WF-C5 proves), so by the inductive hypothesis each corresponding
excess is `≥0` (or exactly `0` in the empty-leftover case). Hence
`e(A,budget)`, being the minimum of nonnegative quantities, is `≥0`.
`∎`

## Independent verification (proof-reviewer, round 13)

- Reimplemented `solve` from scratch (`fractions.Fraction`, memoized,
  exact) and computed `e(A,budget)` over 3000 random trials
  (`m=1..7`, random positive integer entries, `budget∈{0,1}`); minimum
  excess found across all trials: exactly `0`. No violation.
- Confirmed the base cases and the "empty leftover forces excess 0"
  sub-claim directly from the recursion's definitions (one-line
  algebra: `leftover` empty means `S_{j*}=p_1` exactly, so
  `S_{j*}+0 = p_1 = p_1/2+p_1/2`, and `Σ(A)/2 = p_1/2 + Σ(tail)/2`;
  since `leftover` empty also means `S_{j*}=Σ(tail)` — the matched
  prefix is the whole tail — so `Σ(tail)/2=p_1/2`, giving excess exactly
  `S_{j*}-p_1/2-Σ(tail)/2 = p_1-p_1/2-p_1/2=0`).

## Scope

Narrow, as stated above: a fact about the specific uncapped
`solve(A,budget)` recursion only, not about the true mark-capped game
value. Reusable only as an internal consistency check on any future
reimplementation or extension of this specific recursion.
