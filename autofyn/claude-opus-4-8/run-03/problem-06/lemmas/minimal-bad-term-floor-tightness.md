# Lemma (minimal-bad-term floor-tightness / minimal-bad-term descent) — CERTIFIED (round 7)

**Certified** (proof-reviewer, round 7). Independently proved by TWO builders this round
(lex-rewrite-descent §2 "Lemma X"; covering-small-part-descent Step 7c "Lemma 9") with identical core;
reviewer re-derived. Gap-free. Imports only (REAL) `realizability-and-self-dual-clutter.md` (clause (c):
every integer ≥a_1 whose prime set contains a covering set is a term; 𝒯⊆𝒞) and the definition of bad.

Notation: greedy sequence a_1<a_2<…; term = element of E_∞∩[a_1,∞) (ENUM). P:=primes(a_1); P_max:=max P;
S(m):=primes(m)∩[2,P_max]. A prime set is **covering** iff it meets primes(a_i) for every term a_i. A term
m is **bad** iff S(m) is non-covering (some term B, a *witness*, has primes(B)∩S(m)=∅).

## Statement
Suppose a bad term exists; let m_0 be the smallest (well-ordering) and C:=primes(m_0). Then C is covering
(𝒯⊆𝒞), S(m_0) is non-covering, and:

(i) for every prime p with v_p(m_0)≥2:  m_0 < a_1·p;
(ii) for every prime p∈C with v_p(m_0)=1 and C∖{p} covering:  m_0 < a_1·p.

Equivalently (dichotomy form): call p **sheddable** if p²|m_0, or (p‖m_0 and C∖{p} covering). Then either
**(A)** m_0 is squarefree and C is a *minimal* covering set containing a large prime (no sheddable prime);
or **(B)** a sheddable prime exists and for the smallest one p, m_0 < a_1·p.

## Proof
m_0 is a term, so (REAL) 𝒯⊆𝒞 gives C covering; m_0 bad gives S(m_0) non-covering. Since C is covering it
meets P⊆[2,P_max] (a small prime) and, S(m_0) non-covering forces C⊄[2,P_max] (a large prime); so |C|≥2.

(i) Let v_p(m_0)≥2, m':=m_0/p. Then primes(m')=primes(m_0)=C (exponent of p only drops by 1, stays ≥1),
covering, and m'>1. If m'≥a_1, by (REAL) clause (c) m' is a term; S(m')=C∩[2,P_max]=S(m_0) non-covering,
so m' is bad, and m'=m_0/p<m_0 — contradicting minimality of m_0. Hence m'<a_1, i.e. m_0<a_1·p.

(ii) Let p∈C, v_p(m_0)=1, C∖{p} covering, m':=m_0/p. Then primes(m')=C∖{p} (covering, nonempty as
covering sets meet P, so m'>1). If m'≥a_1, by (REAL) clause (c) m' is a term. Its small part
S(m')=(C∖{p})∩[2,P_max] ⊆ S(m_0). Let B witness S(m_0) (primes(B)∩S(m_0)=∅); then
primes(B)∩S(m')⊆primes(B)∩S(m_0)=∅, so B witnesses m' bad. Thus m'<m_0 is a bad term — contradiction.
Hence m'<a_1, i.e. m_0<a_1·p.

Dichotomy: if no sheddable prime, m_0 is squarefree and C has no redundant prime, i.e. C is a minimal
covering set; it contains a large prime (shown above) — case (A). Otherwise a sheddable prime exists; the
smallest one p gives m_0<a_1·p by (i)/(ii) — case (B). The cases are mutually exclusive. ∎

## Scope / caveats
- A genuine DOWNWARD (value) constraint on the minimal bad realizer — the dual of the certified upward
  `bad-signature-geometric-family.md` (which only multiplies up). Reusable by any minimality/descent framing.
- Does NOT close the crux. The descent is blocked exactly at the a_1 threshold: (REAL) clause (c) certifies
  m'=m_0/p a term only when m'≥a_1, and the abstract covering level genuinely admits minimal covering sets
  whose realization can fall below a_1 (Prop D barrier: the a_1=15 self-dual triangle {2,3},{3,5},{2,5} has
  no small centre). Sharpest residual: *no minimal covering set containing a large prime has minimal
  realization ≥ a_1* would close (6b) via this descent — the honest open gap.
- Also pruned (negative certification, lex-rewrite-descent §1): the direct aimo-0960-style (q*,k)-lowering
  active rewrite has no valid operator — (a) producing a link in (P_max,q*) is verbatim the negation of
  Lemma A's minimality of q* (equal in strength to the theorem, not a reduction); (b) the covering-preserving
  exchange A→A·s/q needs a single small prime covering q's entire witness set, which Prop D permits to be
  impossible. Future rounds should not re-field the direct constructive rewrite in the (q*,k) order.
