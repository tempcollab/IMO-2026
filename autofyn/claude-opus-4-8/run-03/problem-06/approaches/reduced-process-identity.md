## Status
partial

## Approaches tried
- (round 4, advance) Patched the reviewer-flagged (SL) ⟸ multi-large-prime gap: stated and proved
  in full **generalized Prop C (GPC)** (§3a), dropping the singleton hypothesis of the certified
  Prop C — any two terms sharing no small prime are both off the a_1-lattice, whatever the number of
  shared large primes. Retired the strictly-weaker "Lemma A" singleton phrasing; the target is now
  correctly (SL) ⟺ (CSP). Reframed the inductive step as **redundancy** (RED_n: S_{n+1} covers the
  predecessor list), not the FALSE "a_{n+1} is P_max-smooth" (disproved: a_1=231 has good term
  237=3·79). Added §5(G5) recording the redundancy structure — missed predecessors are pairwise
  small-compatible yet a_{n+1} avoids all their small supports — and an honest account of why
  redundancy sharpens but does not close the crux (large bridges may coincide; empty window forbids a
  competitor). GPC promoted for certification. Residual = (RED_n), the shared crux, honestly GAP.
- (round 2, new) Static process-coincidence framing: prove the true greedy sequence equals the
  "small-primes-only" greedy sequence termwise, by strong induction. The small-only sequence is
  manifestly finite-state periodic; the whole difficulty is a single reverse inequality equivalent
  to the certified crux (Lemma A / Structural Lemma), re-packaged as "the two sequences never
  diverge, even once." Numerically exact on a_1∈{15,35,77,97,105,143,182,1155,2431}.
- (round 2, build) Filled the framing into a complete rigorous proof of everything EXCEPT the
  reverse inequality. Made the reduced set `E*` and its periodicity fully rigorous (finitely many
  distinct small-supports ⇒ union of residue classes mod L_0 = ∏_{p≤P_max} p), proved the easy
  direction, and reduced the theorem to the clean equivalent: `E_∞ ∩ [a_1,∞) ⊆ E*`, i.e. every
  term small-hits every other term. Proved several new rigorous auxiliary facts (a_{n+1} ≤ a_n+a_1;
  the missed predecessor must itself carry a prime > P_max; the "divergence" is a strict inequality
  with both witnesses in one length-a_1 window). The reverse inequality itself remains an HONEST
  GAP — and I identify precisely why the natural competitor/minimality route cannot close it
  (the window (a_n, a_{n+1}) is empty by minimality, so no smaller compatible competitor exists;
  the claim is a property of the value a_{n+1}, not an existence-of-competitor statement).

## Current best
The whole problem is rigorously reduced (importing the two certified lemmas) to the single
statement **(SL): every term shares a prime ≤ P_max with every other term**, equivalently
**E_∞ ∩ [a_1,∞) ⊆ E\***. Given (SL) the theorem follows completely and rigorously with the
explicit period L = L_0 = ∏_{p ≤ P_max} p and T = #(E\* ∩ [a_1, a_1+L_0)). Everything in the
proof below is complete except the single step **(SL)**, which is the standing crux of P6.
New rigorous sub-results: (round 4) **generalized Prop C (GPC, §3a)** — any two terms sharing no
small prime are both off the a_1-lattice (multi-large-prime case included), which patches the (SL) ⟸
gap and is promoted for certification; the inductive step is reframed as redundancy **(RED_n)**, and
§5(G5) shows the missed predecessors are pairwise small-compatible while a_{n+1} avoids all their
small supports. (round 2) the divergence, if it ever occurred, would be a strict inequality
a_{n+1} < b_{n+1} with both in (a_n, a_n+a_1], forcing a_{n+1} to share a prime > P_max with some a_k
while sharing no small prime with it, and a_k itself off-lattice. The competitor/minimality route is
proved structurally incapable of closing (SL); the residual crux is (RED_n).

