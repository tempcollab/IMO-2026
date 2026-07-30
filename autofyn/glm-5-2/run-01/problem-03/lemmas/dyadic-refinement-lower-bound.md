# Lemma: dyadic-refinement-lower-bound (F-min)

**Statement.** For every balanced-split (dyadic) refinement `M` of `T_n = (2^n,…,1)` (tower
units, total `D_n = 2^{n+1}−1`), with `n ≥ 1`,

$$1 \;\le\; D(M) \;\le\; 2^n - 1.$$

In particular `D(M) ≥ 1 = 1/D_n` (real units), so Liu's dyadic tower resists every Xiang
refinement using only balanced splits, for all `n`. Equality `D = 1` (tower units) is attained
at the fully-cascaded all-1's refinement `e = (1,…,1)` (e.g. the balanced-pairs config
`{2^{n−1},2^{n−1},…,2,2,1,1,1}`).

**Proof.** By induction on `n` using `frontier-recursion`. Base `n=1`: `e_1∈{0,1}` gives
`D_1 = 1` (both `2^1−D_0 = 1` and `D_0 = 1`). Step `n≥2`: by IH `1 ≤ D_{n−1}(\bar e) ≤ 2^{n−1}−1`;
`e_n=1` ⇒ `D_n = D_{n−1} ∈ [1, 2^{n−1}−1] ⊆ [1, 2^n−1]`; `e_n=0` ⇒
`D_n = 2^n − D_{n−1} ∈ [2^{n−1}+1, 2^n−1] ⊆ [1, 2^n−1]`. Equality at the cascade
`e=(1,…,1)`: `D_n = D_{n−1} = … = D_0 = 1`. See `tower-induction` Lemma F-min; the
level-block-dominance proof in `tail-count` §5 is equivalent (largest odd-count level
contributes `+2^K`, rest `≥ −(2^K−1)`, giving `D ≥ 1`).

**Verified.** Exhaustive enumeration of all balanced refinements of `T_n` for n=1..6: min
`D=1`, all `D` odd, max `= 2^n−1`. Over all 2^n parity vectors n=1..7: `1 ≤ D_n(e) ≤ 2^n−1`
holds for every `e`; cascade `e=(1,…,1)` gives `D=1`.

**Closes:** the all-balanced-splits sub-case of lower-bound case (b) for ALL `n`.

**Importable by:** `tail-count`, `tower-induction`, `self-similar` (the balanced sub-case is
now closed for all n, unconditionally).
