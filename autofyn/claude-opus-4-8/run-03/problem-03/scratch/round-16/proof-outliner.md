## imo-2026-03

Two walls, both `partial`. UPPER boundary layer CLOSED exactly (certified Lemma WTC); UPPER deep
interior `a₁ < (L−u_nL)/2` and the entire LOWER wall (GAP MID-core / GAP-EXTR) remain open. The
field below keeps the two walls FAR APART in framing (single-gap-trap rule): a subset-selection /
reachable-value discrepancy object on the UPPER side, a block-parity counting object on the LOWER
side. No dead-family leader is re-nominated.

**Pre-build gate I ran this round (decisive, saves a builder).** The dispatch asked me to encode the
explorer's decimated/alternating-subsequence opening as breakpoint-vertex's make-or-break with a
cheap gate BEFORE full build. I ran that gate (exact `Fraction`, adversarial deep-interior profiles
`a₁<(L−u_nL)/2`, n=4,5,6, /tmp/dec_probe*.py). RESULT — the decimated lever, and every poly-size
structured selection family, is REFUTED as a provable mechanism:
- AP-index decimation `{a_i, a_{i+d}, …}`: worst `min descKK / u_n = 1.90 / 3.09 / 4.17` (n=4,5,6) — grows with n.
- contiguous index blocks: worst `1.06 / 1.29 / 1.50` — grows with n.
- bounded-deletion caterpillars (drop ≤1, ≤2 elements): worst `3.5/4.8/8.2` and `2.4/2.9/3.5` — grows with n.
- true `min over ALL nonempty subsets`: worst `0.59 / 0.47 / 0.40` (margin genuine, improving with n),
  and the arg-min subset size is spread across ALL sizes 1..n+1 (no bounded/structured shape).

So the deep-interior residual genuinely requires an UNRESTRICTED subset of unbounded shape; no fixed
selection family realises `u_n`. The decimated opening is PRE-KILLED — the builder must NOT be sent
to construct it. This matches the R9–R11 pattern (greedy/bounded-depth escape needs depth Θ(n)). The
consequence re-plans breakpoint-vertex's make-or-break from "construct a decimated subset" to "prove
a NON-constructive margin-tolerant EXISTENCE bound," below.

---

### breakpoint-vertex: advance (re-planned make-or-break for the DEEP interior only)

Target: for every n, minimax `D = u_n = 1/(2^{n+1}−1)` (⇒ `c(n)=2^n/(2^{n+1}−1)`) — the whole
problem. This slug owns the UPPER bound; boundary layer + dominant regime are already closed
(certified whole-tail-peel + Lemma WTC). Only the deep interior `a₁ < (L−u_nL)/2` is open.

Technique (re-planned): a NON-constructive, margin-tolerant EXISTENCE bound on the tree-realizable
reachable set — proven by a discrete intermediate-value / exchange argument that exploits the deep
margin, NOT by exhibiting a subset (all constructive families pre-killed above). Spine: certified
Lemma BL (unique first crossing of `a₁` by descending partial sums) + certified WTC two-sided
invariant `a₁−P_k ≤ v_k ≤ |a₁−P_k|`, used for EXISTENCE not construction.

Skeleton (deep interior `a₁ < (L−u_nL)/2`, i.e. `|2a₁−L| > u_nL`, L=1):
  1. Import certified R-COV'(sufficiency) + FGR: suffices to show `Φ(A)=min_{∅≠T} descKK(T) ≤ u_n`. — done/certified.
  2. Import certified BL: the descending survivor partial sums `P_0<…<P_{n+1}=L−a₁` cross `a₁` at a
     unique index `k*`; the crossing residual `r = |a₁ − P_{k*}| < a_{k*} ≤ a₁`, and `r < s := a_{k*+1}`
     (the next gap). — certified.
  3. **[GAP — make-or-break] EXISTENCE lever.** Show that in the deep interior the reachable set
     `R_{n+1}` (tree-realizable signed subset sums, certified RL) contains a point in `[0, u_n]`,
     via a discrete-IVT/exchange: the residual `r` from step 2 lies in a window of width `< a_2`;
     because `a₁ < (L−u_nL)/2` there are ≥ 2 further comparably-sized pieces below the crossing
     whose inclusion toggles the residual by amounts each `≤ a_2` and whose partial toggles SPAN an
     interval of length `≥ r` around 0 — so some signed toggle lands the residual in `[0,u_n]`. The
     margin (`true-min ≤ 0.6 u_n`, non-vanishing) is the slack this existence step spends; it is
     NOT a covering-radius (no per-level radius), NOT a density/COUNT (no injectivity), NOT a
     bounded-depth escape (the toggling set is unbounded), NOT a greedy recursion (existence, not a
     policy), NOT a mass-telescope, NOT extremal-tie.
