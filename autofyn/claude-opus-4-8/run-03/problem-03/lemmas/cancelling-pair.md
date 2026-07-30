# Lemma P (cancelling pair) — CERTIFIED round 1

**Statement.** For any finite multiset `S` and any value `v > 0`,
`D(S ∪ {v,v}) = D(S)`, where `D = Σ_i(−1)^{i+1} b_i` on the descending sort.

**Proof.** Insert two copies of `v` into the descending sort of `S`. Elements `> v` keep
their ranks and signs. The two new copies occupy consecutive ranks `r, r+1`, contributing
`(−1)^{r+1}v + (−1)^{r+2}v = 0`. Every element `< v` has its rank increased by exactly 2,
preserving parity and sign. Hence the alternating sum is unchanged. ∎

**Peel move (corollary).** One cut of a piece `P ≥ Q` into `(P−Q, Q)` creates a token equal
to an existing/other `Q`; by Lemma P the pair `{Q,Q}` may be deleted without changing `D` of
the remaining multiset, at every intermediate stage. So one cut converts the game to the game
on the reduced multiset (delete one `Q`, replace `P` by `P−Q`): piece count −1, total length
−2Q, eventual `D` unchanged. Bisection (`Q = P/2`) deletes `P` entirely for one cut.

Verified numerically (2000 random tests) by the reviewer, round 1. Approach-agnostic.
