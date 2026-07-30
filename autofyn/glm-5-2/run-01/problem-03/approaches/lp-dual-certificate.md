# Approach: lp-dual-certificate (LP / Farkas-dual lower bound)

Whole-problem target: `c(n) = 2^n/(2^{n+1}−1)`, lower-bound side. Liu plays the
dyadic tower `T_n = (2^n, 2^{n−1}, …, 2, 1)` (tower units, total
`D_n = 2^{n+1}−1`); the lower bound is `D ≥ 1` (tower units) against every
Xiang refinement using `≤ n` marks, i.e. Liu guarantees `≥ 2^n/D_n`.

This is a **4th, genuinely-orthogonal LOWER-bound framing.** It certifies `D ≥ 1`
per combinatorial type from the **constraint structure** of Xiang's refinement-min LP
(bin-sum equalities + sort order), via **LP strong duality / Farkas
separating-hyperplane**. The certificate is a *shadow-price sign-pattern on the tower
bins*, a signed tower-value sum — it never evaluates the leftover's global
position-sign (the exact primal obstruction the three converged framings
`tail-count` / `tower-induction` / `gaps-leftover` share).

---

## Status
partial

## Approaches tried
- (round 4, NEW) LP/Farkas-dual lower-bound framing. **GAP-LP1 (clean types) PROVED
  for all `n`, both parities of `m`** — certified `lp-dual-clean-types`. **SIGN
  ERROR in LP-2** (mountain direction flipped, equality used instead of inequality,
  wrong parity in the narrow sub-class); GAP-LP2 open.
- (round 5, REVISE) **LP-2 SIGN ERROR FIXED.** The corrected dual is the
  **inequality** `m_j − m_{j-1} ≤ d_j` with `d_j = (−1)^j − y_eq[b(j)]`, a nonneg
  mountain `m_k = −y_ub[k] ≥ 0` (so `y_ub ≤ 0`, NOT `≥ 0`) with sentinels
  `m_{−1} = m_{m−1} = 0`, and **slack** `s_j = d_j − (m_j − m_{j−1}) ≥ 0` with
  `s_j·p_j = 0` (complementary slackness — the round-4 *equality* is valid only at
  interior points `p_j > 0`; at a breakpoint vertex with `p_j = 0` the constraint is
  slack). Verified by `scipy.optimize.linprog` strong-duality checks: in every tested
  type (n=2..5, 1200+ LPs) the scipy dual marginals satisfy the corrected convention
  and `dual obj = primal min D` (round-4's claimed cert objective 2 > actual min 1
  violated weak duality — confirming the old derivation was wrong). **The round-4
  infeasible T_2 demo CORRECTED:** under the corrected inequality the *uniform* cert
  `y_eq=(+1,−1,−1), y_ub=0` IS feasible for that type (d=`(0,0,0,0,2)`, mountain
  `m=0`, slack `s_4=2` at the `p_4=0` vertex), objective `1 = primal min`; the
  round-4 *claimed* cert `y_eq=(+1,−1,0)` (objective 2) is correctly INFEASIBLE.
  **Narrow interleaved sub-class parity FIXED:** the single-adjacent-2-piece
  interleaving cert works for `k` **EVEN** (0-based), with a single-bump mountain
  `m_k = 1` (round-4 had `k` odd, the opposite). **GAP-LP2 reframed** as the
  LP-feasibility witness of the spine sign-pattern lemma: by strong duality,
  "a feasible dual cert with objective `≥ 1` exists for type `τ`" `⟺` "min `D ≥ 1`
  on cell `τ`" `⟺` (over all `τ`) the spine sign-pattern lemma (= G1). **Integrality
  shortcut attempted and FAILED:** the per-type LP is NOT totally unimodular —
  `min D` is real, not integer (e.g. n=3 type gives `min D = 5/3`, n=4 gives `13/3`,
  `29/3`, verified scipy). The odd-total-mass parity argument rules out only
  `min D = 0` (D=0 forces all-adjacent-equal-pairs + trailing 0 ⇒ even total mass,
  contradicting `D_n` odd) — rigorous but **insufficient** (does not rule out
  `min D ∈ (0,1)` since `min D` is real). GAP-LP2 remains OPEN, honestly
  G1-equivalent by strong duality (not a shortcut).

