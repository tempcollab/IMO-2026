# Approach: concavity-lp (piecewise-affine / LP-vertex + concavity + KKT certificate)

## Status
partial (new this round — skeleton with explicit gaps; no build yet)

## The whole-problem target
Prove `c(n) = 2^n/(2^{n+1}−1)`, equivalently (via the CERTIFIED shared spine — Lemma G,
level-measure identity, cut-flip; see `lemmas/greedy-claim.md`, `lemmas/cut-flip.md`) the
discrepancy minimax
```
D* := max_{Liu partition p}  f(p),      f(p) := min_{Xiang ≤ n cuts}  D(p, cuts)  =  u = 1/(2^{n+1}−1).
```
This approach proves BOTH bounds with ONE mechanism: it shows `f` is a **concave** function
on the simplex of Liu partitions and that the **dyadic partition is a first-order (KKT)
stationary point with `f(dyadic) = u`**, so by concavity dyadic is the global max and
`D* = u`. It never constructs Xiang's response for every Liu partition (that is GAP U in the
other approaches); it replaces that case analysis by a single **finite local certificate** at
one point. This is a genuinely different *proof strategy* (LP-duality / concavity + local
optimality) from the direct-strategy (dyadic-discrepancy) and induction (induction-recursion)
routes, so it does not share their GAP U / GAP L wall.

## Why this framing (the structural engine)
Everything rests on a single structural fact that is essentially a corollary of the already-
certified cut-flip lemma:

