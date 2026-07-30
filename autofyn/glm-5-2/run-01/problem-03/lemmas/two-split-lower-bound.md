# Lemma: two-split-lower-bound (PROPOSED for certification)

**Statement.** Let `T_n = (2^n, 2^{n−1}, …, 2, 1)` (tower units, total `D_n = 2^{n+1}−1`), `n ≥ 2`.
Suppose Xiang uses exactly TWO marks, both splitting fragments of the top piece `2^n` (so the
top `2^n` is replaced by three fragments `a ≥ b ≥ c` with `a+b+c = 2^n`, the multiset being
`{a, b, c} ∪ T_{n−1}`). Then the alternating sum satisfies

$$D \;\ge\; D(T_{n-2}) \;=\; \frac{2^{n-1} + (-1)^{n-2}}{3} \;\ge\; 1 \;=\; \frac{1}{D_n}\text{ (real units)}.$$

The minimum `D(T_{n−2})` is attained at the **dyadic cascade** `2^n → 2^{n−1}+2^{n−1}` then
`2^{n−1} → 2^{n−2}+2^{n−2}`, giving `D = D(T_{n−2})`. The global minimum over all 2-mark
refinements is attained at a **breakpoint (tie) config** (by `pl-breakpoint-minimum`).

**Caveat on scope.** This lemma covers the case where both marks split fragments of the **top
piece** `2^n` (the three-fragment case). The case where one mark splits the top and the other
splits a **tower piece** `2^k` (Type C) is verified `n = 3,…,7` but not fully proved here — it
follows the same block-contribution + parity-constraint pattern (see "Verified cases" below).

---

## Proof

By `pl-breakpoint-minimum`, the global minimum of `D` over all 2-mark refinements is at a
breakpoint (PL vertex) where two independent tie conditions hold. The two cut points are `q`
(first split's smaller fragment) and `s` (second split's smaller fragment); the derived larger
fragment of the second split is `r = 2^n − q − s`. We show `D ≥ D(T_{n−2})` at every breakpoint.

We use `frontier-recursion` (`D(T_n)+D(T_{n−1})=2^n`, `D(T_{n−2}) = D(T_n) − 2^{n−1}`,
`D(T_n) = (2^{n+1}+(−1)^n)/3`) and `block-contribution-formula` (for all-tower multisets).

### Case 1: Both cut points tie tower pieces (`q = 2^a`, `s = 2^b`)

The three fragments are `r = 2^n − 2^a − 2^b`, `s = 2^b`, `q = 2^a`. The config is
`{r, 2^b, 2^a} ∪ T_{n−1}`.

#### Sub-case 1a: `r ≥ 2^{n−1}` (i.e., `2^a + 2^b ≤ 2^{n−1}`)

`r` is the unique largest (position 1, sign `+`). `D = r − D(R)` where
`R = {2^b, 2^a} ∪ T_{n−1}` is all-tower (the fragments `2^a`, `2^b` are tower pieces adding
extra copies at levels `a`, `b`).

**If `a ≠ b`** (let `m = min(a,b)`, `M = max(a,b)`): Levels `m` and `M` have count 2 (even,
cancel). The remaining odd-count levels form three tower segments (above `M`, between `m` and
`M`, below `m`). Summing each as a geometric series `Σ_{k=j}^{ℓ} (−2)^k = ((−2)^j − (−2)^{ℓ+1})/3`
and simplifying (verified `Fraction`-exact `n = 3,…,7`):

$$D = D(T_n) - \frac{c_M \cdot 2^M + c_m \cdot 2^m}{3},$$

where `c_M = 3 + (−1)^{n+M} ∈ {2,4}` and `c_m = 3 + (−1)^{n+m+1} ∈ {2,4}`.

`D ≥ D(T_{n−2})` is equivalent to `c_M·2^M + c_m·2^m ≤ 3·2^{n−1}`. This follows from the
**parity constraint**: `c_M = 4` requires `M ≡ n (mod 2)`, which forces `M ≤ n−2` (since
`M ≤ n−1` and `n−1 ≢ n`). An exhaustive four-case check on `(c_M, c_m) ∈ {2,4}²`:

