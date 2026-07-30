# Approach: self-dual-clutter-grading

## Status
partial

## Approaches tried
- **self-dual-clutter-grading** (round 4, NEW) — Fielded the clutter/blocker-duality + value-grading
  framing. RIGOROUSLY PROVED (new, promotable): (i) the family of covering prime-sets equals the
  family of term prime-sets 𝒯 (realizability: every covering set is realized by an integer ≥ a_1,
  a term) — a genuine value ingredient absent from the dead pure-covering level; (ii) the clutter
  ℰ of minimal covering sets is **self-dual** (blocker(ℰ)=ℰ); (iii) **(CSP) ⟺ H_s is
  covering-dense** (every covering set has a covering subset inside [2,P_max]); (iv) base case
  |P|=1; (v) refined F1: every term is divisible by a prime of P. The **Step-4 grading lever
  remains an honest GAP**: after consuming realizability (Steps 1–3) the residual statement "H_s
  covering-dense" is the standing crux, and — as the gate warned — the value/size axiom I can
  legitimately add (a_1 minimal term; multiples of a_1 tile ℕ; a large-prime edge is realized only
  at value ≥ q) does **not** close it: it reduces to exactly the descent field's open Step 6→7
  (no contradiction from an infinite ascending chain of bad terms). Verdict: the set-theoretic
  reformulation is a clean certifiable win, but this framing does **not** close the crux and shares
  the field's wall. Recorded honestly, not dressed up.

## Current best

The whole problem is reduced (certified scaffold) to the single crux **(CSP)**: for every term m,
its small part S(m) = primes(m) ∩ [2, P_max] is a covering set, where P = primes(a_1),
P_max = max P. This approach recasts (CSP) in clutter/blocker-duality language, proves the
set-theoretic core rigorously (consuming value via realizability), and isolates the residual as a
sharp clutter statement that is the standing crux.

### Imported scaffold (certified — not re-proved)
- **Enumeration** (`lemmas/enumeration-of-E-infinity.md`): the greedy sequence is exactly the
  increasing enumeration of E_∞ ∩ [a_1, ∞), where E_∞ = {m>1 : gcd(m,a_i)>1 ∀ i}. So the *terms*
  are precisely the elements of E_∞ that are ≥ a_1.
- **Periodic-set endgame** (`lemmas/periodic-set-enumeration.md`): if E_∞ is tail-periodic from a_1
  with period L, then a_{n+T}=a_n+L for every n with T = #(E_∞∩[a_1,a_1+L)). Together with a finite
  relevant-prime set this yields the theorem.
- **(SL) ⟸ (CSP) two-liner** (certified reduction, `current.md`): if every term's small part is
  covering, any two terms A,B have S(A),S(B) covering; covering sets pairwise intersect (F1 below),
  so S(A)∩S(B) contains a small prime shared by A,B; hence E_∞ is a union of residue classes mod
  ∏_{p≤P_max}p, periodic, and the endgame closes. **So it suffices to prove (CSP).**
- **Prop C** (`lemmas/sole-connector-off-lattice.md`): if two terms A,B have primes(A)∩primes(B)={q}
  with q∉P then a_1∤A and a_1∤B. (Generalized form proved below as Lemma 6.)

Throughout, a *prime set* is a finite set of primes; for an integer m>1, primes(m) is its prime set.

---

### Step 0. Basic facts.

**F1 (pairwise intersecting terms).** For terms a_i, a_j with i<j the greedy rule imposes
gcd(a_j,a_i)>1, so primes(a_i)∩primes(a_j)≠∅. Hence any two term prime-sets intersect. (Certified;
part of the enumeration lemma.)

**Definition (covering set).** A prime set S is a **covering set** iff S ∩ primes(a_i) ≠ ∅ for every
term a_i (equivalently, ∏-realizations lie in E_∞; see Lemma 1). Write 𝒞 for the family of covering
sets and 𝒯 = {primes(a_i) : i≥1} for the family of term prime-sets.

**Lemma 0 (every term meets P).** For every term t, primes(t) ∩ P ≠ ∅; i.e. every term is divisible
by a prime of P = primes(a_1).
*Proof.* Pick a prime r with r∉P and r∤t (infinitely many primes exist; only finitely many divide
t or lie in P). Then k=r gives the term r·a_1 (a multiple of a_1, hence in E_∞ and ≥ a_1, hence a
term — certified). By F1, primes(t) meets primes(r·a_1) = P∪{r}. Since r∤t, the shared prime lies in
P. ∎ (Verified: `everyTermMeetsP=True` on seeds 15, 99, 231.)

