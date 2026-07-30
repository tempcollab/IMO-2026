## imo-2026-06 — lens: GREEDY SUCCESSOR-CHOICE DYNAMICS

### Context recap (what's certified, what's the wall)
The whole problem is reduced (certified, reused, do not re-derive):
enumeration-of-E-infinity.md, periodic-set-enumeration.md, csp-implies-theorem.md. The single
remaining wall is certified-equivalent across FOUR faces: (CSP) [no large prime load-bearing] =
ℰ-small-only [certified `csp-iff-E-small-only.md`] = (EC) [essential-connector, certified
`essential-connector-equivalence.md`] = ¬(FIN-Q) [certified `finite-connector-pool-periodicity.md`].
Two greedy-value lemmas are already certified and ARE the dynamics toolkit currently in play:
- `window-purity.md`: every integer strictly between a_n, a_{n+1} is ∉E_∞ (non-covering).
- `minimal-bad-term-floor-tightness.md` (Lemma 9/X): for the smallest bad term m_0 with prime set
  C, every "sheddable" prime p (p²|m_0, or p‖m_0 with C∖{p} still covering) satisfies m_0 < a_1·p —
  a genuine downward VALUE bound, but it stalls exactly at the a_1 threshold when C is itself a
  minimal covering set containing a large prime with NO sheddable prime (case A) — Prop D shows
  such minimal covering sets with large minimal realization exist abstractly, so the descent has
  nothing left to shed.
Essentiality propagation (Lemma 14) shows the failing configuration (A,q) reproduces with q
PRESERVED — horizontal, no monovariant. This is the exhausted wall: four framings, one obstruction.

### Distinct openings under this lens

**Opening 1 — direct process-monovariant à la IMO2015-N4 (aimo-0678), NOT yet tried.**
The crux corpus's closest real analog is `aimo-0678` (IMO 2015 SL N4): a coupled gcd/lcm
recurrence proved eventually periodic via (a) a "min of a failing set" monovariant
w_n = min{m ≥ a_n : m ∤ s_n} (s_n = a_n+b_n, frozen in one regime, forced down at a "jump"), shown
NON-INCREASING by an explicit phase case-split (freeze phase vs. jump phase), hence eventually
constant ⇒ a_n bounded; then (b) reduce the OTHER coordinate mod the lcm of attainable bounded
values to get a finite state ⇒ periodicity. This two-stage template — (i) a min-of-a-failing-set
potential proved non-increasing via a PHASE case-split, not a static inequality; (ii) bound one
coordinate first, then mod-reduce the other — has NOT been imported by any of the 15 approaches on
file (they attack CSP as a single static covering fact, never as a phase-switching process
potential). Candidate transplant: let w_n be something like "the least large prime not yet
resolved as non-essential up to index n" or "the least bad-window value not yet excluded", and try
to mimic the freeze/jump case split using window-purity (freeze: gap has length exactly what
Realizability predicts, nothing new recruited) vs jump (a genuinely NEW large prime recruited,
which by Lemma 9 floor-tightness pins the recruiting term to a bound involving a_1·p). This is a
genuinely different PROOF MECHANISM (explicit phase potential with a freeze/jump dichotomy) from
every static covering/EC/FIN-Q reformulation tried so far — worth fielding as its own approach.
Risk: it may simply re-derive (CSP) under new names (the "jump" case is exactly ¬(FIN-Q)'s new-prime
recruitment) — but the VALUE of trying it is that aimo-0678's proof succeeds specifically because
the phase case-split makes the invariant sum s_n do double duty (bounding AND enabling the later
mod-reduction); no approach here has tried an analogous "invariant sum" (e.g. Σ over active
predecessors of something bounded) playing that role.