- `c_M = 2, c_m = 2`: `2·2^M + 2·2^m ≤ 3·2^M ≤ 3·2^{n−1}`. ✓
- `c_M = 4, c_m = 2`: `M ≤ n−2`, so `4·2^M + 2·2^m ≤ 5·2^M ≤ 5·2^{n−2} < 6·2^{n−2} = 3·2^{n−1}`. ✓
- `c_M = 2, c_m = 4`: `m ≡ n−1 (mod 2)`, `M ≡ n−1 (mod 2)` (since `c_M=2`), so `m ≡ M (mod 2)`,
  forcing `m ≤ M−2`. Then `2·2^M + 4·2^m ≤ 2·2^M + 4·2^{M−2} = 3·2^M ≤ 3·2^{n−1}`. ✓
- `c_M = 4, c_m = 4`: `M ≡ n`, `m ≡ n−1` (opposite parities), so `m ≤ M−1 ≤ n−3`.
  `4·2^M + 4·2^m ≤ 4·2^{n−2} + 4·2^{n−3} = 3·2^{n−1}`. ✓ (equality at `M=n−2, m=n−3`).

**If `a = b`**: three copies of `2^a`, level `a` odd-count (`n_a = 3`). A similar geometric-sum
computation gives `D = D(T_n) − 2^{a+1}`. The constraint `s ≤ r` gives `2^a ≤ (2^n−2^a)/2`, i.e.,
`3·2^a ≤ 2^n`, so `a ≤ n−2` (for `n ≥ 2`). Hence `2^{a+1} ≤ 2^{n−1}`, giving
`D ≥ D(T_n) − 2^{n−1} = D(T_{n−2})`. ✓

#### Sub-case 1b: `r < 2^{n−1}` (i.e., `2^a + 2^b > 2^{n−1}`)

This forces `M = n−1` (one cut is balanced: `q = 2^{n−1}`), and `m < n−1`. Then
`r = 2^{n−1} − 2^m < 2^{n−1}`. The two copies of `2^{n−1}` (fragment `q` and tower piece) are
adjacent and cancel (positions 1, 2). Then `D = D({r, 2^m, 2^{n−2}, …, 1})`.

The fragment `s = 2^m` and tower piece `2^m` form a pair (level `m` even-count, cancels). After
cancellation: `D = D({r} ∪ (T_{n−2} \ {2^m}))`.

If `m = n−2`: `r = 2^{n−1} − 2^{n−2} = 2^{n−2}`, tying tower piece `2^{n−2}`. The two copies
cancel, leaving `D = D(T_{n−3}) ≥ D(T_{n−2})` (since `D(T_{n−3}) ≥ D(T_{n−2})` — both are
`≥ 1` and the frontier recursion gives `D(T_{n−2}) = 2^{n−1} − D(T_{n−3})`, so
`D(T_{n−3}) = 2^{n−1} − D(T_{n−2})`; for `n ≥ 3`, `D(T_{n−3}) ≥ 1` and `D(T_{n−2}) ≥ 1`, but
`D(T_{n−3}) ≥ D(T_{n−2})` iff `2^{n−1} ≥ 2·D(T_{n−2})` iff `2^{n−1} ≥ 2(2^{n−1}+(−1)^n)/3`,
i.e., `3·2^{n−1} ≥ 2·2^{n−1} + 2·(−1)^n`, i.e., `2^{n−1} ≥ 2·(−1)^n`, true for `n ≥ 2`). ✓

If `m ≤ n−3`: `r = 2^{n−1} − 2^m ≥ 2^{n−1} − 2^{n−3} = 3·2^{n−3} > 2^{n−2}`. So `r` is the
largest in `{r} ∪ (T_{n−2} \ {2^m})`. `D = r − D(T_{n−2} \ {2^m})`.

