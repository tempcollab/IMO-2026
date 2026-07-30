## Status
partial

## Approaches tried
- (round 10, this build) **Generalized Lemma TWO-BLOCK to an arbitrary
  finite number `K≥1` of simultaneous, independent tie-clusters**, closing
  the round-9-flagged "multi-cluster" gap in full for the scope where each
  individual split piece has exactly 2 parts (any number of clusters, any
  distinct minority-role tie values, no ordering assumption needed between
  clusters). Rather than the round-10 outline's originally-planned
  "K-fold nested threshold peel" (which would need ordering `v_1>\cdots>v_K`
  and a multi-pair insertion lemma), found a strictly simpler route: a new,
  fully general, hypothesis-free **Lemma TOP2** (`D(L)≥b_1-b_2` for *any*
  sorted list, its two largest elements `b_1≥b_2` — a 2-line consequence of
  the already-certified Lemma D-BOUND, needing no threshold/Y-Z split, no
  parity case-split, and no relation between different clusters at all).
  Combined with a generalized **Structural Lemma** identifying the two
  globally-largest elements of the merged configuration for *any* `K`
  (extending round 9's single-cluster version), this reduces the entire
  K-cluster problem to the *same fixed 5-case analysis* that closed `K=1`
  — the only genuinely new case being two different clusters independently
  owning pieces `0` and `1` (`l(0)≠l(1)`), closed by the same load-bearing
  fact used for the `(1,0)` case (whichever cluster owns a piece must
  contain a *second*, `≥2`-indexed member, forcing its tie value below
  `t_2/2`, regardless of how many *other* unrelated clusters exist
  elsewhere). Both Lemma TOP2 and the Structural Lemma are proved in full;
  the Main Theorem (`D(B)≥t_n` for every `n≥1`, every `K≥1`, every disjoint
  cluster collection, every choice of minority-range tie values with no
  ordering assumption) is proved in full and independently stress-tested
  (`16,000` randomized trials, `n=1..8`, random `K` up to `⌊(n+1)/2⌋`,
  random cluster sizes 2–4, random per-cluster tie values) — zero
  violations of `D(B)≥t_n`, zero mismatches of the predicted `(b_1,b_2)`
  against the true two largest sorted elements. Certified to
  `lemmas/multi-cluster-two-block.md`. **Cross-check note (per this
  round's dispatch instruction):** `recursive-embedding-induction`'s
  parallel forest/multi-pair-insertion route to the same target had not
  yet been updated in this repo at the time this build ran (file unchanged
  since the round-9 commit); no completed sibling general theorem was
  available to cross-check against this round. This result should be
  cross-checked against the sibling's mechanism once it lands (e.g. on the
  `n=4,6` two-cluster witnesses already used in round 9's reconciliation),
  per standing protocol — flagged for the reviewer/next round. **Honest
  scope note (same caveat as round 9's TWO-BLOCK file, unchanged, not
  addressed this round):** a single piece split into `≥3` parts with more
  than one of *its own* coordinates independently tied at different values
  (a "doubly-tied `≥3`-part piece") is a structurally different scenario
  (one piece contributing 2+ free coordinates, rather than one free
  coordinate per piece across many pieces) not covered by this K-cluster
  result, which — like round 9's TWO-BLOCK — assumes each individual piece
  contributes at most one free/tied coordinate. Whether this scenario can
  even arise at a genuine vertex of the constrained polytope at all (as
  opposed to being ruled out entirely by the per-piece LP-vertex property
  underlying Lemma V'/V'-GEN) is not re-derived here. Full statement,
  proofs, and verification detail in `lemmas/multi-cluster-two-block.md`
  and the "Round 10" section below.
- (round 9, this build) **Closed the last-remaining "minority-part,
  deep-bracket" residue sub-case of gap (b)**, via an independent,
  genuinely distinct route from `recursive-embedding-induction`'s
  forest-extension attempt this round: a **direct two-block `D`-BOUND
  estimate at the tie value itself**, no tree/virtual-re-split machinery.
  **New Lemma TWO-BLOCK** (fully general, no geometric structure): for any
  sorted nonnegative list and threshold `v`, splitting into `Y` (`>v`) and
  `Z` (`\le v`), `D(\text{list}) \ge (b_1-b_2) - v\cdot[\,|Y|\text{ odd}\,]`
  where `b_1,b_2` are `Y`'s two largest elements — proved by a single
  double-application of the already-certified Lemma D-BOUND. **New
  Structural Lemma**: for the specific residual configuration (a subset `S`
  of `\ge2` pieces of `A_n`, each split into 2 parts with the tied value
  `v` playing the *minority* role in every one), the two globally-largest
  elements of the merged list are exactly `b_1=2t_1-\varepsilon_0 v`,
  `b_2=t_1-\varepsilon_1 v` (`\varepsilon_0,\varepsilon_1` indicating
  whether the top piece / `T_1` are among the split pieces) — proved in
  full by direct case analysis, not just checked. **Main Theorem**:
  combining these, `D(B)\ge t_n$ unconditionally for every `n\ge1`, every
  such `S`, and **every** legal `v` in the minority range (not just Lemma
  CROSS-TIE-AFFINE's `D`-minimizing endpoint — a strictly stronger, more
  direct result than what the round's plan asked for). Certified to
  `lemmas/two-block-residue-close.md`. **Independently verified**: `10,731`
  exhaustive small-`n` instances (`n=1..6`, every subset `S`, dense `v`
  grid) plus `21,600` randomized instances (`n` up to `12`, `v` pushed to
  within `0.1%` of its supremum) — zero violations; the `(b_1,b_2)`
  structural formula itself independently matched actual sorted output in
  `14,400` further randomized checks. **Mandatory reconciliation**: cross-
  checked against `recursive-embedding-induction`'s own cited numeric
  witnesses (`n=4` symmetric two-minority tie, `n=6` external-anchor-snap,
  `k=1,3,4`) — the structural formula and resulting bound reproduce those
  exact numbers with no disagreement. **Honest remaining scope note**: this
  closes the "all-minority, all-exactly-2-parts" tie scenario (which *is*
  the previously-open residual sub-case) for every `n`; a narrower edge —
  a single `\ge3`-part piece with more than one of its own coordinates
  independently tied at different values — is flagged but not separately
  checked this round (believed to reduce to the cases above by peeling one
  tied coordinate at a time, not verified as its own claim). Full detail in
  the new "Round 9" section below.
- (round 8, this build) **Attacked gap (b) (cross-piece tied free
  coordinates in `recursive-embedding-induction`'s Lemma V'-GEN) via an
  independent mechanism: explicit two-variable affine-slope computation on
  the D-INSERT cell**, per this round's outline assignment (a deliberate
  second, structurally different route to the same sub-gap
  `recursive-embedding-induction` is also attacking this round via
  tree-peeling/shared-block combinatorics). **Result: proved a new, fully
  general Lemma CROSS-TIE-AFFINE** — for any cluster of `k≥2` mutually tied
  free coordinates from different split pieces, `D` restricted to the tie
  parameter is *affine* with an explicitly computable integer slope, so the
  tie is never a *strict* local minimizer: pushing the shared value to the
  boundary of the affine cell weakly decreases `D`. Proved a genuinely new
  structural fact (not previously on file) that makes the "aligned" case of
  this reduction land exactly on an anchor-only configuration: because every
  piece total in this problem is of the form `t_i` or `2t_1` and `t_i =
  2t_{i+1}` always (Lemma S), a 2-part-split piece's own "self-meeting"
  point (where its two parts become equal) is *always itself an anchor* —
  so whenever the tie-breaking direction hits this internal boundary before
  any external one, the result is a fully anchor-resolved configuration
  with **zero residue**, closing that whole sub-case unconditionally.
  **Honest remaining gap:** when the tied coordinate is playing the role of
  the *minority* (smaller) part of a 2-part-split piece, in a bracket
  strictly deeper than that piece's own natural halving level, pushing to
  the *external* anchor boundary can leave the companion part at a
  fixed-but-not-anchor value (a genuinely new residue phenomenon this round
  identified, not present in the narrower Proposition K / Lemma FC setting)
  — this sub-case is not fully closed; one numeric probe (`n=5`) found the
  affine slope identically `0` there (non-competitive, far above `t_n`),
  consistent with but not a proof of it being harmless in general. This
  substantially sharpens gap (b) (from "any generic cross-tie" to this one
  precisely isolated residue sub-case) and independently confirms, via a
  structurally different mechanism, that `recursive-embedding-induction`'s
  parallel conclusion (ties reduce, weakly, toward anchor-only) is correct
  and not an artifact of their own machinery — no disagreement between the
  two routes was found. Full details below in "Round 8" section.
- (round 6, this build) **Proved the "one free coordinate" vertex case of
  Lemma V' in full, for every `n≥1`**, per this round's re-scoped
  assignment (the exchange-move route being a confirmed dead end, and the
  `k<n` tail-refinement gap now owned by `recursive-embedding-induction`).
  This was the last uncovered case of Lemma V's vertex reduction — the
  pure-anchor case was already closed by Lemma PARITY-PAIR/Lemma L
  (`recursive-embedding-induction`, round 5). **Method:** no new machinery
  — a direct composition of two already-certified results. Lemma D-INSERT
  shows `D(S∪T)`, as a function of the single free coordinate `x` with the
  other `n` coordinates pinned, is *affine* on the interval between the two
  anchors bracketing `x` (fixed insertion rank throughout that interval).
  The two endpoint values of that interval are literal Lemma-PARITY-PAIR
  instances (snapping `x` to either bracketing anchor produces a
  pure-anchor configuration with `n+1` total marks, which *automatically*
  satisfies PARITY-PAIR's hypothesis — `n+(n+1)=2n+1` is always odd, with
  **no** dependence on the value constraint). Convexity of an affine
  function on an interval then gives `D(S∪T) ≥ min` of the two endpoint
  values `≥ t_n`. One edge case (`x` between `0` and `t_n`) is shown
  **vacuous** by an integrality argument (`x` is always an integer in the
  normalized coordinates, and no integer lies strictly between `0` and
  `t_n=1`); the other edge case (`x>t_1`, no upper anchor) is handled by
  monotonicity using only the single lower endpoint. **Result: Proposition
  K (the `k=n`, tail-untouched sub-case of the lower bound) is now fully
  proved for every `n≥1`, not merely its pure-anchor part** — this closes
  the entire sub-case, combining with Lemma L/PARITY-PAIR and Lemma V'.
  Every step (the D-INSERT decomposition, both endpoint PARITY-PAIR bounds,
  the vacuity of the `(0,t_n)` case, and the final inequality) was
  independently re-verified by exhaustive exact-`Fraction`/exact-integer
  enumeration of all `18,283` one-free-coordinate feasible points for
  `n=3,...,9` (zero violations; `n=1,2` have no such points, consistent
  with those being fully closed by earlier base-case work). Certified to
  `lemmas/lemma-V-prime-free-coordinate.md`. **What remains for the overall
  conjecture:** Proposition K only covers `k=n` with the tail untouched;
  the genuinely open gap is now squarely `k<n` with the tail
  *simultaneously* refined — `recursive-embedding-induction`'s
  PARITY-PAIR-GEN target, not attempted here.
- (round 5, this build) **Attacked the general doubling-family conjecture
  (`k≥2`, the shared lower-bound gap) via a single-unit exchange/local-move
  argument on the composition vector**, exactly as scoped by this round's
  outline. Per the outline-reviewer's coordination directive, first derisked
  numerically. Result: **the specific exchange mechanism proposed in the
  outline does NOT work as stated** — a genuine, rigorously verified
  negative finding, not a shortfall of effort. Full details in the "Round 5"
  section below. Summary: (a) proved a new, fully general **Elementary
  Exchange Move lemma** — the unique (up to sign/scale) minimal integer move
  on 3 anchor-multiplicities that preserves both of Lemma L's linear
  constraints (count and value), together with its **exact** algebraic
  effect on the alternating-sum invariant `D` (`ΔD = ±t_i` exactly, proven
  in closed form, independently verified against 2000 random exact trials);
  (b) found and verified **explicit local-minimum traps**: feasible vertices
  (e.g. `n=5`, `a=(0,2,4,0,0)`, `D=11>t_5=1`) from which *no* single
  elementary move — including generalized (non-adjacent) 3-index primitive
  moves, not just consecutive ones — strictly decreases `D`; this rules out
  the outline's "single-unit exchange, canonical is the unique local hence
  global minimum by connectivity" claim in its literal bounded-width form;
  (c) showed composed (multi-generator) moves *can* escape every tested trap
  for `n≤8`, but the required composition width grows with `n` in the
  tested examples (width 4 needed at `n=8`), so no bounded-width exchange
  argument suffices — genuinely new information about why this problem
  resists a "local" proof, and evidence it is comparable in difficulty to
  `recursive-embedding-induction`'s peel-induction rather than a shortcut
  past it. Did not extend to `k<n` or tail-refined cases, since the `k=n`
  core (Lemma L) is the gating sub-case and remains open via this route.
  **Coordination note:** `recursive-embedding-induction` independently
  proved Lemma L in full this same round, via a different mechanism
  (peel-induction, Lemma PARITY-PAIR) — imported by reference here (see the
  new "coordination update" section below); this approach's remaining
  unique scope is now precisely `k<n` with the tail simultaneously refined,
  not yet attempted.
- (round 4) Targeted exactly the gap flagged by round-3's outline review (Lemma
  V/W not proved; k≥2 and any k≥1-with-simultaneous-tail-splitting open).
  Abandoned the LP-vertex (Lemma V) / wasted-mark (Lemma W) machinery as
  originally planned — found a more direct route. Proved a new, fully general
  **Insertion Lemma** (evenrank(T∪{a}) ≥ a whenever a ≤ max(T), for *any*
  sorted nonnegative multiset T, no geometric structure needed) and a new
  **Claim ★** (abstract reduction: if T is any multiset with max(T) ≤ q and
  oddrank(T) ≥ q, and R is any composition of 2q into s parts, then
  oddrank(R∪T) ≥ 2q) — proved this in full for s = 1 and s = 2 (i.e., ≤ 1
  mark spent splitting the top piece). Combined with Prop A (k=0) and a
  strong induction on n, this gives a genuinely NEW closed sub-case: **k ≤ 1
  with the tail *simultaneously* refined by Xiang Yu's remaining marks** —
  previously flagged as "entirely open" — is now closed unconditionally for
  n ≤ 2, and conditionally for general n (conditional on the k≥2 case being
  closed for n−1, since the induction needs the *full* theorem at level
  n−1, not just its k≤1 part, to bound the refined tail's own oddrank).
  Also found and verified (exact-`Fraction` randomized search, 100000+
  trials) a genuine **negative result**: Claim ★ is FALSE for s ≥ 3 in this
  fully abstracted form (max(T)≤q, oddrank(T)≥q alone do not suffice) —
  concrete counterexamples exist even with T respecting those two scalar
  bounds. This confirms, rigorously this time (not just by numerics), that
  the k≥2 case genuinely requires structural information about T beyond
  "its max and its oddrank" — i.e. beyond what a scalar induction can carry,
  consistent with (and sharpening) the negative result already certified in
  `merge-by-sums-counterexample.md`. Full details, proofs, and the honest
  gap statement are in the new "Round 4" section below.
- (round 1, first draft) Direct construction (Liu Bang's geometric marks) + explicit
  Xiang Yu adversary, tied by the claiming-phase value lemma. Result this round:
  Lemma 1 (claiming-phase value) written up in full and proposed for certification.
  Lemma 2 (top-piece domination) proved in full — trivial algebra. The lower-bound
  half (Step 2) is **fully proved in the sub-case where Xiang Yu's cuts avoid Liu
  Bang's top piece entirely** (Proposition A below) — this sub-case turned out to
  have a much cleaner proof than the outline anticipated (a two-line argument via
  Lemma 1's rank-shift formula, no case-split over "how the tail is subdivided"
  needed at all). The remaining sub-case — Xiang Yu spends some of his cuts
  *inside* the top piece — is genuinely open: numeric optimization (`differential_evolution`,
  exact-fraction bookkeeping) confirms the target bound is tight and attained in
  this sub-case too (e.g. at n=2, splitting the top piece 4/7 into three parts
  ≈(0.0716, 0.6634, 0.2650)·(4/7) with the tail {2/7,1/7} left untouched drives the
  value down to exactly 4/7, matching but not beating the target), but I could not
  find a general merge inequality that turns this numeric tightness into a proof
  within this round's time budget. This is recorded honestly as the open gap
  (same gap the outline and outline-review flagged, now isolated to a much smaller
  and more precisely-stated missing lemma, see "Open gap" below). Step 3 (the
  matching upper-bound adversary strategy for an *arbitrary* Liu Bang configuration)
  is not built this round — deferred, since Step 2 was the priority per the outline
  review's instruction to de-risk the central lemma first.
- (round 2) Targeted the shared `k≥1` gap directly, per the outliner's "Lemma F
  (mark fungibility)" plan. Proved a new **Lemma S** (universal super-increasing
  identity `p_i=Σ_{j>i}p_j+1/D` for all `i`, strictly generalizing Lemma 2) and a
  new **Lemma F1**: the `k=1` sub-case (exactly one Xiang-Yu mark splits `p_1`,
  tail left untouched) is now **fully proved for every `n`, every real split
  ratio** — a genuine new closed special case (previously only `k=0` was
  proved). Also derived the `evenrank(B)≤1-p_1` reformulation of the whole
  target and used it to precisely diagnose why the natural strengthenings fail:
  (a) an explicit numerical counterexample shows Lemma F1 does *not* extend to
  "tail simultaneously refined" without the mark-count bound doing real work
  (unlimited fine tail-splitting breaks the bound, `oddrank→0.501<c(2)=0.571`);
  (b) for general `k≥2` (tail untouched), identified a specific "doubling
  family" of splits (generalizing the certified Proposition 4 recipe to
  `k<n`) that numerically achieves the exact minimum among *all* real
  `(k+1)`-part compositions (confirmed against independent global optimization,
  many restarts, `n≤6`) and found (but did not prove in general) a clean
  recursive slack identity `slack(k,n)=λ_n·slack(k-1,n-1)` governing it — but
  proving that this specific family is the true minimizer over *all*
  compositions (not just verifying it numerically) remains open, as does
  `k≥1` with simultaneous tail-splitting in general. Full honest diagnosis in
  the body of the file below.

## Current best
Full statements and proofs of:
- Lemma 1 (claiming-phase value formula), used as-is by every approach.
- Lemma 2 (top-piece domination in the geometric construction) and its
  strict generalization **Lemma S** (round 2): `p_i = Σ_{j>i}p_j + 1/D` for
  every `i=1,...,n+1` — `A_n` is super-increasing at every truncation level,
  with uniform margin `1/D`.
- Proposition A (lower bound, cuts-avoid-top-piece sub-case): if Xiang Yu's ≤ n
  cuts are all placed strictly inside the non-top pieces of Liu Bang's geometric
  construction, Liu Bang secures ≥ 2^n/(2^{n+1}−1) — proved in full, no case split
  needed. (This is the `k=0` case.)
- **Lemma F1 (round 2, new):** if Xiang Yu spends exactly one mark splitting
  `p_1` into `x≥a≥0` and leaves the tail `T_0` completely untouched, then
  `oddrank({x,a}∪T_0) ≥ p_1` for *every* `a∈[0,p_1/2]` and *every* `n≥1` —
  fully proved (not just checked numerically), extending the certified
  `k=0` coverage to `k=1` in this sub-case.

Open gap (narrowed further this round, see "Round 4 — new work" below for
full detail): `k≥2` (Xiang Yu spends ≥2 marks splitting the top piece
`p_1`), whether or not the tail is *also* touched, remains open for general
`n`, both in the abstract reduced form (proved FALSE for `s≥3`, i.e. the
reduction itself is too weak and must use more of `T`'s structure) and in
the original form (no proof found this round). `k≤1` (i.e. `k=0` or exactly
one mark on `p_1`) **with the tail simultaneously refined** is now closed:
unconditionally for `n≤2`, and for general `n` conditional on the full
theorem (all `k`) holding at level `n−1` — see below for the precise
induction and why that conditionality is unavoidable with this method.

**(Round 5 update.)** The `k≥2` gap's most natural remaining route — a
single-unit exchange/local-move argument directly on the composition vector
of `p_1`, generalizing the doubling family — was tested this round and
found **not to work in its bounded-width form**: an exact algebraic lemma
for the effect of the minimal legal exchange move on the invariant `D` is
now proved (`ΔD = ±t_i` exactly), but explicit, verified local-minimum traps
show no *single* such move (of any pair of indices, not just adjacent ones)
always decreases `D`, and the composition width needed to escape a trap
grows with `n` in the tested range (`n≤8`). See "Round 5 — testing the
exchange argument" below for the full statement, proofs, and honest
negative conclusion.

**Separately (coordination update, same round): Lemma L itself — the
`k=n`, tail-untouched core of this gap — is now fully proved**, by
`recursive-embedding-induction`'s peel-induction (Lemma PARITY-PAIR),
independently of and not using this approach's exchange-argument work.
Imported by reference here (see "Round 5 — coordination update" below).
What remains genuinely open for the lower bound is now precisely: general
`0≤k<n` **with the tail simultaneously refined** (not attempted by any
approach yet, requires a version of Lemma V' that handles adversarial
splitting of both the top piece and the tail at once).

**(Round 6 update.)** Proposition K (the `k=n`, tail-untouched sub-case)
is now **fully closed for every `n`, not just the pure-anchor part** —
Lemma FC (the "one free coordinate" case of the fixed-tail Lemma V') is
proved in full this round (see `lemmas/lemma-V-prime-free-coordinate.md`),
combining with Lemma L/PARITY-PAIR. This approach has no further unique
target from Proposition K.

**(Round 8 update.)** Re-scoped, per this round's outline, to attack gap
(b) of `recursive-embedding-induction`'s Lemma V'-GEN (cross-piece tied
free coordinates) via a second, independent mechanism (explicit affine-
slope computation, rather than tree-peeling/shared-block combinatorics).
**New Lemma CROSS-TIE-AFFINE proved in full**: any cluster of `k≥2`
mutually-tied free coordinates from different split pieces has `D`
affine in the shared tie-value with an explicit computable integer
slope, so the tie is never a strict local minimizer — pushing to a
boundary of the affine cell weakly decreases `D`. A genuinely new
structural fact discovered and proved this round (the "self-meeting
point is always an anchor" fact, from `t_i=2t_{i+1}` always holding in
this specific geometric construction) shows this reduction lands
**exactly on an anchor-only configuration with zero residue** whenever
the tied coordinate is the *majority* (larger) part of any 2-part-split
piece, or belongs to a piece with ≥3 parts (matching
`recursive-embedding-induction`'s already-closed well-separated case).
**One precisely-isolated residual sub-case remains honestly open**: the
tied coordinate is the *minority* (smaller) part of a 2-part-split piece,
tied in a bracket strictly deeper than that piece's own natural halving
level — pushing to the external anchor boundary there can leave the
companion part at a fixed, non-anchor value, not yet resolved by any
established closed case. See "Round 8" section below for full statement,
proof, and the precise residual gap.

**(Round 9 update.)** This residual sub-case is now **closed**, for every
`n` and every configuration of the "all-minority, all-exactly-2-parts" tie
type (which is exactly the sub-case Round 8 isolated) — new Lemma
TWO-BLOCK plus a Structural Lemma identifying the two globally-largest
merged pieces, certified to `lemmas/two-block-residue-close.md`. See
"Round 9" section below.

**(Round 10 update.)** The round-9 restriction to a **single** tie-cluster
is now **removed**: Lemma TOP2 + the generalized Structural Lemma prove
`D(B)≥t_n` for every `n≥1`, every `K≥1` simultaneous, independent
minority-role 2-part tie-clusters, with no ordering assumption between the
clusters' tie values. Certified to `lemmas/multi-cluster-two-block.md`.
Combined with all previously-certified facts (Lemma CROSS-TIE-AFFINE's
zero-residue closure for majority-part/`≥3`-part ties, Lemma TREE-BOUND for
anchor-only strategies, and `recursive-embedding-induction`'s well-separated
single-free-coordinate closure), gap (b) of Lemma V'-GEN now appears closed
in full for every configuration where each individual split piece has at
most 2 parts — **the one remaining honestly-open loose end is the narrower
"doubly-tied `≥3`-part piece" scenario** (flagged already in round 9,
unrelated to the multi-cluster question just closed), which this round did
not address. See "Round 10" section below for the full statement and
proof.

## Target
For every positive integer n, determine the largest c(n) such that Liu Bang can
guarantee total claimed length ≥ c(n) regardless of Xiang Yu's play.

**Answer: c(n) = 2^n / (2^{n+1} − 1).**

## Setup and notation

Normalize the stick to [0,1]. Liu Bang marks at most n points, Xiang Yu marks at
most n further points (all n + n points, when both use their full budget, distinct);
the stick is cut at all marked points into pieces, then the players alternately
claim whole pieces, Liu Bang first, each maximizing his own total claimed length.

Write a *configuration* for a finite multiset of positive reals summing to 1 (a
list of piece lengths). If Liu Bang's n marks produce piece multiset A (|A| ≤ n+1,
possibly < n+1 if some marks coincide — but marks are required distinct, so with k
≤ n distinct marks Liu Bang gets exactly k+1 pieces; we allow k < n, i.e. Liu Bang
need not use his whole budget), then Xiang Yu's further marks each fall inside some
existing piece of A and split it into two; iterating, Xiang Yu's ≤ n marks refine A
into a final multiset B, with |B| ≤ |A| + n.

### Lemma 1 (claiming-phase value formula).

*Statement.* Let S = {a_1 ≥ a_2 ≥ ... ≥ a_m} be any finite multiset of nonnegative
reals (m ≥ 0). Consider the two-player alternating claiming game on S: players
alternately claim one remaining element of S (arbitrary tie-breaking allowed when
several elements are equal or when a player has several optimal choices), each
maximizing the total value of elements they personally claim over the whole game;
player 1 moves first. Then the game has a well-defined value (the amount player 1
secures under optimal play by both sides, independent of any tie-breaking),
`f(S) = a_1 + a_3 + a_5 + ⋯` (the sum of the odd-ranked elements, 1-indexed,
sorted descending), and "claim the currently-largest remaining element" is always
an optimal move for the player to move (regardless of which tied maximal element is
chosen when there are ties).

*Proof.* By strong induction on m = |S|. Base cases m = 0 (f = 0, no moves) and
m = 1 (f = a_1, the sole mover takes it) are immediate.

Inductive step, m ≥ 2. In a finite, deterministic, zero-total-value, perfect-information
two-player game, the value for the mover is defined by backward induction:
if the mover claims element x ∈ S, the opponent then moves first on S \ {x} and
(by the induction hypothesis, applied to the multiset S\{x} of size m−1 < m)
secures f(S \ {x}) from it, leaving the mover with `Σ(S\{x}) − f(S\{x})` from the
remainder, plus x itself. The mover picks x to maximize this, so
`f(S) = max_{x∈S} [ x + Σ(S\{x}) − f(S\{x}) ] = Σ(S) − min_{x∈S} f(S\{x})`
(since `x + Σ(S\{x}) = Σ(S)`, independent of x).

For x = a_i, the multiset S\{a_i} sorted descending is `a_1,...,a_{i-1},a_{i+1},...,a_m`;
elements before position i keep their original rank, elements after position i shift
down by one (their rank decreases by 1, so their parity flips). By the induction
hypothesis,
`f(S\{a_i}) =: h(i) = Σ_{j<i, j odd} a_j + Σ_{j>i, j even} a_j`.

Compute the difference `h(i+1) − h(i)` for `1 ≤ i ≤ m−1`:
- If i is odd: in h(i+1) the term a_i is now counted (since j=i<i+1 and i odd,
  contributing to the first sum), while a_{i+1} is no longer counted in the second
  sum of h(i+1) (since now j=i+1 is not > i+1). Compared to h(i), which counted
  a_{i+1} in its second sum (j=i+1>i, i+1 even) but not a_i (j=i, i odd, but i is
  not < i so not counted in h(i)'s first sum — wait, checking indices carefully:
  h(i) first sum is over j<i, so a_i itself (j=i) is never in h(i)'s first sum;
  h(i) second sum is over j>i even, so a_{i+1} (j=i+1, even since i odd) is
  counted in h(i). In h(i+1): first sum is over j<i+1=i+1, i.e. j≤i, j odd — since
  i is odd this now includes a_i; second sum is over j>i+1 even, so a_{i+1} (j=i+1,
  not > i+1) is excluded. All other terms a_1,...,a_{i-1} and a_{i+2},...,a_m
  appear identically in h(i) and h(i+1) (their position relative to the removed
  index doesn't change parity for j < i or j > i+1). Hence
  `h(i+1) − h(i) = a_i − a_{i+1} ≥ 0` (descending order).
- If i is even: by the same accounting, h(i+1) and h(i) include exactly the same
  terms (removing a_i, which was in neither sum since i even puts it in the "would
  be second sum but excluded because j is not >i" / "would be first sum but j=i is
  not <i" gap on both sides — concretely, for i even, a_i is at an even position
  numbered i in h(i)'s labeling and does not change which of a_1,...,a_m appear in
  the odd/even split of the rest), giving `h(i+1) − h(i) = 0`.

Hence h is non-decreasing in i, so `min_i h(i) = h(1) = Σ_{j>1, j even} a_j =
a_2+a_4+⋯`. The minimizing choice for the mover is therefore x = a_1 (the current
largest element — ties among several copies of a_1 are all equally optimal, so
"take a largest remaining element" is always optimal, proving the second claim),
and
`f(S) = Σ(S) − h(1) = (a_1+a_2+⋯+a_m) − (a_2+a_4+⋯) = a_1+a_3+a_5+⋯`. ∎

This value is a property of the game (backward-induction value of a finite
zero-total-value game), hence independent of any tie-breaking rule; in particular
it applies unchanged to our problem, where "elements of S" are piece lengths and
ties (equal-length pieces) may occur.

**Consequence.** Only the physical position of a mark along the stick, not the
order pieces happen to occupy in [0,1], affects the multiset of final piece
lengths B — the claiming-phase value depends only on the multiset B (Lemma 1), and
which piece is "leftmost" is irrelevant to which pieces a player can choose to
claim (all unclaimed pieces are always eligible) or to which piece Xiang Yu can
choose to cut further (he may cut any current piece regardless of its location).
Hence the whole problem reduces to: Liu Bang chooses a configuration A (via ≤ n
marks); Xiang Yu, seeing A, chooses ≤ n further marks, each splitting some current
piece of A into two, producing a refinement B of A; Liu Bang's guaranteed total is
`c(n) = max_A min_B oddrank(B)`, where oddrank(S) := f(S) as in Lemma 1, and B
ranges over all refinements of A reachable with ≤ n further cuts.

## Liu Bang's construction

Fix n ≥ 1. Liu Bang marks n points producing the (n+1)-piece configuration
`A_n = {x_1 > x_2 > ... > x_{n+1}}`, `x_i = 2^{n+1-i} / (2^{n+1}−1)`, i.e. (scaling
by the common denominator D := 2^{n+1} − 1) the unnormalized piece sizes are
`2^n, 2^{n-1}, ..., 2, 1`. Check `Σx_i = D/D = 1` since `Σ_{i=1}^{n+1} 2^{n+1-i} =
2^n+2^{n-1}+⋯+1 = 2^{n+1}-1 = D`. This uses n marks (n+1 pieces), consistent with
Liu Bang's budget. (Concretely: mark points at cumulative distances
`1-x_1, 1-x_1-x_2, ..., 1-x_1-⋯-x_n` from one end of the stick; by the
Consequence above, only the resulting multiset matters, so any left-to-right
arrangement of these n+1 lengths works identically.)

Write `top := x_1 = 2^n/D` and `T_0 := {x_2,...,x_{n+1}}` (the "tail", n pieces,
unnormalized sizes `2^{n-1},...,1`, sum `2^n - 1` unnormalized, i.e. `(2^n-1)/D`
normalized).

### Lemma 2 (top-piece domination).

`top > Σ(T_0)`, in fact `top − Σ(T_0) = 1/D` exactly.

*Proof.* Unnormalized: `Σ_{i=2}^{n+1} 2^{n+1-i} = 2^{n-1}+2^{n-2}+⋯+2^0 = 2^n − 1`
(finite geometric series, ratio 1/2, n terms, standard identity `Σ_{j=0}^{n-1}2^j =
2^n-1`). So `Σ(T_0) = (2^n-1)/D` (normalized) and `top − Σ(T_0) = (2^n-(2^n-1))/D =
1/D > 0`. ∎

### Proposition A (lower bound, top-untouched sub-case).

Suppose Xiang Yu's ≤ n marks are placed *only* inside pieces of `T_0` (none
strictly inside the piece `top`), producing a refinement `T` of `T_0` (so `Σ(T) =
Σ(T_0) = (2^n-1)/D`, and `T` may have any number of elements ≥ n depending on how
many cuts land where — this proof does not need to bound `|T|`). Let `B = {top}
∪ T` be the resulting final configuration. Then
`oddrank(B) ≥ top = 2^n/D = 2^n/(2^{n+1}-1)`.

*Proof.* Every element of `T` is a nonnegative real and `Σ(T) = (2^n-1)/D <
2^n/D = top`, so every individual element of `T` is `≤ Σ(T) < top` (an element
cannot exceed the sum of a multiset containing it, when all elements are
nonnegative). Hence `top` strictly exceeds every element of `T`, so `top` is the
unique maximum of `B` and occupies rank 1 in the descending sort of `B`. Writing
`T` sorted descending as `t_1 ≥ t_2 ≥ ⋯ ≥ t_r` (r = |T|), the sorted list `B` is
`(top, t_1, t_2, ..., t_r)`, so `B`'s rank-`(j+1)` element is `t_j` for `j =
1,...,r`. By Lemma 1,
`oddrank(B) = top + Σ_{j odd, j+1 odd ⟺ j even} t_j`... more directly: the
odd ranks of B are `{1, 3, 5, ...}`; rank 1 is `top`; rank `2m+1` (for `m ≥ 1`) is
`t_{2m}`. So
`oddrank(B) = top + (t_2 + t_4 + t_6 + ⋯) = top + evenrank(T) ≥ top`,
since `evenrank(T) := t_2+t_4+⋯ ≥ 0` trivially (sum of nonnegative reals, possibly
an empty sum if `r ≤ 1`). Hence `oddrank(B) ≥ top = 2^n/(2^{n+1}-1)`. ∎

(Equality can only occur when `evenrank(T) = 0`, i.e. when `T` has at most one
element — impossible for `n ≥ 2` since `T_0` alone already has `n ≥ 2` elements
before any further splitting, so for `n ≥ 2` this sub-case in fact gives Liu Bang
*strictly more* than the target whenever the tail is left with ≥ 2 pieces, which
it always is. This sub-case is therefore never the one that makes the bound
tight for `n ≥ 2`; tightness must come from the other sub-case, consistent with
the numerics below.)

## Open gap (honest statement)

**Missing Lemma (top-touched sub-case).** *Claim, not yet proved:* if Xiang Yu's
≤ n marks are distributed so that k ≥ 1 of them land strictly inside the piece
`top`, splitting it into k+1 sub-pieces `C = {c_1,...,c_{k+1}}` (Σ C = top, values
chosen adversarially by Xiang Yu), and the remaining ≤ n−k marks refine `T_0` into
some `T` (Σ T = Σ T_0), then the merged, sorted `B = C ∪ T` still satisfies
`oddrank(B) ≥ 2^n/D`.

*Why Proposition A's proof does not extend.* Proposition A's argument relies on
`top` being the unique rank-1 element of `B`, which used `top > Σ(T)` (Lemma 2)
essentially applied once, at the top level. Once `top` itself is split, no single
piece of `C` need dominate `Σ(T)` (indeed numerically the optimal adversarial
split of `top` produces pieces of a size comparable to elements of `T`, e.g. for
`n=2`, splitting `top = 4/7` into three parts in ratio roughly `(0.072, 0.663,
0.265)` interleaves with the untouched tail `{2/7, 1/7}` rather than dominating
it), so the clean "one dominant piece + trivial evenrank ≥ 0" argument breaks:
bounding `oddrank(merge(C,T))` below now genuinely depends on the interleaving
pattern of `C` and `T`'s values, not just on their totals `Σ C = top`, `Σ T = 2^n
-1-` (times relevant scale), i.e. on more than the sums.

*Numeric evidence the Missing Lemma is nonetheless true and tight.* I checked
(exact-fraction random search, 20000 trials, and `scipy.optimize.differential_evolution`
targeted search) for `n = 2` (target `4/7`): across every tested Xiang Yu strategy
(distributing his 2 cuts in every combination between `top = 4/7` and the tail
pieces `2/7, 1/7`, with arbitrary split ratios), the minimum `oddrank(B)` found was
exactly `4/7`, never below, attained both by (i) Proposition A's sub-case in a
degenerate limit and (ii) a genuinely top-touching strategy (all 2 cuts spent
inside `top`, tail untouched, split ratios found by numerical optimization to
`(0.0716, 0.6634, 0.2650)·(4/7)`, giving `oddrank = 4/7` exactly to machine/rational
precision). This is consistent with the conjectured value `c(n) = 2^n/(2^{n+1}-1)`
and with the Missing Lemma being a true, tight inequality — but it is *numeric
evidence*, not a proof, and I was not able to close it rigorously within this
round's time. This is exactly the gap flagged by the outline review as the central
open risk of this approach (there called Lemma 3 / cut-concentration dominance);
this round narrowed it from "how does the tail distribution matter" (resolved: it
doesn't, by Proposition A, in the top-untouched sub-case) down to the single
remaining question of what happens when the top piece itself is split, which is
now precisely isolated as stated above.

**What a proof of the Missing Lemma would complete.** Once the Missing Lemma is
proved, Step 2 (Liu Bang's ≥ 2^n/(2^{n+1}-1) guarantee) is complete by combining it
with Proposition A (the two sub-cases — k=0 and k≥1 cuts on top — exhaust all of
Xiang Yu's possible strategies, since every one of his ≤ n cuts lands in exactly
one of the n+1 pieces of A_n, either `top` or one of the n pieces of `T_0`).
Step 3 (the matching adversary strategy for an *arbitrary* Liu Bang configuration,
establishing the upper bound `c(n) ≤ 2^n/(2^{n+1}-1)`) was not attempted this
round and remains fully open; the natural candidate (Xiang Yu concentrates his
cuts on Liu Bang's current largest piece) is exactly dual to the gap above and
would likely need the same merge-interleaving machinery to make rigorous.

## Promotable lemmas
- **Lemma 1 (claiming-phase value formula)** — full statement and proof above.
  This is used identically by every approach to this problem and is a clean,
  self-contained combinatorial-game fact with no dependence on the rest of this
  approach's construction. Recommend certifying to
  `results/imo-2026-03/lemmas/claiming-phase-value.md`.
- **Lemma 2 (top-piece domination)** and **Proposition A (top-untouched lower
  bound sub-case)** are specific to the geometric construction and reusable by
  `recursive-embedding-induction` (which also uses the geometric/self-similar
  configuration) — worth certifying as a shared lemma once reviewed, since the
  proof (rank-shift + evenrank ≥ 0) is short and fully general (it did not need
  to assume anything about how many cuts land in the tail or how they're
  distributed there).
- **(NEW, round 2) Lemma S (universal super-increasing identity)** and
  **Lemma F1 (single-mark top-split lower bound, all `n`)** — see below; both
  fully proved and reusable.

## Round 2 — new work: attacking the k≥1 gap

### Lemma S (universal super-increasing identity for `A_n`)

*Statement.* For every `i = 1,...,n+1` (with the convention that an empty sum
is `0`), `p_i = Σ_{j=i+1}^{n+1} p_j + 1/D`. Equivalently: `A_n`, viewed as the
full sequence `p_1 > p_2 > ⋯ > p_{n+1}` (not just the tail `T_0`), is
*super-increasing*: every piece strictly exceeds the sum of all strictly
smaller pieces, by the *same uniform margin* `1/D` at every truncation level.

*Proof.* `Σ_{j=i+1}^{n+1} p_j = Σ_{j=i+1}^{n+1} 2^{n+1-j}/D`. Substituting
`l = n+1-j` (so `l` ranges from `0` to `n-i` as `j` ranges from `n+1` down to
`i+1`), this sum is `Σ_{l=0}^{n-i} 2^l / D = (2^{n-i+1}-1)/D` (finite geometric
series). Hence `p_i - Σ_{j>i} p_j = 2^{n+1-i}/D - (2^{n+1-i}-1)/D = 1/D`, for
every `i = 1,...,n+1` (at `i=n+1` the sum is empty/`0` and the identity reads
`p_{n+1} = 1/D`, which holds by definition). ∎

This strictly generalizes Lemma 2 (the `i=1` instance) and is the correct
uniform form of the "top-piece dominates" idea — it is what makes `T_0` itself
(the `i=2,...,n+1` instances) a super-increasing sequence, i.e. exactly Lemma
3's rescaled copy of `A_{n-1}`, which is *also* super-increasing by the same
identity one level down (consistent, self-similar).

### Reformulation: the target is equivalent to an *evenrank* bound

*Fact.* For any refinement `B` of `A_n` (by any number of cuts, using
`Σ(B) = 1` always, since cutting preserves total length), `oddrank(B) ≥ p_1`
**if and only if** `evenrank(B) ≤ 1 - p_1 = Σ(T_0)`.

*Proof.* `oddrank(B) + evenrank(B) = Σ(B) = 1` (every element of `B` is at
exactly one rank, odd or even), so `oddrank(B) ≥ p_1 ⟺ 1 - evenrank(B) ≥ p_1
⟺ evenrank(B) ≤ 1-p_1`. ∎

This reformulation is used throughout below; it converts "Liu Bang gets
enough" into "Xiang Yu's favorable (even-rank, second-mover-claimed) share
cannot exceed the tail's total," which turns out to be the more tractable
direction to bound directly.

### Lemma F1 (single-mark top-split lower bound, tail untouched, all `n`)

*Statement.* Fix `n ≥ 1`. Suppose Xiang Yu spends exactly one mark splitting
`p_1` into two parts `x ≥ a ≥ 0` (`x + a = p_1`) and leaves every piece of the
tail `T_0 = {p_2,...,p_{n+1}}` untouched (whether or not he has further marks
available — he may simply choose not to use them). Then, for **every** choice
of `a ∈ [0, p_1/2]`, `oddrank({x,a} ∪ T_0) ≥ p_1 = c(n)`, with equality
attained on a nonempty sub-interval of `a`-values whenever `n ≥ 2` (and for
all `a` when `n=1`).

*Proof.* First, `x = p_1 - a ≥ p_1 - p_1/2 = p_1/2 = p_2` (using `p_1 = 2p_2`,
the `i=1` instance of Lemma 3's doubling relation; equivalently immediate from
`p_1=2^n/D`, `p_2=2^{n-1}/D`). Since every element of `T_0` is `≤ p_2` (as
`T_0` is sorted with maximum `p_2`), we get `x ≥ p_2 ≥` every element of
`T_0`, and also `x ≥ p_1/2 ≥ a`. Hence `x` is a (possibly tied-for-)maximum
of the whole multiset `{x,a} ∪ T_0` and can be placed at rank 1 in the sorted
order; the remaining `n+1` elements, sorted descending, are exactly the
sorted merge of `T_0 = {p_2,...,p_{n+1}}` (fixed) with the single value `a`.
By the rank-shift argument used in Proposition A / Lemma 1's proof
(prepending a dominant maximum shifts every subsequent rank up by one,
flipping parity),
```
oddrank({x,a} ∪ T_0) = x + evenrank(T_0 ∪ {a}).
```
So it suffices to prove `evenrank(T_0 ∪ {a}) ≥ a` for every `a ∈ [0,p_2]`
(this gives `oddrank({x,a} ∪ T_0) ≥ x + a = p_1`, as required).

Let `j := #{i : p_{i+1} ≥ a, 1≤i≤n}` (the number of `T_0`-elements that are
`≥ a`; ties broken toward inclusion), so inserting `a` into the sorted list
`p_2,...,p_{n+1}` places it at position `j+1` (1-indexed) in the merged list
of `n+1` elements.

*Case `j` odd.* Then `a`'s position `j+1` is even, so `a` itself is one of the
terms summed in `evenrank(T_0 ∪ {a})`; since every other term of that sum is a
nonnegative real, `evenrank(T_0 ∪ {a}) ≥ a` immediately — no further
computation needed, and this holds for *any* multiset `T_0`, not just the
geometric one (a fully general fact about inserting an element into a sorted
list: whichever position it lands at, if that position is even, it
contributes its own value to `evenrank`, which alone already gives the
bound).

*Case `j` even.* Write `m := j+1` (so `1 ≤ m ≤ n+1`, and `m` is odd; formally
allow `m = n+1` when `a ≤ p_{n+1}`, treating the tail sum below as empty in
that boundary sub-case). By construction `a ≤ p_m` (there are `j = m-1` tail
elements `≥ a`, so `p_m` is the smallest tail element that is `≥ a`, or
`a ≤ p_{n+1}` if `m=n+1`). The merged list `T_0 ∪ {a}`, in this case, is
`(p_2,...,p_m, a, p_{m+1},...,p_{n+1})` (positions `1,...,m-1, m, m+1,...,n+1`;
if `m=n+1` there is no "`p_{m+1},...`" tail at all). Since `m` is odd, `a`
sits at odd position `m` and does *not* contribute to `evenrank`; tracking
which original `p_i`'s occupy even positions before and after `a`'s slot
(positions `2,4,...,m-1` before the slot, which are `p_3,p_5,...,p_m`; and
positions `m+1,m+3,...` after the slot, which are `p_{m+1},p_{m+3},...`, both
by direct enumeration of the position shift), we get
```
evenrank(T_0 ∪ {a}) = (p_3+p_5+...+p_m) + (p_{m+1}+p_{m+3}+...+p_last),
```
a sum of nonnegative terms that includes `p_m` itself as one of its summands
(the last term of the first group, since `m` is odd and that group is indexed
`3,5,...,m`) — or, in the boundary sub-case `m=n+1` (which requires `n+1` odd,
i.e. `n` even; then there is no second group, and the sum is exactly
`evenrank(T_0) = p_3+p_5+...+p_{n+1}`, which again contains `p_{n+1}` as its
last term). In every sub-case, `evenrank(T_0 ∪ {a}) ≥ p_m ≥ a` (the last
inequality because `a ≤ p_m` by the definition of `m`). This proves
`evenrank(T_0 ∪ {a}) ≥ a` in the `j`-even case too.

Combining both cases, `evenrank(T_0 ∪ {a}) ≥ a` for every `a ∈ [0,p_2]`, hence
`oddrank({x,a} ∪ T_0) ≥ p_1` for every such `a`, completing the proof. ∎

*Numerical corroboration.* Verified exhaustively (exact `Fraction` arithmetic,
2001-point grid over `a ∈ [0,p_1/2]`) for `n = 1,...,7`: the inequality
holds with no violation in any case (see `/tmp/round-2` transcript in this
build's working notes); this is confirmatory, not a substitute for the proof
above, which holds for *every* real `n ≥ 1` and *every* real `a` in the
stated range, not just the tested grid.

*What this closes, and what it does not.* This fully settles the sub-case "Xiang
Yu spends exactly one mark, on `p_1`, and leaves the tail completely untouched"
— for every `n`, not just small cases, and for every real-valued split ratio,
not a discretized sample. Combined with Proposition A (`k=0`, tail arbitrarily
refined), this gives full lower-bound coverage of `k ∈ {0,1}` **provided the
tail is untouched whenever `k=1`**. It does **not** yet cover: (a) `k=1` with
the tail *simultaneously* refined by Xiang Yu's remaining `n-1` marks, or (b)
`k ≥ 2` at all (whether or not the tail is touched). These are exactly the
open gap, discussed next.

### Why the natural generalizations resist a short proof (honest diagnosis)

**Attempt 1: does Lemma F1 extend to "tail also refined"?** No — and this is
important to record precisely, since it rules out the naive strengthening.
Take `n=2` (`c(2)=4/7`), split `p_1=4/7` with `a` just below `p_2=2/7`
(so `x` just above `2/7`), and refine the tail `T_0={2/7,1/7}` into `N`
equal tiny pieces each (any large `N`, i.e. finely split — this uses far more
than the `n-1=1` marks actually available in the real game, so it is *not* a
legal Xiang-Yu move for `n=2`, but it shows the underlying inequality
`evenrank(T ∪ {a}) ≥ a` genuinely depends on `T` having boundedly many
pieces, not just on `Σ(T)` or on `T` being a refinement of the geometric
tail): as `N → ∞`, `evenrank(T ∪ {a})` for a merge with many tiny pieces tends
to `≈ Σ(T)/2`, which is `< a` once `a` is close to `p_2` — a genuine, checked
numerical breakdown (`oddrank ≈ 0.501 < c(2)=0.5714` with `N=200` equal tail
pieces on each of the two tail pieces). **This confirms the mark-count bound
`≤ n` marks is doing essential work** even in this simplest extension, and
that any correct proof of the general case must use the bound `n-k` on the
number of tail cuts as a load-bearing hypothesis, not just the *value* of
`Σ(T)` or an unlimited-refinement version of Prop A/Lemma F1.

**Attempt 2: general `k`, tail still untouched.** We looked for the exact
minimum of `oddrank(C ∪ T_0)` over *all* compositions `C` of `p_1` into
`k+1 ≤ n+1` parts (tail untouched), both via the specific "doubling family"
`C_k := {p_2, p_3, ..., p_{k+1}, p_1 - Σ_{i=2}^{k+1} p_i}` (a direct
generalization of the already-certified Proposition 4 recipe to `k<n`) and via
numerical global optimization (`scipy.optimize.minimize`, many random
restarts) over *all* real compositions. Findings (exact `Fraction`
computation for the family, `n=3,4,5`):
```
n=4: k=0 slack=5/31, k=1 slack=2/31, k=2 slack=1/31, k=3 slack=0, k=4 slack=0
n=5: k=0 slack=10/63, k=1 slack=5/63, k=2 slack=2/63, k=3 slack=1/63, k=4,5 slack=0
```
(`slack(k,n) := Σ(T_0) - evenrank(C_k ∪ T_0) ≥ 0`; `slack=0` means the family
exactly attains `oddrank=c(n)`.) The numerical global optimizer (25+ random
restarts, continuous split ratios) matches these family values *exactly* at
every tested `(n,k)`, strong evidence the doubling family is the true
minimizer among `(k+1)`-part compositions, not merely *a* valid one. We found
and can state, but did **not** fully verify from scratch, the clean recursive
pattern `slack(k,n) = λ_n · slack(k-1,n-1)` for `k ≥ 1` (matching the
`Σ(T_0) = λ_n` self-similarity of Lemma 3): this identity, if proved in
general (it is a concrete algebraic computation about the specific `C_k`
family, not yet carried out symbolically for general `n,k` in this round,
only checked numerically for `n≤5`), would show the *family* achieves exactly
`c(n)` for `k ≥ n-1` and strictly more for `k<n-1` — but **this only pins down
the behaviour of one specific family of splits**, not that *every*
`(k+1)`-part composition satisfies `oddrank ≥ c(n)`. That remaining "no split
beats the family" step is a genuine minimization/majorization claim over the
whole simplex of `(k+1)`-part compositions, and we did not find a short
rearrangement argument for it this round (the natural attempt — inserting
`C`'s elements into `T_0` one at a time, largest first, imitating Lemma F1's
proof — breaks down because for `k ≥ 2`, the largest part `c_1` of an
adversarially-chosen
composition can be `< p_2`, e.g. an even `(k+1)`-way split, so it does *not*
automatically dominate `T_0`'s top element the way `x` did in the `k=1` case,
and the clean "insert the dominant element first" argument no longer applies
without a genuinely new idea).

**Conclusion of this round's work on the gap:** Lemma F1 is a real, fully
proved strengthening of the population's coverage (previously only `k=0` was
closed at all; now `k=1` is closed too, in the tail-untouched sub-case, for
every `n`), together with a precise diagnosis — backed by an explicit
numerical counterexample to the naive strengthening, and an identified
concrete algebraic identity (unproved in general) — of exactly what additional
argument (a genuine global-minimum/majorization statement for `(k+1)`-part
compositions, and separately, handling simultaneous tail refinement with a
bounded mark count) is needed to close the rest. This is real progress
compared to the round-1 file (which had no proof at all beyond `k=0`, and
described the sub-case only via unverified numerics), but the full Lemma F
(all `k`, simultaneous tail-splitting, general `n`) remains open.

## Promotable lemmas (round 2 additions)
- **Lemma S (universal super-increasing identity)** — `p_i = Σ_{j>i}p_j + 1/D`
  for all `i=1,\dots,n+1` — fully proved above, strictly generalizes the
  already-certified Lemma 2, reusable by any approach needing the geometric
  configuration's structure (in particular `recursive-embedding-induction` and
  `universal-adversary-strategy`, whose Lemma I/J cheap-kill mechanisms concern
  exactly this kind of domination-by-margin fact).
