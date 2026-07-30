# Lemma: block-contribution-formula (F-block)

**Statement.** Let `M` be a dyadic (all-balanced-splits) refinement of `T_n`. Let `n_k` =
number of pieces of value `2^k` (`k = 0,…,n`) and `C_k = Σ_{j>k} n_j`. Then the alternating
sum of the sorted-descending multiset `M` is

$$D(M) \;=\; \sum_{k=0}^{n} 2^k\,(-1)^{C_k}\,(n_k \bmod 2).$$

In particular `D(M)` depends only on the split-parity vector `e_k := c_k \bmod 2` (where
`c_k` = number of splits of value-`2^k` pieces), via `n_k \bmod 2 = (1 + c_k) \bmod 2 =
(1 - e_k) \bmod 2` and `C_k \bmod 2 = Σ_{j>k}(1-e_j) \bmod 2`.

**Proof.** In the sorted multiset, all value-`2^k` pieces form a contiguous block occupying
positions `C_k+1,…,C_k+n_k`. The block's total signed contribution is
`2^k Σ_{i=1}^{n_k} (−1)^{C_k+i+1} = 2^k (−1)^{C_k+1} Σ_{i=1}^{n_k}(−1)^i`, and
`Σ_{i=1}^{n_k}(−1)^i = 0` (even `n_k`) or `−1` (odd `n_k`), giving `2^k(−1)^{C_k}(n_k mod 2)`.
Summing over `k`. The parity-only dependence follows from
`n_k = 1 + 2c_{k+1} − c_k` (a split at level `k+1` adds two `2^k` pieces; a split at level `k`
removes one `2^k`). See `tower-induction` Lemma F-block.

**Verified.** Matches direct alternating-sum recomputation on every balanced refinement of
`T_n` for n=1..6 (counts 2,4,10,28,79,224; 0 mismatches).

**Importable by:** any approach computing `D` for dyadic refinements; the engine for
`frontier-recursion` and `dyadic-refinement-lower-bound`.
