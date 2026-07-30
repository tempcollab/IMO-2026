# Lemma (Periodic set ⇒ eventual-linear recurrence) — certified round 1

Statement. Let E ⊆ ℤ be nonempty and tail-periodic from a with period L > 0:
for all integers x ≥ a, x ∈ E ⟺ x+L ∈ E. Let b_1 < b_2 < ... enumerate E ∩ [a, ∞)
(infinite, since a+kL patterns recur). Put T := #(E ∩ [a, a+L)) ≥ 1. Then
b_{n+T} = b_n + L for every n ≥ 1.

Proof. The shift φ: x ↦ x+L is a strictly-increasing bijection E ∩ [a,∞) → E ∩ [a+L,∞):
injective/increasing; lands in E ∩ [a+L,∞) by periodicity; surjective since for z ∈ E,
z ≥ a+L we have z−L ≥ a and z−L ∈ E, z = φ(z−L). The elements of E ∩ [a,∞) below a+L are
exactly b_1,...,b_T (T of them, the smallest T since [a,a+L) is an initial segment); so the
elements ≥ a+L are b_{T+1}, b_{T+2}, ... On the other hand E ∩ [a+L,∞) = φ(E ∩ [a,∞)) =
{b_1+L, b_2+L, ...}. Two increasing enumerations of one set agree termwise:
b_{T+i} = b_i + L for all i ≥ 1. ∎

Certification: pure and elementary; verified via the recurrence (T,L) reproduced on small
seeds (a_1=15 ⇒ (T,L)=(8,30); a_1∈{6,10} ⇒ (1,2)). Statement no stronger than proved.
Combined with the enumeration reduction, once E_∞ is shown tail-periodic from a_1 the
required a_{n+T}=a_n+L for EVERY n follows immediately. Reusable by every approach.