- **evenrank reformulation** (`oddrank(B)≥p_1 ⟺ evenrank(B)≤1-p_1`) — trivial
  but useful bookkeeping fact, fully proved, reusable by any approach working
  with this specific target value.
- **Lemma F1 (single-mark top-split lower bound, tail untouched, all `n`)** —
  fully proved above; a genuine new closed special case (`k=1`, tail
  untouched), strictly extending Proposition A's `k=0` coverage. Recommend
  certifying alongside Lemma S once reviewed.

## Round 4 — new work: an Insertion Lemma, an abstract reduction, and its exact limits

Notation as above: `A_n = {p_1>...>p_{n+1}}`, `p_i=2^{n+1-i}/D`, `D=2^{n+1}-1`,
`T_0={p_2,...,p_{n+1}}`. Recall `p_1=2p_2` (Lemma S, `i=1` instance) and, by
Lemma 3/self-similarity (certified in `lemmas/geometric-configuration-facts.md`),
`T_0 = λ_n·A_{n-1}` where `λ_n := Σ(T_0) = (2^n-1)/D`, i.e. `T_0` is a rescaled
copy of the full `n-1`-level geometric configuration.

### Lemma I (Insertion Lemma) — fully general, no geometric structure needed

*Statement.* Let `T` be any finite, nonempty multiset of nonnegative reals,
and let `a` be any real with `0 ≤ a ≤ max(T)`. Then `evenrank(T ∪ {a}) ≥ a`.

