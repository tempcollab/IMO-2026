# Lemma TREE-BOUND (round 8, `recursive-embedding-induction`)

**Closes gap (a)** of round 7's Lemma PARITY-PAIR-GEN plan (the
partial-budget anchor-only sub-case), and in fact proves something
strictly stronger: the anchor-only sub-case is closed **unconditionally,
for every mark budget whatsoever, including unlimited budget** — the mark
cap `b ≤ n` is never needed.

## Setting

Fix `n ≥ 1`, normalized units `t_i := 2^{n-i}` (`i=1,...,n`, so
`t_1=2^{n-1} > ... > t_n=1`), `P_1` = Liu's top piece with value `2t_1=2^n`,
and tail pieces `T_1,...,T_n` with `T_i = t_i`.

**Fact 0 (forced halving).** No two *distinct* powers of `2` sum to a power
of `2` (their binary representations have two `1`-bits, a power of `2` has
one). Hence the *only* way to split a piece of value `2^e` into two pieces
whose values are again both powers of `2` is the exact halving
`2^e → 2^{e-1}, 2^{e-1}`. Consequently, any **anchor-only** strategy (every
final piece value lies in `{t_1,...,t_n} = \{2^{n-1},...,2^0\}`) is exactly
described by independent **binary subdivision trees**: `P_1`'s tree is
rooted at value `2^n` (exponent `n`, not itself an anchor since anchors
only go up to `t_1=2^{n-1}`, so it is **forced** to split at least once —
matching Fact 1 of `lemmas/parity-pair-anchor.md`), and each `T_i`'s tree
is rooted at value `t_i=2^{n-i}` (already an anchor, so it may remain a
single leaf or split further, freely). Every leaf value is `2^e` for some
`0 ≤ e ≤ n-1`, i.e. some `t_{n-e}`; a leaf at exponent `0` (value `t_n=1`)
cannot split further while remaining anchor-exact (Fact 2 of
`lemmas/parity-pair-anchor.md`). Each split costs exactly one mark, so a
tree of `L` leaves uses exactly `L-1` marks, and using budget `≤ n` total
restricts this forest to a **subset** of all possible such trees.

**Definition (`D` of a forest).** Given any choice of `P_1`'s tree and each
`T_i`'s tree, the merged multiset `B` of all leaves — sorted descending —
is exactly the ordinary quantity `D(B) = Σ (-1)^{rank+1}(\text{value})`
already used throughout this problem (Lemma D-REFORM).

## Lemma TREE-BOUND

**Statement.** For every `n ≥ 1` and every choice of an anchor-only forest
(`P_1`'s tree, forced non-leaf at the root, and `T_1,...,T_n`'s trees, each
arbitrary — **no bound whatsoever on the number of marks used**), the
merged leaf multiset `B` satisfies `D(B) ≥ t_n = 1`.

In particular this covers every anchor-only strategy reachable within
Xiang Yu's actual budget `b ≤ n` (full or partial), closing the gap left
open by `lemmas/parity-pair-anchor.md`.

### Reduction to a general "forest" sub-lemma

Peel `P_1`'s forced root split: it must split into two level-`(n-1)`
children `L, R` (value `t_1` each, by Fact 0). This turns the whole
problem into: three independent trees rooted at value `t_1` (`L`, `R`,
and `T_1`), together with `T_2,...,T_n` (rooted at `t_2,...,t_n`).

**Definition (`(m,r)`-forest).** For integers `m ≥ 1`, `r ≥ 0`, an
`(m,r)`-forest is a choice of `r` independent trees rooted at value
`τ_1 := 2^{m-1}`, together with one tree each rooted at
`τ_2 := 2^{m-2}, τ_3, \ldots, τ_m := 2^0=1` (present only when `m ≥ 2`;
for `m=1` there is no further level, just the `r` trees rooted at
`τ_1=τ_m=1`). Write `D(m,r)` for the set of possible `D`-values of such a
forest's merged leaves (against the local anchor sequence
`τ_1 > \cdots > τ_m`).

