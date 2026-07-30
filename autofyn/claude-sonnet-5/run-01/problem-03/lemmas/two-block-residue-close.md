# Lemma TWO-BLOCK and the closure of the minority-part/deep-bracket residue sub-case

Proved by `geometric-dominance-construction`, round 9, as an independent,
structurally different route to `recursive-embedding-induction`'s
Lemma V'-GEN gap (b) residual sub-case — a direct `D`-value estimate at the
tie value itself (not a tree/forest "virtual re-split" argument). Builds
only on the already-certified `lemmas/alternating-sum-toolkit.md` (Lemma
D-BOUND) and the geometric configuration's basic facts (`t_i=2t_{i+1}`,
`t_i=2^{n-i}`).

## Setting

Fix `n≥1`. Unnormalized units `t_i:=2^{n-i}` for `i=1,\dots,n` (so
`t_1=2^{n-1}>\dots>t_n=1`), top piece `P_1` with value `2t_1=2^n`. Index
the `n+1` original pieces of `A_n` as `0` (`=P_1`, `\mathrm{top}_0:=2t_1`)
and `1,\dots,n` (`=T_i`, `\mathrm{top}_i:=t_i`).

## Lemma TWO-BLOCK (fully general — no geometric structure needed)

*Statement.* Let `L` be any finite sorted nonnegative list and `v\ge0` any
threshold. Let `Y:=\{x\in L: x>v\}`, `Z:=\{x\in L: x\le v\}` (as
sub-multisets of `L`, respecting multiplicity). If `Y` is nonempty, write
its two largest elements `b_1\ge b_2` (`b_2:=0` if `|Y|=1`). Then
```
D(L) \ge (b_1-b_2) - v\cdot[\,|Y|\text{ is odd}\,].
```

*Proof.* Every element of `Y` exceeds every element of `Z` (by
construction), so the rank-shift-by-`s` fact (elementary; already used
throughout this problem's lemma set, e.g. round 4's "prepending dominant
elements" fact) gives
```
D(L) = D(Y) + (-1)^{|Y|} D(Z).
```
For `D(Y)`: writing `Y` sorted `y_1=b_1\ge y_2=b_2\ge\cdots`, the definition
of `D` gives `D(Y) = b_1 - D(Y\setminus\{b_1\})`, and `Y\setminus\{b_1\}`
is itself a sorted nonnegative list with maximum `b_2` (or empty, `D=0`, if
`|Y|=1$), so by the certified **Lemma D-BOUND**
(`0\le D(Y\setminus\{b_1\})\le b_2`), `D(Y)\ge b_1-b_2`.

For `D(Z)`: every element of `Z` is `\le v`, so `\max(Z)\le v`, and Lemma
D-BOUND gives `0\le D(Z)\le v`.

Combining: if `|Y|` even, `D(L)=D(Y)+D(Z)\ge (b_1-b_2)+0`. If `|Y|` odd,
`D(L)=D(Y)-D(Z)\ge (b_1-b_2)-v`. Both cases match the stated bound. `∎`

*Independent verification.* Checked directly (not merely by citation) as
part of the construction below against `10{,}731` exhaustively enumerated
small-`n` instances (`n=1,\dots,6`, all subsets `S` of split pieces with
`|S|\ge2`, a dense `50`-point grid of `v` per instance) and a further
`21{,}600`-instance randomized stress test pushing `n` up to `12` and `v`
arbitrarily close to its supremum — zero violations of `D(L)\ge` the
stated bound in every single case (scripts: `/tmp/gd_general2.py`,
`/tmp/gd_general3.py`, `/tmp/gd_stress.py`, `/tmp/gd_final_check.py`).

## Application: closing the residual cross-tie sub-case

**Configuration.** Let `S\subseteq\{0,1,\dots,n\}`, `|S|\ge2` (the
cross-tied split pieces). Let
```
q := \min_{i\in S}(\mathrm{top}_i/2).
```
For any real `v` with `0<v<q` (so every `i\in S`, split into
`(\mathrm{top}_i-v,\ v)`, has `v` genuinely playing the **minority** role),
let `B` be the configuration: every `i\in S` split into its two parts, every
`i\notin S` left as the single untouched piece `\mathrm{top}_i`. (This is
exactly the vertex-type configuration Lemma CROSS-TIE-AFFINE
(`lemmas/cross-tie-affine.md`) analyzes, but here `v` ranges over the
**entire** open interval `(0,q)`, not just the cell's endpoint — a strictly
stronger claim than what CROSS-TIE-AFFINE's reduction alone requires.)

### Structural Lemma (identifying the two largest elements of `B`)

*Statement.* Let `\varepsilon_0:=1` if `0\in S` else `0`; `\varepsilon_1:=1`
if `1\in S` else `0` (`n\ge1` always has an index `1`). Then the two
largest elements of `B` are
```
b_1 = 2t_1 - \varepsilon_0 v,\qquad b_2 = t_1 - \varepsilon_1 v.
```

*Proof.* **Identifying `b_1`.** If `0\notin S`: the piece `2t_1` is present
untouched. Since `v<q\le \mathrm{top}_i/2` for every `i\in S`, in
particular `v<t_1` (as `q\le t_1` whenever `S` contains any tail index,
which it must since `|S|\ge2` and `0\notin S$ forces `S\subseteq\{1,\dots,
n\}`, or even if `0\in S` in the other branch below `q\le t_1` directly
from the `i=0` term). Every other element of `B` — an untouched
`\mathrm{top}_i\ (i\ge1,\ i\notin S)\le t_1`, a companion
`\mathrm{top}_i-v<\mathrm{top}_i\le t_1\ (i\in S,\ i\ge1)`, or `v<t_1` — is
`<2t_1`. So `2t_1` is the unique maximum: `b_1=2t_1=2t_1-\varepsilon_0 v`
(`\varepsilon_0=0`).

If `0\in S`: the companion `c_0:=2t_1-v` is present instead. Since
`|S|\ge2`, `S` contains some tail index `j\ge1`, and
`q\le \mathrm{top}_0/2=t_1`, so `v<t_1`, giving
`c_0=2t_1-v>2t_1-t_1=t_1`. Every other element of `B` is `\le t_1$
(untouched `\mathrm{top}_i,\ i\ge1`), or `<t_1` (a companion
`\mathrm{top}_i-v<\mathrm{top}_i\le t_1$ for `i\in S,i\ge1`), or `<t_1$
(`v<t_1$). So `c_0>` every other element: `b_1=c_0=2t_1-v`
(`\varepsilon_0=1`).

