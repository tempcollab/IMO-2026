## Status
partial

## Approaches tried
- **minimal-cover-small-only** (round 8, NEW — pure-transversal / hypergraph-minimality mechanism).
  Attacks the whole P6 claim via (CSP), through the target **ℰ-small-only** ("every minimal covering
  set ⊆ [2,P_max]"). Closes steps 1,2,3,5 gap-free from certified lemmas, and makes genuine NEW rigorous
  progress on the gap (step 4):
  - **Intersecting-clutter Lemma (A):** any two edges of ℰ meet; every covering set meets every edge; in
    particular every edge meets P=primes(a_1). Clean, one line from certified Lemma 2 (b(ℰ)=ℰ). Promotable.
  - **Essential-witness Lemma (B):** for an edge C and each r∈C there is a term B_r with
    primes(B_r)∩C={r}. Rigorous from edge-minimality + realizability.
  - **Large-witness structure Lemma (C):** if q∈C is large, its essential witness B_q is a *bad* term,
    q is essential in primes(B_q), and there is another edge C'≠C with C∩C'={q}. Rigorous.
  - **Base case |P|=1 (a_1 a prime power): ℰ-small-only PROVED** via the new mechanism (C and C' both meet
    P={p}, forcing p∈C∩C'={q}, impossible). Full for prime-power a_1.
  Honest GAP: |P|≥2. Status: partial (base case + 3 structural lemmas; general P open).
- **minimal-cover-small-only** (round 9, ADVANCE — target pinned down exactly, one new gap-free lemma).
  Two rigorous new items and a precise reading of the obstruction:
  - **NEW Lemma D (ℰ-small-only ⟺ (CSP)), gap-free and promotable.** Proves the *converse* of the
    endgame too: (CSP) ⟹ ℰ-small-only, by realizing any large-prime edge as an explicit bad term
    m=(∏_{p∈C}p)·q^k≥a_1. So the pure-transversal target is *exactly* the standing crux (CSP) — not
    weaker, not strictly stronger, but LITERALLY EQUIVALENT. This settles the reviewer's
    "crux-equivalent-or-stronger" question: it is crux-*equivalent*, and it explains rigorously why no
    downward monovariant on the large-prime data appears (see below).
  - **Monovariant obstruction made precise (honest, not a closure).** The essential-witness partner map
    C↦C' of Lemma C is *horizontal*: C∩C'={q} keeps the SAME large prime q, so q∈C', whence
    max(large primes), |Q_C|, ∏Q_C, smallest-large-prime and largest-large-prime are all NON-decreased
    by it. The construction therefore supplies no strictly-downward well-founded quantity on primes/edges
    — consistent with Lemma D (the target is CSP, whose sole wall is the a_1 value inequality that no
    transversal quantity touches). Recorded as an obstruction, NOT promoted as a theorem (no numeric
    witness of an increase exists — CSP holds on every seed — so "no downward monovariant exists" is not
    claimed).
  Honest GAP unchanged in kind: ℰ-small-only for |P|≥2 = (CSP) = the value inequality. Not closed.

## Current best

Target reduction (steps 1,2,3,5 — gap-free from certified lemmas), the structural Lemmas A–C, the
complete base case |P|=1, and the NEW exact equivalence Lemma D (ℰ-small-only ⟺ (CSP)).

Notation (as in the workspace): greedy sequence a_1<a_2<…; a **term** is an element of E_∞∩[a_1,∞)
(certified `enumeration-of-E-infinity.md`, ENUM); P:=primes(a_1); P_max:=max P; a prime is **small** if
≤P_max, **large** if >P_max; S(m):=primes(m)∩[2,P_max]. A finite prime set is **covering** iff it meets
primes(a_i) for every term a_i; 𝒞 = covering sets, 𝒯 = {primes(a_i)}. By certified Realizability
(`realizability-and-self-dual-clutter.md`, Lemma 1) 𝒞=𝒯, and clause (c): every integer ≥a_1 whose prime
set contains a covering set is a term. ℰ = minimal covering sets (edges); by certified Lemma 2 the clutter
is self-dual, b(ℰ)=ℰ, and a prime set meets every edge ⟺ it is covering. A term m is **bad** iff S(m) is
non-covering. **(CSP)** = no term is bad.

**Elementary monotonicity used throughout.** Covering sets form an *up-set*: if D⊆D' and D is covering
then D' is covering (D' still meets every color that D meets). Equivalently, a subset of a non-covering
set is non-covering. (Immediate from the definition; used in Lemma D and the endgame.)

**Endgame closure (steps 1,2,3,5), gap-free.** Suppose (CSP) fails; let m_0 be a bad term. C:=primes(m_0)
is covering (𝒯⊆𝒞). Since 𝒞 is an up-set of finite sets under ⊆, C contains an edge C'∈ℰ (minimal member;
finite descent). **If ℰ-small-only holds** then C'⊆[2,P_max], and C'⊆C, so C'⊆C∩[2,P_max]=S(m_0). Supersets
of covering sets are covering, so S(m_0)⊇C' is covering — contradicting m_0 bad. Hence no bad term; (CSP)
holds; by certified `csp-implies-theorem.md` the theorem (a_{n+T}=a_n+L for all n) follows. ∎
[The ENTIRE weight is on **ℰ-small-only**: every edge C'∈ℰ satisfies C'⊆[2,P_max].]