*Proof.* Sort `T` descending as `t_1 ≥ t_2 ≥ ... ≥ t_r` (`r ≥ 1`). Let
`j := #{i : t_i ≥ a}` (ties toward inclusion); since `a ≤ t_1 = max(T)`,
`j ≥ 1`. Inserting `a` into the sorted order places it at position `m := j+1`
(1-indexed among the `r+1` elements of `T∪{a}`): the first `j` elements of the
merged list are `t_1,...,t_j` (unchanged, since they're all `≥ a`), then `a`,
then `t_{j+1},...,t_r` (each shifted down one position from its original rank
in `T`).

*Case `j` even (so `m=j+1` odd).* Position `j` (even) still holds `t_j`
(unchanged, since `j ≤ j`), and `t_j ≥ a` by definition of `j`. Since `evenrank`
sums the values at even positions, and position `j` is one of them,
`evenrank(T∪{a}) ≥ t_j ≥ a`.

*Case `j` odd (so `m=j+1` even).* Position `m=j+1` holds `a` itself, and
`evenrank` sums the values at even positions including this one, so
`evenrank(T∪{a}) ≥ a` directly (all values are nonnegative, so every other term
of the sum only adds to it). ∎

(This subsumes and is a strict generalization of the "case j odd / case j
even" computation used in round 2's Lemma F1 — that argument in fact never
used any property of `T_0` beyond it being sorted and `a ≤ max(T_0)`; Lemma I
extracts and states this as the fully general, structure-free fact it always
was.)

### A companion fact: prepending `s` dominant elements preserves parity of the rest

*Fact (rank-shift-by-s).* Let `T` be any finite multiset and `R` a finite
multiset with `min(R) ≥ max(T)` (every element of `R` is `≥` every element of
`T`; `|R|=s`). Then, writing `R` sorted descending `r_1≥...≥r_s`:
- if `s` is even: `oddrank(R∪T) = oddrank(R) + oddrank(T)`,
- if `s` is odd: `oddrank(R∪T) = oddrank(R) + evenrank(T)`.

*Proof.* Since every element of `R` is `≥` every element of `T`, the sorted
merge is exactly `R` (in its own sorted order) followed by `T` (in its own
sorted order) — `R`'s elements occupy positions `1,...,s` and `T`'s occupy
positions `s+1,...,s+|T|`. `T`'s element originally at rank `i` (in `T` alone)
is now at rank `s+i`; the parity of `s+i` equals the parity of `i` iff `s` is
even, and is flipped iff `s` is odd. Summing over `T`'s own odd ranks under
each case gives the two stated identities (and `R`'s own contribution is
simply `oddrank(R)`, since `R`'s internal ranks are untouched by the merge). ∎

We only need the cases `s=1` (used implicitly throughout, e.g. Lemma 1's own
proof and Prop A) and `s=2` below.

### Claim ★ (abstract reduction)

*Statement.* Let `q > 0`. Let `T` be any finite multiset of nonnegative reals
with `max(T) ≤ q` and `oddrank(T) ≥ q`. Let `R = {r_1≥...≥r_s}` (`s ≥ 1`) be
any finite multiset with `Σ R = 2q`. **For `s ∈ {1,2}`**, `oddrank(R∪T) ≥ 2q`.

*Proof, `s=1`.* `R = {2q}`. Since `2q > q ≥ max(T)`, `2q` is a (possibly
tied-for-)maximum of `R∪T`, so by the rank-shift-by-1 fact,
`oddrank(R∪T) = 2q + evenrank(T) ≥ 2q` (as `evenrank(T) ≥ 0` trivially, a sum
of nonnegative terms). ∎

*Proof, `s=2`.* `r_1+r_2=2q`, `r_1≥r_2≥0`. Since `r_1≥r_2` and `r_1+r_2=2q`,
`r_1 ≥ q` always (the larger of two nonnegative numbers summing to `2q` is at
least their average `q`). Combined with `max(T) ≤ q`, this gives
`r_1 ≥ q ≥ max(T)`, so `r_1` unconditionally dominates every element of `T`
(occupies rank 1 of the full merge). Two sub-cases on `r_2`:

- **`r_2 ≤ max(T)`.** By the rank-shift-by-1 fact (applied to the singleton
  `{r_1}` dominating the rest, `T∪{r_2}`), `oddrank(R∪T) = r_1 +
  evenrank(T∪{r_2})`. By Lemma I (`r_2 ≤ max(T)`), `evenrank(T∪{r_2}) ≥ r_2`.
  Hence `oddrank(R∪T) ≥ r_1+r_2 = 2q`.
- **`r_2 > max(T)`.** Then both `r_1,r_2` exceed every element of `T`, i.e.
  `min(R) = r_2 > max(T)`, so the rank-shift-by-`s` fact applies with `s=2`
  (even): `oddrank(R∪T) = oddrank(R) + oddrank(T) = r_1 + oddrank(T)` (since
  `oddrank({r_1,r_2})=r_1`, `r_2` sits at even rank 2 within `R` alone). Using
  the hypothesis `oddrank(T) ≥ q` and `r_1 ≥ q`, `oddrank(R∪T) ≥ q+q = 2q`.

Both sub-cases give `oddrank(R∪T) ≥ 2q`. ∎

### Application: closing `k ≤ 1` with simultaneous tail-splitting, by induction on `n`

**Theorem M(n), restricted to `k≤1`.** For every `n≥1` and every refinement
`B` of `A_n` obtained by ≤`n` marks of which **at most one** splits `p_1`
(the rest, if any, refine `T_0` arbitrarily, subject only to the total mark
count being ≤`n`), `oddrank(B) ≥ p_1 = c(n)`.

*Proof.* By strong induction on `n`.

*Base case `n=1`.* `A_1={p_1,p_2}`, only 1 mark total available, so `k≤1` is
automatic (the only choices are: no mark; the mark on `p_1`; the mark on
`p_2`). If no mark: `oddrank(A_1)=p_1`. If the mark splits `p_1` into `x≥a`
(`x+a=p_1`): since `p_1=2p_2`, `x=p_1-a≥p_1-p_1/2=p_1/2=p_2`, so `x` dominates
`{a,p_2}`; by rank-shift-by-1 and Lemma I (`a≤p_2=max({p_2})`),
`oddrank = x+evenrank({p_2,a}) ≥ x+a = p_1`. If the mark splits `p_2` into
`u≥v`: `p_1>p_2≥u+v` (Lemma 2) so `p_1` dominates `{u,v}`; rank-shift-by-1
gives `oddrank = p_1+evenrank({u,v}) ≥ p_1$ (evenrank≥0). All three cases give
`oddrank ≥ p_1`; this proves M(1) in full (every case for `n=1` is covered,
not just `k≤1` — there is no `k≥2` possible when `n=1`). ∎ (base case)

*Inductive step (`n≥2`), assuming the FULL Theorem M(n−1)* (i.e. **every**
`k`, not just `k≤1`, holds for `A_{n-1}` — this is the exact ingredient we
need and do not have unconditionally for `n-1≥2`; see the honest scope
statement after the proof).

Let `B` be a refinement of `A_n` with at most one mark on `p_1` (`m_1∈{0,1}`)
and the remaining `≤n-m_1` marks refining `T_0` into some multiset `T`
(`Σ T = Σ T_0 = 1-p_1`).

- **`m_1=0`.** This is exactly Proposition A (certified, no bound on the
  number of tail marks needed at all): `oddrank(B) = oddrank({p_1}∪T) ≥ p_1`.
  Done, no induction needed for this sub-case.

- **`m_1=1`.** `p_1` is split into `R=\{x,a\}` (`x≥a≥0`, `x+a=p_1`), and `T`
  is a refinement of `T_0` using `≤n-1` marks. By self-similarity,
  `T_0=λ_n·A_{n-1}`, so `T = λ_n·T'` where `T'` is a refinement of `A_{n-1}`
  using `≤n-1` marks. By the inductive hypothesis (FULL M(n-1), applied to
  `T'`), `oddrank(T') ≥ p_1^{(n-1)}` (the top piece of `A_{n-1}`). Since
  `oddrank` is a fixed linear combination of the sorted values (Lemma 1) and
  rescaling by `λ_n>0` preserves sort order, `oddrank(T) = λ_n·oddrank(T') ≥
  λ_n·p_1^{(n-1)} = p_2` (the last equality is the defining relation of
  `λ_n`-rescaling: `T_0`'s largest element `p_2` equals `λ_n` times `A_{n-1}`'s
  largest element `p_1^{(n-1)}`, both certified in
  `lemmas/geometric-configuration-facts.md`). Also `max(T) ≤ max(T_0) = p_2`
  (refining a piece can only produce sub-pieces strictly smaller than the
  piece they came from, or leave an untouched piece unchanged, so no element
  of `T` exceeds the largest original tail piece `p_2`).

  So `T` satisfies the hypotheses of Claim ★ with `q := p_2`: `max(T) ≤ q` and
  `oddrank(T) ≥ q`. And `R = \{x,a\}` has `Σ R = p_1 = 2p_2 = 2q` and `s=|R|=2`.
  By Claim ★ (`s=2` case), `oddrank(R∪T) ≥ 2q = p_1`. Done. ∎ (inductive step,
  restricted to `m_1∈{0,1}`)

### Honest scope of this result

The inductive step above genuinely requires the **full** Theorem M(n−1) (all
`k`, i.e. including `k≥2` at level `n-1`) to bound `oddrank(T)≥p_2` when the
tail is refined via a sub-refinement of `A_{n-1}` that might itself use ≥2
marks on `A_{n-1}`'s own top piece. Since full M(n−1) is only established
unconditionally for `n-1=1` (the base case above), what is **unconditionally
proved** by this round's work is:

- **`M(2)` restricted to `m_1∈{0,1}`** (i.e., for `n=2`: `k=0` (any tail
  refinement) and `k=1` (the mark splits `p_1`, and the other mark, if used,
  refines the tail freely) both give `oddrank(B) ≥ 4/7`) — a genuinely new
  closed case (previously, `k=1` combined with simultaneous tail-splitting
  was open even for `n=2`, per round 3's outline-review). The only case left
  open for `n=2` is `k=2` (both marks split `p_1`, no marks left for the
  tail — numerically confirmed tight at `4/7` in `/tmp/round-4` working
  notes, but not proved here).
- For general `n≥3`: a **conditional** theorem — "if M(n−1) holds in full,
  then M(n) holds for `k≤1`" — which is itself a correctly proved
  implication, narrowing exactly what remains: closing `k≥2` at every level
  is necessary and (by this round's argument) sufficient to also get `k≤1`
  with simultaneous tail-splitting "for free" one level up. `k≥2` itself
  remains open for `n≥2` in all forms (tail-touched or not).

### Negative result: Claim ★ is FALSE for `s ≥ 3` — the abstraction is provably too weak

We asked whether the same clean argument extends to `s=3` (i.e. `k=2`
marks splitting `p_1`), by checking whether Claim ★'s exact hypotheses
(`max(T)≤q`, `oddrank(T)≥q`, nothing else about `T`) suffice. They do **not**:
exhaustive exact-`Fraction` random search (300,000 trials, `q` random
rational, `T` random multisets rescaled to satisfy `max(T)≤q` and
`oddrank(T)≥q` exactly, `R` a random 3-part composition of `2q`) found
concrete violations of `oddrank(R∪T)≥2q`, e.g. (exact fractions, reproducible)
`q=1/8`, `T=\{1/8\}` (so `max(T)=oddrank(T)=1/8=q`, satisfying both hypotheses
with equality), `R = \{649/4000, 116181/2000000, 59319/2000000\}` (a 3-part
composition of `2q=1/4`), giving `oddrank(R∪T) = 440681/2000000 <
1/4 = 2q`. This is a genuine, exact counterexample to Claim ★ at `s=3`, not
numerical noise (all arithmetic exact, verifiable by direct substitution).

**Diagnosis.** The reason `s=1,2` work is that `Σ R = 2q` and `s≤2` forces
`R`'s *largest* element `r_1` to be `≥q` automatically (average of `≤2`
nonnegative numbers summing to `2q`), so `r_1` is guaranteed to dominate `T`
(`≥ max(T)`, since `max(T)≤q≤r_1`) — this is exactly what let the whole
argument reduce to a rank-shift-by-1 (or by-2) computation. For `s≥3`, the
largest part of an adversarial `s`-way composition of `2q` can be made
`<q` (e.g. the equal 3-way split gives `r_1=2q/3<q`), so `r_1` need **not**
dominate `T` at all — the clean "peel the dominant piece first" mechanism
that powers Lemma I / Claim ★ has no anchor point, and the counterexample
above shows that `max(T)` and `oddrank(T)` alone genuinely do not carry
enough information about `T`'s *internal* structure to compensate. This
confirms — rigorously, via an exact counterexample, not just numerically —
that closing `k≥2` requires exploiting more of `T`'s actual structure (e.g.
its own recursive/self-similar shape as a rescaled `A_{n-2}`-refinement, not
just two scalar summaries), consistent with and sharpening the negative
finding already certified in `merge-by-sums-counterexample.md` (that a
purely-scalar sums-based induction cannot close the general gap).

### What remains open

`k≥2` (two or more of Xiang Yu's marks split Liu Bang's top piece `p_1`),
whether or not the remaining marks also refine the tail, for every `n≥2` —
this is now precisely isolated as: does `oddrank(R∪T) ≥ 2q` hold when `R` is
a composition of `2q` into `s≥3` parts, PROVIDED `T` retains the actual
recursive/self-similar structure of a (possibly further-refined) rescaled
`A_{n-1}`, not merely `max(T)≤q, oddrank(T)≥q`? This is now a sharper,
better-isolated open question than at the start of the round (we know
precisely which extra structural fact about `T` must be invoked, and we know
a whole natural class of arguments — those depending only on `max(T)` and
`oddrank(T)` — cannot possibly work, since we exhibited an exact
counterexample within that class).

## Round 5 — coordination update: Lemma L is now proved (imported, not re-derived here)

**While this build was in progress, `recursive-embedding-induction` independently
completed a full proof of Lemma L** (the `k=n`, tail-untouched sub-case), via
its peel-the-top-block induction — in fact via a strictly more general
statement, **Lemma PARITY-PAIR**, which drops the value constraint
`Σa_it_i=2t_1` entirely and needs only the parity condition "`n+m` is odd"
(automatically satisfied for Lemma L's own `m=n+1`). This is now a fully
proved, reusable result (see `recursive-embedding-induction.md`, "Round 5:
Lemma L proved in full"). Per this round's coordination directive, this
approach **imports Lemma L by reference** rather than re-deriving it, and
records here (below) the honest outcome of this round's own independent
attempt (the exchange-argument route), which — despite not itself closing
Lemma L — is a genuinely different, complementary line of investigation: it
identifies precisely *why* a bounded local-move argument could not have
closed Lemma L as easily as the peel-induction did (the exchange graph under
single elementary moves is not monotonically connected to the canonical
vertex; see the move-trap negative result below), which is useful negative
information even though the target was reached by the other approach first.

**What this means for this approach's own scope.** With Lemma L now
available, the *unique* remaining contribution expected of this approach —
extending the doubling-family conjecture from `k=n` (tail untouched) to
general `0≤k<n` **with the tail simultaneously refined** — is still open
and was not attempted this round (the round's assigned target was the
exchange-argument route on the `k=n` case specifically, per the outline).
This extension needs a version of Lemma V' (LP-vertex reduction) that
handles simultaneous adversarial splitting of *both* the top piece and the
tail, which has not been established by any approach yet (recorded as open
in `current.md`'s gap 1 and in `recursive-embedding-induction.md`'s own
"Round 5 update to gap 1"). This is flagged as the concrete next target for
this approach, rather than further exchange-argument work on `k=n`, which
this round's evidence shows is not a shortcut past the peel-induction.

## Round 5 — testing the exchange argument for the general doubling-family conjecture

This round's assigned target (per the outliner and outline-reviewer) was to
attempt the `k≥2` gap — equivalently, per the outline-reviewer's confirmed
identification, `recursive-embedding-induction`'s **Lemma L** at `k=n` — via
a single-unit exchange/local-move argument on the composition vector,
independent of that approach's peel-induction mechanism. Per the
coordination directive, this was derisked numerically first. The numerics
reveal a genuine, precise obstruction: the exchange mechanism as envisioned
in the outline does not close Lemma L in bounded form. This section states
and proves every claim rigorously (the positive lemma in full; the negative
finding by exact, reproducible counterexample; the partial positive finding
honestly scoped).

### Setup: Lemma L's exact combinatorial statement (imported, not re-derived)

We use the reduction already proved by `recursive-embedding-induction`
(Lemma V', certified there), restated here for self-containedness. Fix
`n≥1`. Normalize `t_i := 2^{n-i}` for `i=1,...,n` (so `t_1=2^{n-1}>t_2>
\cdots>t_n=1`, and `t_{i}=2t_{i+1}` for every `i<n`). For a nonnegative
integer vector `a=(a_1,\dots,a_n)` with

```
Σ_{i=1}^n a_i = n+1,        Σ_{i=1}^n a_i t_i = 2 t_1,
```

let `c_i := a_i+1` (the multiplicity of value `t_i` in the merged multiset
`T ∪ S`, where `T=\{t_1,\dots,t_n\}` is the fixed tail and `S` is Xiang Yu's
`(n+1)`-part split of the top piece assigned to anchors), and define the
alternating-sum invariant

```
D(a) := Σ_{i: c_i odd} (-1)^{C_{i-1}} t_i,   C_{i-1} := Σ_{j<i} c_j
```

(this is the exact value of `D` on the sorted merge, by the **block-parity
formula**: a maximal run of `c_i` equal copies of `t_i` starting at sorted
position `C_{i-1}+1` contributes `(-1)^{C_{i-1}}t_i` to the alternating sum
if `c_i` is odd, and `0` if `c_i` is even — a direct telescoping
computation, and exactly the formula already derived and used by
`recursive-embedding-induction`). **Lemma L** (the open sub-case) states:
`D(a) ≥ t_n` for every feasible `a`, with equality attained uniquely at the
**canonical vector** `a^\* = (1,1,\dots,1,2)` (i.e. `a^*_i=1` for `i<n`,
`a^*_n=2`).

*Verification of the block-parity formula.* We re-derived and independently
re-verified this formula from scratch (not merely re-citing it): for a
sorted list built from blocks of sizes `c_1,\dots,c_n` at values
`t_1>\cdots>t_n`, the alternating sum restricted to one block of size `c`
starting at position `p` (1-indexed) is `t\cdot\sum_{j=0}^{c-1}(-1)^{p+j+1}
= t\cdot(-1)^{p+1}\cdot[1\text{ if }c\text{ odd},\,0\text{ if }c\text{ even}]`
(a finite `\pm1` telescoping sum: an even-length run of a constant value
cancels in pairs, an odd-length run leaves exactly one copy with the sign of
its first position). Summing over blocks, with `p=C_{i-1}+1` for block `i`,
gives exactly the stated formula (`(-1)^{p+1}=(-1)^{C_{i-1}+2}=(-1)^{C_{i-1}}`).
Confirmed against direct sort-and-alternate computation on `2000+` random
integer multiplicity vectors, exact integer arithmetic, `n` up to `8` — zero
mismatches (script `block_D` vs. `D_of_multiset` in this round's working
notes).

### The Elementary Exchange Move and its exact effect on `D` (Lemma X — fully proved)

**Definition (elementary move).** The two linear constraints on `a`
(`Σa_i=n+1`, `Σa_i t_i=2t_1`) cut out an affine sublattice of `ℤ^n` of rank
`n-2`. For three indices `p<q<r`, the *elementary move at `(p,q,r)`* is the
unique (up to sign) primitive integer vector `(x,y,z)` supported on
coordinates `p,q,r` with `x+y+z=0` and `x t_p+y t_q+z t_r=0` — concretely,
writing `A:=t_q-t_r`, `B:=t_p-t_r`, `g:=\gcd(A,B)`, `(x,y,z) = (A/g,\,-B/g,\,
-x-y)`. Since every `t_i=2^{n-i}` is a power of `2`, this is an explicit
integer triple computable in closed form for every `(p,q,r)`; for
**consecutive** indices `(i-1,i,i+1)` (`t$_{i-1}=4t_{i+1}$, `t_i=2t_{i+1}`),
direct computation gives the specific primitive move `(x,y,z)=(1,-3,2)`
(applied as `a_{i-1}{+}{=}1,\ a_i{-}{=}3,\ a_{i+1}{+}{=}2`, or its negation).
Applying `+(x,y,z)` (resp. `-(x,y,z)`) to a feasible `a` at positions
`(p,q,r)` yields another point of the same affine sublattice (both
constraints preserved exactly, by construction); it is a legal *move* iff
the result has all coordinates `≥0`.

**Lemma X (exact effect formula, consecutive case).** For the consecutive
elementary move at `(i-1,i,i+1)` (`i=2,\dots,n-1`), applied to a feasible
vector `a` with `a_i≥3$ (so the forward move `+(1,-3,2)` is legal), the
resulting vector `a'` satisfies
```
D(a') - D(a) = (-1)^{a_{i-1}+1}\cdot s_0\cdot t_i,     s_0 := (-1)^{C_{i-2}(a)},
```
where `C_{i-2}(a) = Σ_{j<i-1} c_j = (i-2) + Σ_{j<i-1}a_j` is the prefix sum
strictly before position `i-1` (unaffected by the move). In particular
`|D(a')-D(a)| = t_i` exactly, and **applying the reverse move**
`-(1,-3,2)` (legal when `a_{i-1}≥1,\ a_{i+1}≥2`) **to the same vector `a`
changes `D` by the identical amount** `(-1)^{a_{i-1}+1}s_0 t_i` (not its
negative) — i.e. from a fixed vector `a`, both directions of the same
elementary move at the same position change `D` by the same signed amount.

*Proof.* Write `α:=a_{i-1}` (so `c_{i-1}=α+1`), `β:=a_i`, `γ:=a_{i+1}`, and
let `s_0:=(-1)^{C_{i-2}}` (a quantity depending only on `a_1,\dots,a_{i-2}`,
untouched by the move). The move sends `(c_{i-1},c_i,c_{i+1})` from
`(α+1,\,β+1,\,γ+1)` to `(α+2,\,β-2,\,γ+3)` (since `Δc_j=Δa_j=(+1,-3,+2)`).

*Prefix sums.* `C_{i-1}^{\rm old}=C_{i-2}+(α+1)`, so `C_{i-1}^{\rm new}
=C_{i-2}+(α+2)=C_{i-1}^{\rm old}+1` — parity **flips**. `C_i^{\rm old}
=C_{i-1}^{\rm old}+(β+1)`, `C_i^{\rm new}=C_{i-1}^{\rm new}+(β-2)
=C_{i-1}^{\rm old}+1+β-2=C_i^{\rm old}-2` — parity **unchanged**.
`C_{i+1}^{\rm new}=C_i^{\rm new}+(γ+3)=C_i^{\rm old}-2+γ+3=C_{i+1}^{\rm old}`
exactly — recovered, consistent with the total count being preserved past
index `i+1`. Hence: the sign used for term `i-1` (`(-1)^{C_{i-2}}=s_0`) is
unaffected by the move; the sign used for term `i` (`(-1)^{C_{i-1}}`)
flips; the sign used for term `i+1` (`(-1)^{C_i}`) is unaffected.

*Term `i-1`* (value `t_{i-1}=2t_i`): contributes `[c_{i-1}\text{ odd}]\,s_0\,
t_{i-1}`. Old: `c_{i-1}=α+1`, so indicator is `[α\text{ even}]`. New:
`c_{i-1}=α+2`, indicator `[α\text{ odd}]`. Change
`=\big([α\text{ odd}]-[α\text{ even}]\big)s_0\,(2t_i) = (-1)^{α+1}s_0\,(2t_i)`
(using the convention `[α\text{ odd}]-[α\text{ even}]=+1` if `α` odd,
`-1` if `α` even, i.e. `=(-1)^{α+1}`).

*Term `i`* (value `t_i`): let `s_1:=(-1)^{C_{i-1}^{\rm old}}=s_0\cdot
(-1)^{\alpha+1}` (using `C_{i-1}^{\rm old}=C_{i-2}+\alpha+1`). Old
contribution: `[c_i\text{ odd}]\,s_1\,t_i = [β\text{ even}]\,s_1\,t_i` (since
`c_i^{\rm old}=β+1`). New: sign is `-s_1` (flipped), and `c_i^{\rm new}
=β-2$, indicator `[β\text{ even}]` — **the same indicator as the old term**.
So new contribution `=[β\text{ even}]\,(-s_1)\,t_i`. Change `=[β\text{
even}]\big((-s_1)-s_1\big)t_i = -2[β\text{ even}]\,s_1\,t_i`? — this would
depend on `β`'s parity, contradicting the claimed clean formula, so we must
also handle `β` odd: if `β` odd, `c_i^{\rm old}=β+1` even (indicator `0`,
old contribution `0`); `c_i^{\rm new}=β-2` odd (indicator `1`, new
contribution `-s_1 t_i`); change `=-s_1t_i-0=-s_1t_i`. If `β` even,
`c_i^{\rm old}=β+1` odd (old contribution `s_1t_i`); `c_i^{\rm new}=β-2`
even (indicator `0`, new contribution `0`); change `=0-s_1t_i=-s_1t_i`.
**Both parities give the same change**, `-s_1t_i` — the case split
collapses to a single value (the apparent parity-dependence above was an
error from conflating the indicator functions; correctly, in each of the
two parities of `β` exactly one of old/new contributes, and it is always
the term carrying `-s_1t_i` net). So `Δ(\text{term }i) = -s_1t_i =
-s_0(-1)^{\alpha+1}t_i = s_0(-1)^{\alpha}\,t_i`.

*Term `i+1`* (value `t_{i+1}=t_i/2`): both the indicator (`c_{i+1}` parity
unchanged, `+3` shifts by an odd amount — wait, `Δc_{i+1}=+2`, even, so
parity of `c_{i+1}` is unchanged) and the sign (`(-1)^{C_i}` unchanged, shown
above) are unaffected: `Δ(\text{term }i{+}1)=0`.

*Total.*
```
ΔD = Δ(\text{term }i{-}1)+Δ(\text{term }i)+Δ(\text{term }i{+}1)
   = (-1)^{α+1}s_0(2t_i) + (-1)^{α}s_0\,t_i + 0
   = s_0 t_i\Big[2(-1)^{α+1}+(-1)^{α}\Big]
   = s_0 t_i (-1)^\alpha\big[-2+1\big] = -s_0t_i(-1)^\alpha = s_0t_i(-1)^{α+1}.
```
This is exactly `ΔD=(-1)^{a_{i-1}+1}s_0t_i`, the formula claimed. This
closed-form derivation was independently cross-checked against, and matches
exactly, `2000` random exact-integer trials (`n=8`, random legal move
positions), comparing directly-recomputed `D(a')-D(a)` (full block-parity
recomputation on both `a` and `a'`, no shortcuts) against the predicted
value — zero mismatches.

*Reverse move.* Applying `-(1,-3,2)` to `a` (legal when `α\ge1,\gamma\ge2`)
produces `a_{\rm rev}` with `a_{\rm rev}+(1,-3,2)=a`, i.e. `a` is obtained
from `a_{\rm rev}` by the *forward* move. Applying the formula just proved
with `a_{\rm rev}$ playing the role of the "old" vector (whose `(i-1)`-th
coordinate is `α-1`, and whose prefix sign `s_0` is identical to `a`'s,
since coordinates `<i-1` are untouched by the move):
`D(a)-D(a_{\rm rev}) = (-1)^{(α-1)+1}s_0t_i=(-1)^{α}s_0t_i`. Hence
`D(a_{\rm rev})-D(a) = -(-1)^\alpha s_0 t_i = (-1)^{α+1}s_0t_i` — **exactly
the same signed quantity** as the forward move's effect computed at `a`
itself. This proves the reverse-move claim directly from the forward
formula, with no separate computation needed. `\blacksquare`

### Negative result: bounded single elementary moves do not connect every vertex to the canonical minimum

**Definition.** Say a feasible vector `a` (for Lemma L's constraints, fixed
`n`) is a **move-trap** if `a≠a^*` (not canonical) but no elementary move —
forward or reverse, at *any* triple of indices `p<q<r$ (not only consecutive
ones) — applied to `a` yields a feasible vector `a'` with `D(a')<D(a)`.

**Fact (verified by exhaustive exact computation, not sampling).** For
`n=5`, the vector `a=(0,2,4,0,0)` (feasible: `Σa_i=6=n+1`, `Σa_it_i=
0\cdot16+2\cdot8+4\cdot4+0\cdot2+0\cdot1=32=2t_1$; `D(a)=11`, computed via
the block-parity formula and cross-checked by direct sort-and-alternate
computation) **is a move-trap**: we enumerated all `\binom{5}{3}=10` index
triples `(p,q,r)`, computed the primitive elementary move at each (via the
closed-form `(x,y,z)` above), and checked both `\pm(x,y,z)` applied to `a`
at every triple — in every one of the `20` resulting candidate vectors,
either the result has a negative coordinate (infeasible) or its `D`-value is
`\ge 11$ (no strict decrease). (Full enumeration script and output recorded
in this round's working notes; the target value is `t_5=1$, so `a` is far
from optimal, `D(a)=11\gg1$, yet is completely stuck for single elementary
moves.) The same phenomenon recurs at every tested `n\in\{6,7,8\}`
(additional move-traps found: `n=6`: `(0,2,3,2,0,0)$, `D=19`; `(1,0,2,4,0,0)`,
`D=11`; `n=7`: three further traps; `n=8`: five further traps — full lists
recorded in working notes, all confirmed by exhaustive triple-enumeration,
not partial search).

**Consequence.** The outline's proposed mechanism — "moving one unit of
multiplicity between adjacent (or, more generally, any) coordinates never
increases `oddrank(merge)`, with the canonical vector the unique local hence
global minimum by connectivity of the exchange graph" — is **false as
stated** for the natural minimal notion of "single-unit exchange" (any
single primitive elementary move, consecutive or not): the exchange graph
under single elementary moves is **not** connected-with-monotone-`D` to the
canonical vertex from every feasible vertex; genuine local minima (in the
single-move sense) exist away from the canonical vector. This is a precise,
reproducible negative finding, not a failure to search hard enough — the
search was exhaustive over all `\binom{n}{3}` index triples and both move
directions at each verified trap.

### Partial positive finding: composed moves escape every tested trap, but with growing width

We tested whether **composed** moves (sums of several elementary moves,
applied as a single combined step, i.e. allowing intermediate infeasible
states) rescue the mechanism. Result: **every move-trap found above is
resolved by a composed move of bounded but growing width**:
- `n=5` trap `(0,2,4,0,0)`: resolved by a width-`2` composed move (two
  consecutive-index elementary moves combined) to `(1,0,3,2,0)`, `D=7<11`.
- `n=6` traps: both resolved at width `2`.
- `n=7` trap `(0,0,8,0,0,0,0)$, `D=43`: **not** resolved at width `2`; found
  resolved at width `3$, reaching `(0,2,3,1,2,0,0)`, `D=35<43`.
- `n=8` trap `(0,0,7,2,0,0,0,0)$, `D=75`: **not** resolved at width `2` or
  `3`; found resolved at width `4`, reaching `(1,0,0,8,0,0,0,0)`, `D=43<75`
  (which is itself further resolved by additional composed moves, in a
  chain, down to the canonical vector).

So a chain of composed moves *does* reach the canonical vector with `D`
strictly decreasing at each composed step, in every case tested — but the
**width of the composed move needed to escape a given trap grows with how
far that trap is from the canonical vector** (concretely, with `n` in the
tested range `5\le n\le8`, the maximum width needed grew from `2` to `4`).
We did not find a bound on this width independent of `n`, nor a formula
predicting the needed width from `a` directly; extrapolating the trend, the
required width plausibly grows at least linearly in `n` in the worst case
(the traps found are increasingly extreme — mass concentrated at a single
low index — as `n` grows, and these are exactly the cases needing the
widest composed moves).

### Honest conclusion of this round's exchange-argument attempt

**This round did not close Lemma L (equivalently, the `k=n` core of the
general doubling-family conjecture) via the exchange mechanism.** The
precise, rigorously-established reason: the natural "bounded local move,
connectivity implies global minimum" argument sketched in the outline is
**false** for the minimal notion of local move (single elementary move, any
index triple) — genuine traps exist, exhaustively verified. A *repaired*
version of the argument (composed moves of unboundedly growing width)
appears numerically to work in every tested case, but proving that such a
composed-move chain *always* exists and *always* terminates at the
canonical vector, for **every** `n` and **every** non-canonical feasible
vector, is a claim of essentially the same depth and difficulty as
`recursive-embedding-induction`'s peel-induction on Lemma L directly (both
require tracking how mass redistributes across the *whole* index range as
`n` grows, not a bounded neighborhood) — i.e., this round's finding is that
**the exchange-argument route, as scoped, is not actually a genuinely
easier or shorter path to Lemma L than the peel-induction route already
being pursued in parallel**; it is at best an equally-hard reformulation,
and at worst (given the unresolved sign-bookkeeping fragility noted in
Lemma X's proof, and the unbounded-width composed-move gap) a harder one to
push to full rigor. Per the outline-reviewer's own coordination directive
("if one lands a certified Lemma L first, the other should import it by
reference... neither should re-do this if the other's proof is already
certified"), and given this round's finding that the exchange route is not
ahead, **this approach should not continue independently re-deriving Lemma
L via exchange**; it should import Lemma L by reference once
`recursive-embedding-induction` (or any other approach) certifies it, and
redirect further effort on this approach's unique contribution — extending
from `k=n` to general `k<n$ with the tail also refined — once that import is
available, rather than continuing to search for a bounded exchange
argument that this round's evidence suggests does not exist in bounded
form.

**What remains open from this round's work specifically:**
1. Lemma L itself (imported target, not re-derived here) — still open.
2. Whether the composed-move width needed to escape a trap is bounded by
   any function of `n` (let alone proved to always terminate at canonical)
   is open; only numeric evidence up to `n=8` exists.
3. `k<n` and tail-refined extensions of the doubling-family conjecture were
   not attempted, gated on `k=n` (Lemma L).

(Lemma X's sign convention, initially derived with an error that was caught
and corrected in-place above, is now a fully clean, self-contained hand
proof — no longer an open item; it matches the independent 2000-trial exact
computational check exactly.)

## Round 6: re-scoping (exchange route retired; unique remaining target)

The round-5 exchange/move-trap negative result (bounded-width single moves
provably cannot prove Lemma L, confirmed by explicit traps) plus this
approach's now-mandatory import of Lemma L from `recursive-embedding-
induction` (proved there first, independently) means this approach's
*only* remaining unique scope was "`k<n`, tail simultaneously refined" —
which is now **the same target** `recursive-embedding-induction` is
attacking this round via Lemma PARITY-PAIR-GEN (a direct, working
generalization of its own certified Lemma PARITY-PAIR). Continuing to
pursue that target here via the exchange-move mechanism would be pursuing
an already-falsified mechanism on an already-claimed target — both a dead
end and a duplication.

**Decision: re-scope, not merge or retire.** This approach keeps its own
slug (it still carries live, load-bearing, unique-to-it certified content —
Lemma I, the rank-shift-by-`s` fact, Claim ★ for `s∈{1,2}`, and Lemma X/the
move-trap negative result) but its **live target for round 6 changes** to
the one concrete open item that is genuinely its own and not claimed by any
sibling: the **"one free coordinate" vertex case of Lemma V'**
(`recursive-embedding-induction`'s gap (1) — closing Proposition K fully,
i.e. every possible split of `p_1` into `n+1` parts with the tail
untouched, not just the "pure-anchor" vertices already handled by Lemma
PARITY-PAIR). `recursive-embedding-induction` has explicitly ceded this
item to focus on PARITY-PAIR-GEN this round (see its file).

**Skeleton for the free-coordinate case.** Lemma V' currently reduces the
tail-untouched sub-case to finitely many "pure-anchor" vertices of the
split polytope (each coordinate of the split either 0 or forced by the
running peel order). The uncovered vertices instead have exactly **one**
coordinate free (not pinned to 0 or to the peel-forced value) — geometrically,
an edge of the polytope rather than a vertex, or a vertex reached by a
different active-constraint set. Concretely: adapt Lemma D-INSERT (the
exact single-insertion recursion for `D`, already certified, shared
machinery with `recursive-embedding-induction`) to bound `D` along the
one-parameter family swept by the free coordinate directly, rather than
assuming it is pinned; the endpoints of that one-parameter sweep should
reduce to already-covered pure-anchor vertices (giving a base case), and
the question sketched-but-unresolved in prior rounds — *is the free
coordinate's configuration actually reachable under the sum constraint
`Σa_i t_i = 2t_1`?* — must be settled first (a small, concrete
feasibility check, not open-ended). This is a narrower, self-contained
target than PARITY-PAIR-GEN and should not require re-deriving any of the
already-certified toolkit (D-REFORM/D-BOUND/D-INSERT/PARITY-PAIR are all
directly reusable, shared with the sibling approach).

## Round 8 — Lemma CROSS-TIE-AFFINE: an independent affine-slope route to gap (b)

**Target.** `recursive-embedding-induction`'s Lemma V'-GEN (the
multi-free-coordinate vertex reduction feeding into Lemma PARITY-PAIR-GEN,
`recursive-embedding-induction.md`, Step 2) is proved in the "well-separated"
case (every free coordinate's global sorted neighbors are anchors, not
other free coordinates) but leaves the "cross-piece tie" case open: a free
coordinate `x` (from split piece `π`) whose immediate sorted neighbor is a
*different* free coordinate `x'` (from split piece `π'≠π`, no anchor
between them). This round's outline assigns this approach a second,
independent route to the same open gap — direct two-variable slope
computation, rather than `recursive-embedding-induction`'s shared-block
combinatorics.

### Setup (recalled from `alternating-sum-toolkit.md` and
`lemma-V-prime-free-coordinate.md`)

Fix `n≥1`, `t_i:=2^{n-i}` for `i=1,\dots,n` (`t_1=2^{n-1}>\cdots>t_n=1`,
and `t_i=2t_{i+1}` for `i<n` — Lemma S). Xiang Yu's strategy assigns each
of Liu Bang's `n+1` original pieces of `A_n` (the top piece, total `2t_1`,
and the `n` tail pieces, totals `t_1,\dots,t_n`) either untouched, or split
by some number of his ≤`n` marks into several parts; let `π` range over
the pieces he actually splits. For a sort-order cell in which `π`'s parts
have (at most) one strictly-non-anchor value `x` (all others of `π`'s parts
pinned to specific anchors — the vertex-reduction fact, `n_π-2` of `π`'s
`n_π` parts pinned when `n_π≥3`, or `π`'s whole single degree of freedom
when `n_π=2`), `D` restricted to the cell is affine in `x` by Lemma
D-INSERT (`alternating-sum-toolkit.md`).

### Lemma CROSS-TIE-AFFINE (general `k`-piece cluster, fully proved)

**Statement.** Let `π_1,\dots,π_k` (`k≥2`) be distinct split pieces, each
contributing exactly one coordinate `y_1,\dots,y_k` currently tied at a
common value `v`, with `v` strictly between two consecutive anchors
`t_{j+1}<v<t_j` (with the convention `t_0:=+\infty`, `t_{n+1}:=0`), and
suppose no anchor lies between `v` and the endpoints of the interval over
which `v` can move while every `y_l`'s global rank-relationship to
everything *except the other tied `y_m`'s* stays fixed (the "cell").
**Then, on this cell (an interval `v\in(\ell,u)$ containing the tie), `D`
is an affine function of `v` with an explicit integer slope**
```
M := Σ_{l=1}^k m_l,      m_l :=
  σ_l                              if π_l has ≥3 parts (all others pinned),
  σ_l - σ_l'                       if π_l has exactly 2 parts (companion
                                    `c_l = \mathrm{top}_{π_l} - v` co-varies),
```
where `σ_l:=(-1)^{r_l+1}` is the sign contributed by `y_l`'s current global
sorted rank `r_l`, and (in the 2-part case) `σ_l'` is the sign contributed
by the companion `c_l`'s current rank. Consequently `D(v)$ attains its
minimum, over the whole cell, **at one of the cell's two endpoints** — the
tie is never a *strict* local minimizer of `D`; the interior tie ties or
loses to at least one endpoint.

*Proof.* Write `C_{\rm bg}$ for every coordinate of the merge *other than*
`y_1,\dots,y_k` and, for the 2-part pieces, their companions
`c_1,\dots,c_{k'}` ($k'\le k$ of the `k` pieces are 2-part) — but the
companions themselves are functions of `v`, not independent background, so
more precisely: fix the SORTED ORDER of `\{y_1,\dots,y_k\}\cup
\{c_1,\dots,c_{k'}\}` relative to each other and to every anchor other than
`t_{j+1},t_j`. Since all of `y_1,\dots,y_k` share the value `v`, and each
`c_l=\mathrm{top}_{π_l}-v` is a fixed affine (in fact linear, slope `-1`)
function of `v`, this relative order is determined for `v` in a
sufficiently small punctured neighborhood of the tie and stays fixed as
long as no two of these quantities cross each other or an anchor. Every
element outside `\{y_1,\dots,y_k,c_1,\dots,c_{k'}\}$ then occupies a rank
that changes only by shifts of the *total count* of the tied-plus-companion
block below/above it — a fact used only to confirm `D`'s dependence on that
block is *exactly* the sum of each individual element's own signed
contribution `\pm(\text{value})` at its own current rank, since — by the
identical argument used in `lemma-V-prime-free-coordinate.md`'s Step 1 and
independently re-verified here by direct computation on 5000 random exact-
`Fraction` background-list instances (`/tmp/verify_formula.py`, zero
mismatches) — repeatedly applying D-INSERT to insert each element of the
block one at a time, in sorted order, into the fixed background gives
`D = D(\text{everything else}) + \sum(\pm\text{element})`, with each sign
determined purely by *that element's own rank within the block*, which for
`y_l$ is `\sigma_l$ (constant on the cell) and for `c_l$ is `\sigma_l'$
(constant on the cell, since crossing a rank boundary is exactly what
defines the cell's edge).

Each `y_l=v$ contributes `\sigma_l\cdot v$; each companion `c_l=
\mathrm{top}_{π_l}-v` contributes `\sigma_l'\cdot(\mathrm{top}_{π_l}-v) =
\sigma_l'\mathrm{top}_{π_l} - \sigma_l'v$, i.e. a *constant* (in `v`) plus
`-\sigma_l'v`. Summing over the whole block: `D(v) = (\text{constant}) +
\big(\sum_l \sigma_l - \sum_{l\in\text{2-part}}\sigma_l'\big)v`, exactly
the claimed affine formula with slope `M`. An affine function on a bounded
interval `[\ell,u]` attains its minimum at `\ell` or `u` (elementary
calculus: `D(v)=D(\ell)+M(v-\ell)$, monotone in `v` unless `M=0`, in which
case constant, i.e. the minimum is ALSO attained, trivially, at both
endpoints). `∎`

*Independent computational verification (the pairwise `k=2$ case).* We
re-derived the `k=2$, "background fixed, no companions" special case of
this formula from scratch as `D(y,y')=D(C_{\rm bg})+\sigma|y-y'|` (`σ:=
(-1)^{r+1}`, `r$ the global rank of `\max(y,y')`) and checked it against
5000 random exact-`Fraction` trials of background lists (any size `0$-`6`,
any anchor gap): **zero mismatches** (`/tmp/verify_formula.py`). We also
directly re-verified the `n=2` genuine cross-tie example from the
round-8 explorer's report end to end (`/tmp/verify_n2.py`): `P_1$ split
into 2 parts (1 mark) tied with a split tail piece's free part (1 mark);
`D(v) = -2v+C$, exactly affine, ranging from `D=3` at `v\to1^+$ down to
`D=1=t_2$ at `v=2=t_1` (the anchor endpoint) — matching the explorer's
reported cross-tie value `D=3` (the *non-minimizing* endpoint) exactly, and
independently confirming the true minimum `D=1` is achieved at the
anchor-snapped endpoint, not at the interior tie. We repeated this for the
explorer's `n=3` example (`/tmp/verify_n3.py`): again exactly affine
(`D(v)=-2v+C$), ranging from `D=3` (at `v\to1^+$) to `D=1=t_3` at the
anchor endpoint `v=2=t_2$ — again matching the reported figures exactly and
confirming the true minimum sits at the anchor endpoint.

### The "self-meeting point is always an anchor" fact (new, fully proved) — closes the "majority-part" and "≥3-part" sub-cases with zero residue

**Fact.** For any piece `π` of `A_n$ that Xiang Yu splits with exactly one
mark (2 parts, `y+c=\mathrm{top}_π$), the point `v=\mathrm{top}_π/2$ (where
`y=c`, i.e. `π`'s two parts coincide) is *itself always an anchor*: if
`\mathrm{top}_π=t_i$ (an untouched tail piece before this split), then
`\mathrm{top}_π/2=t_i/2=t_{i+1}$ exactly (Lemma S, `t_i=2t_{i+1}`); if
`\mathrm{top}_π=2t_1$ (`π$ is the top piece `P_1$ itself), then
`\mathrm{top}_π/2=t_1$ exactly.

*Proof.* Immediate from Lemma S (`t_i=2t_{i+1}` for `i<n`, and by
definition `\mathrm{top}(P_1)=2t_1`, so `\mathrm{top}(P_1)/2=t_1`). `∎`

**Consequence: whenever the affine cell's endpoint that Lemma
CROSS-TIE-AFFINE pushes towards is `π`'s own self-meeting boundary (i.e.
whenever `y=v` is playing the *majority* — larger-or-equal — role among
`π`'s two parts, so `v` ranges down to `\mathrm{top}_π/2` before it could
range down to any deeper external anchor), the resulting endpoint
configuration is fully anchor-resolved with *zero residue*: `y` and its
companion `c` become simultaneously equal to the *same* anchor
(`t_{i+1}` or `t_1` as appropriate), an even-multiplicity block — this is
*exactly* the "shared block, contributes `0`, even-multiplicity"
mechanism `recursive-embedding-induction`'s own outline independently
proposed as the needed generalization of its certified Lemma
PARITY-PAIR-GENERAL Case A, now derived here by an entirely different
(explicit slope/self-meeting) route, cross-confirming their mechanism
without importing it.** Likewise, whenever `π` has `≥3$ parts (so `π`'s
*other* coordinates besides the tied one are already independently pinned
to fixed anchors, not co-varying), pushing `v$ to *either* external anchor
`t_j$ or `t_{j+1}$ trivially yields a fully anchor-resolved configuration
(no companion at all) — this is exactly `recursive-embedding-induction`'s
already-closed well-separated single-free-coordinate case (their "Peeling
induction" section), reproduced here as a special case (`k=1$) of Lemma
CROSS-TIE-AFFINE's own formula (`m_1=\sigma_1$, no companion term).

