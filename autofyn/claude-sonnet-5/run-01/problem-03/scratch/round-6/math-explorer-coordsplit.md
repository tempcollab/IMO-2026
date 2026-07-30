# math-explorer report — lens: general-n upper bound, arbitrary configs, "coordinated split" gap (round 6)

Target: `universal-adversary-strategy`'s open gap — the general upper bound
over arbitrary (non-geometric) Liu Bang configurations, specifically the
regime where neither Lemma DOM (`p1≥S`) nor Lemma HALVE (`p1≥2p2`) fires,
which the round-5 file claims requires "a coordinated simultaneous split of
two pieces at jointly-optimized non-half ratios" — evidenced by the exact
witness `A=(4649/10000,3042/10000,2309/10000)`, `n=2`.

**Headline finding: that "coordination is required" diagnosis is not
tight.** A single-piece split, at a non-half ratio chosen so the new piece
exactly *ties* an existing tail element, already achieves the claimed
optimal value on the recorded witness — using only 1 of the 2 available
marks, not 2. The real missing tool is not "simultaneous two-piece moves"
but "single-piece splits at an arbitrary (tie-inducing) ratio, not just
halves" — Lemma SPLIT / TAIL-SNIP as certified only cover equal-half splits
of one position; that's the actual gap.

## 1. The recorded witness needs only 1 mark, not 2

`A=(p1,p2,p3)=(4649/10000,3042/10000,2309/10000)`, `n=2`. Exact search
(`Fraction`, denominator 10000) over all single splits of `p1` alone:

```
split p1 -> (x, p1-x), x = 1607/10000, p1-x = 3042/10000 = p2 exactly
resulting pieces sorted: p2, p2(orig), p3, x   [4 pieces]
oddrank = p2 + p3 = 5351/10000 = 0.5351   (exact)
```

This *exactly* matches the value the round-5 file found via a 2-mark grid
search over splitting both `p1` and `p2` simultaneously (`≈0.5351`), and
both are `< c(2)=4/7≈0.5714`. So a single 1-mark move — split `p1` so its
larger part ties `p2` — already solves the recorded counterexample, with
one mark to spare. The key move is: **choose the split ratio so the larger
piece equals an existing element**, not "split in half." This generalizes
Lemma DOM-boundary-slack's flavor (splitting to force an exact match) to a
single non-half cut.

Recommend flagging this correction in `universal-adversary-strategy.md`
before the next round builds on the "2 marks required" framing — it's not
false that a 2-piece move *also* attains the value (the file's finding is
correct as far as it goes), but the claim that single-piece moves are
*insufficient* is refuted by this cheaper witness.

## 2. Structural reason ties happen: this is Lemma D, directly

Within any fixed ordering (a "cell" of the split-ratio parameter space),
`oddrank` of the final multiset is an **affine function** of the free split
parameters (it's just a fixed subset-sum of the pieces, and the pieces are
affine in the cut positions). `interior-point-linear-obstruction.md`'s
Lemma D says an affine functional maximized (here, minimized — same
argument with sign flipped) over a polytope at a *relative-interior* point
forces it constant on that polytope. Contrapositive: **if the functional
is non-constant on a cell, the minimum over that cell is attained on its
boundary** — i.e. at a point where either (a) some split piece has length
exactly `0` (a wasted mark / degenerates to fewer marks), or (b) two
adjacent-rank pieces become exactly tied (the cell boundary where the sort
order changes).

