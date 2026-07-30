# Lemma PARTIAL-DOM (certified, round 6)

Source: `universal-adversary-strategy.md`, round 6 (skeleton proposed by the
round-6 `math-explorer-coordsplit` report; proved in full by the round-6
proof-builder, using the already-certified alternating-sum toolkit
`D-REFORM`, `D-INSERT`, `lemmas/alternating-sum-toolkit.md`). Strictly
generalizes the already-certified **Lemma DOM**
(`lemmas/generalized-domination-and-halving.md`), which is the special case
`j = m-1` (full tail) below. Verified independently by exact-`Fraction`
computation: the general closed-form formula against 5,000 random trials
(sizes `m=3..7`, zero mismatches) and exactly against the round-6 explorer's
worked numeric example (`A=(0.4859,0.3439,0.0884,0.0496,0.0322)`, `j=2`,
reproduces `oddrank=5181/10000=0.5181` exactly, matching the explorer's
independently-found numeric optimum to the digit).

## Setup

Let `A=(p_1\ge p_2\ge\cdots\ge p_m)` sorted descending, `m\ge2`. Tail
`T=(p_2,\ldots,p_m)` (already sorted). For `0\le j\le m-1`, write the
**prefix sum** `S_j := p_2+\cdots+p_{j+1}` (`S_0:=0`). For a sorted list
`X=(x_1\ge\cdots\ge x_\ell)`, write `D(X):=\sum_i(-1)^{i+1}x_i` (the
alternating sum of the certified `D-REFORM`/`D-INSERT` toolkit;
`D(\emptyset):=0`).

## Statement

Suppose `j` is chosen with `j\le k` (available marks) and `p_1\ge S_j`, and
(this is the natural/intended case, see Remark below) `j` is **maximal**
with this property among `0,\ldots,\min(k,m-1)` — equivalently `p_1<S_{j+1}`
whenever `j<\min(k,m-1)`. Using exactly `j` marks (all inside `p_1`), split
`p_1` into the `j+1` parts
```
q_1=p_2,\; q_2=p_3,\;\ldots,\;q_j=p_{j+1},\quad q_{j+1}=r:=p_1-S_j\;(\ge0),
```
and merge with the **untouched, full** tail `T` (size `m-1`, not just its
first `j` elements) to get `B` (size `m+j`). Write `U:=(p_{j+2},\ldots,p_m)`
(the tail elements *beyond* the matched prefix, size `m-1-j`; empty if
`j=m-1`) and let `e:=\#\{i: U_i\ge r\}` (`0\le e\le m-1-j`), `U_{>e}` the
suffix of `U` after dropping its first `e` elements. Then:
```
D(B) = D(U) + (-1)^e\big[r - 2\,D(U_{>e})\big],
oddrank(B) = \tfrac12\big(p_1+\Sigma(T)+D(B)\big).
```

**Special case `j=m-1` (full tail, `U=\emptyset`) recovers Lemma DOM.**
Then `D(U)=0`, `e=0` (vacuously, `U` empty so `U_{>0}=\emptyset`,
`D(U_{>0})=0`), giving `D(B)=r`, hence
`oddrank(B)=\tfrac12(p_1+S+r)=\tfrac12(p_1+S+p_1-S)=p_1` (using `r=p_1-S`,
`S=S_{m-1}=\Sigma(T)`) — exactly Lemma DOM's conclusion, independently
re-derived here as a special case.

## Proof

**Step 1: `D` of the pre-insertion merge `M := \{q_1,q_1'\},\ldots` — precisely,
`M:=\{p_2,p_2,\ldots,p_{j+1},p_{j+1}\}\cup U`** (the duplicated matched
prefix, from the split `q_1,\ldots,q_j` merging with `T`'s own copies of
`p_2,\ldots,p_{j+1}`, together with the untouched remainder `U` of `T`).
Write `t_i:=p_{i+1}` (`i=1,\ldots,j`, the matched prefix). Since every
`t_i\ge` every element of `U` (as `T` is sorted and `U` is `T`'s tail beyond
position `j`), `M`'s sorted order is exactly
`t_1,t_1,t_2,t_2,\ldots,t_j,t_j,\,U_1,\ldots,U_{m-1-j}` (duplicated block
first, size `2j`, then `U`, size `m-1-j`).

