# Lemmas C1–C3: term density and large-prime pair capacity

**Certified** (proof-reviewer, round 2). Source: `approaches/large-prime-capacity-counting.md` Steps 1–3.
These are the counting facts; they are rigorous and reusable. NOTE: they do NOT close the crux —
the same approach proves the capacity route cannot force L(X)=0 (bounds only a positive fraction).

Notation: N(X) := #{terms in [a_1, X]}; μ_p(X) := #{terms in [a_1,X] divisible by p}; P_max := max primes(a_1).

## Lemma C1 (term density)
For all X ≥ a_1,  ⌊X/a_1⌋ − 1 ≤ N(X) ≤ X;  in particular N(X) = Θ(X).
Number of unordered term-pairs in [a_1,X] is ≥ C(⌊X/a_1⌋−1, 2) = (1+o(1))·X²/(2 a_1²).
*Proof.* Lower: multiples k·a_1, 2 ≤ k ≤ ⌊X/a_1⌋, are terms (certified: every multiple of a_1 is a term),
giving ⌊X/a_1⌋−1 distinct terms in [a_1,X]. Upper: terms are distinct integers in [1,X]. ∎

## Lemma C2 (per-prime pair capacity)
For every prime p, #{unordered term-pairs {A,B} ⊆ [a_1,X] : p | gcd(A,B)}
≤ C(μ_p(X), 2) ≤ C(⌊X/p⌋, 2) ≤ (X/p)²/2.
*Proof.* Both members are p-divisible terms (μ_p(X) of them, all multiples of p in [1,X], so ≤ ⌊X/p⌋);
count pairs among them. Double counting. ∎

## Lemma C3 (large-prime capacity is a bounded fraction)
Let L(X) := #{term-pairs in [a_1,X] with some prime p > P_max dividing gcd}. Then
L(X) ≤ (X²/2)·Σ_{p>P_max} 1/p² < 0.21·(X²/2).
*Proof.* Sum Lemma C2 over p > P_max (overcounts each large pair ≥ once). Elementary tail bound:
Σ_{p>y} 1/p² ≤ Σ_{n>y} 1/n² < 1/y (telescoping via 1/(n(n−1))). Sharply, Σ_p 1/p² = P(2) = 0.452247…;
removing the p=2 term (P_max ≥ 2 always) gives Σ_{p>P_max} 1/p² ≤ P(2) − 1/4 < 0.2023. ∎
(Verified numerically: P(2) − 1/4 = 0.20225.)

## Reusability / caveat
Reusable by any counting-based approach. CRITICAL caveat (also proved in the source approach): C3 bounds
only a positive FRACTION of pairs, never zero, so capacity counting alone cannot force the relevant-prime
set finite — the localize-to-globalize step is un-closable in this framing without a circular periodicity
input. Use these as building blocks, not as a route to the crux.
