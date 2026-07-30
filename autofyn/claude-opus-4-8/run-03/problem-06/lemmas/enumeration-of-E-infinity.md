# Lemma (Enumeration reduction) — certified round 1

Setup. Integers a_1 < a_2 < ... defined by a_{n+1} = smallest integer > a_n with
gcd(a_{n+1}, a_i) > 1 for every i ≤ n, all a_i > 1. Let
E_∞ := { m ∈ ℤ_{>1} : gcd(m, a_i) > 1 for every i }.

Statement. The sequence is exactly the increasing enumeration of E_∞ ∩ [a_1, ∞):
{a_n : n ≥ 1} = E_∞ ∩ [a_1, ∞), and a_n is the n-th smallest element of E_∞ that is ≥ a_1.

Proof. For i < j the rule gives gcd(a_j, a_i) > 1; by symmetry gcd(a_i, a_j) > 1 for all
i ≠ j, and gcd(a_i,a_i)=a_i>1, so every term a_j hits every constraint, i.e. a_j ∈ E_∞.
Also E_∞ ⊆ E_n := {m>1 : gcd(m,a_i)>1 ∀ i≤n} for every n (fewer constraints on E_n).
By the rule a_{n+1} = min(E_n ∩ (a_n,∞)). If some y ∈ E_∞ had a_n < y < a_{n+1}, then
y ∈ E_n and y > a_n contradicts minimality of a_{n+1}. So no element of E_∞ lies strictly
between consecutive terms; with a_1 ∈ E_∞ the left endpoint, induction gives equality. ∎

Certification: verified computationally (recurrence and enumeration reproduce the greedy
sequence for a_1 ∈ {6,10,15,35,99,...}). Statement no stronger than proved. Reusable by
every approach — it removes all dependence on the order in which constraints were imposed,
reducing the problem to the arithmetic of the static set E_∞.