**In both of these sub-cases, gap (b) is therefore fully closed:** the
cross-tie (or single free coordinate) is dominated (weakly, with equality
possible) by an anchor-only configuration at the *same* mark budget,
reducing entirely to the anchor-only case (gap (a), `recursive-embedding-
induction`'s remaining target) or to the already-certified full-budget
anchor case (Lemma PARITY-PAIR-ANCHOR / Lemma L).

### The one residual sub-case, precisely isolated (honest, not closed)

**When `v` is playing the *minority* (strictly smaller) role among a
2-part piece `π`'s two parts, in a bracket `(t_{j+1},t_j)` strictly below
`π`'s own natural halving level** (i.e. `t_j < \mathrm{top}_π/2$, so `v`
would have to cross the external anchor `t_j` — or `t_{j+1}` — *before*
ever reaching `π`'s self-meeting point `\mathrm{top}_π/2`), Lemma
CROSS-TIE-AFFINE still correctly identifies the D-minimizing endpoint (an
external anchor), but the companion `c=\mathrm{top}_π - (\text{that
anchor})` is now a **fixed, but generically non-anchor**, real number —
e.g. `\mathrm{top}_π=t_i` and the winning endpoint is `t_j` with `j>i+1`,
giving `c=t_i-t_j=2^{n-j}(2^{j-i}-1)`, which is a power of `2` (hence an
anchor) only when `j-i=1` — i.e. only in the already-closed "aligned" case.
This is a **genuinely new residue phenomenon**, not present in the
narrower Proposition K / Lemma FC setting (there, `π=P_1` always has
`\ge n+1\ge3$ parts for `n\ge2$, so the "exactly 2 parts" case with its
self-meeting subtlety never arose). Closing this fully — showing the
resulting configuration (fully-resolved but with one non-anchor "residue"
value floating in the merge) still satisfies `D\ge t_n$ — was **not
completed this round**.

*Partial evidence it is not a real threat.* A concrete probe at `n=5`
(`/tmp/verify_residue.py`: `P_1` split by 1 mark into a large part `\approx
32-v` and small part `v`, tied with the free part of splitting the tail
piece `t_3=4` into 2 parts, `v` ranging in the deep bracket `(t_5,t_4)=
(1,2)`, several levels below `P_1`'s own natural halving level `16=t_1`)
found the affine slope `M=0` identically throughout the tested bracket,
with `D\equiv21` far above `t_5=1` — the whole family is flat and grossly
non-competitive, so this particular instance poses no threat to the
`D\ge t_n` target, but this is one numeric instance, not a general
argument, and the slope need not always vanish in this residual sub-case
(only observed to here).

### Reconciliation with `recursive-embedding-induction`'s route (required by this round's outline)

Per the outline-reviewer's explicit coordination directive, we checked for
disagreement between the two independent routes to gap (b). **No
disagreement found.** Both routes conclude: (1) a genuine interior cross-
tie is never a *strict* global minimizer of `D` (this route: proved via an
explicit affine-slope argument with an exact formula for the slope;
`recursive-embedding-induction`'s route: via a shared-block/tree-peeling
argument); (2) the natural reduction is to treat the tied pair as an
even-multiplicity shared block at a common anchor (this route derives this
*independently*, via the self-meeting-point fact, in the "majority-part or
≥3-part" sub-case; `recursive-embedding-induction`'s outline independently
proposed exactly this same mechanism as the needed generalization of their
own Case A). This route additionally identifies a **sharper, previously
unnoticed residual sub-case** (the "minority-part, deep-bracket" scenario)
that `recursive-embedding-induction`'s own writeup does not separately
flag — this is new information for the population, narrowing (not
widening) what remains of gap (b): it is no longer "cross-ties in
general," but specifically this one residue phenomenon.

## Full proof
(Not present — Status is `partial`. Fully proved and reusable this round:
Lemma I (Insertion Lemma, general), the rank-shift-by-s fact, Claim ★ for
`s∈{1,2}`, and their combination closing `k≤1` with simultaneous
tail-splitting unconditionally for `n≤2` and conditionally for general `n`
(conditional on the full theorem at `n-1`). Also proved: an exact
counterexample showing Claim ★ is false for `s≥3`, ruling out the natural
generalization. The remaining gap — `k≥2`, general `n` — is precisely
restated above. The upper-bound half over arbitrary Liu Bang configurations
is not attempted by this approach (deferred to `universal-adversary-strategy`).
Proposition K is fully closed (round 6). Round 8 proves Lemma CROSS-TIE-
AFFINE (gap (b), the majority-part/≥3-part sub-cases fully closed with zero
residue) and precisely isolates the one remaining residual sub-case
(minority-part, deep-bracket ties) — see "Round 8" above for full detail.
Round 9 proves Lemma TWO-BLOCK and the Structural Lemma, closing that
residual sub-case unconditionally for every `n` (the "all-minority,
all-exactly-2-parts" tie scenario) — see "Round 9" below. Combined with
Lemma CROSS-TIE-AFFINE and `recursive-embedding-induction`'s
already-closed cases, gap (b) is closed except for one narrow,
not-separately-checked edge (a `≥3`-part piece with more than one of its
own coordinates tied at independently different values) — see "Round 9"
for the precise honest scope statement.

## Promotable lemmas (round 9 additions)
- **Lemma TWO-BLOCK**: for any sorted nonnegative list and any threshold
  `v`, splitting into `Y` (`>v`) and `Z` (`\le v`),
  `D(\text{list})\ge (b_1-b_2)-v\cdot[\,|Y|\text{ odd}\,]` where `b_1,b_2`
  are `Y`'s two largest elements — fully general (no geometric structure),
  proved by a double application of the already-certified Lemma D-BOUND.
  Reusable by any approach needing a quick, direct lower bound on `D` from
  only the two largest elements above a cut and D-BOUND's crude tail
  estimate. Certified to `lemmas/two-block-residue-close.md`.
- **Structural Lemma (two-largest-elements identification) + Main
  Theorem (residual cross-tie closure)**: for the "all-minority,
  all-exactly-2-parts" cross-tie configuration (any `S\subseteq\{0,\dots,
  n\}`, `|S|\ge2`, common tie value `v` in the legal minority range), the
  two globally-largest merged pieces are `2t_1-\varepsilon_0v,\
  t_1-\varepsilon_1v`, and consequently `D(B)\ge t_n` unconditionally for
  every `n\ge1` and every such `v` — closes the previously-open
  minority-part/deep-bracket residue sub-case of gap (b) (Lemma V'-GEN),
  independently of and via a different mechanism than `recursive-
  embedding-induction`'s forest-extension route. Certified to
  `lemmas/two-block-residue-close.md`.

## Promotable lemmas (round 8 additions)
- **Lemma CROSS-TIE-AFFINE**: for any cluster of `k≥2` mutually tied free
  coordinates from distinct split pieces, `D` is affine in the shared tie
  value with an explicit computable integer slope `M` (formula given
  above), so the tie is never a strict local minimizer — proved in full,
  independently verified by exact-`Fraction` computation (5000 random
  background-list trials for the pairwise formula, plus exact
  reproduction of the round-8 explorer's `n=2,3` cross-tie examples).
  Reusable by `recursive-embedding-induction` (or any future approach) for
  Lemma V'-GEN's general-case closure.
- **Self-meeting-point-is-an-anchor fact**: for any 2-part-split piece `π`
  of `A_n` (total `t_i` or `2t_1`), the point where its two parts coincide
  (`\mathrm{top}_π/2`) is always exactly an anchor (`t_{i+1}` or `t_1`) —
  a direct one-line consequence of Lemma S (`t_i=2t_{i+1}`), but not
  previously stated or exploited; it is the reason the "majority-part"
  cross-tie sub-case reduces to a zero-residue anchor block. Fully proved,
  reusable.

## Promotable lemmas (round 4 additions)
- **Lemma I (Insertion Lemma)**: for any finite nonempty nonnegative multiset
  `T` and any `a∈[0,max(T)]`, `evenrank(T∪{a}) ≥ a`. Fully proved above, no
  geometric structure assumed — a clean, general, structure-free fact,
  strictly generalizing (and correctly isolating the truly general content
  of) round 2's Lemma F1 computation. Reusable by any approach doing
  rank-shift bookkeeping (in particular `recursive-embedding-induction`'s
  planned Lemma R, and `universal-adversary-strategy`'s DOM/HALVE/PEEL
  family, all of which are instances of the same mechanism).
- **Rank-shift-by-s fact**: if every element of `R` dominates every element
  of `T`, `oddrank(R∪T) = oddrank(R) + oddrank(T)` (`|R|` even) or
  `oddrank(R) + evenrank(T)` (`|R|` odd). Fully proved, fully general.
- **Claim ★ (`s=1,2` cases)**: abstract reduction (stated fully above) proved
  in full for `s≤2`, together with the exact counterexample establishing it
  is false for `s≥3` — the negative half is itself a reusable, certified fact
  (rules out an entire class of "scalar-summary-only" arguments for `k≥2`,
  reusable by `recursive-embedding-induction`, whose Lemma R faces exactly
  this same three-regime case split).

## Promotable lemmas (round 5 additions)
- **Lemma X (elementary exchange move effect formula)**: for Lemma L's
  integer-vector combinatorial setting (`a_1,\dots,a_n≥0`, `Σa_i=n+1`,
  `Σa_it_i=2t_1`, `t_i=2^{n-i}`), the minimal legal move at three consecutive
  indices (`a_{i-1}{+}{=}1,\ a_i{-}{=}3,\ a_{i+1}{+}{=}2`, or its negation)
  changes the alternating-sum invariant `D` by *exactly*
  `ΔD=(-1)^{a_{i-1}+1}(-1)^{C_{i-2}}t_i` — proved in full by a clean,
  self-contained closed-form derivation (an initial hand-algebra error was
  caught and corrected in-place this round) and independently confirmed
  against 2000 exact-integer trials, zero mismatches. Also proves that the
  reverse move (applied to the same starting vector) changes `D` by the
  *identical* signed amount as the forward move — a genuinely
  counter-intuitive but fully proved fact about this move family. Reusable
  by any approach doing further exchange-argument or local-move analysis on
  Lemma L's combinatorial structure (in particular useful groundwork for
  `recursive-embedding-induction` if it later wants an exchange-style
  cross-check of its peel-induction).
- **Move-trap negative result**: explicit, exhaustively-verified feasible
  vectors for Lemma L's polytope (e.g. `n=5`, `a=(0,2,4,0,0)`) from which no
  single elementary move (any index triple, either direction) strictly
  decreases `D`, despite `D(a) > t_n` (i.e. `a` is far from the true
  minimum) — rules out, by explicit counterexample rather than failure to
  search, the "single local move + connectivity" mechanism as a viable
  bounded-width proof strategy for Lemma L / the doubling-family
  conjecture. Reusable as a documented negative result for any future
  attempt at an exchange-argument proof of Lemma L, to prevent re-attempting
  the same falsified mechanism.

## Round 9: closing the minority-part residue sub-case via a direct two-block D-BOUND estimate

**Target this round**: the same last sub-case of gap (b) that
`recursive-embedding-induction` is attacking via forest extension this
round — kept as a genuinely separate route per CLAUDE.md's reconciliation
requirement. Where the round's plan anticipated needing Lemma CROSS-TIE-
AFFINE's affine/endpoint reduction plus a crude D-BOUND split, the
mechanism that actually worked is simpler and more general: a **direct
two-block estimate applied to the two globally-largest merged pieces**,
valid at *every* point of the tie's interior, not just the affine cell's
endpoint.

### Lemma TWO-BLOCK (fully general, no geometric structure)

For any sorted nonnegative list `L` and threshold `v\ge0`, split
`L=Y\cup Z` (`Y:=` elements `>v`, `Z:=` elements `\le v`). Writing `Y`'s two
largest elements `b_1\ge b_2` (`b_2:=0` if `|Y|\le1`):
```
D(L) \ge (b_1-b_2) - v\cdot[\,|Y|\text{ is odd}\,].
```
*Proof.* Every element of `Y` exceeds every element of `Z`, so the
rank-shift-by-`s` fact gives `D(L)=D(Y)+(-1)^{|Y|}D(Z)`. Peeling `Y`'s top
element, `D(Y)=b_1-D(Y\setminus\{b_1\})`, and `D(Y\setminus\{b_1\})\in
[0,b_2]` by the certified **Lemma D-BOUND** (`lemmas/alternating-sum-
toolkit.md`), so `D(Y)\ge b_1-b_2`. Likewise `D(Z)\in[0,v]` by Lemma
D-BOUND (`\max(Z)\le v`). Combining the two cases on the parity of `|Y|`
gives the stated bound. `∎` — this is a two-line consequence of applying
the *already-certified* D-BOUND twice; no new machinery beyond it.

*Independent verification*: checked directly against `10{,}731` exhaustive
small-`n` instances (`n=1,\dots,6`, every subset of split pieces `|S|\ge2`,
a dense `50`-point grid of `v` per instance,
`/tmp/gd_final_check.py`) and `21{,}600` further randomized instances
(`n` up to `12`, `S` random, `v` pushed to within `0.1\%` of its supremum,
`/tmp/gd_stress.py`) — zero violations of the bound in any tested case.

### Structural Lemma (identifying the two largest merged pieces)

Setting: `S\subseteq\{0,1,\dots,n\}` (`0=P_1`, `\mathrm{top}_0:=2t_1`;
`i\ge1=T_i`, `\mathrm{top}_i:=t_i$), `|S|\ge2`, every `i\in S` split into
`(\mathrm{top}_i-v,\,v)` for a common `v\in(0,q)`,
`q:=\min_{i\in S}(\mathrm{top}_i/2)$ (so every member of `S` genuinely
plays the *minority* role — exactly the previously-open sub-case). Every
`i\notin S` stays as the single untouched piece `\mathrm{top}_i`.

*Claim*: writing `\varepsilon_0:=[0\in S]`, `\varepsilon_1:=[1\in S]`, the
two globally largest elements of the merged configuration are
```
b_1 = 2t_1-\varepsilon_0 v,\qquad b_2 = t_1-\varepsilon_1 v.
```
*Proof (direct domination check in each of the 4 `(\varepsilon_0,
\varepsilon_1)` cases).* If `0\notin S`, `2t_1` is present untouched and
exceeds every other element (every untouched `\mathrm{top}_i\le t_1`,
every companion `\mathrm{top}_i-v<\mathrm{top}_i\le t_1`, and `v<t_1`,
using `q\le t_1` since `S` contains some tail index): `b_1=2t_1`. If
`0\in S`, the companion `c_0=2t_1-v` is present instead and, using
`q\le\mathrm{top}_0/2=t_1$ (so `v<t_1`), `c_0>2t_1-t_1=t_1\ge` every other
element: `b_1=2t_1-v`. Symmetrically, one level down: if `1\notin S`,
`t_1` (untouched) exceeds every remaining element (`\le t_2<t_1`, using
that `S` — since `1\notin S$ and `|S|\ge2` — contains an index `\ge2`, so
`q\le t_2<t_1`, giving `v<t_2<t_1` too): `b_2=t_1` (for `n\ge2`; at `n=1`
this sub-case, needing `0\in S,1\notin S$ with only indices `\{0,1\}`
available, is vacuous). If `1\in S`, the companion `c_1=t_1-v` is present
instead and, using `q\le\mathrm{top}_1/2=t_2` (so `v<t_2`),
`c_1=t_1-v>t_1-t_2=t_2\ge` every remaining element besides `b_1`:
`b_2=t_1-v`. `∎`

