## imo-2026-06 (foreign-technique / crux-corpus scan for ¬(FIN-Q))

### Setup recap (from current.md + lemmas/, read in full)
Crux (round 7): ¬(FIN-Q) — an E_∞-inhabited bad class r_0 (mod L_0) whose large-connector pool
Q(r_0) = ⋃_{i∈W(r_0)} Q_i is INFINITE (Q_i = large primes of witness term a_i). Membership dichotomy
(★, certified in finite-witness-periodicity.md / reused in finite-connector-pool-periodicity.md):
m≡r_0 (mod L_0) is in E_∞ iff for every i∈W(r_0), some prime of Q_i divides m. Also on hand: Window
Purity (gaps are E_∞-free), Local Hub-Cover (one hub's finite Q(h) covers all its own missed colors),
bounded-gap fact a_{n+1}-a_n ≤ a_1 (⟹ a_n grows linearly, a_1 ≤ a_n ≤ n·a_1 roughly), minimal-bad-term
floor-tightness (v_p(m_0)≥2 ⟹ m_0 < a_1·p).

### Distinct openings surfaced (from corpus scan)

**1. Bounded-window distinctness (aimo-0415, aimo-0447) — most promising lead, HONEST GAP flagged.**
`aimo-0415` (P(x)=∏(x+d_i), 9 factors, prove a prime >20 divides P(x) eventually) and `aimo-0447`
(gcd(a+i,b+j)>1 grid, prove min{a,b}>(cn)^{n/2}) both use the SAME two-step engine:
(a) a *local* Σ1/p² (or 1/⌈N/p⌉²) capacity count shows small primes fill less than half a BOUNDED
window (length N), so ≥half the window's slots must carry primes exceeding the window length;
(b) **distinctness-by-difference**: a prime p > (window length) can divide at most ONE element of that
window (else p | their difference, but 0 < |difference| < window length < p — impossible). Combined,
this forces the window's line-values to be a PRODUCT of ≥N/2 distinct large primes — a growth/size
lower bound, not just an existence statement.
- **How it would transplant**: if the witnesses i∈W(r_0) contributing new large primes to Q(r_0) could
  be shown to lie inside one BOUNDED-length window of *values* (not indices) — e.g. via Window Purity +
  the already-proved linear growth of a_n, restrict attention to one period [x, x+L_0) or one hub's
  local window [a_1, a_1+M) — then any two terms a_i, a_j in that window sharing a *large* connector
  prime q > window-length would force q | (a_i − a_j), q ≤ window length, contradicting "large." This
  would upper-bound the number of DISTINCT large primes usable inside one bounded window, giving exactly
  the missing "value/dynamics inequality tying a_1 to the covering structure."
- **Honest gap it must still cross**: our witnesses a_i (i∈W(r_0)) are NOT confined to one bounded
  window — they are actual terms of the unbounded greedy sequence, spread arbitrarily far out (i→∞,
  a_i→∞), unlike aimo-0415/aimo-0447's genuinely bounded grid. The transplant needs a NEW argument for
  why "new-prime-contributing" witnesses must recur within a bounded band relative to L_0 or to each
  other — this is not automatic and is a real gap to close, not a free import. But it IS a technique the
  field hasn't tried: a **value-difference distinctness bound inside a window**, as opposed to every
  live approach's set-covering / abstract-membership framing.

**2. Finite-fiber gcd pigeonhole (aimo-0421 — "Der größte gemeinsame Teiler").** Crux: for fixed a,
{gcd(a,s): s∈S} is finite (divisors of a), so an infinite family S pigeonholes to an infinite subfamily
with CONSTANT gcd with a; alternatively "every prime dividing only finitely many elements ⟹ only
finitely many elements fail to be coprime to a fixed pair." **Checked carefully — this does NOT close
¬(FIN-Q):** applying the finite-hitting-set pigeonhole to {Q_i}_{i∈W(r_0)}, a hitting set S (the prime
factors of the actual witness m_0∈E_∞∩class r_0) can be finite and hit every Q_i via ONE recurring prime
p∈S, while Q_i also carries arbitrarily many "extra" primes irrelevant to hitting — these extra primes
alone can make ⋃Q_i infinite without violating m_0's membership. So this pigeonhole is CONSISTENT with
¬(FIN-Q), not a contradiction of it. **This mechanism collapses to the already-dead Prop D
(covering-structure-alone is insufficient)** — do not re-propose it as a fresh route; flag explicitly so
no builder wastes a round rediscovering this.

**3. Sunflower / Δ-system dichotomy (not in corpus, foreign import considered and REJECTED).** I tested
whether "{Q_i} is an infinite family of finite sets ⟹ either some prime recurs in infinitely many Q_i,
or an infinite pairwise-disjoint subfamily exists (extractable greedily), and a finite hitting set can
meet only finitely many pairwise-disjoint sets" gives a clean kill of ¬(FIN-Q). It does NOT: the
recurring-prime branch is always available and consistent (same "extra primes" escape as #2) — a finite
S can hit an infinite family via one recurring element regardless of how many other distinct primes the
Q_i's carry. **This is Prop D again in disguise. Confirmed dead on inspection — do not re-propose.**

**4. Zsigmondy / primitive-prime growth (aimo-0157 zsigmondy-and-primitive-divisors, aimo-0611 IMO-style
"a_n has a prime dividing none of a_1..a_{n-1}").** These PRODUCE new primes via growth
(x_n > x_1···x_{n-2} forces a valuation gap) — the opposite direction of what we need (we need to
*forbid* infinitely many distinct new primes, not manufacture them). Not transplantable as a closing
mechanism; only useful as a sanity check that "new primes keep appearing" is a real, not paradoxical,
phenomenon in general NT sequences — i.e. ¬(FIN-Q) is not obviously self-contradictory in the abstract,
which matches 3 rounds of failure to kill it structurally. **Do not pursue.**

**5. Reversible finite-state / mirror-recurrence (aimo-0964 "lamps", aimo-0351 injectivity-vs-revisit).**
Both use "a deterministic (or injective) process on a finite/structured state space that revisits an
earlier state forces exact periodicity from there on, and an invariant (parity/mirror-symmetry/
injectivity) is violated by short-circuiting the loop." This is conceptually the ancestor of the
"class-graph revisiting walk" framing already on the table (window-purity-class-cycle), but BOTH source
problems have a genuinely deterministic step map (cellular automaton, or f injective from an algebraic
identity) supplying the invariant for free. **Our situation has no such deterministic map**: which large
prime "gets used" at witness i is not a function of i alone in any established sense — GPC/Local
Hub-Cover give existence/coverage facts, not a deterministic transition rule. Transplant needs the
outliner to FIRST construct a genuine deterministic (or at least monovariant-bearing) transition on the
class-graph — e.g. "the least available connector prime at each revisit" — before this schema is usable;
that construction is exactly the open Step-5 descent (5a/5b) already named in current.md. Flag as
*inspiration for the shape of a monovariant* (an injectivity/mirror-style argument), not a ready import.

### Candidate technique(s)
- Bounded-window value-difference distinctness (opening #1) is the one genuinely new, not-yet-dead lever
  worth fielding — it operates on VALUES (differences bounded by window length) rather than on abstract
  set-covering, which is exactly what distinguishes it from Prop D/Helly (already dead) and from openings
  #2–#3 (also dead on inspection this round).
- Local capacity counting (Σ1/p² à la aimo-0447) is reusable ONLY if re-scoped to a genuinely bounded
  window; the already-certified global Lemmas C1–C3 (`lemmas/term-density-and-prime-capacity.md`) supply
  the needed Σ_{p>P_max} 1/p² < 0.2022 estimate and can likely be reused verbatim for the local version —
  no need to re-derive the numeric bound, just re-scope its application.

### Cheap-kill candidates
- None obvious for closing ¬(FIN-Q) directly. But a useful CHEAP PRUNE for the next round: before
  building out opening #1, check computationally whether, in small seeds where a genuine star/bad-class
  configuration can be forced by hand (e.g. deliberately constructed a_1 with many prime factors), the
  "new-prime witnesses" for one bad class actually cluster in index/value — i.e. numerically test whether
  W(r_0)'s new-prime-contributing indices lie within O(L_0) or O(a_1) of each other. This is cheap
  (reuse existing seeds a_1∈{15,35,99,231,1155}) and would validate/kill the bounded-window hypothesis
  BEFORE the outliner invests a full round building it out.

### Knowledge-base entries to use
- **Bertrand's postulate** / **Dirichlet (primes in AP)** — not directly load-bearing here but worth
  keeping in mind if the bounded-window argument needs to guarantee a prime IN a specific range rather
  than merely bound one out.
- No sunflower/Δ-system entry exists in knowledge_base.md — if the outliner wants that tool it must be
  stated and proved from scratch (it is NOT a citable KB entry); given finding #3 above, it is not needed
  since it doesn't close the crux anyway.
- Existing certified lemmas remain the base: Window Purity, Local Hub-Cover, finite-connector-pool-
  periodicity (FIN-Q⟹theorem), minimal-bad-term-floor-tightness — all reusable as-is.

### Analogous past problems (cruxes)
- `aimo-0415` (number_theory, size-bounding-and-descent / divisibility-and-gcd) — bounded-window
  pigeonhole-then-distinctness-by-difference. Best structural analogy for a genuinely new mechanism;
  crux move: "a large prime dividing two window members divides their bounded difference, so oversized
  primes are pairwise distinct within the window." Adapt with the honest gap noted above (need to
  establish boundedness of the relevant window of witnesses first).
- `aimo-0447` (number_theory, size-bounding-and-descent) — same engine at a higher size (grid), PLUS the
  local Σ1/p² capacity half-count that could re-use the already-certified C1–C3 estimate. Second-best
  analogy; same transplant gap.
- `aimo-0421` (number_theory, divisibility-and-gcd) — analogous in flavor (infinite family + finite-gcd
  pigeonhole) but VERIFIED not to close the crux (collapses to dead Prop D). Report as a dead end found
  this round, not a lead.
- Nothing in the corpus resembles the "class-graph revisiting walk" framing closely enough to supply its
  missing monovariant off the shelf; `aimo-0964`/`aimo-0351` are the closest available shape (deterministic
  revisit ⟹ periodicity/injectivity contradiction) but require a deterministic transition rule our problem
  does not yet have — inspiration only, not a transplant.

### Prior progress
(See current.md, fully read.) Crux weakened FIN-W→FIN-Q (round 7, certified). 4 lemmas certified this
lineage: Window Purity, Local Hub-Cover, (FIN-Q)⟹theorem, minimal-bad-term floor-tightness. No approach
has closed ¬(FIN-Q).

### Dead ends (do not retry)
- Global Σ1/p² capacity as a GLOBAL closer (bounds a positive fraction, never zero) — proven dead round 2.
- Pure covering/Helly (Prop D) — proven dead round 4: set-covering structure alone never forbids a large
  minimal member.
- Symmetric bad-partner ascent — proven dead (partner relation symmetric, no infinite-chain contradiction).
- aimo-0016 infinitely-often⇒always template — proven dead.
- Direct (q*,k) active rewrite (lex-rewrite-descent) — proven dead round 7 (needs a covering-preserving
  exchange Prop D permits to fail).
- Charging/injection vs the m·r^k orbit (constant prime set, Lemma 6's family) — proven dead (density→0
  fixed-signature orbit doesn't feed a global count).
- **NEW THIS ROUND**: finite-fiber gcd pigeonhole (aimo-0421-style) and the sunflower/Δ-system dichotomy —
  both checked in detail and found to collapse to Prop D via the same "extra irrelevant primes in Q_i"
  escape hatch (a finite hitting set can recur on one prime while the rest of Q_i's contents are
  unconstrained). Do not re-propose either as a fresh closing mechanism.

### Small-case / intuition notes
- Conjecture (unverified beyond existing seeds): in every numerically-checked a_1, no bad class is ever
  actually inhabited with an infinite pool — consistent with FIN-Q always holding, i.e. the theorem is
  true "for structural reasons stronger than mere set-covering," which is exactly why Prop-D-style
  arguments (openings #2, #3) fail: they only use the abstract covering shape, not the numeric/dynamic
  fact that Q_i is the actual large-prime factorization of an actual, minimally-chosen greedy term. This
  reinforces the round-7 mandate: the missing ingredient is a value inequality from the GREEDY MINIMALITY
  of a_{n+1}, not a purely combinatorial set-family fact — opening #1 (bounded-window distinctness) is
  the only surveyed candidate that touches VALUES rather than pure set structure, hence the strongest
  new lead to hand the outliner, with its gap stated honestly.
