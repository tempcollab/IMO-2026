# Lemma PAIR-VALUE (unconditional value of an arbitrary set of tied pairs)

**Status:** proved in full below (round 9, `universal-adversary-strategy`).
Recommend certifying. Strictly generalizes the certified Lemma BLOCK-RECURSE
(`lemmas/block-recurse.md`) by removing its contiguity/domination hypothesis
entirely.

## Statement

Let `B` be a finite multiset of positive reals that decomposes as
```
B = U \uplus \{v_1,v_1\} \uplus \{v_2,v_2\} \uplus \cdots \uplus \{v_k,v_k\}
```
(multiset union), i.e. `B` consists of `k` **tied pairs** — each pair being
two elements of *exactly* equal value `v_i` — together with a remaining
sub-multiset `U` of "unpaired" elements. The pairs may sit **anywhere** in
`B`'s sorted order, in any relative position to `U` and to each other (no
domination, no contiguity, no ordering assumption of any kind relating the
`v_i` to `U` or to one another). Then, unconditionally,
```
oddrank(B) = oddrank(U) + \sum_{i=1}^k v_i.
```

## Proof

By induction on `k`.

**Base case `k=0`.** `B=U`, trivial.

**Inductive step.** Assume the claim holds for every multiset decomposable
into `k-1` tied pairs plus an unpaired remainder (of any composition).
Given `B` with `k` tied pairs as above, fix any one pair, say the one with
value `v:=v_k`, and consider `B`'s sorted (descending) arrangement.

*Claim: the two elements of this pair occupy two globally-adjacent ranks
`r,r+1` for some `r`.* Both elements equal `v` exactly. In a descending
sorted arrangement, any element strictly between two elements of value `v`
in rank order must itself have value `v` (sorted order is monotone in
value); so no element of a *different* value can be interposed between the
two chosen copies. If additional elements of `B` also equal `v` (i.e. `v`
appears with higher multiplicity than just this one pair, whether from
other pairs sharing the same value or from `U` containing copies of `v`),
all such equal-valued elements occupy one contiguous run of ranks, and we
may always designate *some* two of them adjacent to each other as "this
pair" (the specific labelling of which formal copies constitute the pair
is immaterial to the value of `oddrank`, since all these elements are
numerically identical — this is the same tie-insensitivity observation
used already in the certified Lemma DOM, Step 1, and Lemma BLOCK-RECURSE,
Step 2). So without loss of generality the pair occupies adjacent global
ranks `r,r+1`.

*Contribution of this pair.* Of the two consecutive ranks `r,r+1`, exactly
one is odd. Since both elements equal `v`, that odd rank contributes `v` to
`oddrank(B)`, regardless of which of `r,r+1` is the odd one. So this pair
contributes exactly `v` to `oddrank(B)`.

*Effect of removing this pair.* Let `B' := B` with these two elements
deleted (`k-1` remaining tied pairs, unpaired part still exactly `U`,
unchanged). Every element of `B` at global rank `<r` is unaffected (same
value, same rank, in `B'`). Every element of `B` at global rank `>r+1` is
shifted down by exactly `2` positions in `B'` (its rank in `B'` equals its
rank in `B` minus `2`) — a shift by an **even** number, which preserves the
parity of every such element's rank. Hence
```
oddrank(B) = oddrank(B') + v,
```
since the only rank-parity–relevant change between `B` and `B'` is the
removal of the pair itself (contributing `v`, computed above), and every
other element's parity-class (odd/even rank) is unchanged by the even
shift.

*Applying the inductive hypothesis to `B'`.* `B'` decomposes into the
remaining `k-1` tied pairs `\{v_1,v_1\},\ldots,\{v_{k-1},v_{k-1}\}` plus the
*same* unpaired remainder `U` (untouched by this step). By the inductive
hypothesis,
```
oddrank(B') = oddrank(U) + \sum_{i=1}^{k-1} v_i.
```
Combining,
```
oddrank(B) = oddrank(U) + \sum_{i=1}^{k-1}v_i + v_k = oddrank(U) + \sum_{i=1}^k v_i.
```
This completes the induction. `∎`

## Independent numerical verification

