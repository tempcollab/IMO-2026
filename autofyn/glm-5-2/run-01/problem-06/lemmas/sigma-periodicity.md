# Lemma: σ-periodicity (conditional on B1')

## Status
CERTIFIED with CORRECTION (round 3, proof-reviewer), CONDITIONAL on B1'. Originally certified round 2; the round-2 `T'` formula was BUGGY (drops a factor of `p` when a prime `p ≤ R` divides `T` but not `L`). Corrected below. Proved in `approaches/bounded-diff-finite-state.md` Lemma 5. Verified empirically for `a_1=15` (`T=8, L=30, T'=8·7·11·13=8008`) and for `a_1=35` (the round-2 formula FAILED here: `T=34, L=210, p=17` with `17≤35, 17∤210, 17|34` — the 17-component has minimal period `578=17·34`, but the round-2 formula gave `lcm(34,17)=34`, which is NOT a period).

## Statement
Assume B1' holds for steps `≤ n` (i.e. `a_i = b_i` for `i ≤ n`, where `b_i` is the small-prime greedy). Let `N` be the stabilization index of `F'_n`, `B` the fixed `L`-periodic small-prime admissible set, `T = |B ∩ [0,L)|`, `L = ∏_{p ∈ ∪M'_∞} p` (kernel product). Then for `i ≥ N` the small-prime support `σ_i = σ(a_i) = supp(a_i) ∩ P_R` is periodic with period
```
T' := lcm( T, {p·T : p ≤ R, p ∤ L, p prime} )  =  T · ∏_{p ≤ R, p ∤ L, p prime} p
```
(a fixed finite constant). [ROUND-3 CORRECTION: the round-2 formula `lcm(T, {p ≤ R : p ∤ L})` was too small — it dropped the factor `p` whenever `p | T` and `p ∤ L`. The correct period uses `p·T`, not `p`, in the lcm, because the `p`-divisibility of `b_i` cycles with period `p·T` (`p` blocks of `T`), and `lcm(T, p·T) = p·T` regardless of whether `p | T`.] Over one `T'`-period the value lifts by `L' := (T'/T)·L` (an integer). Each `σ*`-class `{a_i : σ_i = σ*} ∩ [N,n]` is, as a set of values, the truncation of a union of `c* := |{r ∈ [0,T') : σ(b_{N+r}) = σ*}| ≥ 1` arithmetic progressions with common difference `L'`. Finally, every prime factor of `L'` is `≤ R` (factors of `L` lie in `S ⊆ P_R`; factors of `T'/T = ∏{p ≤ R, p ∤ L}` lie in `P_R`), hence `gcd(L', q) = 1` for every prime `q > R`.

## Proof (sketch)
For `i ≥ N`, `b_{i+T} = b_i + L` (Theorem 1). For `p ≤ R`: if `p | L` then `b_{i+T} ≡ b_i (mod p)`, so `p`-divisibility is `T`-periodic; if `p ∤ L` then `b_{i+T} ≡ b_i + L (mod p)` with `gcd(L mod p, p) = 1`, so the residue cycles through all `p` residues in `p` blocks of `T`. Therefore `σ_i` is `T'`-periodic. The rest follows. ∎

## Scope / reusability
The structural input for any density/counting argument on B1' (`v_p` union bound, sieve). Conditional on B1' holding inductively — so it is an *induction* tool, not a standalone fact.
