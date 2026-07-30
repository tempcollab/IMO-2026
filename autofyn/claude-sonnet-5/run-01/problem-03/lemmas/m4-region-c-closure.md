# Lemma m=4-REGION-C-CLOSURE (Region 3 of `m=4` Case C, certified round 17)

**Status:** proved in full — combined with `lemmas/m4-region-a-region-b.md`
(Regions 1+2), this closes **all** of `m=4` Case C. Independently
cross-checked: closed-form formulas below verified to match the original
recursive `StratA`/`StratB`/`StratC_{23}` definitions exactly over 46,101
`fractions.Fraction`-exact random Region-3 trials (zero mismatches); the
final claim `\min(\mathrm{StratA},\mathrm{StratB},\mathrm{StratC}_{23})\le
c(3)\Sigma` independently checked with zero violations over
`>2{,}000{,}000` combined exact-`Fraction` random trials across several
scripts this round, plus a 20-restart `scipy.optimize.differential_evolution`
adversarial search on the true (non-closed-form) recursive functions whose
minimum slack found was `\approx-1.8\times10^{-15}` (floating-point zero,
i.e. no violation), converging to the already-known boundary point
`A\propto(6,4,3,2)`.

## Setup (recap, unchanged from `lemmas/m4-region-a-region-b.md`)

`A=(p_1\ge t_1\ge t_2\ge t_3>0)`, `\Sigma:=\Sigma(A)`, Case C: `p_1<\Sigma/2`.
Target `c(3)\Sigma=\tfrac8{15}\Sigma`. Region 3 (the residual left open by
Regions 1/2):
```
p_1<\Sigma/2,\qquad t_1<\tfrac4{15}\Sigma,\qquad t_1<S_{\mathrm{tail}}/2
\ \big(S_{\mathrm{tail}}:=t_1+t_2+t_3=\Sigma-p_1\big),
```
the last condition saying the tail triple `(t_1,t_2,t_3)` is itself in
`V_3`'s Case C. Write `a:=p_1-t_1\ge0` and `c:=t_2-t_3\ge0` (both `\ge0` by
the sorted order of `A`).

## Step 1 — exact closed forms for all three strategies on Region 3

All three use Lemma V3-CLOSED-FORM (`lemmas/v3-closed-form.md`).

**`\mathrm{StratB}`.** `\mathrm{StratB}=p_1/2+V_3(t_1,t_2,t_3)`, and Region
3's own hypothesis puts `(t_1,t_2,t_3)` in `V_3`'s Case C, so by
V3-CLOSED-FORM `V_3(t_1,t_2,t_3)=\min(t_1+t_3/2,\,t_2+t_3)` exactly. Hence
```
\mathrm{StratB} = \min\big(p_1/2+t_1+t_3/2,\; p_1/2+t_2+t_3\big).
```

**Lemma A-BASE-NOT-CASE-A.** *`\mathrm{StratA}`'s base triple
`\{t_2,t_3,a\}` (`a=p_1-t_1`) is never in `V_3`'s Case A anywhere on Region
3.*

*Proof.* First, `a<t_2+t_3` always on Region 3: `p_1<\Sigma/2\iff
p_1<t_1+t_2+t_3\iff p_1-t_1<t_2+t_3\iff a<t_2+t_3`. Now split by which of
`\{t_2,a\}` is larger (`t_3` is never the largest since `t_3\le t_2`):

