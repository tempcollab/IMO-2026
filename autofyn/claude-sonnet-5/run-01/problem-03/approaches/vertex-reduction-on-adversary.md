## Status
unsolved

## Approaches tried
- **Vertex/extreme-point reduction on the adversary's configuration `A`**
  (this round, feasibility check only, scoped to `m=4` Case C Region 1 ∪
  Region 2, already fully proved by `universal-adversary-strategy` /
  `lemmas/m4-region-a-region-b.md`) — **re-derivation succeeds cleanly, but
  is confirmed to be a restatement of the existing proof in vertex language,
  not an independent proof route.** No new inequality was proved, no new
  case was closed. See full analysis below. Not a dead end in the sense of
  "wrong" — the framing is correct and does recover the known extremal
  witness exactly — but it supplies no leverage this run doesn't already
  have, and its extension to Region 3 / general `m` is genuinely
  high-risk (unresolved combinatorial-blowup concern, consistent with the
  explorer's own flag), not a shortcut past the open gaps.

## Current best
Nothing new toward closing the problem. What is established (restatement,
not new content):

**Setup — reduce to a bounded polytope.** Both the objective `V_4(A)` (via
each strategy formula) and the target `c(3)\Sigma(A)` are positively
homogeneous of degree 1 in `A`, so by scale invariance we may fix `\Sigma=1`
WLOG. `m=4` Case C, projected to `\Sigma=1`, is the bounded polytope
```
P_C = \{(p_1,t_1,t_2,t_3)\in\mathbb R_{>0}^4 : p_1\ge t_1\ge t_2\ge t_3,\ 
       p_1+t_1+t_2+t_3=1,\ p_1<1/2\}.
```

**Region 1 (`t_1\ge4/15`), re-derived in vertex language.** The certified
bound (Lemma m=4-REGION-A) is
```
\mathrm{StratA}=t_1+V_3(t_2,t_3,p_1-t_1)\le t_1+\tfrac47(1-2t_1)=\tfrac47-\tfrac{t_1}7
```
(Lemma V3-BOUND applied to the sub-triple `(t_2,t_3,p_1-t_1)`). This RHS is
**affine in `t_1` alone** (equivalently affine in `A`, since `t_1` is a
linear functional of `A`) and strictly decreasing, so on the closed interval
`t_1\in[4/15,\,1/2)` (Region 1 intersected with Case C) its supremum is
attained at the *smaller* endpoint `t_1=4/15`, where it equals `c(3)=8/15`
exactly. This is exactly `aimo-0656`'s corner-optimum principle applied to
one coordinate.

Important nuance found in re-deriving this: the bound depends on `A` **only
through `t_1` and `\Sigma`**, not on `p_1,t_2,t_3` individually, so the
"worst" locus `\{t_1=4/15\}` is a whole 2-dimensional facet of `P_C`, not an
isolated vertex — the naive "vertex of the flat 4-D Case-C polytope" claim
from the seed file is **not literally true at the outer level**. The known
extremal point `A=(6,4,3,2)` (`\Sigma=15`) is singled out only by *also*
demanding the inner `V_3`-BOUND application be tight, which (per
`lemmas/v3-bound.md`, Case C) happens exactly when the sub-triple
`(t_2,t_3,p_1-t_1)\propto(3,2,2)`. Checking: `t_1=4,\ p_1=6\Rightarrow
p_1-t_1=2`, and `(t_2,t_3,p_1-t_1)=(3,2,2)` — proportional to `(3,2,2)`
exactly. So `(6,4,3,2)` is recovered precisely as the intersection of the
outer facet `t_1=4/15\Sigma` with the *inner* recursive cell's own extremal
vertex — a **nested vertex of a nested (product) cell structure**, not a
vertex of a single flat LP. This is a genuine, verified structural fact, and
a more accurate statement of the vertex-reduction principle than the seed
file's first pass: extremality must be tracked recursively through the
strategy tree, one affine reduction per recursive call, not as one flat
optimization over `A\in\mathbb R^4`.

**Region 2 (`t_1<4/15`, tail in `V_3`-Case-B), re-derived in vertex
language.** Here `V_3(t_1,t_2,t_3)=t_1` exactly (no loose bound needed), so
`\mathrm{StratB}=p_1/2+t_1` is affine in `(p_1,t_1)` and increasing in both.
Region 2's domain is open in both defining directions: `p_1<1/2` (Case C)
and `t_1<4/15` (Region 2's own condition), so the supremum of the affine
function is approached at the corner `(p_1,t_1)\to(1/2,4/15)` but **not
attained**, giving:
```
\sup \mathrm{StratB} \to \tfrac12\cdot\tfrac12+\tfrac4{15}=\tfrac{31}{60}<\tfrac{32}{60}=c(3),
```
margin exactly `1/60` in the limit — this reproduces the certified Lemma's
stated margin `\ge\Sigma/60` exactly, and explains why the inequality is
strict rather than merely `\le`: the extremal corner lies just outside the
open region.

**Assessment (per this round's mandate, step 3).** Honest verdict: **this is
a restatement, not new leverage**, for Region 1/2. Every piece of work
needed to prove Region 1/2 — deriving the loose `V_3`-BOUND, checking the
sign of the derivative in `t_1`, and doing the boundary arithmetic — is
identical to what `lemmas/m4-region-a-region-b.md` already did; the vertex
language only supplies a *post hoc* explanation of why the ad hoc
monotonicity argument worked (because the relevant bound is affine, and
affine functions on an interval extremize at an endpoint — a true but
unsurprising fact once stated), plus one nontrivial correct refinement (the
"nested vertex," not flat vertex, structure, confirmed to match `(6,4,3,2)`
exactly). It produced zero new inequalities and closed zero new territory.

**On `A=(8,4,3,2)` (per the task's step 2).** This point is **not** in
Region 1 ∪ Region 2 — per `/tmp/round-17/math-explorer-region3.md`, it has
`\Sigma=17`, `t_1/\Sigma=4/17\approx0.235<4/15`, and its tail is *not* shown
to be in `V_3`-Case-B, so it sits in the still-open Region 3, outside this
round's scope. It is also **not** a target-tight extremal point: all five
strategies coincide there (`=9`), but the shared value has strict positive
margin `1/15` against target `136/15` (margin `1/255\cdot\Sigma`), unlike
`(6,4,3,2)` where `\mathrm{StratA}=c(3)\Sigma$ exactly. Under the
vertex-reduction framing it *is* a natural vertex-type object — the
intersection of all five strategies' affine-cell boundaries (a "5-way tie"
vertex of the strategy arrangement) — but since it is not tight against the
target, it does not correspond to a binding constraint, and confirming this
required no more than restating the existing round-17 numeric finding in
vertex language. No independent confirmation power beyond what was already
known.

**Extension to Region 3 / general `m` (step 4, kept brief per the mandate).**
Sketch only, not attempted: in principle the same recursive-nested-vertex
description applies to `V_4=\min(\mathrm{StratA},\mathrm{StratB},
\mathrm{StratC}_{12},\mathrm{StratC}_{13},\mathrm{StratC}_{23})$ throughout
Case C, since each `\mathrm{StratC}_{ij}=t_j+V_3(\cdot)` is likewise affine
within any fixed branch of its own nested `V_3`/`L_2` calls
(`universal-adversary-strategy.md` lines 437–439). So the *type* of
argument extends mechanically. But this does **not** resolve the open risk
flagged by the originating explorer: the number of nested cells is the
product, over all five strategies, of the number of branches each one's
recursive sub-calls can take, and Region 3 is precisely the zone where *no*
single strategy's loose bound suffices uniformly (per
`/tmp/round-17/math-explorer-region3.md` §4) — i.e. exactly where the
cell/vertex enumeration would need to be done in full, which is neither
smaller nor structurally simpler than the case-split
`universal-adversary-strategy` is already carrying out. Nothing found this
round suggests the vertex framing collapses that casework to fewer cases;
it only relabels the same cases as "vertices of cells." For general `m\ge5`
the risk is the same one order of magnitude worse (the recursion tree is
one level deeper, so the cell count is a product over more levels) and was
not tested at all here, per the mandate's explicit scope limit.

**Conclusion:** legitimate, confirmed-correct feasibility check with a
negative-for-leverage result on Region 1/2, and an unresolved (not
positive, not refuted) outlook for Region 3/general `m`. Recommend: do not
promote this to a competing build for Region 3 unless a future round can
show the nested-cell count is provably small (e.g. polynomial, not
exponential, in `m`) — otherwise it degenerates into the same "more
casework" outcome that killed `minimax-mixed-duality` (RETHINK, rounds 6-9)
and `case-c-secondary-extremality` (RETHINK, round 11).

## Full proof
Not applicable — Status is `unsolved`. No new result toward the problem was
established; this file records a feasibility/framing check only, per the
outline-reviewer's round-17 scoping mandate.