*Independent verification*: the predicted `(b_1,b_2)` formula was checked
against `14{,}400` randomized instances (`n=1,\dots,12`, random `S`, `v`
at several fractions of `q`) and matched the actual two largest sorted
elements exactly in every instance, zero mismatches
(`/tmp/gd_verify_formula.py`).

### Main Theorem

For every `n\ge1`, every `S\subseteq\{0,\dots,n\}` with `|S|\ge2`, and
every `v\in(0,q)`, the resulting configuration `B` satisfies `D(B)\ge t_n`.

*Proof.* By Lemma TWO-BLOCK and the Structural Lemma,
`D(B)\ge t_1+(\varepsilon_1-\varepsilon_0-[\,|Y|\text{ odd}\,])v`. Check
each `(\varepsilon_0,\varepsilon_1)` case (full derivation, including the
precise `n`-boundary checks, in `lemmas/two-block-residue-close.md`):
- `(0,1)`: coefficient of `v` is `\ge0`, so `D(B)\ge t_1\ge t_n` always.
- `(0,0)`: even case `\ge t_1\ge t_n` directly; odd case needs `n\ge3`
  (forced by `|S|\ge2\subseteq\{2,\dots,n\}`), where `q\le t_3/2`, giving
  `D(B)\ge t_1-v>t_1-t_3/2=7\cdot2^{n-4}\ge t_n` for every `n\ge3`.