---

### Step 4 — progress on ℰ-small-only

**Lemma A (Intersecting clutter).** (i) Every covering set meets every edge of ℰ. (ii) Consequently any
two edges of ℰ meet: C,C'∈ℰ ⟹ C∩C'≠∅. (iii) Every edge meets P; in particular every edge C contains a
small prime, and C∩P⊆C∩[2,P_max].

*Proof.* (i) By certified Lemma 2 (`realizability-and-self-dual-clutter.md`), a prime set S meets every
member of ℰ iff S is covering; the forward direction gives: S covering ⟹ S meets every edge. (ii) Each
edge C∈ℰ⊆𝒞 is a covering set, so by (i) it meets every edge. (iii) P=primes(a_1) is the prime set of the
term a_1, so P∈𝒯=𝒞 is covering; by (i) P meets every edge. Since P⊆[2,P_max], C∩P is a set of small primes
in C. ∎

**Lemma B (Essential witnesses).** Let C∈ℰ and r∈C. There is a term B_r with primes(B_r)∩C={r}.

*Proof.* C is minimal covering, so C∖{r} is non-covering: by definition some term B_r has
primes(B_r)∩(C∖{r})=∅. C is covering, so primes(B_r)∩C≠∅; the shared prime lies in C but not in C∖{r},
hence equals r. Thus primes(B_r)∩C={r}. ∎

**Lemma C (Structure at a large prime).** Suppose C∈ℰ and q∈C is large. Let B_q be an essential witness
for q (Lemma B): primes(B_q)∩C={q}. Then:
1. C∩[2,P_max] is non-empty (C meets P) and is a **non-covering** set;
2. B_q is a **bad** term (S(B_q) is non-covering);
3. q is **essential** in primes(B_q): primes(B_q)∖{q} is non-covering;
4. there is an edge C'∈ℰ with C'≠C and C∩C'={q} (in particular q∈C').

*Proof.* Write C_s:=C∩[2,P_max] (small part) and note q∈C is large so q∉C_s.

(1) By Lemma A(iii), C∩P≠∅ and C∩P⊆C_s, so C_s≠∅. If C_s were covering it would be a covering set with
C_s⊊C (proper: q∈C∖C_s), contradicting minimality of the edge C. So C_s is non-covering.

(2) B_q is a term, so primes(B_q)∈𝒞 is covering. Its small part S(B_q)⊆primes(B_q); since
primes(B_q)∩C={q} and q is large, S(B_q)∩C=∅. If S(B_q) were covering, by Lemma A(i) it would meet the
edge C, i.e. S(B_q)∩C≠∅ — contradiction. Hence S(B_q) is non-covering, i.e. B_q is bad.