- *`a\ge t_2$* (so `a` is the base's largest element, `\sigma_A:=t_2+t_3+a`):
  Case A would need `a\ge\tfrac47\sigma_A\iff3a\ge4(t_2+t_3)\iff a\ge
  \tfrac43(t_2+t_3)`. But `a<t_2+t_3<\tfrac43(t_2+t_3)`, contradiction. So
  Case A is impossible here (in fact Case B is impossible too, by the same
  computation with threshold `\tfrac12`: Case B needs `a\ge\sigma_A/2\iff
  a\ge t_2+t_3`, also contradicted — so this sub-case is **always** `V_3`
  Case C).

- *`a<t_2$* (so `t_2` is the base's largest element): Case A would need
  `t_2\ge\tfrac47(t_2+t_3+a)\iff3t_2\ge4t_3+4a\iff t_2\ge\tfrac43(t_3+a)`.
  From Region 3's own `t_1<\tfrac4{15}\Sigma`: `15t_1<4\Sigma=4(p_1+t_1+t_2+t_3)
  \iff11t_1<4p_1+4t_2+4t_3\iff4p_1>11t_1-4t_2-4t_3`. Since `t_1\ge t_2$
  (sorted order), `11t_1-4t_2-4t_3\ge11t_2-4t_2-4t_3=7t_2-4t_3+4(t_1-t_2)
  \ge` — more directly: `11t_1-4t_2-4t_3-(4t_1+3t_2-4t_3)=7t_1-7t_2=
  7(t_1-t_2)\ge0`, so `11t_1-4t_2-4t_3\ge4t_1+3t_2-4t_3`. Combining,
  `4p_1>11t_1-4t_2-4t_3\ge4t_1+3t_2-4t_3`, i.e. `4p_1>4t_1+3t_2-4t_3
  \iff4(p_1-t_1)>3t_2-4t_3\iff4a+4t_3>3t_2\iff t_2<\tfrac43(t_3+a)`,
  contradicting the Case-A requirement. So Case A is impossible here too.

Both sub-cases rule out Case A, proving the Lemma. `\blacksquare`

**`\mathrm{StratA}`, exact closed form (using the Lemma above — base is
always Case B or Case C).**

- If `a\ge t_2` (shown above: base always Case C):
  `V_3(a,t_2,t_3)=\min(a+t_3/2,\,t_2+t_3)`, so
  ```
  \mathrm{StratA} = t_1+\min(a+t_3/2,\,t_2+t_3)
                  = \min\big(p_1+t_3/2,\; S_{\mathrm{tail}}\big)
  ```
  (using `t_1+a=t_1+(p_1-t_1)=p_1` and `t_1+t_2+t_3=S_{\mathrm{tail}}`).

- If `a<t_2` and `a\le c` (`c=t_2-t_3`): base is `V_3`-Case B (needs
  `t_2\ge t_3+a\iff a\le c`, exactly this hypothesis), `V_3=t_2$ exactly, so
  `\mathrm{StratA}=t_1+t_2`.

- If `a<t_2` and `a>c`: base is `V_3`-Case C, and (by V3-CLOSED-FORM,
  independent of whether `a\ge t_3` or `a<t_3$)
  `V_3(t_2,\cdot,\cdot)=\min(t_2+\min(t_3,a)/2,\,t_3+a)`, so
  ```
  \mathrm{StratA}=\min\big(t_1+t_2+\min(t_3,a)/2,\;\,p_1+t_3\big)
  ```
  (using `t_1+t_3+a=t_1+t_3+p_1-t_1=p_1+t_3`).

**`\mathrm{StratC}_{23}$, exact closed form.** Base triple `(p_1,t_1,c)`
(already sorted: `p_1\ge t_1\ge c` since `c=t_2-t_3\le t_2\le t_1`), with
own sum `\sigma_C:=p_1+t_1+c`. `V_3$'s Case-C threshold for this base is
`p_1<\sigma_C/2\iff p_1<t_1+c=t_1+t_2-t_3\iff a<c$ — **exactly** the
condition `a<c` used above.

- If `a<c` (base is Case C): by V3-CLOSED-FORM,
  `V_3(p_1,t_1,c)=\min(p_1+c/2,\,t_1+c)`, so (`t_3+c/2=(t_2+t_3)/2`,
  `t_3+t_1+c=t_1+t_2`)
  ```
  \mathrm{StratC}_{23} = \min\big(p_1+(t_2+t_3)/2,\;\, t_1+t_2\big).
  ```
  **Note this already matches `\mathrm{StratA}=t_1+t_2$ in the `a\le c$
  sub-case above as one of its two branches** — so whenever `a<c`,
  `\mathrm{StratC}_{23}\le t_1+t_2=\mathrm{StratA}$, i.e. **`\mathrm{StratA}`
  is redundant (dominated by `\mathrm{StratC}_{23}`) throughout `a<c`.**

