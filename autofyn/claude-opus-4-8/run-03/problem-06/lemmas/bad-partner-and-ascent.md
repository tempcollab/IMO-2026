# Lemma (Bad-partner + smallest-bad-term ascent)

**Certified** (proof-reviewer, round 4). Source: covering-small-part-descent Steps 3–5.

Notation: greedy sequence; P := primes(a_1); P_max := max P; S(m) := primes(m) ∩ [2,P_max]. A term m is
**bad** iff S(m) is not covering, i.e. some term B has primes(B) ∩ S(m) = ∅ (B is a *witness*). Imports:
F1 (every two terms share a prime), certified GPC (`generalized-sole-connector-off-lattice.md`), and
"every multiple of a_1 is a term with small part ⊇ P (good)".

## Lemma (bad terms are off-lattice, and have a bad partner)
Let m be bad with witness B.
1. Every prime shared by m and B is large (>P_max): a small shared prime would lie in S(m)∩primes(B),
   contradicting primes(B)∩S(m)=∅. By F1 they share ≥1 prime, hence a large prime q. By GPC, a_1∤m and
   a_1∤B — both are off the a_1-lattice, pinned in open windows of length <a_1.
2. B is bad: if B were good, S(B) would meet primes(m) in a small prime s ∈ primes(B)∩primes(m),
   contradicting that m,B share only large primes. And B≠m (primes(B)∩S(m)=∅ but primes(m)∩S(m)=S(m)≠∅
   by F1). The pair is mutual: primes(m)∩S(B) ⊆ primes(m)∩primes(B) = {large} while S(B) is small, so
   =∅, i.e. m is a witness of B. So {m,B} are two distinct off-lattice bad terms sharing only large primes.

## Corollary (ascent)
If a bad term exists, let m_0 be the smallest bad term (well-ordering). Its bad partner B is bad and
≠ m_0, so by minimality B > m_0: the smallest bad term admits a strictly larger bad partner sharing only
a large prime q_0 > P_max, both off-lattice. ∎

## Reusability
Correct and gap-free. NOTE the recorded limitation: the partner relation is symmetric, so the ascent
gives only ONE upward step (m_0→B), NOT an infinite strictly increasing chain; and even an infinite chain
of bad terms is not yet a contradiction (global Σ1/p² capacity caps only a positive fraction of
large-prime pairs). This lemma is the *engine* of the value-ascent framing, not a closure of the crux.
