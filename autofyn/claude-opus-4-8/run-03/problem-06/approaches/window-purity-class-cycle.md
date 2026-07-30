## Status
partial

## Approaches tried
- **window-purity-class-cycle** (round 7, NEW — mandated GREEDY-DYNAMICS route). Delivered two new,
  fully-proved, certifiable lemmas and a strict sharpening of the standing wall:
  (i) **Window Purity** — every integer strictly between consecutive terms has non-covering small part
  (proved gap-free from ENUM + the immediate "covering ⟹ ∈E_∞" direction; verified numerically, 0
  violations on a_1∈{15,35,99,231});
  (ii) **(FIN-Q) ⟹ theorem** — the airtight form of "single-sided infinite witnessing is harmless": the
  periodicity conclusion holds as soon as, for each E_∞-inhabited bad class r, the pool of large connector
  primes Q(r)=⋃_{i∈W(r)}Q_i is FINITE, *even if the witness-index set W(r) itself is infinite*. This is a
  strict weakening of the certified Reduction Lemma's hypothesis (FIN-W) [W(r) finite]; it makes precise
  and rigorous the DERIVED-not-certified claim the outliner flagged, folding infinite single-prime
  witnessing into a finite Q_rel.
  (iii) **Crux sharpened to ¬(FIN-Q)** and modelled as an infinite walk on a finite directed class-graph
  G on R_bad (≤L_0 nodes), which must revisit a class. Honest **GAP** at Step 5: the descent/revisit
  mechanism (a strictly smaller large linking prime on each return, or a first-hole over-constraint) is
  NOT extracted; neither (5a) nor (5b) is completed. Reviewer: expected CHANGES REQUESTED / partial
  (advanced — two certifiable lemmas + crux strictly weakened FIN-W → FIN-Q).

## Current best

The whole problem is reduced, with full rigor, to a single finiteness statement **strictly weaker than
the previously-standing crux (FIN-W)**, namely (FIN-Q) below; and the reduction is proved end to end.
Two new lemmas (Window Purity; (FIN-Q)⟹theorem) are gap-free and certifiable. The sole remaining gap is
the failure branch of (FIN-Q), isolated as a revisit on a finite class-graph.

### Notation and imported (certified) facts

Greedy sequence a_1<a_2<… of integers >1. E_∞ := {m∈ℤ_{>1} : gcd(m,a_i)>1 for every i}.
P := primes(a_1); P_max := max P; a prime is **small** if ≤P_max, **large** if >P_max.
L_0 := ∏_{p≤P_max} p (squarefree). For m>1, S(m) := primes(m)∩[2,P_max] (the small part). For a term
a_i, Q_i := primes(a_i)∩(P_max,∞) (its large primes). A finite prime set S is **covering** iff
S∩primes(a_i)≠∅ for every term a_i. A term m is **good** iff S(m) is covering; otherwise **bad**
(some term B has primes(B)∩S(m)=∅, a *witness* for m). Two terms are **small-disjoint** iff their small
parts are disjoint.

Imported by reference, not re-proved (all certified):
- **ENUM** (`enumeration-of-E-infinity.md`): the sequence is exactly the increasing enumeration of
  E_∞∩[a_1,∞); in particular no element of E_∞ lies strictly between two consecutive terms.
- **PER** (`periodic-set-enumeration.md`): if E⊆ℤ is tail-periodic from a with period L>0 and E∩[a,∞)
  is infinite, its increasing enumeration b_1<b_2<… satisfies b_{n+T}=b_n+L, T=#(E∩[a,a+L))≥1.
- **F1** (in `csp-implies-theorem.md`): every two terms share a prime; every term meets P, so
  S(t)⊇(S(t)∩P)≠∅ for every term t.
- **GPC** (`generalized-sole-connector-off-lattice.md`): two small-disjoint terms A,B satisfy a_1∤A, a_1∤B.
- **Residue-locality** (`csp-implies-theorem.md` Step 1a): for a small prime p, p|m depends only on m mod p,
  hence (CRT) S(m) and every property of it depends only on m mod L_0. So "m bad", the class R_bad of bad
  residues, and W(r) below all depend only on m mod L_0; |R_bad|≤L_0 is finite.
