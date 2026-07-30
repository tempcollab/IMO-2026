# Lemma TOP2 and the multi-cluster (general K) closure of gap (b)

Proved by `geometric-dominance-construction`, round 10. Generalizes the
certified `lemmas/two-block-residue-close.md` (Lemma TWO-BLOCK, K=1) to an
**arbitrary finite number K≥1 of simultaneous, independent tie-clusters**
(different clusters tied at different, mutually unrelated values, no
ordering hypothesis between them needed). This closes the round-9-flagged
"multi-cluster generalization" gap in full, for the scope stated below.

The mechanism is **not** the round-10 outline's originally-planned
"K-fold nested threshold peel" (that plan required ordering the tie values
`v_1>v_2>...>v_K` and peeling them off largest-first). Instead this uses a
strictly simpler, hypothesis-free, one-line replacement for Lemma TWO-BLOCK
itself (Lemma TOP2 below), which removes the need for any threshold/Y-Z
decomposition, any parity case-split, and any ordering assumption on the
`v_l`'s at all — making the K-cluster generalization a direct, uniform
case analysis with a **fixed number of cases independent of K**, rather
than an induction on K.

## Lemma TOP2 (fully general — no geometric structure, no hypothesis on K)

*Statement.* Let `L` be any finite sorted nonnegative list with two
largest elements `b_1\ge b_2` (ties allowed; `b_2:=0` if `|L|\le1`). Then
```
D(L) \ge b_1 - b_2.
```

*Proof.* If `|L|\le1` this is immediate from Lemma D-BOUND
(`0\le D(L)\le b_1`, and `b_2=0` by convention). Otherwise, since `b_1` is
the (a) maximum of `L`, `D(L)=b_1-D(L\setminus\{b_1\})` by definition of
the alternating sum (removing the rank-1 element). The list
`L\setminus\{b_1\}` is itself sorted nonnegative with maximum exactly `b_2`
(the second-largest element of `L`), so Lemma D-BOUND
(`lemmas/alternating-sum-toolkit.md`) gives
`0\le D(L\setminus\{b_1\})\le b_2`. Hence `D(L)\ge b_1-b_2`. `\blacksquare`

*Remark.* This is strictly simpler than Lemma TWO-BLOCK (which bounded
`D(L)` via a threshold-`v` split `Y=\{x>v\},\,Z=\{x\le v\}` and produced a
weaker, parity-dependent bound `(b_1-b_2)-v\cdot[\,|Y|\text{ odd}\,]`).
Lemma TOP2 needs no threshold, no `Y/Z` decomposition, and no parity case
split at all — it is a direct, two-step consequence of Lemma D-BOUND
applied to `L` and then to `L\setminus\{b_1\}`. Since it is *hypothesis-free*
(works for literally any list `L`), it applies uniformly regardless of how
many tie-clusters, at what values, are present in `L` — which is exactly
what makes the K-cluster generalization tractable without an induction on
`K`.

