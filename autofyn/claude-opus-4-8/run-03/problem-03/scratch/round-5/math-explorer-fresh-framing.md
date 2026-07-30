## imo-2026-03

### Context: what the field already covers (so I don't repeat it)
All four live/registered approaches (parity-measure-potential, induction-peel, two-box-balancing,
smoothing-majorization) work on the SAME reduced target: after Lemma R (claiming ⇒ Liu gets the
odd-rank sum) and Lemma M (`D = μ{t : N(t) odd}`, purely a function of the **multiset of final
lengths**, position-free), the whole problem is: Liu picks a multiset `A` (≤ n+1 numbers, Σ=1),
Xiang refines it with ≤ n splits to minimize `D = Σ(-1)^{rank+1}b_i` over the sorted result. All
four approaches then attack this by (a) a global measure/parity potential, (b) strong induction +
peeling the unique max, (c) an odd/even "box" reformulation, (d) continuous exchange/smoothing
toward the dyadic maximizer. They all bottom out on the SAME two walls: GAP U (Liu balanced,
`a_1 < L/2`, needs a real adaptive-cut argument, not ad hoc subset-match) and GAP L (Xiang's first
top-cut is imperfect, `p_1≠p_2`, needs the imperfect-bisection coupling).

### Distinct openings evaluated (per the assigned candidates)

1. **LP-corner / breakpoint finiteness theorem (piecewise-linearity of D in each cut coordinate).**
   **This is the one I recommend registering.** For a *single* cut of a piece of length `ℓ` into
   `(s, ℓ−s)` with everything else fixed, `D` (as a function of `s∈[0,ℓ]`) is **piecewise linear
   with slope in {−2, 0, +2}** — verified numerically (background `{0.35,0.15,0.10}`, `ℓ=0.4`: slopes
   take exactly the values `{-2,0,2}`, min attained at a breakpoint `s→0`, i.e. a degenerate/no-cut
   corner). *Why:* within a fixed rank-order region, `s` sits at some odd/even rank `i` and `ℓ−s` at
   rank `j`; `dD/ds = (-1)^{i+1} − (-1)^{j+1} ∈ {−2,0,2}` since only `s,ℓ−s` move (correlated,
   `d(ℓ−s)/ds=−1`) and everything else is locally constant. Hence a linear objective on an interval
   ⇒ **the minimum of D over that single cut is attained at a boundary of some linear piece — i.e.
   at a *tie* (`s` or `ℓ−s` equals another current piece's length, a rank-order breakpoint) or a
   *degenerate* endpoint (`s=0` or `s=ℓ`, i.e., the cut is not used / is trivial).** Iterating over
   Xiang's ≤n cuts (played in any order, since the final multiset is what matters — order of
   application doesn't change the final piece set), this gives a **general finiteness theorem**:
   *Xiang has an optimal strategy in which every cut either exactly matches an already-existing
   length (⇒ a Lemma-P cancelling pair) or exactly bisects (creates a self-tie between the two new
   fragments), never an "interior" generic split.* This is qualitatively different from any current
   approach: it is not a potential/measure argument (framing A/B), not an induction peel (framing
   A), not a box reformulation (framing D), and not a continuous exchange toward one target profile
   (framing E, smoothing-majorization) — it is a **combinatorial finiteness/LP-vertex reduction**
   that would justify, once and for all, why Xiang's known good moves are *always* either
   "replicate-to-cancel" or "bisect" and **rule out any other kind of optimal cut**, turning the
   open-ended real search in GAP U (what fraction/subset to match) into a genuinely finite
   combinatorial search over tie-patterns of a bounded multiset. **Key lemma needed:** formalize the
   single-cut breakpoint fact above, then a compactness/exchange argument that WLOG *all* of
   Xiang's cuts can be pushed to breakpoints simultaneously (the subtlety: moving one cut to its
   breakpoint can shift the rank structure seen by the others — needs an inductive/lexicographic
   "settle cuts one at a time, outermost first" argument, verified not to unsettle earlier ties).
   This plausibly reaches `u_n` for BOTH walls: GAP U's subset-match becomes "which subset of ties
   to realize" (a finite optimization over a poset of tie-patterns bounded by budget `n`), and GAP
   L's imperfect-top-cut case is *itself ruled out*: the theorem says Xiang's optimal first move on
   the top piece is not a generic `p_1≠p_2` split at all — either it's a tie against an existing
   piece (`p_2` matches one of `2^{n-1},…,1`, i.e. `p_2=2^{n-1}` — already covered by "SL Case A"
   fragments!) or a self-bisection (`p_1=p_2=2^{n-1}`, already the closed "SL perfect bisection"
   fragment!). **If this finiteness theorem holds, GAP L (imperfect `p_1≠p_2`) may not need a
   separate coupling argument at all — it could be proved *vacuous*: an optimal Xiang never plays an
   imperfect top cut in the first place.** That would be a genuine shortcut past the current wall,
   not just a bypass that hits the same wall one step later.

