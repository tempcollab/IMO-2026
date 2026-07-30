## Status
partial

## Approaches tried
- (round 2, new) Dynamic recruitment monovariant: process terms in order, track the finite set
  R_i of load-bearing primes, and show a new prime enters R only via the P_max-smooth cofactor of
  a greedily-minimal witness term. Reduces the crux to a cofactor-smoothness claim about the
  smallest compatible integer in a length-a_1 window. Distinct surface from the static framings:
  analyses the factorization of the term that TRIGGERS each recruitment (explorer-2, round 2).
- (round 2, build) Imported the certified reduction verbatim; recast the crux (Lemma A) in the
  recruitment/cofactor language with full rigor; **proved two new clean facts** — (i) a
  sole-connector term is never a multiple of a_1 (Prop C), and (ii) a *set-theoretic barrier*: the
  crux is FALSE at the level of abstract covering families, so any proof MUST use the greedy order
  (Prop D). Localized the residual to a single greedy-minimality statement (Gap G). The
  cofactor-smoothness bound is NOT closed; recorded honestly. Status remains partial.

## Current best
The whole problem is imported-reduced (certified, gap-free) to: **no prime q > P_max is the exact
common-prime factor of two terms** (Lemma A). This round adds, in full rigor:
- **Prop C** (new): if two terms share exactly one prime q with q ∉ P (in particular q > P_max),
  then neither term is a multiple of a_1. So every sole-connector term avoids the a_1·ℤ lattice.
- **Prop D** (new, a *barrier* result): the crux cannot be decided by the covering/hitting-set
  structure of F alone — there is an abstract intersecting covering family in which a large prime is
  a minimal member. Hence every correct proof (this framing included) must invoke the greedy
  minimality of the terms, not just "which sets are covering." This kills a class of purely
  set-theoretic attempts and sharply focuses the remaining work.
- The crux is restated as **Gap G** (below): the connectivity-carrying cofactor of the greedily
  minimal witness term is P_max-smooth. This is the sole open step; it is a statement about the
  greedy minimum in a length-a_1 window, and by Prop D it genuinely requires the dynamics.

## Imported (certified, gap-free)
- `lemmas/enumeration-of-E-infinity.md`: terms = increasing enumeration of E_∞ ∩ [a_1,∞),
  E_∞ = {m>1 : gcd(m,a_i)>1 ∀i}.
- `lemmas/periodic-set-enumeration.md`: E tail-periodic mod L ⇒ b_{n+T}=b_n+L for all n.
- `approaches/enum-covering-primes.md` Steps 1–4 + R1/R2 (reviewer-certified): the covering
  characterization, the exact identity **R = {q : some pair of terms has prime-intersection exactly
  {q}}**, and **R finite ⇒ the theorem**. In particular **Lemma A ⇒ R ⊆ {primes ≤ P_max} ⇒ theorem.**
- Certified auxiliary facts: every multiple of a_1 lies in E_∞ (its prime set ⊇ P is covering) and
  is therefore a term; consecutive gaps a_{n+1} − a_n ≤ a_1.

## Notation
D := a_1. For m>1, primes(m) is its set of prime factors. P := primes(D), P_max := max P.
A finite prime set S is **covering** if S ∩ primes(a_i) ≠ ∅ for every index i. E_∞ and terms as
above. F := {primes(a_i) : i ≥ 1}; a member is **minimal** if no member is a proper subset of it;
R := union of all minimal members of F. Because m ∈ E_∞ ⟹ m^N ∈ E_∞ for all N (same prime set,
still covering) and m^N ≥ D is a term for large N, we have F = {primes(m) : m ∈ E_∞}; we use this
freely. A prime q is a **sole connector** if some two terms a_i, a_j have
primes(a_i) ∩ primes(a_j) = {q}; by R1, R = {sole connectors}. **Lemma A** is: no q > P_max is a
sole connector.

---

## Step 1 (import). Reduction to Lemma A.
By the certified enumeration lemma, the terms are exactly E_∞ ∩ [D,∞) enumerated increasingly. By
enum-covering-primes Steps 3–4 (certified), if R is finite then E_∞ is exactly periodic modulo
L := ∏_{q∈R} q, and the certified periodic-set lemma gives T, L with a_{n+T} = a_n + L for every
n ≥ 1. By enum-covering-primes R1/R2 (certified), R = {sole connectors}, and R ⊆ {primes ≤ P_max}
(equivalently Lemma A) makes R finite. **So it suffices to prove Lemma A.** ∎(Step 1)