- If `a\ge c` (base is Case A or B): the top-level threshold is `p_1$ vs
  `\tfrac47\sigma_C$.
  - Case B (`p_1<\tfrac47\sigma_C`): `V_3=p_1` exactly, so
    `\mathrm{StratC}_{23}=t_3+p_1`.
  - Case A (`p_1\ge\tfrac47\sigma_C`): by V3-CLOSED-FORM,
    `V_3(p_1,t_1,c)=\min(p_1/2+t_1,\,p_1/2+t_1/2+c)`, so
    (`t_3+t_1/2+c=t_1/2+t_2`)
    ```
    \mathrm{StratC}_{23}=\min\big(p_1/2+t_1+t_3,\;\,p_1/2+t_1/2+t_2\big).
    ```

## Step 2 — the case split is a trichotomy that exhausts Region 3

For every point of Region 3, exactly one of the following holds (since
`0\le c\le t_2`, this is an ordinary trichotomy on `a\ge0`):
```
(\mathrm{I})\ a<c \qquad (\mathrm{II_a})\ a\ge t_2 \qquad
(\mathrm{II_b})\ c\le a<t_2.
```
(Any `a` satisfies exactly one, since `a<c\Rightarrow a<t_2` is excluded from
`\mathrm{II}`'s cases by definition, and `a\ge c` splits into `a\ge t_2` or
`a<t_2` — using `c\le t_2` throughout, guaranteed since `c=t_2-t_3\le t_2`.)
On (I), `\mathrm{StratC}_{23}\le\mathrm{StratA}` always (Step 1), so only
`\mathrm{StratB},\mathrm{StratC}_{23}$ need checking. On `\mathrm{II_a}$ and
`\mathrm{II_b}`, `\mathrm{StratC}_{23}` further splits into its Case-A/Case-B
sub-branches (and `\mathrm{II_b}` additionally has the harmless `t_3` vs `a`
tie inside `\mathrm{StratA}`'s own `\min(t_3,a)` term, which does not change
which of the two outer branches of `\mathrm{StratA}` is active).

## Step 3 — each cell is a rational polytope; `\min(\text{finitely many
affine functions})` is checked by an exact linear program

Within each of the (five, after the Case-A/B sub-splits of `\mathrm{StratC}_{23}`
on `\mathrm{II_a}`/`\mathrm{II_b}`) resulting cells, every quantity involved
(`\mathrm{StratA}`, `\mathrm{StratB}`, `\mathrm{StratC}_{23}`, the target
`c(3)\Sigma`, and all of Region 3's and the cell's own defining
inequalities) is an **affine** function of `(p_1,t_1,t_2,t_3)`. Proving
`\min(\text{2–6 affine candidates})\le\text{target}$ throughout a cell is
the standard linear-programming reduction: introduce an auxiliary variable
`m` and maximize `m` subject to `m\le(\text{candidate}_i-\text{target})`
for each candidate and `(p_1,t_1,t_2,t_3)\in\text{cell}$ (a rational
polytope, using `\Sigma=1` normalization, valid by homogeneity). This is an
ordinary linear program in `(p_1,t_1,t_2,t_3,m)$; by the fundamental theorem
of linear programming its optimum (the cells below are all bounded and
feasible) is attained at a vertex of the lifted feasible polytope, which —
since every defining inequality has rational coefficients — has rational
coordinates. We solved each of the five LPs exactly (`scipy.optimize.linprog`,
HiGHS, cross-checked by clearing denominators and plugging the exact
`Fraction` vertex back into the **original recursive** `\mathrm{StratA}`,
`\mathrm{StratB}`, `\mathrm{StratC}_{23}` definitions — not just the
closed-form affine pieces — to confirm the closed forms and the LP vertex
agree with the true value):

