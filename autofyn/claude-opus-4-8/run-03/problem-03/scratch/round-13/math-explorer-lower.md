## imo-2026-03 (LOWER wall: GAP-EXTR, lens = vertex characterizations / combinatorial LB over polytope vertices)

### Recap of exactly where the wall sits (certified, not to re-derive)
- Lemma **VERT-LOW**: MID-core (D(S)≥1 for |F|≥3 residual) is loss-free equivalent to **GAP-EXTR**:
  for every combinatorial type T = (|F|, (k_0,…,k_{n-1}), σ) and every vertex v of the polytope
  P_T (variables = piece values; constraints (E) n+1 group-sum equalities ΣF=2^n, Σgroup_j=2^j;
  (O) descending order fixed by σ; (C) box 0≤v_i≤2^{n-1}), the alternating functional
  L_T(v) = Σ_odd v − Σ_even v ≥ 1.
- Lemma **BLK**: at a vertex, the m coordinates take ≤ n+3 distinct values (≤ n+2 positive) — active
  rank count: (n+1) group-sum equalities always active (disjoint supports ⇒ full rank n+1) + tight
  order-ties (m−p of them, p = #distinct-value blocks) + ≤2 box faces (top cap 2^{n-1}, bottom 0).
- Lemma **ATT**: tight family B=C_{n-1} uncut, F={2^{n-1},…,2,1,1} gives D=1 for all n (cancelling
  pairs at each dyadic scale + a residual triple of 1's) — confirms the target is exactly 1, not more.
- Cheap-kill exact LP (scipy HiGHS): min L_T = 1, no sub-1 vertex, for n=3 (5 F-types) and n=4
  (21 F-types), independently reviewer-reproduced on finer rational grids. **ONE-REC is refuted as a
  binding facet** — do not reintroduce it as a lever (R12 finding, confirmed correct: two fragments
  of one dyadic group exceeding half the group sum is already excluded by (E)+positivity, so it
  restricts realisable words, not P_T itself).
- Two shortcuts refuted: D not constant across words (Case (a): D=2^{n-1}); D not always integral at
  a vertex (132 non-integer vertices at n=3, all with D>1, so "prove D∈ℤ" is a dead lever).

### Distinct openings for GAP-EXTR (general n)
1. **Vertex-level peel / induction on n directly on P_T.** BLK shows the box contributes at most 2
   active constraints; a vertex either (a) touches the top box face (some coordinate =2^{n-1}) or
   the bottom face (some coordinate =0), or (b) is "generic" (rank exactly n+1 from (E) alone plus
   m−(n+1) tie-constraints, i.e. p=n+1 distinct values). Case (b) is the maximal-tie / most-degenerate
   regime; case (a) is where a coordinate collapses to a dyadic-scale value or to 0, which should let
   you literally delete that coordinate (0-value pieces contribute nothing; a coordinate pinned at
   2^{n-1} matches the top-band decomposition already certified as Lemma TB) and recurse to a vertex
   of a smaller-n polytope. This is the natural place to try a genuine **vertex-restricted PEEL**
   (parallel to certified Lemma PEEL/TB but staying inside the finite vertex family, not the whole
   continuum) — potentially avoids re-deriving the ∫g=1 aggregate machinery that stalled the MID
   route for 5+ rounds.
2. **Generic-vertex (case (b), p=n+1) exact characterization.** When rank is saturated purely by
   (E)+ties (no box), the n+1 blocks are forced into a very rigid combinatorial shape: each block's
   value must simultaneously satisfy several group-sum equations (a block can straddle multiple
   dyadic groups only if members from different groups coincide numerically). This is a genuinely
   FINITE, name-able object — worth asking whether generic vertices are *exactly* the "one
   fragment per dyadic level, tail uncut" canonical layouts (the ATT family and its permutations),
   in which case L_T ≥ 1 might follow from a direct telescoping/superincreasing argument specific
   to that shape, with the degenerate (box-touching) vertices handled by the induction of opening 1.
3. **Local-exchange / minimal-counterexample-among-vertices argument** (the aimo-0333 pattern, see
   corpus below): assume a global minimizer vertex v* over ALL types T and ALL n with L_{T*}(v*) < 1;
   since the vertex family is finite for each n, WLOG take n minimal. Use the active-constraint
   structure (BLK) to find a *feasible swap* — e.g. move mass between two tied coordinates in the
   same dyadic group, or between a group-j coordinate and a group-j' coordinate under a
   value-coincidence tie — that changes L_T by an exactly computable amount, and derive either a
   contradiction with v* being extremal/minimal, or a reduction to a strictly smaller n (closing by
   strong induction). This mirrors the aimo-0333 crux: "pigeonhole-repeated block swapped for copies
   of a designated extremal block, preserving feasibility, and optimality forces an equality" — here
   the designated block would be the dyadic unit at the bottom (value 1) or the top block (2^{n-1}).
4. **LP-duality / explicit certificate.** Since the cheap-kill is an exact LP for small n, extract
   the dual (shadow prices / active-constraint multipliers) at the worst-case vertices for n=3,4 and
   look for a pattern (e.g. multipliers equal to inverse dyadic weights, or telescoping coefficients)
   that could be written down explicitly and verified as a valid dual feasible point for general n
   (a genuine LP-duality proof of L_T≥1, i.e. exhibit λ_E, λ_O, λ_C ≥0 with Σλ·(constraint) ≤ L_T − 1
   identically). This is a concrete, checkable probe a builder could run computationally before
   attempting the general argument by hand — flagged as untried in the current record.

### Cheap-kill candidates (structural, before heavy work)
- **Block-length-parity count.** Within a vertex, a block of *even* length contributes exactly 0 to
  L_T (equal values cancel in pairs at consecutive odd/even positions — this is exactly Lemma P's
  cancelling-pair mechanism, already certified). So L_T is a sum over the ODD-length blocks only,
  with sign alternating by the parity of the block's starting position. Since p ≤ n+3 (BLK), there
  are at most n+3 blocks total; the number of odd-length blocks has the same parity as m (mod 2) —
  a cheap parity/counting fact worth checking as a first filter on which block-patterns can even be
  candidates for L_T<1 (this is essentially re-deriving Lemma M's μ{odd} content in the finite
  vertex setting — flag: may just recreate the MID-core content in new language, not a genuine
  shortcut, so treat as a sanity lens, not a standalone lever).
- **Mass/size bound per block.** Because group sums are fixed (ΣF=2^n, Σgroup_j=2^j), a block that
  straddles k distinct dyadic groups has its value pinned to a sub-sum of the geometric ladder — a
  quick size argument (superincreasing property: 2^j > Σ_{i<j}2^i) may immediately rule out most
  cross-group ties as infeasible, pruning the combinatorial search space for opening 2 without new
  machinery. Worth a computational pass but not yet done.

### Knowledge-base entries to use
- No dedicated polytope/LP-vertex entry in `knowledge_base.md`; the closest generic entries are
  **Pigeonhole / extremal principle** and **Extremal graph theory: decompose the vertex set
  dyadically / by levels and pigeonhole within a level** (knowledge_base.md line 111-112) — this
  "dyadic-level decomposition + pigeonhole" phrasing matches exactly the shape of opening 1/2 (peel
  by dyadic scale, pigeonhole within a level's block structure). No SOS/majorization/rearrangement
  entry directly named, but the general **Invariants & monovariants** entry is the closest match to
  opening 3's exchange-argument flavor.
- The **Fundamental Theorem of LP** (linear functional on nonempty compact polytope attains min at a
  vertex) is already the backbone of certified VERT-LOW/VERT (upper wall); no further KB entry needed
  for that half.

### Analogous past problems (cruxes)
- **aimo-0333** (Iran, algebra/sequences-and-recurrences, subtopic tags `exchange-argument`,
  `extremal-ratio-normalization`): superadditive recurrence a_n=max_k(a_k+a_{n-k}) unfolds into a
  maximum of a LINEAR functional over compositions of n into bounded parts (exactly our situation:
  D/L_T is linear over a combinatorial family of "words"/compositions). The crux move — normalize by
  the extremal per-index density ratio a_i/i, designate the maximizer ℓ as a privileged block, then
  use an **exchange argument**: pigeonhole-repeated block j (appearing ≥ℓ times in an optimal
  composition) is swapped for ℓ copies of the designated block, preserving the sum and feasibility,
  and optimality of the original forces the exchanged composition to also be optimal, giving an
  equality a_j/j = a_ℓ/ℓ. This is the closest genuine analogue to opening 3 above: "optimal/extremal
  discrete structure constrained by a linear-in-composition objective, cracked by swapping a
  repeated block for copies of a designated extremal one." Worth reading in full if opening 3 is
  picked up (`aimo-0333` in `past_problems_database.json`).
- **aimo-0459** (Taiwan, algebra/inequalities-SOS-and-convexity): bounds a cyclic sum of a sorted
  4-tuple by re-pairing via rearrangement into extreme (smallest-with-largest) pairs. Weak analogue
  only — our alternating sum is over a FIXED descending order (not a free rearrangement), so
  rearrangement inequality itself doesn't directly transfer, but the "pair extremes across an
  excursion" flavor is suggestive for opening 3's swap move. Judged partial-fit, not a strong match.
- **aimo-0800** (Ukraine, combinatorics/extremal-principle, convex-polygon good-triangles): a
  double-counting/charging argument bounding an extremal count via "extreme constituent" charging.
  Structurally different (geometry, not a linear functional over a combinatorial polytope) — judged
  NOT genuinely analogous; mentioned only because it surfaced under the "extreme point" keyword
  search, flagged here so it is not mistakenly chased.
- No corpus problem was found that is literally "min of a linear functional over vertices of an
  explicit combinatorial/dyadic-ladder polytope ≥ target" — the closest true structural match is
  aimo-0333's linear-functional-over-compositions + exchange argument; the LP-vertex / polytope
  framing itself (Fundamental Theorem of LP as the driving tool) does not have a close corpus
  precedent, consistent with this being a genuinely constructed reduction rather than a textbook
  pattern.

### Prior progress
Vertex reduction (VERT-LOW) is rigorous and certified; block-structure bound (BLK, ≤n+3 distinct
values) is rigorous and certified; tightness (ATT, D=1 attained for all n) is rigorous and certified;
cheap-kill exact for n=3,4 (min=1, no sub-1 vertex). GAP-EXTR itself (general n) is open — it is
loss-free equivalent to MID-core, so no net progress on the actual inequality has been made beyond
reframing/sharpening the target to a finite block-structured family. No approach has yet used the
BLK-forced block structure to run an actual induction or exchange argument on the vertex family
itself (as opposed to on general refinements, which is what the parity-measure-potential and
induction-peel lineages tried and stalled on for 5+ rounds via MID/ONE-REC/aggregate-integral
machinery).

### Dead ends (do not retry)
- **ONE-REC-tightness as a binding facet** — refuted R12: it's implied by (E)+positivity inside a
  fixed P_T, not a separate constraint; do not resurrect as "the spread mechanism."
- **Integrality of D at a vertex** — refuted (132 non-integer vertices at n=3, all D>1).
- **D constant across words / "canonical value 1"** — refuted (D varies; Case (a) gives D=2^{n-1}).
- **Scalar-reserve / structured transport / Hall-matching lower levers (R10, R11 ballot-matching)** —
  these targeted the pre-vertex-reduction MID-core directly and are dead (prefix/suffix/interval-Hall/
  value-dominating all fail; the GAP-TERMINAL premise is false). They predate the vertex framing and
  are not levers on GAP-EXTR specifically, but their failure mode (no single scalar/local monovariant
  suffices, the target is irreducibly aggregate over the whole ladder) is a warning: any opening-3
  exchange argument likely needs to be genuinely GLOBAL (compare a full vertex to a full smaller-n
  vertex), not a single local swap producing a scalar inequality in isolation.
- **Aggregate-integral / measure route (∫g=1 vs μ{g odd}≥1, MID/ONE-REC lineage)** — not "dead" but
  stalled for 5+ rounds (R7-R11) on the same aggregate-compensation obstruction; the vertex framing
  (VERT-LOW/BLK) was introduced in R12 precisely to sidestep this stall by working with a FINITE
  object instead of the continuum measure. Any new approach should stay inside the finite vertex
  family (openings 1-4 above) rather than reopening the continuum aggregate route.

### Small-case / intuition notes (conjectural)
- n≤4 exact LP confirms min L_T=1 exactly, attained ONLY at the canonical dyadic-cancelling-pair
  layouts (ATT family and permutations thereof) — no other vertex ties or undercuts it in the
  n=3,4 data. This is consistent with opening 2's conjecture that generic (p=n+1, non-box-touching)
  vertices are exactly these canonical layouts, but it is UNVERIFIED for general n and should be
  treated as conjecture, not fact, until an explorer/builder checks n=5 computationally or proves it
  structurally.
- The block-length-parity mechanism (odd-length blocks alone contribute to L_T) combined with the
  superincreasing dyadic ladder strongly suggests an induction that peels the smallest dyadic scale
  (value 1) or the largest (2^{n-1}) first, since these are the scales where BLK's box-face
  constraints (v=2^{n-1} top, v=0 bottom) are most likely active — this is the intuitive justification
  for opening 1's vertex-restricted peel, but it has not been carried out or verified computationally
  this round.