We reprove one certified equivalence we use repeatedly, for a self-contained account.

**(★) (import of R1's core).** For a term a_i with q | a_i, put T_i := primes(a_i) ∖ {q}. Then T_i
is non-covering ⟺ there is a term a_j with primes(a_i) ∩ primes(a_j) = {q}. *Proof.* Every term a_j
shares a prime with a_i (any two terms share a prime, Step 1 of enum-covering-primes). If
primes(a_j) ∩ T_i = ∅, the shared prime must be q, so primes(a_i) ∩ primes(a_j) = {q}. Conversely
such an a_j witnesses primes(a_j) ∩ T_i = ∅, so T_i is non-covering. ∎

---

## Step 2. The recruitment monovariant (bookkeeping, rigorous).
For i ≥ 1 let F_i := {primes(a_1), …, primes(a_i)} and let R_i := union of the minimal members of
F_i (minimal within F_i). Then R_1 = primes(a_1) = P ⊆ {≤ P_max}, and R = ∪_i R_i in the sense that
every minimal member of F is minimal in some F_i (a shortest occurrence). We say **prime q is
recruited at step i** if q ∈ R_i ∖ R_{i-1}. Recruitment can only happen when primes(a_i) is a *new
minimal member*: if primes(a_i) contains, as a subset, an earlier minimal member g ∈ F_{i-1}, then
adding a_i creates no new minimal member and R_i = R_{i-1}. (Removing a set that is a superset of an
existing member changes no minimal member; adding a set that contains an existing member likewise
adds no minimal member and can only *delete* minimal members that strictly contain it, shrinking R.)
Hence:

> **(Recruitment lemma).** If q is recruited at step i, then primes(a_i) is a minimal member of F_i,
> and no earlier term a_k (k<i) has primes(a_k) ⊆ primes(a_i)∖{q}. In particular T_i :=
> primes(a_i)∖{q} contains no member of F_{i-1} as a subset.

*Proof.* q ∈ R_i means q lies in some minimal member of F_i; the only new member is primes(a_i), and
if q were in an *old* minimal member then q ∈ R_{i-1}, contradiction. So primes(a_i) is a minimal
member of F_i containing q. If some earlier a_k had primes(a_k) ⊆ T_i ⊊ primes(a_i), then
primes(a_i) would not be minimal in F_i. ∎

So each recruited prime q > P_max would be carried by a **witness term a_i** whose prime-set is a
brand-new minimal member. We now extract the structure of that witness.

---

## Step 3. Structure of a large-prime witness (rigorous).
Suppose, for contradiction toward Lemma A, that some prime q > P_max is a sole connector; among all
sole-connector primes > P_max choose one recruited at the *earliest* step i, with witness term
a_i (primes(a_i) a new minimal member of F_i, q ∈ primes(a_i)).

**(3a) The small part S_i := primes(a_i) ∩ {≤ P_max} is non-empty and non-covering.** a_i shares a
prime with a_1 = D (Step 1), and that prime lies in P ⊆ {≤ P_max}; so S_i ≠ ∅. By the Recruitment
lemma no earlier term's prime-set sits inside T_i = primes(a_i)∖{q}; since S_i ⊆ T_i, in particular
S_i is not covering *on the whole sequence* — indeed by (★), because primes(a_i) is minimal, T_i is
non-covering, so there is a term a_j with primes(a_i) ∩ primes(a_j) = {q}. Thus the witness a_i has
a partner a_j sharing *only* the large prime q. (This is the sole-connector pair for q.)

**(3b) The connectivity split.** Write a_i = q^{α} · c_i with q ∤ c_i (the **cofactor** c_i > 1,
since a_i is divisible by some p ∈ P ⊆ {≤ P_max}, p ≠ q, so p | c_i). Then primes(c_i) =
primes(a_i) ∖ {q} = T_i, and S_i ⊆ primes(c_i). The pair (a_i, a_j) shares only q, so the cofactor
c_i shares no prime with a_j: primes(c_i) ∩ primes(a_j) = ∅. Symmetrically a_j = q^{β} c_j with
primes(c_j) ∩ primes(a_i) = ∅ and primes(c_j) hitting P.

So a large sole connector forces two terms a_i = q^α c_i, a_j = q^β c_j whose cofactors are
**coprime**, each cofactor hitting P (via a prime of P_max-bounded size), and q is the unique bridge.

---

## Step 4 (new). Prop C: a sole-connector term is never a multiple of a_1.
**Proposition C.** If two terms A, B satisfy primes(A) ∩ primes(B) = {q} with q ∉ P, then D ∤ A and
D ∤ B.

*Proof.* Suppose D | A. Then primes(A) ⊇ primes(D) = P. Now B is a term, so B shares a prime with D
(Step 1): some p ∈ P divides B. But p ∈ P ⊆ primes(A) and p | B, so p ∈ primes(A) ∩ primes(B) = {q},
forcing p = q. This contradicts q ∉ P. Hence D ∤ A; by symmetry D ∤ B. ∎

Applied to the witness pair (a_i, a_j) of Step 3 (here q > P_max ⟹ q ∉ P): **neither witness term
is a multiple of D.** Combined with the certified fact that *all* multiples of D are terms and gaps
are ≤ D, each witness term a_i lies strictly between two consecutive multiples of D, in an interval
(M, M+D) (M := D⌊a_i/D⌋) that contains no D-multiple in its interior; and the previous term
a_{i-1} lies in (M, a_i), so a_i is the greedy minimum of E_∞ on (a_{i-1}, a_i], with a_{i-1} > M.
(Numerically confirmed: for a_1 ∈ {15,35,77,99,105,143,231}, no sole-connector pair with the shared
prime outside P has either term a multiple of a_1.)

Prop C is the first non-trivial *positive* constraint on the witness beyond the certified
reduction: the connectivity-carrying witness is squeezed off the a_1-lattice into a length-<D window.

---

## Step 5 (new). Prop D: the crux is not set-theoretic — the greedy order is essential.
It is tempting to try to rule out a large minimal member purely from the abstract structure that F
is a family of pairwise-intersecting sets that is "covering-closed." Prop D shows this is impossible,
which both explains why round 1's four framings stalled and tells us precisely what a proof must use.

**Proposition D.** There is a finite family G of pairwise-intersecting prime-sets, closed under the
covering relation in the sense that {primes(m) : m realizes a covering set of G} has a minimal member
containing an arbitrarily large prime q — with no contradiction available from the intersection /
covering axioms alone.

*Construction.* Take small primes p_1 = 2, p_2 = 3 and any large prime q. Let the family be
G = { {p_1, q}, {p_2, q} }. Any two members intersect (in q). A prime set H is "covering for G" iff
H meets both members, i.e. (p_1 ∈ H or q ∈ H) and (p_2 ∈ H or q ∈ H). The minimal covering sets are
{q}, {p_1,p_2}. Now perturb to G' = { {p_1,q}, {p_2,q}, {p_1,p_2} } (all pairwise intersecting: the
first two meet in q, and {p_1,p_2} meets {p_1,q} in p_1 and {p_2,q} in p_2). H covering for G' iff H
meets all three; the minimal covering sets are exactly {p_1,q}, {p_2,q}, {p_1,p_2}, and **{p_1,q} is
a minimal covering set containing the arbitrarily large prime q.** Every pair among these minimal
sets intersects; the family is intersecting and covering-consistent; no axiom of "intersecting +
covering-closed" is violated. ∎