2. **Direct LP-duality certificate (single global weighting).** Considered, but the game is not a
   one-shot LP: Xiang's response is adaptive across a tree of ≤n sequential cuts and the objective
   is the alternating sum of a *re-sorted* list (rank membership changes with every cut — the
   "CRITICAL" warning already flagged in two-box-balancing.md). A naive single dual weighting
   (find `λ` with `D ≥ λ·(Liu profile) ` type bound) collapses to the same measure/parity potential
   already in play (framing B). Not a genuinely new lever — subsumed by opening 1, which gives the
   *rigorous justification* for why only finitely many response-shapes need a certificate at all.

3. **Generating-function / dyadic-binary encoding.** The recursion `u_n = u_{n-1}/(2+u_{n-1})`,
   equivalently `1/u_n = 2(1/u_{n-1})+1` (Mersenne-number recursion, same shape as Tower-of-Hanoi
   move counts / `2^{n+1}-1` = weight of a depth-`(n+1)` complete binary tree) suggests a
   Huffman/Kraft-inequality framing (assign each final piece a "codeword length" via its dyadic
   scale). Investigated: this recursion is **already** the content of the induction-peel /
   two-box-balancing recursion (`L(n)` in terms of `L(n-1)`); it does not open a route past GAP
   L/GAP U, it just re-derives the target value. Not recommended as a fresh top-level attack —
   it's the same recursive skeleton already in the field, dressed in coding-theory language.

4. **Scheduling/Hackenbush-style game with an invariant.** No natural Hackenbush/Nim-value
   structure here: the game is not impartial, has no "last player to move loses/wins" flavor, and
   the payoff is continuous (a real number, `D`), not a win/loss outcome. Sprague–Grundy theory does
   not apply. Rejected.

5. **Discrepancy / two-coloring / necklace-splitting (Hobby–Rice, Borsuk–Ulam).** Tempting because
   `D=|O|−|E|` looks like a signed-discrepancy statistic, and Hobby–Rice-type theorems guarantee an
   alternating-sign partition into `k+1` intervals via `k` cuts making several integrals vanish
   simultaneously. **Checked and rejected as inapplicable**: Hobby–Rice balances integrals over
   *positionally* alternating intervals (left-to-right order on the stick); our `D` (via the
   certified Lemma M) depends **only on the multiset of final lengths**, not position at all — the
   problem has already been fully de-positionalized. A topological existence theorem for a
   positional alternating partition doesn't address a rank-by-size alternating sum. This is a
   genuine (if negative) finding: **topological/measure-theoretic necklace-splitting tools are the
   wrong tool for this problem** once Lemma M is in hand — save the outliner from chasing this.

