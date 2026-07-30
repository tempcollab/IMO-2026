## Status
partial

## Approaches tried
- **bad-residue-witness-index** (round 5, NEW) — Residue-class reformulation of badness with a fixed
  per-class witness-index-set W(r). Rigorously built Steps 1–4 (residue-level badness; W(r)-large-link;
  W(r) points to bad terms) from certified facts. **NEW rigorous result:** proved that the theorem follows
  from the *finite-witness* hypothesis **(FIN-W)** — *for every term m, the set of terms small-disjoint
  from m is finite* — via a **direct** periodicity of E_∞ modulo an enlarged period M = L_0·∏Q_rel
  (relevant large primes), WITHOUT going through (CSP). This strictly weakens the standing crux: (CSP)
  ⟹ (FIN-W) ⟹ theorem, and (FIN-W) is sufficient. Honest GAP: (FIN-W) itself, i.e. the infinite-witness
  branch of Step 5 — the pigeonhole reduces it to a clean "star" configuration (one term m small-disjoint
  from an infinite family of terms all divisible by one fixed large prime p, in a single residue class),
  but the final contradiction there is not closed. Reviewer: partial. Distinct framing confirmed
  (non-symmetric, residue-level; not covering/Helly, not global capacity, not window-CRT).

## Current best

The whole problem is reduced, with full rigor, to a single clean finiteness statement that is strictly
weaker than the standing crux (CSP), and the reduction is proved end to end. Below, everything through the
Reduction Lemma is gap-free; the sole remaining gap is (FIN-W)'s infinite-witness branch, isolated as
precisely as possible.

### Notation and imported facts

Greedy sequence a_1 < a_2 < … of integers > 1. Let
E_∞ := { m ∈ ℤ_{>1} : gcd(m, a_i) > 1 for every i }.
P := primes(a_1); P_max := max P; a prime is **small** if ≤ P_max, **large** if > P_max.
L_0 := ∏_{p ≤ P_max} p (squarefree). For m > 1, S(m) := primes(m) ∩ [2, P_max] (the small part).
For a term a_i, Q_i := primes(a_i) ∩ (P_max, ∞) (its large primes).

Imported, certified (used by reference, not re-proved):
- **ENUM** (`enumeration-of-E-infinity.md`): the sequence equals the increasing enumeration of
  E_∞ ∩ [a_1, ∞); in particular the terms are exactly E_∞ ∩ [a_1, ∞).
- **PER** (`periodic-set-enumeration.md`): if E ⊆ ℤ is nonempty and tail-periodic from a with period
  L > 0 (∀x ≥ a: x ∈ E ⟺ x+L ∈ E) and E ∩ [a,∞) is infinite, then its increasing enumeration
  b_1 < b_2 < … satisfies b_{n+T} = b_n + L with T = #(E ∩ [a, a+L)) ≥ 1.
- **F1** (in `csp-implies-theorem.md`): every two terms share a prime; every term is divisible by a prime
  of P, so S(t) ⊇ (S(t) ∩ P) ≠ ∅ for every term t.
- **GPC** (`generalized-sole-connector-off-lattice.md`): if two terms A, B share no small prime
  (S(A) ∩ S(B) = ∅) then a_1 ∤ A and a_1 ∤ B.
- Certified fact "S(m) depends only on m mod L_0" (`csp-implies-theorem.md` Step 1a): for a prime
  p ≤ P_max, p | m depends only on m mod p, hence (CRT) on m mod L_0; so S(m), and every property of
  S(m), depends only on m mod L_0.
- Certified "every multiple of a_1 is a term with S(·) ⊇ P" (used in `bad-partner-and-ascent.md`).

**Definitions.** A term m is **good** iff S(m) meets every color, i.e. primes(a_i) ∩ S(m) ≠ ∅ for every i;
otherwise **bad** (some term B has primes(B) ∩ S(m) = ∅; call such B a *witness* for m). For r ∈ ℤ/L_0ℤ
let S(r) denote S(m) for any m ≡ r (well-defined by the certified fact). Call r **covering** iff S(r)
meets every color; **non-covering** otherwise. Put R_bad := { r ∈ ℤ/L_0ℤ : S(r) non-covering } and, for
r ∈ R_bad, the **fixed witness-index-set**
W(r) := { i : primes(a_i) ∩ S(r) = ∅ }  (nonempty, since S(r) is non-covering).

### Step 1 — Badness is a residue property (gap-free)

Whether a term m is good or bad is a property of S(m) and the fixed color family {primes(a_i)}, and S(m)
depends only on m mod L_0. Hence m is bad ⟺ (m mod L_0) ∈ R_bad, and W(m mod L_0) is exactly the set of
witness indices of m. Since R_bad ⊆ ℤ/L_0ℤ and, more sharply, each r ∈ R_bad has S(r) ⊆ {primes ≤ P_max},
|R_bad| is finite (≤ L_0). (This is `csp-implies-theorem.md` Step 1a plus the definitions.)

### Step 2 — W(r)-large-link (gap-free)