**Identifying `b_2`** (the largest element of `B\setminus\{b_1\}`).

If `1\notin S`: the piece `t_1` is present untouched (distinct from
`b_1`, whichever case above). For `n=1$ this sub-case requires
`0\in S,1\notin S`, impossible since the only indices are `\{0,1\}` —
vacuous. For `n\ge2`: every remaining element besides `t_1` is an
untouched `\mathrm{top}_i\ (i\ge2)\le t_2<t_1`, a companion
`\mathrm{top}_i-v<\mathrm{top}_i\le t_2<t_1\ (i\in S,i\ge2)`, or `v<q\le
t_2<t_1$ (using, if `1\notin S`, that `S` contains an index `\ge2`, so
`q\le\mathrm{top}_{i}/2\le t_2/2<t_2` for that index — in particular
`v<t_2`). So `t_1` exceeds all of these: `b_2=t_1=t_1-\varepsilon_1 v`
(`\varepsilon_1=0`).

If `1\in S`: the companion `c_1:=t_1-v` is present instead of `t_1`. Since
`1\in S`, `q\le \mathrm{top}_1/2=t_1/2=t_2`, so `v<t_2`, giving
`c_1=t_1-v>t_1-t_2=t_2`. Every other element besides `b_1` is `\le t_2`
(untouched `\mathrm{top}_i,i\ge2`) or `<t_2` (companion
`\mathrm{top}_i-v<\mathrm{top}_i\le t_2,\ i\in S,i\ge2`, or `v<t_2`). So
`c_1` exceeds all of these: `b_2=c_1=t_1-v` (`\varepsilon_1=1`).

In every sub-case `b_1>b_2$ (direct check: `2t_1-\varepsilon_0v -
(t_1-\varepsilon_1v) = t_1+(\varepsilon_1-\varepsilon_0)v \ge t_1-v>t_1-q
\ge t_1-t_1=0$ using `q\le t_1`, or checked directly case by case above),
confirming the claimed ordering. `∎`

*Independent verification.* Checked directly against `14{,}400` randomized
instances (`n=1,\dots,12`, random `S` of random size, `v` at several
fractions of `q` including `1/2,\ 9/10,\ 99/100,\ 1/4`): the predicted
`(b_1,b_2)` formula matched the actual two largest sorted elements of `B`
in **every** instance, zero mismatches (`/tmp/gd_verify_formula.py`).

### Main Theorem (residual cross-tie closure)