Each duplicated pair `(t_i,t_i)` occupies two *consecutive* sorted
positions, contributing `t_i-t_i=0` to any alternating sum computed over
just that pair in isolation; more precisely, by direct summation, the
duplicated block alone (size `2j`) has alternating sum `0` (telescoping:
`t_1-t_1+t_2-t_2+\cdots=0`). Appending `U` after it shifts `U`'s global
positions by `2j` (**even**), which preserves the sign `(-1)^{\text{pos}+1}`
attached to each of `U`'s elements (since flipping the parity of a shift by
an even number does nothing). Since alternating sum is by definition a sum
of signed terms and the duplicated block's own signed sum is `0`
independent of `U`, we get
```
D(M) = 0 + D(U) = D(U).
```
(This "block cancels, shift by an even amount preserves the rest" argument
is the same mechanism as Lemma DOM's Step 1, restated in `D`-language;
directly verified by exact computation above, 5,000 trials, zero
mismatches.)

**Step 2: insert `r` via the certified Lemma D-INSERT.** We must locate
`r`'s sorted rank within `M` (size `m-1+j`). By the maximality hypothesis on
`j`: if `j<\min(k,m-1)`, `p_1<S_{j+1}=S_j+p_{j+2}=S_j+U_1`, so
`r=p_1-S_j<U_1=\max(U)\le t_j=\min(\text{duplicated block})`; if
`j=\min(k,m-1)` and `j=m-1` there is no `U` and this comparison is vacuous;
if `j=k<m-1`, the maximality hypothesis is about the *budget* boundary, and
we separately require `r<U_1` as a standing hypothesis for this formula (see
Remark). In every case covered by the statement, `r` is **strictly below
the entire duplicated block** and inserts somewhere within (or at the very
end of) the `U`-portion of `M`. Concretely `r` lands at sorted rank
`\rho:=2j+e+1` in `M` (immediately after the duplicated block and the first
`e` elements of `U`, all `\ge r`, and immediately before `U_{>e}`, all
`<r`, up to ties which don't affect the sum).

Lemma D-INSERT gives `D(B) = D(M) - 2\tau(\rho) + (-1)^{\rho+1}r`, where
`\tau(\rho)=\sum_{i\ge\rho}(-1)^{i+1}M_i$ (over `M`'s *original* positions).
The elements at original `M`-positions `\ge\rho=2j+e+1` are exactly
`U_{>e}=(U_{e+1},\ldots,U_{m-1-j})`, at positions `2j+e+1,2j+e+2,\ldots`; the
sign at position `2j+e+\ell` (`\ell=1,\ldots$) is
`(-1)^{2j+e+\ell+1}=(-1)^{e+\ell+1}$ (since `2j` is even), i.e. `(-1)^e`
times the *standard* sign `(-1)^{\ell+1}` that `U_{e+\ell}` would carry as
the `\ell`-th element of `U_{>e}` on its own. Hence
`\tau(\rho)=(-1)^e\,D(U_{>e})`. Also `(-1)^{\rho+1}=(-1)^{2j+e+2}=(-1)^e`.
Substituting, and `D(M)=D(U)` from Step 1:
```
D(B) = D(U) - 2(-1)^e D(U_{>e}) + (-1)^e r = D(U) + (-1)^e\big[r-2D(U_{>e})\big].
```

**Step 3: `oddrank` from `D`.** For any sorted list `X`,
`oddrank(X)-evensum(X)=D(X)` and `oddrank(X)+evensum(X)=\Sigma(X)`
(pairing/definition, the general — not just sum-`1` — form of the certified
`D-REFORM` identity, same proof: add and divide by `2`). Applying to `B`
(total mass `\Sigma(B)=p_1+\Sigma(T)`, conserved since splitting preserves
sum):
```
oddrank(B) = \tfrac12\big(\Sigma(B)+D(B)\big) = \tfrac12\big(p_1+\Sigma(T)+D(B)\big).
```
∎

## Remark (scope / what is *not* proved here)

**Corrected round 7** (per the round-6 catch-up proof-review, independently
confirmed by a round-7 witness — see `lemmas/partial-dom-residual.md`'s
worked example): the formula above is proved and stated under the
hypothesis `r < t_j` (`r` stays strictly below the smallest element of the
*duplicated prefix block*, `t_j`), **not** the stricter `r<U_1` originally
claimed. This is exactly the hypothesis Step 2's derivation actually uses
(`r` must sit at or after the duplicated block in sorted order, which needs
only `r<t_j=\min$ of the block, not `r<U_1=\max$ of everything beyond the
block — `U_1\le t_j` always, so `r<U_1` is *sufficient* but not necessary).

The hypothesis `r<t_j` holds automatically whenever `j` is chosen maximal
*among `0,\ldots,\min(k,m-1)`* (i.e. `p_1<S_{j+1}=S_j+U_1` forces
`r=p_1-S_j<U_1\le t_j`), but it can **also** hold for a deliberately
**sub-maximal** `j` (chosen, e.g., to leave spare budget for a further
refinement of `r` itself, as in Lemma PARTIAL-DOM-RESIDUAL,
`lemmas/partial-dom-residual.md`) — the round-7 witness there
(`A=(5798,3515,687)/10000`, `j=1` chosen although domination reaches `j=2`)
is a genuine instance of this: `r<t_1` holds even though `j=1` is not
maximal. The certified formula's scope is exactly `r<t_j`, checked directly
on whatever `j` is used, with no further conditions.

If `r\ge t_j` (`r` would land *inside* the duplicated block rather than
after it), the general formula requires the additional "Case 1" analysis
(a straightforward variant of Step 2 above, same technique, `\rho\le 2j`
instead of `>2j`) which was **not** separately written up or verified —
flagged as an easy, low-risk mechanical extension for a future round if
that regime is needed. All numeric verification to date (round 6's 5,000
random trials plus the round-6 and round-7 worked examples) satisfies
`r<t_j`, so the certified formula's scope is exactly as stated above.

## What this does and does not close

**Closes:** an exact, general closed form for the "prefix-tie chain"
family of responses (tie `p_1` down through as much of the tail-prefix as
the budget/domination allows, in one contiguous chain) — strictly
generalizing Lemma DOM (`j=m-1`) to any `j\le\min(k,m-1)`. Confirmed to
reproduce the true numeric optimum exactly on a genuine `m=5` example.

**Does not close:** whether the maximal-prefix-chain response is *always*
optimal. A round-6 counterexample (`A=(0.3374,0.2589,0.242,0.1617)`, `m=4`,
budget `2`) shows it is **not**: the maximal single-piece chain on `p_1`
(`j=1`, tying `p_2`) gives `oddrank=0.5794`, *identical* to the untouched
baseline `oddrank(A)=0.5794` (zero improvement — an even-`m` parity
cancellation, see `universal-adversary-strategy.md`), while the true
optimum `\approx0.5009` is achieved by **two independent, non-adjacent**
single-piece ties (`p_1` ties `p_3`, *not* `p_2`; `p_2` independently ties
`p_4`) — a "matching" between pieces-to-split and tail-targets-to-tie that
is not a single contiguous PARTIAL-DOM chain. This is exactly the open
"matching/assignment" question flagged by the round-6 explorer and left
open by this round's builder; see `universal-adversary-strategy.md` for the
verified numeric confirmation and the precise open status.

## Status
Certified (round 6). The closed-form formula is fully proved (Steps 1-3
above) and independently verified numerically. Its role in closing the
general upper bound is **not** established — see "What this does and does
not close."
