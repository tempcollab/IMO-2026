## imo-2026-03 (UPPER wall — first-gap/min-distance telescope lens)

### Setup recap (all certified, do not re-derive)
Balanced valley: full budget m=n+1, a1<L/2, a2<β_nL (β_n=2^{n-1}u_n). Descending include/skip
reachable set R_0={0}, R_i=R_{i-1}∪{|v−a_i|:v∈R_{i-1}}. Lemma CONF: R_i⊆[0,a1]. Lemma MD2: reachable
*multiset* M_i doubles, |M_i|=2^i, support=R_i, enumerates all 2^{n+1} subset-KK values. Lemma FGR
(certified): μ_i=min(μ_{i-1}, dist(a_i,R_{i-1})), so μ_{n+1}=min_{1≤i≤n+1} dist(a_i,R_{i-1}). Reduction
R-COV' (certified, sufficiency direction only): μ_{n+1}≤u_nL ⟹ upper bound holds (via ESF-2, exactly n
DM moves, T=∅ correctly excluded). So the ENTIRE upper wall = prove the **first-gap pigeonhole**
μ_{n+1}≤u_n. Covering-radius (max-gap) family is dead (saturates 3–5·u_n, R10+R12); density/COUNT
pigeonhole is dead (set-injectivity false, all-equal counterexample, R11). Robustly true numerically
(0 fails over thousands of exact valley profiles n=2..7, worst ratio 0.70–0.75, tight exactly at the
dyadic ladder a_i=2^{n+1-i}/(2^{n+1}-1)) — I independently re-verified this with an exact-fraction
Python check, worst ratios ~1281/545291≈0.0023 (n=2) down to ~63/859490≈0.00007 (n=5), i.e. even more
comfortable margins than reported, confirming the claim (conjecture-level confirmation, not proof).

### Distinct openings for this lens

1. **Seeded/generalized strong induction (the most promising new angle, NOT yet tried in this exact
   form).** Lemma BL lands a first residual r∈[0,β_n) using pieces a1..a_k (k moves). The REFUTED
   round-9 "iterate BL" idea was a fixed DETERMINISTIC policy (greedy/flip-if-helps/drop-one) — those
   are refuted with explicit counterexamples (up to 11.4× overshoot) because they commit to *one*
   subset ahead of time. What has NOT been tried: an EXISTENTIAL strong induction on a *generalized*
   statement — treat r as a new "seed piece" together with the untouched pieces a_{k+1},…,a_{n+1}
   (mass L−P_k, remaining budget n−k+1ish — needs exact cut-accounting) and inductively invoke the
   FULL upper-bound theorem (not a greedy rule) on this smaller sub-instance, generalizing the target
   from "seed 0" to "seed r." This is different in kind from the dead greedy recursions: it uses IH as
   an *existence* claim (some good subset exists) at a strictly smaller n, not a fixed rule. The open
   technical question (why 12 rounds of induction-flavored attempts have not closed it) is finding the
   RIGHT generalized statement/scaling — Lemma VS already rules out a *single*-move IH certificate
   (proven, not just numerics), so this seeded induction must consume ≥2 further moves before invoking
   IH, and the seed r must be tracked multiplicatively against a *shrunk* u_{n-k} threshold. Flag for
   outliner: state precisely what generalized statement (parametrized by seed r and remaining mass) is
   being inducted, and verify by exact-fraction machine check BEFORE committing prose (per the
   standing numeric-first-gate rule) — the round-9 negative results already show naive greedy versions
   of this fail, so any new attempt must differ structurally (adaptive subset choice, not a fixed rule)
   or it will just re-hit the same wall.

2. **Complete-sequence / postage-stamp density analogy (classical combinatorics tool, not yet
   invoked).** The valley caps a1<L/2, a2<β_nL<a1/2ish are exactly a "superincreasing-from-the-top"
   condition: a1 dominates the rest, a2 is much smaller again. This is structurally the hypothesis of
   the classical **complete sequence / subset-sum density lemma** (used e.g. for postage-stamp
   problems and completeness of the Fibonacci sequence: if sorted decreasingly b1≥b2≥…, each bi ≤
   1+Σ_{j>i}b_j, then subset sums are "dense" with gaps ≤ min part). The catch: our reachable set is
   NOT the free subset-sum set — Lemma RL shows only *tree-realizable* (difference-caterpillar)
   patterns occur, strictly fewer than {0,±1}-signed sums. So the classical lemma does not transfer
   directly, but the STRUCTURE (dominant top element, geometrically-decaying tail, target = an
   exponentially small residual) strongly suggests hunting for a **restricted/weighted version of the
   density lemma for signed difference-trees** — i.e. prove an analogous "smoothness of consecutive
   sorted reachable values" fact but for the doubling map v↦|v−a_i| instead of free ±addition. This
   is a genuinely different target than both the dead covering-radius (worst gap) and dead
   set-count/multiset-gap (average gap) approaches: it would track the SORTED spectrum's *local*
   behavior near 0 specifically (not globally), exploiting that the many SMALL a_i's (i≥3,4,…) act
   like binary digits refining an approximation, converging fastest exactly near where the process is
   "aimed" (near the seed/landing point from opening 1). Concretely: after CONF+MD2 confine 2^{n+1}
   values (with multiplicity) into [0,a1], and BL/ESF-2 show they can be built by *any* subset order,
   the outliner should investigate whether **near 0 specifically**, the *local* density of
   tree-realizable values is provably ≥ 2^{n+1}−1 per unit length of [0,a1] — using the caps a1<L/2,
   a2<β_nL jointly with ALL remaining a_i (not just the first two, which is why the two-cap
   covering-radius approach — using only global caps — necessarily saturated).