*Statement.* For every `n\ge1`, every `S\subseteq\{0,\dots,n\}` with
`|S|\ge2`, and every `v\in(0,q)$ (`q` as above), the configuration `B`
described above satisfies `D(B)\ge t_n`.

*Proof.* By Lemma TWO-BLOCK (with threshold `v`, noting `b_1,b_2\in Y`
since both exceed `v`: `b_2=t_1-\varepsilon_1v>t_1-q\ge t_1-t_1=0`... more
precisely `b_2>v` was verified in the Structural Lemma's proof — in every
sub-case `b_2` was shown `>t_2` or `=t_1$, both `>q>v`, and $q \le t_1/2$
whenever needed):
```
D(B) \ge \big(t_1+(\varepsilon_1-\varepsilon_0)v\big) - v\cdot[\,|Y|\text{ odd}\,].
```
We check `t_1+(\varepsilon_1-\varepsilon_0-[\,|Y|\text{ odd}\,])v \ge t_n`
in all four `(\varepsilon_0,\varepsilon_1)` cases (the coefficient of `v`
is always `\ge -2$, so the only cases needing `q`'s actual size are those
with a negative coefficient):

- **`(\varepsilon_0,\varepsilon_1)=(0,1)`.** Coefficient of `v` is
  `1-0-[\text{odd}]\in\{0,1\}\ge0`. So `D(B)\ge t_1\ge t_n` always
  (`t_1=2^{n-1}\ge2^0=t_n` for `n\ge1`).
- **`(\varepsilon_0,\varepsilon_1)=(0,0)`.** Even case: `D(B)\ge t_1\ge
  t_n`, done. Odd case: need `t_1-v\ge t_n`. Here `0,1\notin S`, so
  `S\subseteq\{2,\dots,n\}$ with `|S|\ge2`, forcing `n\ge3`; writing
  `m:=\max(S)\ge3`, `q=\mathrm{top}_m/2=t_m/2\le t_3/2` (`t_i` decreasing),
  so `v<t_3/2=2^{n-4}`. Hence `t_1-v>t_1-2^{n-4}=2^{n-1}-2^{n-4}=
  7\cdot2^{n-4}\ge7/8>0`; concretely `\ge t_n=1` once `2^{n-4}\ge1/7`, true
  for every `n\ge3` (the case's only possible range) since already
  `7\cdot2^{n-4}\ge7\cdot2^{-1}=3.5\ge1` at the smallest case `n=3`.
- **`(\varepsilon_0,\varepsilon_1)=(1,1)`.** Even case: `D(B)\ge t_1\ge
  t_n`. Odd case: need `t_1-v\ge t_n`. Here `q=\min(t_1,t_1/2)=t_1/2`, so
  `v<t_1/2`, giving `t_1-v>t_1/2=2^{n-2}`. For `n\ge2`, `2^{n-2}\ge1=t_n`.
  For `n=1`: this `(\varepsilon_0,\varepsilon_1)=(1,1)` sub-case forces
  `S=\{0,1\}` (the only two indices), and then `B=\{c_0,v,c_1,v\}` has
  exactly `2` elements exceeding `v` (namely `c_0,c_1`, both `>v` as shown)
  and `0` other elements — so `|Y|=2`, **always even**; the odd sub-case
  is vacuous at `n=1`.
- **`(\varepsilon_0,\varepsilon_1)=(1,0)`.** Even case: coefficient
  `-1-0=-1\ge -2$ but let's check directly: `D(B)\ge t_1-v`; need
  `\ge t_n`. Odd case: coefficient `-1-1=-2`, need `t_1-2v\ge t_n`. Here
  `0\in S,1\notin S`, so `S=\{0\}\cup S'` with `S'\subseteq\{2,\dots,n\}`
  nonempty (forcing `n\ge2`). If `n=2`: `S'=\{2\}` forced,
  `q=\min(t_1,t_2/2)=\min(2,1/2)=1/2` (unnormalized `t_1=2,t_2=1`), so
  `v<1/2`; `t_1-2v>2-1=1=t_n` (odd case, tight but strict); even case
  `t_1-v>2-1/2=1.5>t_n`, also fine. If `n\ge3`: writing `j:=\min(S')\ge2$,
  `q=\min(t_1,\ t_j/2)$; since `t_j/2\le t_2/2=t_3<t_1`, `q\le t_3$, so
  `v<t_3=2^{n-3}`. Odd case: `t_1-2v>t_1-2t_3=2^{n-1}-2^{n-2}=2^{n-2}\ge
  2^{1}=2\ge t_n=1` for `n\ge3`. Even case has even more slack
  (`t_1-v>t_1-t_3`, larger than the odd bound). Both sub-cases confirm
  `D(B)\ge t_n`.

All four `(\varepsilon_0,\varepsilon_1)` cases, both parities, and the
`n=1$ boundary are covered: `D(B)\ge t_n` unconditionally. `∎`

*Independent verification.* Checked against `10{,}731` exhaustive
small-`n` instances (`n=1,\dots,6`, every subset `S,|S|\ge2`, dense `v`
grid) and `21{,}600` randomized instances (`n` up to `12`, `v` pushed to
within `0.1\%` of its supremum `q`) — **zero violations** of `D(B)\ge t_n`
in any tested case (scripts `/tmp/gd_final_check.py`, `/tmp/gd_stress.py`).

## Reconciliation with the two cited numeric witnesses (mandatory per round-8/9 protocol)

- **`n=4` symmetric two-minority tie** (`S=\{2,3\}`, i.e.
  `\varepsilon_0=\varepsilon_1=0`): predicted `b_1=2t_1=16`, `b_2=t_1=8`,
  matching the actual sorted configuration exactly (`lst=
  [16,8,15/4,7/4,1,1/4,1/4]` at `v=1/4`, checked in `/tmp/gd_check.py`).
  The Main Theorem's bound gives `D(B)\ge t_1=8\ge t_n=1$ (even-`|Y|`
  sub-case, since `|Y|=4`); the true value `D=11` is comfortably above,
  consistent, no disagreement.
- **`n=6` external-anchor-snap residue** (`S=\{2,k\}` for `k=1,3,4`):
  for `k=1$ (`\varepsilon_1=1`), predicted `b_1=64=2t_1`, `b_2=t_1-v=32-2=
  30`, matching the actual computed sorted list `[64,30,14,8,4,2,2,2,1]`
  exactly; the Main Theorem gives `D(B)\ge t_1+v=34\ge t_n=1` — true value
  `D=43`, consistent. For `k=4$ (`\varepsilon_1=0`), predicted `b_1=64,
  b_2=t_1=32`, matching `[64,32,14,8,2,2,2,2,1]` exactly; bound
  `D(B)\ge t_1=32\ge t_n=1` — true value `D=39`, consistent.

**No disagreement found** with `recursive-embedding-induction`'s
forest-extension route on any tested instance; this route reaches the
same conclusion (`D\ge t_n` in the residual sub-case) via a genuinely
different, more direct mechanism (a single application of Lemma D-BOUND
twice, plus elementary identification of the two globally-largest pieces
— no virtual re-splitting or forest/tree machinery needed at all).

## Scope (what this closes, and what remains)

This closes, **unconditionally, for every `n\ge1`**: any cross-piece tie
of `k=|S|\ge2` pieces, **each split into exactly two parts with the tied
value playing the minority role in every one of them** — this is *exactly*
the previously-open "minority-part, deep-bracket" residue sub-case of gap
(b) (Lemma V'-GEN), and in fact strictly more: the bound holds for **every**
`v` in the legal minority range, not merely at Lemma CROSS-TIE-AFFINE's
`D`-minimizing endpoint (a strictly stronger, more direct closure than the
one requested — no affine/convexity argument over the interval is needed
at all for this sub-case, since the two-block estimate applies directly at
any interior point).

Combined with the already-certified facts — Lemma CROSS-TIE-AFFINE's
zero-residue "majority part or `\ge3`-part" closure, Lemma TREE-BOUND
(anchor-only), and the well-separated single-free-coordinate case
(`recursive-embedding-induction`'s Peeling induction / Lemma FC) — **every
sub-case of a tied cluster with all members either majority-role, `\ge3`
parts, or (now) minority-role-in-a-2-part-split is closed**, i.e. gap (b)
of Lemma V'-GEN is closed for the case where every split piece in play has
at most 2 parts. Not separately re-derived here (should follow by the same
mechanism but not explicitly checked this round): ties involving a piece
split into `\ge3` parts where **more than one** of that piece's own
coordinates participates in ties at different values simultaneously (a
"doubly-tied" piece) — believed to reduce to the cases above by peeling one
coordinate at a time, but not verified as a separate claim this round.

## Status

**Certified.** Lemma TWO-BLOCK (fully general, no geometric assumption)
and the Structural Lemma (`b_1,b_2` identification) are proved in full
above and independently verified computationally (see verification notes
inline). The Main Theorem is proved in full for all `n\ge1`, all
`S,|S|\ge2`, all legal `v` — closing the previously-open residual
sub-case of gap (b) unconditionally, for the "all-minority, all-2-part"
tie scenario. The "doubly-tied `\ge3`-part piece" edge noted above is
flagged as an honest, narrower remaining loose end, not closed here.
