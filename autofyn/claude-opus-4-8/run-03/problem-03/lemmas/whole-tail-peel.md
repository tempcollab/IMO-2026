# Lemma WHOLE-TAIL-PEEL (upper-bound closed region) — CERTIFIED (round 4)

**Statement (unconditional).** Let `a₁ ≥ … ≥ a_m` be a sorted profile, `m ≤ k+1`, sum `L`,
with `L/2 ≤ a₁ ≤ c(k)L` (where `c(k) = 2^k/(2^{k+1}−1) = (1+u_k)/2`, `u_k = 1/(2^{k+1}−1)`).
Then Xiang using `≤ k` cuts can force
```
    D(final) = 2a₁ − L      (exactly),   and   2a₁ − L ≤ u_k L.
```

**Proof.** Since `a₁ ≥ L/2`, the tail mass `Σ_{i≥2} a_i = L − a₁ ≤ a₁`, so `a₁` can be cut
into the `m−1` tail values `a₂,…,a_m` plus a leftover `ℓ = a₁ − (L−a₁) = 2a₁ − L ≥ 0`. This
uses `m−1 ≤ k` cuts (`m−2` if `ℓ=0`). Each `a_i` (`i≥2`) now appears twice; delete the `m−1`
cancelling pairs by certified Lemma P (cancelling-pair). The residual is the single piece
`{ℓ}`, so `D = ℓ = 2a₁ − L`. Finally `2a₁ − L ≤ u_k L ⟺ a₁ ≤ (1+u_k)L/2 = c(k)L`, using
`(1+u_k)/2 = (1 + 1/(2^{k+1}−1))/2 = 2^k/(2^{k+1}−1) = c(k)`. ∎

**Certification.** Arithmetic verified (`c(k)=(1+u_k)/2` exact; bound holds on 200 random
dominant profiles, `k ≤ 5`). Self-contained given certified Lemma P. Reviewer-approved round 4.

**Coverage.** Combined with the bisect branch (`a₁ ≥ c(k)L` ⇒ DELETE `a₁`, residual tail,
apply UB(k−1) via `u_{k−1}(L−a₁) ≤ u_k L`) this closes the ENTIRE range `a₁ ≥ L/2` for the
upper bound — the bisect branch, however, is *conditional on the inductive hypothesis UB(k−1)*
(not yet an established unconditional theorem). Only the whole-tail piece above is unconditional.

**Negative companion (recorded, not a lemma).** The mass-threshold subset-cover disjunction is
NON-EXHAUSTIVE for `a₁ < L/2`: witness `A=(0.44, 0.281, 0.279)`, `k=2` — every threshold move
fails (Branch 0/whole-tail need `a₁ ≥ L/2`; `j=1` peel size-1 sums `< θ₁=2/7`; `j=2` peel sum
`0.560 > a₁`), yet bisecting `a₁` gives `D = 0.002 ≤ 1/7 = u_2`. Verified exactly (D=1/500).
Conclusion: no mass-only residual bound closes `a₁ < L/2`; that regime needs a D-tracking
argument. Do NOT re-attempt subset-cover variants there.
