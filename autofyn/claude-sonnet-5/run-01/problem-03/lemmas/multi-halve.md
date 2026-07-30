# Lemma MULTI-HALVE (certified, round 7)

Source: `universal-adversary-strategy.md`, round 7, certifying a construction
found by the round-7 `math-explorer-menucoverage` report ("cascade/multi-HALVE").
Strictly generalizes the already-certified **Lemma HALVE**
(`lemmas/generalized-domination-and-halving.md`), which is the special case
`K=1`. Proved directly (same rank-shift technique as Lemma HALVE/DOM/SPLIT),
not merely numerically — verified exactly against the round-7 explorer's
worked witness `A=(0.583,0.3461,0.0709)`, `K=2`: exact-`Fraction` computation
reproduces `oddrank(B)=10709/20000=0.53545` both directly (sorting the
resulting multiset) and via the closed form below.

## Statement

Let `A=(p_1\ge p_2\ge\cdots\ge p_m)` be any sorted list of positive reals,
`m\ge1`. Fix `1\le K\le m-1` and suppose `p_K \ge 2\,p_{K+1}`. Using exactly
`K` marks (one mark splitting each of `p_1,\ldots,p_K` into two equal
halves, independently), write `B := \{p_1/2,p_1/2,\ldots,p_K/2,p_K/2\}\cup
\text{Tail}`, where `\text{Tail}:=(p_{K+1},\ldots,p_m)`. Then
```
oddrank(B) = \sum_{i=1}^{K} p_i/2 \;+\; oddrank(\text{Tail}).
```
More generally, if after spending these `K` marks Xiang Yu applies **any**
further refinement `\text{Tail}'` of `\text{Tail}` (using any number of
further marks, not touching the `2K` halved pieces), the same identity holds
with `\text{Tail}'` in place of `\text{Tail}`:
```
oddrank(B) = \sum_{i=1}^{K} p_i/2 \;+\; oddrank(\text{Tail}').
```
(`K=1` recovers Lemma HALVE exactly, including its own "any further
refinement of the tail" corollary.)

## Proof

**Step 1: sortedness of the merged list.** Since `A` is sorted,
`p_1\ge p_2\ge\cdots\ge p_K`, hence `p_1/2\ge p_2/2\ge\cdots\ge p_K/2`
(dividing a sorted chain of positive reals by the same positive constant `2`
preserves the order). By hypothesis `p_K\ge 2p_{K+1}`, i.e. `p_K/2\ge
p_{K+1}=\max(\text{Tail})`. Combining, the full list
`p_1/2,p_1/2,p_2/2,p_2/2,\ldots,p_K/2,p_K/2,\,p_{K+1},\ldots,p_m` is sorted
descending — this is exactly the sorted order of `B` (size `m+K`).

(For the "further refinement `\text{Tail}'`" version: refining `\text{Tail}`
only shrinks individual piece values while preserving their total, so every
resulting fragment of `\text{Tail}'$ is `\le p_{K+1}\le p_K/2`, and the same
sortedness argument applies verbatim with `\text{Tail}'$ in place of
`\text{Tail}`.)

**Step 2: contribution of the `K` halved pairs.** For each `i=1,\ldots,K`,
the pair `(p_i/2,p_i/2)` occupies the two consecutive global ranks
`2i-1,2i` (immediately following the `i-1` earlier pairs, each contributing
exactly `2` ranks, and immediately preceding pair `i+1`). Rank `2i-1` is odd
and rank `2i` is even; since the two copies are numerically identical, the
pair contributes exactly `p_i/2` to `oddrank(B)` regardless of which
specific copy is "nominally" at the odd rank (the standard duplicate-pair
tie observation already used in Lemma DOM's and Lemma HALVE's proofs). Summing
over `i=1,\ldots,K`: the `2K` halved pieces contribute
`\sum_{i=1}^K p_i/2` to `oddrank(B)`.

**Step 3: contribution of the tail.** The tail's elements occupy global
ranks `2K+1,2K+2,\ldots,2K+|\text{Tail}|`. For a local rank `j$ of
`\text{Tail}` (`\text{Tail}` itself sorted, `j=1,\ldots,|\text{Tail}|`), the
global rank is `2K+j`. Since `2K` is **even**, the parity of `2K+j` equals
the parity of `j`: local odd ranks of `\text{Tail}` map to global odd
ranks, and local even ranks map to global even ranks. Hence the tail
contributes exactly `oddrank(\text{Tail})` to `oddrank(B)` (this step is
identical to Lemma DOM's Step 3 / Lemma HALVE's proof, generalized from a
shift of `2` to a shift of `2K`, both even).

**Combining** Steps 2 and 3:
```
oddrank(B) = \sum_{i=1}^K p_i/2 + oddrank(\text{Tail}).
```
The "further refinement" version follows identically: Step 1's sortedness
argument and Step 3's even-shift-by-`2K` argument both go through verbatim
with `\text{Tail}'` (any refinement of `\text{Tail}`, hence still bounded
above by `p_{K+1}\le p_K/2`) in place of `\text{Tail}`. ∎

## Worked numeric check (exact `Fraction`, round-7 explorer's witness)

`A=(583/1000,\,3461/10000,\,709/10000)`, `K=2` (`m=3`). Hypothesis
`p_2\ge2p_3`: `3461/10000 \ge 1418/10000` ✓ (note this is **strictly
weaker** than Lemma HALVE's own top-level hypothesis `p_1\ge2p_2`, which
fails here: `5830/10000 < 6922/10000`).

Direct construction: `B=\{p_1/2,p_1/2,p_2/2,p_2/2,p_3\}` sorted
`= 2915/10000,2915/10000,17305/100000\ldots` — computed exactly:
`p_1/2=2915/1000`, `p_2/2=17305/100000`, giving sorted list
`(2915/1000,\,2915/1000,\,17305/100000,\,17305/100000,\,709/10000)`.
`oddrank(B) = p_1/2+p_2/2+p_3 = 2915/1000+17305/100000+709/10000 =
10709/20000 = 0.53545`, matching the closed-form formula and the explorer's
reported numeric value exactly.

Since `c(2)=4/7\approx0.5714 > 0.53545`, this witness — on which neither
Lemma DOM nor Lemma HALVE fires their own hypothesis at the top level — is
closed by Lemma MULTI-HALVE alone (`K=2`), using the full `2`-mark budget.

## Status

Certified (round 7). Fully proved by direct rank-shift argument (Steps 1–3
above), the same technique already certified for Lemma DOM / Lemma HALVE /
Lemma SPLIT; no new proof machinery beyond generalizing the shift amount
from `2` to the even number `2K`. Independently verified exactly (`Fraction`
arithmetic) against the round-7 explorer's witness. Reusable as a base
mechanism (alongside Lemma DOM, Lemma HALVE, Lemma PARTIAL-DOM, Lemma
PARTIAL-DOM-RESIDUAL, Lemma SPLIT, Lemma TAIL-SNIP, Lemma SANDWICH) for any
future casework or inductive attack on the general upper bound.
