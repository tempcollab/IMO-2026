# Lemma (Local Hub-Cover finite-capacity) — CERTIFIED (proof-reviewer, round 7)

Source: covering-small-part-descent Step 7b. Reviewer re-derived from (REAL) 𝒯⊆𝒞 + pigeonhole;
gap-free. primes(h)=S(h)⊔Q(h) with primes(h) covering forces primes(B)∩Q(h)≠∅ for every B∈W(h).

Notation: greedy sequence a_1<a_2<…; a term = element of E_∞∩[a_1,∞) (ENUM). P:=primes(a_1);
P_max:=max P; S(m):=primes(m)∩[2,P_max]. A prime is **small** if ≤P_max, **large** if >P_max. A
prime set is **covering** iff it meets primes(a_i) for every i. A term m is **bad** iff S(m) is
non-covering (some term B has primes(B)∩S(m)=∅). Import: **(REAL)**
`lemmas/realizability-and-self-dual-clutter.md` Lemma 1, clause 𝒯⊆𝒞 — the prime set of any term is
covering. Import: **Pigeonhole principle** (knowledge_base.md, Pigeonhole / extremal principle).

## Statement
Let h be a **bad** term. Put
  Q(h) := primes(h) ∩ (P_max,∞)   (the finitely many LARGE prime factors of h),
  W(h) := { terms B : primes(B) ∩ S(h) = ∅ }   (the colors S(h) misses).
Then W(h) ≠ ∅, Q(h) ≠ ∅, and every B ∈ W(h) satisfies primes(B) ∩ Q(h) ≠ ∅; equivalently

  W(h) ⊆ ⋃_{q∈Q(h)} { B : q ∣ B }.

Consequently, if W(h) is infinite then some single q ∈ Q(h) divides infinitely many members of W(h).

## Proof
h is bad, so S(h) is non-covering: some term B_0 has primes(B_0)∩S(h)=∅, i.e. B_0∈W(h); thus
W(h)≠∅.

Write primes(h) = S(h) ⊔ Q(h) (disjoint: S(h) collects the small prime factors, Q(h) the large
ones). h is a term, so by (REAL) 𝒯⊆𝒞 its prime set primes(h) is covering: for every term B,
primes(B)∩primes(h) ≠ ∅.

Fix B∈W(h). Then primes(B)∩S(h)=∅, so
  primes(B)∩primes(h) = primes(B)∩(S(h)⊔Q(h)) = primes(B)∩Q(h).
The left side is nonempty (covering), hence primes(B)∩Q(h)≠∅: some large prime q∈Q(h) divides B.
Applying this to B=B_0 gives Q(h)≠∅. This proves W(h) ⊆ ⋃_{q∈Q(h)}{B:q∣B}.

If W(h) is infinite: Q(h) is finite (h is one integer, finitely many prime factors), so the finite
union ⋃_{q∈Q(h)}{B∈W(h):q∣B} = W(h) is infinite; by the pigeonhole principle some q∈Q(h) has
{B∈W(h):q∣B} infinite. ∎

## Scope / caveats
- This is a LOCAL finite-capacity fact about ONE fixed hub h: its ≤|Q(h)| large primes must jointly
  account for every color S(h) misses. It NEVER sums Σ1/p² over all hubs, so it is entirely distinct
  from the proven-dead global capacity route (`lemmas/term-density-and-prime-capacity.md`).
- It does NOT by itself close the crux (6b): a bad term may miss exactly ONE color with |Q(h)|=1, so
  the missed-color-vs-|Q(h)| count need not overflow. Its value is structural — it identifies the
  (FIN-W) "star" prime q as one of the hub's OWN large prime factors, and is reusable by
  bad-residue-witness-index and window-purity-class-cycle.