## Imported (certified, gap-free)
- `lemmas/enumeration-of-E-infinity.md`: with E_∞ := {m>1 : gcd(m,a_i)>1 ∀i}, the sequence is the
  increasing enumeration of E_∞ ∩ [a_1,∞); and a_{n+1} = min(E_n ∩ (a_n,∞)) where
  E_n := {m>1 : gcd(m,a_i)>1 ∀ i≤n}.
- `lemmas/periodic-set-enumeration.md`: if E ⊆ ℤ is nonempty and tail-periodic from a with period
  L>0, and b_1<b_2<… enumerates E ∩ [a,∞), then b_{n+T}=b_n+L for all n, with
  T = #(E ∩ [a,a+L)) ≥ 1.

Notation. a_1 > 1 is the given first term. P := {primes dividing a_1}, P_max := max P (well-defined
since a_1>1). For an integer m>1 write primes(m) for its set of prime factors, and
S(m) := primes(m) ∩ [2, P_max] its "small support". For a term a_i write Q_i := primes(a_i) and
S_i := S(a_i). Set L_0 := ∏_{p ≤ P_max} p (product over all primes ≤ P_max; squarefree).

---

## Full reduction and proof (complete except step (SL))

### 1. Standing facts (fully proved)

**(F1) Every term shares a prime of P with a_1, so S_i ≠ ∅.**
For i ≥ 2 the defining rule imposes gcd(a_i, a_1) > 1, and gcd(a_1,a_1)=a_1>1 for i=1; hence a_i
and a_1 share a prime p. Since p | a_1, p ∈ P, so p ≤ P_max, thus p ∈ S_i and p ∈ P. In
particular S_i ≠ ∅ and P ∩ S_i ≠ ∅ for every i.  ∎(F1)

**(F2) Every multiple of a_1 that is > 1 lies in E_∞ and is "small-compatible".**
Let m = k·a_1 (k ≥ 1). For each i, by (F1) a_i and a_1 share a prime p ∈ P; then p | m and p | a_i,
so gcd(m,a_i) ≥ p > 1, giving m ∈ E_∞. Moreover p ≤ P_max, so p ∈ S(m) ∩ S_i, i.e. m shares a
small prime with every a_i.  ∎(F2)

**(F3) Bounded gap: a_{n+1} - a_n ≤ a_1, hence a_{n+1} ≤ a_n + a_1 ≤ 2a_n.**
The least multiple of a_1 exceeding a_n is some k·a_1 with a_n < k·a_1 ≤ a_n + a_1. By (F2)
k·a_1 ∈ E_∞ ⊆ E_n and k·a_1 > a_n, so it is a candidate for a_{n+1} = min(E_n ∩ (a_n,∞)); thus
a_{n+1} ≤ k·a_1 ≤ a_n + a_1. Since a_n ≥ a_1 (the sequence is increasing from a_1), a_1 ≤ a_n and
a_{n+1} ≤ 2a_n.  ∎(F3)

### 2. The reduced set E* and its periodicity (fully proved)

Define the **reduced compatible set**
> E* := { m > 1 : S(m) ∩ S_i ≠ ∅ for every index i },

i.e. m ∈ E* iff m shares a prime ≤ P_max with every term. (The constraints range over the fixed —
though a priori unknown — infinite family {S_i}_{i≥1}.)

**(P1) E* ⊆ E_∞.**
If m ∈ E* then for each i it shares a prime p ≤ P_max with a_i; that p divides both m and a_i, so
gcd(m,a_i) ≥ p > 1. Hence m ∈ E_∞.  ∎(P1)