The all-tower multiset `T_{n−2} \ {2^m}` has levels `n−2, …, m+1, m−1, …, 0` (level `m`
removed). Its alternating sum, computed by geometric series (pieces above level `m` keep
positions; pieces below shift by 1, flipping signs), is:

$$D(T_{n-2} \setminus \{2^m\}) = \frac{2^{n-1} - (-1)^n + (-1)^{n+m-1} \cdot 2^m}{3}$$

(verified `Fraction`-exact `n = 3,…,7`, all `m ≤ n−3`; e.g. `n=5, m=2`:
`D({8,2,1}) = 7 = (16−(−1)^5+(−1)^6·4)/3 = (16+1+4)/3 = 21/3`). Hence:

$$D = (2^{n-1} - 2^m) - \frac{2^{n-1} - (-1)^n + (-1)^{n+m-1} \cdot 2^m}{3}
= \frac{2^n + (-1)^n - c \cdot 2^m}{3},$$

where `c = 3 + (−1)^{n+m−1} ∈ {2,4}`. `D ≥ D(T_{n−2}) = (2^{n−1} + (−1)^n)/3` is equivalent to
`2^n − c·2^m ≥ 2^{n−1}`, i.e., `c·2^m ≤ 2^{n−1}`.

- `c = 2`: `2^{m+1} ≤ 2^{n−1}` iff `m ≤ n−2`. ✓ (since `m ≤ n−3` here).
- `c = 4` (when `m ≡ n−1 mod 2`): `2^{m+2} ≤ 2^{n−1}` iff `m ≤ n−3`. ✓ (since `m ≤ n−3`).
  Equality at `m = n−3`: `c = 4` (since `n−3 ≡ n−1 mod 2`), `4·2^{n−3} = 2^{n−1}`. ✓

### Case 2: Balanced second split (`s = r = (2^n − q)/2`)

The two equal fragments `s = r` are adjacent in the sorted order and cancel. The config reduces
to `{q} ∪ T_{n−1}` (one fragment plus the intact tower `T_{n−1}`). If `q = 2^a` (tower-tie
breakpoint for `q`), then `{2^a} ∪ T_{n−1}` has level `a` with count 2 (even, cancels), and

$$D = D(T_{n-1} \setminus \{2^a\}) = \frac{2^n + (-1)^n + (-1)^{n+a} \cdot 2^a}{3}$$

(same formula as Sub-case 1b with `n → n−1`, `m → a`). Then `D ≥ D(T_{n−2})` iff
`2^{n−1} ≥ |(−1)^{n+a}·2^a| = 2^a`, i.e., `a ≤ n−1`. ✓ (always). Equality when `a = n−2` and
`(−1)^{n+a} = −1` (giving `D = (2^n + (−1)^n − 2^{n−2})/3`; check: `2^n − 2^{n−2} = 3·2^{n−2}`,
`D = (3·2^{n−2} + (−1)^n)/3`; vs `D(T_{n−2}) = (2^{n−1} + (−1)^n)/3 = (2·2^{n−2} + (−1)^n)/3`;
`D − D(T_{n−2}) = 2^{n−2}/3 > 0`... hmm, not equality. Let me recheck.)

Actually for `a = n−1` (balanced first split too): `q = 2^{n−1}`, `s = r = (2^n − 2^{n−1})/2 = 2^{n−2}`.
This is the dyadic cascade! `D = D(T_{n−2})`. The formula gives
`(2^n + (−1)^n + (−1)^{2n−1}·2^{n−1})/3 = (2^n + (−1)^n − 2^{n−1})/3 = (2^{n−1} + (−1)^n)/3 = D(T_{n−2})`. ✓

### Case 3: `q = s` (two equal non-tower fragments)

The two equal fragments cancel. `D = D({r = 2^n − 2q} ∪ T_{n−1})`. The constraint `s ≤ r` gives
`q ≤ 2^n − 2q`, i.e., `3q ≤ 2^n`, so `r = 2^n − 2q ≥ 2^n/3 ≥ 2^{n−2}` (for `n ≥ 2`).

