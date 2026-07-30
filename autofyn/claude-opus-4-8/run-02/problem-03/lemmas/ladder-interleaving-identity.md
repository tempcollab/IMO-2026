# Lemma: Ladder-interleaving identity (extremal base case b=0 of GAP L)

Setting (P3, dyadic integer normalization). Let `L` be the uncut dyadic ladder
`L = {2^{n−1}, 2^{n−2}, …, 2, 1}` (so `ΣL = 2^n − 1`, `θ := 2^{n−1}`), and let `π_0` be ANY finite
positive multiset with `Σπ_0 = 2^n` (in the base case `b=0` of the peel, `F' = L` and `π_0` is a
partition of `2^n` into `a_0+1 ≤ n+1` parts; the identity holds for any such multiset with the
stated total). `D̃(P) = Σ_j (−1)^{j−1} w_j` is the value-only alternating sum of the descending
sort `w_1 ≥ w_2 ≥ …` (certified Lemma G, tie-invariant).

Form the descending merge `G := π_0 ⊎ L`, `w_1 ≥ … ≥ w_N` (`N = |π_0| + n`). Colour each element
**red** if it is a part of `π_0`, **blue** if it is a part of `L`.

**(★-id) identity.**
```
   D̃(π_0 ⊎ L) = 1 + 2·( Σ_{blue at odd rank} w_j − Σ_{red at even rank} w_j ).
```
Consequently
```
   D̃(π_0 ⊎ L) ≥ 1   ⟺   (★)  Σ_{blue at odd rank} ≥ Σ_{red at even rank},
```
with `D̃ = 1` **iff** equality in `(★)`. Consistency with the certified (FLOOR) reduction:
`I_n = Σ_{red even} − Σ_{blue odd}`, so `I_n ≤ 0 ⟺ (★)`.

**Proof.** Write `s_j := (−1)^{j−1}` (`+1` at odd rank, `−1` at even rank), so
`D̃(G) = Σ_j s_j w_j` (Lemma G). Assign the colour sign `τ_j := +1` if `w_j` is red, `−1` if blue.
Summing colour signs,
```
   Σ_j τ_j w_j = Σ_{red} − Σ_{blue} = Σπ_0 − ΣL = 2^n − (2^n − 1) = 1.        (C)
```
Subtract (C) from `D̃(G)`:  `D̃(G) − 1 = Σ_j (s_j − τ_j) w_j`. Evaluate `s_j − τ_j` by colour and
rank parity:  red odd `(+1)−(+1)=0`;  red even `(−1)−(+1)=−2`;  blue odd `(+1)−(−1)=+2`;
blue even `(−1)−(−1)=0`. Hence `Σ_j(s_j−τ_j)w_j = 2Σ_{blue odd} − 2Σ_{red even}`, giving (★-id). ∎

**Well-definedness.** `D̃(G)` is tie-break-independent (Lemma G) and (C) is exactly `1` under any
tie-break, so the bracket `Σ_{blue odd} − Σ_{red even}` is well-defined (the individual sums may
depend on tie-break; their difference does not).

**Certified corollaries (unconditional).**
- (a) If `M := N_{π_0} − N_L ≤ 1` on `(0,θ)` then `⌊M/2⌋ ≤ 0` pointwise, so `I_n ≤ 0` and
  `D̃(π_0⊎L) ≥ 1` (closes the `M≤1` region; ≈88% of sampled base configs).
- (b) Exact ladder value `D̃(L) = (2^n − (−1)^n)/3` (`= 1,1,3,5,11,21,…`); with the certified
  difference bound `D̃(π_0⊎L) ≥ |D̃(π_0) − D̃(L)|`, the shell `|D̃(π_0) − D̃(L)| ≥ 1` is closed.
- (c) `n=1`: `D̃(π_0 ⊎ {1}) ≡ 1` for every partition `π_0` of `2` (both sides of (★) are `0`).

**Verification (reviewer, exact `Fraction`).** (★-id) holds with `0` mismatches and
`I_n = Σ_{red even} − Σ_{blue odd}` with `0` mismatches over `3·10³` random `π_0` per `n=1..6`
(reviewer's independent re-derivation), consistent with the builder's `0`/`1.8·10⁵`. Base-case
minimum `min_{π_0} D̃(π_0⊎L) = 1` over all integer partitions of `2^n` into `≤n+1` parts, `n≤6`
(reviewer enumeration).

**Status of the base case (NOT closed by this lemma).** (★-id) *reduces* the extremal base case
`b=0` to the single combinatorial inequality (★). (★) is proved on the two regions (a),(b) and for
`n=1`, but the residual cross-block ladder-dominance form of (★) (GAP-P1′-a) is OPEN, and the
reduction of general `b` to `b=0` (GAP-P1′-b) is OPEN. This lemma certifies only the IDENTITY and
its three closed sub-regions.

Origin: `approaches/peel-scale-rank-induction.md` §10.2 (round 11). Self-contained from Lemma G.