**Consequence.** The set of prime-sets of E_∞ can, as an abstract intersecting/covering family,
legitimately contain a large minimal member. Hence Lemma A is *false at the covering-set level*: it
holds only because the actual F is generated by the greedy rule, which forbids realizing families
like G'. Therefore any proof of Lemma A — including the closure of this approach — must use the
greedy minimality of the terms (the dynamics), not merely the pairwise-intersecting covering
structure. In particular, the static process-coincidence framing must also, at bottom, invoke
window-minimality; and no purely combinatorial (Helly/sunflower/covering) argument on F can succeed.
This is a genuine steering result for the field: the residual difficulty is irreducibly dynamical.

---

## Step 6. The residual, as a single greedy statement (Gap G).
By Steps 3–5 the entire problem is now reduced to the following, and Prop D guarantees it must be
proved from the greedy rule.

> **Gap G (cofactor-smoothness / greedy witness).** Let a_i be a term that is the greedy minimum of
> E_∞ on (a_{i-1}, a_i] and is a *new minimal member* of F_i (Recruitment lemma), with a_i = q^α c_i,
> q > P_max, q ∤ c_i, and a partner term a_j (primes(a_i)∩primes(a_j) = {q}). Then no such
> configuration exists: equivalently, the cofactor c_i that carries a_i's connectivity to the small
> primes cannot be forced coprime to a partner a_j while a_i is the minimal compatible integer in its
> length-<D window. Concretely: the connectivity-carrying cofactor of the minimal compatible term is
> P_max-smooth in the sense that its recruited primes are already ≤ P_max, so q never enters R.

