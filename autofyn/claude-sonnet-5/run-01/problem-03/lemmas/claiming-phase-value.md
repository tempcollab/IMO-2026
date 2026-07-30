# Lemma: claiming-phase value formula

**Status:** certified (round 1). Independently re-derived by both
`geometric-dominance-construction.md` and `recursive-embedding-induction.md`
(and originally by `math-explorer-gamevalue.md`); statements agree verbatim.
Reviewer independently verified by exhaustive brute-force computation
(`game_value` via backward induction vs. `oddrank` via direct sorted-sum, 200
random trials, multiset sizes 0–6, exact `Fraction` arithmetic) — no
mismatches found.

## Statement

Let `S = {a_1 ≥ a_2 ≥ ... ≥ a_m}` be any finite multiset of nonnegative reals.
Consider the alternating-claim game on `S`: two players alternately claim one
remaining element of `S` (player 1 moves first), each maximizing the total
value of the elements they personally claim. Then the game has a
well-defined value for player 1 (independent of any tie-breaking when
several elements are equal or several choices are optimal),
```
f(S) = a_1 + a_3 + a_5 + ⋯  (sum of odd-ranked elements, 1-indexed, descending)
```
and "claim a currently-largest remaining element" is always an optimal move
for whichever player is to move.

## Proof

By strong induction on `m = |S|`.

- **Base cases.** `m = 0`: `f(∅) = 0`, no moves, matches the empty sum.
  `m = 1`: the sole mover takes `a_1`, so `f({a_1}) = a_1`, matches.

- **Inductive step (`m ≥ 2`).** The game is finite, deterministic, zero-sum
  (total value `Σ(S)` is fixed and split between the two players), and
  perfect-information, so its value is given by backward induction: if the
  mover claims `x ∈ S`, the position passes to the opponent on `S \ {x}`, who
  by the induction hypothesis (applied to the smaller multiset `S \ {x}`,
  size `m-1 < m`) secures `f(S \ {x})` from that point on. This leaves the
  original mover with `(Σ(S) - x) - f(S \ {x})` from the remainder, plus `x`
  itself, i.e. payoff `Σ(S) - f(S \ {x})` (using `x + (Σ(S)-x) = Σ(S)`,
  independent of which `x` is chosen). The mover picks `x` to maximize this,
  i.e. to **minimize** `f(S \ {x})`:
  ```
  f(S) = Σ(S) - min_{x ∈ S} f(S \ {x}).
  ```
  Write `h(i) := f(S \ {a_i})` for `i = 1,...,m`. Removing `a_i` from the
  sorted list `a_1,...,a_m` leaves `a_1,...,a_{i-1},a_{i+1},...,a_m` sorted
  descending; elements before position `i` keep their rank, elements after
  position `i` shift down by one (their parity flips). By the induction
  hypothesis applied to this `(m-1)`-element multiset,
  ```
  h(i) = Σ_{j<i, j odd} a_j + Σ_{j>i, j even} a_j.
  ```
  Comparing consecutive values: for `1 ≤ i ≤ m-1`,
  ```
  h(i+1) - h(i) = a_i - a_{i+1} ≥ 0   if i is odd
                = 0                    if i is even
  ```
  (when `i` is odd, position `i` moves from being excluded by both sums in
  `h(i)` into the first sum as `a_i` in `h(i+1)`, while `a_{i+1}` drops out
  of the second sum; all other terms are unaffected. When `i` is even, the
  two defining sums of `h(i)` and `h(i+1)` contain identical terms.) Since
  `a_1 ≥ a_2 ≥ ⋯`, this shows `h` is non-decreasing in `i`, hence minimized
  at `i = 1`: `min_i h(i) = h(1) = a_2 + a_4 + ⋯`. The mover's optimal choice
  is therefore `x = a_1` (a currently-largest element; ties among copies of
  `a_1` are equally optimal), and
  ```
  f(S) = Σ(S) - h(1) = a_1 + a_3 + a_5 + ⋯,
  ```
  closing the induction. Optimality of "take the current largest" for
  either player follows since the argument applies verbatim at every stage
  of the game (each sub-game after any sequence of moves is again an
  alternating-claim game on the remaining multiset). ∎

## Consequence used by all approaches to imo-2026-03

The value `f(S)` depends only on the finite multiset of piece lengths, not
on their order/position along the stick and not on any tie-breaking rule.
Applied to Liu Bang / Xiang Yu's stick-cutting game (where "elements of `S`"
are the final piece lengths after all marks are placed and cuts made), this
reduces the whole problem to: Liu Bang picks a configuration `A` (a
multiset of `≤ n+1` positive reals summing to 1, via `≤ n` marks); Xiang Yu,
seeing `A`, refines it into `B` using `≤ n` further marks (each splitting one
current piece into two positive parts); Liu Bang's guaranteed value is
```
c(n) = max_A min_B oddrank(B),   oddrank(S) := f(S).
```
