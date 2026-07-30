# Lemma (Generalized Prop C / GPC): terms sharing no small prime are off the a_1-lattice

**Certified** (proof-reviewer, round 4). Sources: reduced-process-identity §3a, self-dual-clutter-grading
Lemma 6, covering-small-part-descent (PROPC note). Strictly generalizes the singleton
`sole-connector-off-lattice.md` (Prop C).

Notation: greedy sequence a_1<a_2<…; P := primes(a_1); P_max := max P. A prime is *small* if ≤ P_max.
For m>1, S(m) := primes(m) ∩ [2,P_max].

## Statement
If two terms A, B share no small prime — i.e. primes(A) ∩ primes(B) ⊆ {primes > P_max}, equivalently
S(A) ∩ S(B) = ∅ — then a_1 ∤ A and a_1 ∤ B (regardless of how many large primes they share).

## Proof
Suppose a_1 | A. Then primes(A) ⊇ primes(a_1) = P. Since B is a term and a_1 is a term, the certified
fact "every two terms share a prime" gives a prime dividing both B and a_1; that prime lies in P (it
divides a_1), call it p ∈ P. Then p ∈ P ⊆ primes(A) and p | B, so p ∈ primes(A) ∩ primes(B); but
p ≤ P_max is small, contradicting S(A) ∩ S(B) = ∅. Hence a_1 ∤ A. By symmetry (swap A,B) a_1 ∤ B. ∎

## Reusability
Uses only the certified facts "every two terms share a prime" and "a_1 | A ⇒ P ⊆ primes(A)"; never
uses that the shared large-prime set is a singleton, so it supersedes the |shared|=1 case of Prop C.
Confines every (SL)-violating / bad pair strictly to open windows between consecutive multiples of a_1
(length < a_1). Reusable by any descent/induction attack on the crux.
