# Lemma THRESHOLD-REDUCTION (peel+halve / DOM close two of the three cases of Claim PTBI)

**Status:** proved in full below (round 8, `universal-adversary-strategy`).
Recommend certifying.

## Setup

Recall Claim PTBI: for every `m\ge1` and every sorted `A=(p_1\ge\cdots\ge
p_m)` of positive reals, using `\le m-1` marks Xiang Yu can achieve
`oddrank(B)\le c(m-1)\Sigma(A)`, where `c(k):=2^k/(2^{k+1}-1)` (`c(0):=1`).
Write `\Sigma:=\Sigma(A)`, `S:=\Sigma-p_1`.

## The algebraic identity

**Fact.** For every integer `k\ge1`,
```
c(k-1) = \frac{c(k)}{2(1-c(k))}.
```
*Proof.* `1-c(k) = 1-\dfrac{2^k}{2^{k+1}-1} = \dfrac{2^{k+1}-1-2^k}{2^{k+1}-1}
= \dfrac{2^k-1}{2^{k+1}-1}`. Hence
`\dfrac{c(k)}{2(1-c(k))} = \dfrac{2^k/(2^{k+1}-1)}{2(2^k-1)/(2^{k+1}-1)} =
\dfrac{2^k}{2(2^k-1)} = \dfrac{2^{k-1}}{2^k-1} = c(k-1)`. `∎`

Equivalently: `c(k) = \dfrac{2c(k-1)}{1+2c(k-1)}`, or `2c(k-1)(1-c(k))=c(k)`.
(Sanity check, `k=2`: `c(1)=2/3,\ c(2)=4/7`; `2\cdot(2/3)(1-4/7) =
2\cdot(2/3)(3/7) = 4/7 = c(2)$ ✓.)

## Case A: `p_1 \ge c(m-1)\,\Sigma` — closed by peel+halve + IH

Assume Claim PTBI holds for all sizes `<m` (strong induction hypothesis;
for this case only the immediate tail `T$, of size `m-1`, is needed).
Split `p_1` into two equal halves (`1` mark, unconditional via the
certified **Lemma DOUBLE-INSERT**, `lemmas/double-insert.md`). Apply the
inductive hypothesis to `T=(p_2,\ldots,p_m)` (size `m-1`, budget `m-2`) to
get a response `T'` with `oddrank(T')\le c(m-2)\,S`. By Lemma DOUBLE-INSERT
(unconditional, no domination hypothesis needed for inserting a duplicated
value),
```
oddrank(\{p_1/2,p_1/2\}\cup T') = oddrank(T') + p_1/2 \le g(p_1)
:= p_1/2 + c(m-2)(\Sigma-p_1),
```
using `1+(m-2)=m-1` marks total (exactly the full budget for size `m`).

`g$ is affine in `p_1` with slope `1/2-c(m-2)`. Since `c(k)>1/2` for every
finite `k$ (direct computation: `2^k/(2^{k+1}-1)>1/2 \iff 2^{k+1}>2^{k+1}-1`,
always true), the slope is **strictly negative**, so `g` is strictly
decreasing in `p_1`. Hence for `p_1\ge c(m-1)\Sigma`,
```
g(p_1) \le g(c(m-1)\Sigma) = \Sigma\Big[c(m-1)/2 + c(m-2)\big(1-c(m-1)\big)\Big].
```
By the Fact above (with `k=m-1`), `c(m-2)(1-c(m-1)) = c(m-1)/2`, so the
bracket equals `c(m-1)/2+c(m-1)/2 = c(m-1)`. Hence `g(c(m-1)\Sigma) =
c(m-1)\Sigma`, and therefore `oddrank(B)\le g(p_1) \le c(m-1)\Sigma`
whenever `p_1\ge c(m-1)\Sigma`. **Case A closed**, for every `m\ge2`.

(Base of the induction on which this recursion rests: `m=1` is trivial
(`0` marks, `oddrank(A)=p_1=\Sigma=c(0)\Sigma`); `m=2` is the fully closed
`n=1` result in `universal-adversary-strategy.md`.)

## Case B: `\Sigma/2 \le p_1 < c(m-1)\Sigma` — closed by DOM directly

`p_1\ge\Sigma/2 \iff p_1 \ge \Sigma-p_1 = S`, exactly Lemma DOM's hypothesis
(`lemmas/generalized-domination-and-halving.md`). Lemma DOM gives, using
`m-1` marks (all inside `p_1`), `oddrank(B)=p_1` exactly. Since
`p_1<c(m-1)\Sigma` by hypothesis, `oddrank(B)=p_1<c(m-1)\Sigma`. **Case B
closed**, for every `m\ge2`, with no recursion needed at all.

## Conclusion: reduction to Case C

Cases A and B together cover exactly `p_1\ge\Sigma/2` (since
`c(m-1)>1/2\ge 0` makes the two ranges `[\,c(m-1)\Sigma,\infty)` and
`[\Sigma/2,\,c(m-1)\Sigma)` adjacent and covering `[\Sigma/2,\infty)`
jointly, and `p_1\le\Sigma` always). Hence:

**Claim PTBI, for every `m\ge2`, reduces exactly to the single remaining
case**
```
Case C:   p_1 < \Sigma(A)/2   (equivalently p_1 < S).
```
Case C is the genuine open content of Claim PTBI's inductive step; Cases A
and B are fully, unconditionally closed by the argument above, for every
`m\ge2` and every sorted `A$ of size `m`, using only the certified Lemma
DOUBLE-INSERT, Lemma DOM, and the induction hypothesis at size `m-1`.
