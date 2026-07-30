# Lemma MATCH-TAIL-PAIR (halve all but the two smallest, match those two)

**Status:** proved in full below (round 10, `universal-adversary-strategy`).
Recommend certifying. A second direct corollary of the certified,
hypothesis-free Lemma PAIR-VALUE, complementary to Lemma ALL-BUT-MIN
(`lemmas/all-but-min.md`).

## Statement

Let `A=(p_1\ge\cdots\ge p_m)` be any sorted list of positive reals, `m\ge2`,
`\Sigma:=\Sigma(A)`. Using exactly `m-1` marks — split each of
`p_1,\ldots,p_{m-2}` into two exact halves (`m-2` marks; vacuous if `m=2`),
and split `p_{m-1}` into `(p_m, r:=p_{m-1}-p_m)` (`1` mark; `0` marks if
`r=0`, by the same boundary saving as Lemma DOM-boundary-slack) — the
resulting multiset `B` satisfies, **unconditionally** (no hypothesis
relating `p_{m-1}` and `p_m` beyond sortedness `p_{m-1}\ge p_m`):
```
oddrank(B) = \Sigma/2 + (p_{m-1}-p_m)/2.
```
Consequently, whenever
```
p_{m-1}-p_m \le \Sigma/(2^m-1),
```
this construction gives `oddrank(B)\le c(m-1)\Sigma`.

## Proof

`B` decomposes as `m-2` tied pairs `\{p_i/2,p_i/2\}` (`i=1,\ldots,m-2`) plus
one further tied pair `\{p_m,p_m\}` (the copy of `p_m` split from `p_{m-1}`,
matched to the original `p_m`) plus the single unpaired residual `U=\{r\}`.
By Lemma PAIR-VALUE (no domination/contiguity hypothesis needed for any of
these `m-1` pairs, regardless of how the residual `r` interleaves with them
in sorted order):
```
oddrank(B) = \sum_{i=1}^{m-2}\frac{p_i}{2} + p_m + r
= \frac{\Sigma-p_{m-1}-p_m}{2} + p_m + (p_{m-1}-p_m)
= \frac{\Sigma}{2} - \frac{p_{m-1}}{2} - \frac{p_m}{2} + p_{m-1}
= \frac{\Sigma}{2} + \frac{p_{m-1}-p_m}{2}.
```
Total marks: `(m-2)+1=m-1` (or `m-2` if `r=0`, comfortably within budget).
The threshold `p_{m-1}-p_m\le\Sigma/(2^m-1)` follows from the same identity
`2c(m-1)-1=1/(2^m-1)` used in Lemma ALL-BUT-MIN. `∎`

## Relationship to Lemma ALL-BUT-MIN, and to the `m=2` boundary case

For `m=2` (`m-2=0`), this reduces to: match `p_1` to `p_2` (or do nothing
if `r=0`), giving `oddrank(B)=\Sigma/2+(p_1-p_2)/2=p_1` — exactly the
"do nothing" baseline of the already-closed `n=1` result, consistent (not
new content at `m=2`; the construction's genuine new content starts at
`m\ge3`, where it provides a second, complementary threshold to Lemma
ALL-BUT-MIN's `p_m\le\Sigma/(2^m-1)`).

**Neither lemma dominates the other in general**: ALL-BUT-MIN needs the
single smallest element small in absolute terms; MATCH-TAIL-PAIR needs the
two smallest elements close to each other in absolute terms (regardless of
their common size). A configuration can fail both simultaneously — e.g. a
near-uniform `5`-element configuration with all `p_i\approx\Sigma/5`: no
`p_i` is small in the ALL-BUT-MIN sense, and no two of the smallest are
close enough in the MATCH-TAIL-PAIR sense once perturbed unevenly (concrete
witness recorded in `approaches/universal-adversary-strategy.md`, round
10). So the combination of these two lemmas, while a genuine strict
extension of the certified menu, does **not** close Claim PTBI's Case C in
general for `m\ge5`; see that file for the precise remaining gap.

## Independent numerical verification

Checked exactly (`fractions.Fraction`) on 2,000+ random configurations,
`m=2,\ldots,8`: the identity holds exactly in every trial, and the min of
this construction and Lemma ALL-BUT-MIN was checked against `c(m-1)\Sigma`
on 19,133 random Case-C (`p_1<\Sigma/2`) configurations, `m=4,\ldots,8`:
succeeds in the overwhelming majority but a concrete violation was found at
`m=5` (near-uniform configuration, gap `\approx0.036`; recorded exactly in
`approaches/universal-adversary-strategy.md`), confirming the two lemmas
together are a genuine but **incomplete** extension of the certified menu.
