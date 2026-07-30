# Lemma (Essential-connector equivalence + essentiality propagation)

**Certified** (proof-reviewer, round 9). Source: `covering-small-part-descent` Lemmas 13, 14 (+ (W-inf)).
Recasts the crux (CSP) as a pure term-*divisibility* statement, the arithmetic/value face.

Notation as in `csp-iff-E-small-only.md`. A term B is **A-avoiding** iff primes(B)∩A=∅. For a prime set
A and a large prime q, **q is an essential connector for A** iff A is non-covering and every A-avoiding
term is divisible by q.

## Lemma EC (equivalence)
The following are equivalent for a prime set A and large prime q:
(a) q is an essential connector for A;
(b) A is non-covering and A∪{q} is covering.
Moreover **(CSP) fails ⟺ some large prime is an essential connector for some non-covering set.**
Consequently (CSP) ⟺ **(EC)**: for every non-covering A and large q, some A-avoiding term is not
divisible by q.

*Proof.* (a)⟹(b): let t be any term; if primes(t)∩A≠∅ then A∪{q} meets t; else t is A-avoiding, so q∣t
(essential connector), so {q}⊆A∪{q} meets t. So A∪{q} covering; A non-covering by hypothesis. (b)⟹(a):
let B be A-avoiding; primes(B)∈𝒞 meets the covering set A∪{q}; as primes(B)∩A=∅, q∈primes(B), i.e. q∣B.

CSP-fails ⟹ connector: by certified `csp-iff-E-small-only.md` there is an edge C∈ℰ with a large prime
q∈C. Put A:=C∖{q}, non-covering by edge-minimality. Any A-avoiding term B: primes(B)∈𝒞 meets C, and
primes(B)∩A=∅, so q∣B. So q is an essential connector for A.

Connector ⟹ CSP-fails: given (a), A∪{q} is covering (by (b)), so contains an edge C''∈ℰ, C''⊆A∪{q}.
C''⊄A (else A covering), so q∈C''. Edge with a large prime ⟹ (by `csp-iff-E-small-only.md`) CSP fails. ∎

## (W-inf)
If (A,q) is an essential-connector config, the set W_A of A-avoiding terms is infinite. *Proof.* A
non-covering ⟹ some term B_0 is A-avoiding. Pick a prime r∉A (A finite). For k≥1,
primes(B_0·r^k)=primes(B_0)∪{r} ⊇ primes(B_0) covering and B_0·r^k≥a_1, so B_0·r^k is a term (clause c),
and primes(B_0·r^k)∩A=∅. Distinct for distinct k. ∎ (All of W_A lies in the class 0 mod q, being q-mult.)

## Lemma (essentiality propagation)
If (A,q) is an essential-connector config, then for **every** A-avoiding term B, primes(B)∖{q} is
non-covering; hence (primes(B)∖{q}, q) is again an essential-connector config with the same q.

*Proof.* B∈W_A ⟹ q∣B, so T:=primes(B)∖{q} is defined; T≠∅ (else B a power of q, but gcd(q^j,a_1)=1 as q
large ⟹ B∉E_∞, contradiction). If T were covering, realize N with primes(N)=T, N≥a_1 a term (clause c);
N is A-avoiding (T⊆primes(B), primes(B)∩A=∅) and q∤N (q∉T), an A-avoiding term not divisible by q —
contradicting that q is an essential connector for A. So T non-covering. And T∪{q}=primes(B) is covering
(B a term), so by Lemma EC (b), q is an essential connector for T. ∎

## Reusability / scope
(EC) is (CSP) in term-divisibility language: rule out any large prime being an essential connector.
Propagation shows the failing configuration is **self-reproducing with q PRESERVED** — it supplies NO
downward monovariant on q, rad, or size. Certified as a correct reformulation + a pruning fact (records
that the naive lever "realize primes(B)∖{q}" is exactly what the failing case blocks); it does NOT close
the crux. Gap-free; no stronger than proved.
