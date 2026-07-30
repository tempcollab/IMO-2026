# Lemma: n2-upper-bound-complete

**Statement.** `c(2) ≤ 4/7`. Equivalently, for every Liu config with ≤ 3 pieces summing to 1
(`m ∈ {1,2,3}`), Xiang Yu has ≤ 2 marks forcing `D ≤ 1/7` (where `D` is the alternating sum
of the sorted refined multiset, and `c(2) = (1 + D^{*}(2))/2` with `D^{*}(2) = 1/7` by
`claim-game-odd-index`). Moreover the tower `T_2 = (4/7, 2/7, 1/7)` is the **unique** Liu
config with `min_Xiang D = 1/7`; every non-tower config is strict (`< 1/7`).

**Proof.** Regime partition on `(a_1, a_2)` (m ≥ 2):
- **Regime A** (`a_1 ≥ 2a_2` AND `a_1 ≥ 4/7`): halve `a_1` (`dominant-factorization` U2 with
  n=2). `D(total) = D(rest = {a_2, a_3})`, `R = 1 − a_1 ≤ 3/7`. n=1 optimum on `{a_2,a_3}`
  gives `D(rest) ≤ R/3 ≤ 1/7`. Equality iff `R = 3/7` (i.e. `a_1 = 4/7`) AND `{a_2,a_3} = R·T_1
  = (2/7, 1/7)`: the tower `T_2`.
- **Regime B1** (`a_1 < 2a_2` AND `a_2 ≥ 2/7`): pair `a_1 → {a_2, a_1 − a_2}` (U3). `D =
  D(rest' = {a_1−a_2, a_3})`, `R' = 1 − 2a_2 ≤ 3/7`. n=1 optimum: `D(rest') ≤ R'/3 ≤ 1/7`,
  strict (U3 strictness).
- **Regime C** (`a_1 ≥ 2a_2` AND `a_1 < 4/7`): halve `a_1`, `R = 1−a_1 > 3/7` (IH overshoots).
  Resolve directly. Note: sub-case C1 (`a_2 ≥ 2a_3`) is **vacuous** here, since
  `a_1 + a_2 + a_3 ≤ a_1 + a_1/2 + a_1/4 = 7a_1/4 < 1` (as `a_1 < 4/7`), contradicting
  `sum = 1`. So always `a_2 < 2a_3` (C2, pairable): `D(rest) = min(a_2−a_3, 2a_3−a_2) ≤
  a_3/2`, and `a_3 ≤ a_2 ≤ a_1/2 < 2/7` ⇒ `D < 1/7`. Strict.
- **Regime B2** (`a_1 < 2a_2` AND `a_2 < 2/7`): pair `a_1`, `R' = 1−2a_2 > 3/7` (overshoots).
  Resolve directly. `b_1 := max(a_1−a_2, a_3)`, `b_2 := min(a_1−a_2, a_3)`. One shows `b_1 <
  2b_2` always in B2 (the alternative `b_1 ≥ 2b_2` forces `a_1 ≥ 4/7`, contradicting
  `a_1 < 2a_2 < 4/7`). Then `D(rest') = min(b_1−b_2, 2b_2−b_1) ≤ b_2/2`; if `b_2 = a_1−a_2 <
  a_2 < 2/7` then `D < 1/7`; if `b_2 = a_3 ≤ a_2 < 2/7` then `D < 1/7`. Strict.
- **m = 1** (single piece `a_1 = 1`): Xiang marks at `3/7, 6/7` → `{3/7, 3/7, 1/7}`,
  `D = 1/7`; can do strictly better (`s > 3/7` ⇒ `D = 1 − 2s < 1/7`). Strict.
- **m = 2** (`{a, 1−a}`, `a ≥ 1/2`): if `a ≥ 2/3` halve both pieces → `D = 0`; if `a < 2/3`
  pair `a` and halve the rest → `D = 0`. Strict.

Every non-tower config is strict; `T_2` is the unique equality case. See `majorization-upper`
Part III.

**Verified.** Exhaustive exact-`Fraction` search over all Liu configs with `m ≤ 3` on a 1/28
grid (Xiang 2-mark optimum on a 1/20-per-piece grid): **0 exceedances of `D > 1/7`**; max of
`min_Xiang D` over all configs `= 1/7`, attained **uniquely** at `T_2 = (4/7, 2/7, 1/7)`.

**Caveat (defect repaired).** The source proof's displayed chain
`a_3 ≤ (1−a_1)/3 < (3/7)/3 = 1/7` in regime C1 has a sign error (in regime C, `1−a_1 > 3/7`).
This is harmless because C1 is **vacuous** in regime C (shown above); the corrected proof
drops C1 entirely and uses C2's `a_3/2 < 1/7` bound. The conclusion is unaffected and
exhaustively verified.

**Importable by:** `majorization-upper` (base of the "tower-is-unique-worst" induction
beyond n=1). Combined with the lower bound for n=2 (cases a, b-i, b-ii-dyadic certified; the
non-dyadic multi-split sub-case for n=2 is grid-verified, not proved — so the LOWER bound
`c(2) ≥ 4/7` is still partial pending the non-dyadic-multi-split gap G1).
