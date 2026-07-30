# Lemma TREE-BOUND-MULTICLUSTER (round 10, `recursive-embedding-induction`)

**Closes the last remaining sub-gap of the lower bound**: the case of
**arbitrarily many (`K≥2`) simultaneous, independent tie-clusters/impurities**
in the forest, generalizing the certified **Lemma TREE-BOUND-RESIDUAL**
(`lemmas/tree-bound-residual.md`, which only allowed **at most one** impure
node in the whole forest) to **any finite number of impurities, distributed
anywhere in the forest, including several landing simultaneously at the same
top level of the same recursive pass** — the one configuration the
single-impurity induction hypothesis could never reach. Uses only the
already-certified **Lemma D-BOUND** and elementary telescoping arithmetic on
the geometric anchors; no new atomic machinery beyond one short, self-
contained "adjacent-equal-pair-cancellation" fact proved from scratch below.

## Setting

Same normalization as `lemmas/tree-bound-anchor.md` / `tree-bound-residual.md`:
`τ_1>τ_2>\cdots>τ_m` with `τ_l=2^{m-l}`. An `(m,r)`-forest is `r` independent
trees rooted at `τ_1` plus one standard tree at each of `τ_2,\ldots,τ_m`.

**Definition (impure node, unchanged).** A node of current value `τ_i` may,
instead of staying a leaf or splitting purely, undergo one **impure cut**:
it terminates immediately into two leaves `y:=τ_j`, `c:=τ_i-τ_j`, for some
`j>i`.

**Definition (`(m,r)`-forest with arbitrarily many impurities).** An
`(m,r)`-forest in which **any finite number** of nodes, anywhere in the whole
structure (any of the `r` top trees, any of the `m-1` standard trees, at any
depth), may independently be impure; every other node is pure. (No bound on
the total count, and — the genuinely new content — no restriction on how many
of them may coincide at the current top level of any one recursive pass.)

## Lemma TREE-BOUND-MULTICLUSTER

**Statement.** For every `m≥1`, every odd `r≥1`, and every `(m,r)`-forest with
arbitrarily many impurities distributed arbitrarily, the merged leaf multiset
`B` satisfies `D(B)≥τ_m`.

*Proof, by strong induction on `m`.*

**Base case `m=1`.** No node in the forest has value `2^e` with `e≥1` (every
tree is already at exponent `0`), so no impure cut is possible anywhere: the
forest is automatically fully pure, identical to the original base case.
`D(B)=τ_m` exactly (odd `r` copies of `τ_1=τ_m=1`).

**Inductive step, `m≥2`, `r` odd.** Among the `r` top-level (`τ_1`) trees, let
`k≥0` be the number that are pure leaves, `p≥0` the number that are
**themselves** impure (cut short right at the root of that top-level tree,
at some depth `j∈\{2,\ldots,m\}`), and `r-k-p` the number that split purely
into two `τ_2`-valued children — each of these children, and each of the
standard trees at `τ_2,\ldots,τ_m`, may independently harbor **any number of
further impurities at any depth below**, with no restriction whatsoever.

