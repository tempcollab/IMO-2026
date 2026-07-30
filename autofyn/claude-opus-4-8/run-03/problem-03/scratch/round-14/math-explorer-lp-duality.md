## imo-2026-03 (ESCALATION LENS: potential-free / LP-duality / extremal re-derivation attacking both walls)

### Summary verdict up front
A genuine, NEW, computationally-supported mechanism exists for the **LOWER** wall (GAP-EXTR): an
**explicit LP-duality / Farkas certificate**, which turns out to be the *same* object as a
**smoothing/exchange-toward-extremal argument** on the fixed-sum groups (the two views are
literally dual to each other — verified below). This is genuinely different in *kind* from all 5
exhausted lower/upper families (it is a static certificate for a completed finite LP per
combinatorial type, not an online/foresight running scan, not a transport/matching certificate, not
a monovariant on an adaptively-built adversarial sequence). I do **not** find a single joint
LP/minimax argument that closes BOTH walls at once in one shot — the upper wall's claim is an
*existence* statement (∃ a subset with small value), which is not the natural shape for a Farkas/LP
lower-bound certificate; the natural LP/duality-flavored analogue there is an **averaging/expectation
argument** (a different, but still new, mechanism), not literally the same duality machinery. I report
both, with the caveat that the "single certificate for both walls" hope is likely NOT realizable as
stated — say so honestly to the outliner rather than force a match.

---

### LOWER wall (GAP-EXTR / MID-core): the LP-duality opening — WORKED OUT CONCRETELY

