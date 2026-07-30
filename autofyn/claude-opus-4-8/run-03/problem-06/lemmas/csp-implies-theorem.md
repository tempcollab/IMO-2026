# Lemma (CSP ⇒ theorem): self-contained order-free reduction

**Certified** (proof-reviewer, round 4). Source: covering-small-part-descent Step 1 (equivalently the
E*-reduction of reduced-process-identity §2–§3). Order-free; does not need the (SL) intermediary.

Notation: greedy sequence a_1<a_2<…; P := primes(a_1); P_max := max P; S(m) := primes(m) ∩ [2,P_max];
L_0 := ∏_{p ≤ P_max} p (squarefree). Imports certified `enumeration-of-E-infinity.md` (ENUM),
`periodic-set-enumeration.md` (PER), and F1 ("every two terms share a prime; every term is divisible by
a prime of P, so S(t) ≠ ∅").

Call a term m **good** iff S(m) ∩ primes(a_i) ≠ ∅ for every i (its small part meets every color).
**(CSP)** := every term is good.

## Statement
If (CSP) holds, then a_{n+T} = a_n + L for every n ≥ 1, with L = L_0 and T = #(E*∩[a_1,a_1+L_0)) ≥ 1,
where E* := {m>1 : S(m) ∩ primes(a_i) ≠ ∅ ∀ i}.

## Proof
(1a) E* is a union of residue classes mod L_0: for a prime p ≤ P_max, whether p | m depends only on
m mod p, hence on m mod L_0 (CRT); so S(m), and the property "S(m) meets every primes(a_i)", depend only
on m mod L_0. Thus m ∈ E* ⟺ m+L_0 ∈ E* (both >1); E* is tail-periodic from a_1 with period L_0.

(1b) Under (CSP), E*∩[a_1,∞) = E_∞∩[a_1,∞).
 • ⊇: m ∈ E_∞∩[a_1,∞) is a term (ENUM); (CSP) makes it good, so S(m) meets every color, m ∈ E*.
 • ⊆: m ∈ E*∩[a_1,∞): S(m) ⊆ primes(m) meets every color, so gcd(m,a_i)>1 ∀i, m ∈ E_∞. (no hypothesis)

(1c) a_1 ∈ E* (S(a_1)=P meets every color by F1) and every k·a_1 ∈ E* (S(k a_1) ⊇ P), so E*∩[a_1,∞) is
infinite. Apply PER to (E*, a_1, L_0): its increasing enumeration b_1<b_2<… satisfies b_{n+T}=b_n+L_0,
T=#(E*∩[a_1,a_1+L_0))≥1. By (1b) that set equals E_∞∩[a_1,∞), whose increasing enumeration is a_1,a_2,…
(ENUM). Two increasing enumerations of one set agree termwise, so a_n=b_n and a_{n+T}=a_n+L_0 ∀n. ∎

## Reusability
Packages the finiteness endgame directly from (CSP)="every term's small part is covering", the field's
standing crux. Any approach that proves (CSP) closes the theorem by importing this. Gap-free; no
stronger than proved (conclusion is conditional on (CSP)).