If `r ≥ 2^{n−1}` (i.e., `q ≤ 2^{n−2}`): `r` is largest, `D = r − D(T_{n−1}) = D(T_n) − 2q ≥ D(T_{n−2})`
iff `2q ≤ 2^{n−1}` iff `q ≤ 2^{n−2}`. ✓ (by assumption).

If `r < 2^{n−1}` (i.e., `q > 2^{n−2}`, but `q ≤ 2^n/3`): the two `2^{n−1}`'s (if `r` ties
tower) ... actually `r` might not tie a tower piece. But for a **vertex**, we need a second tie
condition beyond `q = s`. The possibilities are:
- `r = 2^c` (tower-tie for `r`): reduces to Case 1 with `r` as a tower fragment. ✓ (proved above).
- `r = q` (all equal, `3q = 2^n`): see Case 4. ✓
- `q = 2^a` (tower-tie for `q`, and `q = s`): reduces to Case 1 with `a = b`. ✓

### Case 4: All three equal (`q = s = r = 2^n/3`)

Two cancel, one remains. `D = D({2^n/3} ∪ T_{n−1})`. Since `2^n/3 < 2^{n−1}` (for `n ≥ 1`),
the largest is `2^{n−1}` (tower). Since `2^n/3 > 2^{n−2}` (for `n ≥ 2`, as `4/3 > 1`), the
non-tower piece `2^n/3` sits between `2^{n−1}` and `2^{n−2}` at position 2 (sign `−`):

$$D = 2^{n-1} - \frac{2^n}{3} + D(T_{n-2}) = D(T_{n-2}) + \frac{2^{n-1}}{3} \ge D(T_{n-2}). \quad\checkmark$$

### Summary of proved cases

Cases 1–4 cover all breakpoint types where the ties involve tower pieces or fragment-fragment
equalities. Specifically:
- **Case 1** (tower-tie for both cuts): Sub-cases 1a and 1b proved by block-contribution formula
  + parity-constrained geometric bound.
- **Case 2** (balanced second split): proved by pair cancellation + tower formula.
- **Case 3** (equal fragments, `q = s`): reduces to Cases 1 or 4 at a vertex.
- **Case 4** (all equal): proved directly.

The formula `D = D(T_n) − f(a,b)/3` (Case 1a) or `D = (2^n + (−1)^n − c·2^m)/3` (Case 1b), with
the parity constraint `c·2^m ≤ 2^{n−1}`, is the load-bearing identity. The dyadic cascade
(`q = s = 2^{n−2}`, Case 1 with `a = b = n−2`) attains `D = D(T_n) − 2^{n−1} = D(T_{n−2})`. ∎

---

**Verified but not fully proved (Type C — second split on a tower piece):** When the second mark
splits a tower piece `2^k` (not a fragment of the top), the config has two fragments from the top
split plus a modified tower. At a tower-tie breakpoint (`q = 2^a`, second cut `= 2^c`), the same
block-contribution + parity-constraint pattern applies (one non-tower piece in an all-tower
rest). Verified `D ≥ D(T_{n−2})` for all such breakpoints, `n = 3,…,7` (0 violations).
The algebraic proof follows the same geometric-sum computation; the formula is structurally
identical but with two removed tower levels (from the split tower piece) instead of two extra
levels. **This is a GAP in the general-`n` proof**, closing which would complete the lemma.

**Importable by:** `tail-count` (closes the 2-split sub-case of G1 for the top-fragment-split
type, all `n`), `tower-induction`, `gaps-leftover`.

**Verified.** Exact `Fraction` arithmetic on all 2-split breakpoints (Types A, B, and r-tower-tie)
of `T_n` for `n = 3, 4, 5, 6, 7`: minimum `D = D(T_{n−2})` in every case (1, 3, 5, 11, 21 resp.),
0 breakpoints below `D(T_{n−2})`. Formula matches direct computation at every breakpoint.
