## Status
unsolved

## Approaches tried
- (round 1) Original "Lemma C" (bare claim: `V(p) := min_B oddrank(B)` is concave
  in the sorted Liu-Bang vector `p`, because it is "a min of linear functions of
  `p`") — **RETHINK/dead end**. Falsified by the round-1 outline-reviewer at
  `n=2` (3 pieces): `p1=(0.7,0.2,0.1)`, `p2=(0.34,0.33,0.33)`,
  `mid=(0.52,0.265,0.215)`, with `V(p1)=0.55`, `V(p2)=0.50`,
  `V(mid)=0.52 < (0.55+0.50)/2 = 0.525`. Never built past the initial skeleton.
- (round 3) proof-outliner proposed a **revision**: Lemma C' — first solve the
  inner continuous-split-ratio optimization for each fixed discrete
  combinatorial "split type" `T`, THEN check whether the resulting `f_T(p)` is
  genuinely affine in `p` (refining `T` further if it is only piecewise-affine
  internally), with a **mandatory Step 0 reconciliation gate**: reproduce the
  round-1 falsification with the TRUE, exactly-computed `V` before treating
  anything else as progress. Outline-reviewer APPROVED this into the round-3
  build set, but the round was cut short and this file was never updated.
- (round 4, this round) **Executed Step 0 in full.** Result: **the
  falsification REPRODUCES exactly**, with the true `V` computed two
  independent ways (exhaustive combinatorial + global-optimizer search, and a
  full closed-form case analysis by hand — see below). Per the mandatory gate
  in the round-3 outline ("If it reproduces, STOP — this is still a dead end,
  report RETHINK with the reconciled numbers, and do not proceed further"),
  this approach is **RETHINK / dead** as a route to global concavity of `V`.
  Beyond just reproducing the number, this round also identifies and proves
  the *structural reason* concavity fails, which shows the Lemma C' repair
  strategy cannot work even in principle (not merely "not yet proved") — see
  "Current best" below. This is new information beyond round 1's bare numeric
  counterexample.

## Current best

### Step 0 — reconciliation gate, executed

**Setup.** `n=2` (Liu Bang uses 2 marks ⇒ 3 pieces), sorted descending
`p=(p_1,p_2,p_3)`, `p_1+p_2+p_3=1`. Xiang Yu has a budget of `≤2` marks to
distribute among the 3 pieces (any composition `(k_1,k_2,k_3)`,
`k_1+k_2+k_3≤2`, each piece split into `k_i+1` parts by `k_i` further cuts, cut
positions and the induced continuous split ratios free), producing multiset
`B`; `V(p) := min_B oddrank(B)` using the certified `oddrank` formula (Lemma 1,
`lemmas/claiming-phase-value.md`).

**Reproduction.** I computed `V` at the three round-1 points using (a) an
exhaustive enumeration of all `7` compositions `(k_1,k_2,k_3)` with
`k_1+k_2+k_3≤2`, each inner continuous optimization solved by a global
optimizer (`scipy.optimize.differential_evolution`, `tol=1e-12`, cross-checked
with multiple seeds), and (b) independently, exact algebra (below). Both agree
exactly:

```
p1  = (0.7, 0.2, 0.1)        V(p1)  = 0.55   (attained by k=(1,0,0))
p2  = (0.34, 0.33, 0.33)     V(p2)  = 0.50   (attained by k=(1,0,0))
mid = (0.52, 0.265, 0.215)   V(mid) = 0.52   (attained by k=(1,0,0))
```

`V(mid) = 0.52 < (V(p1)+V(p2))/2 = 0.525`. **This is exactly round 1's
falsifying instance, reproduced with the true, exhaustively-verified `V`, not
an approximation.** Per Step 0's explicit instruction, this means the
approach must STOP here and be reported RETHINK — which is what this file
records. What follows documents the reconciliation itself (what exactly the
"true V" computation entailed) and a rigorous explanation of *why* the Lemma
C' repair (refine the type until each piece is affine) cannot rescue global
concavity — recorded for the benefit of any future revival attempt, so the
same dead end is not rediscovered from scratch.

**What was verified, precisely (closing the "was round 1 using an
approximation?" question the gate raises).** For the composition `(1,0,0)`
(one mark splitting `p_1` into `x, p_1-x`, tail `p_2,p_3` untouched), I did a
*complete* case analysis over `x ∈ [0,p_1]` (using the symmetry
`oddrank({x,p_1-x,p_2,p_3}) = oddrank({p_1-x,x,p_2,p_3})`, so WLOG
`x ∈ [p_1/2, p_1]`, writing `y=p_1-x≤x`). Sorting `{x,y,p_2,p_3}` splits into
six sub-regions of `x` according to how `x` compares to `p_2` and how `y`
compares to `p_2,p_3`:

1. `x≥p_2`, `y≥p_2`: order `x,y,p_2,p_3` ⇒ `oddrank = x+p_2` (increasing in `x`).
2. `x≥p_2`, `p_3≤y<p_2`: order `x,p_2,y,p_3` ⇒ `oddrank = x+y = p_1` (**constant**).
3. `x≥p_2`, `y<p_3`: order `x,p_2,p_3,y` ⇒ `oddrank = x+p_3` (increasing in `x`).
4. `x<p_2`, `x≥p_3`, `y≥p_3`: order `p_2,x,y,p_3` ⇒ `oddrank = p_2+y = p_1-x+p_2` (decreasing in `x`).
5. `x<p_2`, `x≥p_3`, `y<p_3`: order `p_2,x,p_3,y` ⇒ `oddrank = p_2+p_3 = 1-p_1` (**constant**).
6. `x<p_3`: order `p_2,p_3,x,y` ⇒ `oddrank = p_2+x` (increasing in `x`).

Regions 1,3,4,6 are strictly monotone in `x`, so their contribution to the
minimum is pushed to their boundary with an adjacent constant region (2 or 5)
or to the overall domain boundary `x=p_1/2`. Region 2 (value `p_1`) is
non-empty exactly when `p_1 > p_2+p_3 = 1-p_1`, i.e. `p_1>1/2`; region 5
(value `1-p_1`) is non-empty exactly when `p_1<1/2`. So together they
contribute exactly `max(p_1,\,1-p_1)` (continuously, one or the other is
active depending on which side of `1/2` the value `p_1` falls on). The
boundary value `x=p_1/2` (`x=y`) gives, by the tie-pair fact "two equal
elements occupy one odd and one even rank, contributing that value exactly
once regardless of where the tied pair sits in the sort" (immediate from the
`oddrank` definition), `oddrank = p_1/2 + p_2` **for every** relative position
of `p_1/2` versus `p_2,p_3`. Hence:

```
V_{(1,0,0)}(p) = min( max(p_1, 1-p_1),  p_1/2 + p_2 ).      (†)
```

Checking `(†)` against the three points: `p1`: `max(.7,.3)=.7`,
`p_1/2+p_2=.55` ⇒ `min=.55` ✓. `p2`: `max(.34,.66)=.66`, `.17+.33=.50` ⇒
`min=.50` ✓. `mid`: `max(.52,.48)=.52`, `.26+.265=.525` ⇒ `min=.52` ✓. All
three match the numeric search exactly, and (by the exhaustive enumeration
over all 7 compositions, see the differential-evolution search) composition
`(1,0,0)` is in fact the overall minimizer at all three points, so
`V(p) = V_{(1,0,0)}(p)` there. **The Step 0 gate is conclusively passed
(reproduced): this is not an artifact of round 1's optimizer, it is the true
value, confirmed by exact closed-form algebra.**

### Why Lemma C' cannot rescue this (structural, not just "not yet done")

Identity `(†)` is the key structural fact, and it explains *why* the round-3
Lemma C' repair strategy is doomed, not merely incomplete:

- The "always-affine" candidate `p_1/2+p_2` (equal split) really is affine in
  `p` on the whole simplex — no refinement issue there.
- But the *other* strategy available under the same discrete type "one mark
  splits `p_1`" — namely "tie the split to `p_2`" — does **not** simplify to a
  single affine function of `p` even after correctly solving the inner
  continuous optimization and restricting to its own natural sub-region. Its
  true value is `max(p_1, 1-p_1)`: a **convex** (upward) kink in `p_1`, not an
  affine function, and not even concave on its own. This is not a case of "we
  didn't refine finely enough" — refining the type further (splitting into
  the `p_1≥1/2` and `p_1<1/2` sub-cases) makes each *piece* affine
  (`p_1` resp. `1-p_1`), exactly as Lemma C' anticipated, but the two
  resulting affine pieces are joined by a **max**, not a min: on region
  `p_1≥1/2` this branch equals `p_1` and on `p_1<1/2` it equals `1-p_1`, and
  `p_1` is the larger of the two exactly on the region where it's active
  (that is what makes it a "max", i.e. convex kink, structurally, rather than
  a "min", i.e. concave kink) — this is forced by the mechanics of the game
  (it is precisely because Xiang Yu is choosing which of two nearly-tied
  candidate ranks to sacrifice that the *worse* of the two local options,
  not the better, ends up describing the achieved value in each region).
- `V(p)` is then the **min** of this genuinely convex function `max(p_1,1-p_1)`
  together with the genuinely affine function `p_1/2+p_2` (and possibly other
  combinatorial-type contributions, which only make `V` smaller still). A
  min of a concave (affine) function and a convex function is, in general,
  **neither concave nor convex** — and indeed dips below the affine function's
  chord exactly where the convex piece is active and lower, which is exactly
  what happens at `p=mid` (`max(p_1,1-p_1)=0.52` is active and beats
  `p_1/2+p_2=0.525` there, while at the two endpoints `p1,p2` the affine
  branch is the active/smaller one). This is not a failure of proof
  technique or of "not refining enough" — Lemma C' explicitly anticipated
  needing pieces to be affine after refinement, and here refinement *does*
  produce affine pieces, but they combine via `max` (convex) at one level
  before being combined via `min` (concave) at the outer level, and that
  inner `max` is exactly what breaks concavity of the whole. No finite
  re-refinement of "type" changes this: the two pieces `p_1` and `1-p_1` are
  already the finest possible refinement (they are honest affine functions,
  each exactly the achieved value on its exact region of validity), and their
  `max` is unavoidable because BOTH are genuinely optimal-for-Xiang-Yu
  sub-strategies within their own regions and Xiang Yu is a **minimizer**
  choosing the smaller of `{max(p_1,1-p_1), p_1/2+p_2}` — the `max` itself
  arises from the tie-branch's own internal case split, which is intrinsic to
  the combinatorics of `oddrank` (which element the "tied pair" pushes to an
  odd vs. even rank depends discontinuously, in a convex-kink way, on whether
  `p_1` or `1-p_1` is larger), not from an artifact of an under-refined proof.

**Conclusion.** The global-concavity framing (`majorization-smoothing`'s
entire selling point: "V is concave, so a single subgradient inequality at
`p*=A_n` proves both halves of the minimax at once") is **false**, confirmed
both numerically (exhaustive search, reproducing round 1 exactly) and via a
full closed-form derivation exposing the exact mechanism (a convex kink
nested one level inside the outer min). This is a genuine structural
obstruction to the *whole* approach, not a gap in a particular lemma's proof;
per the round-3 outline's own mandatory gate, this approach is retired
(RETHINK) rather than carried forward with a patched Lemma C'.

## Full proof
(Not applicable — Status is `unsolved`. This approach does not yield a proof
of the problem; see "Current best" for the completed negative result.)

## Promotable lemmas

- **Closed form for the `m=3, one-mark-on-top` Xiang-Yu value** (proved in
  full above, identity `(†)`): for sorted `p=(p_1,p_2,p_3)`,
  `p_1+p_2+p_3=1`, the best value Xiang Yu can achieve using a single mark
  that splits only `p_1` is exactly
  `V_{(1,0,0)}(p) = min(max(p_1, 1-p_1),\ p_1/2+p_2)`.
  This is a complete, from-scratch, case-exhaustive derivation (six sorted
  sub-regions of the split point `x`, each shown affine or constant, endpoints
  matched) and could be useful to `geometric-dominance-construction` /
  `recursive-embedding-induction` as a concrete `k=1`, `n=2` exact-value data
  point (not just a lower bound) if either needs to sanity-check their
  general-`n` formulas against a fully solved small case. Not yet certified —
  offered here for the reviewer to certify into `lemmas/` if useful.
- **Structural non-concavity mechanism** (the convex-kink-inside-a-min
  argument above): a from-scratch proof that `V(p)` genuinely fails to be
  concave, with the exact mechanism identified (not just a numeric
  counterexample) — useful negative-result documentation so this framing
  is not attempted again without a fundamentally different fix.
