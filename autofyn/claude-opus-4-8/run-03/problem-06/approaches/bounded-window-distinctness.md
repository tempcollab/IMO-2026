# Approach: bounded-window-distinctness

## Status
partial

## Approaches tried
- **bounded-window-distinctness** (round 9, RE-ATTACK of step 4 abstractly, per reviewer request). The
  outline-reviewer asked that step 4 (window localization) be argued abstractly from Window Purity + linear
  growth rather than numerically. I carried this out and it **confirms the gap is not closable, and moreover
  pins down WHY as a crisp theorem, not a heuristic**: I prove the exact contrapositive **(R2′) below** —
  *if the new-large-prime witnesses lay in ANY bounded value-band, the pool Q(r_0) would already be finite*
  — so the infinite-pool case ¬(FIN-Q) is EXACTLY the case with unbounded witnesses, i.e. the one case in
  which distinctness-by-difference is vacuous. Hence the mechanism kills only the empty sub-case. This is a
  rigorous *impossibility* argument for the distinctness closer (not merely "unverified"), and it is exactly
  the abstract form the reviewer requested. No new closing mechanism found; Status stays **partial**, route
  remains **dead as a closer** (RETHINK-worthy). The Distinctness-by-Difference lemma (Step 3) is re-confirmed
  gap-free and promotable. Net: the requested abstract argument was executed and it *decides* step 4 in the
  negative, sharpening Proposition R with the crisp contrapositive (R2′).