Verified exactly (`fractions.Fraction`, no floating point) by 20,000 random
trials with `k\in\{0,\ldots,5\}` random tied pairs and `c\in\{0,\ldots,6\}`
random unpaired singletons, values drawn independently and uniformly (so
pairs and unpaired elements interleave in arbitrary, unpredictable relative
order — no domination or contiguity engineered into the test), zero
mismatches. Repeated with values drawn from a small range `\{1,\ldots,8\}`
specifically to force frequent exact coincidences between different pairs'
values and between pair values and unpaired values (stress-testing the
tie-insensitivity argument in the proof), again zero mismatches across
20,000 trials.

## Relationship to Lemma BLOCK-RECURSE

Lemma BLOCK-RECURSE (`lemmas/block-recurse.md`) is the special case of
Lemma PAIR-VALUE where the `k` pairs additionally satisfy a domination
hypothesis (every pair value `\ge` every element of `U`), which forces the
pairs to occupy the **contiguous** top `2k` ranks. Lemma PAIR-VALUE shows
this domination/contiguity hypothesis was never actually necessary for the
*value identity* — exactly the same phenomenon already found for Lemma
HALVE vs. its hypothesis-free generalization Lemma DOUBLE-INSERT
(`lemmas/double-insert.md`; indeed Lemma DOUBLE-INSERT is itself the `k=1`
special case of Lemma PAIR-VALUE, with `v_1=p_1/2` and `U=T`). Lemma
PAIR-VALUE is the common generalization of Lemma DOUBLE-INSERT and Lemma
BLOCK-RECURSE (and, applied iteratively, of Lemma MULTI-HALVE), and removes
the "contiguity does not automatically transfer to arbitrary subsets"
technical risk flagged for arbitrary-subset matching: **contiguity is
never needed in the first place**, for any number of pairs, in any
arrangement.

## Consequence: arbitrary-subset matching ("SUBSET-DOM" construction)

**Corollary (SUBSET-DOM).** Let `A=(p_1\ge\cdots\ge p_m)` be any sorted
list of positive reals. Choose any element `p_i` and any subset
`T=\{q_1,\ldots,q_j\}` of the *other* elements' current values (a subset of
the multiset `A\setminus\{p_i\}`, with multiplicity, `j\ge1`), such that
`p_i \ge \Sigma(T) := q_1+\cdots+q_j`. Split `p_i` into the `j+1` parts
`q_1,\ldots,q_j,\ r:=p_i-\Sigma(T)` (`j` marks; if `r=0`, only `j-1` marks,
by the same argument as the certified Lemma DOM-boundary-slack). This
creates `j` tied pairs (each new fragment `q_\ell` paired with the
already-present element of value `q_\ell` it was chosen to match) and
leaves an unpaired remainder `U := (A\setminus(\{p_i\}\cup T)) \cup \{r\}`
(the elements of `A` neither `p_i` nor matched, together with the
residual). By Lemma PAIR-VALUE, **unconditionally, regardless of how `T`
was chosen (prefix, arbitrary subset, or otherwise) and regardless of any
domination relationship between `T`, `r`, and the rest of `A`**:
```
oddrank(B) = \Sigma(T) + oddrank(U),
```
and this identity is preserved under **any** further recursive refinement
of `U` alone (apply Lemma PAIR-VALUE again to the refined multiset, since
the `j` matched pairs are untouched by refining `U`). This is exactly Lemma
BLOCK-RECURSE's conclusion, but now proved **without** the hypothesis
`r<t_j` (equivalently `\max(U)\le\min(T)`) that Lemma BLOCK-RECURSE needed
to establish contiguity — `T` may be an arbitrary subset of the other
elements, not merely a sorted prefix.

(Choosing *which* subset `T` to match, among all subsets of the current
multiset with `\Sigma(T)\le p_i`, so as to minimize the resulting
`oddrank(U)` recursively, is a combinatorial selection problem — Hall's
marriage theorem, cited in `knowledge_base.md`, is the natural tool for
proving *existence* of a valid simultaneous multi-donor assignment when
several elements are split at once to match disjoint target subsets
without conflict (a bipartite system-of-distinct-representatives
condition); Lemma PAIR-VALUE itself does not need Hall's theorem for the
*value identity* — that identity is unconditional in `T` — Hall's theorem
becomes relevant only for the separate, harder question of *proving a good
`T` always exists* for the general induction, which remains open, see
`approaches/universal-adversary-strategy.md`.)