## Current best
**Proved and certified (intact from round 4):** the per-type LP formalization
(Lemma LP-0); the primal bounded below `D ≥ 0` (Lemma LP-1); **the clean-types
lower bound `min D ≥ 1` for all `n`** (Lemma LP-3 = GAP-LP1, certified
`lp-dual-clean-types` — UNAFFECTED by the sign error since `y_ub = 0` makes the
sign convention irrelevant). **Corrected this round (round 5):** Lemma LP-2 — the
corrected dual derivation with the inequality `m_j − m_{j-1} ≤ d_j`,
nonneg-mountain `m ≥ 0` (so `y_ub ≤ 0`), sentinel-0, complementary-slack slack
where `p_j = 0`; scipy-verified (strong duality `dual obj = primal min` on all
tested types). Narrow interleaved sub-class (single adjacent 2-piece interleaving
at even `k`, rest clean) PROVED with the single-bump mountain. **Open gap
(GAP-LP2):** the structural sign-pattern feasibility lemma for general interleaved
types — reframed as the LP-feasibility witness of the spine sign-pattern lemma,
G1-equivalent by strong duality (NOT a shortcut). The integrality route was a
serious attempt and is recorded as FAILED (min D real); the parity argument is a
rigorous sub-result ruling out `min D = 0` only.

---

## Full proof (partial — GAP-LP2 open)

### 0. Setup and the claim-game-dual non-circularity

Let `T_n = (2^n, 2^{n−1}, …, 2, 1)` in tower units (total `D_n = 2^{n+1}−1`). A
Xiang refinement using `≤ n` marks turns `T_n` into a sorted multiset
`p_0 ≥ p_1 ≥ … ≥ p_{m−1} ≥ 0` (0-based; sign of position `k` in the alternating sum is
`(−1)^k`, so the largest piece is at sign `+`). The margin (Liu's advantage in tower
units) is
$$D(p) \;=\; \sum_{k=0}^{m-1} (-1)^k\, p_k .$$
The lower-bound target is `min D ≥ 1` over all `≤ n`-mark refinements.

**Non-circularity (distinguish from the round-3 claim-game-dual dismissal).** The
round-3 alt-framing dismissed an "F4 LP saddle" as circular: that dual lived on the
**alternate-pick claim game**, with weights `w_i` on the *pieces* satisfying
`w_1 ≥ 1, w_i + w_{i+1} ≥ 1, w_i ≥ 0`; there `Σ w_i p_i` is *by construction* the
odd-index sum (the thing being bounded), so "every feasible `w` gives `Σ w_i p_i ≥ v_n`"
IS the statement "odd-index `≥ v_n`" — a re-derivation, not a certificate. **The
LP-dual here is different.** It is the dual of **Xiang's refinement-min LP** (per
combinatorial type), whose dual variables are shadow prices on the **bin-sum equality
constraints** (one per tower piece `t`, weight on the tower value `2^{n−t}`) and on the
**sort-order inequalities**. The dual objective
`Σ_t y_eq[t]·2^{n−t}` is a **signed tower-value sum** — it depends only on the tower
piece *values*, never on the sorted positions of the fragments. It does not re-derive
the odd-index sum; it certifies a lower bound on Xiang's min from the constraint
structure. The round-3 dismissal does not apply.

### 1. Lemma LP-0 (per-type LP is exact)

Fix a **combinatorial type** of a refinement of `T_n`: a bin assignment
`b: {0,…,m−1} → {0,…,n}` (which tower piece `t`, value `V_t = 2^{n−t}`, spawned sorted
piece `k`) together with the sort order `p_0 ≥ p_1 ≥ … ≥ p_{m−1} ≥ 0`. Consider the
**bin-partition LP** on the open type-cell:

$$
\begin{aligned}
\min\ & \textstyle D(p)=\sum_{k=0}^{m-1}(-1)^k p_k \\
\text{s.t.}\ & \textstyle\sum_{k:\,b(k)=t} p_k = 2^{n-t}
&& \text{for each nonempty bin } t \in \{0,\dots,n\}, \\
& p_k \ge p_{k+1}, \quad p_k \ge 0, && k=0,\dots,m-2 .
\end{aligned}
$$

**Claim.** The feasible region of this LP is exactly the type-cell (the set of sorted
fragment-length vectors realizable by a `≤ n`-mark refinement of `T_n` with bin
assignment `b` and sort order as fixed). Hence the LP is **exact** (not a relaxation):
`min` of `D` over the LP = `min` of `D` over the type-cell.

