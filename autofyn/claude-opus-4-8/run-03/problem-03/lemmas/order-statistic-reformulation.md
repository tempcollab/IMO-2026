# Lemma OSR (order-statistic reformulation of the a=0 lower bound) — CERTIFIED (round 8)

**Statement.** Let `S = F ⊔ B` be an admissible `a=0` refinement of `C_n = {2^0,…,2^n}`
(in units of `u`): `F` = fragments of the top `2^n` (each `≤ 2^{n−1}`, `ΣF = 2^n`), `B` a
`≤(n−1)`-cut refinement of `C_{n−1}` (each piece `≤ 2^{n−1}`, `ΣB = 2^n − 1`). Merge `S` in
strictly-descending value order `v_1 > … > v_m` (`m = |F|+|B|`; ties split arbitrarily) with
signs `e_i = +1` if `v_i ∈ F`, `e_i = −1` if `v_i ∈ B`. Then
- (a) `D(S) = Σ_{i=1}^m (−1)^{i+1} v_i`  (certified Lemma R applied to `S`);
- (b) `Σ_{i=1}^m e_i v_i = ΣF − ΣB = 2^n − (2^n − 1) = 1`;
- hence `D(S) − 1 = Σ_i d_i v_i`, `d_i := (−1)^{i+1} − e_i ∈ {−2,0,+2}`, and
```
    D(S) ≥ 1  ⟺  Σ_{B at odd rank} v_i  ≥  Σ_{F at even rank} v_i.
```

**Proof.** (a) is certified Lemma R (`reduction-odd-rank`) on the descending sort of the full
multiset `S`. (b) collects `+f` for each `f∈F` and `−b` for each `b∈B`; the total is
`ΣF − ΣB = 1`, the superincreasing signature of the ladder. Subtracting (b) from (a) gives
`D(S) − 1 = Σ_i((−1)^{i+1} − e_i)v_i`. Coefficient analysis: for `i` odd, `(−1)^{i+1} = +1`, so
`d_i = 0` if `e_i = +1` (F) and `d_i = +2` if `e_i = −1` (B); for `i` even, `(−1)^{i+1} = −1`, so
`d_i = −2` if `e_i = +1` (F) and `d_i = 0` if `e_i = −1` (B). Thus
`D(S) − 1 = 2(Σ_{B at odd rank} v − Σ_{F at even rank} v)`, giving the stated equivalence. ∎

**Certification.** Self-contained on certified Lemma R + the ladder mass identity. Identities
`D(S) = Σ(−1)^{i+1}v_i`, `Σe_iv_i = 1`, and `D−1 = 2(Σ_{B odd} − Σ_{F even})` verified exact on
20000 admissible refinements `n=2..6` (reviewer, round 8); aggregate inequality held in all cases,
`min D(S) = 1.0003 > 1`. Cleaner than Lemma MID (no integration). Reviewer-approved round 8.