Peeling `P_1` turns the original problem exactly into an `(n,3)`-forest
(with `m=n`, `τ_i = t_i`) for `n ≥ 2`; the case `n=1` is handled directly
below since `P_1`'s children at `n=1` are themselves already at the bottom
level (exponent `0`) and there is no room to peel further.

### Sub-lemma ODD

**Statement.** For every `m ≥ 1` and every **odd** `r ≥ 1`, every
`(m,r)`-forest satisfies `D ≥ τ_m = 1`.

*Proof, by strong induction on `m`.*

**Base case `m=1`.** Here `τ_1 = τ_m = 1`, and each of the `r` trees is
rooted at exponent `0`, hence (Fact 2 style reasoning: exponent `0` cannot
split anchor-exactly) is forced to be a single leaf of value `1`. So `B`
is exactly `r` copies of `1`; since `r` is odd, `D(B) = 1 - 1 + 1 - \cdots
+ 1 = 1 = τ_m` (an alternating sum of an odd number of equal terms equals
that term — direct computation, pairing consecutive `+1,-1` terms which
cancel, leaving one unpaired `+1`). So `D = τ_m` exactly. ✓

**Inductive step, `m ≥ 2`, `r` odd.** Among the `r` top-level (`τ_1`)
trees, let `k` (`0 ≤ k ≤ r`) be the number that remain single leaves (the
other `r-k` split into two `τ_2`-valued children each). The `k` leaves of
value `τ_1` occupy consecutive top ranks `1,\ldots,k` of the sorted merged
list `B` (they are the unique maximum value present, since every other
leaf — from a split top-tree, or from any lower-level tree — has value
`≤ τ_2 < τ_1`). By the single-block alternating-sum fact (already
established and certified in `lemmas/alternating-sum-toolkit.md`'s
derivation of the `(BLOCK)` formula): a run of `k` consecutive equal
values starting at rank `1` contributes `τ_1` to `D` if `k` is odd, and
contributes `0` to `D` (while leaving every element ranked below it with
its sign **unchanged**, since the run's length `k` is even) if `k` is
even.

The remainder of the list (everything below rank `k`) is exactly the
merged leaves of: the `2(r-k)` new `τ_2`-valued children (from the split
top trees) together with the fixed trees rooted at `τ_2,\ldots,τ_m`
(i.e. `T_2`'s-type tree at `τ_2`, plus the standing trees at
`τ_3,\ldots,τ_m`) — this is *exactly* an `(m-1, r')`-forest, re-indexed so
that `τ_2,\ldots,τ_m` play the role of the new top-through-bottom anchors
`τ'_1=τ_2,\ldots,τ'_{m-1}=τ_m`, with
$$r' := 2(r-k) + 1,$$
the `+1` accounting for the one standard tree originally rooted at `τ_2`
(previously called `Θ_2`/`T_2`) which is *always* present in addition to
the `2(r-k)` new children. **Crucially, `r' = 2(r-k)+1` is always odd,
regardless of the parities of `r` and `k`** — this is the key structural
fact that makes the reachability constraint (unlike the abstract
`(c_1,\ldots,c_n)`-vector formalism) automatically self-correcting: every
genuine tree-split produces children in pairs, so the remainder always
inherits an odd top-level multiplicity.

- **Case `k` even.** Block-1 contributes `0`, and by the "shift by an
  even amount preserves sign" fact, `D(B) = D(\text{remainder})`, where
  the remainder is an `(m-1,r')`-forest with `r'` odd, `r' ≥ 1`. Since
  `1 ≤ m-1 < m`, the induction hypothesis (Sub-lemma ODD at level `m-1`)
  applies: `D(\text{remainder}) ≥ τ'_{m-1} = τ_m` (using
  `τ'_{m-1} = 2^{(m-1)-(m-1)} = 2^0 = 1 = τ_m`). Hence `D(B) ≥ τ_m`. ✓
- **Case `k` odd.** Block-1 contributes `+τ_1`, and the remainder's sign
  is **flipped**: `D(B) = τ_1 - D(\text{remainder})`, where the remainder
  is again an `(m-1,r')`-forest (this time we do **not** need `r'`'s
  parity — the bound below is unconditional). The remainder's leaves are
  nonempty (the standard tree rooted at `τ_2` alone always contributes at
  least one leaf) and all have value `≤ τ_2` (every remainder leaf has
  exponent `≤ m-2`). By the certified **Lemma D-BOUND**
  (`lemmas/alternating-sum-toolkit.md`, `0 ≤ D(Y) ≤ \max(Y)` for any
  finite sorted nonnegative list `Y`), `0 ≤ D(\text{remainder}) ≤ τ_2`.
  Hence
  $$D(B) = τ_1 - D(\text{remainder}) ≥ τ_1 - τ_2.$$
  Since `τ_1 = 2^{m-1} = 2·2^{m-2} = 2τ_2`, `τ_1-τ_2 = τ_2 = 2^{m-2}`.
  Since `m ≥ 2`, `m-2 ≥ 0`, so `τ_2 = 2^{m-2} ≥ 2^0 = τ_m`. Hence
  `D(B) ≥ τ_2 ≥ τ_m`. ✓

Both cases give `D(B) ≥ τ_m`, completing the induction on `m`.
`\blacksquare`

*(Independently verified: exhaustive — not sampled — enumeration in Python
of every `(m,r)`-forest's leaf-exponent multiset and its exact integer `D`
value, for `m=1,2,3,4` and `r=1,3,5` (up to `175{,}760` distinct tree-shape
combinations at `m=4,r=3`): the minimum `D` found is exactly `1=τ_m` in
**every** case, matching the proof's prediction with zero violations.)*

### Proof of Lemma TREE-BOUND from Sub-lemma ODD

- **`n=1`.** `P_1` (value `2`) is forced to split into two leaves of value
  `1` (exponent `0`, the only option by Fact 0); `T_1` (value `t_1=1`) is
  itself already at exponent `0`, hence forced to be a single leaf.
  Merged `B = \{1,1,1\}`, `D(B) = 1-1+1 = 1 = t_n`. ✓ (This is also the
  `m=1,r=3`... actually directly the `m=1` base case of Sub-lemma ODD with
  `r=3`, since two children of `P_1` plus `T_1` are exactly three trees
  rooted at exponent `0` when `n=1`; consistent either way.)
- **`n ≥ 2`.** As shown above, peeling `P_1`'s forced root split turns the
  whole configuration into exactly an `(n,3)`-forest (`m=n`, `r=3`, odd).
  By Sub-lemma ODD, `D(B) ≥ τ_n = t_n = 1`. ✓

`\blacksquare`

### Consequence for `lemmas/parity-pair-anchor.md`'s open gap

Every anchor-only strategy reachable by Xiang Yu with any budget `b`
(`0 ≤ b ≤ n`, or indeed **any** `b` at all) is, by Fact 0, some instance of
the forest described above. Lemma TREE-BOUND shows `D(B) ≥ t_n` for
**every** such instance, unconditionally — in particular for every
`b < n` (the partial-budget case, both `M`-parities), closing the gap left
open by `lemmas/parity-pair-anchor.md`'s Theorem (which only handled
`b = n`, i.e. `M` automatically odd). The abstract counterexample
`c=(0,4)` at `n=2` cited there is (as already diagnosed) simply not
tree-reachable at all — Lemma TREE-BOUND explains *why* in full generality
(such a vector would require `P_1`'s subtree alone to reach `4` copies of
`t_2` with **zero** copies of `t_1`, forcing `k=0` at the top level, whose
remainder is an `(n-1,2r_{\text{sub}}+1)`-type object that, when correctly
accounted with `T_1`'s own mandatory contribution, cannot produce the
claimed vector — consistent with, and now subsumed by, the general
inductive bound above, which holds regardless of which specific vector
results).

**No monotonicity principle is needed**: Lemma TREE-BOUND proves the bound
directly for every reachable configuration, without going through any
"more marks can only help" argument (the round-7 file's "extension
monotonicity" conjecture, correctly flagged there as unnecessary and
possibly false in general form, is neither needed nor used here).
