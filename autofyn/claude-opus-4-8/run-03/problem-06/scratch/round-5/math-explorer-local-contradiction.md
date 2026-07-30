## imo-2026-06 (lens: sub-gap 6b — localized contradiction from an assumed infinite off-lattice bad-term chain, WITHOUT global Σ1/p² capacity counting)

### Setup recap (given, not re-derived)
Assume (toward contradiction) an infinite strictly-ascending chain of "bad" terms m_0<m_1<m_2<…
(bad = small part S(m):=primes(m)∩[2,P_max] fails to meet primes(B) for some term B), each pinned
strictly inside an open window (k·a_1,(k+1)·a_1) (length <a_1) by certified GPC
(`lemmas/generalized-sole-connector-off-lattice.md`), each linked to a witness sharing only large
primes (>P_max), and each has a good a_1-multiple within distance <a_1 above it
(`approaches/covering-small-part-descent.md` Steps 3–5, `lemmas/bad-partner-and-ascent.md`).

### Distinct openings (localized mechanisms tried/considered, none closed)

1. **Finite-signature pigeonhole (most promising).** For each integer m, S(m) ⊆ Q :=
   {primes ≤ P_max}, a FIXED finite set of size π(P_max). So S(m) ranges over at most 2^|Q|
   possible subsets, independent of m. Given the assumed infinite chain, pigeonhole (not density!)
   forces some fixed non-covering signature s* ⊆ Q to recur for infinitely many chain terms
   m_{i_1}<m_{i_2}<…, ALL with S(m_{i_j})=s*. This is a genuinely local/finite-alphabet argument —
   no asymptotic density needed, works for an arbitrarily sparse infinite subsequence. It mirrors
   the crux-corpus template in aimo-0016 (see below): "a windowed/indexed sequence with a bounded
   value-alphabet must repeat a value infinitely often; iterate/upgrade the repeat into structure."
   **Where it stalls:** two terms sharing the SAME signature s* also share every prime of s*
   (s*≠∅ by F1, so they share a SMALL prime) — this does NOT by itself contradict anything (badness
   is about missing some OTHER witness B, not about the pair m_{i_j},m_{i_k} directly). Also: the
   set B_{s*}:={m : S(m)=s*} is itself periodic mod L_0=∏_{p≤P_max}p (an algebraic/local fact, via
   Step 1a of covering-small-part-descent — CRT/residue periodicity, NOT a density claim), hence has
   bounded gaps ≤ L_0 between consecutive representatives, and EVERY integer in B_{s*} (not just the
   sampled bad terms) is a "non-covering-signature" integer. This gives a bounded-gap recurring
   pattern to work with, but connecting "B_{s*} is dense mod L_0" to an actual contradiction on
   TERMS (elements of E_∞, not just integers with the right residue) is the open step — being in
   B_{s*} doesn't make an integer a term, and I did not find a way to force a term-level conflict
   from this alone. Flag as the strongest surviving lever for next round, not a closed argument.

2. **Window-vs-modulus size caveat (a REAL obstruction to any window-based pigeonhole).**
   `reduced-process-identity.md` (G3, lines ~225–234) already proves generic CRT/pigeonhole
   window-counting fails on the *empty-window/smaller-competitor* route because the window
   (a_n,a_{n+1}) can be shorter than the CRT modulus L_0. I confirmed this numerically-flavored
   fact analytically: **a_1 can be either smaller or larger than L_0** (e.g. a_1 = large prime p ⇒
   L_0 = primorial up to p ≫ a_1; a_1 = 2·3·5·7=210 ⇒ L_0=210=a_1; a_1=12 ⇒ L_0=6<a_1). So any
   argument that needs "a window of length a_1 contains a full residue system mod L_0" is FALSE in
   general and must be discarded — this rules out the naive form of idea 1 combined with the a_1
   window bound. Any localized pigeonhole must either (a) not require a_1 ≥ L_0, or (b) split into
   cases on the relative size of a_1 vs L_0.