**Opening 2 — window-as-sieve / exact-one-survivor rigidity (not tried as a counting device).**
Window Purity + the certified gap bound a_{n+1}-a_n ≤ a_1 together say: the interval
(a_n, a_n+a_1] contains AT LEAST one term (a_{n+1}) and every integer strictly below a_{n+1} in
that interval is killed by SOME earlier predecessor a_i (i≤n), i.e. lies in one of the "kill
classes" {x : gcd(x,a_i)=1}. This is a genuine SIEVE structure: the window of length ≤a_1 is
covered by n kill-conditions except for exactly the survivor(s) a_{n+1}, a_{n+2}, .... No prior
approach has tried treating this literally as a Jacobsthal-function-style bound (the classical
Jacobsthal function g(N) bounds the maximal gap between integers coprime to N by using ONLY
primes dividing N). Here the "kill classes" are defined not by one fixed modulus but by n
DIFFERENT a_i's — so it is not literally Jacobsthal, but the counting technique (bound how many
consecutive integers a union of "non-covering" residue conditions can kill) is the same genre and
untried. Concretely: ask whether the SAME large prime q, once first recruited at some hub term h,
must recur inside EVERY subsequent window of length a_1 (by essentiality propagation, Lemma 14,
its "descendant" configs keep the same q) — if so, q divides a positive-density residue class and
must appear as a factor of some term in every window of length ≤ (period of that residue class),
giving an explicit "one slot per window" COST that can be compared against the proven O(X) term
density (`term-density-and-prime-capacity.md`, C1: N(X)=Θ(X)) FOR A SINGLE FIXED q, rather than
against the whole dead global Σ1/p² sum over ALL large primes. This is the round-8 "growth-
rate/recruitment counting" suggestion, restated with the exact certified handle (Lemma 14 q-
preservation) that makes it concrete: since q recurs with the SAME identity (not just "some large
prime"), a per-q recruitment argument sidesteps the proven-dead aggregate Σ1/p² count. WARNING:
this must be checked against `distinctness-by-difference.md`'s (R2′) impossibility — that lemma
killed a similar-looking "confine to bounded value-band" argument by showing it's equivalent to
Q(r_0) finite. The NEW ingredient that might escape (R2′) is tracking a SINGLE q's own residue
class (density 1/q, not a bounded value-band) rather than confining to [a_1,V) — worth having the
outliner verify this is not the same trap before committing a builder.

**Opening 3 — floor-tightness iterated along the class-graph walk (closing the round-7 Step-5 gap
with the SPECIFIC "value, not prime" monovariant).**
Round 7's ¬(FIN-Q) is modelled as a revisiting walk on a finite (≤L_0-node) class-graph; its
descent (Step 5) was never extracted because "the refined star ascends q_k→∞, no monotone
descent." But floor-tightness (Lemma 9) is a VALUE bound, not a prime bound: m_0 < a_1·p. The
natural monovariant to try on the walk is NOT the prime q_k (unbounded, as already noted) but the
VALUE of the hub term at each revisit, i.e. define v_k = the k-th revisited hub's term value, and
ask whether Lemma 9's proof technique (remove a shedddable-prime factor, get a smaller bad term
unless it drops below a_1) can be run not just once (on the single smallest bad term) but on EVERY
node of the walk with a running bound that ties v_k to a_1 · (product of primes used so far in the
walk) — since the walk lives on a graph with ≤L_0 nodes, if the value bound can be shown to force a
strict decrease in v_k modulo the finitely many residues, pigeonhole gives a repeat, hence a cycle,
hence (by minimality assumptions) a contradiction. This is exactly what round 7/9 flagged as
"needs a genuinely new descent variable" — the concrete new variable being VALUE (not prime, not
size |Q_C|, not rad) computed via repeated floor-tightness application rather than a single
application. Not yet attempted as a repeated/iterated argument (Lemma 9 has only ever been applied
ONCE, to the single global smallest bad term, never iterated along a walk).