(3) If primes(B_q)∖{q} were covering, by Lemma A(i) it would meet C:
(primes(B_q)∖{q})∩C ⊆ (primes(B_q)∩C)∖{q} = {q}∖{q} = ∅, contradiction. So primes(B_q)∖{q} is non-covering:
q is essential in primes(B_q).

(4) primes(B_q) is covering (finite), so it contains an edge C'∈ℰ with C'⊆primes(B_q). By Lemma A(ii)
C'∩C≠∅, and C'∩C⊆primes(B_q)∩C={q}, so C'∩C={q}; in particular q∈C'. Finally C'≠C: since C'⊆primes(B_q)
we have C'∩C_s⊆primes(B_q)∩C_s=∅, whereas C⊇C_s≠∅, so C⊄primes(B_q) and thus C≠C'. ∎

**Lemma D (Exact crux-equivalence: ℰ-small-only ⟺ (CSP)).** The following are equivalent:
(I) every edge C∈ℰ satisfies C⊆[2,P_max] (**ℰ-small-only**); (II) no term is bad (**(CSP)**).

*Proof.* (I)⟹(II) is the endgame closure above (repeated for completeness): assume (I) and let m_0 be any
term; C:=primes(m_0)∈𝒯=𝒞 is covering, so contains an edge C'∈ℰ; by (I) C'⊆[2,P_max], and C'⊆C, so
C'⊆C∩[2,P_max]=S(m_0). Since C' is covering and covering is up-closed, S(m_0) is covering; m_0 is not bad.
As m_0 was arbitrary, (CSP) holds.

(II)⟹(I). Assume (CSP) and suppose, for contradiction, some edge C∈ℰ contains a large prime q>P_max.
Choose an integer k≥0 with m:=(∏_{p∈C}p)·q^k ≥ a_1 (possible since q≥2). Because q∈C already,
multiplying by q^k adds no new prime: primes(m)=C. C is covering and m≥a_1, so by certified Realizability
(`realizability-and-self-dual-clutter.md`, Lemma 1, clause (c): every integer ≥a_1 whose prime set
contains a covering set is a term — here primes(m)=C⊇C, covering) m is a term. Its small part is
S(m)=primes(m)∩[2,P_max]=C∩[2,P_max], which does not contain the large prime q, so S(m)⊆C∖{q}. Because C
is a *minimal* covering set and q∈C, the proper subset C∖{q} is non-covering; hence its subset S(m) is
non-covering (subset of non-covering is non-covering). Therefore m is a bad term, contradicting (CSP). So
no edge contains a large prime: every C∈ℰ satisfies C⊆[2,P_max], i.e. (I). ∎

*Consequence.* The pure-transversal target of this approach is **not** a weakening of the crux: it is
literally the same statement as (CSP), phrased in the language of the minimal transversals (edges) of the
self-dual covering clutter. This is the exact form of "crux-equivalent" the outline-reviewer asked to
resolve; it also pins the shared wall precisely at the transversal level.

**Theorem (base case, |P|=1). If a_1 is a prime power then ℰ-small-only holds.**

*Proof.* Say P={p}. Suppose, for contradiction, some edge C∈ℰ contains a large prime q. By Lemma C(4)
there is an edge C'≠C with C∩C'={q}. By Lemma A(iii) every edge meets P={p}, so p∈C and p∈C'; hence
p∈C∩C'={q}, i.e. p=q. But p≤P_max<q (p small, q large) — contradiction. Therefore no edge contains a
large prime: every edge C⊆[2,P_max]. ∎

Combined with the endgame closure (equivalently Lemma D, direction (I)⟹(II)), this **fully proves the P6
theorem whenever a_1 is a prime power** (ℰ-small-only ⟹ (CSP) ⟹ theorem), through the pure-transversal
mechanism, with no value induction.

---

### The remaining gap (|P|≥2), stated honestly

For |P|≥2 the base-case contradiction dissolves: Lemma A(iii) forces C and C' each to meet P, but
C∩C'={q} only forces C∩P and C'∩P to be *disjoint non-empty* subsets of P, which is possible when
|P|≥2. Iterating Lemma C produces edges C=C^{(0)}, C^{(1)},… all containing q with (consecutively)
disjoint P-parts, but this only bounds their number by |P| — no contradiction.

