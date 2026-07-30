# Lemma: single-split-top-lower-bound

**Statement.** Let `T_n = (2^n, 2^{n−1}, …, 2, 1)` (tower units, total `D_n = 2^{n+1}−1`), `n ≥ 1`.
Suppose Xiang uses exactly ONE mark, splitting the top piece `2^n` into `p + q` with
`p ≥ q > 0`, `p + q = 2^n` (so `q ∈ (0, 2^{n−1}]`). Then the alternating sum of the refined
multiset satisfies

$$D \;\ge\; D(T_{n-1}) \;=\; \frac{2^n + (-1)^{n-1}}{3} \;\ge\; 1 \;=\; \frac{1}{D_n}\text{ (real units)},$$

with the minimum attained on the whole plateau `q ∈ [2^{n-2}, 2^{n-1}]` (value `D(T_{n-1})`).
Moreover `D` is a continuous piecewise-linear function of `q` on `(0, 2^{n-1}]` with slopes in
`{0, −2}` (non-increasing).

**Proof.** `p = 2^n − q ≥ 2^{n−1}`, the largest piece of `T_{n−1}`, so `p` occupies position 1
(sign `+`); writing `R = {q} ∪ T_{n−1}` sorted, `D(M) = p − D(R) = (2^n − q) − D(R)`. On each
segment `S_s := (2^{s−1}, 2^s]` (`s = 0,…,n−1`), `q` lands between tower pieces `2^s` (above)
and `2^{s−1}` (below); a direct sign count gives `D(R) = D({2^{n−1},…,2^s}) + (−1)^{n−s} q ± D(T_{s−1})`,
so `D(M) = 2^n − D({…2^s}) ∓ D(T_{s−1}) − 2q` if `n−s` even (slope `−2`) and `D(M) = 2^n − D({…2^s}) − D(T_{s−1})`
if `n−s` odd (slope `0`). Hence `D` is non-increasing in `q`; the minimum is at `q = 2^{n−1}`
(top of segment `S_{n−1}`, where `n−s = 1` is odd ⇒ plateau at the constant value, which by
the balanced-split recursion `frontier-recursion` equals `D(T_{n−1})`). `D(T_{n−1}) ≥ 1`
(`frontier-recursion` closed form, equality at `n=1,2`). See `tail-count` §4.

**Verified.** Exact `Fraction` brute-force on `T_n` for n=2,3,4 (grid step 1/512, all cut
positions dyadic and non-dyadic): min `D = D(T_{n−1})` ✓, non-increasing in `q` ✓ (0
violations), plateau `[2^{n−2}, 2^{n−1}]` at `D(T_{n−1})` ✓.

**Closes:** lower-bound case (b-i) (exactly one split of the top) for ALL `n`, standalone.

**Importable by:** `tail-count`, `tower-induction` (the single-split sub-case of case (b) is
now closed unconditionally).