3. **Euclidean-algorithm / continued-fraction analogy (structural insight, not a ready-made theorem).**
   The fold map φ_i(v)=|v−a_i| restricted to two numbers is exactly the subtractive (slow) Euclidean
   algorithm / continued-fraction step. Repeated differencing of a small set of reals is the classical
   mechanism by which gcd (rational case) or arbitrarily-small residues (irrational case, via
   three-distance / Steinhaus equidistribution) are produced. Our setting is a FINITE, BUDGET-LIMITED
   (n cuts), MULTI-NUMBER (n+1 pieces) generalization of this, with a target residual u_n that is
   EXACTLY what the "worst-case slow Euclidean algorithm" (Fibonacci-like, but with our caps forcing
   a factor-2 contraction per level rather than the golden ratio) would produce. This reframes GAP
   U-cover as: "does the n+1-piece tree-differencing process realize the analogue of a gcd/continued-
   fraction convergent within n steps, given the valley's mass constraint plays the role of the
   Euclidean 'size' bound?" This is a genuinely different vocabulary (continued fractions /
   Stern-Brocot / Ostrowski representations) that the field has not tried; it may or may not yield a
   clean lemma, but it explains WHY the extremal (tight) case is exactly the dyadic ladder
   2^n,2^{n-1},…,1 (the "worst" superincreasing sequence, analogous to the all-1 continued fraction /
   Fibonacci being the slowest-converging Euclidean input) — worth flagging to the outliner as intuition
   even if not directly provable.

### Candidate technique(s)
- Seeded/generalized strong induction (opening 1) — most concrete, closest to existing certified
  machinery (BL, ESF-2, R-COV', VS).
- Restricted density/completeness lemma for difference-trees (opening 2) — needs a genuinely new
  combinatorial lemma, likely the deepest but most structurally motivated route.
- Continued-fraction/Euclidean-algorithm framing (opening 3) — reframing/intuition only; flag for the
  outliner as a possible source of the right potential function, not a ready technique.

### Cheap-kill candidates
- Before any new prose: machine-check (exact fractions) any proposed seeded-induction statement or
  density bound on hundreds of valley profiles per n=2..7, exactly as rounds 9–12 did — this has
  reliably found counterexamples to naive recursions in 1 round each time (11.4×, 24.6× overshoots),
  so it is the fastest way to prune a bad idea before writing it up.
- Check whether the seeded induction's remaining-budget arithmetic even balances (k moves for BL +
  remaining n−k+1 pieces must fit within n total cuts) — a pure bookkeeping check that can kill a
  malformed generalization instantly.

### Knowledge-base entries to use
- `## General Proof Methods` — Induction (esp. "pick the right variable to induct on"; here that
  variable is likely the *seed value* jointly with n, not n alone — this is exactly the kind of
  generalization KB flags as necessary for induction to work).