**The key structural point.** Let
$$X:=\bigl[\,2(r-k-p)\text{ copies-worth of the purely-split children's own
merged leaves}\,\bigr]\ \cup\ \bigl[\text{the standard trees at }
τ_2,\ldots,τ_m\bigr].$$
By construction every leaf of `X` has value `≤τ_2` (each of its constituent
trees is rooted at a value `≤τ_2`, and every leaf of a subtree is at most its
root's value, pure or impure). `X` is exactly an `(m-1,r'')`-forest with
$$r''=2(r-k-p)+1$$
(the `+1` for the standing `τ_2`-tree, always odd regardless of the parities
of `r,k,p` — the same forced-parity fact from `lemmas/tree-bound-anchor.md`)
carrying **its own arbitrary distribution of arbitrarily many impurities**
anywhere inside it. This is *exactly* an instance of the statement being
proved, one level down (`m-1<m`), so **the strong induction hypothesis
applies directly and unconditionally**:
$$D(X)\ \ge\ τ_m,$$
**regardless of how many impurities `X` contains or where they sit** — this
is the mechanism that lets deeper/"distributed" impurities (not at the
current top level) be handled with zero extra work at every level of
peeling, closing the "impurities in disjoint subtrees" branch identified by
this round's explorer report.

It remains to control the contribution of the `p` top-level impurities
(paired leaves `\{y_i,c_i\}_{i=1}^p`, `y_i=τ_{j_i}`, `c_i=τ_1-τ_{j_i}`,
`2\le j_i\le m`) and the `k` top-level leaves, on top of `X`. This is the
genuinely new content (the case `p=0` is the already-certified Lemma
TREE-BOUND; `p=1` is the already-certified Lemma TREE-BOUND-RESIDUAL's
Case C; general `p\ge2` is proved here).

### Step 1 — two exact, cost-free reductions on the `p` impurities

**Reduction R1 (eliminate `j=2` impurities).** If `j_i=2`, the impure cut
produces leaves `\{τ_2,\,τ_1-τ_2\}=\{τ_2,τ_2\}` — **exactly the two leaves a
genuine pure split of that same top-level tree would have produced.** Hence
an impurity at `j=2` is literally indistinguishable, as a multiset of
produced leaves, from a pure split; reclassify every such impurity as a pure
split (moving it from "the `p` impure trees" to "the `r-k-p` purely-split
trees" — this changes neither `B` nor any quantity computed from `B`). **WLOG
every remaining genuine impurity has depth `j_i\ge3`.**　If this reclassifi-
cation reduces `p` to `0`, skip directly to Step 3's `p=0` case below.

**Reduction R2 (pairwise cancellation of tied depths).** Group the remaining
impurities by depth: for each `j\in\{3,\ldots,m\}` let `n_j\ge0` be the number
of impurities at that exact depth (so `\sum_j n_j = p` after R1). If any
`n_j\ge2`, remove two of them at once (i.e. delete two copies of `y=τ_j` and
two copies of `c=τ_1-τ_j` from the merged multiset `B`) — repeat until every
`n_j\in\{0,1\}$. This is justified by:

> **Fact PAIR-CANCEL (adjacent equal pair removal).** *If a sorted list
> `Z=(z_1\ge\cdots\ge z_N)` has two adjacent equal entries `z_i=z_{i+1}=v`,
> then `D(Z) = D(Z')` where `Z'` is `Z` with both copies deleted.*
>
> *Proof.* Direct from the definition:
> $$D(Z)=\sum_{l<i}(-1)^{l+1}z_l\;+\;(-1)^{i+1}v+(-1)^{i+2}v\;+\;\sum_{l>i+1}(-1)^{l+1}z_l
> =\sum_{l<i}(-1)^{l+1}z_l+0+\sum_{l>i+1}(-1)^{l+1}z_l$$
> (the two middle terms are `+v-v=0`). Deleting positions `i,i+1` shifts every
> later term's position down by exactly `2`, which **preserves its sign**
> `(-1)^{l+1}=(-1)^{(l-2)+1}`; so
> $$D(Z')=\sum_{l<i}(-1)^{l+1}z_l+\sum_{l>i+1}(-1)^{(l-2)+1}z_l=\sum_{l<i}(-1)^{l+1}z_l+\sum_{l>i+1}(-1)^{l+1}z_l=D(Z).\ \blacksquare$$

Since all `y_i=τ_j` (`j` fixed) are mutually equal and, being `\le τ_2\le`
every companion `c$, occupy consecutive adjacent ranks among themselves
whenever there are `\ge2` of them at the same depth (ties only ever occur
*within* a single depth's group, since distinct depths give strictly
different — hence strictly ordered — `y`- and `c`-values, by
`τ$ strictly decreasing); likewise all `c_i=τ_1-τ_j` (same `j`) are mutually
equal and adjacent. So Fact PAIR-CANCEL applies to each such pair, both for
the `y`'s and (separately) for the `c`'s, and removing them changes `D(B)`
by exactly `0`. Iterating, `D(B)` is **unchanged** by reducing every `n_j` to
`n_j\bmod 2\in\{0,1\}$.

**Conclusion of Step 1.** `D(B)` equals `D` of the configuration with the `p`
impurities replaced by `p'\le p` impurities at **pairwise distinct** depths
`3\le j_1<j_2<\cdots<j_{p'}\le m$ (possibly `p'=0`).

### Step 2 — telescoping bound on the distinct-depth companion block

Write `c_l:=τ_1-τ_{j_l}` for `l=1,\ldots,p'$ ($c_1<c_2<\cdots<c_{p'}$, since
`c` is strictly increasing in `j`); sorted descending, the companions are
`c_{(1)}=c_{p'}\ge c_{(2)}=c_{p'-1}\ge\cdots\ge c_{(p')}=c_1$. Let
`A_{p'}:=\sum_{i=1}^{p'}(-1)^{i+1}c_{(i)}$ (the alternating sum of the sorted
companion block alone). Using the telescoping anchor identity
`τ_1-τ_j=τ_2+τ_3+\cdots+τ_j` (immediate from `τ_i=2τ_{i+1}$ summed as a
geometric series):

- **`p'` odd (`p'\ge1`).** Pairing `(c_{(1)},c_{(2)}),(c_{(3)},c_{(4)}),\ldots`
  leaves the single unpaired term `c_{(p')}=c_1` with a `+` sign, and every
  paired difference `c_{(2t-1)}-c_{(2t)}\ge0$ (consecutive differences of an
  increasing sequence), so
  $$A_{p'}\ \ge\ c_{(p')}\ =\ c_1\ =\ τ_1-τ_{j_1}\ =\ τ_2+τ_3+\cdots+τ_{j_1}
  \ \ge\ τ_2+τ_{j_1}$$
  (the sum has `\ge2$ terms since `j_1\ge3$, so it dominates its first term
  `τ_2$ plus its last term `τ_{j_1}$, all terms being nonnegative). Since
  `j_1\le m`, `τ_{j_1}\ge τ_m`, so `A_{p'}\ge τ_2+τ_m`.
- **`p'` even (`p'\ge2`).** Pairing the same way, every term is
  `\ge0`, so `A_{p'}\ge$ (any single pair's contribution). Take the pair
  `(c_{(1)},c_{(2)})=(c_{p'},c_{p'-1})$: its difference is
  $$c_{p'}-c_{p'-1}\ =\ τ_1-τ_{j_{p'}}-\bigl(τ_1-τ_{j_{p'-1}}\bigr)\ =\ τ_{j_{p'-1}}-τ_{j_{p'}}
  \ =\ τ_{j_{p'-1}+1}+\cdots+τ_{j_{p'}}\ \ge\ τ_{j_{p'}}\ \ge\ τ_m$$
  (telescoping identity again, using `j_{p'-1}<j_{p'}$, and the last/smallest
  term of the sum is `τ_{j_{p'}}$). So `A_{p'}\ge τ_m` (dropping all other
  nonnegative pairs).
- **`p'=0`.** `A_0=0` (empty sum, vacuously).

### Step 3 — assembling the bound

Let `Y:=X\cup\{y_1,\ldots,y_{p'}\}` (all elements `\le τ_2$, since `X`'s
elements are `\le τ_2$ and each `y_l=τ_{j_l}\le τ_3<τ_2$). By the certified
**Lemma D-BOUND**, `0\le D(Y)\le τ_2`. Inserting the `p'` companions on top of
`Y` one at a time, each as the current maximum (valid since every companion
`c_l\ge τ_2\ge$ every element of `Y$, by `j_l\ge3\Rightarrow c_l\ge τ_2+τ_{j_l}>τ_2$
— strictly, but `\ge$ suffices), gives the exact identity
$$D(X\cup\{y_i,c_i\}_{i=1}^{p'}) = A_{p'} + (-1)^{p'}D(Y)$$
(the same telescoping computation used in Lemma TREE-BOUND-RESIDUAL's Case C,
now for a general block of `p'` companions instead of one).

Now combine with the `k` top-level leaves of value `τ_1` exactly as in
Lemma TREE-BOUND-RESIDUAL: write `R:=X\cup\{y_i,c_i\}_{i=1}^{p'}$ (so
`B = [k\text{ copies }τ_1]\cup R`), and recall the standard block fact:
`k` even `\Rightarrow D(B)=D(R)`; `k` odd `\Rightarrow D(B)=τ_1-D(R)`.

- **`k` odd** (any `p'\ge0$, in fact this sub-case needs **neither** Step 1
  nor Step 2 — it is robust to ties and even `p=0$ before reduction):
  every element of `R=X\cup\{y_i,c_i\}` is `\le\max_i c_i` (shown above, `X`'s
  and each `y_i`'s value are both `\le τ_2\le$ every `c_i`), so by Lemma
  D-BOUND, `0\le D(R)\le\max_i c_i = τ_1-\min_i τ_{j_i} = τ_1-τ_{j_{\max}}`
  where `j_{\max}:=\max_i j_i$ (the deepest impurity present, `p=0` giving the
  vacuous `\max_i c_i=τ_2$ by convention, consistent with the original `p=0`
  case). Hence
  $$D(B)=τ_1-D(R)\ \ge\ τ_1-(τ_1-τ_{j_{\max}})\ =\ τ_{j_{\max}}\ \ge\ τ_m$$
  (`j_{\max}\le m` always). ✓ — this bound requires no distinctness, no
  reclassification, works for the raw `p` before any reduction.
- **`k` even, `p'=0`** (after R1/R2 possibly collapse all impurities away, or
  there simply were none): `D(B)=D(R)=D(X)\ge τ_m` **directly from the strong
  induction hypothesis** (Step 0 above). ✓
- **`k` even, `p'` odd (`\ge1`)**: `D(B)=D(R)=A_{p'}-D(Y)`. By Step 2,
  `A_{p'}\ge τ_2+τ_m`; by D-BOUND, `D(Y)\le τ_2`. Hence
  $$D(B)\ \ge\ (τ_2+τ_m)-τ_2\ =\ τ_m.\ ✓$$
- **`k` even, `p'` even (`\ge2`)**: `D(B)=D(R)=A_{p'}+D(Y)`. By Step 2,
  `A_{p'}\ge τ_m$; by D-BOUND, `D(Y)\ge0`. Hence
  $$D(B)\ \ge\ τ_m+0\ =\ τ_m.\ ✓$$

Every case gives `D(B)\ge τ_m$, completing the inductive step, hence the
induction on `m`. `\blacksquare`

### Consequence for the original problem

Peeling `P_1`'s forced root split turns the `n\ge2` case into an
`(n,3)`-forest exactly as in `lemmas/tree-bound-anchor.md`; **any finite
number of impurities, distributed anywhere in the forest including several
landing simultaneously at the same top level of the same recursive pass**,
are carried through this peeling into the resulting `(n,3)`-forest, to which
the Lemma above applies directly (`r=3` odd): `D(B)\ge t_n=1` for **every**
configuration in which Xiang Yu splits some pieces into anchor values and
some pieces into one anchor value plus one un-split residual companion —
with **no restriction on how many such residual/tied pieces occur, nor on
whether several of them share the same forest level simultaneously**.

## Independent verification

**Randomized, arbitrary-depth recursive construction** (`/tmp/explore_multi3.py`):
for each of `m=1,\ldots,7` and odd `r\in\{1,3,5,7\}`, generated `2{,}000`
random forests in which **every node, at every depth, independently and
recursively** has a `20\%` chance of being an impure cut to a uniformly
random deeper anchor (so the number and placement of impurities is
unrestricted and typically several land simultaneously at the same level) —
minimum `D` found is exactly `1=τ_m` in all `28` `(m,r)` combinations, zero
violations. **Sanity check (even `r`)**: the same generator with `r=2,4`
produces genuine violations (`D=0<1` at `m=1,r=2`), confirming the test
harness is discriminating and the odd-`r` hypothesis is load-bearing, exactly
as in the `p\le1` lemmas.

**Targeted adversarial probe** (`/tmp/explore_multi.py`,
`/tmp/explore_multi2.py`): `p=2` impurities with **exactly tied** depths
(`j_1=j_2`, the case Reduction R2 exists to neutralize) across
`m=3,\ldots,7`, all tested depths, `300` trials each: minimum `D` found is
exactly `1=τ_m` (matching the R2 mechanism's prediction `D(B)=D(X)\ge τ_m`
exactly, not merely `\ge`). `p=2` with **distinct** depths, `k` of both
parities, `m=4,5,6`, `r\in\{3,5\}`, all `\binom{m-1}{2}$ depth pairs, `150`
trials each: zero violations, matching the Step 2/3 bound.

## What this closes

Combined with the already-certified `lemmas/cross-tie-affine.md` (reduces
every cross-piece tie to the well-separated / self-meeting-point / minority-
residue cases) and `lemmas/tree-bound-anchor.md` (gap (a)), this lemma
**closes gap (b) in full generality**, including the multi-cluster case
flagged as open by the round-9 review and this round's explorer: **every
Xiang-Yu-reachable configuration against the geometric construction `A_n`,
with any number of simultaneous independent tied/residual pieces, satisfies
`D(B)\ge t_n`.** Together with the already-certified well-separated and
anchor-only cases, **Lemma PARITY-PAIR-GEN's lower bound `D(B)\ge t_n` for
every Xiang-Yu-reachable configuration against `A_n` is now fully proved,
unconditionally, for every `n\ge1`, every budget, and every number of
simultaneous tie-clusters.**

## What this does not close

As with every lemma in this approach, this closes only the **lower bound for
the specific geometric configuration `A_n`**. Combined with the
already-certified Lemma 1–4/Proposition 4 (Xiang Yu's exact-equality
response), `A_n`'s value is now fully proved to equal `c(n)` exactly, for
every `n`. This does **not** address the separate "general upper bound over
all Liu Bang configurations" question (`universal-adversary-strategy`'s
scope, not this approach's).

## Status

Proved in full this round (round 10). Strong induction on `m`, generalizing
Sub-lemma ODD / TREE-BOUND-RESIDUAL from "at most one impurity" to
"arbitrarily many, anywhere, including several simultaneous at one level" —
the new content is a two-step exact reduction (R1: reclassify depth-`2`
impurities as pure; R2: cancel pairs of tied-depth impurities via the newly
proved, self-contained Fact PAIR-CANCEL) followed by a telescoping-anchor
bound on the resulting distinct-depth companion block (Step 2), closed by
the same two already-certified tools (Lemma D-BOUND, applied twice per case,
plus the unconditional strong-induction bound on `X`) used throughout this
lemma family. Independently stress-tested: `28` `(m,r)` combinations with
fully unrestricted recursive random impurity placement (`2{,}000` trials
each), zero violations; targeted tied-depth and distinct-depth `p=2` probes,
zero violations; even-`r` sanity check confirms the harness is
discriminating.
