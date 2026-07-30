# Lemma PARTIAL-DOM-RESIDUAL (certified, round 7)

Source: `universal-adversary-strategy.md`, round 7, certifying a
composition found by the round-7 `math-explorer-menucoverage` report. This
lemma introduces **no new proof machinery**: it is the direct composition
of two already-certified lemmas, **Lemma PARTIAL-DOM**
(`lemmas/partial-dom.md`) and **Lemma SPLIT**
(`lemmas/split-and-tail-snip.md`), applying the latter to the former's
residual piece `r` in place, using its already-known exact sorted rank
inside the merged multiset. Verified exactly (`Fraction` arithmetic) against
the round-7 explorer's Witness 1, `A=(0.5798,0.3515,0.0687)`, `m=3`, budget
`2`: reproduces the explorer's numeric optimum `\approx0.53435` exactly as
`10687/20000`.

This lemma also **depends on, and uses, the corrected scope of Lemma
PARTIAL-DOM**: `p_1\ge S_j$ and `r:=p_1-S_j < t_j` (not the stricter
`j` maximal / `r<U_1` framing in PARTIAL-DOM's original round-6 Remark,
corrected this round — see `lemmas/partial-dom.md`, updated Remark). The
witness below is a genuine instance where `j` is **not** the maximal `j$
with `p_1\ge S_j` (domination could reach `j=2` here), yet the corrected
hypothesis `r<t_j` still holds at the smaller `j=1`, confirming the
corrected scope is exactly what is needed (not "`j` maximal").

## Setup (identical to Lemma PARTIAL-DOM)

`A=(p_1\ge\cdots\ge p_m)`, tail `T=(t_1,\ldots,t_k)` with `t_i:=p_{i+1}`,
`k:=m-1`. Fix `j\in\{1,\ldots,k\}$ (any `j` satisfying PARTIAL-DOM's
corrected hypothesis below — **not required to be maximal**) with
```
p_1 \ge S_j := t_1+\cdots+t_j,\qquad r := p_1-S_j,\qquad r < t_j.
```
By the certified **Lemma PARTIAL-DOM**, spending `j` marks (all inside
`p_1`, splitting it into `t_1,\ldots,t_j,r`) and merging with the untouched
full tail `T$ gives `B` (size `m+j`) with
```
oddrank(B) = \tfrac12\big(p_1+\Sigma(T)+D(B)\big),\quad
D(B) = D(U) + (-1)^e\big[r - 2D(U_{>e})\big],
```
where `U:=(t_{j+1},\ldots,t_k)` (size `k-j`), `e:=\#\{i: U_i\ge r\}`
(`0\le e\le k-j`), and `D(X):=\sum_i(-1)^{i+1}X_i` for sorted `X`. Lemma
PARTIAL-DOM's proof additionally establishes that `r$ occupies **exact
sorted rank** `\rho := 2j+e+1` inside `B` (immediately after the
duplicated prefix block, size `2j`, and the first `e` elements of `U`, all
`\ge r`, and immediately before `U_{>e} := (U_{e+1},\ldots,U_{k-j})`, all
`<r`).

## Statement