- `## Combinatorics` — Pigeonhole/extremal principle (for opening 2's density lemma); no direct KB
  entry on "complete sequences," but the density/pigeonhole framing is the closest KB category.
- No KB entry on three-distance theorem / continued fractions exists; opening 3 is outside current KB
  coverage, would need to be built from scratch if pursued.

### Analogous past problems (cruxes)
Searched crux corpus (`domain=combinatorics`, subtopics `pigeonhole`, `extremal-principle`,
`size-bounding-and-descent`, `processes-and-algorithms`, `invariants-and-monovariants`; also
`number_theory` `size-bounding-and-descent`/`p-adic-valuation` for continued-fraction/dyadic keywords)
for "reachable set," "signed sum," "discrepancy," "minimum distance," "superincreasing," "dyadic,"
"continued fraction," "Euclidean algorithm." Best candidates, all only PARTIALLY analogous:
- **aimo-0836** (China, combinatorics) — repeatedly erase a,b and write {a+b, |a−b|} (unless already
  present) on a board of 1..n; goal: reduce to exactly two numbers. Structurally the closest match:
  it is literally a differencing/folding process on a finite set of numbers, solved by an explicit
  induction on n reducing to ⌈n/2⌉. But its target (collapse the *board size*) and its move set
  (allows SUMS as well as differences, and de-duplicates) differ enough from our tree-differencing
  min-value target that its crux move (halving induction with explicit small-case base) is only
  loosely transferable — worth skimming for induction-scaffolding style, not for the core lemma.
- **aimo-0913** (Croatia, combinatorics, graph-theory/forest bound) — smallest set S of integers such
  that for every k=2..n some x,y∈S have x−y=F_k (Fibonacci). Crux: build a graph with an edge per
  required difference, argue acyclicity via the greedy/Zeckendorf property of Fibonacci sums, bound
  |S| via the forest inequality; construction realizes each difference from a common anchor or
  adjacent element. Analogous in spirit (differences as edges, dyadic/Fibonacci-scale target) but the
  target there is a *lower bound on set size* via a forest/graph argument, not a "some difference is
  small" discrepancy claim — the mechanism doesn't transfer directly, but the "differences as a graph,
  use no-cycle to bound" trick is a technique worth the outliner being aware of if a graph/hypergraph
  reformulation of the reachable-set DP is ever tried.
- No genuine three-distance-theorem / continued-fraction crux was found in the corpus (searched
  `continued fraction`, `three-distance`, `equidistribution`, `stern-brocot`, `golden ratio`,
  `Euclidean algorithm`, `subtractive` — 19 hits, none on a min-of-differences-from-a-growing-
  reachable-set target). If opening 3 is pursued, it will need to be built essentially from scratch
  (no corpus crux to adapt), which should be flagged honestly rather than forcing a weak match.

### Prior progress
See recap above — everything through Lemma FGR + Reduction R-COV' (sufficiency) is certified. The
Covering claim/first-gap pigeonhole μ_{n+1}≤u_n is the entire open residual; I independently
re-verified it holds with wide margin on exact-fraction random valley profiles n=2..5 (own check,
worst ratio ≈0.00007–0.0023 — even more comfortable than the builder's reported 0.70–0.75, likely
because uniform-random sampling under-represents the tight dyadic-boundary profiles; consistent with
the established tightness at the exact dyadic ladder).

### Dead ends (do not retry)
- ANY covering-radius bound (one-cap R10, two-cap/windowed/exact-point R12) — exhausted, saturates at
  3–5·u_n, provably cannot reach u_n since max-gap and first-gap are not comparable in the needed
  direction (explicitly explained in FGR's certification note).
- Density/count pigeonhole on the reachable SET (R11) — set-injectivity is false in the valley
  (all-equal profile has |R_{n+1}|=2, not 2^{n+1}); the always-2^{n+1} MULTISET pigeonhole gap also
  does NOT bound the covering value (ratios up to 2.07×/3.0×, no gap→value conversion exists).
- Deterministic single-pass greedy recursions iterating Lemma BL (greedy band-landing, flip-if-helps,
  drop-one) — all refuted with explicit machine-verified overshoots up to 11.4× and an explicit n=2
  algebraic counterexample (A={9/20,7/25,27/100}: ESF-1/BL floor 17/100 > u_2=1/7; only the abs-flip
  subset {a2,a3} reaches 1/100 ≤ u_2). Any new recursive/inductive attempt (opening 1) MUST differ
  structurally from these (existential IH, not a fixed rule) or it will re-hit the same counterexample.
- Bounded-depth "escape to dominant regime" two-case skeletons (R10) — escape depth provably grows
  with n (failures 2.4%→52.9% at depth 2, n=4→6), not confined to near-uniform profiles.

### Small-case / intuition notes (conjecture, not proof)
- The first-gap pigeonhole is tight exactly at the dyadic ladder a_i=2^{n+1-i}/(2^{n+1}-1): here every
  nonzero {0,±1}-combination of powers of 2 is a nonzero integer ≥1 in absolute value (in the
  unnormalized ladder), and the descending cascade realizes exactly 1 = u_n·(2^{n+1}-1), i.e. equality.
  This strongly suggests the correct proof mechanism should specialize to an EXACT identity at this
  profile (not just an inequality with slack), which is a good sanity check for any candidate lemma:
  it must be tight, with no room for a "generic +ε" slack argument.
  All other tested profiles have comfortable margin (ratio well below 1, often orders of magnitude
  below), consistent with the dyadic ladder being the unique (or near-unique) extremizer — a useful
  fact for the outliner: a correct proof likely needs to show the dyadic ladder minimizes some
  "distance-to-target" functional over the valley, which is a smoothing/rearrangement flavor argument,
  distinct from all three openings above but possibly combinable with opening 2's density lemma
  (show the density bound is tight iff superincreasing-by-exactly-2× at every scale, i.e. the dyadic
  case).