In particular S(t) = primes(t)∩[2,P_max] ⊇ (primes(t)∩P) ≠ ∅: every term's small part is nonempty.

---

### Step 1. Realizability: the family of covering sets equals 𝒯. **(consumes value)**

**Lemma 1 (realizability).** For a finite prime set S the following are equivalent:
(a) S is a covering set; (b) some term has prime set exactly S; (c) every integer with prime set
⊇ S that is ≥ a_1 is a term. Consequently 𝒞 = 𝒯 (the covering sets are exactly the term
prime-sets), and every covering set is realized by infinitely many terms.

*Proof.* (a)⇒(b): fix p₀∈S and set m_k = (∏_{p∈S}p)·p₀^{k}. Then primes(m_k)=S for all k≥0, so
m_k has prime set S which is covering, giving gcd(m_k,a_i) ≥ (the shared prime) >1 for every i,
i.e. m_k ∈ E_∞. As m_k→∞ there is k with m_k ≥ a_1; by the enumeration lemma m_k is then a term
with prime set exactly S. (b)⇒(a): a term's prime set meets every term prime-set by F1, so it is
covering. (a)⇒(c): if primes(m)⊇S with S covering then primes(m) is covering, so m∈E_∞, and if
m≥a_1 it is a term. (c)⇒(b) take m=∏_{p∈S}p·p₀^k≥a_1 as above. Finally 𝒞=𝒯: a term prime-set is
covering by F1 (⇒ 𝒯⊆𝒞), and every covering set is a term prime-set by (a)⇒(b) (⇒ 𝒞⊆𝒯). ∎

This is the ingredient the abstract covering level (Prop D) lacks: covering sets are not an abstract
axiom system but are *realized by integers of controllable size ≥ a_1*. Every covering set literally
occurs as a term.

---

### Step 2. The clutter of minimal covering sets is self-dual.

Let **ℰ** = the minimal elements of 𝒞 under ⊆ (the *edges*). Since 𝒞 is an up-set (a superset of a
covering set is covering) and every covering set is finite, every covering set contains a member of
ℰ; ℰ is an antichain (a *clutter*). The **blocker** b(ℰ) is the clutter of minimal prime sets that
meet every member of ℰ.

**Lemma 2 (self-duality: b(ℰ)=ℰ).** A prime set S meets every member of ℰ iff S is a covering set.
Hence the minimal sets meeting every ℰ-member are exactly the minimal covering sets: b(ℰ)=ℰ.

*Proof.* (⇒) Suppose S meets every E∈ℰ. Let a_i be any term; primes(a_i)∈𝒯=𝒞 (Lemma 1), so
primes(a_i) contains some edge E∈ℰ. S meets E ⊆ primes(a_i), so S∩primes(a_i)≠∅. As a_i was
arbitrary, S is covering. (⇐) Suppose S is covering. Any E∈ℰ⊆𝒞=𝒯 is a term prime-set (Lemma 1),
and S covering means S meets every term prime-set, so S∩E≠∅. Thus S meets every ℰ-member.
Therefore {S : S meets every E∈ℰ} = 𝒞, and its minimal elements are ℰ; i.e. b(ℰ)=ℰ. ∎

So ℰ is a **self-dual clutter**: it is its own blocker. (This is consistent with, and sharper than,
the Prop-D observation that a_1=15 gives the self-dual triangle {2,3},{3,5},{2,5} among small
primes — a self-dual clutter with no common element/Helly centre. Self-duality is a *structural*
fact, not a proof of (CSP): the triangle is self-dual yet has no centre, exactly why pure
self-duality is insufficient and value must be consumed.)

---

### Step 3. (CSP) ⟺ H_s is covering-dense.

Let **H_s** := {E ∈ ℰ : E ⊆ [2, P_max]} — the *small edges*, minimal covering sets built from
primes ≤ P_max.

**Lemma 3 (H_s nonempty).** P = primes(a_1) is covering (Lemma 0 / F1: every term meets P) and
P ⊆ [2,P_max]; so P contains a minimal covering subset, which lies in H_s. Hence H_s ≠ ∅.

**Definition.** H_s is **covering-dense** iff every covering set E has a subset in [2,P_max] that is
covering, i.e. E∩[2,P_max] is covering for every covering set E.