### Cheap numerical probe (rules out one naive "universal formula" idea, informative negative result)
Tested a simple non-adaptive candidate — "Xiang cuts every piece above the smallest piece's length
at that common threshold `t=min(A)`" (a single global rule, no casework) — against known
counterexample profiles from parity-measure-potential's GAP-U refutation. It fixes those specific
counterexamples (`D=0.12 ≤ u_2=0.143` on `(0.44,.281,.279)` and `(0.5,.28,.22)`) but **FAILS badly**
on near-equal-piece profiles (e.g. three pieces `≈1/3` each for `n=2`: best achievable `D≈0.33 ≫
u_2=0.143`, since no piece exceeds the threshold so Xiang can't cut at all). Even optimizing the
single threshold `t` over all breakpoints still fails on near-uniform profiles (`n=2..4`: worst case
`D≈0.32-0.33`, tested `20000` random balanced trials each `n`). **Conclusion: no single non-adaptive
global rule (threshold-cut, or any one fixed formula) can close GAP U uniformly — the near-equal
multiset case genuinely needs the pairing/duplication mechanism (Lemma U0/P), while the
skewed-balanced case needs the threshold-type mechanism; a valid strategy must be casework on the
"how-equal-are-the-pieces" structure, which is exactly what opening 1's finiteness theorem would
formalize (case = tie-pattern) rather than papering over.**

### Candidate technique(s)
- Primary recommendation: **piecewise-linear-objective / LP-vertex (corner-point) reduction** —
  a discrete-optimization technique (not in knowledge_base.md verbatim, but squarely a "Standard
  extremal principle" / "constructive vs. existence" style argument per the Meta-Strategy section:
  reduce a continuum of Xiang strategies to a finite family by convexity/piecewise-linearity, à la
  Pólya "generalize/reformulate"). Closest KB entries: **Piecewise-concavity smoothing** (Algebra
  section) is the mirror technique (concave ⇒ min at breakpoint; here it's the *opposite* sign,
  piecewise-linear ⇒ min at a breakpoint too — same "argmin of PL/PC function is a vertex" logic,
  can cite by analogy). **Extremal principle / pigeonhole** (Combinatorics section) for the
  "settle-cuts-one-at-a-time" induction needed to combine single-cut breakpoints into a joint one.

### Knowledge-base entries to use
- "Piecewise-concavity smoothing" (Algebra & Polynomials) — analogous vertex-of-piecewise-function
  argument, adapt the proof pattern (partition domain by breakpoints, min/max at an endpoint).
- "Invariants & monovariants" and "Extremal principle" (Combinatorics) — for the induction needed
  to lock in one cut's breakpoint without unsettling others.
- Already-imported (shared, don't re-derive): Lemma R (reduction-odd-rank), Lemma M/I
  (measure-identity), Lemma P (cancelling-pair) — this finiteness theorem's conclusion IS "every
  optimal cut is a Lemma-P tie or a bisection," so it directly upgrades Lemma P from "a legal move"
  to "WLOG the only kind of move."

### Analogous past problems (cruxes)
- `aimo-0117` (already in use by two others: dyadic geometric sequence / single largest term
  exceeds the rest) — genuinely analogous to the Case-A top-scale argument, not to this new
  finiteness idea specifically.
- `aimo-0560` (surrogate-opponent domination, already claimed by smoothing-majorization) — not
  analogous to the LP-corner idea; flagging so the outliner doesn't double-assign it.
- Searched `combinatorics` × `games-and-strategy` (39 cruxes) and `combinatorics` ×
  `extremal-principle`/`linear-algebra-method` for a genuine "piecewise-linear objective ⇒ vertex"
  crux; **none of the 39 games-and-strategy cruxes match this LP-corner mechanism** — the closest
  in spirit is `aimo-0663`'s "shadow game coupled by a position map, one-direction domination,"
  which is a *different* device (already earmarked for GAP L's shadow-coupling in
  two-box-balancing) — do not conflate the two. **Verdict: no strong crux match for opening 1; it
  is a self-contained elementary convexity argument, not something to borrow from the corpus.**

### Prior progress
Shared answer confirmed: `c(n) = 2^n/(2^{n+1}-1)`, minimax `D = u_n = 1/(2^{n+1}-1)`. Upper bound
closed for `a_1 ≥ L/2` (all approaches). Lower bound closed for Case A (top scale uncut) and for
perfect bisection in Case B. Two shared open gaps: GAP U (`a_1 < L/2`) and GAP L (imperfect top
cut `p_1≠p_2`). See current.md for full certified-lemma list; nothing in this report contradicts
it — this is purely a reconnaissance of a fifth, unregistered framing.

### Dead ends (do not retry)
- Single global non-adaptive threshold-cut rule (this report, §"cheap numerical probe"): refuted
  by near-equal-piece profiles for `n≥2`. Do not propose "one formula for Xiang, no casework" for
  GAP U without first pairing/deduplicating near-equal pieces.
- Necklace-splitting / Hobby–Rice / Borsuk–Ulam discrepancy theorems: inapplicable, since Lemma M
  already shows `D` is position-free (depends only on the length multiset) — a positional-balancing
  theorem answers the wrong question. Do not chase this.
- Hackenbush / Sprague–Grundy: game is not impartial/win-loss, payoff is a continuous real value —
  no Grundy-value structure exists here.
- Generating-function/Huffman-coding dressing of the recursion `u_n=u_{n-1}/(2+u_{n-1})`: same
  content as the already-registered induction-peel recursion, not a new lever.

### Small-case / intuition notes (conjectural, numeric)
- The single-cut piecewise-linearity fact (`slopes ∈ {-2,0,2}`, min at a breakpoint) was verified
  numerically on one example (`background={0.35,0.15,0.10}`, cut `ℓ=0.4` piece); this is a
  *local* algebraic fact that should be provable exactly (it follows directly from the definition
  of `D` as an alternating rank-sum plus `d(ℓ−s)/ds=-1`), not merely conjectural — but the
  **multi-cut joint statement** (WLOG *all* n cuts simultaneously at breakpoints) is genuinely open
  and is the crux of registering this as a new approach.
- Conjecture (numeric, `n=2,3,4`, tested via brute-force best-single-threshold search): Xiang's
  optimal strategy on any Liu profile decomposes into "first pair off near-equal pieces (ties),
  then bisect what's left" — consistent with (and would formally explain) why Lemma U0
  (replicate-to-cancel) and the bisection chain (§4 of two-box-balancing) are exactly the two
  building blocks every current approach already uses ad hoc; opening 1 would make this provably
  exhaustive rather than a guess.