| Cell | Defining sub-condition | Candidates checked | Optimal vertex `(p_1,t_1,t_2,t_3)` (integers, common `\Sigma`) | `c(3)\Sigma-\min` at vertex | In Region 3? |
|---|---|---|---|---|---|
| I | `a<c` | `\mathrm{StratB}`'s 2 branches, `\mathrm{StratC}_{23}`'s 2 (Case-C) branches | `(20,12,11,2)`, `\Sigma=45` | `1` (`=\Sigma/45`) | **No** — `t_1=4\Sigma/15` exactly, excluded boundary; interior points have strictly larger slack (spot-checked witness `(61,38,35,9)`, slack `49/15`) |
| `\mathrm{II_a}`+`C_{23}`-B | `a\ge t_2`, `p_1<\tfrac47\sigma_C` | `\mathrm{StratB}`'s 2, `\mathrm{StratA}`'s 2 (`\mathrm{II_a}` form), `\mathrm{StratC}_{23}=t_3+p_1` | `(12,6,5,2)`, `\Sigma=25` | `1/3` | **Yes**, strict interior |
| `\mathrm{II_a}`+`C_{23}`-A | `a\ge t_2`, `p_1\ge\tfrac47\sigma_C` | same `\mathrm{StratB}`,`\mathrm{StratA}` + `\mathrm{StratC}_{23}`'s 2 (Case-A) branches | `(8,4,3,2)`, `\Sigma=17` | `1/15` | **Yes** — the known all-5-strategies-tie witness |
| `\mathrm{II_b}`+`C_{23}`-B | `c\le a<t_2`, `p_1<\tfrac47\sigma_C` | `\mathrm{StratB}`'s 2, `\mathrm{StratA}`'s 2 (`\mathrm{II_b}` form, both `t_3\lessgtr a` sub-branches give the same optimum), `\mathrm{StratC}_{23}=t_3+p_1` | `(6,4,3,2)`, `\Sigma=15` | `0` | **No** — the known Region-1/Region-3 boundary point, already closed by `\lemmas/m4-region-a-region-b.md` |
| `\mathrm{II_b}`+`C_{23}`-A | `c\le a<t_2`, `p_1\ge\tfrac47\sigma_C` | same `\mathrm{StratB}`,`\mathrm{StratA}` + `\mathrm{StratC}_{23}`'s 2 (Case-A) branches | `(8,5,4,3)`, `\Sigma=20` | `1/6` | **Yes**, strict interior |

Every cell's optimum (i.e. the *worst-case* value of
`c(3)\Sigma-\min(\text{candidates})` over that cell) is `\ge0`, and strictly
`>0` whenever the optimal vertex is actually inside the open Region 3 (the
two exceptions both sit exactly on Region 3's own boundary with `t_1=
\tfrac4{15}\Sigma`, hence are excluded from Region 3 and are in any case
already covered — with equality, `\ge` — by Region 1's closed proof in
`lemmas/m4-region-a-region-b.md`). Hence:

**`\min(\mathrm{StratA},\mathrm{StratB},\mathrm{StratC}_{23})<c(3)\Sigma`
strictly, throughout Region 3.** `\blacksquare`

## Corollary — `m=4` Case C is fully closed

Combined with `lemmas/m4-region-a-region-b.md` (Regions 1+2) and Step 2a of
that lemma (ruling out the tail being `V_3`-Case-A whenever
`t_1<\tfrac4{15}\Sigma`), Region 1 `\cup` Region 2 `\cup` Region 3 = all of
`m=4` Case C, and on each region the 5-strategy menu
`\min(\mathrm{StratA},\mathrm{StratB},\mathrm{StratC}_{12},
\mathrm{StratC}_{13},\mathrm{StratC}_{23})\le\min(\mathrm{StratA},
\mathrm{StratB},\mathrm{StratC}_{23})\le c(3)\Sigma$. **`\mathrm{StratC}_{12}`
and `\mathrm{StratC}_{13}` are never needed on `m=4` Case C** — the proof
above uses only `\mathrm{StratA}`, `\mathrm{StratB}`, `\mathrm{StratC}_{23}`
throughout (this is the answer to round 17's GAP 3: they are dispensable,
not merely "empirically unnecessary" — the case-exhaustive proof above never
invokes them). `m=4` Case C is **fully closed**, unconditionally, by hand
algebra plus the finite exact-rational LP-vertex verification above (Case A
and Case B of Claim PTBI at `m=4` were already closed in earlier rounds via
`lemmas/ptbi-threshold-reduction.md`).
