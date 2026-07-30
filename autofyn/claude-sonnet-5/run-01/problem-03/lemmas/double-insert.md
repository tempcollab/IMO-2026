# Lemma DOUBLE-INSERT (certified, round 7)

Source: `universal-adversary-strategy.md`, round 7, discovered while
attempting the retargeted matching/assignment induction (Task 3 of this
round's assignment). **Strictly generalizes the certified Lemma HALVE**
(`lemmas/generalized-domination-and-halving.md`) by removing its domination
hypothesis (`p_1\ge2p_2`) entirely — the identity holds unconditionally.
Independently verified by exact-`Fraction` computation: `2,000` random
trials (list sizes `0`–`6`, arbitrary positive rational values, arbitrary
relative position of the inserted value), **zero mismatches**.

## Statement

Let `T=(t_1\ge t_2\ge\cdots\ge t_\ell)` be **any** sorted list of positive
reals (`\ell\ge0`, `T=\emptyset` allowed), and let `v>0` be any value.
Write `B := \{v,v\}\cup T` (merge and re-sort, size `\ell+2`). Then,
**with no hypothesis relating `v` to `T` at all**:
```
oddrank(B) = oddrank(T) + v.
```

## Proof

Let `j := \#\{i : t_i \ge v\}` (`0\le j\le\ell`), so `T`'s sorted order
splits as `t_1,\ldots,t_j$ (all `\ge v`) followed by `t_{j+1},\ldots,t_\ell`
(all `<v`, up to ties, which do not affect the sum). The sorted order of
`B` is then
```
t_1,\ldots,t_j,\;v,\;v,\;t_{j+1},\ldots,t_\ell.
```
- **Ranks `1,\ldots,j`** (the elements `t_1,\ldots,t_j`): unchanged from
  their ranks in `T` alone (same values, same positions), so this block
  contributes exactly `\sum_{i\le j,\,i\text{ odd}} t_i` to `oddrank(B)` —
  identical to its contribution to `oddrank(T)`.
- **Ranks `j+1,j+2`** (the two copies of `v`): exactly one of these two
  consecutive ranks is odd. Since the two copies are numerically identical,
  the contribution to `oddrank(B)` is exactly `v`, regardless of which
  physical copy sits at the odd rank (the same "duplicate-pair tie"
  observation used in Lemma DOM's and Lemma HALVE's proofs — the value
  does not depend on breaking the tie one way or the other).
- **Ranks `j+3,\ldots,j+2+(\ell-j)`** (the elements `t_{j+1},\ldots,t_\ell`):
  each such element had original rank `i\in\{j+1,\ldots,\ell\}$ in `T`
  alone, and now sits at global rank `i+2` in `B`. Since `2` is **even**,
  the parity of `i+2` equals the parity of `i`, so this block contributes
  exactly `\sum_{i>j,\,i\text{ odd}} t_i` to `oddrank(B)` — again identical
  to its contribution to `oddrank(T)`.

Summing all three contributions:
```
oddrank(B) = \sum_{i\le j,\text{ odd}}t_i \;+\; v \;+\;
\sum_{i>j,\text{ odd}}t_i = oddrank(T) + v.
```
This holds for **every** value of `j\in\{0,\ldots,\ell\}`, i.e.
unconditionally on where `v` falls relative to `T` — no domination or
ordering hypothesis of any kind is needed, because the two inserted copies
are always mutually adjacent (being numerically equal) regardless of their
absolute position, and the shift they impose on everything below them is
always by the even number `2`. ∎

## Why this is new content, not a restatement of Lemma HALVE

Lemma HALVE's proof (and Lemma SPLIT's general `i`-th-position version)
both require a domination-style hypothesis (`p_1\ge2p_2$, resp.
`a_i/2\ge a_{i+1}`) specifically to pin down that the two new pieces stay
mutually adjacent **at the very top** of the sorted order (occupying ranks
`1,2`, or `i,i+1`). Lemma DOUBLE-INSERT shows that hypothesis was never
actually load-bearing for the *value formula* itself when the two new
pieces are **exactly equal**: two equal copies are automatically mutually
adjacent in sorted order *wherever they land*, because a value can never be
strictly between itself and its own copy. This is the precise reason equal
splits enjoy an unconditional identity that Lemma SPLIT's general (unequal)
splits do not — Lemma SPLIT's hypothesis is only needed to control *where*
an unequal fragment lands relative to a *specific* neighbor, which matters
because unequal fragments are not automatically mutually adjacent to each
other.

**Corollary (Lemma HALVE re-derived, hypothesis-free).** Taking `T` to be
the tail `(p_2,\ldots,p_m)$ of `A=(p_1\ge\cdots\ge p_m)` (or any further
refinement `T'` of it) and `v=p_1/2`, Lemma DOUBLE-INSERT gives
`oddrank(\{p_1/2,p_1/2\}\cup T') = oddrank(T') + p_1/2` for **every** `A`
— with no domination hypothesis `p_1\ge2p_2` required. Lemma HALVE
(certified, `lemmas/generalized-domination-and-halving.md`) is exactly the
special case where domination additionally happens to hold (in which case
the two halves are guaranteed to occupy the very top two ranks); Lemma
DOUBLE-INSERT shows the *value* is the same regardless, only the *sorted
position* of the pair differs.

## Numeric verification

`2{,}000` random exact-`Fraction` trials, list sizes `\ell\in\{0,\ldots,6\}`,
arbitrary positive rational values for both `T`'s entries and `v` (drawn
independently, so `v` lands at every possible relative position across
trials, including strictly interior, strictly above, strictly below, and
exactly tied with an element of `T`): **zero mismatches** against the
closed form `oddrank(T)+v`.

## Status

Certified (round 7). Fully proved by a direct, general rank-shift argument
(the proof above), no hypothesis needed, no reliance on any other lemma.
Strictly generalizes the certified Lemma HALVE. Independently verified
exactly (`Fraction` arithmetic, `2,000` trials, zero mismatches).
