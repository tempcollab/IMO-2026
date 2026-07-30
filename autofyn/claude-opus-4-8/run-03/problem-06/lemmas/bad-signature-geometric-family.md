# Lemma (bad-signature geometric family) — closes sub-step (6a)

**Certified** (proof-reviewer, round 5). Source: covering-small-part-descent Step 6 (Lemma 6).

Notation: greedy sequence a_1<a_2<…; a term = element of E_∞∩[a_1,∞) (ENUM). P:=primes(a_1);
P_max:=max P; S(m):=primes(m)∩[2,P_max]. A prime set is **covering** iff it meets primes(a_i) for
every i. A term m is **bad** iff S(m) is non-covering, i.e. some term B (a *witness*) has
primes(B)∩S(m)=∅. Imports: **(REAL)** `realizability-and-self-dual-clutter.md` Lemma 1 —
in particular clause (c): every integer n≥a_1 whose prime set contains a covering set is a term; and
𝒯⊆𝒞 (the prime set of any term is covering).

## Statement
If m is a **bad** term, then for every prime r ∣ m and every k ≥ 0 the integer n := m·r^k is again a
**bad** term, with S(n) = S(m) and the *same* witness B. These integers are strictly increasing in k,
so a single bad term forces infinitely many bad terms, unbounded above, all carrying one fixed
non-covering signature S(m) and one fixed witness B.

## Proof
m is a term, so by (REAL) 𝒯⊆𝒞, its prime set primes(m) is covering. Fix a prime r∣m (exists,
m>1) and k≥0; set n:=m·r^k. Since r already divides m, multiplying by r^k adds no new prime, so
primes(n)=primes(m), which is covering; and n=m·r^k ≥ m ≥ a_1. By (REAL) clause (c) (every integer
≥ a_1 whose prime set contains a covering set is a term), **n is a term**.

Its small part is unchanged: S(n)=primes(n)∩[2,P_max]=primes(m)∩[2,P_max]=S(m). Since m is bad, its
witness B (a term) has primes(B)∩S(m)=∅; hence primes(B)∩S(n)=primes(B)∩S(m)=∅, so the same B
witnesses n non-covering: **n is bad**. Finally r≥2, so k↦m·r^k is strictly increasing, giving the
unbounded family m < m·r < m·r^2 < …. ∎

## Scope / caveats
- This CLOSES sub-step **(6a)** (an unbounded family of bad terms) unconditionally from a single bad
  term. It does NOT touch the substantive crux **(6b)** — the value-level contradiction. The family is
  a single arithmetic-progression-like orbit with one fixed signature and one fixed witness (density
  →0), so the certified global capacity count (Σ1/p²) still cannot exploit it (that route is dead).
- Consistency with GPC: a bad term misses some prime of P (else S(m)⊇P is covering, m good), so
  primes(n)=primes(m)⊉P and a_1∤n automatically — no conflict with "bad ⇒ off-lattice".
- Cross-approach use: the orbit m·r^k mod L_0 cycles through finitely many residues, so one residue
  class mod L_0 contains infinitely many bad terms — the "a bad residue class is inhabited infinitely
  often" input that residue/extremal framings' pigeonhole needs.

Verified computationally (a_1∈{15,35,231}, 400 terms): m·r is a term for every term m and r∣m; S and
witness preserved.
