# Lemma: parallel-halving-saturates-tower (U1)

**Statement.** Let `T_n = (2^n, 2^{n−1}, …, 2, 1)/D_n` (real units, `D_n = 2^{n+1}−1`).
Xiang's **parallel-halving** response — one mark splitting each of the tower's `n` largest
pieces `2^k/D_n` (`k = 1,…,n`) into two equal halves `2^{k−1}/D_n, 2^{k−1}/D_n` — uses exactly
`n` marks and produces the balanced-pairs multiset

$$B_n \;=\; \frac{1}{D_n}\bigl(\,2^{n-1},2^{n-1},\;2^{n-2},2^{n-2},\;\ldots,\;2,2,\;\underbrace{1,1,1}_{\text{two halves of }2\text{ + unsplit bottom}}\,\bigr),$$

whose alternating sum is `D(B_n) = 1/D_n` exactly. Hence

$$\min_{\text{Xiang refinements of }T_n} D \;\le\; \frac{1}{D_n}.$$

Combined with the lower bound (`T_n` resists every refinement, `D ≥ 1/D_n`), this gives
`min_Xiang D(T_n) = 1/D_n` exactly: the tower is a **tight** config for the upper bound.

**Proof.** (Tower units.) Splitting `2^k` into `2^{k−1}+2^{k−1}` for each `k=1,…,n` turns the
`n` largest tower pieces into pairs of halves, leaving the bottom `1` unsplit. The result
`{2^{n−1},2^{n−1}, 2^{n−2},2^{n−2}, …, 2,2, 1,1,1}` is sorted (each pair equal, consecutive
pairs `≥`). In the alternating sum each equal pair occupies adjacent positions `(2j−1, 2j)`
and cancels (`+2^{k−1} − 2^{k−1} = 0`); one piece (the unsplit bottom `1`) remains at the last
position `2n+1` (odd, sign `+`), so `D(B_n) = 1` (tower units) `= 1/D_n` (real units). Total:
`2·(2^{n−1}+…+1) + 1 = 2(2^n−1)+1 = 2^{n+1}−1 = D_n` ✓. See `majorization-upper` Lemma U1.

**Verified.** Exact `Fraction` n=1..6: `D(B_n)=1` tower units ✓, total `= D_n` ✓.

**Importable by:** `majorization-upper` (the upper-bound witness against the tower), any
approach needing the equality-attaining config for `c(n) = 2^n/D_n`.