- **Reduction Lemma / (FIN-W)⟹theorem** (`finite-witness-periodicity.md`): with
  W(r):={i:primes(a_i)∩S(r)=∅} for r∈R_bad and R'_bad:={r∈R_bad : E_∞ meets class r}, if every W(r) is
  finite then E_∞ is tail-periodic and a_{n+T}=a_n+L for all n. Its Steps 1–4 (residue-level badness;
  W(r)-large-link; W(r) points to bad terms; the membership dichotomy (★)) are certified and imported.
- **Lemma A / Lemma B** (`minimal-linking-prime-and-window-cap.md`): if a small-disjoint pair exists,
  q* := min{large q : q links some small-disjoint pair} exists and floors every large link; multiples of
  a prime p≥q* in one length-a_1 window are ≥p apart and number ≤a_1/q*+1.

For r∈R_bad, recall from the certified Reduction Lemma the **membership dichotomy** for m≡r (mod L_0):
> (★)  m∈E_∞ ⟺ for every i∈W(r), some q∈Q_i divides m.

and its two companions: if r is covering then every m>1, m≡r lies in E_∞; if E_∞ misses class r then no
m≡r lies in E_∞.

---

### Lemma 1 (Window Purity) — DELIVERED, gap-free, certifiable

**Statement.** For every n≥1 and every integer x with a_n<x<a_{n+1}:
(i) x∉E_∞; and (ii) S(x) is non-covering — there is a term a_j with primes(a_j)∩S(x)=∅.

**Proof.** (i) By ENUM the sequence a_1<a_2<… is precisely the increasing enumeration of E_∞∩[a_1,∞).
Suppose some y∈E_∞ had a_n<y<a_{n+1}. Then y>a_n≥a_1, so y∈E_∞∩[a_1,∞); being strictly between the
n-th and (n+1)-th elements of the increasing enumeration of that set, y would be an element of E_∞∩[a_1,∞)
distinct from every a_k yet lying between two consecutive enumerated values — impossible, as the increasing
enumeration lists *all* elements of E_∞∩[a_1,∞) in order and leaves no element strictly between consecutive
ones. Hence no element of E_∞ lies strictly between a_n and a_{n+1}; in particular x∉E_∞. Since
x>a_n≥a_1>1, x∉E_∞ means (unwinding the definition) there is a term a_j with gcd(x,a_j)=1.

(ii) Suppose, for contradiction, S(x) were covering: for every term a_i, primes(a_i)∩S(x)≠∅. As
S(x)⊆primes(x), for each i a common (small) prime divides both x and a_i, so gcd(x,a_i)>1 for **every** i;
with x>1 this gives x∈E_∞, contradicting (i). Therefore S(x) is non-covering: some term a_j has
primes(a_j)∩S(x)=∅. ∎

*Remarks.* (1) This is strictly window-wide and sharper than GPC, which only pins the *endpoints* (bad
terms) off-lattice; Window Purity certifies non-covering small part for **every** interior integer, using
no dead global count. (2) It uses only ENUM and the immediate direction "covering ⟹ ∈E_∞" already implicit
in the certified E*⊆E_∞ arguments. Verified numerically (a_1∈{15,35,99,231}, first ~400 terms): 0 integers
in any open gap are in E_∞ or have covering small part. Certifiable now (offered below).

---

### Lemma 2 ((FIN-Q) ⟹ theorem) — DELIVERED, gap-free, certifiable; the airtight "single-sided harmless"

For r∈R'_bad define the **large connector pool** Q(r) := ⋃_{i∈W(r)} Q_i (the large primes appearing across
the witness colors of r). Consider the hypothesis:

> **(FIN-Q):** for every E_∞-inhabited bad class r∈R'_bad, the pool Q(r) is finite.

**Statement.** (FIN-Q) implies E_∞ is tail-periodic from a_1, hence there exist T,L with a_{n+T}=a_n+L
for every n. Moreover (FIN-Q) is **strictly weaker** than the certified (FIN-W): W(r) may be infinite,
provided the *primes* it contributes, Q(r), are finitely many.