## Worked check against the round-9 falsifying witness

`A=(12,6,5,4,2)/29`, `m=5`, budget `4`, target `c(4)=16/31\approx0.5161`.
Applying SUBSET-DOM with `p_i=p_2=6/29` and `T=\{p_4,p_5\}=\{4/29,2/29\}`
(a genuinely non-prefix subset, skipping `p_3=5/29`): `\Sigma(T)=6/29=p_2`
exactly, so `r=0` and this match costs `1` mark (not `2`, by the
`r=0`-boundary saving). The unpaired remainder is
`U=\{p_1,p_3\}=\{12/29,5/29\}`. Recursing on `U` (an `n=1` sub-instance,
already fully closed in `universal-adversary-strategy.md`): `\max(U)/\Sigma(U)
= (12/29)/(17/29)=12/17\in[2/3,1]`, so the "halve the max" sub-case
applies, `1` mark, giving `oddrank(U')=\Sigma(U)-p_1/2 = 17/29-6/29=11/29`
(equivalently `p_1/2+p_3=6/29+5/29=11/29`). Total marks used:
`1\,(\text{match }p_2)+1\,(\text{halve }p_1) = 2 \le 4`. By SUBSET-DOM,
```
oddrank(B) = \Sigma(T) + oddrank(U') = \frac{6}{29} + \frac{11}{29} =
\frac{17}{29} \approx 0.586,
```
which does **not** beat `c(4)\approx0.5161` by itself — recursing on `U`
alone (leaving `p_3` untouched) is not the winning choice. **Splitting
`p_3` as well** (still within budget: `1`+`1`+`1`=`3\le4` marks) gives a
strictly better value: match `p_2\to\{p_4,p_5\}` (1 mark, pairs
`(4/29,4/29)`,`(2/29,2/29)`), halve `p_1` (1 mark, pair `(6/29,6/29)`), halve
`p_3` (1 mark, pair `(5/58,5/58)`). Now **every** element of `B` is paired
(`U=\emptyset`), so by Lemma PAIR-VALUE,
```
oddrank(B) = 0 + \left(\frac{p_1}{2}+\frac{p_3}{2}+p_4+p_5\right)
= \frac{6}{29}+\frac{5}{58}+\frac{4}{29}+\frac{2}{29}
= \frac{12}{58}+\frac{5}{58}+\frac{8}{58}+\frac{4}{58} = \frac{29}{58} =
\frac12.
```
Independently verified by direct exact-`Fraction` computation of the full
sorted `8`-element multiset
`(6/29,6/29,4/29,4/29,5/58,5/58,2/29,2/29)`: `oddrank = 6/29+4/29+5/58+2/29
= 12/58+8/58+5/58+4/58=29/58=1/2`, matching. Uses `3` marks, within the
budget-`4` limit, and `1/2 < c(4)=16/31\approx0.5161`, **closing the
witness** — this fixes the concrete falsifying construction the round-9
explorer found (the previous certified menu's best value on this witness
was `15/29\approx0.5172 > c(4)`).

**What this shows and what it does not.** This confirms Lemma PAIR-VALUE
(via its SUBSET-DOM corollary) supplies the missing move: an arbitrary,
non-prefix subset match, with the matched block's contribution to
`oddrank` computed exactly with **no contiguity/domination hypothesis at
all** — resolving the specific technical risk the round-9 plan flagged
("BLOCK-RECURSE's contiguity argument does NOT automatically transfer to
arbitrary subsets"): it does transfer, because contiguity was never
actually required for the value identity in the first place (Lemma
PAIR-VALUE's proof needs only that each pair's two elements are
*mutually* adjacent, not that different pairs or the unpaired remainder
sit in any particular global arrangement). This closes the one concrete
falsifying witness. It does **not** by itself prove a general theorem that
*some* choice of donor element(s) and target subset(s) always achieves
`oddrank(B)\le c(m-1)\Sigma(A)` for every configuration and every `m` — that
general existence statement (where Hall's marriage theorem would be the
natural tool for handling *simultaneous, non-conflicting* multi-donor
matches) is not attempted in general this round; see
`approaches/universal-adversary-strategy.md` for the precise scope of what
remains open.