### Cheap-kill candidates
- None obvious as an outright kill; but a cheap SANITY CHECK before fielding Opening 2: verify
  numerically whether the SAME large prime q, once recruited, really does recur in bounded-length
  windows forever (i.e. whether Q(r_0) staying infinite necessarily means SOME single q has positive
  density, vs. genuinely needing infinitely many DISTINCT q's each appearing once) — if the latter,
  Opening 2's "per-q cost" argument is moot since no single q ever gets charged more than O(1) times
  and the whole leverage evaporates. Quick numerical probe below suggests this scenario has never
  been observed at all (CSP holds unconditionally on every tested seed), consistent with round 7/9
  notes.

### Knowledge-base entries to use
- `knowledge_base.md` "Modular arithmetic, CRT" (residue-class covering, relevant to Opening 2/3
  finite-state mod-L_0 reduction).
- "Invariants & monovariants" entry (generic template for Opening 1/3 — a quantity proven monotone
  under a process, forcing termination/periodicity).
- "Dirichlet's theorem" is NOT directly load-bearing here (no need for primes in AP), flag as a
  red herring if a builder reaches for it.

### Analogous past problems (cruxes)
- **aimo-0678** (IMO 2015 SL N4) — STRONGEST analog. Crux: min-of-a-failing-set monovariant
  w_n=min{m≥a_n : m∤s_n} proved non-increasing via an explicit freeze/jump phase case-split on a
  coupled gcd/lcm recurrence, giving boundedness, then mod-reduction of the other coordinate gives
  a finite state ⇒ eventually periodic. Genuinely analogous IN GOAL (prove a gcd-defined integer
  sequence eventually periodic) and IN OBSTACLE SHAPE (need to bound one quantity before a
  mod-reduction argument works) — but its invariant sum s_n has no ready-made analog here; the
  transplant is a genuinely new mechanism to TRY, not a proof to copy.
- **aimo-0503** (IMO SL 2008 N3, gcd(a_i,a_{i+1})>a_{i-1} ⟹ a_n≥2^n) — same genre (bound gaps of a
  gcd-driven sequence from below via the gcd itself), but its technique (gcd(a_i,a_{i+1}) ≤ a_i, so
  the gap is bounded below by the PREVIOUS term) doesn't transplant — our gaps are bounded ABOVE
  by a_1 already (certified), and the open direction here is an upper/finiteness obstruction on
  primes, not a lower growth rate. Listed for completeness; not a strong match.
- **aimo-0447** (USAMO 2014/6, gcd(a+i,b+j)>1 grid ⟹ min{a,b} large) — same covering-grid technique
  already fully absorbed into Prop D / the certified capacity lemmas (`term-density-and-prime-
  capacity.md`); its Σ1/p² count is EXACTLY the proven-dead global capacity route. Confirms (does
  not open) that global density counting is a dead end here — no new leverage from re-reading it.

### Prior progress
Current best (unchanged from round 9): full reduction to (CSP)=ℰ-small-only=(EC)=¬(FIN-Q), all
four certified-equivalent. Two greedy-VALUE lemmas certified and reusable (window-purity, minimal-
bad-term-floor-tightness/Lemma 9) — these ARE the dynamics leverage extracted so far, and they are
exactly the material Opening 1 and Opening 3 propose to re-deploy in a genuinely new way (phase
potential; iterated/repeated application along a walk) rather than the single static application
tried in rounds 7–9.

### Dead ends (do not retry)
- Global Σ1/p² capacity counting (round 2, `large-prime-capacity-counting`) — proven insufficient,
  bounds only a positive fraction, never zero.
- Pure covering/Helly/sunflower combinatorics alone (Prop D barrier, round 2) — provably admits a
  large minimal covering member; dynamics is REQUIRED.
- Direct (q*,k) active-rewrite operator (`lex-rewrite-descent`, round 7) — proven no valid operator
  exists (circular / Prop-D-blocked).
- Transversal ℰ-small-only monovariant via partner map (`minimal-cover-small-only`, round 9) — its
  only lever is horizontal (q preserved), self-certified dead.
- Bounded-value-band distinctness confinement (`bounded-window-distinctness`, round 9) — (R2′)
  proves this is equivalent to the negation of what it needs to show; vacuous as a closer. NOTE:
  Opening 2 above is NOT a re-run of this — it proposes tracking ONE fixed q's own residue class
  (unbounded density argument), not confining to a bounded value window; but the outliner should
  double check this distinction holds before committing a builder, since it is easy to collapse
  back into the same (R2′)-barred shape.
- aimo-0016 "infinitely-often ⇒ always" template — proven not to transplant (round 5), no per-index
  local recurrence in the bad family.

### Small-case / intuition notes (conjecture only)
Quick numerical check (python, gcd-greedy simulation) for a_1 ∈ {15, 21, 35, 45, 99, 105, 231}
confirms (as in prior rounds) zero bad terms / zero large-prime essential connectors across 300+
generated terms each — (CSP) appears to hold unconditionally, consistent with all previous rounds'
numerics. This is evidence only, not a proof, and does not by itself favor any one opening; it does
suggest that whichever monovariant is found, it should be provable WITHOUT any exceptional small
cases (no seed has ever produced a genuine bad term to study structurally) — meaning any of the
three openings above must ultimately be a fully general argument, not one calibrated against an
observed counterexample-adjacent configuration (none exists in the data).
