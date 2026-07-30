# Lemma m=4-REGION-A/REGION-B (certified, round 16)

**Status:** proved in full, independently re-verified by the proof-reviewer
(round 16, exact `fractions.Fraction`, ~300,000 random trials, zero
violations, plus a full independent hand re-derivation of the algebra).
Recommend certifying.

**Scope caveat (load-bearing — read before reuse):** this Lemma closes only
**part** of `m=4` Case C (the union of Region 1 and Region 2 below). The
residual Region 3 (`t_1<\tfrac4{15}\Sigma` and the tail is `V_3`-Case-C for
itself) is **not** covered and remains open as of round 16. Do not cite this
Lemma as closing `m=4` Case C in full.

## Setup

`A=(p_1\ge t_1\ge t_2\ge t_3>0)`, `\Sigma:=\Sigma(A)`. Case C:
`p_1<\Sigma/2`. Target: `c(3)\Sigma=\tfrac8{15}\Sigma`. Using Lemma
DOUBLE-INSERT and the certified `m=3` theorem `V_3` (`\le2`-mark recursive
budget):
```
\mathrm{StratA} := t_1+V_3(t_2,t_3,p_1-t_1),
\mathrm{StratB} := p_1/2+V_3(t_1,t_2,t_3).
```
Each costs exactly `1+(\le2)\le3=m-1` marks.

## Statement

(a) **Region 1** (`t_1\ge\tfrac4{15}\Sigma`): `\mathrm{StratA}\le c(3)\Sigma`.

(b) **Region 2** (`t_1<\tfrac4{15}\Sigma` and `t_1\ge(\Sigma-p_1)/2`, i.e.
the tail `(t_1,t_2,t_3)` is itself in `V_3`'s Case B / DOM regime):
`\mathrm{StratB}=p_1/2+t_1<c(3)\Sigma` strictly, with uniform margin
`\ge\Sigma/60`.

Together, (a)+(b) prove `\min(\mathrm{StratA},\mathrm{StratB})\le c(3)\Sigma`
on Region 1 `\cup` Region 2 — an exact algebraic (not numerically-fitted)
sub-region of `m=4` Case C that includes the known extremal point
`A=(6,4,3,2)` (on Region 1's closed boundary `t_1=\tfrac4{15}\Sigma`
exactly).

## Proof

**(a)** By Lemma V3-BOUND (`lemmas/v3-bound.md`) applied to the triple
`(t_2,t_3,r)`, `r:=p_1-t_1`:
```
\mathrm{StratA}\le t_1+\tfrac47(t_2+t_3+r) = t_1+\tfrac47(\Sigma-2t_1)
= \tfrac47\Sigma-\tfrac{t_1}7,
```
using `t_2+t_3+r=\Sigma-2t_1`. This is strictly decreasing in `t_1`, and at
`t_1=\tfrac4{15}\Sigma` it equals `\tfrac47\Sigma-\tfrac17\cdot\tfrac4{15}
\Sigma=\tfrac{56}{105}\Sigma=\tfrac8{15}\Sigma=c(3)\Sigma` exactly. Hence for
`t_1\ge\tfrac4{15}\Sigma`, `\mathrm{StratA}\le\tfrac47\Sigma-\tfrac{t_1}7\le
c(3)\Sigma`.

**(b), Step 1 (tail can never be `V_3`-Case-A here).** Write
`S_{\mathrm{tail}}:=\Sigma-p_1>\Sigma/2` (Case C). Then `\tfrac47
S_{\mathrm{tail}}>\tfrac27\Sigma>\tfrac4{15}\Sigma` (since
`\tfrac27=\tfrac{30}{105}>\tfrac{28}{105}=\tfrac4{15}`). So
`t_1<\tfrac4{15}\Sigma\implies t_1<\tfrac47S_{\mathrm{tail}}`, ruling out the
tail's `V_3`-Case-A threshold unconditionally whenever Region 2's own
hypothesis `t_1<\tfrac4{15}\Sigma` holds.

**(b), Step 2.** Given additionally `t_1\ge S_{\mathrm{tail}}/2` (tail in
`V_3`-Case-B), `V_3(t_1,t_2,t_3)=t_1` exactly (Case B is the exact DOM
value). So `\mathrm{StratB}=p_1/2+t_1`. Using the two strict bounds
`p_1<\Sigma/2` and `t_1<\tfrac4{15}\Sigma`:
```
\mathrm{StratB}<\tfrac\Sigma4+\tfrac4{15}\Sigma=\tfrac{31}{60}\Sigma<
\tfrac{32}{60}\Sigma=\tfrac8{15}\Sigma=c(3)\Sigma,
```
margin `\ge\tfrac1{60}\Sigma`. `\blacksquare`

## Independent verification (round 16, proof-reviewer)

Re-implemented `V_3`/`L_2`/StratA/StratB from scratch (exact `Fraction`),
300,000 random sorted-descending 4-tuples restricted to Case C, classified
into Region 1 / Region 2 / Region 3 (exhaustive, disjoint by construction):
zero violations of the Region-1/Region-2 claims. Independently reproduced
the extremal witness `A=(6,4,3,2)`: `\mathrm{StratA}=8=c(3)\cdot15` exactly
(Region 1 boundary). Independently reproduced witness `A=(6,5,4,2)/17`
(scaled: `\mathrm{StratA}(6,5,4,2)=9\le\tfrac{136}{15}=c(3)\cdot17`, Region
1). Independently reproduced witness `A=(1859,931,619,611)` (Region 3, not
covered by this Lemma — closed instead by `\mathrm{StratC}_{23}=2014\le
2144=c(3)\Sigma`, min over all 5 strategies, per the round-16 build's
uncertified Region-3 partial evidence).