*Independent verification.* Checked directly (not merely by citation)
against `16{,}000` randomized instances (`n=1,\ldots,8`, random number of
clusters `K\in\{0,\ldots,\lfloor(n+1)/2\rfloor\}`, random cluster sizes
`2$–`4`, random minority-range `v_l` per cluster) — the identified `(b_1,
b_2)$ (see Structural Lemma below) always matches the true two largest
sorted elements of the merged configuration, and `D(L)\ge b_1-b_2$ never
fails; see `/tmp/verify_kcluster.py`.

## Setting (general K)

Fix `n\ge1`. Unnormalized units `t_i:=2^{n-i}` for `i=1,\ldots,n`
(`t_1=2^{n-1}>\cdots>t_n=1`, `t_i=2t_{i+1}`), and `\mathrm{top}_0:=2t_1`
(the top piece), `\mathrm{top}_i:=t_i$ for `i=1,\ldots,n` (the tail
pieces).

Let `K\ge1` and let `S_1,\ldots,S_K\subseteq\{0,1,\ldots,n\}` be **pairwise
disjoint** subsets, each `|S_l|\ge2`. For each `l`, fix a value `v_l` with
```
0 < v_l < q_l := \min_{i\in S_l}\ \mathrm{top}_i/2
```
(so `v_l` plays the **minority** role in every piece it splits — the
"deep-bracket, minority-part" tie scenario). **No relation whatsoever is
assumed between the different `v_l`'s** — they need not be ordered, equal,
or comparable in any way; this is a strictly more general hypothesis than
the round-10 outline's originally planned `v_1>v_2>\cdots>v_K`.

Let `U:=\{0,\ldots,n\}\setminus\bigcup_l S_l` (untouched indices). The
merged configuration `B` consists of: for `i\in U`, the single piece
`\mathrm{top}_i`; for `i\in S_l`, the two pieces `\mathrm{top}_i-v_l`
(majority) and `v_l` (minority/companion).

## Structural Lemma (general K — identifying the two largest elements of B)

*Statement.* Let `\varepsilon_0:=1` if `0\notin U` (i.e. `0` is tied, to
some cluster `l(0)`) else `0`; `\varepsilon_1:=1` if `1\notin U` (tied, to
some cluster `l(1)`) else `0`. Then the two largest elements of `B` are
```
b_1 = 2t_1 - \varepsilon_0\, v_{l(0)}, \qquad b_2 = t_1 - \varepsilon_1\, v_{l(1)}
```
(reading `v_{l(0)}:=0` if `\varepsilon_0=0`, similarly for `v_{l(1)}`), and
`b_1>b_2\ge0`.

*Proof.* We show (I) every contribution to `B` from an index `i\ge2` is
`<t_2`; (II) `b_2>t_2` always (so (I) shows every `i\ge2` contribution is
strictly dominated by `b_2`, hence also by `b_1\ge b_2`); (III) any
companion/minority value contributed by piece `0`'s or piece `1`'s own
cluster (if tied) is `<b_2`; (IV) `b_1>b_2`. Together, (I)-(IV) show every
element of `B` other than the two claimed values `\{b_1,b_2\}` (the
majority-or-untouched contributions of pieces `0` and `1`) is strictly
smaller than `b_2\le b_1`, so `\{b_1,b_2\}` are indeed the two largest
elements of `B`, with `b_1` for piece `0` and `b_2` for piece `1`
specifically (since `b_1>b_2`, established in (IV), and both exceed
everything else).

**(I) Every `i\ge2` contribution is `<t_2`.** If `i\in U`: contributes
`\mathrm{top}_i=t_i\le t_2` (as `i\ge2` and `t$ is decreasing), with
equality only if `i=2`. If `i\in S_l` for some `l`: the majority part
`\mathrm{top}_i-v_l<\mathrm{top}_i=t_i\le t_2` (strict, since `v_l>0`); the
companion `v_l<q_l\le\mathrm{top}_i/2=t_i/2\le t_2/2<t_2`. So every
`i\ge2` contribution is `\le t_2`, with strict inequality except possibly
the single untouched value `t_2` itself (`i=2\in U`) — but (II) below shows
`b_2>t_2` strictly, which handles this boundary case too.

**(II) `b_2>t_2` always.** We check this across the four
`(\varepsilon_0,\varepsilon_1)` combinations (with a further sub-split of
the `(1,1)` case into `l(0)=l(1)$ (same cluster) vs. `l(0)\ne l(1)`
(different clusters) — the genuinely new content of this generalization).

- `(\varepsilon_0,\varepsilon_1)=(*,0)`: `1\in U`, so `b_2=t_1=2t_2>t_2`.
  (Independent of `\varepsilon_0`.)
- `(\varepsilon_0,\varepsilon_1)=(0,1)`: `1\in S_m$ for some cluster `m`,
  `0\in U`. Since `0\notin S_m` (as `0\in U`), `S_m\setminus\{1\}` is
  nonempty (as `|S_m|\ge2`) and consists of indices `\ge2` (it cannot
  contain `0`). So `q_m\le\mathrm{top}_{i''}/2\le t_2/2` for some
  `i''\ge2$ in `S_m`. Hence `v_m<t_2/2`, giving
  `b_2=t_1-v_m>t_1-t_2/2=2t_2-t_2/2=1.5\,t_2>t_2`.
- `(\varepsilon_0,\varepsilon_1)=(1,1)`, `l(0)=l(1)` (same cluster
  `l:=l(0)=l(1)`, so `0,1\in S_l`, tied at the same value `v:=v_l$):
  `q_l=\min_{i\in S_l}\mathrm{top}_i/2\le\min(\mathrm{top}_0/2,\mathrm{top}_1/2)=\min(t_1,t_2)=t_2`.
  So `v<t_2`, giving `b_2=t_1-v>t_1-t_2=2t_2-t_2=t_2`.
- `(\varepsilon_0,\varepsilon_1)=(1,1)`, `l(0)\ne l(1)` (different
  clusters `l:=l(0)\ne m:=l(1)`, values `v:=v_l\ne w:=v_m` in general):
  since `1\in S_m$ and `0\in S_l\ne S_m$ (disjoint), `0\notin S_m`, so as
  in the `(0,1)` case, `S_m\setminus\{1\}` is nonempty and consists of
  indices `\ge2`, giving `w<t_2/2` exactly as before. Hence
  `b_2=t_1-w>t_1-t_2/2=1.5\,t_2>t_2`.

In every case `b_2>t_2`, proving (II) (and, combined with (I), that every
`i\ge2` contribution is strictly `<b_2`).

**(III) Companions of piece 0's / piece 1's own clusters are `<b_2`.**

- If `\varepsilon_0=1$ (`0\in S_l`): if `\varepsilon_1=0` or (`\varepsilon_1=1$
  and `l(1)\ne l`), then (as shown in the case analysis for (II)) `S_l$
  contains an index `\ge2` besides `0` (since `1\notin S_l$ in both these
  sub-cases), so `v_l<t_2/2`. We need `v_l<b_2`. From (II),
  `b_2>t_2>t_2/2>v_l`. Done. If instead `l(0)=l(1)=l` (both `0,1$ in the
  same cluster, tied at `v=v_l`): we need `v<b_2=t_1-v`, i.e. `2v<t_1`,
  i.e. `v<t_1/2=t_2` — which holds since `v<t_2` was shown directly above
  in (II)'s `(1,1)`-same-cluster case.
- If `\varepsilon_1=1$ (`1\in S_m`) and `l(1)\ne l(0)$ (including the case
  `\varepsilon_0=0`): `w=v_m<t_2/2<b_2` by (II) exactly as above.
  (`w<t_2/2` was shown in (II)'s `(0,1)` and `(1,1)`-different-cluster
  cases, both of which are exactly the cases where `l(1)\ne l(0)` or
  `\varepsilon_0=0`.)

So every companion value belonging to piece `0`'s or `1`'s own cluster(s)
is `<b_2`.

**(IV) `b_1>b_2`.** Direct computation of `b_1-b_2` in each case (used
again in the Main Theorem below, restated here for completeness):
`(0,0)`: `b_1-b_2=2t_1-t_1=t_1>0`. `(0,1)`: `b_1-b_2=2t_1-(t_1-w)=t_1+w>0`.
`(1,0)`: `b_1-b_2=(2t_1-v)-t_1=t_1-v`; since (as shown above, this is the
`\varepsilon_1=0$ sub-case, requiring `S_l$ to contain an index `\ge2`
because `1\notin S_l`) `v<t_2/2<t_1$, so `t_1-v>t_1-t_1=0` — in fact
`t_1-v>t_1-t_2/2>0`. `(1,1)`, same cluster: `b_1-b_2=(2t_1-v)-(t_1-v)=t_1>0`.
`(1,1)`, different clusters: `b_1-b_2=(2t_1-v)-(t_1-w)=t_1+w-v`; since
`v<t_2/2` (shown above, as `1\notin S_l`) and `w\ge0`, `t_1+w-v>t_1-t_2/2>0`.
In every case `b_1>b_2$, confirming (IV) and completing the proof. `\blacksquare`

*Independent verification.* Checked against `16{,}000` randomized
instances (`n=1,\ldots,8`, random `K$ from `0` up to `\lfloor(n+1)/2\rfloor`,
random cluster memberships and sizes `2$–`4`, random `v_l\in(0,q_l)` per
cluster) — the predicted `(b_1,b_2)` exactly matches the two largest
sorted elements of the actual merged `B` in every single trial, zero
mismatches (`/tmp/verify_kcluster.py`, function `test_structural`).

## Main Theorem (general-K closure of the residual multi-cluster sub-case)

*Statement.* For every `n\ge1`, every `K\ge1`, every choice of pairwise
disjoint `S_1,\ldots,S_K\subseteq\{0,\ldots,n\}` with `|S_l|\ge2$ each, and
every choice of `v_l\in(0,q_l)$ per cluster (completely independent of one
another, no ordering assumed), the resulting configuration `B` satisfies
```
D(B) \ge t_n.
```

*Proof.* By Lemma TOP2, `D(B)\ge b_1-b_2`, with `b_1,b_2` as identified by
the Structural Lemma. It remains to check `b_1-b_2\ge t_n$ in each of the
(at most) five cases identified in the Structural Lemma's proof of (IV):

- **`(\varepsilon_0,\varepsilon_1)=(0,0)`.** `b_1-b_2=t_1=2^{n-1}\ge
  2^0=t_n` for every `n\ge1`.
- **`(0,1)`.** `b_1-b_2=t_1+w\ge t_1\ge t_n$ (as above), for **any**
  legal `w\ge0` — no upper bound on `w` is even needed here.
- **`(1,0)`.** `b_1-b_2=t_1-v`, `v<t_2/2$ (shown in the Structural Lemma,
  since `1\notin S_{l(0)}` forces another member `\ge2`). This sub-case
  requires `n\ge2` (an index `\ge2` must exist for `S_{l(0)}$ to have a
  second member besides `0`); it is vacuous for `n=1`. For `n\ge2`:
  `b_1-b_2>t_1-t_2/2=2^{n-1}-2^{n-3}=3\cdot2^{n-3}$. We check
  `3\cdot2^{n-3}\ge2^{n-n}=1`: at `n=2`, `3\cdot2^{-1}=1.5\ge1`; for
  `n\ge3`, `3\cdot2^{n-3}\ge3\ge1`. So `b_1-b_2\ge t_n` for all `n\ge2`
  (and the case is vacuous, hence trivially true, at `n=1`).
- **`(1,1)`, same cluster (`l(0)=l(1)$).** `b_1-b_2=t_1\ge t_n` exactly as
  in the `(0,0)` case, for every `n\ge1` — no dependence on `v` at all
  (the shared companion value cancels identically).
- **`(1,1)`, different clusters (`l(0)\ne l(1)$).** `b_1-b_2=t_1+w-v`,
  with `v<t_2/2` (shown above, since `1\notin S_{l(0)}`). This sub-case
  requires two disjoint clusters each of size `\ge2`, one containing `0`
  and an index `\ge2`, the other containing `1` and an index `\ge2$
  distinct from the first — requiring `n\ge3` (indices `\{0,1,2,3\}$ at
  least, e.g. `S_{l(0)}=\{0,2\},\,S_{l(1)}=\{1,3\}`); vacuous for `n\le2`.
  For `n\ge3`: `b_1-b_2>t_1-t_2/2=3\cdot2^{n-3}\ge3\ge1=t_n$ using `w\ge0`
  to drop the `+w` term (only weakening the bound) and the same
  computation as the `(1,0)` case.

Every case gives `D(B)\ge b_1-b_2\ge t_n$ (with two sub-cases vacuous for
small `n`, hence trivially satisfied there), establishing the Main
Theorem for every `n\ge1`, every `K\ge1`, every disjoint cluster
collection, and every choice of minority-range tie values, with **no**
ordering assumption between the clusters' tie values whatsoever.
`\blacksquare`

*Independent verification.* Checked against `16{,}000` randomized
instances as described above (`/tmp/verify_kcluster.py`, function `test`):
`D(B)\ge t_n` held in every single trial across `n=1,\ldots,8`, random
`K` (0 up to `\lfloor(n+1)/2\rfloor`), random cluster sizes and minority
`v_l` values — zero violations.

## Why this is stronger than the round-10 outline's planned mechanism

The outline's original plan required peeling thresholds in decreasing
order `v_1>v_2>\cdots>v_K` and an induction on `K` via a "multi-pair
insertion" lemma inserting companions largest-first. That plan is
**superseded**, not needed: Lemma TOP2 is a single, hypothesis-free
2-line fact (no threshold, no `Y/Z` split, no parity distinction, no
ordering on the `v_l`'s), so the entire "K clusters" problem collapses to
**exactly the same 5-case structural analysis** that closed `K=1` — with
the sole new content being the `(1,1)`-different-clusters sub-case
(`l(0)\ne l(1)`), which is handled by the *same* bound
(`v<t_2/2`) used for the `(1,0)$ case, since in both cases the load-bearing
fact is simply "whichever cluster contains index `0` (resp. contains
index `1$ but not `0`) must also contain some *other* index `\ge2`,
forcing its minority value below `t_2/2`" — a fact that holds regardless
of how many *other*, entirely unrelated clusters exist elsewhere in the
configuration. There is genuinely no induction on `K` needed at all: the
number of cases is fixed (five), independent of `K`.

## Scope (what this closes, and what remains)

This closes, **unconditionally, for every `n\ge1` and every `K\ge1`**: any
number of simultaneous, independent tie-clusters, each cluster consisting
of `\ge2` pieces of `A_n` **each split into exactly two parts with the
cluster's tie value playing the minority role in every one of them** — no
relation between different clusters' tie values is required. This is
exactly the round-9-flagged "simultaneous-multiple-tie-cluster case" that
neither `TREE-BOUND-RESIDUAL` nor `TWO-BLOCK` addressed, now closed in
full (subsuming `TWO-BLOCK`'s `K=1` case as the `(\varepsilon_0,
\varepsilon_1)\in\{(0,0),(0,1),(1,0),(1,1)\text{-same-cluster}\}` cases
above, with the `(1,1)$-different-clusters case being the sole genuinely
new content).

Combined with the already-certified facts (Lemma CROSS-TIE-AFFINE's
zero-residue "majority-part or `\ge3`-part" closure, Lemma TREE-BOUND
(anchor-only, any budget), the well-separated single-free-coordinate case
`recursive-embedding-induction`'s Lemma V'-GEN / Lemma FC), this appears
to close gap (b) of Lemma V'-GEN **in full**, for every configuration
where each individual split piece has at most 2 parts (whether one or
many pieces are simultaneously tied, at one or many distinct values).
**Not separately re-verified here** (same honest caveat as round 9's
`TWO-BLOCK` file): a piece split into `\ge3` parts with more than one of
*its own* coordinates independently tied at different values (a
"doubly-tied `\ge3`-part piece") — this is a structurally different
scenario (one piece contributing multiple free/tied coordinates, rather
than one free coordinate per piece across many pieces) and is not covered
by this K-cluster result, which assumes each individual piece contributes
at most one free/tied coordinate (i.e. is split into at most 2 parts, or
is left fully untouched). Whether a genuine vertex of the full
constrained polytope can ever exhibit such a "doubly-tied" piece at all
(as opposed to this being ruled out entirely by the per-piece LP-vertex
property underlying Lemma V'/V'-GEN) is a question for the sibling
approach's machinery, not re-derived here.

## Status

**Certified.** Lemma TOP2 (fully general, hypothesis-free) and the
Structural Lemma (general-`K` two-largest-element identification) are
proved in full above and independently verified computationally
(`16{,}000` trials, zero violations/mismatches, see inline notes and
`/tmp/verify_kcluster.py`). The Main Theorem is proved in full for every
`n\ge1`, every `K\ge1`, every disjoint cluster collection with minority-role
ties, and every choice of tie values (no ordering assumption) — closing
the round-9-flagged multi-cluster generalization of gap (b) for the "every
split piece has exactly 2 parts" scope. The "doubly-tied `\ge3`-part
piece" edge (a narrower, structurally distinct concern already flagged as
open in round 9, not multi-cluster in this sense) remains a separate,
un-closed loose end.