**Setup recap (certified, from `merge-interleave-pattern.md`, Theorem VERT-LOW / Lemma BLK).** For
each combinatorial type T (a word σ interleaving F-fragments and B-tail-fragments, plus the tail's
group structure), P_T is a polytope: variables = piece values; (E) n+1 linear equalities (F-sum = 2^n,
and each dyadic-level group sums to 2^j); (O) the descending order chain fixed by σ; (C) box
0≤v_i≤2^{n-1}. On P_T, D coincides with the LINEAR functional L_T(v) = Σ_odd v − Σ_even v (alternating
sum in σ's order). GAP-EXTR is: min_{vertex of P_T} L_T ≥ 1, for every type T, every n.

**New opening: prove this via an explicit LP dual / Farkas certificate rather than vertex
enumeration + induction.** Since P_T is defined by equalities (E) and inequalities (O),(C), for ANY
type T, weak LP duality gives: if there exist multipliers y_j (one per equality in (E)) and
nonnegative multipliers z_k (one per inequality in (O)∪(C)) such that

  L_T(v) − 1 ≡ Σ_j y_j·(equality_j(v) − rhs_j) + Σ_k z_k·(slack_k(v))   for ALL v (as a linear identity),

then L_T(v) ≥ 1 automatically on the *whole* feasible region P_T (not just at the vertex) — a
certificate-based proof, no case-split on which vertex is extremal.

**Computational check (three independent hand-built types, n=3, via `scipy.optimize.linprog`,
`method='highs'`, exact-rational-checked by hand/sympy too):**
1. Type A: |F|=3, tail C_2={4,2,1} uncut, word (desc.) B(4),F1,F2,B(2),F3,B(1); signs +−+−+−.
   Symbolic: L_T − 1 = 8 − 2F1 = **2·(4 − F1)**, i.e. 2× the slack of the single order constraint
   "B(4) ≥ F1". Min at F1=4 (boundary) ⇒ L_T=1. Matches ATT witness exactly.
2. Type B (|F|=4, tail uncut, word B(4),F1,F2,B(2),F3,B(1),F4): LP dual gave eq-multiplier
   **y=+1** (on ΣF=8) and a SINGLE nonzero inequality multiplier **z=2** on the constraint "F1≤4"
   (all other order-constraint multipliers 0). min L_T = 1 exactly, x*=(4,3,1,0), reproducing the
   ATT tight family {4,4,3,2,1,1,0→trivial}.
3. Type C (|F|=3, tail C_2 with the level-2 group SPLIT into b1a+b1b=2, i.e. one extra tail cut,
   word F1,B(4),F2,b1a,b1b,F3,B(1)): LP dual gave eq-multipliers **y=(+1,−1)** and a single nonzero
   inequality multiplier **z=2** on "F3≤b1b" — min L_T=3 (not tight for this word, correctly ≥1).

**Pattern (labelled CONJECTURE, only 3 hand-built instances checked, not exhaustive):** in every
instance tried, the optimal LP dual is supported on (a) the n+1 equality constraints with multiplier
**exactly ±1** (sign = the word's net parity contribution of that group), and (b) **exactly ONE**
binding order-inequality (a single "B-piece ≥ F-fragment" or "F-fragment ≥ B-piece" cross comparison)
with multiplier **exactly 2**. This is a strikingly *sparse*, small-integer certificate — not the kind
of unbounded-κ blowup that killed the scalar-reserve family (R10: κ unbounded in n). It also
**coincides exactly** with a smoothing/exchange view: within a fixed-sum group (E-constraint), moving
one unit of value from a "−"-position element to a "+"-position element changes L_T by exactly **+2**
per unit (holding the group sum fixed), until an order constraint (O) becomes binding — that binding
constraint is exactly the dual-certificate's single active inequality. **So the LP-duality certificate
and a same-group exchange-smoothing argument are the same mechanism, viewed two ways** — a coherent,
non-accidental finding.

**Crux-corpus analogue found (strong match): `aimo-0146`** (algebra/extremal-principle — "Maximize a
fixed weighted sum of a sorted nonnegative integer sequence under a sum constraint by
exchange-smoothing weight toward the higher-coefficient positions until the free coordinates
equalize and the tail drains, then enumerate the few surviving profiles"). Its "Algebraic bound"
lemma is close to line-for-line our situation: bound Σ a_i x_i for a SORTED sequence x_1≥…≥x_65
subject to Σx_i ≤ const, via (i) an adjacent-swap smoothing move that strictly increases the
objective while preserving sortedness+sum (exactly our "move value from a low-coefficient slot to a
high-coefficient slot"), reducing to "all values in a block differ by ≤1", then (ii) enumerating the
resulting FEW candidate extremal sequences directly. The one structural difference: aimo-0146 has a
SINGLE sum constraint; our GAP-EXTR has n+1 simultaneous group-sum constraints (the dyadic ladder).
This is exactly why R13's step-4 ("generic box-free vertex = canonical ATT layout") stalled as an
unverified-beyond-n=4 conjecture: it is precisely the "enumerate the few surviving profiles" step of
the aimo-0146 template, but for our MULTI-constraint (superincreasing) version, and no one has yet
run the exchange-smoothing argument itself (only vertex LP enumeration) — the smoothing argument is
the natural NEXT step, and looks tractable: within each dyadic group, smoothing is a same-group
transfer (1-D, exactly as in aimo-0146); cross-group interaction is controlled because group sums are
FIXED and superincreasing (2^j > Σ_{i<j}2^i), so a smoothing move can never make a lower group
"compete" with a higher one for value — this is exactly the mechanism ONE-REC already certified
(single-excursion per scale), now repurposed as a MONOTONE-DIRECTION argument (does the exchange
strictly increase L_T, hence WLOG smooth away from any non-canonical vertex without decreasing L_T)
rather than as a facet-counting argument (where ONE-REC was refuted as "non-binding," R12).

**Recommendation:** hand the outliner an approach that runs a **same-group exchange-smoothing
argument, group by dyadic group**, proving each smoothing move is weakly-L_T-increasing (in the
direction toward the canonical ATT-style profile) subject to the order/box constraints remaining
feasible, terminating at a FINITE set of canonical profiles which are then checked directly (as in
aimo-0146). This is NOT vertex enumeration (which stalled past n=4) and NOT the refuted ONE-REC
facet-counting; it is a genuinely new, third framing on the SAME certified reduction (VERT-LOW/BLK),
with concrete small-n numeric support (the ±1/2 dual-multiplier sparsity above) that it should
generalize. Flag as CONJECTURE, not proof — needs a builder to actually run the smoothing induction
and check it does not lose the "−1" the way earlier crude bounds did (same failure risk the
outline-reviewer has repeatedly flagged).

**Cheap kill to run before committing a builder:** exhaustively check, for n=5 (per the standing R13
gate), whether the LP-dual sparsity pattern (exactly one binding order-inequality with multiplier 2,
plus ±1 equality multipliers) holds for EVERY type/word, using `scipy.optimize.linprog` dual output
(`res.ineqlin.marginals`, `res.eqlin.marginals`) — this is a fast, decisive numeric gate (minutes, not
hours) that would either strongly de-risk the smoothing mechanism or kill it before a builder invests
in the induction.

---

### UPPER wall (first-gap pigeonhole `min_{∅≠T} descKK(T) ≤ u_n`): does LP duality help?

**Finding: LP duality does NOT naturally apply here — this is an EXISTENCE claim, not a min-over-a-
polytope inequality.** The upper-wall target is "some subset T has small value," i.e. an upper bound
on a MINIMUM over a finite (not polytope-continuous) combinatorial family of subset values. Farkas/LP
duality certificates prove LOWER bounds on minima over convex regions; they do not directly produce
existence-of-a-small-value witnesses over a discrete family. Forcing an "LP-duality" framing onto the
upper wall would be a category error — I flag this honestly rather than manufacture a fake analogy.

**The natural LP/duality-flavored ANALOGUE for an upper (existence) bound is an averaging/expectation
argument:** define a natural probability distribution (or just a finite explicit family with known
size) over subsets T of the reachable-word positions, compute E[descKK(T)] (or a suitable signed
analogue) in closed form using the SAME group-sum/dyadic structure as the lower wall, and conclude
some T attains ≤ the average ≤ u_n. This is genuinely different from all 5 dead upper families
(covering-radius ×2, density/COUNT, greedy recursion R9, bounded-depth escape R10, mass-telescope
discrepancy R13 — this round's gate refuted BOTH the SEED(p) induction AND GAP-TELE structurally,
via the exact inequality Σ_i dist(a_i,R_{i−1}) ≤ a_1(2−2^{-n}) < 2a_1, certified as new Lemma DSUM).
Averaging is NOT charging against Σa_i (which DSUM shows is structurally the wrong direction — the
distance-sum is bounded ABOVE by <2a_1, not below); instead it would directly bound an EXPECTATION
of the target quantity itself over an explicit combinatorial ensemble, sidestepping DSUM's obstruction
entirely since it never sums distances-from-below.

**No crux-corpus analogue found that is a close match for this specific averaging idea** (searched
`combinatorics`/`probabilistic-method` and `games-and-strategy` — nothing directly on "expectation
over a reachable/tree-realizable subset family bounds its minimum," see below).

---

### Corpus search notes (domain-filtered, per crux_moves_documentation.md field names)
- `combinatorics` × `games-and-strategy` (39 cruxes): scanned all. None resemble a continuous
  claiming/alternating-sum game with an LP-duality or minimax-value target; they are almost all
  discrete pairing/parity/potential strategies on finite boards — not a new lever for either wall.
- `combinatorics` × `linear-algebra-method` (16 cruxes): mostly F_2-linear-system / dimension-counting
  (aimo-0050, aimo-0441, aimo-0542) — not analogous (our polytope isn't over a finite field).
- `combinatorics`/`algebra` × `extremal-principle` (166 cruxes, scanned first ~30 + targeted
  `aimo-0146`): **`aimo-0146` is the strong match** (see above — exchange-smoothing of a linear
  functional over a sorted sequence with sum constraints, reduce to few candidates, verify directly).
  `aimo-0114` ("hand the adversary one specific extremal configuration and read a parity obstruction
  straight off it") is the same flavor as our already-certified Lemma ATT (an explicit witness) —
  confirms ATT's shape is the standard move, not a new lever.
- `probabilistic-method` (algebra/combinatorics): did not find a crux specific to "expectation over a
  tree-realizable/reachable subset family bounds a min" — the averaging idea above is proposed fresh,
  not corpus-retrieved; label it as a fresh proposal, not a validated crux-adapted move.

---

### Distinct openings (for the outliner to choose from)
1. **[STRONGEST, LOWER]** Same-group exchange-smoothing (aimo-0146-style) on GAP-EXTR, proven to be
   the same mechanism as the observed sparse LP-dual certificate (±1 equalities, single ×2 order
   slack) — concretely supported by 3 hand-computed types at n=3; cheap n=5 gate proposed above.
2. **[LOWER, weaker/parallel]** Direct LP-dual-certificate search (skip the smoothing narrative,
   just search computationally for the (y,z) Farkas multipliers per type and try to spot a
   closed-form pattern in y,z as a function of the type's block structure) — the outline-reviewer's
   own "opening 4" from R13, now de-risked by the 3-instance check above.
3. **[UPPER, fresh]** Averaging/expectation argument over an explicit reachable-subset family,
   replacing the now-fully-dead mass-telescope-discrepancy family (DSUM shows the sum-charging
   direction is structurally impossible) — genuinely new, not yet attempted in any of the 5 dead
   upper families.
4. **[REJECTED as a framing]** A single joint LP/minimax duality argument proving BOTH walls from one
   calculation — does not fit the problem's shape (existence vs. universally-quantified-min are
   different logical forms); do not chase this as literally "one certificate for both."

### Cheap-kill candidates
- LOWER: exact-fraction LP-dual sparsity check at n=5 across all types/words (minutes; scipy HiGHS +
  exact rational re-verification, same tooling already used for the n=3/4 cheap-kill).
- UPPER: before building the averaging argument, compute E[descKK(T)] over the ESF-1/ESF-2 certified
  tree-realizable subset families at n=2..6 numerically and check it tracks ≤u_n (or find the right
  ensemble by trial) — a fast numeric probe before committing to a proof attempt.

### Knowledge-base entries to use
- No `knowledge_base.md` entry named "LP duality" or "Farkas" was found (grepped `duality`,
  `linear program`, `minimax`, `saddle`, `extremal`, `convex` — only generic "extremal principle" /
  "pigeonhole" boilerplate, no LP-specific entry). The Fundamental Theorem of Linear Programming
  (linear functional on nonempty compact polytope attains min at a vertex) is already invoked and
  certified as Theorem VERT-LOW / Theorem VERT — cite those, do not re-derive.

### Analogous past problems (cruxes)
- **`aimo-0146`** (algebra, extremal-principle) — exchange-smoothing of a linear functional over a
  sorted sequence under sum constraints, reduce to few extremal profiles, verify directly. Strong
  structural match for GAP-EXTR's remaining step (generalize BLK's block-structured vertex to a
  proof, not just a numeric check at n≤4).
- `aimo-0114` (extremal lower bound via one explicit witness) — same shape as already-certified
  Lemma ATT; not new, confirms the existing witness technique is standard/correct, no fresh lever.
- No close analogue found for the upper wall's averaging idea — flagged honestly as a fresh proposal.

### Prior progress
- LOWER: VERT-LOW + BLK + ATT certified (loss-free reduction to GAP-EXTR: min L_T≥1 at every vertex
  of every type's polytope P_T). Cheap-kill passed n≤4 (no sub-1 vertex). GAP-EXTR itself open for
  general n.
- UPPER: FGR + R-COV' (sufficiency) certified; residual = first-gap pigeonhole
  min_{∅≠T} descKK(T) ≤ u_n (0 exact fails, worst ratio 0.75-0.80, tight at dyadic ladder). R13's two
  proposed levers (SEED(p) induction, GAP-TELE mass-charging) BOTH refuted this round (structurally,
  not just a loose constant) — new certified Lemma DSUM: Σ_i dist(a_i,R_{i-1}) ≤ a_1(2-2^{-n}) < 2a_1
  (the WRONG direction for any sum-charging argument).

### Dead ends (do not retry)
- Covering-radius (one-cap R10, two-cap R12): whole family dead, saturates 3-5×u_n.
- Density/COUNT pigeonhole (R11): dead, all-equal valley gives |R|=2.
- Fixed/bounded-depth escape (R10), greedy recursion (R9): dead.
- SEED(p) seeded induction + GAP-TELE mass-telescope-discrepancy (R13, this round): dead — SEED(p)
  overshoot grows with p in every parametrization tried (up to 9.77× at p=6); GAP-TELE is
  structurally impossible (Lemma DSUM shows the distance-sum is bounded ABOVE by <2a_1, the wrong
  direction for a sum≥threshold argument).
- Structured transport/matching (R11), scalar-reserve/potential (R9-10), prefix/termwise monovariant
  (R8), f-partition single-gap localisation (R12): all dead, all lower-wall.
- ONE-REC as a binding facet/lever (R12): refuted non-binding for vertex enumeration — but NOTE this
  is compatible with using ONE-REC's underlying single-excursion FACT as a monotone-direction argument
  inside the smoothing mechanism above (different use, not "ONE-REC-tightness" as a facet).

### Small-case / intuition notes (CONJECTURE, not proof)
- The LP-dual certificates computed at n=3 (3 independent hand-built types, both tail-cut and
  tail-uncut) are uniformly sparse: exactly one nonzero order-inequality multiplier (value 2) plus
  ±1 equality multipliers. This is suggestive but only 3 data points — the mandated cheap-kill (n=5,
  all types) should be run before a builder commits to writing this as a full proof.
- The "single binding constraint" pattern is consistent with BLK's own count (≤n+3 distinct values at
  a vertex — few active constraints), so it is not a surprising finding, but it is a NEW way to
  extract a proof from that structure (certificate/smoothing vs. enumeration), which is what makes it
  a genuinely different lever, not a restatement.