Let r ∈ R_bad and let m be any term with m ≡ r (mod L_0), so S(m) = S(r). Fix i ∈ W(r). Then
primes(a_i) ∩ S(m) = primes(a_i) ∩ S(r) = ∅, so a_i and m share no small prime. By F1, gcd(m, a_i) > 1,
so they share at least one prime, necessarily **large**: m is divisible by some prime of Q_i. Thus every
term m ≡ r shares a large prime with a_i for every i ∈ W(r). (Verbatim the outline-reviewer's validated
Step 3.)

### Step 3 — W(r) points to bad terms (gap-free)

Keep r ∈ R_bad inhabited by a term m, and i ∈ W(r). By Step 2, m and a_i share only large primes, so
primes(m) ∩ S(a_i) = ∅ (a common small prime would lie in S(m) ∩ S(a_i) ⊆ primes(a_i) ∩ S(m) = ∅).
Hence m is a witness for a_i, so a_i is **bad**. Therefore every witness index i ∈ W(r) (for an inhabited
bad class r) points to a bad term a_i. (The outline-reviewer's validated Step 4; mirrors
`bad-partner-and-ascent.md`.)

### Step 4 — Class membership of E_∞ (gap-free)

Fix r ∈ ℤ/L_0ℤ and m > 1 with m ≡ r. Then m ∈ E_∞ ⟺ gcd(m, a_i) > 1 ∀i.
- If r is **covering** (r ∉ R_bad): for every i, primes(a_i) ∩ S(r) ≠ ∅; since S(r) = S(m) ⊆ primes(m),
  gcd(m, a_i) > 1 for all i, so m ∈ E_∞. Thus every element > 1 of a covering class lies in E_∞.
- If r ∈ R_bad: for i ∉ W(r), primes(a_i) ∩ S(r) ≠ ∅ gives gcd(m, a_i) > 1 automatically; for i ∈ W(r),
  a_i and m share no small prime, so gcd(m, a_i) > 1 ⟺ some q ∈ Q_i divides m. Hence
  m ∈ E_∞ ⟺ for every i ∈ W(r), ∃ q ∈ Q_i with q | m.  (★)

So within a bad class r, membership in E_∞ is governed **only** by divisibility by primes of
Q(r) := ⋃_{i ∈ W(r)} Q_i (a set of large primes), together with the residue mod L_0.

### Reduction Lemma (gap-free) — (FIN-W) ⟹ theorem

**(FIN-W):** for every term m, W(m mod L_0) is finite. Equivalently: for every term m only finitely many
terms are small-disjoint from m.

**Claim.** (FIN-W) implies there exist T, L with a_{n+T} = a_n + L for every n.

