## imo-2026-03 — lens: scout the Case-C existence question directly (Hall/matching)

### Distinct openings
1. **Crux-corpus opening (subset-sum interval-covering, NOT Hall/SDR).** `aimo-0292`
   ("n blocks weight >=1, total 2n; every r in [0,2n-2] hit by some subset sum
   within +2") is genuinely analogous in *flavor*: it proves a subset-sum
   *existence* claim by (a) sorting, removing the *largest* element, (b)
   splitting the achievable-sum range of the rest into "excludes it" /
   "includes it" (shifted by that element's value), and (c) showing the two
   shifted intervals overlap using only "later elements are big enough,
   remaining total is small enough" — a clean induction-on-size argument, no
   Hall's theorem, no bipartite graph. This is a genuinely different
   existence-proof shape from Hall/SDR and is worth trying to adapt: reframe
   Case C's need ("does a good donor+subset-match choice exist within budget
   m-1?") as an *interval/slack* covering statement rather than an *exact*
   subset-sum-equals-existing-value statement.
2. **Hall-deficient-set-deletion opening (`aimo-0063`), checked and NOT a good fit
   as-is.** Re-verified the actual mechanism (people vs. one fixed person's `n`
   arcs, iterated Hall-deficient-set deletion + induction on unmatched people).
   This is a genuine 1-1 bipartite SDR between two *equal-size* sides with a
   universal vertex forcing nonemptiness — structurally a different shape than
   our problem: we need one donor's split to match a *chosen subset* of
   already-existing element *values* (no bipartite equal-size structure, no
   natural "universal vertex"), confirming round 10's diagnosis ("closer to
   subset-sum/exact-cover, Hall doesn't directly apply") rather than refuting
   it. Not recommended as the direct model; the *style* of "iteratively peel a
   violating chunk, recurse" is reusable in spirit but not the specific
   construction.
3. **Computational opening: test fixed adaptive-but-mechanical matching rules,
   find where each breaks, and locate the true missing ingredient.** Did this
   directly (see below) — found that the missing ingredient is not a better
   *template* but *budget-awareness*: whether to spend a mark on an element at
   all depends on local structure (e.g. already-tied elements should be
   skipped for free, not halved), matching and sharpening the round 12/13/
   round-5 (`potential-averaging-bound`) diagnosis with a fresh, small,
   concrete witness.

### Candidate technique(s)
- Adapt `aimo-0292`'s interval-covering induction: instead of demanding an
  *exact* subset-sum match (as SUBSET-DOM currently requires: `Σ(T)` exactly
  hits existing values), prove a weaker but sufficient *slack* statement —
  "some subset of the current elements has sum within `[p_i - budget_slack,
  p_i]`" — and bound the residual's damage to `oddrank` by that slack, rather
  than needing residual `r=0` or an exact coincidence.
- A genuinely different possible framing suggested by the new witness below:
  formalize a **budget-aware recursive minimax** (not a fixed template): at
  each step, choose among {skip an already-(near-)tied top pair for free,
  Lemma DOM, halve, arbitrary-subset PAIR-VALUE match} by which locally
  *frees up* marks for the recursive tail, not by a fixed priority order. This
  is the same direction round 13's `solve2(A,marks)` was building, but that
  recursion (per round 13's own honest report) still lacks the general
  non-contiguous subset-match move as an option — my witness below shows
  *why* that move (or rather, the "skip if already tied" option) is load-
  bearing even at `m=4`.

### Cheap-kill candidates
- **"Already-exactly-tied top elements should never be split"** is a cheap,
  checkable structural fact any construction should respect (see witness
  below where violating it costs the whole bound). Any future template that
  unconditionally halves/splits every non-minimal element should first check
  for free ties among the current top elements and skip them.
- No new parity/pigeonhole/injection kill found beyond what's already
  certified (PAIR-VALUE's tie-adjacency argument, Steps 0–2 of BLOCK-RECURSE).

### Knowledge-base entries to use
- Hall's marriage theorem (already cited in `pair-value.md`'s own text as the
  natural-but-unproven-existence tool; my check confirms it does not directly
  transfer from the classical 1-1 SDR shape).
- No other new KB entry surfaced as more apt than what's already cited
  (PAIR-VALUE, BLOCK-RECURSE, DOM, HALVE, DOUBLE-INSERT already cover the
  certified menu).

### Analogous past problems (cruxes)
- `aimo-0292` — best match found. Crux: "split the achievable subset-sum
  range into sums excluding a chosen (largest) element and the same sums
  shifted up by its value; covering the whole target interval reduces to the
  two shifted copies overlapping." Directly suggests an *interval-covering*,
  not exact-match, framing for Case C's donor/subset existence question —
  worth adapting even though the target statement differs (there: hit every
  `r` within a window of 2; here: bound `oddrank` by `c(m-1)Σ`).
- `aimo-0063` — checked in detail (see opening 2 above); NOT a good structural
  match (different quantifier/matching shape: 1-1 SDR with a universal
  vertex, not subset-selection against a single fixed donor). Recorded so no
  future round re-tries importing it wholesale.
- No third crux found that beats these two after filtering
  `combinatorics`/`graph-theory-and-connectivity`,
  `induction-and-construction`, `extremal-principle`,
  `bijections-and-encoding` subtopics for "matching"/"subset-sum"/"greedy
  exchange"/"potential function existence" keywords (full list of hits
  scanned; nothing else besides `aimo-0129`/`aimo-0197`/`aimo-0341` genuinely
  resembled our shape, and those are Hall-on-bipartite-grids problems, same
  mismatch as `aimo-0063`).

### Prior progress
Current best is exactly as `current.md` states: Lemma PAIR-VALUE (hypothesis-
free value identity for arbitrary tied-pair decompositions, no contiguity
needed) is certified and correct; its SUBSET-DOM corollary supplies the
*move* (arbitrary donor + arbitrary-subset match), but no proof that a good
choice of donor/subset always exists within the `m-1` mark budget for every
Case-C configuration, `m≥4`.

### Dead ends (do not retry)
- Fixed-shape templates ("exactly 2 top-level tied pairs") — refuted `m=4..100`
  (round 11), reconfirmed structurally implausible as a *fixed* pattern.
- Greedy largest-first single-donor subset-sum matching — reproduced
  independently this round: **exact same failure mode confirmed**, e.g.
  `A=(996,944,662,225,74,50)`, `m=6`: `oddrank=1940` vs target
  `94432/63≈1498.9`, a large violation (script: donor=current max, greedy
  smallest-first accumulate). Matches round-10's "74% violation" finding in
  spirit.
- **NEW this round, also refuted:** "top-two merge cascade" (repeatedly split
  the current two largest `x≥y` into `(y,x-y)`, recurse) — fails on
  `A=(1964,1909,1817,32)`, `m=4`: gives `oddrank=3726` vs target
  `45776/15≈3051.7`; ALSO fails on the general random sweep (worst margin
  `-10114/15` on `A=(1964,1909,1817,32)` itself). This is a genuinely new
  negative result, distinct from the round-10 greedy dead end (this rule
  always touches the top two, never skips a free tie).
- **NEW this round, also refuted:** "bottom-up smallest-pair snip" (repeatedly
  tie the two globally smallest elements) — fails on the round-10 near-
  uniform-tail family for every tested `m` (`4,5,6,8,10,20`), margins all
  negative (e.g. `m=20`: margin `≈-2.4×10⁻¹`), because it never touches the
  dominant `p_1` at all.
- **NEW this round, also refuted (even after taking the min of 4 templates
  simultaneously):** taking `min(ALL-BUT-MIN, MATCH-TAIL-PAIR, top-cascade,
  greedy-bestfit-subset-match)` still fails on a fresh, small, clean witness
  `A=(965,965,958,482)` (`m=4`, budget `3`, `Σ=3370`, target
  `c(3)Σ=5392/3≈1797.3`): best of all four templates gives `1923`–`1926`,
  still `>` target.

### Small-case / intuition notes (all labeled conjecture/diagnosis, not proof)
**The `A=(965,965,958,482)` witness is the most useful finding of this round.**
By hand (verified with exact `Fraction` arithmetic): the two largest elements
are *exactly* tied (`965=965`) already, at zero cost. Every fixed template
above either (a) halves them anyway (wasting 2 of the 3 marks on elements
that were already contributing optimally for free), or (b) ignores them and
mishandles the tail. The TRUE winning construction: **leave the already-tied
top pair completely untouched (0 marks spent)**, and spend the *entire*
freed-up 3-mark budget refining only the tail `{958,482}` — ordinary halving
of both (2 marks, well under the 3 available) gives
`oddrank({965,965,479,479,241,241}) = 965+479+241 = 1685 = Σ/2` exactly,
comfortably beating the target `1797.3`.

**Conjectured diagnosis (matches and sharpens round 12/13's and round 5's
`potential-averaging-bound` finding, now with a concrete small witness):** the
missing ingredient is not a better fixed template but **budget-awareness** —
whether to spend a mark on a given element must depend on local structure
(is it already tied with something? does spending the mark here help the
*recursive* residual more than spending it elsewhere?), which is exactly a
minimax/DP-style recursive decision, not a priority-ordered menu of
independent moves. This is consistent with (not a refutation of) the
already-flagged fact that a genuinely correct, budget-capped recursive
`solve` (à la round 13's `solve2`) is the right proof *shape* — but round 13
found even that shape's certified move-menu (contiguous-prefix-match only)
insufficient without the general PAIR-VALUE arbitrary-subset move. My witness
here shows a second, cheaper-to-formalize necessary ingredient that isn't
about subset choice at all: **a "skip-if-already-tied" zero-cost option must
be checked and preferred before any halving/splitting is applied to that
element**, at every level of recursion. This is a small, concrete,
checkable addition to whatever recursive definition next round's outliner
builds, and it is *not yet reflected* in ALL-BUT-MIN, MATCH-TAIL-PAIR, or any
of the templates tested this round or in prior rounds (all of them
unconditionally split every element down to the minimum/second-minimum,
regardless of pre-existing ties).