Key lemmas (claim + mechanism):
  - *Existence-toggle lemma (the GAP)* — because the deep condition `2a₁ < L − u_nL` forces the tail
    below the crossing to have total mass `> a₁ + u_n`, the set of achievable signed toggles of the
    residual `r` is `u_n`-dense on `[−r, r]` (discrete IVT on a chain of ≤ n toggles each `≤ a_2`,
    with a step `≤ u_n` guaranteed by the crossing structure), so `0`-neighbourhood `[0,u_n]` is hit.
    THIS IS UNPROVEN and is the honest deep-interior crux — it is an existence/discrepancy statement,
    the same one open since R7, now with the correct read that no constructive family can witness it.
Open gaps: step 3 (the existence-toggle lever) — the sole open deep-interior crux.
Cases to cover: deep interior only (`a₁ < (L−u_nL)/2`); boundary + dominant already closed.
Watch out for: (a) do NOT let step 3 degrade into a per-level covering radius, a density/COUNT
injectivity, a bounded-depth escape, or an extremal-tie perturbation — ALL dead. (b) the toggle-step
`≤ u_n` guarantee is where the argument can silently fail (the true min uses unbounded shape) — the
builder MUST re-run my exact gate on the SPECIFIC toggle chain before prose; if the guaranteed step
exceeds `u_n`, report and STOP (no fake proof). (c) VALLEY-TIGHT's no-margin ban does NOT apply here
(boundary layer only), so a non-tight `[0,u_n]`-window existence bound is admissible.

Pre-build gate (MANDATORY, before any prose): I already ran the family-selection gate (above) — it
KILLS all constructive families. The builder's remaining gate is on the existence-toggle STEP: on
adversarial deep n=4,5,6 profiles, verify that the chain of ≤ n residual-toggles built from the BL
crossing has (i) each step `≤ u_n` and (ii) partial toggles that span an interval of length `≥ r`
around 0 (so `[0,u_n]` is provably hit). If either fails, this lever dies like the constructive
families — report and STOP.

Honest status of this slug: its make-or-break is a genuine EXISTENCE crux with no constructive
witness; the reviewer may reasonably HOLD it from build this round (the constructive gate is already
resolved NEGATIVE) and route the round's build energy to the LOWER slug below, keeping
breakpoint-vertex live as the recorded UPPER vehicle with the decimated lever refuted.

---

### odd-block-counting: new (LOWER wall — a pure counting/pigeonhole on BLK's block structure)

Target: for every n, minimax `D = u_n` — the whole problem, via the LOWER bound `min_R D(R) ≥ 1`
over refinements `R` of the ladder `C_n` with ≤ n cuts (⇔ GAP MID-core: `μ{g odd} ≥ 1`, `|F|≥3`).
This is a NEW mechanism, far from all 8 dead lower levers (scalar-reserve/potential, structured
transport/matching, prefix/termwise monovariant, f-partition single-gap, vertex-polytope/LP-dual,
generating-function/transform, merge/budget-domination) and from route (A) (WTC-analogue, which the
explorer showed collapses to certified PEEL) — it is a direct extremal COUNT on the finite
block-structured vertex set certified by Lemma BLK, with NO duality, NO potential, NO matching, NO
transform, NO merge.

Technique: pure counting / pigeonhole. Spine: certified VERT-LOW (min D at a polytope vertex) +
certified BLK (≤ n+2 distinct positive block-values at a vertex) + the certified vertex-native
identity `L_T = alternating sum (descending) of the ODD-multiplicity distinct block values` (Lemma P:
even-multiplicity blocks are cancelling pairs, net 0) + the integer-valuedness of `g = N_F − N_B`.

Skeleton (prove `min L_T ≥ 1` at every vertex):
  1. Import VERT-LOW + BLK: a minimizing refinement is a vertex; its `m` pieces form `p ≤ n+2`
     maximal equal-value blocks, grouped by dyadic scale with FIXED group sums (each dyadic band's
     total mass is the certified fixed value from ONE-REC / the ladder). — certified.
  2. Reduce the objective: `L_T = D(vertex) = μ{g odd}` where `g = N_F − N_B` is INTEGER-valued on
     `(0, 2^{n−1})` with `∫g = 1` (certified MID); equivalently `L_T = Σ_{i} (−1)^{i+1} v_i` over the
     odd-multiplicity distinct block values `v_1 > … > v_r` descending. — certified reformulation.
  3. **[GAP — make-or-break] The counting bound.** Let `r` = number of odd-multiplicity blocks. Prove:
     (a) a PURE COUNT bound on how many blocks per dyadic band can carry odd multiplicity, given the
     band's group sum is a FIXED integer power of 2 and the F-staircase `N_F` is monotone; and
     (b) that this count, combined with the fixed baseline staircase `N_B` (so the PARITY of `g` on
     each of the ≤ n+2 intervals is pinned up to the odd-block placement), forces
     `Σ_{c_k odd}(x_k − x_{k−1}) ≥ 1`, i.e. the odd-level set of the integer step function `g`
     carries mass ≥ 1. The mechanism is a parity-pigeonhole: because `∫g = Σ c_k Δ_k = 1` is a
     POSITIVE ODD-signature integral and `g` has only ≤ n+2 constant pieces, the even-level pieces
     (`c_k` even, contributing `0` to `μ{g odd}` but full mass to `∫g`) cannot absorb all of the unit
     integral without an odd-level piece of mass ≥ 1 sitting adjacent — the fixed dyadic group sums
     `Σ_band = 2^j` pin exactly where the even plateaus can sit, and a counting argument on odd-block
     placements shows a residual odd-mass ≥ 1 is unavoidable.