**Proof.** (⊆) Every refinement with bin assignment `b` and the given sort order
produces a vector `p` satisfying the bin-sum equalities (each tower piece `t` of value
`2^{n−t}` is partitioned into its spawned fragments, which sum to `2^{n−t}`) and the
sort order; so it is LP-feasible. (⊇) Conversely, any LP-feasible `p` gives, for each
tower piece `t`, a composition of `2^{n−t}` into `|b^{−1}(t)|` nonnegative parts (the
sort + nonnegativity; a zero part is the degenerate "no further mark" boundary point,
included per `pl-breakpoint-minimum`). Any composition of a stick of length `L` into
`r ≥ 1` positive parts is realizable as a split tree (split off one piece at a time, in
any order). Composing across bins gives a valid `≤ n`-mark refinement of `T_n` (the
number of marks is `m − (n+1) ≤ n`, since each mark increases the piece count by exactly
1 and `T_n` starts with `n+1` pieces). ∎

**Reduction to type cells (import `pl-breakpoint-minimum`).** By the certified lemma
`pl-breakpoint-minimum`, the global minimum of `D` over all `≤ n`-mark refinements of
`T_n` is attained at a breakpoint (tie) configuration, i.e. at a vertex of some
type-polytope. The global min is therefore the minimum, over finitely many
combinatorial types, of the per-type LP optimum. So certifying `min-cell D ≥ 1` for
every type certifies the global `min D ≥ 1`.

### 2. Lemma LP-1 (primal bounded below; strong duality applies)

**Claim.** On the feasible region of the per-type LP, `D ≥ 0`. In particular the primal
is feasible and bounded below, so LP strong duality holds: `min D = max (dual objective)`.

**Proof.** Every feasible `p` is sorted descending and nonnegative:
`p_0 ≥ p_1 ≥ … ≥ p_{m−1} ≥ 0`. By the certified `gaps-leftover-identity`,
$$D = \sum_{k=0}^{\lfloor m/2\rfloor -1} (p_{2k}-p_{2k+1}) \;+\; \mathbf 1_{m\text{ odd}}\cdot p_{m-1},$$
(0-based; the pairs `(p_{2k}, p_{2k+1})` telescope, with the lone `+p_{m−1}` when `m`
is odd). Each pair `p_{2k} − p_{2k+1} ≥ 0` (sorted), and `p_{m−1} ≥ 0`; hence `D ≥ 0`.
This holds for **both** parities of `m` (the phantom-zero padding of
`gaps-leftover-identity` covers even `m`). Feasibility is given by the actual
refinement (Lemma LP-0). A feasible, bounded-below LP satisfies LP strong duality
(the strong-duality theorem for LPs; no Slater/interiority condition is needed in the
polyhedral case — see e.g. the LP strong-duality / von-Neumann-duality entry referenced
in `knowledge_base.md` §Linear Algebra / LP). ∎

### 3. Lemma LP-2 (the dual — CORRECTED, round 5)

Write the per-type LP in standard inequality form
$$\min\, c^\top p,\quad A_{\text{eq}}\, p = b_{\text{eq}},\quad A_{\text{ub}}\, p \le 0,\quad p\ge 0,$$
with `c_k = (−1)^k`; `A_eq` = bin-sum indicator rows (one `1` per column, in the row of
its bin `b(k)`), `b_eq[t] = 2^{n−t}`; `A_ub` = sort rows `(-e_k + e_{k+1})^\top` for
`k = 0,…,m−2` (encoding `p_{k+1} − p_k ≤ 0`, i.e. `p_k ≥ p_{k+1}`), `b_ub = 0`.

**The LP dual (standard form; verified by `scipy.optimize.linprog` marginals).** Dual
variables: `y_eq[t]` (free, one per nonempty bin-sum equality) and `y_ub[k]` (one per
sort inequality, `k = 0,…,m−2`). For a **minimization** primal with inequality
constraints `A_ub p ≤ 0`, the dual variable satisfies **`y_ub[k] ≤ 0`** (this is the
sign the round-4 derivation got backwards). The dual is

$$
\max\ \textstyle \Phi(y) = \sum_{t}\, y_{\text{eq}}[t]\cdot 2^{n-t}
\quad\text{s.t.}\quad
(A_{\text{eq}}^\top y_{\text{eq}})_j + (A_{\text{ub}}^\top y_{\text{ub}})_j \;\le\; c_j = (-1)^j
\ \ \forall j,\quad y_{\text{ub}}[k]\le 0,\ \ y_{\text{eq}}[t]\ \text{free}.
$$

