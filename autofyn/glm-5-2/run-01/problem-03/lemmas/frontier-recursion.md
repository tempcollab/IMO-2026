# Lemma: frontier-recursion (F-rec)

**Statement.** Let `T_n = (2^n, 2^{n−1}, …, 2, 1)` (tower units, total `D_n = 2^{n+1}−1`).
Define, for any balanced-split refinement `M` of `T_n`, the parity vector
`e = (e_1, …, e_n) ∈ {0,1}^n` where `e_k = c_k mod 2` and `c_k` = number of balanced splits
of value-`2^k` pieces (`e_0 = 0` fixed). Let `D_n(e_1,…,e_n)` denote the alternating sum of
the resulting multiset. Then

$$D_n(\bar e, e_n=0) \;=\; 2^n - D_{n-1}(\bar e), \qquad D_n(\bar e, e_n=1) \;=\; D_{n-1}(\bar e), \qquad D_0 = 1,$$

where `\bar e = (e_1, …, e_{n−1})`. In particular (the unsplit-tower special case `e ≡ 0`)

$$D(T_n) + D(T_{n-1}) = 2^n, \qquad D(T_0) = 1, \qquad D(T_n) = \frac{2^{n+1} + (-1)^n}{3} \ge 1,$$

with equality `D(T_n) = 1` at `n = 0, 1`. Also, a balanced split of the top piece `2^n` of
`T_n` gives `D_new = 2^n − D(T_n) = D(T_{n−1})`.

**Proof.** See `tower-induction` Lemma F-rec (parity-block telescoping via the block-contribution
formula `block-contribution-formula`). The level-`n` block contributes `2^n·[e_n=0]`; for
`k<n`, `C_k^{(n)} ≡ (1+e_n) + C_k^{(n−1)} (mod 2)`, so each lower block's sign flips iff
`e_n=0`. Unwinding gives the two recursions; base `D_0 = 1`. The unsplit identity
`D(T_n)+D(T_{n−1})=2^n` is the case `e≡0`; the closed form follows from the geometric sum
`D(T_n) = 2^n − 2^{n−1} + … + (−1)^n = (2^{n+1}+(−1)^n)/3`.

**Verified.** Exact `Fraction`: n=0..8 (`D(T_n)=1,1,3,5,11,21,43,85,171`); frontier recursion
holds n=1..8; closed-form integer and `≥1` for all n≥0.

**Importable by:** any approach needing the dyadic-tower alternating-sum identity, the
balanced-split reduction `T_n → T_{n−1}`, or the inductive scaffold for the balanced sub-case
of lower-bound case (b). Subsumes tail-count's `balanced-split-frontier-recursion`.