**What is rigorously established toward Gap G (not the full statement).**
1. *The witness is off the a_1-lattice* (Prop C): a_i, a_j ∈ (M, M+D) with M a multiple of D, so
   a_i is close to a_{i-1} and bounded by the next D-multiple. This confines the witness to a short
   window, which is exactly where a greedy-minimality/smooth-number bound would live.
2. *The cofactor hits P* (Step 3b): primes(c_i) ∩ P ≠ ∅, so c_i is never a pure large-prime object;
   its small part S_i is non-empty. The failure, if any, is that S_i is non-covering, i.e. c_i's
   small primes fail to reach a_j.
3. *The obstruction is dynamical* (Prop D): the missing ingredient is a bound forcing the greedy
   minimum in a length-<D window to be built so that its cofactor's small primes already cover the
   partner class — a statement about the smallest compatible integer in a bounded window, provably
   not derivable from the covering structure alone.

**What is NOT proved (the honest gap).** We do not prove that the greedy minimum in the window
(a_{i-1}, a_{i-1}+D] cannot be a q^α c_i with c_i coprime to a partner a_j. The intended mechanism —
that among the compatible integers in a length-D window, a small-covering competitor (built from
primes ≤ P_max) sits at or below a_i and would be selected first, so the minimal choice never needs
the large prime q — is **not** made rigorous: the local window (a_{i-1}, a_i) is empty of E_∞ by
definition (greedy), so a straightforward "smaller compatible number" competitor does not exist
locally, and no non-local smooth-number density bound (Bertrand-type) was found that forces the
cofactor small. This is the same wall the round-1 framings hit, now localized to a single dynamical
statement and equipped with Prop C (lattice exclusion) and Prop D (the set-level impossibility) as
new constraints on any solution. **Do NOT** attempt to discharge it via the circular cofactor-peel
("the peeled cofactor c_i is compatible with all earlier terms" — that is a corollary of Lemma A,
not a hypothesis).

---

## Cases to cover
- Recruitment bookkeeping and (★): complete (Steps 1–2).
- Witness structure |S_i| = 1 vs ≥ 2, and q the unique large prime vs several: all reduce to the
  single coprime-cofactor configuration of Step 3b; Prop C and Prop D apply uniformly to each, so no
  further split closes the gap without Gap G. (Verified in Step 5 that even |S_i| = 1, single large
  prime, is set-theoretically consistent, so no case is killable abstractly.)
- Gap G: OPEN, dynamical.

## Promotable lemmas
- **Prop C (sole-connector terms avoid the a_1-lattice).** If two terms share exactly one prime q
  with q ∉ primes(a_1), then neither term is a multiple of a_1. Proved in full (Step 4);
  elementary, reusable by every approach that reasons about sole-connector pairs. Numerically
  confirmed on a_1 ∈ {15,35,77,99,105,143,231}.
- **Prop D (set-level impossibility / dynamical barrier).** There is an abstract intersecting,
  covering-consistent prime-family with a large prime as a minimal covering member; hence Lemma A
  cannot be proved from the covering/intersection structure of F alone and any proof must use the
  greedy order. Proved in full (Step 5). Reusable as a *pruning* result: it certifies that purely
  combinatorial (Helly/sunflower/covering) attacks on the crux are dead, focusing the field on
  window-minimality — directly supports the reviewer's shared-wall analysis.
