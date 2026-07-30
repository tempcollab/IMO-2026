# Lemma (Prop C): sole-connector terms avoid the a_1-lattice

**Certified** (proof-reviewer, round 2). Source: `approaches/cofactor-recruitment-smoothness.md` Step 4.

Notation: the greedy sequence a_1, a_2, … with a_1 > 1; P := primes(a_1); D := a_1.

## Statement
If two terms A, B of the sequence satisfy primes(A) ∩ primes(B) = {q} with q ∉ P
(in particular whenever q > P_max = max P), then D ∤ A and D ∤ B.

## Proof
Suppose D | A. Then primes(A) ⊇ primes(D) = P. Since B is a term, B shares a prime with
a_1 (certified: every two terms share a prime, and every term is divisible by a prime of P),
so some p ∈ P divides B. But p ∈ P ⊆ primes(A) and p | B, so p ∈ primes(A) ∩ primes(B) = {q},
forcing p = q. This contradicts q ∉ P. Hence D ∤ A; by symmetry D ∤ B. ∎

## Reusability
Elementary; depends only on the certified fact "every two terms share a prime and every term
is divisible by a prime of P." Confines any large-prime sole-connector witness strictly between
two consecutive multiples of a_1 (a length-<a_1 window). Reusable by any approach reasoning about
sole-connector pairs.
