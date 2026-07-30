# Lemma (Window Purity) — CERTIFIED (proof-reviewer, round 7)

Source: covering-small-part-descent Step 7a / window-purity-class-cycle Lemma 1 (proposed independently
by both builders; identical proof). Reviewer re-derived from ENUM + "covering ⟹ ∈E_∞"; gap-free.
Numerically verified this round (a_1∈{15,35,99,231}, 200 terms): 0 interior integers lie in E_∞.

Notation: greedy sequence a_1<a_2<…; E_∞ = {m>1 : gcd(m,a_i)>1 ∀i}; a term = element of
E_∞∩[a_1,∞) (ENUM). P:=primes(a_1); P_max:=max P; S(m):=primes(m)∩[2,P_max]. A prime set is
**covering** iff it meets primes(a_i) for every i. Import: **(ENUM)**
`lemmas/enumeration-of-E-infinity.md` — the sequence is the increasing enumeration of E_∞∩[a_1,∞);
in particular a_{n+1} is the least term exceeding a_n, and no term lies strictly between a_n and
a_{n+1}.

## Statement
For every n ≥ 1 and every integer x with a_n < x < a_{n+1}:

  x ∉ E_∞  —  equivalently, there is an index i with gcd(x,a_i)=1, i.e. primes(x)∩primes(a_i)=∅.

Hence primes(x) is a non-covering prime set, and a fortiori S(x) ⊆ primes(x) is non-covering.

## Proof
Suppose x ∈ E_∞. Since x > a_n ≥ a_1, we have x ∈ E_∞∩[a_1,∞), so by (ENUM) x is a term. But
a_n < x < a_{n+1}, and by (ENUM) a_{n+1} is the least term exceeding a_n, so no term lies strictly
between a_n and a_{n+1} — contradiction. Therefore x ∉ E_∞, i.e. gcd(x,a_i)=1 for some i, i.e.
primes(x)∩primes(a_i)=∅: primes(x) misses color i and is non-covering. Since S(x)⊆primes(x), S(x)
misses color i as well, hence is non-covering. ∎

## Scope / reusability
A LOCAL greedy handle: it constrains the interior of every gap (a_n,a_{n+1}) to be swept clean of
E_∞ — a statement about the greedy VALUES, exactly the per-window texture the Prop D barrier says a
closing argument must use, and it invokes no dead global count. Reusable by the dynamics/FIN-W
framings (window-purity-class-cycle, bad-residue-witness-index). Verified numerically
(a_1∈{15,35,99,231} by outline-reviewer; a_1=15, 120 terms here): 0 interior integers lie in E_∞.