This is confirmed in every numeric example run this round (see §3): the
argmin always has an exact tie between two resulting pieces, or a
degenerate (zero-length) split. **Recommend certifying this as a new
lemma — call it Lemma TIE-NECESSARY** — since it follows from the
already-certified Lemma D almost immediately (apply Lemma D to the cell
containing the claimed optimum; if non-constant, push to the boundary;
finitely many cells since the ordering is a finite poset, so a global min
exists and lies on some cell's boundary). This converts the *continuous*
optimization over split ratios into a **discrete/combinatorial** problem —
"which ties to make, which pieces get 0" — which is the kind of object the
existing alternating-sum / parity toolkit (Lemma L, PARITY-PAIR, D-BOUND)
is built to handle by induction. This looks like a genuinely cheap,
high-leverage lemma to prove next: it doesn't solve the gap by itself but
turns an intractable continuous search into a finite one.

## 3. Numeric terrain for m=4,5 (tests beyond the recorded witness)

Random configs, budget `k=2` marks, brute + local search over (i) splitting
one piece into 3 parts, (ii) splitting two different pieces once each:

- `A=(0.4859,0.3439,0.0884,0.0496,0.0322)`, `m=5`: optimal (found
  `≈0.5181`, confirmed exactly) is **all 2 marks spent on `p1` alone**,
  split into 3 parts `(p2, p3, r)` with `r=p1-p2-p3` — i.e. `p1`'s split
  ties `p2` **and** `p3` simultaneously (a length-2 prefix match). This is
  literally a truncated version of the *already-certified* Lemma DOM:
  Lemma DOM requires `p1≥S` (dominate the **whole** tail, sum `S`); here
  `p1<S` but `p1≥p2+p3` (dominates a **prefix** of the tail) and the
  budget (`k=2`) matches the prefix length. Call this **Lemma
  PARTIAL-DOM**: with tail sorted `p2≥…≥pm`, prefix sums
  `S_j=p2+…+p_{j+1}`, if `p1≥S_j` for the largest `j≤k` with `p1≥S_j`, then
  splitting `p1` into `(p2,…,p_{j+1}, r=p1-S_j)` costs exactly `j` marks and
  gives an oddrank value verified (by the same duplicate-pair mechanism
  used in Lemma DOM's existing certified proof) to reproduce the found
  numeric optimum exactly. Lemma DOM is the `j=m-1` (full tail) special
  case; this is a strict generalization reusing the identical proof
  technique.
- `A=(0.3374,0.2589,0.242,0.1617)`, `m=4` (**even** `m` — piece count
  matters, see below): partial-DOM with `j=1` gives **zero improvement**
  over doing nothing (`oddrank` unchanged, `=p1+p3` both before and after)
  — because inserting one small remainder at the tail-end of an
  *even*-length list lands it on an odd rank, exactly cancelling the gain.
  The true optimum here (`≈0.5009`, confirmed) instead **splits `p1` and
  `p2` independently**, each tied to a *different*, non-adjacent tail
  target: `p1`'s large part ties `p3` (not `p2`!), and `p2`'s large part
  ties `p4`. So the correct "coordination" here isn't a jointly-optimized
  simultaneous move on two pieces glued together — it's **two independent
  single-piece tie-splits**, each solvable by the same one-piece rule,
  just applied to a *non-adjacent* target chosen from the tail rather than
  the next-largest element. This suggests the real object to characterize
  is a **matching**: choose an injective partial map from {pieces to
  split} to {tail elements to tie with}, each edge costing 1 mark (or a
  chain of edges costing more, as in partial-DOM), such that the total
  tie-value is minimized — evocative of an assignment problem, not a
  single joint Lagrange condition.
- Parity (`m` even/odd) visibly gates whether a given tie/insertion helps
  or is neutral — this is exactly the phenomenon
  `recursive-embedding-induction`'s **Lemma PARITY-PAIR** (round 5, proved
  for the lower-bound side) was built to handle via a two-way case split on
  parity of a block's multiplicity. Worth checking directly whether
  PARITY-PAIR's combinatorial core (or its proof technique) transfers to
  this upper-bound tie-matching problem — the two approaches may be
  fighting the same combinatorial object from opposite sides
  (lower-bound "which anchor wins ties" vs. upper-bound "which piece to
  tie with which target"), which would let the upper-bound gap reuse a
  proof already fully certified in the other approach, rather than
  re-deriving it from scratch.

## 4. What single-piece moves alone cannot yet explain

No genuine case was found this round where a **simultaneous, non-tied**
joint optimum (i.e., two pieces split at ratios where *neither* resulting
piece is a boundary tie, found via a true 2D interior KKT/Lagrange
stationary point rather than a cell-boundary tie) was optimal — consistent
with §2's Lemma D argument ruling that out categorically. So: no evidence
was found for a genuinely new "joint Lagrange condition" mechanism: every
tested optimum decomposes into ties (single-piece, chained-prefix, or
independent-pair), never an interior smooth optimum. This is a positive
simplification for the next attempt — the search space is ties/degeneracies
only, not general continuous joint optimization.

## 5. Recommendation for proof-outliner

1. **Correct the record**: the `universal-adversary-strategy` witness is
   closed by a 1-mark single-non-half-split tie, not a genuine 2-piece
   coordination — update the framing before further building on "2-piece
   moves are necessary."
2. **Prioritize Lemma TIE-NECESSARY** (§2): cheap, follows almost
   immediately from the already-certified Lemma D, and converts the
   continuous optimization into a finite combinatorial one for *every*
   configuration, not just special cases. This is likely the single
   highest-leverage next lemma for this approach.
3. **Prioritize Lemma PARTIAL-DOM** (§3, first bullet): a direct, mechanical
   generalization of the already-certified, already-proven Lemma DOM
   (same duplicate-pair insertion argument, just truncated to a tail
   prefix) — should be a fast, low-risk proof for a proof-builder to close,
   and it already reproduces one nontrivial numeric optimum exactly.
4. **Open, not yet closed**: the `m`-even "independent non-adjacent
   tie-pair" phenomenon (§3, second bullet) — recommend framing this as a
   matching/assignment problem over (piece, tail-target) pairs rather than
   chasing a single closed-form ratio; and explicitly check whether
   `lemmas/parity-pair-lemma-L.md`'s PARITY-PAIR machinery
   (`recursive-embedding-induction`, proved for the lower bound) transfers
   — a cross-approach reuse here could shortcut re-deriving the parity
   case split from scratch.
5. Do **not** frame the next attempt as "find the exact closed-form ratio
   for a jointly-optimized 2-piece split" — that framing is now shown to be
   both unnecessary (the 1-mark tie solves the recorded witness) and
   incomplete (the `m=4` case needs two *independent* non-adjacent ties,
   not one joint move). The productive framing is: (i) certify
   TIE-NECESSARY to restrict to finitely many tie-configurations, (ii)
   certify PARTIAL-DOM as the single-piece-prefix building block, (iii)
   treat the general response as a recursive/greedy choice over which
   (piece, target) ties to spend the budget on, closing the loop with
   parity bookkeeping already built elsewhere in the population.
