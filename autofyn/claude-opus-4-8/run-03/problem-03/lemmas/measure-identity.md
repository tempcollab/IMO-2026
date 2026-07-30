# Lemma M (parity–measure identity) + toggle calculus — CERTIFIED round 1

**Statement.** For a finite multiset of positive lengths, `N(t) := #{i : b_i > t}`. Then
`D = Σ_i (−1)^{i+1} b_i = ∫_0^∞ 𝟙[N(t) odd] dt = measure{ t > 0 : N(t) odd }`.

**Proof.** `b_i = ∫_0^∞ 𝟙[b_i > t] dt`, so `D = ∫_0^∞ Σ_i(−1)^{i+1}𝟙[b_i>t] dt`
(finite sum of integrable functions). Fix t: sorted descending, the pieces exceeding t are
exactly ranks `1..N(t)`, so `Σ_{i=1}^{N(t)}(−1)^{i+1} = 1` if `N(t)` odd, `0` if even.
Integrate. The odd-set ⊆ `[0, b_1)`. ∎

**Corollary.** If every distinct value has even multiplicity, `N(t)` is even for all t, so
`D = 0`.

**Toggle calculus.** Replacing a piece `s` by `s_1 ≥ s_2` (`s_1+s_2=s`) changes `N` by
`+1` on `[0,s_2)`, `0` on `[s_2,s_1)`, `−1` on `[s_1,s)`; it flips the parity of `N` exactly
on `E = [0,s_2)∪[s_1,s)` (measure `2s_2`). Cumulatively the final odd-set is
`O_0 △ E_1 △ … △ E_r`, and one cut changes `D` by at most `2s_2 ≤ s`.

Verified numerically (2000 random multisets) by the reviewer, round 1. Approach-agnostic.