**(P2) E* is exactly periodic mod L_0.**
For m > 1 put D(m) := {p ≤ P_max : p | m} = S(m). Membership m ∈ E* is the condition
"D(m) ∩ S_i ≠ ∅ for all i", which depends on m only through the set D(m). Now each S_i is a subset
of the finite set {primes ≤ P_max}; there are only finitely many subsets of that finite set, so the
family {S_i}_{i} contains only finitely many *distinct* sets — call the distinct nonempty ones
𝒮 = {T_1,…,T_r} (nonempty by (F1)). Then
> m ∈ E* ⟺ D(m) ∩ T_ℓ ≠ ∅ for ℓ = 1,…,r,

finitely many constraints. For a prime p ≤ P_max, whether p | m is determined by m mod p, and since
p | L_0, it is determined by m mod L_0 (CRT — KB: *Modular arithmetic, Chinese Remainder Theorem*:
the residue of m modulo each prime factor of L_0 is a function of m mod L_0). Hence D(m) is a
function of (m mod L_0), and so is the truth value of each constraint. Therefore membership in E* is
constant on each residue class mod L_0: for every m ≥ 2,
> m ∈ E* ⟺ (m + L_0) ∈ E*.
So E* is exactly periodic with period L_0 (in particular tail-periodic from a_1).  ∎(P2)

**(P3) E* ∩ [a_1,∞) is infinite; T_0 := #(E* ∩ [a_1, a_1+L_0)) ≥ 1.**
By (F2) every multiple k·a_1 ≥ a_1 lies in E*, so E* ∩ [a_1,∞) is infinite. In particular a_1 itself
lies in E* (take k=1), and a_1 ∈ [a_1, a_1+L_0), so T_0 ≥ 1.  ∎(P3)

**(P4) a_1 ∈ E*, and consequently the enumerations start together.**
Immediate from (P3) (k=1 in (F2)): a_1 ∈ E* and a_1 = a_1.  ∎(P4)

### 3. The theorem follows from a single set inclusion (fully proved, conditional on (SL))

Let b_1 < b_2 < … be the increasing enumeration of E* ∩ [a_1,∞) (infinite by (P3)). By the certified
`periodic-set-enumeration` lemma applied to E = E*, a = a_1, L = L_0 (hypotheses met by (P2),(P3)):
> b_{n+T_0} = b_n + L_0 for every n ≥ 1,   with T_0 = #(E* ∩ [a_1, a_1+L_0)) ≥ 1.   (★)

By the certified `enumeration-of-E-infinity` lemma, a_1 < a_2 < … is the increasing enumeration of
E_∞ ∩ [a_1,∞). By (P1), E* ∩ [a_1,∞) ⊆ E_∞ ∩ [a_1,∞). Therefore:

> **If E_∞ ∩ [a_1,∞) ⊆ E* (equivalently E_∞ ∩ [a_1,∞) = E* ∩ [a_1,∞)), then a_n = b_n for all n,
> and (★) gives a_{n+T_0} = a_n + L_0 for every n — the theorem, with T = T_0 and L = L_0.**

Indeed, two increasing enumerations of one and the same subset of ℤ agree termwise. So the entire
problem reduces to the inclusion
> **(SL)   E_∞ ∩ [a_1,∞) ⊆ E\*,   i.e. every term a_j shares a prime ≤ P_max with every term a_i.**

