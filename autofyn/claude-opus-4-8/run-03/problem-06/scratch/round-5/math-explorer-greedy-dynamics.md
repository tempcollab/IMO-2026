## imo-2026-06 (lens: attack the greedy DYNAMICS, not E_∞ covering-set variations)

- **Distinct openings** (all avoid re-deriving/using the static E_∞ ∩ [a_1,∞) / (CSP) covering-set
  reduction as the *mechanism of proof* — they use the actual step-by-step greedy search):

  1. **Extremal principle on the linking PRIME, not on the term value.** All 4 rounds so far well-
     order the **terms** (smallest bad term m_0, Step 5 of covering-small-part-descent). That gives a
     *symmetric* witness relation ({m_0,B} is a mutual bad pair — B's witness can be m_0 again), which
     is exactly the stuck (6a) gap. A genuinely different top-level object: well-order the **large
     primes** that ever serve as a sole/only-large-prime link between two terms. Let
     `q* = min{q > P_max : q is the sole linking prime of some bad pair}` (exists by well-ordering of
     ℤ_{>0} if any bad pair exists at all). This is *not* equivalent to ordering by term value — the
     smallest bad term's linking prime need not be q*, and conversely q*'s bad pair need not be the
     value-minimal one. Minimality of q* gives a genuinely different piece of information: **every**
     large-prime-only link anywhere in the whole sequence uses a prime `≥ q*`. Combined with GPC
     (bad pairs are off-lattice, confined to windows of length `< a_1`), this bounds how densely
     q*-or-larger primes can recur inside any single window (multiples of a fixed prime `p ≥ q*` are
     spaced `≥ q*` apart), a LOCAL pigeonhole distinct from the proven-dead GLOBAL Σ1/p² capacity
     count. This escapes both barriers: it is not a covering-set/Helly argument (Prop D dead end) and
     not global density (large-prime-capacity-counting dead end) — it is a genuinely new well-ordering
     target (on primes) feeding a genuinely new *local* counting argument. UNDEVELOPED — flagged only
     as an opening, not attempted here.

  2. **Direct dynamic monovariant on the greedy search itself** (aimo-0678-style "min-of-a-set"
     potential, adapted). aimo-0678 proves eventual periodicity of a coupled gcd/lcm recursion by
     defining `W_n = {m ≥ a_n : m ∤ s_n}` (s_n a frozen combined invariant) and showing
     `w_n = min W_n` is non-increasing directly from the recursive update rule — a genuinely dynamic
     process-level monovariant, not a static set-membership fact. Our process has no closed-form
     algebraic recursion (a_{n+1} is defined by *search*, not formula), so the transplant is not
     literal, but the SHAPE is a real candidate: fix the invariant `L_0 = ∏_{p≤P_max} p` (or `a_1`
     itself) and define a monovariant on the *residue/near-multiple structure* of a_n that tracks how
     far the process currently is from "resyncing" onto the a_1-lattice — e.g.
     `d_n := (\text{next multiple of } a_1 \text{ above } a_n) - a_n \in \{1,...,a_1\}` together with
     which small primes of P are already "satisfied" by a_n's factorization — and ask whether this
     finite-valued state, tracked through the ACTUAL greedy transition (not through E_∞ membership),
     is forced into a bounded orbit for reasons intrinsic to the search rule (every rejected candidate
     in `(a_n, a_1⌈a_n/a_1⌉]` has a concrete blocking predecessor). This targets eventual periodicity
     of the *state* directly (finite-state pigeonhole, aimo-0678 Solution 2 / aimo-0514 style: a
     deterministic map on a provably finite state set forces eventual periodicity) INSTEAD of proving
     "no large prime is ever load-bearing" as an intermediate static fact. Caveat: aimo-0678's
     Solution 2 pigeonhole itself still leans on Solution 1's monovariant-boundedness result first —
     so this route likely still needs *some* boundedness input; the payoff is that the boundedness
     input could be a genuinely different (process-level) quantity than "which primes are load-
     bearing," e.g. boundedness of `d_n` is ALREADY certified (gap ≤ a_1, current.md) — the open
     question is whether `d_n` (or a refinement of it) plus a SMALL amount of extra state already
     forces the transition map to be eventually deterministic/periodic without ever separately
     establishing (CSP).

  3. **Per-large-prime valuation squeeze** (aimo-0477-style Case-1/Case-2 dichotomy, technique donor
     only). aimo-0477 proves `v_p(a_n)` is eventually monotone (hence eventually constant) for each
     prime `p | a_1 a_k` by a two-case argument forced by an algebraic integrality condition
     (`v_p` of a sum of rationals can't have a unique minimal term). Our problem has no such algebraic
     sum, so this is NOT directly transplantable, but the underlying idea — track `v_q(a_n)` (or
     simply "is `q | a_n`?") for a FIXED candidate large prime q across the whole sequence and prove a
     dichotomy (q's occurrences are eventually absent, or eventually periodic-with-bounded-density)
     using the greedy MINIMALITY rule as the source of monotonicity, rather than covering-set
     structure — is a distinct lens worth having on the table. Numerically (see below) large primes q
     DO appear as incidental co-factors of good terms with positive density once E_∞ is periodic, so
     "eventually absent" is the wrong dichotomy target; the right target is "q never becomes the SOLE
     connector of a pair," which is exactly (CSP)/GPC's territory — so on inspection this opening
     mostly re-collapses into the existing crux. Downgrade to a weak lead; report honestly.

  4. **Local (bounded-band) pigeonhole using GPC's window confinement**, distinct from the dead global
     Σ1/p² count. GPC (certified) already confines every bad pair strictly to open windows of length
     `< a_1` between consecutive multiples of a_1. Instead of summing capacity over ALL of `[1,X]`
     (proven insufficient), fix ONE window and ask how many *distinct* bad terms with *distinct*
     linking large primes can co-occur there, bounded by `a_1` itself (a window has only `a_1 - 1`
     integers) — a trivial bound, but combined with opening 1 (extremal-on-prime q*) it could turn
     "one ascent step" into "boundedly many bad terms per window, but the SET of windows containing a
     bad term must itself be finite" — i.e., relocate the induction from term-value to *window index*.
     This is the most promising concrete NEW top-level target: prove **only finitely many windows
     `(k a_1,(k+1)a_1)` ever contain a bad term**, via a monovariant on `k` (not on term value) fed by
     opening 1's prime-extremal argument. UNDEVELOPED, flagged as the strongest lead for the outliner.

- **Candidate technique(s):** well-ordering / extremal principle applied to a NEW object (the linking
  prime, or the window index `k`, rather than the bad term's value) to escape the proven-symmetric
  witness relation of Step 4; process-level (not set-level) monovariants/finite-state pigeonhole in the
  style of aimo-0678/aimo-0514; p-adic valuation tracking (aimo-0477) as a technique donor only —
  largely re-collapses into the known crux on inspection, do not over-invest.

- **Cheap-kill candidates:** (a) check numerically whether the SAME large prime `q` ever serves as the
  sole connector for TWO DIFFERENT bad pairs in the sequence (would immediately give an ascending chain
  along a FIXED prime, bypassing (6a) entirely) — worth a quick simulation next round, since if true it
  hands the outliner a non-symmetric ascent for free; (b) check whether `q*` (globally smallest ever
  sole-linking large prime, opening 1) is ever `≤ 2·P_max` or shows any small/bounded relation to `a_1`
  across seeds — would suggest a clean closed form rather than an abstract existence argument.

- **Knowledge-base entries to use:** "Invariants & monovariants" (knowledge_base.md, Combinatorics
  §117 and General Proof Methods §191) — for opening 2/4's process-level monovariant; "Pigeonhole /
  extremal principle" (§108, §188) — explicitly licenses "take the maximal or minimal element" as a
  top-level device, directly supporting opening 1's well-ordering on primes/windows instead of term
  value; "Infinite descent... no minimal counterexample can exist" (§184-185) — relevant framing for
  why a *fresh* extremal object (prime or window, not term) might dodge the symmetric-pair trap that
  killed the term-value descent.

- **Analogous past problems (cruxes):**
  1. **aimo-0678** (subtopics `size-bounding-and-descent`, `modular-arithmetic-and-CRT`,
     `divisibility-and-gcd`) — genuinely the closest structural analog found: an eventual-periodicity
     claim for an integer sequence defined by a greedy-ish coupled recursion, proved via (i) a
     "min-of-a-set" monovariant `w_n = min{m ≥ a_n : m ∤ s_n}` tied to a frozen invariant, shown
     non-increasing directly from the update rule, giving boundedness, then (ii) a finite-state
     pigeonhole on `(a_n, b_n mod M)` to conclude eventual periodicity. This is a genuine template for
     opening 2 — the crux move ("construct a min-of-a-set integer monovariant tied to a frozen
     invariant and show it never increases from the recursion itself, then pigeonhole a finite state")
     is adaptable in SHAPE, not literally (no closed-form recursion here). Worth the outliner reading
     in full (`past_problems_database.json`, id `aimo-0678`).
  2. **aimo-0477** (subtopics `p-adic-valuation`, `divisibility-and-gcd`) — same target-shape
     (eventually-periodic / eventually-constant integer sequence, finitely many relevant primes) via
     valuation monotonicity per prime. On inspection (see opening 3) it mostly re-collapses into the
     already-known crux for our problem — a technique donor, not a template; lower priority than
     aimo-0678.
  3. **aimo-0514** (subtopic `processes-and-algorithms`, `invariants-and-monovariants`) — "a
     deterministic process is reversible ⇒ its state graph is a union of cycles ⇒ purely periodic" is
     a clean instance of the finite-state pigeonhole idea in opening 2, but the reversibility mechanism
     (bijective one-step map) does not obviously exist for our greedy sieve (the map a_n ↦ a_{n+1} is
     NOT obviously invertible/bijective on any natural finite state space without already knowing
     (CSP)) — weaker analog than aimo-0678, cite only as a second illustration of "finite deterministic
     state ⇒ periodicity," not a route.

- **Prior progress:** (from current.md / bad-partner-and-ascent.md, all CERTIFIED, reusable, do NOT
  re-prove) — enumeration reduction, periodic-set endgame, GPC (bad/covering-violating pairs share only
  large primes ⇒ both off the a_1-lattice), CSP⇒theorem (order-free), bad-partner lemma (every bad term
  has a bad, mutual, off-lattice partner sharing only large primes), and the Step-5 single-ascent
  (smallest bad term has a strictly larger bad partner). The crux is now precisely: **(6a)** upgrade one
  ascent step to an infinite/unbounded family (blocked because the Step-4 witness relation is symmetric
  on a pair) and **(6b)** derive a contradiction from such a family (global capacity proven insufficient).
  All of this is inherited terrain, not new; my openings above are candidate ways to attack (6a)/(6b)
  from OUTSIDE the term-value well-ordering that produced the symmetric trap.

- **Dead ends (do not retry):** pure covering-set/Helly/sunflower closure (Prop D barrier — crux is
  FALSE at the abstract set-system level); global Σ1/p² capacity counting (large-prime-capacity-counting,
  RETHINK — bounds only a positive fraction, never zero); "smaller compatible candidate in the empty
  window `(a_n,a_{n+1})`" (route G3, round 3 — window is provably empty, any argument re-deriving a
  smaller-in-window competitor is circular); self-dual-clutter-grading's value-grading lever (RETHINK,
  round 4 — self-certified to collapse to the SAME Step 6→7 wall as covering-small-part-descent, i.e.
  it does NOT escape the term-value well-ordering trap despite superficially looking different);
  claiming witness/hub terms are "P_max-smooth" (false, a_1=231 counterexample 237=3·79).

- **Small-case / intuition notes (conjecture, from a fresh numeric probe this round):** ran the actual
  greedy construction for a_1 ∈ {15,35,99,231} out to 400 terms and recorded, for every large prime
  `q > P_max` that ever appears, the FIRST term it divides. In every case that term is also divisible by
  a small prime of `P` (e.g. a_1=231: first occurrence of 79 is at term 237 = 3·79, and 3 ∈ P), i.e. the
  large prime is riding along on an already-good term, never itself the sole connector — consistent with
  (CSP) holding but only reconfirms existing zero-counterexample evidence, does not newly test opening
  1's `q*` object (no bad pair has ever been observed to test against). This is weak/negative evidence:
  it says nothing new about openings 1/2/4, since a genuine test of them would require an artificially
  constructed near-miss (e.g. tampering with a_1's factorization to try to force a bad pair) rather than
  observing genuine greedy runs, which by all evidence never produce one — the crux is a genuine
  non-existence statement that small-case search cannot falsify further; it needs the proof.