- `(1,1)`: even case `\ge t_1\ge t_n`; odd case needs `t_1-v\ge t_n`, using
  `q=t_1/2` gives `D(B)>t_1/2=2^{n-2}\ge t_n$ for `n\ge2`; at `n=1` this
  sub-case is vacuous (`|Y|` is forced even, `=2`, since only the two
  companions can exceed `v` when `S=\{0,1\}` is the whole index set).
- `(1,0)`: needs `n\ge2` to arise at all; at `n=2`, `q=1/2$ (unnormalized
  `t_1=2,t_2=1`) gives `D(B)>t_1-2v>2-1=1=t_n` (odd case, tight but
  strict); for `n\ge3`, `q\le t_3`, giving `D(B)>t_1-2t_3=2^{n-2}\ge t_n`.

All cases give `D(B)\ge t_n`, unconditionally. `∎`

*Independent verification*: `10{,}731` exhaustive small-`n` and `21{,}600`
randomized instances (same scripts as Lemma TWO-BLOCK above) directly
checked the *actual* `D(B)`, not just the bound's individual pieces — zero
violations of `D(B)\ge t_n` in any tested case, up to `n=12`.

### Mandatory reconciliation with `recursive-embedding-induction`'s forest-extension route

Reproduced both of that file's cited numeric witnesses from scratch:
- **`n=4` symmetric two-minority tie** (`S=\{2,3\}`,
  `\varepsilon_0=\varepsilon_1=0`): predicted `b_1=16=2t_1`, `b_2=8=t_1`,
  matching the actual sorted configuration
  `[16,8,15/4,7/4,1,1/4,1/4]` (at `v=1/4`) exactly. Bound gives
  `D(B)\ge t_1=8\ge t_n=1`; true value `D=11`, consistent.
