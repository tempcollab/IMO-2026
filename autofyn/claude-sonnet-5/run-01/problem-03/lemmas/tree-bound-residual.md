# Lemma TREE-BOUND-RESIDUAL (round 9, `recursive-embedding-induction`)

**Closes gap (b)'s last remaining sub-case**: a cross-piece tie where the
tied coordinate is the *minority* part of a 2-part-split piece, pinned at
an *external* anchor `t_j` with `j>i+1` (companion `c=t_i-t_j` generically
**not** a power of `2`). Extends the certified **Lemma TREE-BOUND**
(`lemmas/tree-bound-anchor.md`) and its **Sub-lemma ODD** by allowing
exactly one "forced-residual" (non-anchor) leaf anywhere in the forest,
using only the already-certified **Lemma D-BOUND**
(`lemmas/alternating-sum-toolkit.md`) — no new machinery beyond D-BOUND
and elementary arithmetic on the geometric anchors.

## Setting

Same normalization as `lemmas/tree-bound-anchor.md`: `τ_1>τ_2>\cdots>τ_m`
with `τ_l=2^{m-l}` (so `τ_1=2τ_2=\cdots`), an `(m,r)`-forest is `r`
independent trees rooted at `τ_1` plus one standard tree at each of
`τ_2,\ldots,τ_m`, and every *pure* tree is a binary subdivision tree
(Fact 0: a node of value `2^e` either stays a leaf or splits exactly into
two nodes of value `2^{e-1}`).

**Definition (impure/residual node).** A node of current value `τ_i` may,
instead of staying a leaf or splitting purely, undergo **one impure cut**:
it terminates immediately into exactly two leaves
$$y:=τ_j,\qquad c:=τ_i-τ_j,\qquad\text{for some }j>i,$$
i.e. it stops `j-i` levels early and dumps everything it would otherwise
have produced below level `i+1` into one un-split lump `c`. (This is
exactly the situation arising from the gap-(b) vertex: `y=τ_j` is the tied
minority coordinate, `c` is its companion.) At most **one** node in the
*entire* forest is allowed to be impure; every other node is pure.

**Definition (generalized `(m,r)`-forest).** An `(m,r)`-forest-with-at-
most-one-impurity is an `(m,r)`-forest in which every node is pure except
possibly one, anywhere in the whole structure (in any of the `r` top
trees or any of the `m-1` standard trees, at any depth), which may be
impure as just defined.

## Lemma TREE-BOUND-RESIDUAL (= Sub-lemma ODD, extended)

**Statement.** For every `m≥1`, every odd `r≥1`, and every `(m,r)`-forest-
with-at-most-one-impurity, the merged leaf multiset `B` satisfies
`D(B)≥τ_m`.

*Proof, by strong induction on `m`, extending `lemmas/tree-bound-anchor.md`'s
Sub-lemma ODD proof verbatim except for one new case.*

**Base case `m=1`.** No node in the forest has value `2^e` with `e≥1`
(every tree is already at the bottom exponent `0`), so no impure cut is
possible at all: the forest is automatically pure, and the base case is
identical to the original Sub-lemma ODD (`r` copies of `τ_1=τ_m=1`,
`D=τ_m` exactly since `r` is odd).