**Why no downward monovariant appears (now explained rigorously by Lemma D).** The reviewer asked for a
strictly DOWNWARD well-founded monovariant (largest prime, |Q_C|, or ∏Q_C). Lemma C's partner map is
**horizontal**: C∩C'={q} keeps the SAME large prime q (q∈C'), and the other large primes of C' come from
Q(B_q)∖{q} — unconstrained by C, possibly larger than any prime of C. Hence

  max(large primes of C'),  |Q_{C'}|,  ∏Q_{C'},  min/max large prime

are none of them forced ≤ their C-values; the construction supplies no strictly-decreasing quantity on
the large-prime data. Lemma D now *explains* this structurally: since ℰ-small-only IS (CSP), and (CSP)'s
sole surviving obstruction is the value inequality tying a_1 to the covering structure (certified state:
`minimal-bad-term-floor-tightness.md`, `finite-connector-pool-periodicity.md`), any closing pressure must
be a *value* statement, which no purely transversal (prime/edge) quantity can be. This is recorded as an
honest obstruction, **not** a theorem: because (CSP) holds on every numeric seed, there is no observed
configuration in which the monovariant increases, so I do not claim "no downward monovariant can exist" —
only that this construction produces none, and Lemma D shows why one is not to be expected transversally.

**The one lever left is the a_1 value threshold.** By Lemma D(II)⟹(I), ruling out a large-prime edge C is
*exactly* ruling out the bad term m=(∏_{p∈C}p)·q^k; that is the sibling lanes' crisp value inequality
("no minimal covering set with a large prime realizes ≥a_1"). So the pure-transversal route, pushed
rigorously, **is the same wall** — now proven equal, not merely "reduces to." This instance of the gap is
therefore honest and open; it is NOT closed here, and I do not claim otherwise.

**Summary of what is rigorously established (all gap-free):** the endgame closure (ℰ-small-only ⟹
theorem); Lemma A (intersecting clutter); Lemma B (essential witnesses); Lemma C (large-witness structure);
**Lemma D (ℰ-small-only ⟺ (CSP), both directions)**; the **complete base case |P|=1**. Open:
ℰ-small-only for |P|≥2 (= (CSP) = the value inequality).

## Promotable lemmas

- **Intersecting-clutter Lemma (Lemma A).** *For the greedy-sequence covering clutter ℰ (self-dual,
  certified `realizability-and-self-dual-clutter.md` Lemma 2): every covering set meets every edge of ℰ;
  hence any two edges meet, and every edge meets P=primes(a_1) (so every edge contains a small prime of
  a_1's own factor set).* Proof above (one line from certified Lemma 2). Reusable by any covering/clutter
  framing.

- **Essential-witness Lemma (Lemma B).** *For any edge C∈ℰ and any prime r∈C, there is a term B_r with
  primes(B_r)∩C={r}.* Proof above (edge-minimality + definition of covering). Reusable.

- **Large-witness structure (Lemma C).** *If an edge C∈ℰ contains a large prime q, then: its small part
  C∩[2,P_max] is non-empty and non-covering; the essential witness B_q is a bad term; q is essential in
  primes(B_q); and there is a distinct edge C' with C∩C'={q}.* Proof above. Reusable.

- **Crux-equivalence Lemma (Lemma D) — NEW this round, gap-free.** *ℰ-small-only (every edge of ℰ lies in
  [2,P_max]) ⟺ (CSP) (no term is bad).* Proof above: (I)⟹(II) is the endgame; (II)⟹(I) realizes any
  large-prime edge C as an explicit bad term (∏_{p∈C}p)·q^k≥a_1 via Realizability clause (c). Imports only
  certified `realizability-and-self-dual-clutter.md`. Records that the pure-transversal reformulation of the
  crux is *exactly* the crux (settles "crux-equivalent-or-stronger" as: equivalent). Reusable as the bridge
  between the transversal (edge) language and the value language of (CSP).