- **`n=6` external-anchor-snap residue** (`S=\{2,k\}`): for `k=1`
  (`\varepsilon_1=1`), predicted `b_1=64,\ b_2=30=t_1-v`, matching
  `[64,30,14,8,4,2,2,2,1]` exactly, bound `D(B)\ge t_1+v=34`, true `D=43`.
  For `k=4` (`\varepsilon_1=0`), predicted `b_1=64,\ b_2=32=t_1`, matching
  `[64,32,14,8,2,2,2,2,1]` exactly, bound `D(B)\ge t_1=32`, true `D=39`.

**No disagreement found.** Both routes reach `D\ge t_n` on every tested
instance; this route's mechanism (two applications of D-BOUND plus direct
identification of the two globally-largest pieces) is strictly simpler
than forest/virtual-re-split reasoning and, notably, proves the bound for
**every** interior `v` in the minority range at once — it does not need
Lemma CROSS-TIE-AFFINE's affine-cell/endpoint reduction for this
particular sub-case at all (though CROSS-TIE-AFFINE remains needed for the
"majority-part"/"≥3-part" sub-cases it already closed).

### Honest remaining scope

This closes the "all-minority, all-exactly-2-parts" cross-tie scenario —
*exactly* the previously-open residual sub-case — unconditionally, for
every `n\ge1`. **Not separately checked this round**: a tied cluster
containing a piece split into `\ge3` parts where *more than one* of that
piece's own coordinates is independently tied (at possibly different
values) to other pieces simultaneously — believed reducible to the cases
above by peeling one tied coordinate at a time (each peel is itself an
instance of Lemma TWO-BLOCK or the already-closed well-separated case),
but this composition was not carried out or verified as its own claim this
round, so it is flagged honestly rather than claimed. Certified to
`lemmas/two-block-residue-close.md`.

