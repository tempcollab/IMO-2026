# Lemma ATT (MID-core / lower-bound attainment, D=1) — CERTIFIED (round 12)

**Certification (round 12).** Reviewer-verified independently by exact arithmetic for `n=2..6`
(D=1 in every case) and confirmed the multiset structure. Admitted.

**Statement.** For every `n ≥ 2` the lower bound `D ≥ 1` for refinements of `C_n` is **tight**: take
the tail `B = C_{n-1} = {2^0,2^1,…,2^{n-1}}` uncut (`ΣB = 2^n−1`) and the top-piece fragmentation
`F = {2^{n-1}, 2^{n-2}, …, 2, 1, 1}` (`ΣF = (2^n−1)+1 = 2^n`, `|F| = n+1 ≥ 3`, F-cuts `= n`,
`c_B = 0`, total budget `n ≤ n`). The merged descending multiset is
`2^{n-1},2^{n-1},2^{n-2},2^{n-2},…,2,2,1,1,1`: every value `2^{n-1},…,2` occurs twice (a `+x,−x`
cancelling pair at consecutive odd/even positions, Lemma P) and the value `1` occurs three times
(contributing `1−1+1=1`). Hence
```
        D = 1   exactly.
```

**Consequence.** `min_R D(C_n) = 1`, so minimax `D = u_n` and `c(n) = 2^n/(2^{n+1}−1)`; the lower
bound, once GAP-EXTR/MID-core is proven, is sharp. This same multiset is also the tight UPPER witness
(Xiang forces `D` down to `1`).

**Scope.** Attainment/tightness only. Confirms the answer; does not prove the lower bound `D≥1`
(that is GAP-EXTR/MID-core, open).
