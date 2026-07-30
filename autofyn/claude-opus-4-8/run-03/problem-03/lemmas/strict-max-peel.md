# Lemma PEEL (strict-max peel) — CERTIFIED (round 4)

**Statement.** Let `S` be a finite multiset of positive reals whose maximum `f₁` is *unique*
(strictly exceeds the second-largest `b₂`). Then
```
    D(S) = f₁ − D(S ∖ {f₁}).
```
Here `D(mult) = Σ_i (−1)^{i+1} b_i` on the descending sort, equivalently (Lemma M)
`D = μ{ t>0 : N(t) odd }` with `N(t)=#{pieces>t}`.

**Proof.** Put `R = S ∖ {f₁}`, `max R = b₂ < f₁`. By Lemma M, `N_S(t) = 1[t<f₁] + N_R(t)`.
- On `[b₂,f₁)`: `N_R=0`, so `N_S=1` (odd) — contributes `f₁ − b₂`.
- On `[f₁,∞)`: `N_S=0`.
- On `[0,b₂)`: `N_S = 1 + N_R` is odd iff `N_R` even, so its odd-measure there is
  `b₂ − μ{t∈[0,b₂): N_R odd} = b₂ − D(R)` (since the odd-set of `R` lies in `[0,b₂)`).
Summing: `D(S) = (f₁−b₂) + (b₂−D(R)) = f₁ − D(R)`. ∎

**Certification.** Verified exactly on 5000 random multisets (max error 0). Proof is
self-contained given certified Lemma M. Reviewer-approved round 4.

**Note.** parity-measure-potential's "a=1 splitting identity" (`D(S)=f₁−D(S_L)` when `f₁`
exceeds every other piece) is the same statement; this file subsumes both.