- **bounded-window-distinctness** (round 8, NEW — value-difference distinctness engine, transplant of
  aimo-0415/aimo-0447). Built the full skeleton. Steps 1,2,3,5 are gap-free (imported certified lemmas +
  one genuinely new, true, reusable LOCAL lemma proved here in full: **Distinctness-by-Difference**). The
  honest hard step 4 (cluster the infinite connector pool into a bounded value-window) was attacked head-on
  and found to be **structurally unachievable within this framing** — the distinctness engine yields only a
  LOCAL bound D(N) ≤ (#terms in the window) = O(N) on the number of distinct large primes appearing in a
  value-window of length N, which grows with N and gives NO global finiteness; and ¬(FIN-Q) is a consistent
  configuration for any single realizer m (the "extra irrelevant primes" escape). So this route is **DEAD as
  a closer** — it collapses to the same wall as the proven-dead global Σ1/p² count and Prop D. This is
  recorded rigorously below (Proposition R). SALVAGE: the Distinctness-by-Difference lemma is true, cleanly
  proved, and reusable (promotable). Route verdict: RETHINK-worthy (no closing mechanism for the builder to
  complete); the salvage lemma is the value-add.

## Current best

The whole problem is (imported, certified) reduced to refuting **¬(FIN-Q)**. Within this route the furthest
correct progress is:

1. Gap-free steps 1,2,3,5 of the value-difference skeleton (below), including a new true LOCAL lemma.
2. A rigorous **negative result (Proposition R)**: the distinctness engine cannot close step 4; the clustering
   the outline required does not hold (the new-large-prime witnesses genuinely spread over unbounded values),
   so the mechanism gives no global bound on the connector pool.

The open gap (step 4, window localization) is not merely unclosed — it is shown to be **unachievable by the
distinctness mechanism**, and (round 9) the abstract argument the reviewer requested has been executed and
**decides step 4 in the negative** via the crisp contrapositive **(R2′)**: confining the new-prime witnesses
to a bounded value-band is *equivalent* to Q(r_0) being finite, i.e. to the negation of ¬(FIN-Q) itself. So
distinctness can only bite where its own conclusion is already assumed. The correct honest reading: this is a
proven-dead route as a closer, with a salvaged reusable lemma and a now-sharpened impossibility argument. It should not be re-fielded as a live solve route; the surviving crux is still ¬(FIN-Q), to be
attacked by a mechanism that produces a *lower value pressure* (the covering-small-part-descent lane), not by a
value-difference count.

### Setup and imported certified lemmas (used verbatim, NOT re-proved)

Notation (as in the certified lemma cache): the greedy sequence a_1 < a_2 < …; E_∞ = {m>1 : gcd(m,a_i)>1 ∀i};
by **(ENUM)** (`lemmas/enumeration-of-E-infinity.md`) the sequence is the increasing enumeration of
E_∞ ∩ [a_1,∞) — a "term" means an element of E_∞ ∩ [a_1,∞). P := primes(a_1); P_max := max P; a prime is
**small** if ≤ P_max, **large** if > P_max; S(m) := primes(m) ∩ [2,P_max]; for a term a_i, Q_i :=
primes(a_i) ∩ (P_max,∞); L_0 := ∏_{p≤P_max} p. A prime set is **covering** iff it meets primes(a_i) for every
i. A residue class r mod L_0 is **bad** iff S(r) is non-covering; R'_bad := {bad classes that E_∞ meets}. For
r ∈ R'_bad, W(r) := {i : primes(a_i) ∩ S(r) = ∅} (the colors S(r) misses) and the **connector pool**
Q(r) := ⋃_{i∈W(r)} Q_i.

Imported certified results:
- **(FIN-Q) ⟹ theorem** (`lemmas/finite-connector-pool-periodicity.md`): if every r ∈ R'_bad has Q(r)
  finite, then E_∞ is tail-periodic with period M = L_0·∏_{q∈Q_rel} q, giving the conclusion. Hence the
  theorem follows once **¬(FIN-Q) is refuted**: ¬(FIN-Q) asserts some E_∞-inhabited bad class r_0 has Q(r_0)
  infinite.
- **Membership dichotomy (★)** (same file): for r ∈ R'_bad and m ≡ r (mod L_0), m ∈ E_∞ ⟺ for every
  i ∈ W(r) some q ∈ Q_i divides m.
- **Window Purity** (`lemmas/window-purity.md`): for every integer x with a_n < x < a_{n+1}, x ∉ E_∞;
  primes(x) is non-covering.
- **Local Hub-Cover** (`lemmas/local-hub-cover.md`): for a bad hub h, W(h) ⊆ ⋃_{q∈Q(h)}{B : q|B} with Q(h)
  finite; if W(h) infinite, one q ∈ Q(h) divides infinitely many members of W(h).
- **Term density C1–C3** (`lemmas/term-density-and-prime-capacity.md`): N(X)=Θ(X); Σ_{p>P_max}1/p² < 0.2023.
- **GPC** (`lemmas/generalized-sole-connector-off-lattice.md`) and **floor-tightness**
  (`lemmas/minimal-bad-term-floor-tightness.md`): as cached.

### The value-difference skeleton

**Step 1 (reduce to ¬(FIN-Q)).** Gap-free by the imported (FIN-Q)⟹theorem. Assume for contradiction ¬(FIN-Q):
fix an E_∞-inhabited bad class r_0 with Q(r_0) = ⋃_{i∈W(r_0)} Q_i infinite, i.e. infinitely many *distinct*
large primes occur across the factorizations of the witness terms {a_i : i ∈ W(r_0)}.

**Step 2 (membership dichotomy).** Gap-free by (★). Because r_0 ∈ R'_bad, there is m ∈ E_∞ with m ≡ r_0
(mod L_0), and for every i ∈ W(r_0) some q ∈ Q_i divides m.

**Step 3 (Distinctness-by-Difference — NEW, proved in full below).**

> **Lemma (Distinctness-by-Difference, local).** Let N ≥ 1 and let I ⊆ ℤ be any set of integers all lying in
> a value-window of length N (i.e. max I − min I < N). If a prime q > N divides two distinct elements
> A, B ∈ I, then q divides A − B; but 0 < |A − B| < N < q, so q ∤ (A−B) unless A−B = 0 — contradiction.
> Hence **a prime q > N divides at most one element of I.** Consequently the number of distinct primes q > N
> that divide at least one element of I is at most |I|.

*Proof.* q | A and q | B ⟹ q | (A − B). If A ≠ B then A − B is a nonzero integer with |A − B| ≤ max I − min I
< N < q, so |A − B| < q and A − B ≠ 0 forces q ∤ (A − B), contradicting q | (A − B). Thus q divides at most
one element. For the count: assign to each large prime q > N the unique element of I it divides; this is an
injection from {such primes} into I, so there are at most |I| of them. ∎

This is a VALUE-level fact (about differences), verified numerically (window length 30 at x=1000: every large
prime divides exactly one window member, and #distinct large primes = 20 ≤ 30 = |I|).

**Step 4 (window localization — the gap; SHOWN UNACHIEVABLE, Proposition R).** To turn Step 3 into a
contradiction with "Q(r_0) infinite," one must confine the witnesses i ∈ W(r_0) that contribute *new* distinct
large primes into a single bounded value-window of length N; then Step 3 caps the distinct large primes usable
there at ≤ N, contradicting the infinite pool. **This confinement does not hold.** See Proposition R.

**Step 5 (closure).** Would be gap-free from Step 4 (bounded window + Step 3 ⟹ finite pool ⟹ contradiction),
but Step 4 fails.

### Proposition R (negative result): the distinctness engine cannot close ¬(FIN-Q)

We prove three facts that together establish that the value-difference mechanism yields no global finiteness,
so step 4 cannot be completed within this framing. This is not a claim that the theorem is false — only that
THIS mechanism is inadequate, exactly as the dispatch asked us to determine.

**(R1) The distinctness bound is purely local and grows with the window.** By Step 3, in a value-window of
length N the number of distinct large primes (q > N) dividing some window-member is at most the number of
integers (a fortiori terms) in the window. A window of length N contains at most N integers, and (by C1)
Θ(N/a_1) terms. Thus the distinct-large-prime count per window is D(N) = O(N) — it *increases without bound*
as the window lengthens. So distinctness never forces the count to be finite over the whole (unbounded)
sequence; it only says "few large primes per bounded window," which is consistent with infinitely many large
primes overall (one every ≥ q apart in value, for each q). *This is confirmed by the sanity computation:
D(30) = 20 and grows with the window.*

**(R2) The new-large-prime witnesses are not confined to any bounded value-band.** Suppose the pool Q(r_0) is
infinite; enumerate distinct new large primes q_1, q_2, q_3, … with q_k dividing a witness a_{i_k},
i_k ∈ W(r_0). The witness terms {a_i : i ∈ W(r_0)} form an infinite subset of the strictly increasing sequence
(if W(r_0) were finite, Q(r_0) = ⋃_{i∈W(r_0)} Q_i would be a finite union of finite sets, hence finite,
contradicting ¬(FIN-Q); so W(r_0) is infinite). Since a_i → ∞, the values a_{i_k} are unbounded. A large prime
q_k satisfies q_k ≤ a_{i_k}, and there is no lower bound forcing q_k or a_{i_k} into a fixed band. Hence the
new-prime contributors genuinely spread over arbitrarily large values. No fact on hand bounds this spread:
the bounded-gap fact a_{n+1} − a_n ≤ a_1 controls only the *density* of terms, not the range; Window Purity
constrains only gap interiors; linear growth a_n ≍ n·a_1 pushes the witnesses *out*, not into a band. There is
therefore no bounded value-window containing the new-prime contributors, and Step 4's premise is false.

**(R2′) [ROUND 9, the abstract argument the reviewer requested] The infinite-pool case is EXACTLY the
unbounded-witness case; distinctness is vacuous precisely there.** We prove the crisp contrapositive of
Step 4's premise, using only the imported certified facts (no numerics):

> **Claim.** If the set of *new-prime-contributing witnesses* is confined to a bounded value-band, then the
> pool Q(r_0) is finite. Equivalently: Q(r_0) infinite ⟹ these witnesses are unbounded in value.

*Proof.* By definition Q(r_0) = ⋃_{i∈W(r_0)} Q_i, where Q_i = primes(a_i) ∩ (P_max,∞) is a finite set (a term
a_i has finitely many prime factors). Suppose the witnesses that contribute *any* large prime — i.e. the
index set W' := {i ∈ W(r_0) : Q_i ≠ ∅} — all satisfy a_i < V for a fixed bound V. Each such a_i is a distinct
integer in the finite interval [a_1, V), so |{a_i : i ∈ W'}| < V, i.e. W' indexes at most V − a_1 distinct
term-values, hence finitely many terms. Then Q(r_0) = ⋃_{i∈W'} Q_i is a finite union of finite sets, so
Q(r_0) is finite. Contrapositive: Q(r_0) infinite forces the large-prime-carrying witnesses to take
arbitrarily large values a_i. ∎

This is decisive for the mechanism. Distinctness-by-Difference (Step 3) only constrains primes q > N inside a
value-window of length N; a prime q ∈ Q(r_0) divides a witness a_i whose value is unbounded, and q itself may
be as large as a_i, so **no fixed window of finite length N contains more than finitely many of the
new-prime-carrying witnesses** — indeed, by (R2′), a window of length N contains at most N such witnesses and
therefore ≤ N of the pool's primes, exactly the local O(N) bound of (R1), never a global finiteness. Thus the
premise Step 4 needs — "confine the new-prime contributors to one bounded value-window" — is not merely
unverified; by (R2′) it is *equivalent to Q(r_0) being finite*, i.e. to the negation of the very hypothesis
¬(FIN-Q) we are trying to refute. The distinctness engine can only bite where its conclusion is already
assumed away. **This is an impossibility theorem for the distinctness closer, argued abstractly from term
finiteness + the definition of the pool, with no appeal to numerics** (as the reviewer required). It also
respects the reviewer's warning not to conflate same-CLASS with same-VALUE-WINDOW: (R2′) is stated purely in
terms of value bands a_i < V, never residue classes mod M.

**(R3) ¬(FIN-Q) is a consistent configuration for a single realizer, so it cannot be contradicted term-by-term.**
Fix the realizer m from Step 2. By (★), for every i ∈ W(r_0) the set Q_i meets the FINITE set
F := primes(m) ∩ (P_max,∞) (some large prime of Q_i divides m, and it lies in F). Thus every witness shares one
of m's finitely many large primes. But Q_i may carry *additional* large primes ∉ F, and these additional primes
— spread across the infinitely many witnesses — make Q(r_0) = ⋃ Q_i infinite while every single membership
constraint on m is satisfied by a prime in the finite set F. Concretely, the condition defining
E_∞ ∩ (class r_0), namely "∀ i ∈ W(r_0), Q_i ∩ primes(m) ≠ ∅," is an infinite intersection of periodic
constraints (constraint i is periodic mod ∏Q_i) that need NOT reduce to a finite sub-intersection; the pool of
*potentially relevant* large primes is genuinely all of Q(r_0). This is precisely the "extra irrelevant primes
in Q_i" escape that the foreign-explorer scan identified as sinking the finite-fiber and sunflower routes into
Prop D. The distinctness engine (which only compares *values within a window*) never touches these extra primes,
because they sit on witnesses at unbounded, pairwise-far-apart values.

**Conclusion of Proposition R.** By (R2) and its sharpened round-9 contrapositive (R2′) there is no bounded
window to which Step 4 could apply — confinement of the new-prime witnesses is *equivalent* to Q(r_0) being
finite — and by (R1)
even inside any window distinctness caps the count only at O(N), never at a finite global number; by (R3) the
infinite pool is a consistent set-configuration under the single available realizer m. Therefore the
value-difference distinctness mechanism cannot refute ¬(FIN-Q). The route is **dead as a closer**, collapsing
to the same wall (unbounded distinct primes spread over unbounded values) as the proven-dead global Σ1/p² count
and the Prop D barrier. ∎ (of the negative result)

### Honest verdict

- **Proved (correct, reusable):** the Distinctness-by-Difference local lemma (Step 3), and the gap-free
  imported reduction to ¬(FIN-Q) (Step 1).
- **Proved (negative):** Proposition R — the distinctness mechanism cannot close step 4; the clustering the
  outline hoped for does not hold (it is not circular — it is simply false, because the witnesses genuinely
  spread to unbounded values). This is a valuable pruning: it removes value-difference counting from the live
  toolset for ¬(FIN-Q), for the same structural reason as the earlier dead counting/Helly routes.
- **NOT proved / not achievable here:** the whole theorem via this route. Status is `partial`: a true new
  lemma and a rigorous negative result, but no closing of the crux. The route should be marked RETHINK (no
  closing mechanism remains for a builder to complete); the surviving crux ¬(FIN-Q) belongs to a
  value-*pressure* mechanism (covering-small-part-descent), not a value-*difference* count.

## Promotable lemmas

- **Distinctness-by-Difference (local).** *Statement:* For any set I of integers contained in a value-window
  of length N (max I − min I < N) and any prime q > N, q divides at most one element of I; consequently the
  number of distinct primes exceeding N that divide some element of I is at most |I|. *Proof:* fully given
  above (Step 3) — q | A, q | B ⟹ q | (A−B), but 0 < |A−B| < N < q forces A = B. Elementary, self-contained,
  reusable. (Numerically verified: window length 30, multiplicity 1 for every large prime, count 20 ≤ 30.)

- **Route-inadequacy note (Proposition R), for the reviewer to record as a dead-end certification, NOT a
  math lemma:** the value-difference distinctness engine cannot refute ¬(FIN-Q), because (R1) its bound is
  local and O(N), (R2) the new-large-prime witnesses spread to unbounded values (no bounded band exists), and
  (R3) the infinite pool is consistent for a single realizer via the extra-irrelevant-primes escape. Bars
  re-fielding value-difference counting against ¬(FIN-Q).