3. **"No good integer strictly between consecutive terms" — related to, but distinct from, the
   dead G3 route.** Greedy minimality (a_{n+1} = smallest compatible integer > a_n) implies the open
   interval (a_n,a_{n+1}) contains no element of E_n at all (already proven, G3). In particular it
   contains no GOOD integer (S(x)⊇ some covering set), since a good integer is automatically
   compatible with every predecessor (small part alone covers). This is the *same* fact as G3's
   "empty window," already flagged DEAD for the smaller-competitor route (memory: "do not retry
   competitor/minimality-contradiction arguments on (SL_n)"). I re-derived it independently via
   "good ⇒ compatible with everything" rather than pure minimality, but it is the identical
   statement — **do not resurrect this as a new mechanism; it is the same dead G3 fact under a
   different derivation.**

4. **Step-size / linking-prime persistence dichotomy (already recorded, not closed).** Consecutive
   chain terms differ by ≥ the shared large prime q_j > P_max (already noted in
   `covering-small-part-descent.md` Step 6→7 "Partial progress" item 1). Either one large prime q
   persists as the link for infinitely many chain steps, or the linking primes must change
   infinitely often. Neither branch is closed locally: a fixed q linking infinitely many bad terms
   is not yet contradictory (off-lattice q-multiples with a small prime present are legitimate
   terms), and changing primes gives no bound without counting. **This is a genuine open branch,
   not yet a dead end**, and might combine with idea 1 (pigeonhole the *signature* AND the *linking
   prime* jointly — still finite-alphabet if one bounds the number of large primes appearing "low"
   in the sequence, though I did not find such a bound).

5. **Bounded-band occupancy is NOT itself a contradiction.** Multiple bad terms can legitimately
   co-occupy one window (k·a_1,(k+1)·a_1) since window length can exceed P_max (or even L_0) by a
   large margin — there is no a priori cap on how many bad terms one window holds, so "how many bad
   terms fit in one gap" is NOT bounded by anything proven so far; a pure per-window pigeonhole
   count is a dead end unless paired with the finite-signature idea (1) to get a REAL cap.

### Candidate technique(s)
Finite-alphabet pigeonhole on the small-part signature S(m) (idea 1), in the spirit of the
crux-corpus "windowed sequence has ≤ r distinct values ⇒ forced repeat ⇒ upgrade to global
structure" template (KB entry: Pigeonhole/extremal principle, `knowledge_base.md` Combinatorics
section; also Modular arithmetic/CRT for the B_{s*}-periodicity-mod-L_0 fact). NOT global density
(Σ_{p>P_max}1/p², proven dead) — this is a purely combinatorial/algebraic finiteness (|Q| finite),
categorically different from the capacity-counting route.

### Cheap-kill candidates
- Check numerically (small a_1, long runs) whether a bad term's signature s* EVER repeats among two
  or more actual bad TERMS (not just integers) in the real sequence — if it never does even once in
  simulation, that's a strong hint the true mechanism is elsewhere (or that (CSP) genuinely never
  fails, making all of this vacuous / the crux needs a totally different closing idea). Cheap sympy
  check, ~minutes.
- Check whether a_1 vs L_0 ordering (idea 2) correlates with anything in when bad terms could appear
  (though (CSP) held with 0 bad terms on all tested seeds so far — no live bad-term data to probe).

### Knowledge-base entries to use
- **Pigeonhole / extremal principle** (Combinatorics section) — the underlying tool for idea 1.
- **Modular arithmetic, CRT** (Number Theory section) — underlies both L_0-periodicity of S(m) and
  the B_{s*} bounded-gap fact.
- Contradiction (General Proof Methods) — the overall proof shape (assume infinite chain, derive
  impossibility).

### Analogous past problems (cruxes)
- **aimo-0016** (number_theory, subtopics `pigeonhole` + `induction-and-construction`) — IMO-style
  problem: a real sequence where every term recurs within a bounded-length window ahead is proved to
  attain only finitely many (≤ r) distinct values (pigeonhole: more than r distinct values forced
  into one window of length r is absurd), then the repeat is iterated/upgraded via an auxiliary
  windowed-sum sequence into exact periodicity. **Genuinely analogous in shape**: it is exactly the
  template "finite-alphabet pigeonhole on a sequence ⇒ forced value repeat ⇒ upgrade repeat to
  global structure," which is the shape idea 1 above needs to be pushed through (my gap is in the
  "upgrade the repeated signature into a term-level contradiction" step, exactly where aimo-0016's
  hardest work — the D-set / one-step-earlier induction — lives). Worth the outliner reading the
  full solution (`past_problems_database.json`, problem_id aimo-0016) for the "upgrade infinitely
  often to always" induction machinery, which may transplant to upgrading "signature repeats
  infinitely" into "no bad term exists."