**Proof.** Assume (FIN-Q). Since R'_bad⊆R_bad is finite (residue-locality) and each Q(r) is finite, the
set of relevant large primes
    Q_rel := ⋃_{r∈R'_bad} Q(r)
is a finite union of finite sets, hence **finite**. Put M := L_0·∏_{q∈Q_rel} q; this is squarefree, since
L_0's primes are ≤P_max and Q_rel's are >P_max, all distinct. We show m∈E_∞ is a function of m mod M for
every m>1; then for x≥a_1, x∈E_∞ ⟺ x+M∈E_∞ (same residue mod M, both >1), i.e. E_∞ is tail-periodic
from a_1 with period M.

Fix m>1, r:=m mod L_0.
- **r covering (r∉R_bad):** by the covering companion of (★), m∈E_∞ unconditionally — a function of
  r=m mod L_0, a fortiori of m mod M.
- **r∈R'_bad (E_∞ meets class r):** by (★), m∈E_∞ ⟺ for every i∈W(r), some q∈Q_i divides m. Take any
  m'>1 with m'≡m (mod M). For every prime q∈Q_rel we have q|M, so q|m ⟺ q|m'. Since each i∈W(r) has
  Q_i⊆Q(r)⊆Q_rel, the condition "∃q∈Q_i: q|m" holds iff "∃q∈Q_i: q|m'" **for each i separately**; hence
  the (possibly infinite) conjunction over i∈W(r) holds for m iff for m'. Also W(r),Q_i depend only on
  r=m mod L_0 | M, which equals m' mod L_0. Therefore m∈E_∞ ⟺ m'∈E_∞: membership is a function of m mod M.
  *(This is the crux of the strengthening: the argument never needs W(r) finite — only that the finitely
  many primes it can ever use, Q(r), all divide M. An infinite conjunction of conditions each depending on
  m mod M is itself a function of m mod M.)*
- **r∈R_bad, E_∞ misses class r:** then every m≡r has m∉E_∞ (the class-miss companion of (★)); the
  constant "false", a function of m mod L_0 | M.

In all cases m∈E_∞ is determined by m mod M. Now E_∞∩[a_1,∞) is infinite (it contains every multiple
k·a_1, k≥1, each a term). Apply PER with E=E_∞, a=a_1, L=M: the increasing enumeration b_1<b_2<… satisfies
b_{n+T}=b_n+M, T=#(E_∞∩[a_1,a_1+M))≥1; by ENUM that enumeration is a_1,a_2,…, so a_{n+T}=a_n+M for all n.

Finally (FIN-Q) is weaker than (FIN-W): if every W(r) is finite then every Q(r) (a finite union of finite
Q_i) is finite, so (FIN-W)⟹(FIN-Q); but Q(r) can be finite with W(r) infinite (infinitely many witness
colors all built from one fixed finite set of large primes), so the implication is strict. ∎

*Interpretation (single-sided infinite witnessing is harmless — now rigorous).* Suppose a bad class r is
obstructed by infinitely many witness colors that nevertheless draw on only finitely many distinct large
connector primes (in particular the extreme "star" case where a single fixed large prime p serves every
witness color, so Q(r)={p}∪(finite)). Lemma 2 shows this contributes exactly the finite factor
∏_{q∈Q(r)}q to the period M and yields **no obstruction**: E_∞ is still periodic. This is precisely the
finite-Q_rel bookkeeping the outliner flagged as DERIVED-not-certified; it is here proved from the
certified membership dichotomy (★). Consequently the only way periodicity can fail is

> **¬(FIN-Q):** some E_∞-inhabited bad class r_0 has Q(r_0) **infinite** —
> infinitely many *distinct* large primes appear across the witness colors of r_0.

By (FIN-W)⟹(FIN-Q), this is strictly harder to arrange than ¬(FIN-W); the wall has been narrowed.

---

### Step 3 — ¬(FIN-Q) forces a rich star, then a walk on a finite class-graph (gap-free up to the GAP)

Assume, for contradiction, ¬(FIN-Q): fix r_0∈R'_bad with Q(r_0) infinite, and a term m_0≡r_0 (m_0∈E_∞).

**(a) Extract an infinite distinct-prime witness family.** Q(r_0)=⋃_{i∈W(r_0)}Q_i is infinite and each Q_i
is finite, so W(r_0) is infinite. Greedily choose indices i_1,i_2,…∈W(r_0) and primes q_1<q_2<… with
q_k∈Q_{i_k} and all q_k distinct: at each stage only finitely many primes have been used, and Q(r_0) is
infinite, so some i∈W(r_0) contributes an unused large prime — pick it. Set b_k:=a_{i_k}. By the certified
Step 3 of the Reduction Lemma (W(r) points to bad terms), each b_k is **bad**; by Step 2 each b_k is
small-disjoint from m_0; and q_k|b_k with the q_k distinct and →∞. By GPC each b_k is off-lattice
(a_1∤b_k). Pigeonholing the infinitely many b_k into the finitely many classes mod L_0, pass to an infinite
subfamily lying in one class r_1∈R_bad; relabel so every b_k≡r_1 (mod L_0), still with the q_k distinct.

Thus ¬(FIN-Q) yields a **refined star**: a hub m_0 and an infinite family {b_k} of bad off-lattice terms,
all in one class r_1, each small-disjoint from m_0, carrying **distinct** large primes q_k. (The old
single-prime star of `bad-residue-witness-index` Step 5 is the degenerate Q(r_0) finite case, now excluded
by (FIN-Q); the genuine obstruction has infinitely many distinct connectors — the "mutual/cyclic" regime.)
Note each b_k, being small-disjoint from the fixed term m_0, shares a large prime with m_0 lying in the
finite set primes(m_0); so by a further pigeonhole infinitely many b_k share one fixed p_0|m_0 as their
connector to m_0 — the family connects to the hub through a single prime yet fans out through infinitely
many distinct primes q_k of its own. Since r_1∈R_bad is inhabited (by the b_k, which are terms in E_∞) and
bad, r_1∈R'_bad.

**(b) The class-graph and forced revisit.** Define a directed graph G on the finite vertex set R'_bad by:
draw r→r′ whenever some witness color of r lies in class r′, i.e. ∃ i∈W(r) with a_i≡r′ (mod L_0). Every
such a_i is bad (certified Step 3) and inhabited, so r′∈R'_bad: all edges of G stay inside R'_bad, a set
of size ≤L_0. By construction of the refined star, r_0→r_1 is an edge (each b_k=a_{i_k} with i_k∈W(r_0)
and b_k≡r_1). Moreover r_1 itself is bad and inhabited with Q(r_1)... — here we would iterate: each b_k is
bad, so has its own nonempty W(r_1); pick a witness color of r_1, giving an out-edge r_1→r_2, and so on,
producing an **infinite walk** r_0→r_1→r_2→… in the finite graph G. Since |V(G)|≤L_0 is finite, the walk
**revisits** some class: there are indices s<t with r_s=r_t, and in fact some class is revisited
infinitely often (finite range of an infinite sequence). This is the finite class-cycle structure the
approach targets.

**(c) The linking primes along the walk are ≥q* (Lemma A).** Every edge r→r′ of G is realized by a
small-disjoint pair {a_i,·} whose large link is ≥q* (Lemma A). So the walk carries, on each edge, a large
prime ≥q*; and along the refined-star fan-out at r_0 the primes q_k are *distinct* and unbounded.

**GAP (honest, unclosed) — Step 5 descent.** A contradiction from the revisiting walk is NOT established.
The two candidate closures flagged by the outliner remain open:

- **(5a) strict prime descent on a revisited class.** One wants: each return to a fixed revisited class
  r_* forces the realizing large linking prime to be strictly smaller than on the previous visit, yielding
  an infinite strictly-decreasing sequence of large primes ≥q*, impossible by well-ordering. *This descent
  is not produced.* Lemma A gives only the *floor* q* (the global minimum over all links), not a strict
  drop per return; and the refined star at r_0 exhibits the *opposite* behaviour (distinct primes q_k→∞,
  i.e. ascent), so no monotone descent is available from the material assembled. Producing a strictly
  decreasing large-prime monovariant along the walk is exactly the missing ingredient, and I could not
  construct it; asserting it from the q* floor would be the very error the outliner forbids.

- **(5b) first-hole over-constraint via Window Purity.** Along the fixed arithmetic progression of the
  refined star in class r_1 (terms ≡r_1 mod L_0 divisible by the connector p_0), let x be the smallest
  integer of that progression that is NOT in E_∞ (a "first hole"; one exists unless the whole progression
  lies in E_∞). By Window Purity every integer strictly inside each gap (a_n,a_{n+1}) has non-covering
  small part, and by the membership dichotomy (★) a class-r_1 integer fails E_∞ exactly when some witness
  color i∈W(r_1) is not cleared (no q∈Q_i divides it). One wants Window Purity + greedy minimality of the
  bracketing terms to force which witness color blocks x versus its neighbours into a contradiction with
  the fixed finite connector pool. *This contradiction is not extracted.* Crucially, the numeric caveat
  stands (verified this round via the explorer's data): a single predecessor need NOT block a whole window
  — only ~45–100% of windows are explained by one blocker depending on a_1 — so the argument must allow
  several blocking witness colors per interior integer, and the resulting bookkeeping did not close.

Because neither (5a) nor (5b) is completed, the contradiction with ¬(FIN-Q) is **not** obtained. The
theorem is therefore proved **conditionally on (FIN-Q)** (Lemma 2), with (FIN-Q) itself the honest open
gap — a strict weakening of the previously-standing (FIN-W).

---

### Summary of what is proved unconditionally this round

1. **Window Purity** (Lemma 1): every integer in an open gap (a_n,a_{n+1}) has non-covering small part.
   Gap-free, certifiable, numerically verified.
2. **(FIN-Q) ⟹ theorem** (Lemma 2): periodicity holds as soon as every inhabited bad class has a finite
   large-connector pool Q(r) — even with W(r) infinite. Gap-free; strictly weakens the certified
   (FIN-W)⟹theorem; rigorous form of "single-sided infinite witnessing is harmless".
3. The crux is thereby narrowed to **¬(FIN-Q)** (an inhabited bad class with infinitely many *distinct*
   large connector primes) and realized as an infinite revisiting walk on a finite (≤L_0-node) class-graph
   G carrying large primes ≥q*.

### Open gap (Current best of the crux)

**¬(FIN-Q) leads to no contradiction yet.** The revisiting walk on G is established, but the descent
mechanism (5a) (a strictly decreasing large-prime monovariant per revisit) is not produced, and the
first-hole over-constraint (5b) (Window Purity + greedy minimality forcing an impossible blocking pattern)
is not extracted. This is the field's standing wall, here relocated to: *an inhabited bad class cannot
draw on infinitely many distinct large connector primes.* No dead route is used (no covering/Helly — Prop D;
no global Σ1/p² capacity; no symmetric bad-partner ascent — which is proven to give no strict descent).

## Promotable lemmas

- **Window Purity.** *Statement:* for every n and every integer x with a_n<x<a_{n+1}, x∉E_∞ and S(x) is
  non-covering (some term a_j has primes(a_j)∩S(x)=∅). *Proof:* Lemma 1 above — gap-free, imports only
  ENUM and the immediate "covering ⟹ ∈E_∞". Numerically verified (0 violations, a_1∈{15,35,99,231}).
  Recommended for certification as `lemmas/window-purity.md`.

- **(FIN-Q) ⟹ theorem** (finite large-connector-pool periodicity). *Statement:* with Q(r):=⋃_{i∈W(r)}Q_i,
  if every E_∞-inhabited bad class r∈R'_bad has Q(r) finite, then E_∞ is tail-periodic from a_1 with period
  M=L_0·∏_{q∈Q_rel}q (Q_rel=⋃_{r∈R'_bad}Q(r)), hence a_{n+T}=a_n+L for all n. *Proof:* Lemma 2 above —
  gap-free; the key point is that membership (★) is a function of m mod M even when W(r) is infinite,
  because the infinite conjunction ranges over conditions each depending only on m mod M. This is a strict
  strengthening of the certified `finite-witness-periodicity.md` (which assumes the stronger (FIN-W)); it
  certifies the "single-sided-infinite-witnessing-is-harmless" reduction the field needed. Recommended for
  certification as `lemmas/finite-connector-pool-periodicity.md` (or as an amendment to the Reduction Lemma).