**(A_eq^⊤ y_eq)_j = y_eq[b(j)]** (piece `j`'s bin). For **(A_ub^⊤ y_ub)_j**: column `j`
of `A_ub` has `+1` in row `j−1` (if `j ≥ 1`) and `−1` in row `j` (if `j ≤ m−2`); hence

$$(A_{\text{ub}}^\top y_{\text{ub}})_j =
\begin{cases} -y_{\text{ub}}[0] & j=0,\\
y_{\text{ub}}[j-1]-y_{\text{ub}}[j] & 1\le j\le m-2,\\
y_{\text{ub}}[m-2] & j=m-1.\end{cases}$$

Introduce the **nonneg mountain** `m_k := −y_ub[k] ≥ 0` for `k = 0,…,m−2`, with
**sentinels** `m_{−1} := 0` and `m_{m−1} := 0` (notation for the telescoping at the
free ends — `m_{m−1}` is *not* a variable, it encodes that there is no sort constraint
beyond `k = m−2`). Then `(A_ub^⊤ y_ub)_j = m_j − m_{j−1}` for every `j = 0,…,m−1`.
Define the increments

$$d_j \;:=\; (-1)^j - y_{\text{eq}}[b(j)].$$

(Round 4 wrote `d_k = y_eq[b(k)] − (−1)^k` — the **negated** sign; this is the
sign error.) The dual constraint becomes the **inequality**

$$
\boxed{\,m_j - m_{j-1} \;\le\; d_j \;=\; (-1)^j - y_{\text{eq}}[b(j)],\qquad
j = 0,\dots,m-1,\,}
\tag{★}
$$

with `m_k ≥ 0` (`k = 0,…,m−2`), sentinels `m_{−1} = m_{m−1} = 0`. The **dual
objective** is

$$\Phi(y) \;=\; \sum_{t}\, y_{\text{eq}}[t]\cdot 2^{n-t},$$

a **signed tower-value sum**, and LP strong duality (Lemma LP-1) gives

$$\max\{\Phi : \text{(★) feasible}\} \;=\; \min D \quad\text{(on the type-cell).}$$

**Complementary slackness.** The slack `s_j := d_j − (m_j − m_{j−1}) ≥ 0` satisfies
`s_j · p_j = 0`: the constraint (★) is **tight** wherever `p_j > 0` (interior of the
type-cell) and **slack** wherever `p_j = 0` (a degenerate boundary vertex — exactly the
breakpoints of `pl-breakpoint-minimum`). Round 4 used **equality** `m_j − m_{j−1} = d_j`,
which is valid only at interior points; at a breakpoint vertex (where the LP optimum
actually lives, by `pl-breakpoint-minimum`) the equality is false and the inequality is
essential. This is why the round-4 "mountain closes to 0 at `m−1`" condition was an
artifact: with the inequality, telescoping gives only the **necessary** condition
`Σ_j d_j ≥ 0` (since `Σ_j (m_j − m_{j−1}) = m_{m−1} − m_{−1} = 0 ≤ Σ_j d_j`), not
equality.

**Scipy strong-duality verification (verification, not proof).** For every type
tested (n = 2..5, 1200+ LPs incl. all interleaved wall types), `scipy.optimize.linprog`
returns dual marginals `y_eq, y_ub` with `y_ub ≤ 0` (so `m ≥ 0`), satisfying (★) as an
inequality with slack exactly where `p_j = 0`, and `dual obj = primal min D`
(strong duality). The round-4 claimed T_2 cert `y_eq = (+1,−1,0)` (objective 2) is
correctly **infeasible** under (★) (it would violate weak duality since `primal min = 1`);
the *uniform* cert `y_eq = (+1,−1,−1), y_ub = 0` is feasible (d = `(0,0,0,0,2)`, mountain
`m = 0`, slack `s_4 = 2` at the `p_4 = 0` vertex), objective `1 = primal min`.
`/tmp/round-5/lp_sign_verify.py`, `lp_interleaved_verify.py`, `subclass_verify2.py`.

**Integrality caveat (round 5, recorded as a FAILED shortcut).** A tempting route is:
*if the per-type LP is totally unimodular (TU), then `min D` is an integer, and the
odd-total-mass parity argument (below, §5b) rules out `min D = 0`, giving `min D ≥ 1`.*
This **fails**: the LP is **not** TU. Verified by scipy: `min D` takes non-integer
values such as `5/3` (n=3), `13/3`, `29/3` (n=4), `7/3`, `17/3` (n=5). The parity
argument is rigorous but rules out **only `min D = 0`**, not `min D ∈ (0,1)`; since
`min D` is real, this is insufficient for G1. Recorded here so no future round
re-attempts the TU shortcut.

### 4. Lemma LP-3 (GAP-LP1 — clean types, PROVED, all n) ⟹ certified `lp-dual-clean-types`

Call a combinatorial type **clean** if every bin's pieces all sit at positions of a
single parity (each bin is monochromatic in `(−1)^k`). For a clean type, set
$$y_{\text{ub}} \equiv 0, \qquad y_{\text{eq}}[t] := (\text{the common parity } s_t \in\{+1,-1\} \text{ of bin } t).$$
(If bin `t` is nonempty, all its pieces share parity `s_t`, so `y_eq[t]` is
well-defined; empty bins are unconstrained and we set `y_eq[t]=0`.)

**Feasibility (under the corrected inequality ★).** Stationarity: at every position
`j`, `d_j = (−1)^j − y_eq[b(j)] = (−1)^j − s_{b(j)} = 0`, because bin `b(j)` is clean
and piece `j` is one of its pieces, hence `(−1)^j = s_{b(j)}`. With `y_ub ≡ 0` the
mountain is `m ≡ 0`, so `m_j − m_{j−1} = 0 ≤ d_j = 0` — (★) holds with **equality**
(slack `s_j = 0`, tight everywhere — valid since clean-type certificates are tight at
every `p_j > 0`). The cert is feasible. ∎

*(The sign correction in LP-2 does NOT affect LP-3: with `y_ub ≡ 0` the sign of `y_ub`
and the equality-vs-inequality distinction are both irrelevant — `m ≡ 0` makes (★) the
tautology `0 ≤ 0` regardless. GAP-LP1 stands certified, intact.)*

**The top bin is at `+1` parity.** We show `s_0 = +1` (top bin, value `2^n`, at
`(−1)^k = +1` positions). Suppose for contradiction `s_0 = −1`: every top-bin
fragment sits at a `(−1)^k = −1` position (even 0-based index), so the `+1`-positions
contain **only non-top pieces**. By the bin-sum equalities the total non-top mass is
`Σ_{t≥1} 2^{n−t} = 2^n − 1`, while the top bin alone has mass `2^n`. Hence on this
cell
$$D \;=\; (\text{mass at }{+}1\text{-positions}) - (\text{mass at }{-}1\text{-positions})
\;\le\; (2^n-1) - 2^n \;=\; -1 \;<\; 0,$$
contradicting `D ≥ 0` (Lemma LP-1). So the cell is empty unless `s_0 = +1`. A clean
type arising from a real refinement has `s_0 = +1`. ∎

**Objective `≥ 1` (dyadic dominance).** With `s_0 = +1` and `s_t ∈ {±1}` for `t ≥ 1`,
$$\Phi \;=\; 2^n + \sum_{t\ge 1} s_t\, 2^{n-t}
\;\ge\; 2^n - \sum_{t\ge 1} 2^{n-t}
\;=\; 2^n - (2^n - 1) \;=\; 1,$$
since `Σ_{t≥1} 2^{n−t} = 2^n − 1` (geometric series; the strict dominance
`2^n > 2^n − 1`, the *same* tower-dominance used in `tower-top-unsplit` and
`even-group-spine-lower-bound`, here in dual form). ∎

**Conclusion (LP-3).** For every clean type of a refinement of `T_n`, the dual cert
`y_ub = 0, y_eq[t] = s_t` is feasible with objective `Φ ≥ 1`. By LP strong duality
(Lemma LP-1), `min D ≥ 1` on the cell. By `pl-breakpoint-minimum` (the global min is a
min over type cells), `D ≥ 1` at every clean-type breakpoint. This **closes the
clean-types sub-case of G1 for all `n`**, both parities of `m`. ∎

**Note on scope.** "Clean" is a genuine but restricted sub-class: it requires each bin
monochromatic in parity. The strict uniform cert `y_eq = (1,−1,…,−1)` (top `+1`, all
others `−1`) is the *special* clean type where additionally every non-top bin is at
`−1` parity; its boundary condition `#(top-bin pieces) = (m+1)/2` (odd `m`) is the
pigeonhole gate. Lemma LP-3 is strictly broader: it allows non-top bins at either
parity, and the dominance still gives `Φ ≥ 1`.

---

### 5. GAP-LP2 (interleaved types — the G1-equivalent OPEN crux, REFRAMED round 5)

A type is **interleaved** if some bin has pieces at both parities. The clean cert
(`y_ub = 0`) is then *generically* infeasible (at least one `d_j ≠ 0`); scipy confirms
the uniform cert is infeasible on a positive fraction of interleaved types (e.g. the
n=2 type `b = (0,0,1,2,1)`, the n=3 type `b = (0,0,1,2,1,3)`), though it is feasible on
others (e.g. the round-4 demo `b = (0,1,0,2,2)`, where the `p_4 = 0` vertex supplies
slack). A **family** of sign-patterns is required, not one uniform cert (verified: the
uniform cert covers only a minority of interleaved types; the optimal `y_eq` varies by
type — `{(+1,−1,−1), (0,1,−1), (0,1,−1,−1), (+1,−1,−1,+1), …}` across the sample).

#### 5a. The structural lemma (= the spine sign-pattern lemma, in LP language)

**GAP-LP2 (structural sign-pattern feasibility).** *For every combinatorial type `τ`
of a `≤ n`-mark refinement of `T_n`, there exists an assignment
`y_eq: {bins} → ℝ` and a nonneg mountain `m` (sentinels `m_{−1}=m_{m−1}=0`) satisfying
the inequality (★) `m_j − m_{j−1} ≤ (−1)^j − y_eq[b(j)]`, with objective
`Φ = Σ_t y_eq[t]·2^{n−t} ≥ 1`.*

**Equivalence to the spine sign-pattern lemma (and hence to G1) — honest, by strong
duality.** By LP strong duality (Lemma LP-1), `max{Φ : (★) feasible} = min D` on the
cell. Therefore

> "a feasible cert with `Φ ≥ 1` exists for type `τ`" `⟺` "`min D ≥ 1` on cell `τ`"
> `⟺` (min over all `τ`) the **G1** claim `min D ≥ 1` for every refinement.

The nosaddle-close explorer (round 5) established that the COMBINATORIAL shadow of
this fact at a `D = 1` breakpoint is the **spine sign-pattern lemma**: at every
`D = 1` breakpoint, the spine (after `spine-pair-cancellation` S1) interleaves as
`(fragment, tower, fragment, tower, …)` with all fragments at `+` (odd spine-index)
and all tower-valued pieces at `−` (even spine-index), so that
`D(spine) = (Σ fragments) − (Σ towers) = 1` by the telescoping mass identity
(`F = T + 1`, from `D_n` odd). The dual certificate `y_eq` is the LP-shadow of this
spine sign assignment; the dual objective `(Σ fragments) − (Σ towers)` is the signed
tower-value sum certified by (★). GAP-LP2 and the spine sign-pattern lemma are the
**same fact** in two languages — LP-feasibility vs combinatorial subset-sum. **This is
NOT a shortcut**: by `min primal = max dual`, "dual `≥ 1`" is *equivalent* to "primal
`≥ 1`," not a weakening. The value of the dual framing is a **rival PROOF MECHANISM**
(LP feasibility / Farkas separating-hyperplane) for the same closing lemma that
`tail-count` attacks via combinatorial multi-swap subset-sum; if one stalls, the other
may succeed.

#### 5b. A rigorous sub-result: `min D = 0` is infeasible (parity / odd total mass)

**Lemma (parity).** *On any type-cell of a refinement of `T_n`, `D = 0` is
infeasible. Hence `min D ≠ 0`; combined with `min D ≥ 0` (LP-1), `min D > 0`.*

**Proof.** By `gaps-leftover-identity`, `D = Σ_k (p_{2k} − p_{2k+1}) + [m odd]·p_{m−1}`,
with every term `≥ 0` (sorted + nonneg). So `D = 0` forces every term `= 0`:
`p_{2k} = p_{2k+1}` for all `k` *and* (if `m` odd) `p_{m−1} = 0`. The sorted multiset
is then entirely adjacent-equal pairs `(v_0,v_0),(v_1,v_1),…` plus an optional trailing
`0`. The total mass is `2(v_0 + v_1 + …) [+ 0]` — an **even** real number. But the
total mass is the bin-sum total `D_n = 2^{n+1} − 1`, which is **odd**. Contradiction.
So no feasible `p` has `D = 0`. ∎

*(This is rigorous and n-independent. It does NOT close GAP-LP2: `min D` is real, not
integer — the per-type LP is not TU, see §3 integrality caveat — so ruling out `0`
does not rule out `min D ∈ (0,1)`. The parity lemma is a genuine sub-result: it shows
`max Φ > 0` strictly, i.e. a cert with **strictly positive** objective always exists.
To promote "positive" to "≥ 1" requires the full spine sign-pattern lemma = G1.)*

#### 5c. Attempt via Farkas (the LP-feasibility mechanism) — HONESTLY circular

The Farkas/separating-hyperplane attempt: suppose for some type `τ` no feasible cert
with `Φ ≥ 1` exists. By strong duality, `max Φ < 1` on `τ`, i.e. `min D < 1` on the
cell — a primal feasible `p` with `D < 1`. To contradict this we would need an
independent proof that `D ≥ 1` on `τ` — which IS GAP-LP2 / G1. The Farkas route is
therefore **circular** (the negation of the dual-feasibility statement is exactly the
G1 statement we are trying to prove), as the outline-reviewer and the round-4 writeup
honestly flagged. The LP-dual framing does not make the wall weaker; it offers a
different *inspectable object* (the nonneg-mountain inequality (★), read off the bin
assignment `b`) for a direct linear-algebra feasibility proof — but such a proof, if
found, would constitute a proof of G1, not a bypass.

#### 5d. A narrow provable interleaved sub-class (CORRECTED round 5: `k` even)

**Lemma (single-adjacent-2-piece interleaving at even `k`, rest clean).** Suppose
exactly one bin `t* ≥ 1` is interleaved, its two pieces at adjacent positions
`(k, k+1)` with `k` **even** (0-based), and all other bins clean with `s_0 = +1`. Set
`y_eq[t*] = 0`, `y_eq[t] = s_t` (parity) on the clean bins, and mountain
`m_k = 1` (a single unit bump at position `k`), `m_j = 0` elsewhere. Then (★) is
feasible and `Φ ≥ 1`, so `min D ≥ 1` on this sub-class.

**Proof.** Clean positions have `d_j = 0`; in a clean run, (★) reads
`m_j − m_{j−1} ≤ 0`, so with sentinels `m_{−1} = 0` and the mountain nonincreasing
through clean runs, `m` stays `0` until position `k`. At the interleaving
(`k` even): `(−1)^k = +1`, `(−1)^{k+1} = −1`, `y_eq[t*] = 0`, so `d_k = +1`,
`d_{k+1} = −1`. (★) at `j = k`: `m_k − 0 ≤ 1` → `m_k ≤ 1`; at `j = k+1`:
`m_{k+1} − m_k ≤ −1` → `m_k ≥ m_{k+1} + 1 ≥ 1` (since `m_{k+1} ≥ 0`). So `m_k = 1`
(saturating both), and `m_{k+1} = 0`; the clean run after `k+1` keeps `m = 0` to the
sentinel `m_{m−1} = 0`. The mountain `m = (0,…,0,1,0,…,0)` is nonneg, sentinel-0, and
satisfies (★) everywhere (with equality at `k, k+1` and slack-free elsewhere). ✓
Objective: `Φ = 2^n + Σ_{t ≠ t*, t≥1} s_t 2^{n−t} + 0 ≥ 2^n − (2^n − 1) = 1` (the `0`
on `t*` only removes a term; the worst case is all other non-top bins at `−1`, giving
exactly `1`). ∎

*(Round 4 stated this sub-class with `k` **odd** — the opposite parity, an artifact of
the sign error. Under the corrected convention the bump saturates for `k` even. For
`k` odd the single bump would need `m_k ≤ −1` at the `j = k+1` constraint, violating
`m ≥ 0` — so a single adjacent odd-`k` interleaving is NOT certifiable by this cert
and requires a compensating interleaving elsewhere (exactly the open crux).
Verified scipy on `b = (0,1,2,2)` and `b = (0,1,2,2,3)`: feasible, objective `= min D`,
mountain `m = (0,0,1[,0])`.) `subclass_verify.py`.*

#### 5e. Status of GAP-LP2

**OPEN**, honestly G1-equivalent by strong duality. Evidence (NOT proof): scipy
strong-duality checks give `min D ≥ 1` on all 1200+ sampled types (n=2..5, including
all interleaved wall types), with `min D = 1` exactly on the "tight" types — so a
feasible cert with `Φ = min D ≥ 1` provably EXISTS in every sampled case (strong
duality). The obstruction to a GENERAL proof is the same wall the three primal framings
hit (odd-count non-dyadic leftover / deficit-covering / multi-swap subset-sum), now in
LP language: exhibit, for every interleaved type, a nonneg mountain absorbing the
`d_j = (−1)^j − y_eq[b(j)]` mismatches via (★). The data to inspect (bin assignment `b`
+ sort parity) is different from the primal data (fragment position-sign), which is
why the dual framing is kept live as a rival mechanism — but it is **not** easier than
G1, and is not presented as such.

### 6. Closure (conditional on GAP-LP2)

If GAP-LP2 (the structural sign-pattern feasibility lemma) holds, then every
combinatorial type of a `≤ n`-mark refinement of `T_n` admits a feasible dual cert
with objective `Φ ≥ 1` (dyadic dominance gives `Φ ≥ 1` whenever `y_eq[0] = +1`, which
the spine sign-pattern forces), hence `min D ≥ 1` on every type cell (LP strong
duality), hence the global `min D ≥ 1` (`pl-breakpoint-minimum`). This is the lower
bound `c(n) ≥ 2^n/D_n`. **Without GAP-LP2 the lower bound is not closed by this
framing.** The clean-types sub-case (Lemma LP-3) is closed unconditionally; the
parity sub-result (§5b, `min D > 0`) is closed unconditionally; the narrow
even-`k` interleaved sub-class (§5d) is closed unconditionally.

The upper bound `c(n) ≤ 2^n/D_n` is **deferred** to `majorization-upper` (Xiang has
`≤ n` adaptive marks forcing `D ≤ 1/D_n`); this slug owns only the lower side.

---

## Promotable lemmas

- **`lp-dual-clean-types`** (Lemma LP-3, GAP-LP1) — *For every clean combinatorial
  type (each bin's pieces all at one position parity) of a `≤ n`-mark refinement of
  `T_n`, the dual certificate `y_ub = 0`, `y_eq[t] = (bin parity)` is feasible, and the
  dyadic dominance `2^n > 2^n − 1` gives dual objective `≥ 1`; by LP strong duality
  `min D ≥ 1` on the cell. Closes the clean-types sub-case of G1 for all `n`, both
  parities of `m`. Proved in full above (feasibility via `d_k=0`; top-bin-at-`+1` via
  the `D ≥ 0` mass contradiction; objective via geometric series `2^n − (2^n−1) = 1`).
  UNAFFECTED by the round-5 LP-2 sign correction (`y_ub = 0` makes the sign
  irrelevant). ALREADY CERTIFIED (round 4); re-confirmed intact this round.*

- **`lp-dual-odd-mass-parity`** (Lemma §5b, NEW) — *On any type-cell of a refinement
  of `T_n`, `D = 0` is infeasible: `D = 0` forces (by `gaps-leftover-identity`) all
  adjacent pairs equal + a trailing `0`, giving even total mass, contradicting
  `D_n = 2^{n+1} − 1` odd. Hence `min D > 0` (with `min D ≥ 0`, LP-1). A rigorous
  n-independent sub-result; does NOT close GAP-LP2 (min D is real, not integer — the
  LP is not TU).*
  **Submit for certification.** Depends on: `gaps-leftover-identity`, `pl-breakpoint-minimum`
  (for the cell reduction). Proved in full in §5b.

- **`lp-dual-even-k-interleaved`** (Lemma §5d, NEW) — *For a type with exactly one
  interleaved bin `t*` whose two pieces sit at adjacent positions `(k, k+1)` with
  `k` even (0-based), all other bins clean with top bin at `+1` parity, the dual cert
  `y_eq[t*]=0, y_eq[t]=s_t` (clean parities), mountain `m_k = 1` (single bump) is
  feasible under (★) with objective `Φ ≥ 1` (dyadic dominance); by LP strong duality
  `min D ≥ 1` on the cell. scipy-verified (objective `= primal min`).*
  **Submit for certification.** Depends on: LP-1, LP-2 (corrected), `pl-breakpoint-minimum`.
  Proved in full in §5d.

(No other lemma proved in full this round. Lemma LP-0/LP-1/LP-2 are supporting
definitions/theorems internal to this approach; LP-3 is already certified. GAP-LP2 is
open, G1-equivalent by strong duality.)