Key lemmas (claim + mechanism):
  - *Band-parity count (the GAP)* — because on each dyadic band the fixed group sum `2^j` is EVEN for
    `j≥1` while the ladder baseline `N_B` is a FIXED known parity staircase, the number of
    odd-multiplicity blocks a band can host is constrained mod 2 by `2^j` and the F-monotonicity; the
    UNIQUE band forced to odd total parity (the one carrying the `∫g=1` surplus, `|F|` odd ⇒ some band
    unbalanced) must contribute an odd-level interval of mass ≥ 1. This is a counting statement on the
    finite BLK block set, NOT an LP-dual certificate and NOT a running potential.
Open gaps: step 3 (the band-parity count) — the sole open crux; equivalent to GAP MID-core for `|F|≥3`.
Cases to cover: `|F|≥3` (|F|=2 and 0≤g≤1 already closed inside MID); across all ≤ n+2 block counts.
Watch out for: (a) HIGH RISK it degrades into vertex ENUMERATION (dead #5, LP-dual/vertex-polytope) —
the count MUST be a scale-by-scale parity/pigeonhole inequality, never "search the vertices"; if the
only proof is enumeration, it is the dead framing in disguise — report and STOP. (b) the pure-integral
version is FALSE (`g≡2` on measure 1/2) — the dyadic group sums `2^j` and the ladder-fixed baseline
parity are LOAD-BEARING and must be used explicitly, not dropped. (c) non-integer vertices exist (R12),
so do NOT route through "`L_T` is an integer" — use the integer-valuedness of `g` (counts), which
holds at every vertex regardless of breakpoint values, NOT integrality of the block values `v_i`.

Pre-build gate (MANDATORY, before any prose, cheap — reuse existing data): enumerate the n=3,4,5
vertices already produced by merge-interleave's LP cheap-kill (or re-enumerate integer refinements of
`C_n` with ≤ n cuts). For each vertex compute: number of odd-multiplicity blocks `r`, the per-dyadic-
band count of odd-multiplicity blocks, and check whether a CLEAN extractable inequality holds —
specifically: is there always a UNIQUE band (or a pinned-parity band) whose odd-level mass alone is
≥ 1, and does "number of odd blocks per band mod 2" obey a closed rule pinned by the group sum `2^j`?
If NO clean per-band counting inequality emerges (i.e. odd-mass ≥ 1 requires cross-band cancellation
that only the global alternating sum sees), the counting lever collapses to MID-core restated —
report the collapse and STOP (do NOT dress it as a proof). If a clean per-band rule DOES emerge,
build it.

---

## Build set nomination

- **odd-block-counting** (NEW, LOWER) — PRIMARY build target. It is the one genuinely-untried lower
  sub-lever (route (B)'s BLK-odd-multiplicity count), far from all 8 dead lower levers, with a cheap
  mandatory pre-build gate that reuses existing n=3,4,5 vertex data (fails fast if it collapses to
  vertex enumeration or to MID-core restated). Highest-value shot at the wall that has had no live
  vehicle since R14.
- **breakpoint-vertex** (ADVANCE, UPPER) — nominate for build ONLY IF the reviewer wants the
  existence-toggle gate run; its constructive families are already gate-refuted by me this round (the
  decimated opening is PRE-KILLED, recorded above), so its remaining make-or-break is a
  non-constructive existence crux. The reviewer may instead HOLD it and keep it live as the recorded
  UPPER vehicle (boundary layer closed; deep interior isolated with all constructive levers refuted),
  routing this round's build energy to odd-block-counting. I recommend: build odd-block-counting;
  hold breakpoint-vertex build pending the existence-toggle gate, with the decimated-lever refutation
  recorded in its approach file so no future round re-tries a constructive selection family.

Rationale for a tight 2-slug field (not 3–5): both walls have been shown (R11 role-memory, R14)
to have NO far-apart second vehicle per wall; a third slug on either wall would share its wall's
single gap (single-gap-trap). Breadth here comes from the two walls being genuinely far apart in
mechanism (reachable-value existence discrepancy vs dyadic block-parity count), not from slug count.
