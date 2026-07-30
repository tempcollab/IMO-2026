# Lemmas (Realizability 𝒞=𝒯; self-dual clutter b(ℰ)=ℰ)

**Certified** (proof-reviewer, round 4). Source: self-dual-clutter-grading Lemmas 0,1,2.

Notation: greedy sequence a_1<a_2<…; P := primes(a_1); P_max := max P. A **prime set** is a finite set
of primes. A prime set S is a **covering set** iff S ∩ primes(a_i) ≠ ∅ for every term a_i. 𝒞 = family of
covering sets; 𝒯 = {primes(a_i) : i≥1}. Imports: ENUM (enumeration lemma), F1 (every two terms share a
prime), and the certified fact that every multiple k·a_1 ≥ a_1 is a term.

## Lemma 0 (every term meets P)
Every term t satisfies primes(t) ∩ P ≠ ∅. *Proof.* a_1 is a term, so by F1 t and a_1 share a prime,
which divides a_1 hence lies in P. ∎ (So S(t)=primes(t)∩[2,P_max] ⊇ primes(t)∩P ≠ ∅.)

## Lemma 1 (Realizability, 𝒞 = 𝒯)
For a finite prime set S: (a) S covering ⟺ (b) some term has prime set exactly S ⟺ (c) every integer
with prime set ⊇ S and ≥ a_1 is a term. Consequently 𝒞 = 𝒯, and every covering set is realized by
infinitely many terms.
*Proof.* (a)⇒(b): fix p₀∈S, m_k=(∏_{p∈S}p)·p₀^k; primes(m_k)=S is covering, so gcd(m_k,a_i)≥(shared
prime)>1 ∀i, m_k∈E_∞; for large k, m_k≥a_1, so by ENUM m_k is a term with prime set exactly S. (b)⇒(a):
a term's prime set meets every term prime set by F1, so is covering. (a)⇒(c): primes(m)⊇S covering ⇒
primes(m) covering ⇒ m∈E_∞; if m≥a_1 it is a term (ENUM). (c)⇒(b): take m=(∏_{p∈S}p)p₀^k≥a_1. Finally
𝒯⊆𝒞 by (b)⇒(a) and 𝒞⊆𝒯 by (a)⇒(b), so 𝒞=𝒯. ∎

## Lemma 2 (self-dual clutter, b(ℰ)=ℰ)
Let ℰ = minimal elements of 𝒞 under ⊆ (a clutter; 𝒞 is an up-set of finite sets so every covering set
contains a member of ℰ). The blocker b(ℰ) = minimal prime sets meeting every member of ℰ. Then a prime
set S meets every member of ℰ ⟺ S is covering; hence b(ℰ)=ℰ.
*Proof.* (⇒) S meets every edge. Any term prime set primes(a_i)∈𝒞 contains an edge E∈ℰ; S meets
E⊆primes(a_i), so S∩primes(a_i)≠∅; S covering. (⇐) S covering. Any E∈ℰ⊆𝒞=𝒯 (Lemma 1) is a term prime
set, so S meets E. Thus {S : S meets every edge}=𝒞, whose minimal elements are ℰ; b(ℰ)=ℰ. ∎

## Reusability
Realizability turns "covering set" (an abstract set-system property) into "prime set of an actual term of
value ≥ a_1", the value ingredient the abstract covering level (Prop D barrier) lacks. Self-duality is a
structural fact (not a proof of the crux: the a_1=15 triangle {2,3},{3,5},{2,5} is self-dual with no
centre). Reusable by any approach reasoning about covering sets as objects.
