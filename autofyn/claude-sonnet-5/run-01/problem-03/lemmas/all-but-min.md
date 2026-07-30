# Lemma ALL-BUT-MIN (halve every piece except the smallest)

**Status:** proved in full below (round 10, `universal-adversary-strategy`).
Recommend certifying. Direct corollary of the already-certified,
hypothesis-free Lemma PAIR-VALUE (`lemmas/pair-value.md`); generalizes the
round-9 `m=3` sub-case-1 computation (`p_3≤Σ/7`) to every `m≥2`.

## Statement

Let `A=(p_1\ge p_2\ge\cdots\ge p_m)` be any sorted list of positive reals,
`m\ge2`, `\Sigma:=\Sigma(A)`. Using exactly `m-1` marks — split each of
`p_1,\ldots,p_{m-1}` into two exact halves, leaving `p_m` (the smallest
element) untouched — the resulting multiset `B` satisfies, **unconditionally
(no domination hypothesis of any kind)**:
```
oddrank(B) = \Sigma/2 + p_m/2.
```
Consequently, whenever
```
p_m \le \Sigma/(2^m-1),
```
this construction gives `oddrank(B)\le c(m-1)\,\Sigma`, closing that
instance of Claim PTBI's inductive step directly (no recursion, no
induction hypothesis needed).

## Proof

*Value identity.* `B` decomposes exactly as `m-1` tied pairs
`\{p_i/2,p_i/2\}` (`i=1,\ldots,m-1`) plus the single unpaired element `p_m`
(the certified decomposition hypothesis of Lemma PAIR-VALUE:
`B = U \uplus \{v_1,v_1\}\uplus\cdots\uplus\{v_{m-1},v_{m-1}\}` with
`U=\{p_m\}`, `v_i=p_i/2`). By Lemma PAIR-VALUE (no domination or contiguity
hypothesis required — it holds for pairs in *any* relative position),
```
oddrank(B) = oddrank(U) + \sum_{i=1}^{m-1} v_i = p_m + \sum_{i=1}^{m-1}
\frac{p_i}{2} = p_m + \frac{\Sigma-p_m}{2} = \frac{\Sigma}{2}+\frac{p_m}{2}.
```
This uses exactly `m-1` marks (one per split piece `p_1,\ldots,p_{m-1}`),
matching Claim PTBI's budget exactly.

*Threshold.* We need `\Sigma/2+p_m/2 \le c(m-1)\Sigma`, i.e.
`p_m \le \bigl(2c(m-1)-1\bigr)\Sigma`. Compute, for every `k\ge0`,
```
2c(k)-1 = \frac{2\cdot2^k}{2^{k+1}-1} - 1 = \frac{2^{k+1}-(2^{k+1}-1)}
{2^{k+1}-1} = \frac{1}{2^{k+1}-1}.
```
With `k=m-1`, `2c(m-1)-1 = 1/(2^m-1)`, giving the stated threshold
`p_m\le\Sigma/(2^m-1)`. `∎`

## Sanity check against round-9's `m=3` sub-case-1

For `m=3`, the threshold is `\Sigma/(2^3-1)=\Sigma/7`, exactly the
round-9-established boundary (`p_3\le1/7` when `\Sigma=1`) for the
"peel+halve both `p_1` and `p_2`" construction (there proved directly via
two applications of Lemma DOUBLE-INSERT; Lemma ALL-BUT-MIN is the
`m`-general form of exactly this construction, now derived in one line from
Lemma PAIR-VALUE instead of iterated DOUBLE-INSERT).

## Independent numerical verification

Checked directly (`fractions.Fraction`, exact arithmetic) on 3,000+ random
configurations, `m=2,\ldots,8`: the identity `oddrank(B)=\Sigma/2+p_m/2`
holds exactly in every trial, and the predicted threshold
`p_m\le\Sigma/(2^m-1)` is confirmed to be exactly the boundary at which this
construction meets the target `c(m-1)\Sigma` with equality (checked
symbolically for `m=2,\ldots,9`).

## Scope

This closes one further explicit sub-region of Claim PTBI's Case C
(`p_1<\Sigma/2`) for every `m\ge2`: the region `p_m\le\Sigma/(2^m-1)`
(the smallest element is small enough). It does **not** by itself close
Case C in general — see `approaches/universal-adversary-strategy.md`,
round 10, for the precisely narrowed residual gap and a second,
complementary construction (Lemma MATCH-TAIL-PAIR,
`lemmas/match-tail-pair.md`) plus an explicit witness showing the two
together still do not cover all of Case C for `m\ge5`.