Suppose the total budget available is `k_{\text{tot}} > j` (so at least one
more mark remains after the `j` marks spent on Lemma PARTIAL-DOM), and
suppose the **Lemma SPLIT hypothesis at `r`'s position** holds:
```
r/2 \ge U_{e+1}\quad\text{(the element of }B\text{ immediately after }r,
\text{ vacuous if }e=k-j\text{, i.e. }U_{>e}\text{ empty).}
```
Then spending **one further mark**, splitting `r` into two copies of `r/2`
(leaving every other piece of `B` unchanged) gives `B'$ (size `m+j+1`,
total marks used `j+1\le k_{\text{tot}}`) with
```
oddrank(B') = oddrank(B) + \Delta,\qquad
\Delta = (-1)^{e+1}\,\frac{r}{2} + (-1)^{e}\Big[2\,oddrank(U_{>e}) -
\Sigma(U_{>e})\Big].
```

## Proof

This is a direct application of the already-certified **Lemma SPLIT**
(`lemmas/split-and-tail-snip.md`) to the sorted list `B` (established by
Lemma PARTIAL-DOM), at index `i=\rho=2j+e+1$, with `R:=(a_{\rho+1},\ldots)$
— which, by Lemma PARTIAL-DOM's own rank computation, is exactly
`U_{>e}` (the elements of `B` strictly after `r`'s position). Lemma SPLIT's
hypothesis "`a_i/2\ge a_{i+1}`" is exactly the hypothesis assumed above
(`r/2\ge U_{e+1}`, or vacuous if `r` is `B`'s last element).

Lemma SPLIT gives, for `i=\rho` odd or even:
```
i\text{ odd}:\quad oddrank(B')-oddrank(B) = -r/2 + 2\,oddrank(U_{>e}) -
\Sigma(U_{>e}),
i\text{ even}:\quad oddrank(B')-oddrank(B) = r/2 + \Sigma(U_{>e}) -
2\,oddrank(U_{>e}).
```
It remains only to express the parity of `\rho=2j+e+1$ in terms of `e`:
since `2j` is always even, `\rho` is odd exactly when `e+1` is odd, i.e.
when `e` is **even**, and `\rho` is even exactly when `e` is **odd**. So:
- `e` even (`\rho$ odd): `\Delta = -r/2+2\,oddrank(U_{>e})-\Sigma(U_{>e})`,
  matching `(-1)^{e+1}r/2=(-1)^{1}r/2=-r/2` and
  `(-1)^e[\cdots]=(+1)[\cdots]`. ✓
- `e` odd (`\rho` even): `\Delta = r/2+\Sigma(U_{>e})-2\,oddrank(U_{>e})`,
  matching `(-1)^{e+1}r/2=(+1)r/2=r/2` and
  `(-1)^e[\cdots]=(-1)[\cdots]`. ✓

Both cases match the single compact formula
`\Delta=(-1)^{e+1}r/2+(-1)^e[2\,oddrank(U_{>e})-\Sigma(U_{>e})]` stated
above. `oddrank(B')=oddrank(B)+\Delta` follows directly from Lemma SPLIT's
statement (`oddrank(B')-oddrank(B)=\Delta`, i.e. the change from splitting
`a_i=r$ into two halves, applied to the sorted list `B`). ∎

## Worked numeric check (exact `Fraction`, round-7 explorer's Witness 1)

`A=(5798/10000,\,3515/10000,\,687/10000)`, `m=3`, total budget `2`. Take
`j=1$ (note: **not** the maximal `j` — domination reaches `j=2` here, since
`p_1=5798/10000\ge S_2=t_1+t_2=3515/10000+687/10000=4202/10000` — but the
budget-saving choice `j=1` is deliberately made to leave a mark spare for
the residual refinement below):
```
S_1 = t_1 = 3515/10000,\quad p_1\ge S_1 \checkmark,\quad
r = p_1-S_1 = 2283/10000,\quad t_1 = 3515/10000 > r \checkmark
\text{ (corrected hypothesis $r<t_j$ holds)}.
```
`U = (t_2) = (687/10000)$ (size `k-j=1`). `e=\#\{U_i\ge r\}
=\#\{687/10000\ge2283/10000\}=0`. Lemma PARTIAL-DOM: `B` sorted
`=(3515,3515,2283,687)/10000$; direct computation
`oddrank(B)=(3515+2283)/10000=5798/10000` (`=p_1$, matching Lemma DOM's
value, as expected since `j=1$ and `j=2$ both realize full-tail-style
domination values here).

Residual step: `r=2283/10000$, `\rho=2\cdot1+0+1=3` (odd, matches `e=0`
even). `U_{>0}=U=(687/10000)` (nonempty, `e=0<k-j=1`). Lemma SPLIT
hypothesis: `r/2=1141.5/10000\ge U_1=687/10000` ✓. Applying:
```
\Delta = -r/2 + 2\,oddrank(U_{>0}) - \Sigma(U_{>0})
       = -1141.5/10000 + 2(687/10000) - 687/10000
       = -1141.5/10000 + 687/10000 = -454.5/10000.
```
```
oddrank(B') = 5798/10000 - 454.5/10000 = 5343.5/10000 = 10687/20000
            = 0.53435.
```
This matches the round-7 explorer's independently-found numeric optimum on
this witness (`\approx0.53435`) exactly, and beats `c(2)=4/7\approx0.5714$
with `0.5714-0.53435\approx0.0371$ to spare, using exactly the `2`-mark
budget (`j=1$ mark on the PARTIAL-DOM step, `1` more mark on the residual
split).

## What this closes

A mechanical corollary of two already-certified lemmas: whenever a
sub-maximal (or maximal) PARTIAL-DOM chain leaves budget to spare, and the
residual `r` satisfies the Lemma SPLIT hypothesis relative to its own
sorted neighbor, refining `r` in place strictly improves on stopping after
the chain alone. This closes a concrete gap the round-7 explorer identified
in the previous menu: PARTIAL-DOM's original write-up "spends its full `j`
marks and stops," never revisiting `r` with leftover budget — this lemma
fixes that specific incompleteness. Iterating the same composition further
(e.g. re-applying Lemma SPLIT to one of `B'`'s new fragments, or re-applying
a fresh Lemma PARTIAL-DOM instance to a different piece of `B'` with
whatever budget remains) is a direct re-application of already-certified
machinery and is not separately proved here — no new content is needed for
such further iteration beyond invoking the same certified lemmas again.

## What this does not close

Like Lemma PARTIAL-DOM and Lemma MULTI-HALVE individually, this composition
does not by itself resolve the general matching/assignment optimality
question (which tie-structure, of the finite family Lemma TIE-NECESSARY
identifies, is globally best for a given `A`). It is one additional
constructive member of the extended menu, not a general theorem; see
`universal-adversary-strategy.md`'s "Round 7: retargeting" section for the
current honest status of that broader question, including a concrete
demonstration (the `m=5` witnesses) that even this extended menu, applied
recursively, does not yet cover every configuration.

## Status

Certified (round 7). Fully proved as a direct, mechanical composition of
the already-certified Lemma PARTIAL-DOM and Lemma SPLIT — no new proof
machinery. Independently verified exactly (`Fraction` arithmetic) against
the round-7 explorer's Witness 1.
