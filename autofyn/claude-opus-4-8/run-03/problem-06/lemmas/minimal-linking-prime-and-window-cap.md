# Lemmas (minimal linking prime q*; per-window spacing cap)

**Certified** (proof-reviewer, round 5). Source: minimal-linking-prime-extremal Steps 3–4.

Notation: greedy sequence a_1<a_2<…; term = element of E_∞∩[a_1,∞); P:=primes(a_1); P_max:=max P;
S(m):=primes(m)∩[2,P_max]. Two terms A,B are **small-disjoint** iff S(A)∩S(B)=∅. Window
W_k:=(k·a_1,(k+1)·a_1) (open, length a_1). Imports: certified **(F1)** (every two terms share a prime).

## Lemma A (minimal linking prime q* floors every large link)
Suppose a small-disjoint term pair exists. Let Q*:={primes q>P_max : q∣A and q∣B for some small-disjoint
term pair {A,B}}. Then Q*≠∅; set q*:=min Q* (well-ordering). For *any* small-disjoint term pair {A,B}:
(i) A,B share at least one prime (F1); (ii) every prime they share is **large**; (iii) every such shared
prime is ≥ q*.
*Proof.* If A,B share a small prime p≤P_max then p∈S(A)∩S(B)=∅, contradiction; so every shared prime is
large (ii). By F1 a shared prime exists (i). Any large shared prime q divides both members of a
small-disjoint pair, so q∈Q*, hence q≥q* (iii). Q*≠∅ because a small-disjoint pair shares such a q. ∎

## Lemma B (per-window spacing cap)
Fix a prime p≥q* and a window W_k. Then:
(a) the number of multiples of p in W_k is ≤ ⌊(a_1−1)/p⌋+1 ≤ a_1/q*+1 (and ≤1 when q*≥a_1);
(b) two distinct terms X,Y∈W_k both divisible by a prime p≥q* satisfy p∣(Y−X) with 0<|Y−X|<a_1, so
    p<a_1 and |Y−X|≥p. Hence a small-disjoint pair linked by a prime ≥a_1 straddles two distinct windows.
*Proof.* (a) W_k∩ℤ = {ka_1+1,…,(k+1)a_1−1}, a_1−1 consecutive integers; among any a_1−1 consecutive
integers at most ⌊(a_1−1)/p⌋+1 are divisible by p; p≥q* gives the bound a_1/q*+1. (b) X,Y∈W_k ⇒
0<|Y−X|<a_1; p∣X, p∣Y ⇒ p∣(Y−X); a nonzero multiple of p that is <a_1 forces p<a_1, and |Y−X|≥p as the
least positive multiple. ∎

## Scope / caveats
- These are correct, elementary, and rest only on certified F1 + well-ordering. They supply a genuinely
  non-symmetric handle (q* is attached to the whole configuration, not a symmetric pair) and a strictly
  LOCAL count (never sums Σ1/p² — avoids the dead global-capacity route).
- They do NOT close the crux. The window-index descent **(DESC)** — a bad window forcing a
  smaller-index bad window — is unproved and difficulty-equivalent to (CSP); NOT certified.