(The equivalence "(SL) ⟺ every term small-hits every term" holds because E_∞ ∩ [a_1,∞) is exactly
the set of terms by the enumeration lemma, and a_j ∈ E* unfolds to "a_j shares a prime ≤ P_max with
every a_i".) The true admissible set and the reduced admissible set coincide above a_1 exactly when
(SL) holds, so the two greedy sequences coincide termwise.

**Corrected note on the earlier "Lemma A" phrasing (patched below).** A previous round phrased the
crux as **Lemma A**: "no prime q > P_max is the *sole* shared prime of two terms." (SL) ⟹ Lemma A is
immediate, but Lemma A ⟹ (SL) is **not** valid: two terms could share exactly the large primes
{q_1, q_2} (both > P_max) and no small prime — an (SL)-violation that Lemma A (a singleton ban) does
not forbid. So Lemma A is strictly weaker than (SL), and one must not target it. We therefore target
**(SL) / (CSP) directly**; §3a below (generalized Prop C) is the tool that handles the multi-large-
prime configuration uniformly, closing the ⟸ gap the reviewer flagged.

### 3a. Generalized Prop C (multi-large-prime patch; PROMOTED for certification)

**(GPC) Generalized sole-off-lattice constraint.** Let A, B be any two terms of the sequence that
share *no* small prime, i.e. S(A) ∩ S(B) = ∅ (equivalently primes(A) ∩ primes(B) contains only
primes > P_max — of which there may be one, several, or, together with the pairwise-hit guarantee,
at least one). Then a_1 ∤ A and a_1 ∤ B.

*Proof.* Suppose a_1 | A. Then primes(A) ⊇ primes(a_1) = P, so P ⊆ primes(A). By (F1), B is a term
and hence shares a prime of P with a_1; that is, some p ∈ P divides B. Now p ∈ P ⊆ primes(A) and
p | B, so p ∈ primes(A) ∩ primes(B). But p ∈ P means p ≤ P_max, so p ∈ S(A) ∩ S(B), contradicting
S(A) ∩ S(B) = ∅. Hence a_1 ∤ A. The argument is symmetric in A, B, so a_1 ∤ B as well.  ∎(GPC)

*Remarks.* (i) The proof uses **only** the two certified facts "every term is divisible by a prime of
P" and "P ⊆ primes(A) when a_1 | A"; it never uses that the shared large primes are a singleton, so
it strictly generalizes the certified `sole-connector-off-lattice` (Prop C), whose hypothesis
primes(A) ∩ primes(B) = {q}, q ∉ P, is the special case |shared| = 1. (ii) Consequence used below:
**every (SL)-violating pair of terms lies entirely off the a_1-lattice** — regardless of how many
large primes the two terms share. In particular a "bad" term (one violating (CSP)) is never a
multiple of a_1, so it is strictly confined between two consecutive multiples of a_1 (a window of
length < a_1).  This patches the multi-large-prime gap in the (SL) ⟸ direction: we no longer need
the singleton phrasing, and no (SL)-violation can hide behind two-or-more shared large primes.

### 4. (SL) as a strong induction (the assigned framing)

(SL) is equivalent to the following statement, proved by strong induction on n:
> **(SL_n)   for every n, a_{n+1} shares a prime ≤ P_max with each of a_1,…,a_n.**

Equivalence: (SL_n) for all n ⟹ (SL): given terms a_i, a_j with i < j, apply (SL_{j-1}) with the
predecessor a_i (i ≤ j-1) to get a_i, a_j small-sharing; and a_j shares a small prime with itself
trivially. Conversely (SL) ⟹ (SL_n) directly.

Reformulate via small supports: a_{n+1} small-hits a_k ⟺ S_{n+1} ∩ S_k ≠ ∅ (a shared prime
≤ P_max lies in both small supports; conversely a common element of S_{n+1}, S_k is a shared prime
≤ P_max). So (SL_n) says **S_{n+1} meets each of S_1,…,S_n**.

**Base n = 1.** By (F1), a_2 shares a prime of P (hence ≤ P_max) with a_1: S_2 ∩ S_1 ⊇ P ∩ S_1 ∩ S_2;
concretely a_2 and a_1 share a prime p ∈ P, and p ∈ S_1 ∩ S_2. So S_2 ∩ S_1 ≠ ∅. ✓

**Inductive hypothesis (IH_n).** S_1,…,S_n are pairwise intersecting nonempty subsets of the finite
set {primes ≤ P_max}. (This is exactly (SL_k) for all k < n, plus (F1).)

**Inductive step — the reverse inequality (THE GAP).** We must show S_{n+1} meets each S_k (k ≤ n).
By the enumeration lemma, a_{n+1} = min(E_n ∩ (a_n,∞)). Consider the reduced quantity
> β := min{ m > a_n : m shares a prime ≤ P_max with each of a_1,…,a_n }
>    = min{ m > a_n : S(m) ∩ S_k ≠ ∅ for all k ≤ n }.

β is well-defined and β ≤ a_n + a_1: the next multiple of a_1 above a_n lies in (a_n, a_n+a_1] and
small-hits every a_k by (F2). By (P1)-type reasoning any such m lies in E_n (a small hit is a hit),
so β ∈ E_n ∩ (a_n,∞); minimality of a_{n+1} gives the **easy direction**
> a_{n+1} ≤ β.   (Easy)

(SL_n) is precisely the reverse inequality **β ≤ a_{n+1}**, i.e. a_{n+1} is itself one of the
small-compatible candidates competed for by β, i.e. **a_{n+1} ∈ {m : S(m) ∩ S_k ≠ ∅ ∀k≤n}**. This
is the whole difficulty and is **left as an honest gap** — see §5 and §6.

### 5. New rigorous facts about the (hypothetical) failure of (SL_n)

Suppose, for contradiction toward a future proof, that (SL_n) fails at some n: a_{n+1} shares no
prime ≤ P_max with some predecessor a_k (k ≤ n). The following are rigorous consequences (they
sharpen the target and rule out the naïve routes; none of them closes the gap).

**(G1) Strict divergence in a single length-a_1 window.** By (Easy), a_{n+1} ≤ β. If a_{n+1} = β then
a_{n+1} would small-hit every a_k (β does), contradicting the failure; so a_{n+1} < β. Both satisfy
a_n < a_{n+1} < β ≤ a_n + a_1 (using (F3) and β ≤ a_n+a_1). Thus the failure is a *strict* inequality
with a_{n+1} and its small-competitor β both inside the window (a_n, a_n + a_1].

**(G2) The connection to a_k is via large prime(s); both a_{n+1} and a_k are off the a_1-lattice.**
a_{n+1} ∈ E_n so gcd(a_{n+1}, a_k) > 1: they share a prime q. Since they share no prime ≤ P_max
(failure), q > P_max, and in fact **every** prime shared by a_{n+1} and a_k exceeds P_max, i.e.
S_{n+1} ∩ S_k = ∅. So the pair (a_{n+1}, a_k) satisfies the hypothesis of **(GPC)** (share no small
prime); by (GPC), **a_1 ∤ a_{n+1} and a_1 ∤ a_k**. In particular the predecessor a_k carries a prime
> P_max and is itself off the a_1-lattice, and so is a_{n+1}. This holds whether the two terms share
one large prime or several — the multi-large-prime case is covered with no extra hypothesis.

*Caveat (the false target, avoided).* We do **not** claim a_{n+1} is P_max-smooth: it may carry large
primes freely. E.g. for a_1 = 231 (P = {3,7,11}, P_max = 11) the term 237 = 3·79 carries the large
prime 79, yet it is a **good** term because S(237) = {3} already meets every predecessor. The correct
target is **redundancy** — that a_{n+1}'s *small* support S_{n+1} alone already meets every
predecessor — not smoothness of a_{n+1}.

**(G3) The competitor/minimality route is structurally blocked — do not retry it.**
The interval (a_n, a_{n+1}) contains **no** element of E_n at all, by the definition
a_{n+1} = min(E_n ∩ (a_n,∞)). Hence (SL_n) can NOT be established by exhibiting a compatible integer
smaller than a_{n+1}: no such integer exists. (SL_n) is a statement about the *value* a_{n+1} (that
its shared primes with each predecessor can be taken ≤ P_max), not an existence-of-smaller-competitor
statement. Equivalently, one cannot contradict the minimality of a_{n+1}: it is genuinely minimal.
This is why generic CRT/pigeonhole window-counting fails here (a length-a_1 window need not contain a
representative of a prescribed small hitting-pattern, since the CRT modulus can exceed a_1), and why
the "peel the large prime q from a_{n+1}" idea is circular (a_{n+1}/q < a_n by (F3), so it is not a
candidate for minimality; and its being in E_∞ is a consequence of (SL), not a hypothesis).

**(G4) The IH is a pairwise-intersecting (not necessarily commonly-intersecting) family.** By (IH_n),
{S_1,…,S_n} is pairwise intersecting, but need NOT have a common element (e.g. {2,3},{3,5},{2,5}
occur as small supports for suitable a_1). So Helly/sunflower on a common small prime is unavailable;
(SL_n) must be forced by the greedy value a_{n+1} together with the pairwise structure, not by a
single universal small prime.

**(G5) The inductive step in redundancy form (the assigned reframing).** By §4 the step is exactly:
> **(RED_n)   S_{n+1} meets each of S_1,…,S_n**   (the small support of a_{n+1} is *covering* on the
> predecessor list — i.e. a_{n+1} ∈ E* restricted to the first n constraints).

Assume (RED_n) fails, so a_{n+1} is bad: pick k ≤ n with S_{n+1} ∩ S_k = ∅. By (G2), a_{n+1} hits a_k
only through large primes, and (GPC) puts both off the a_1-lattice. We now record what redundancy
forces and where the argument stalls, honestly.

(a) *S_{n+1} is nonempty and covering except at the missed set.* By (F1), a_{n+1} shares a prime of P
with a_1, so S_{n+1} ⊇ {that prime} ≠ ∅. Let J := {k ≤ n : S_{n+1} ∩ S_k = ∅} be the set of missed
predecessors (nonempty by assumption). For k ∈ J the hit a_{n+1}↔a_k is purely large; for k ∉ J it is
(also) small.

(b) *The missed predecessors are pairwise large-linked to a_{n+1} and mutually small-compatible.*
By (IH_n) the family {S_1,…,S_n} is pairwise intersecting, so any two missed predecessors a_k, a_{k'}
(k,k' ∈ J) themselves share a small prime: S_k ∩ S_{k'} ≠ ∅. Yet a_{n+1} avoids the small support of
each of them (S_{n+1} ∩ S_k = ∅ = S_{n+1} ∩ S_{k'}). So a_{n+1}'s small support S_{n+1} is disjoint
from ⋃_{k∈J} S_k, while a_{n+1} must nonetheless *hit* every a_k, k ∈ J, through large primes.

(c) *Simultaneous compatibility is the pressure — but it is not yet a contradiction.* For each k ∈ J
choose a large prime q_k > P_max with q_k | a_{n+1}, q_k | a_k. The q_k need not be distinct (one
large prime could serve several missed predecessors), and this is exactly the residual difficulty:
"a_{n+1} bridges every missed predecessor by large primes" costs a_{n+1} only *some* large prime
factors, of which it may have arbitrarily many, so no immediate numeric contradiction with
a_{n+1} ≤ a_n + a_1 arises (the large primes may coincide, keeping a_{n+1} small). The natural closing
move — replace the large bridges by small ones to build a compatible integer below a_{n+1} — is
**forbidden**: by (G3) the window (a_n, a_{n+1}) is empty of E_n, so no smaller compatible integer
exists, and any construction of one would contradict the *proven* minimality of a_{n+1}. Thus (RED_n)
is a statement about the *value* a_{n+1} (that its already-present small factors suffice), not an
existence-of-competitor statement, and the redundancy reframing, while it sharpens the target to the
covering property of the single set S_{n+1}, does **not** by itself produce the contradiction.

This isolates the crux to its sharpest form: *the minimal E_n-element a_{n+1} above a_n — which lies in
a length-a_1 window that also contains the fully small-compatible good integer β (a multiple of a_1) —
has a small support S_{n+1} that already meets every predecessor's small support.* Equivalently, the
greedy minimum never needs a large prime as its **sole** bridge to any predecessor. That combinatorial
fact about greedy minimality against an unbounded pairwise-intersecting history is the genuine content
of IMO 2026 P6 and is **not closed here**.

### 6. The honest gap

**GAP (unproven).** The redundancy step **(RED_n)** of §4/§5(G5): the greedy term a_{n+1} has a
small support S_{n+1} that meets S_k for every predecessor k ≤ n (equivalently the reverse inequality
β ≤ a_{n+1}; equivalently (SL_n)). This is the standing crux (CSP) at the single value a_{n+1},
re-expressed as termwise non-divergence of the two greedy processes. Verified computationally with
zero exceptions (a_1 ∈ {15,35,77,97,99,105,143,182,231,1024,1155,2431,…}, 40–200 terms each), but not
proved. §5 records precisely which attack routes are structurally excluded and must not be retried:
competitor/minimality in the empty window (G3), generic CRT window-counting (G3), Helly/common-prime
on the pairwise-but-not-central family (G4), and the false "a_{n+1} is P_max-smooth" target (G2
caveat; 237 = 3·79 is a good term for a_1 = 231).

**What is newly complete this round.** The multi-large-prime patch is closed: **(GPC)** (§3a) is a full,
gap-free proof that *any* (SL)-violating pair — one shared large prime or several — has both members
off the a_1-lattice, so the (SL) ⟺ (CSP) target is now correctly and uniformly stated (the weaker
singleton "Lemma A" is retired). Everything else — the reduction (§1–§3, §3a), the periodicity of E*
(§2), the easy direction (§4 Easy), and the deduction of the theorem with explicit L = L_0 = ∏_{p≤P_max} p
and T = #(E* ∩ [a_1,a_1+L_0)) from (SL) — is complete and rigorous. The sole residual is (RED_n).

∎ (conditional on (SL))

## Promotable lemmas
- **Generalized Prop C (GPC) — multi-large-prime off-lattice constraint.** Statement: if two terms
  A, B share no prime ≤ P_max (S(A) ∩ S(B) = ∅), then a_1 ∤ A and a_1 ∤ B. Proved in full in §3a from
  the two certified facts "every term is divisible by a prime of P" and "a_1 | A ⇒ P ⊆ primes(A)";
  the singleton hypothesis of the certified `sole-connector-off-lattice` (Prop C) is dropped, so this
  strictly generalizes it and covers the multi-large-prime configuration with no extra cost. Gap-free
  and reusable: it confines every (SL)-violating pair (hence every bad term) strictly off the
  a_1-lattice, patching the (SL) ⟸ multi-large-prime gap the reviewer flagged. **Propose to certify
  into `lemmas/generalized-sole-connector-off-lattice.md`.**
- **Reduced-set periodicity (E\* periodic mod L_0).** Statement: with S_i = primes(a_i) ∩ [2,P_max]
  and E* = {m>1 : S(m) ∩ S_i ≠ ∅ ∀ i}, the set E* is exactly periodic mod L_0 = ∏_{p≤P_max} p, is
  contained in E_∞, contains every multiple of a_1, and a_1 ∈ E*. Proved in full in §2 ((P1)–(P4))
  from (F1)–(F2); uses only CRT and finiteness of the subsets of {primes ≤ P_max}. Reviewer may
  certify: it is gap-free and reusable (it packages the "E_∞ periodic once the small-support family
  is the true constraint set" endgame for the process-identity framing).
- **Reduction to set inclusion (§3).** Statement: if E_∞ ∩ [a_1,∞) ⊆ E*, then a_{n+T}=a_n+L for all
  n with L = L_0, T = #(E* ∩ [a_1,a_1+L_0)). Proved in full from the two certified lemmas + (P1)–(P3).
  Gap-free; equals the standing "R finite ⇒ theorem" endgame in the E* phrasing.
- (No new certifiable lemma resolves the crux (SL); it remains the open gap.)