**Lemma 4 ((CSP) ⟺ H_s covering-dense).**
*Proof.* By Lemma 1, quantifying over terms is the same as quantifying over covering sets (each term
prime-set is covering; each covering set is a term prime-set). For a covering set E:
E∩[2,P_max] is covering ⟺ E∩[2,P_max] contains a member of ℰ (up-set + minimality) ⟺ E∩[2,P_max]
contains a member of H_s (a covering set inside [2,P_max] contains a minimal covering set which is
itself ⊆[2,P_max], hence in H_s). Thus:
"every term m has S(m)=primes(m)∩[2,P_max] covering" (= (CSP))
⟺ "every covering set E has E∩[2,P_max] covering" (= H_s covering-dense). ∎

So the whole problem is now: **prove H_s is covering-dense** — every covering set (equivalently every
edge E∈ℰ) contains a small covering subset. Equivalently: **no edge E∈ℰ has E∩[2,P_max] non-covering.**

---

### Step 4 base case: |P| = 1.

**Lemma 5 (|P|=1 ⇒ (CSP)).** If a_1 = p^k is a prime power, P={p}, P_max=p. By Lemma 0 every term is
divisible by a prime of P, i.e. by p. Then {p}=P meets every term prime-set, so {p} is covering, and
{p}⊆[2,P_max]; thus for every term m, S(m)⊇{p} is covering. (CSP) holds, and H_s={{p}} is trivially
covering-dense. ∎

Henceforth assume |P| ≥ 2.

---

### Step 4: the grading lever — honest attempt and GAP.

Goal: show H_s is covering-dense, i.e. every edge E∈ℰ has E∩[2,P_max] covering. Suppose not; we seek
a contradiction from the extra **value/size axioms** the greedy dynamics supply (this is mandatory:
by the Prop-D barrier, no argument using only the self-dual clutter structure can succeed — the
a_1=15 triangle is a self-dual clutter with a non-covering... it must be broken by value).

**Value axioms available.**
- (V1) a_1 is the smallest term (enumeration lemma).
- (V2) Every multiple k·a_1 (k≥1) is a term; these *good* terms tile ℕ with gap a_1, and each has
  small part ⊇ P (Lemma 0 gives their small part meets P; in fact primes(k a_1)⊇P), which is
  covering — so every good term satisfies (CSP).
- (V3) Consecutive-gap bound a_{n+1}-a_n ≤ a_1 (certified), so terms are at least as dense as the
  a_1-lattice.
- (V4) Realizability with size control (Lemma 1): an edge E containing a large prime q>P_max is
  realized only by integers divisible by q, hence of value ≥ q.

**Lemma 6 (generalized Prop C).** If two terms A,B have primes(A)∩primes(B) ⊆ {primes > P_max}
(they share no small prime), then a_1∤A and a_1∤B.
*Proof.* If a_1|A then primes(A)⊇P. B meets a_1 in a prime p∈P (Lemma 0), so p∈P⊆primes(A) and p|B,
giving p∈primes(A)∩primes(B) with p≤P_max — contradicting that the intersection has only large
primes. So a_1∤A; symmetrically a_1∤B. ∎ (Promotes the singleton Prop C to any number of shared
large primes.)

**Structure of a would-be counterexample.** Suppose H_s is not covering-dense. Then there is an edge
E∈ℰ with W := E∩[2,P_max] non-covering. Realize E as a term m (Lemma 1); m is *bad* (S(m)=W
non-covering). Non-covering W means there is a term B with primes(B)∩W=∅. By F1 m,B share a prime,
which is not in W, hence not in E∩[2,P_max]; being in primes(m)=E it is a **large** prime q>P_max, so
q | m and q | B. By minimality of the edge E, E∖{q} is non-covering, so we may take B with
primes(B)∩E ⊆ {q}, i.e. B shares with m only the large prime q. By Lemma 6, a_1∤m and a_1∤B, so both
lie strictly inside length-<a_1 windows between consecutive multiples of a_1 (V2).

