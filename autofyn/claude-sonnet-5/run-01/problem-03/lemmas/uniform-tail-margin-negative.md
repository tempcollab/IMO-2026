# Fact: uniform-tail worst-case margin for the one-level match+IH bound is negative for all m>=4 (certified, round 14)

Source: `case-c-slack-covering.md`, round 14, Step 4. Independently
re-derived from scratch by the proof-reviewer with `sympy` symbolic
simplification (not just numeric sampling): the reviewer's own symbolic
expression for `margin(m) := c(m-1) - UB_1(m)` was simplified and found to
be **identically equal** (exact `sympy.simplify` zero-difference check) to
the builder's claimed closed form, and matches the builder's numeric table
exactly at `m=4` (`-1/70`) and `m=8` (`-641/453390`).

## Setup

For a Case-C configuration `A` (sorted descending, `|A|=m`, `\Sigma(A)=1`
WLOG), tail `T=(t_1\ge\cdots\ge t_{m-1})`, define (via the certified Lemma
DOUBLE-INSERT-MATCH-VALUE combined with the strong induction hypothesis
applied to the leftover, using exactly the remaining `m-2` marks)
```
UB_i := c(m-2) + (1-2c(m-2)) t_i    (with Sigma(A) = 1 normalized),
```
an upper bound on the value achievable by matching `p_1` against `t_i`
and recursing on the leftover. Since `c(n) > 1/2` for every `n`, the
coefficient `(1-2c(m-2))` is strictly negative, so `\min_i UB_i = UB_1`
(attained at the largest tail element `t_1 = p_2`), and this dominates any
weighted average of the family (mean >= min is elementary, so averaging
can never beat `UB_1`).

## Statement

At the uniform-tail boundary (`\Sigma(A)=1`, `p_1 = 1/2`, tail uniform:
`t_1 = \cdots = t_{m-1} = \tfrac{1}{2(m-1)}$), writing
`UB_1(m) := c(m-2) + (1-2c(m-2))\cdot\tfrac{1}{2(m-1)}`,
```
margin(m) := c(m-1) - UB_1(m) = \frac{2^m(3-m)-2}{2\,(2^m-2)(2^m-1)(m-1)}
```
exactly, and `margin(m) < 0` for **every** integer `m \ge 4`.

## Proof

The closed form is a direct algebraic simplification of the definitions
(verified symbolically, see above). For the sign: the denominator
`2(2^m-2)(2^m-1)(m-1) > 0` for every integer `m \ge 2` (each factor
positive). The numerator `2^m(3-m)-2`: for every integer `m \ge 4`,
`3-m \le -1`, so `2^m(3-m) \le -2^m`, giving numerator
`\le -2^m - 2 < 0`. Hence `margin(m) < 0` for every integer `m\ge4`. ∎

## Consequence (reusable pruning fact)

Any future Case-C construction that reduces, even approximately, to "one
top-level match of `p_1` against a single tail element (or an average
over such matches), combined with one coarse application of the induction
hypothesis to the leftover using its generic `c(m-2)` bound" is
automatically insufficient at this exact uniform-tail boundary, for every
`m \ge 4`. A fix must either use a value-aware (not size-only) treatment
of the leftover, or a genuinely multi-level / multi-match construction —
this fact rules out the whole one-level-averaging family at once, so
future rounds should not re-attempt it or re-discover this margin by
numeric search alone.
