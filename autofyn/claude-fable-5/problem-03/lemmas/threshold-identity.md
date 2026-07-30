# Lemma: threshold-identity (discrepancy identity, layer-cake form, tied-pair invariance)

*Proposed by the discrepancy-halving builder (Identities 1–2, Lemma 3) and, independently, the tie-structure-variational builder (Lemma D §4), round 1. **CERTIFIED by the proof-reviewer, round 2**: both derivations re-checked line by line; they agree (N(t) with ">" vs "≥" differ on a finite set, measure zero). Verified in exact arithmetic on random multisets.*

## Statement

Let S be a finite multiset of nonnegative reals, sorted p₁ ≥ p₂ ≥ … ≥ p_m, with sum T. Define the **discrepancy**

Δ(S) := p₁ − p₂ + p₃ − p₄ + ⋯ (alternating sum; last term +p_m if m odd).

Then:

1. **(Discrepancy identity.)** odd(S) = (T + Δ(S))/2, where odd(S) is the odd-rank sum (= Liu Bang's claiming value by Lemma G). In particular odd(S) ≥ T/2 always.
2. **(Threshold / layer-cake identity.)** With N(t) := #{p ∈ S : p > t},
   Δ(S) = ∫₀^∞ 1[N(t) is odd] dt = λ({t > 0 : N(t) odd}).
3. **(Tied-pair invariance.)** For any x ≥ 0, Δ(S ∪ {x, x}) = Δ(S). Consequently a final multiset consisting of exactly-tied pairs plus one residual piece x has Δ = x, and one of only tied pairs has Δ = 0.
4. **(Zero-padding.)** Adjoining entries of size 0 changes neither odd(S) nor Δ(S).

Δ(S) is independent of tie-breaking in the sort (exchanging equal entries permutes equal summands).

## Proof

**(1)** odd(S) + even(S) = T and odd(S) − even(S) = Δ(S) by definition; add and divide by 2. Each term (p_{2i−1} − p_{2i}) ≥ 0, so Δ ≥ 0 and odd(S) ≥ T/2.

**(2)** Each p_i = ∫₀^∞ 1[p_i > t] dt (layer cake for a single number). Hence
Δ(S) = ∫₀^∞ Σ_i (−1)^{i+1} 1[p_i > t] dt (interchange is finite additivity of the integral over a finite sum; integrand supported on [0, p₁], bounded by m). For fixed t, since the list is sorted decreasing, p_i > t holds exactly for i = 1, …, N(t); so the inner sum is Σ_{i=1}^{N(t)} (−1)^{i+1} = 1 if N(t) odd, 0 if even. ∎

**(3)** The count function of S ∪ {x, x} is N_S(t) + 2·1[x > t], of the same parity as N_S(t) for every t; apply (2). ∎

**(4)** Positive entries keep their ranks; zeros contribute 0 to any alternating or rank sum regardless of position among the zeros. ∎

## Equivalent form (used by tie-structure-variational)

With N′(t) := #{p ≥ t}: odd(S) = ∫₀^∞ ⌈N′(t)/2⌉ dt and T = ∫₀^∞ N′(t) dt, so odd(S) − T/2 = ½ λ{t : N′(t) odd}; N′ and N differ only at the finitely many values t ∈ S, a null set, so this is the same Δ.

## How to use it

For the stick game (T = 1), Liu's value on final multiset S is (1 + Δ(S))/2, so the target c(n) = 2^n/(2^{n+1}−1) is equivalent to sup_a inf_x Δ = u := 1/(2^{n+1}−1).