**Attempted grading contradiction (and where it fails).** The natural grading lever is: B is bad too
(if S(B) were covering it would meet primes(m)=E in a *small* prime, contradicting
primes(B)∩E⊆{q}), and B≠m (they meet only in q, and S(m)≠∅ ≠ S(B) by Lemma 0 gives distinct small
parts... more simply, if m=B then q∈W=S(m), contra), so we obtain another bad term B. Iterating
produces an infinite sequence m=m₀, m₁=B, m₂, … of bad terms, each linked to the next by a large
prime. Grading by **value** would demand this sequence be forced to *decrease* (well-ordering ⇒
contradiction). But value forces the opposite: taking m₀ minimal among bad terms makes every
large-partner strictly *larger* (minimality), giving an **infinite strictly ascending** chain of bad
terms. An infinite ascending chain is **not** a contradiction — there is no largest term and the
sequence lives inside the infinite off-lattice windows guaranteed by Lemma 6.

I tried to close this with the good-term tiling (V2): each bad m sits within a_1 of a good term
M=a_1⌈m/a_1⌉ that satisfies (CSP). But M being good gives an *upper* structural bound only on the
a_1-lattice; it does not constrain how "large-prime-heavy" the off-lattice m is, and it cannot be
used as a *smaller competitor* against m (the interval (a_n, m) below a term m=a_{n+1} is empty of
E_n by minimality — the dead window-minimality wall recorded in `run_state.md`). I also tried
tracking the linking prime q up the chain (V4: each bad term has value ≥ its large prime): if a
single q persisted it would divide an infinite set of bad terms in distinct windows, but nothing
bounds the number of q-multiples that can be bad; if q must change each step, I found no monovariant
on the (value, largest-large-prime) pair that is forced to descend.

**GAP (Step 4).** After consuming realizability (Steps 1–3) and the value axioms (V1)–(V4), the
residual — *H_s is covering-dense* / *no edge has non-covering small part* — is **not** closed by
this framing. It reduces to producing a contradiction from an infinite strictly ascending,
large-prime-linked chain of bad off-lattice terms, which is **exactly** the open Step 6→7 of the
`covering-small-part-descent` approach. The clutter/self-duality reformulation is rigorous and
consumes value at the realizability level, but the grading/size axiom I can legitimately add does
**not** break the self-dual triangle at the edge level; it collapses to the shared wall.

**Honest verdict (as the gate requested).** This framing succeeds set-theoretically (Lemmas 1–5 are
clean, new, promotable) but its Step-4 grading lever does not consume value in a way that closes the
crux. It should be kept as a *reformulation* (the self-dual clutter picture + covering-density
target are genuinely useful restatements), not advanced as a live route to the solve unless a value
monovariant on the bad-term chain is found. It shares the field's wall.

---

### Summary of what is rigorously established here
1. 𝒞 = 𝒯: covering sets = term prime-sets (realizability, Lemma 1). **New, promotable.**
2. ℰ (minimal covering sets) is a self-dual clutter, b(ℰ)=ℰ (Lemma 2). **New, promotable.**
3. (CSP) ⟺ H_s covering-dense (Lemma 4); H_s≠∅ (Lemma 3). **New, promotable.**
4. |P|=1 base case (Lemma 5); every term meets P (Lemma 0); generalized Prop C (Lemma 6).
5. The residual crux is *H_s covering-dense*, equivalent to the descent field's open gap; Step 4
   grading does **not** close it. Recorded as GAP.

## Promotable lemmas

- **Realizability / 𝒞=𝒯** (Lemma 1): For a finite prime set S, S is a covering set ⟺ some term has
  prime set exactly S ⟺ every integer with prime set ⊇S and ≥a_1 is a term. Hence the covering sets
  are exactly the term prime-sets, and every covering set is realized by infinitely many terms.
  *Proved above from the enumeration lemma + F1 (m_k=(∏_{p∈S}p)p₀^k realizes S and →∞).* Reusable
  by any approach reasoning about covering sets as objects.
- **Self-dual clutter** (Lemma 2): the clutter ℰ of minimal covering sets satisfies b(ℰ)=ℰ; a prime
  set meets every minimal covering set iff it is covering. *Proved above via 𝒞=𝒯.*
- **(CSP) ⟺ H_s covering-dense** (Lemma 4): (CSP) holds iff every covering set has a covering subset
  inside [2,P_max]. *Proved above.* A clean equivalent target for the crux.
- **Every term meets P** (Lemma 0): every term is divisible by a prime of P=primes(a_1); hence every
  term's small part is nonempty. *Proved above (choose a fresh prime r for the good term r·a_1).*
- **Generalized Prop C** (Lemma 6): two terms sharing no small prime are both off the a_1-lattice.
  *Proved above; supersedes the singleton `sole-connector-off-lattice.md`.*