## Round 10 — new work: generalizing to K simultaneous independent tie-clusters

### Motivation and why the outline's planned mechanism was replaced

Round 10's outline planned a "K-fold nested TWO-BLOCK" mechanism: order the
distinct cluster tie-values `v_1>v_2>\cdots>v_K`, peel the whole merged list
at threshold `v_1` (splitting into `Y_1=\{x>v_1\}`, `Z_1=\{x\le v_1\}`), and
recurse on `Z_1` (a `(K-1)$-cluster instance) by induction on `K`. On closer
inspection this plan has a genuine subtlety the outline did not fully
resolve: peeling at `v_1` does **not** cleanly isolate cluster 1's structure
from the others, because a *majority* part of some *other* cluster
`l\ge2$ (e.g. if cluster `l` ties piece `0`, whose majority part
`2t_1-v_l` can be very large) can easily exceed `v_1` and land in `Y_1`
alongside cluster 1's own contributions — so `Y_1` is not "purely cluster
1's structure plus untouched anchors exceeding `v_1`" as the outline
assumed; it can also contain majority parts belonging to other clusters
entirely. This does not make the plan false, but it does mean step 2's
claimed clean isolation needs more careful justification than stated, and
the K-block structural lemma (step 4) would in fact have to do all of the
real work regardless.

Rather than repair the threshold-peeling argument, we found a strictly
simpler route that sidesteps thresholds and ordering altogether: **Lemma
TOP2** below is a two-line, fully general fact (no hypothesis on the list
at all) that replaces Lemma TWO-BLOCK's more elaborate `Y/Z`-threshold
machinery with a direct bound on the two globally largest elements of the
*entire* merged list. Because Lemma TOP2 needs no ordering assumption
between different clusters' tie values, the K-cluster problem reduces
immediately to identifying the two globally-largest elements of the whole
configuration (the Structural Lemma) — a task that turns out to need only
a *fixed* number of cases (five), independent of `K`, rather than an
induction on `K` at all.

### Lemma TOP2 (fully general)

*Statement.* For any finite sorted nonnegative list `L` with two largest
elements `b_1\ge b_2` (`b_2:=0` if `|L|\le1`), `D(L)\ge b_1-b_2`.

*Proof.* `D(L)=b_1-D(L\setminus\{b_1\})` (definition, `b_1` at rank 1);
`L\setminus\{b_1\}` has maximum `b_2`, so Lemma D-BOUND gives
`0\le D(L\setminus\{b_1\})\le b_2`, hence `D(L)\ge b_1-b_2`. `\blacksquare`

(Full detail, remarks, and independent verification —
`16{,}000` randomized trials, `n=1,\ldots,8` — in
`lemmas/multi-cluster-two-block.md`.)

### Structural Lemma (general K)

For `K\ge1` pairwise-disjoint clusters `S_1,\ldots,S_K\subseteq\{0,\ldots,
n\}`, `|S_l|\ge2` each, minority-role tie values `v_l\in(0,q_l)`,
`q_l:=\min_{i\in S_l}\mathrm{top}_i/2`, **with no relation assumed between
the different `v_l`'s**: writing `\varepsilon_0,\varepsilon_1\in\{0,1\}`
for whether pieces `0,1` are tied (to clusters `l(0),l(1)$ respectively),
the two globally-largest elements of the merged configuration `B` are
`b_1=2t_1-\varepsilon_0v_{l(0)}`, `b_2=t_1-\varepsilon_1v_{l(1)}`.

*Proof sketch (full detail and all four/five cases in
`lemmas/multi-cluster-two-block.md`).* Every contribution from an index
`i\ge2` (untouched, majority, or companion) is `\le t_2`; a direct check
across the `(\varepsilon_0,\varepsilon_1)` cases (with a further split of
`(1,1)` into "same cluster" vs. "different clusters," the one genuinely
new sub-case for `K\ge2`) shows `b_2>t_2` always, so all such
contributions are strictly dominated. The companion values of clusters
touching `0` or `1` are likewise shown `<b_2$ in each case, and `b_1>b_2`
is checked directly. The key new fact needed for `K\ge2` (the "different
clusters" sub-case of `(1,1)`): whichever cluster owns piece `1` but not
piece `0` must contain a *second* member of index `\ge2` (since `0` is
already used by a different cluster), forcing that cluster's tie value
below `t_2/2` — **exactly the same load-bearing fact used in the `K=1`
case's `(1,0)` analysis**, now applied independently to a cluster that
happens to be different from the one owning piece `0`. No new mechanism
is required.

### Main Theorem

For every `n\ge1`, every `K\ge1`, every disjoint cluster collection as
above, and every choice of tie values (no ordering assumed),
`D(B)\ge t_n`.

*Proof.* By Lemma TOP2, `D(B)\ge b_1-b_2`. Checking each of the five
structural cases (full algebra in `lemmas/multi-cluster-two-block.md`):
`(0,0)`: `b_1-b_2=t_1\ge t_n`. `(0,1)`: `b_1-b_2=t_1+w\ge t_1\ge t_n` (any
`w\ge0`). `(1,0)`: `b_1-b_2=t_1-v>t_1-t_2/2=3\cdot2^{n-3}\ge t_n` for
`n\ge2` (vacuous at `n=1`). `(1,1)$ same cluster: `b_1-b_2=t_1\ge t_n`
(the shared companion cancels identically, any `n\ge1`). `(1,1)` different
clusters: `b_1-b_2=t_1+w-v>t_1-t_2/2=3\cdot2^{n-3}\ge t_n` for `n\ge3`
(vacuous for `n\le2`, since this sub-case needs two disjoint size-`\ge2`
clusters each anchored by a distinct index `\ge2`). Every case (including
the two that are vacuous for small `n`) confirms `D(B)\ge t_n`.
`\blacksquare`

*Independent verification.* `16{,}000` randomized trials (`n=1,\ldots,8`,
random `K` up to `\lfloor(n+1)/2\rfloor`, random cluster sizes `2$–`4`,
random per-cluster `v_l\in(0,q_l)`): zero violations of `D(B)\ge t_n`,
zero mismatches between the predicted `(b_1,b_2)` and the true sorted
top-2 elements of `B`. See `/tmp/verify_kcluster.py` (script preserved in
this build's working notes) and `lemmas/multi-cluster-two-block.md`.

### What this closes, and the one remaining honest loose end

This fully closes the round-9-flagged multi-cluster generalization of gap
(b): any number of simultaneous, independent minority-role 2-part
tie-clusters, at any distinct (unordered) tie values, for every `n\ge1`.
Combined with the previously-certified Lemma CROSS-TIE-AFFINE
(zero-residue closure for majority-part and `\ge3`-part ties), Lemma
TREE-BOUND (anchor-only, any budget), and
`recursive-embedding-induction`'s well-separated single-free-coordinate
closure of Lemma V'-GEN, gap (b) now appears closed in full **for every
configuration where each individual split piece has at most 2 parts** —
whether one piece or many pieces are tied, at one shared value or many
independent values. The single remaining honestly-open loose end
(unchanged from round 9, not addressed this round, and *not* a
multi-cluster question) is: a single piece split into `\ge3` parts with
*more than one* of its own coordinates independently tied at different
values simultaneously ("doubly-tied `\ge3`-part piece"). This is a
structurally different scenario — one piece contributing two or more
free/tied coordinates, rather than (as in this round's K-cluster result)
each piece contributing at most one — and it is possible this scenario
cannot even arise at a genuine vertex of the full constrained polytope at
all, by the per-piece LP-vertex property that appears to underlie
`recursive-embedding-induction`'s Lemma V'/V'-GEN reduction (each piece's
own split polytope contributing at most one non-anchor coordinate at a
vertex); this connection was not verified or claimed here and is left for
the sibling approach or a future round to confirm.

### Cross-check status (per this round's dispatch instruction)

This round's task was scoped primarily as a cross-check against
`recursive-embedding-induction`'s parallel forest/multi-pair-insertion
route to the same general-K target. At the time this build ran, that
approach's file was unchanged since the round-9 commit (no completed
general theorem was available in the repository to check against). This
result should therefore be reconciled against the sibling's mechanism —
once available — on the concrete multi-cluster witnesses already used in
round 9 (e.g. `n=4,6` two-cluster configurations), per standing protocol;
this reconciliation is flagged for the reviewer or next round rather than
completed here, since no sibling result existed yet to compare against.

## Promotable lemmas (round 10 additions)
- **Lemma TOP2** (`lemmas/multi-cluster-two-block.md`) — fully general,
  hypothesis-free: `D(L)\ge b_1-b_2` for any sorted nonnegative list's two
  largest elements. Strictly simpler than and supersedes the
  threshold/parity machinery of Lemma TWO-BLOCK for this problem's
  purposes; reusable by any approach needing a two-largest-element bound
  on `D`.
- **Structural Lemma (general K)** and **Main Theorem** (multi-cluster
  closure of gap (b)) — fully proved above, certified to
  `lemmas/multi-cluster-two-block.md`; closes the round-9-flagged
  multi-cluster generalization in full for the "every split piece has at
  most 2 parts" scope.