**Proof.** Assume (FIN-W). Let R'_bad := { r ∈ R_bad : E_∞ meets class r }. For each r ∈ R'_bad pick a
term m_r ≡ r; by Step 1, W(r) = W(m_r mod L_0) is finite (FIN-W), and each Q_i (i ∈ W(r)) is finite, so
Q(r) is finite. Since R'_bad ⊆ R_bad is finite (Step 1), the set of **relevant large primes**
Q_rel := ⋃_{r ∈ R'_bad} Q(r) is a finite union of finite sets, hence **finite**.

Put M := L_0 · ∏_{q ∈ Q_rel} q (squarefree; all these primes are distinct — L_0's are ≤ P_max, Q_rel's
are > P_max). I claim membership in E_∞ is determined by residue mod M. Fix m > 1 and let r = m mod L_0.
- If r covering: m ∈ E_∞ (Step 4), a condition depending only on r = m mod L_0, a fortiori on m mod M.
- If r ∈ R_bad and E_∞ meets class r (r ∈ R'_bad): by (★), m ∈ E_∞ ⟺ for every i ∈ W(r) some q ∈ Q_i
  divides m. Each such q lies in Q_rel | M, so "q | m" depends only on m mod q, hence on m mod M; and W(r),
  Q_i depend only on r = m mod L_0 | M. So m ∈ E_∞ is determined by m mod M.
- If r ∈ R_bad and E_∞ does **not** meet class r: then E_∞ ∩ (class r) = ∅. For such m, m ∉ E_∞. This is
  the constant "false", trivially determined by m mod M (indeed by m mod L_0, which fixes the class).

  [Consistency check that "E_∞ misses class r" is a legitimate mod-L_0, hence mod-M, statement: "class r
  is met by E_∞" means ∃ m > 1, m ≡ r, m ∈ E_∞. This is a fixed truth value attached to the residue r;
  when it is false, *every* m ≡ r has m ∉ E_∞. So on class r the predicate m ∈ E_∞ is constantly false,
  a function of m mod L_0.]

In all three cases m ∈ E_∞ is a function of m mod M. Hence for every integer x ≥ a_1, x ∈ E_∞ ⟺
x + M ∈ E_∞ (same residue mod M, both > 1): E_∞ is tail-periodic from a_1 with period M. Moreover
E_∞ ∩ [a_1, ∞) is infinite (it contains every multiple k·a_1, k ≥ 1, each a term). Apply PER to
(E := E_∞, a := a_1, L := M): its increasing enumeration b_1 < b_2 < … satisfies b_{n+T} = b_n + M with
T = #(E_∞ ∩ [a_1, a_1 + M)) ≥ 1. By ENUM that enumeration is exactly a_1, a_2, …, so a_{n+T} = a_n + M
for every n. Take L = M and this T. ∎ (Reduction Lemma)

**Consequence.** (CSP) — no bad term — is the special case R'_bad = ∅ (whence Q_rel = ∅, M = L_0,
recovering `csp-implies-theorem.md`). But (FIN-W) is strictly weaker than (CSP) and already suffices:
the theorem holds as soon as **each term is small-disjoint from only finitely many terms**. This is the
sharpened crux this approach delivers.

### Step 5 — the remaining gap: proving (FIN-W)

We must rule out the failure of (FIN-W). Suppose, for contradiction, some term m has W(r) infinite,
r := m mod L_0 ∈ R_bad, s_0 := S(m) = S(r) ≠ ∅ (nonempty by F1).

**Pigeonhole to a star configuration (gap-free part of Step 5).**
The infinitely many terms { a_i : i ∈ W(r) } are, by Step 2, each divisible by a large prime shared with
m. The single term m has finitely many prime factors, so by pigeonhole one **fixed large prime p | m**
divides infinitely many of them. Pigeonholing those further into one residue class mod L_0 (finitely many
classes, Step 1) yields an infinite family of terms
    T_p := { t_1 < t_2 < … } , all t_j ≡ r* (mod L_0), all p | t_j,
with S(t_j) = S(r*) =: s_1 for all j, and s_1 ∩ s_0 = ∅ (each t_j is small-disjoint from m, Step 2/3).
By GPC (each t_j small-disjoint from m), a_1 ∤ t_j and a_1 ∤ m: all off-lattice. By Step 3 every t_j is
bad, and m witnesses r* bad so r* ∈ R_bad. By CRT (gcd(p, L_0) = 1) the t_j lie in one arithmetic
progression t_j ≡ c (mod pL_0). So we have:
  • one "hub" term m (bad, small-part s_0), and
  • an infinite "star" family T_p of bad off-lattice terms, all divisible by the single large prime p,
    all in one residue class mod L_0 (so pairwise small-connected via the fixed nonempty s_1), each
    small-disjoint from m, all congruent mod pL_0.

**GAP (honest, unclosed).** A contradiction from this star configuration is NOT established. The reviewer's
and outliner's warning applies exactly here: "a single large prime dividing infinitely many terms in a
fixed residue class" is not, by itself, contradictory — a periodic E_∞ genuinely contains infinitely many
multiples of any prime. The extra structure available and unused is:
  (i)  every t_j is off the a_1-lattice (GPC), strictly interior to a window (k a_1, (k+1)a_1) whose
       endpoints are good on-lattice terms;
  (ii) the t_j all share the nonempty small part s_1 with each other but are small-disjoint from the hub m;
  (iii) m and every t_j are bad, so each t_j again spawns (Steps 2–3) its own witness structure.
No argument combining (i)–(iii) into a contradiction has been found; the dead routes remain barred (pure
covering/Helly — Prop D barrier; global Σ_{p>P_max} 1/p² capacity — bounds only a positive fraction; a
length-a_1 window holding a full residue system mod L_0 — false since a_1 < L_0). This is precisely the
field's standing wall, here relocated to: *"the star configuration above cannot occur."* Marked as the
open gap; NOT asserted as proved.

**Precise statement of what remains.** The theorem is proved (Reduction Lemma) once the following is
established:

  (FIN-W)  For every term m, only finitely many terms are small-disjoint from m.

Equivalently, the star configuration (an infinite family of terms all divisible by one fixed large prime
p, all small-disjoint from a fixed term m) does not exist.

This is a strictly weaker sufficient condition than the previously-standing crux (CSP), and its
per-term/per-large-prime, off-lattice, single-residue-class formulation is the cleanest isolation of the
crux the population has produced.

## Promotable lemmas

- **Finite-witness periodicity (FIN-W ⟹ theorem).** Statement: with notation above, if for every term m
  the set of terms small-disjoint from m is finite, then E_∞ is tail-periodic from a_1 with period
  M = L_0 · ∏_{q ∈ Q_rel} q (Q_rel = the finite set of large primes of witness colors of E_∞-inhabited bad
  classes), and hence a_{n+T} = a_n + M for every n with T = #(E_∞ ∩ [a_1, a_1 + M)). Proof: the Reduction
  Lemma above (gap-free; imports ENUM, PER, F1, GPC, and the certified "S(m) depends only on m mod L_0").
  This generalizes `csp-implies-theorem.md` (the R'_bad = ∅ / M = L_0 case) and reduces the whole problem
  to (FIN-W), a strictly weaker condition than (CSP). Recommended for certification.
- Steps 1–3 (residue-level badness; W(r)-large-link; W(r) points to bad terms) are short corollaries of
  already-certified facts and are folded into the lemma above; no separate certification needed.