- **aimo-0079** (number_theory, `pigeonhole`/`sequences-and-recurrences`/`coloring-and-parity`) —
  pigeonholes a {0,1}-valued parity pattern over a bounded window (2^50 patterns) to find two
  positions with identical windows, then uses periodicity + a doubling trick (Ω(2n)=Ω(n)+1, opposite
  parity) to contradict an assumed nontrivial period. The "assume periodicity mod d, then compare n
  and a multiple of n to get a forced parity/value flip" trick is a plausible template for closing
  idea 1's B_{s*} periodicity fact into an actual contradiction, IF an analogous "doubling" or
  "shift" operation can be found for term-membership in E_∞ (not obviously available here — the
  problem has no multiplicative doubling structure, so treat this as a weaker analogy than aimo-0016).
- Not a match: no corpus entry found for "greedy minimal witness in a bounded window forces bounded
  large-prime linking" specifically for gcd-covering sequences — the `processes-and-algorithms` and
  `divisibility-and-gcd` subtopics were checked, nothing closer than the two above.

### Prior progress
Steps 1–5 of `covering-small-part-descent.md` are complete and gap-free (imported, not re-derived):
theorem ⟸ (CSP); base case |P|=1; bad terms off-lattice with a bad partner (mutual pair sharing only
large primes); smallest bad term has a strictly larger bad partner. The chain THIS lens assumes to
exist is exactly the hypothetical object Step 6→7 needs to either build (sub-gap 6a, out of scope for
this lens) or refute (sub-gap 6b, this lens). No approach has yet derived a contradiction from an
assumed infinite chain by any means, local or global.

### Dead ends (do not retry)
- **Global Σ_{p>P_max}1/p² capacity counting** (excluded by the dispatch itself) — proven dead,
  caps only a positive fraction of pairs (round 2, `lemmas/term-density-and-prime-capacity.md`).
- **Smaller-competitor-in-the-empty-window route (G3)** — proven structurally impossible: the
  interval (a_n,a_{n+1}) is empty of E_n by definition of greedy minimality, so no smaller compatible
  integer (good or bad) can ever be exhibited there; this includes my independently-derived "no good
  integer in the window" restatement (idea 3 above) — it is the SAME fact, already dead.
  `reduced-process-identity.md` G3, memory line 29.
- **Naive window pigeonhole assuming a window of length a_1 contains a full residue system mod
  L_0** — FALSE in general (idea 2): a_1 can be smaller than L_0 (e.g. a_1 prime), so this exact
  form of argument cannot be used without a case split or a workaround.
- **Pure covering-set/Helly/sunflower arguments** (Prop D barrier, round 2) — dead at the abstract
  set-system level regardless of locality; any closing argument needs the greedy VALUE dynamics
  (which idea 1 partially uses via the actual term chain, so it survives this barrier, unlike pure
  combinatorics).

### Small-case / intuition notes
- CSP (no bad terms) holds with ZERO exceptions on every tested seed (a_1 ∈ {15,35,99,231,1155,...})
  across multiple rounds — so the "infinite chain" this lens assumes may simply never be
  instantiable, i.e. the TRUE mechanism might be a direct proof that no SINGLE bad term can exist
  (closing (6a) instead, by contradiction at the very first bad term) rather than needing an infinite
  chain at all. This is a conjecture worth flagging to the outliner: **if 6a (unboundedness) turns
  out to be provably impossible to establish in general, it may be because the correct closing move
  short-circuits the chain argument entirely — e.g. deriving a contradiction directly from the single
  ascent step of Step 5 (m_0 has strictly larger bad partner B) using idea 1's finite-signature
  pigeonhole locally on JUST {m_0, B} plus finitely many further forced partners, without needing a
  literal infinite chain.** Not verified — a structural hunch based on where all the "no bad term
  found" empirical evidence points, worth the outliner considering as an alternative framing that
  bypasses splitting into (6a)+(6b) altogether.
