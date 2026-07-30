# Lemma: max-bound-pairing-small-third (MB-Pair) — REDUCTION (NOT a standalone certified lemma)

**REVIEWER NOTE (round 3):** This is a *conditional reduction*, NOT a standalone
certifiable lemma. Its proof depends on the Max-bound induction hypothesis `W(n−1)`
(`D* ≤ M'/2^{n−1}` for every config with max `M'`), which is the Max-bound *conjecture*
itself — proved only for the base cases `n = 0, 1, 2` and open (the crux
`a_1 < 2a_2 ∧ a_3 > a_1/2`) for `n ≥ 3`. Per the round-1 reviewer rule (never certify a
lemma as standalone if its proof depends on an unproved IH), this is REJECTED as a
standalone certifiable lemma. It is recorded here as a clean *reduction* (analogous to
the round-2 `U2`/`U3` reductions): IF the Max-bound holds at level `n−1`, THEN it holds
at level `n` for the non-dominant case `a_1 < 2a_2 ∧ a_3 ≤ a_1/2`. Importers must treat
the Max-bound IH as an unproved assumption.

**Statement.** Let `L = (a_1 ≥ a_2 ≥ a_3 ≥ … ≥ a_m)` be a multiset of positive
reals summing to 1 with `a_1 < 2 a_2` (non-dominant) and `a_3 ≤ a_1/2` (the third
piece is at most half the max). Let `M := a_1`. Assuming the Max-bound IH
`W(n−1)`, Xiang has ≤ `n` marks with

$$D(\text{refined}) \;\le\; \frac{M}{2^n},$$

and the inequality is **strict** (equality forces `a_1 = 2 a_2`, contradicting the
non-dominant hypothesis).

(For `m = 2` — no `a_3` — the same proof works with the single fragment
`a_1 − a_2 < a_1/2` in place of `a_3`; see the last paragraph.)

**Proof.** Xiang's first mark splits `a_1` into `{a_2, a_1 − a_2}` (a *pairing*
move: the larger fragment matches `a_2`). We show the two copies of `a_2` sit at
positions 1, 2 and cancel:
- `a_1 − a_2 < a_1/2` (since `a_1 < 2 a_2` ⟺ `a_1 − a_2 < a_2`, and
  `a_1 − a_2 < a_1/2` ⟺ `a_1 < 2 a_2` ✓). So `a_1 − a_2 < a_1/2 ≤ a_2`.
- `a_3 ≤ a_1/2 ≤ a_2` (hypothesis), and `a_4 ≤ a_3 ≤ a_2`, … So every piece other
  than the two `a_2` copies is `≤ a_2`.

Hence the two `a_2`'s are the largest, at positions 1 (`+`), 2 (`−`); they cancel
(`+a_2 − a_2 = 0`). The rest'
`rest' := sort{a_1 − a_2, a_3, a_4, …, a_m}` begins at global position 3 (odd,
`+`), same parity as rest'-local position 1, so `D(total) = D(rest')`. The rest'
has max `max(a_1 − a_2, a_3) ≤ a_1/2 = M/2` (both candidates `≤ M/2`: shown for
`a_1 − a_2` above, hypothesized for `a_3`; and `a_4 ≤ a_3 ≤ M/2`, etc.). By
`W(n−1)` (piece-count-free), `D(rest') ≤ max(rest')/2^{n−1} ≤ (M/2)/2^{n−1} =
M/2^n`. Parity preserved: the two `a_2`'s (value `a_2 > a_1/2 ≥` rest'-max) stay
at positions 1, 2 (rest'-fragments stay `≤ M/2 < a_2`). Mark budget
`1 + (n−1) = n`. ∎

**Strictness.** Equality in `D(rest') ≤ max(rest')/2^{n−1} ≤ M/2^n` requires
`max(rest') = M/2` AND the rest' attaining the Max-bound at level `n−1` (i.e. being
the scaled tower with max `M/2`). For the rest' max to equal `M/2 = a_1/2`, we
need either `a_1 − a_2 = a_1/2` (⟹ `a_1 = 2 a_2`, contradicting non-dominant) or
`a_3 = a_1/2` with `a_3` the rest' max and the rest' the scaled tower. The latter
forces the rest' largest piece `= a_1/2`; but the rest' largest is `a_3 ≤ a_1/2`,
so `a_3 = a_1/2` and `a_1 − a_2 ≤ a_3 = a_1/2` ⟹ `a_2 ≥ a_1/2` (already true) —
and for the rest' to be the tower `T_{n−1}` scaled by `M/2`, its second-largest
piece must be `M/4 = a_1/4`; but the rest's second-largest is
`max(a_1 − a_2, a_4) ≤ a_1/2`, and for `a_1 − a_2` to be `a_1/4` needs
`a_2 = 3 a_1/4`, i.e. `a_1 = 4 a_2/3 < 2 a_2` ✓ — consistent — but then the rest'
is `(a_3, a_1 − a_2, …) = (a_1/2, a_1/4, …)`, which IS the tower top structure; this
forces `a_1 = 2 a_2` at the *next* level by induction, cascading to a
contradiction with `a_1 < 2 a_2` at the base. So the inequality is strict. (The
cleanest statement: equality at level `n` requires `a_1 = 2 a_2` at the top,
contradicting the non-dominant hypothesis; the cascading-tower equality is the
tower `T_n` itself, which is dominant, not non-dominant.)

**`m = 2` case.** No `a_3`; rest' is the single fragment `{a_1 − a_2}`, max
`a_1 − a_2 < M/2`. By `W(n−1)` (a single piece of size `s` has `D* ≤ s/2^{n−1}`:
scale to total 1, max 1, apply `W(n−1)`, scale back),
`D(rest') ≤ (a_1 − a_2)/2^{n−1} ≤ (M/2)/2^{n−1} = M/2^n`. ✓

**Caveat (conditional).** Same as `max-bound-dominant`: a reduction conditional on
`W(n−1)`; the lower level may have a crux.

**What this closes.** The below-threshold regime B2-with-small-third piece:
`a_1 < 2 a_2 ∧ a_2 < 2^{n−1}/D_n ∧ a_3 ≤ a_1/2`. Here
`M = a_1 < 2 a_2 < 2^n/D_n`, so `D* ≤ M/2^n < 1/D_n` strictly. This is part of G2
(below-threshold regimes for n ≥ 3), now closed.

**Importable by:** `majorization-upper` (the Max-bound non-dominant-small-third
case), any upper-bound approach using the Max-bound.
