# Lemma OSR-cap (one-sided walk sub-case of the a=0 lower bound) — CERTIFIED (round 8)

**Statement.** In the setting of Lemma OSR (`order-statistic-reformulation`), let
`S_k = Σ_{i≤k} e_i` be the signed merge walk (`S_0 = 0`). If `S_k ≤ 1` for every `k = 1,…,m`
(equivalently `N_F(t) ≤ N_B(t) + 1` for all `t`, i.e. `g = N_F − N_B ≤ 1`), then `D(S) ≥ 1`.

**Proof.** Let `P_k := Σ_{i≤k} d_i` be the partial sums of the coefficients `d_i` of Lemma OSR.
Since `Σ_{i≤k}(−1)^{i+1} = 1[k odd]`, we have `P_k = 1[k odd] − S_k`. By parity, `S_k ≡ k (mod 2)`.
For `k` odd, `S_k` is odd and `S_k ≤ 1` gives `P_k = 1 − S_k ≥ 0`. For `k` even, `S_k` is even and
`S_k ≤ 1` forces `S_k ≤ 0`, so `P_k = −S_k ≥ 0`. Hence `P_k ≥ 0` for all `k`. Abel summation
(with `v_{m+1} := 0`, `w_k := v_k − v_{k+1} ≥ 0` by descending order):
```
    Σ_{i=1}^m d_i v_i = Σ_{k=1}^m P_k (v_k − v_{k+1}) = Σ_{k=1}^m P_k w_k ≥ 0.
```
By Lemma OSR, `D(S) = 1 + Σ_i d_i v_i ≥ 1`. ∎

**Certification.** Self-contained on Lemma OSR + Abel summation. Strictly generalizes the
previously-closed `0 ≤ g ≤ 1` floor case (drops the lower bound on `g`). Verified: over all sampled
admissible refinements with `max_k S_k ≤ 1`, `D(S) ≥ 1` with no exception (reviewer, round 8).
Reviewer-approved round 8.

**Scope note.** This closes only the regime where the merge walk never leads by two. The hard
residual (`max_k S_k ≥ 2`, `|F| ≥ 3`) is NOT covered; the reviewer-verified negative fact is that
the prefix form of the aggregate inequality fails ~27% of the time (8043/30000), so no
running-deficit monovariant can close the residual — it needs a genuine aggregate transport.