**Inductive step, `m≥2`, `r` odd.** As in the original proof, split on
whether the (at most one) impure node lies at the **current top level**
(one of the `r` trees rooted at `τ_1` is *itself* impure, i.e. the impure
cut happens at that tree's root) or **strictly below** it.

- **Impurity strictly below the top level** (inside a lower-level standard
  tree, or inside one of the `r-k` top trees that undergoes a *pure* first
  split before the impurity occurs deeper inside one of its two `τ_2`-
  children). Peeling the top level exactly as in the original proof: `k`
  of the `r` top trees are leaves, `r-k` split purely into two `τ_2`-
  children; the merged leaves below the top block form an
  `(m-1,r')`-forest (`r'=2(r-k)+1`, automatically odd) which now carries
  the (at most one) impurity somewhere inside it. This is *exactly* an
  instance of the statement one level down (`m-1<m`), so the **strong
  induction hypothesis directly applies**: whatever is inside the
  remainder, `D(\text{remainder})≥τ_m` (`k` even case, `D(B)=
  D(\text{remainder})`) — or, for the `k` odd case, we use **Lemma
  D-BOUND** exactly as in the original proof, which needs only that every
  element of the remainder is `≤τ_2$: this holds regardless of any
  impurity inside the remainder, since **every leaf produced by any node
  — pure or impure — has value at most its parent's value** (an impure
  cut at a node of value `τ_i≤τ_2` produces `y,c<τ_i≤τ_2`). So
  `0≤D(\text{remainder})≤τ_2`, giving `D(B)=τ_1-D(\text{remainder})≥
  τ_1-τ_2=τ_2≥τ_m` exactly as before. Both sub-cases match the original
  proof's case analysis with no new content needed.

- **Impurity exactly at the current top level (new Case C).** One of the
  `r` top-level trees is *itself* the impure node: instead of being a leaf
  or a pure split, it directly produces leaves `\{y,c\}` with `y=τ_j$,
  `c=τ_1-τ_j` for some `2≤j≤m$ (local re-indexing: `j=2` means `c=τ_2`,
  the "aligned" case that is really just a disguised pure split;
  `j\ge3` is the genuinely new residual case). Let `k'$ (`0≤k'≤r-1`) be the
  number of the *remaining* `r-1` trees that are leaves (of value `τ_1`),
  so `r-1-k'$ of them split purely into two `τ_2`-children each. Write
  $$X:=\bigl[\,2(r-1-k')\text{ copies of }τ_2\,\bigr]\ \cup\ \bigl[\text{the
  standard trees at }τ_2,\ldots,τ_m\bigr],$$
  the merged leaves of everything *except* the top block and the impure
  tree — by construction every element of `X` is `≤τ_2` (every standard
  tree is rooted at a value `≤τ_2`, and every leaf of a subtree is at most
  its root's value), and `X$ is itself (with `τ_2,\ldots,τ_m$ replaced by
  its own top-through-bottom anchors) exactly an `(m-1,r'')`-forest,
  `r''=2(r-1-k')+1$ (odd), so **by the strong induction hypothesis
  `D(X)≥τ_m$.**

  The full merged list is `B = [\,k'\text{ copies of }τ_1\,]\ \cup\
  X\ \cup\ \{y,c\}$. Two elementary facts about `y,c` (both immediate from
  `j≥2`, `τ_i=2τ_{i+1}$):
  $$0<y=τ_j≤τ_2,\qquad c=τ_1-τ_j\ \ge\ τ_1-τ_2=τ_2,$$
  with the second inequality an equality exactly at `j=2`. So `c≥τ_2≥$
  every element of `X` and `c≥τ_2≥y` (since `j\ge2\Rightarrow y\le τ_2$);
  i.e. **`c` is always a maximum of `X\cup\{y,c\}`** (tied with any
  `τ_2`'s present in `X$ when `j=2`, strictly the unique maximum when
  `j≥3`, since then `c=τ_2+τ_3+\cdots+τ_j>τ_2$ using the telescoping
  identity `τ_2+\cdots+τ_j=τ_1-τ_j$, itself immediate from
  `τ_i=2τ_{i+1}$ summed as a geometric series).

  Exactly as in the original proof, the top block of `k'` copies of `τ_1`
  (still the unique overall maximum, since `y,c<τ_1$ always) contributes
  `0` to `D(B)` and preserves the remainder's sign if `k'` is even, or
  contributes `τ_1` and flips the remainder's sign if `k'` is odd, where
  the "remainder" is now `R:=X\cup\{y,c\}$ (size `|X|+2`):
  $$k'\text{ even:}\quad D(B)=D(R),\qquad\qquad
    k'\text{ odd:}\quad D(B)=τ_1-D(R).$$

  **Two applications of the already-certified Lemma D-BOUND close both
  sub-cases:**

  - **`k'` odd.** `R=X\cup\{y,c\}$ is a finite sorted nonnegative list with
    maximum `c` (shown above), so Lemma D-BOUND gives `0≤D(R)≤c`. Hence
    $$D(B)=τ_1-D(R)\ \ge\ τ_1-c\ =\ τ_1-(τ_1-τ_j)\ =\ τ_j\ \ge\ τ_m$$
    (the last step since `j≤m`). ✓
  - **`k'` even.** `D(B)=D(R)$. Write `Y:=X\cup\{y\}` (size `|X|+1`,
    maximum `≤τ_2` since both `X`'s elements and `y=τ_j≤τ_2` are `≤τ_2`).
    Inserting `c` — the maximum of `Y\cup\{c\}=R` — at sorted rank `1`
    (Lemma D-INSERT with `r=1`, `τ(1)=D(Y)`, `(-1)^{1+1}=+1`) gives the
    exact identity `D(R)=c-D(Y)`. By Lemma D-BOUND applied to `Y`,
    `0≤D(Y)≤τ_2$, so
    $$D(B)=D(R)=c-D(Y)\ \ge\ c-τ_2\ =\ (τ_1-τ_j)-τ_2\ =\ τ_2-τ_j$$
    (using `τ_1=2τ_2`). If `j=2` this already reduces to
    `D(B)\ge τ_2-τ_2=0`; but `j=2` is the aligned/pure case, where in fact
    `y=c=τ_2` exactly and the elementary "adding a pair of equal maxima
    changes `D` by `0`" fact (immediate from Lemma D-INSERT applied
    twice, or directly: a block of `τ_2`'s changes size by an even amount
    `+2`, preserving its own parity-contribution and shifting everything
    below by an even amount) gives the sharper `D(B)=D(X)≥τ_m$ directly
    from the induction hypothesis — so `j=2` is fully covered either way.
    For the genuinely new case `j≥3`: `τ_j≤τ_3$ (anchors are decreasing),
    so
    $$D(B)\ \ge\ τ_2-τ_j\ \ge\ τ_2-τ_3\ =\ τ_3\ \ge\ τ_m$$
    (using `τ_2=2τ_3`, and `τ_3≥τ_m` since `j≥3\Rightarrow m≥3\Rightarrow
    3≤m`). ✓

  Both sub-cases give `D(B)≥τ_m`, completing Case C, hence the inductive
  step, hence the induction on `m`. `\blacksquare`

### Consequence: Lemma TREE-BOUND-RESIDUAL for the original problem

Peeling `P_1`'s forced root split turns the `n≥2` case into an
`(n,3)`-forest exactly as in `lemmas/tree-bound-anchor.md`; the impurity
(if present anywhere, including possibly inside `P_1`'s own peeled
children) is carried through this peeling into the resulting
`(n,3)`-forest-with-at-most-one-impurity, to which the Lemma above applies
directly (`r=3` odd): **`D(B)≥t_n=1` for every anchor-only-except-one-
residual-leaf configuration**, i.e. every configuration in which Xiang Yu
splits every piece into anchor values except for **exactly one** piece
which he splits into an anchor value `y=t_j` (its minority part, tied
cross-piece) and one un-split, generically non-anchor companion
`c=\mathrm{top}_π-t_j$.

## Independent verification

**Exhaustive** (`m,r\in\{(2,3),(3,3),(4,3)\}`, i.e. the full original
`(n,3)`-forest problem for `n=2,3,4`): enumerated *every* choice of (i)
which single node in the whole forest hosts the impurity, (ii) every
possible impure cut `(τ_j$-value) at that node, and (iii) every possible
pure binary-tree shape for every other node (up to `36` shapes per
`τ_2`-rooted tree at `n=4`) — **minimum `D` found is exactly `1=t_n` in
every single case, zero violations** (`/tmp/verify3.py`, reproduced in the
build). This is strictly stronger than what the Lemma requires (it
additionally confirms optimality is not beaten by *any* impure placement
or shape, not merely that the bound holds).

**Randomized** (`n=2,\ldots,12`, `17{,}876$ trials, exact `Fraction`
arithmetic, impurity placed at the root of a uniformly random tree slot
with uniformly random depth `j`, every other tree given a random pure
shape via unbiased recursive coin-flip): **zero violations**
(`/tmp/verify_final.py`). Also independently confirmed the two concrete
witnesses reported by this round's `math-explorer-crosstie.md`: `n=4`
symmetric two-minority tie (reported `D=11≫t_4=1`) and `n=6`
external-anchor-snap residue (`c=14$, reported `D=43≫t_6=1`) — both
match the Lemma's bound with large margin, consistent with the Lemma's
own (non-tight, but always-sufficient) quantitative bound `D(B)≥τ_j$ or
`≥τ_2-τ_j$ respectively derived in the two sub-cases above.

## Honest note on the round-9 plan's proposed mechanism

The round-9 plan proposed comparing the residual configuration directly
to its "virtually fully split" counterpart (replacing the one residual
leaf `c` by the deeper anchor chain `t_{i+1},\ldots,t_j$ it stands for) via
a single domination inequality. **This naive direct comparison is FALSE in
general** — a stress test with the two configurations' *common* background
list left otherwise unconstrained (i.e. an arbitrary sorted list, not
tied to an actual achievable forest remainder) produced violations in
`159/600` random trials (`/tmp/verify1.py`). The correct route (this file)
does not compare "residual" against "virtually split" as a single
external inequality at all; instead it reruns the *induction itself* with
a third case (Case C, above), bounding `D(B)` directly via two applications
of the already-certified Lemma D-BOUND — which turns out to require only
elementary arithmetic on the geometric anchors, not a comparison to a
different (fully split) configuration. This matches the plan's flagged
risk ("verify the direction of inequality carefully... report honestly if
it fails") — the specific mechanism sketched needed correction, but the
underlying goal (extend the forest recursion to forced-residual leaves)
is achieved by a different, and simpler, route.

## What this closes

Combined with the already-certified `lemmas/cross-tie-affine.md` (which
reduces every cross-piece tie to either the well-separated case, the
self-meeting-point case, or exactly this minority/deep-bracket residue
case) and `lemmas/tree-bound-anchor.md` (gap (a), anchor-only, every
budget), **this closes gap (b) in full**: every cross-piece tied free
coordinate, in every one of the three sub-cases identified by
`cross-tie-affine.md`, now satisfies `D(B)≥t_n`. Together with the
already-certified well-separated single-free-coordinate case (round 7) and
the anchor-only case (round 8), **Lemma PARITY-PAIR-GEN's lower bound
`D(B)≥t_n$ for every Xiang-Yu-reachable configuration against the
geometric construction `A_n` is now fully proved**, for every `n≥1` and
every budget `≤n`.

## What this does not close

This closes the **lower bound for the specific geometric configuration
`A_n`** (i.e. that Liu Bang, playing `A_n`, guarantees at least `c(n)`
against every Xiang Yu response) — combined with the already-certified
Lemma 1–4/Proposition 4 (Xiang Yu's matching upper-bound response showing
`A_n` gives *exactly* `c(n)`, not more), this fully proves `A_n`'s value is
exactly `c(n)`. It does **not** address the separate, explicitly
out-of-scope-for-this-approach question of whether some *other*
(non-geometric) configuration could let Liu Bang guarantee *more* than
`c(n)` — the "general upper bound over all Liu Bang configurations",
which this approach has never attempted and which belongs to
`universal-adversary-strategy` (see that approach's own status).

## Status

Certified (round 9). Sub-lemma ODD's Case C extension is fully proved
using only the already-certified Lemma D-BOUND (twice) plus elementary
geometric-anchor arithmetic; independently verified both exhaustively
(`n=2,3,4`, every impurity placement/shape) and by large-scale randomized
exact-`Fraction` sampling (`n=2,\ldots,12`, `17{,}876` trials, zero
violations), and cross-checked against this round's explorer's two
hand-built numeric witnesses.