**Affine-per-order-type.** By the level-measure identity, `D = Σ_pieces ε_r · (piece length)`
where `ε_r = +1` if the piece's rank `r` in sorted-descending order is odd, `−1` if even.
For a **fixed combinatorial order-type** (fixed relative ranking of all final pieces, Liu's
and Xiang's), the sign pattern `ε` is constant, so `D` is an **affine (signed-linear)**
function jointly of Liu's piece lengths `p` and Xiang's free cut positions `x`.

Two consequences, both flagged by the fresh-framing explorer and matching the certified n=1 rule:
- **A single cut is affine in its position with slope in {0, ±2}** (cut-flip: one cut of `ℓ`
  into `x, ℓ−x` toggles parity on `[0,x)∪[ℓ−x,ℓ)`, so `∂D/∂x ∈ {0,±2}`). Hence Xiang's optimum
  in any free cut coordinate is never a generic interior point: it is at a **boundary** —
  either `x→0` (cut not used) or a **tie crossing** (two pieces become equal, i.e. an
  order-type wall). This is exactly the n=1 optimum: "bisect" (children tie), "pin the median"
  (a Xiang child ties a Liu piece), or "no cut."
- Therefore Xiang's minimizing response is attained at a **vertex strategy** `S`: a finite
  combinatorial datum (which pieces are cut, and which ties/pins are active) that pins every
  cut position as an affine function of `p`, making `D = g_S(p)` an **affine functional of `p`**.

Hence `f(p) = min_S g_S(p)` is a **min of finitely many affine functionals of `p`**, so `f`
is **concave** on the partition simplex `Δ = {p_1 ≥ … ≥ p_{n+1} ≥ 0, Σp_i = 1}`. Maximizing a
concave function over a convex set: **any KKT/subgradient-stationary point is a global max.**

## Skeleton (hypothesis → conclusion)
1. **Reduction to `D* = u`** — by the certified shared spine (Lemma G + level-measure identity).
   Import verbatim; no re-proof. `D(p, cuts) = λ{t : #(final pieces > t) odd}`.
2. **Vertex-optimality of Xiang's response** — GAP C1. For any fixed `p`, `min_{≤n cuts} D`
   is attained at a vertex strategy `S` (each cut position pinned by a tie/pin or set to
   `x=0`), so `min_{≤n cuts} D = min_{S ∈ 𝒮} g_S(p)` with `g_S` affine in `p` and `𝒮` finite.
3. **Concavity of `f`** — GAP C2. `f = min_{S∈𝒮} ĝ_S` where each `ĝ_S` is a **global** affine
   functional on `Δ` with `ĝ_S(p) ≥ f(p)` everywhere and `ĝ_S(p) = f(p)` on the region where
   `S` is Xiang-optimal (a supporting-functional / envelope extension). A pointwise min of
   global affine functions is concave on all of `Δ`.
4. **Evaluate `f(dyadic) = u`** — by Case A / the certified `D ≥ 2b₁−1` for the lower side and
   the explicit "all cuts on the top piece" (or "bisect the pairs") vertex response for the
   upper side; both already known numerically (n=2,3) and Case A is certified. This pins the
   value at the candidate maximizer.
5. **KKT / subgradient certificate at dyadic** — GAP C3. Let `p*` = dyadic partition and
   `A = {S : ĝ_S(p*) = u}` its active vertex strategies (Xiang's tied-optimal responses at
   dyadic). Exhibit convex weights `λ_S ≥ 0`, `Σ_{S∈A} λ_S = 1`, with
   `Σ_{S∈A} λ_S ∇ĝ_S = γ·(1,…,1)` for some scalar `γ` (i.e. the subgradient combination is
   **constant**, hence orthogonal to the simplex tangent space `{d : Σd_i = 0}`). By Gordan /
   LP duality this certifies that **no feasible direction increases `f`**: for every `d` with
   `Σd_i = 0`, `min_{S∈A} ∇ĝ_S·d ≤ 0`. (Dyadic is interior to `Δ` — all `p*_i > 0`, strictly
   sorted — so the only active constraint is `Σp_i = 1`; face/boundary cases of `Δ` — Liu
   using `< n` marks — are dominated (certified: those give `D=0<u`), so need not be checked.)
6. **Conclude** — By step 3 `f` is concave on convex `Δ`; by step 5 `p*` is KKT-stationary;
   for a concave function on a convex set a stationary point is a **global maximizer**. With
   step 4, `max_Δ f = f(p*) = u`, i.e. `D* = u`, i.e. `c(n) = (1+u)/2 = 2^n/(2^{n+1}−1)`. ∎

## Key lemmas (claim + mechanism)
- **Vertex-optimality (GAP C1)** — *Xiang's `≤n`-cut minimum is attained with every cut
  position pinned by a tie/pin (or unused).* Mechanism: within one order-type `D` is affine in
  each free cut position with slope `∈{0,±2}` (cut-flip), so a free coordinate can be pushed to
  its region boundary without increasing `D`; iterate over the `≤n` coordinates (they act on
  disjoint pieces, so the moves do not interfere) until all are pinned — an LP whose feasible
  region is a polytope of order-type cells, optimum at a vertex.
- **Global affine envelope (GAP C2)** — *each Xiang vertex strategy `S` extends to a globally
  affine `ĝ_S ≥ f` on `Δ`, equal to `f` where `S` is optimal.* Mechanism: `g_S(p)` is the
  signed sum `Σ ε^S_r p_r(p)` with the tie-pinned cut positions substituted as affine functions
  of `p`; this expression is affine on all of `Δ`, and since applying the *fixed* combinatorial
  strategy `S` to any `p` is a legal Xiang response, `ĝ_S(p) ≥ min_{cuts} D = f(p)` everywhere.
- **Constant-subgradient certificate (GAP C3)** — *a convex combination of the active
  strategies' gradients at dyadic is a constant vector.* Mechanism: each `∇ĝ_S` is the vector of
  effective signs `ε^S` that strategy `S` assigns to Liu's pieces (after substituting the
  pinned cuts); the numerically-observed active responses at dyadic ("all `n` cuts on the top
  piece" recursively, and "bisect the pairs") have gradient vectors that positively combine to a
  constant — this is the general-`n` pattern the builder must exhibit and prove (n=1 case: the
  two active strategies "bisect big" and "pin median" give gradients whose average is constant,
  reproducing the certified `p=1/3` optimum).

## Open gaps (the builder fills these)
- **GAP C1 — vertex-optimality for ≤n *simultaneous* cuts.** Single-cut version is a direct
  corollary of certified cut-flip. The joint version (n cuts on possibly the same or nested
  pieces, with the sorted order re-shuffling as positions move) is the real work: prove the LP
  polytope / order-type-cell decomposition is finite and the min sits at a vertex.
- **GAP C2 — global concavity of `f` over the WHOLE simplex.** Need the envelope extension
  `ĝ_S ≥ f` on all of `Δ` (not just near dyadic) and finiteness of `𝒮`. Combinatorial blow-up
  in `n` of reachable order-types must be controlled (or bypassed by the envelope inequality,
  which only needs `ĝ_S ≥ f`, not an exact cell map).
- **GAP C3 — the KKT certificate at dyadic for general `n`.** Identify the active strategy set
  `A` at the dyadic partition and produce the convex weights `λ_S` making `Σλ_S∇ĝ_S` constant.
  This is a finite check per `n`; the hard part is the uniform-in-`n` pattern/proof.

## Cases to cover
- Interior maximizer only: dyadic is strictly-sorted, all-positive ⇒ interior of `Δ`; the sole
  active linear constraint is `Σp_i=1`. Boundary faces of `Δ` (Liu uses `< n` marks / equal
  pieces) are dominated (certified `D=0<u` under full bisection) — record, do not KKT-check.
- n=1 sanity: the certificate must reproduce the certified `p*=1/3`, active strategies
  {bisect big, pin median}, `f=1/3=u_1`. This is a required consistency check before general n.

## Watch out for
- **The envelope inequality direction.** `ĝ_S ≥ f` (a fixed strategy is only a *feasible*, not
  optimal, response off its region) is what gives concavity — do NOT claim `ĝ_S = f` globally.
- **Finiteness / blow-up of `𝒮`.** If reachable order-types explode, lean on the envelope
  inequality (needs only `ĝ_S ≥ f`) rather than an exact cell enumeration.
- **KKT needs the RIGHT active set.** Missing one active tie at dyadic breaks the constant-
  gradient combination. Cross-check the active set against the numerically-found tied optima
  ("all cuts on top" AND "bisect pairs" both hit `u` at dyadic — likely both are active).
- **Interior vs boundary.** Confirm dyadic is interior so only `Σp_i=1` is active; otherwise
  extra KKT multipliers for the sorted/positivity constraints appear.

## Full proof
Not present — Status `partial`. Three explicit gaps (C1 vertex-optimality, C2 global concavity,
C3 KKT certificate at dyadic).
