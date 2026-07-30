## Status
unsolved (NEW round 18 — UPPER wall, sliver/deep interior). A genuinely different framing far from
breakpoint-vertex's LP-vertex/covering lineage: the caterpillar (largest-first) differencing residue
viewed as a **reflected 1-D walk**, and the residual `Φ ≤ u_nL` attacked as a prefix-discrepancy /
contraction statement over the walk, restricted to the DM-tree-realizable (caterpillar) family — which
round-18 gating shows is **minimum-complete** (so achievability costs nothing for the minimum).

## Target (the whole problem's UPPER bound, valley/sliver region)
Xiang forces `D ≤ u_nL` for every valley profile `a₁≥…≥a_{n+1}>0`, `Σ=L`, `a₁<L/2`. By certified
R-COV'/ESF-2 this follows from `Φ(A) := min_{∅≠T} descKK(T) ≤ u_nL`, where `descKK(b₁≥…≥b_r)` is the
reflected walk `v₁=b₁, v_k=|v_{k−1}−b_k|`, output `v_r`. Boundary layer `a₁≥(L−u_nL)/2` already CLOSED
by certified WTC (`descKK(full) ≤ |2a₁−L|`). Open: deep interior `a₁<(L−u_nL)/2`, tightest at the
sliver `a₁∈(L/2−u_n, L/2−u_n/2)`.

## Technique (spine — distinct route)
The caterpillar residue is a **reflected walk on [0,∞)** driven by the sorted decrements `b_k`. WTC is
the trivial `v_r ≤ |2b₁−Σ|` bound (single reflection off 0). The NEW mechanism: after the prefix sum
`P_k=b₂+…+b_k` first CROSSES `b₁` (certified band-landing BL), the walk enters a **contraction regime**
where each further reflected step multiplies the residual by the local scale ratio; under the dyadic
caps (ONE-REC on the tail) the residual telescopes down to the smallest scale `~u_nL`. This is a
walk-contraction argument, NOT a covering radius (dead R10/R12), NOT a density count (dead R11), NOT a
per-subset WTC (dead R16), NOT a single-target subset-sum bound (REFUTED round 18, see below).

## Round-18 foundational gate results (exact Fraction; scripts /tmp/gate_upper*.py, /tmp/gate_cover.py)
- **Caterpillar-min completeness (candidate lemma, 0 counterexamples n≤5 full-tree):**
  `Φ(A) = min_{∅≠T} descKK(T)` equals the min over ALL differencing trees and subsets, on every tested
  profile (random sliver, A^{(n)}, and A^{(n)} perturbed into the sliver). ⇒ the reflected-walk
  (caterpillar) family is minimum-complete; the GAP-ACH factor-2 achievability deficit does NOT affect
  the minimum. This is the load-bearing simplification that makes a walk argument legitimate.
- **Depth-margin structure:** on the A^{(n)}-derived family, `Φ/u_n` = 0.88/0.94/0.97 at the
  boundary (n=3,4,5) but DROPS to 0.38/0.44/0.47 one `u_n/4` deeper. The sup over the sliver is
  attained at the sliver/boundary interface (a continuous limit of the WTC-closed boundary), and
  decreases with depth. ⇒ the right object is a SHARPENED-WTC continuation across the boundary, tight
  at the interface, with genuine slack that grows as a₁ deepens.
- **GUARDRAIL — single-target subset-sum density is REFUTED as a closing lever (round 18):**
  `min_{S⊆tail}|a₁−Σ_S| ≤ u_n` is FALSE — fails 15–33% of sliver profiles (worst ratio 1.76/1.86/1.91/1.99
  at n=3..6, growing with n). It is only ever an UPPER bound on Φ (WTC corollary) and is strictly loose;
  do NOT build the deep interior on "some tail subset sum lands near a₁." The true Φ requires genuine
  differencing (≥2 tail pieces cancelling), i.e. the reflected-walk contraction, not a one-target sum.

## Skeleton
1. Reduce to `Φ ≤ u_nL` in the deep interior — by certified R-COV'/ESF-2 (imported). [done]
2. Caterpillar-min completeness: `Φ = min_{∅≠T} descKK(T)` — GATE first (candidate lemma), then prove
   via Lemma RL (tree signings) + an exchange showing any tree value is ≥ some caterpillar value on a
   subset. [gap C1 — candidate certification]
3. Two-sided invariant (certified I_k, WTC): `b₁−P_k ≤ v_k ≤ |b₁−P_k|`, and BL: `P_k` crosses `b₁` at a
   unique index `k*`. At `k*`, `v_{k*} ≤ P_{k*}−b₁` (overshoot of the crossing). [imported]
4. **Contraction lemma (the crux):** choosing the subset `T` = the pieces up to and including the ones
   that realize the dyadic ladder on the tail, the post-crossing reflected walk satisfies
   `v_{k+1} ≤ max(scale_{k+1}, v_k − scale_{k+1})`-type contraction, and under ONE-REC's per-scale caps
   the residual telescopes to `≤ (smallest active scale) ≤ u_nL`. [gap C2 — MAKE-OR-BREAK]
5. Conclude `Φ ≤ u_nL`; combine with WTC boundary closure to cover all `a₁<L/2`. [gap C3]

## Key lemmas (claim + mechanism)
- **Caterpillar-min completeness** — because MATCH only produces differences (Lemma RL), and for a fixed
  achievable sign-support `T` the smallest |signed sum| is realized by processing in descending order
  (largest-first greedily minimizes the reflected residual); an exchange argument on two out-of-order
  steps does not increase the output. [GATE: 0 counterexamples so far; prove or refute the exchange.]
- **Post-crossing contraction** — because once `P_k` exceeds `b₁` the walk value equals `P_k−b₁` and each
  subsequent decrement `b_{k+1}` (bounded by the dyadic cap at its scale) either overshoots (reflect,
  residual `≤ b_{k+1}`) or undershoots (residual shrinks by `b_{k+1}`); the superincreasing/dyadic cap
  structure (ONE-REC) forces the reachable residual to halve per active scale, telescoping to `~u_nL`.
  [THIS is the make-or-break; the growing-arity signature = the number of active scales = O(n).]

## Open gaps
C1 (caterpillar-min completeness — gate then prove), C2 (post-crossing contraction under ONE-REC caps —
the whole difficulty; must reproduce the O(n)-arity telescoping the sliver demands), C3 (cover).

## Cases to cover
Deep interior split by whether the tail satisfies the dyadic-cap "no big jump" (spread regime → walk
contracts) vs a big jump (collision regime → an even cancellation gives residual 0 ≤ u_nL). Must handle
BOTH uniformly (the R11 spread/collision dichotomy).

## Watch out for
- The sliver has NO uniform margin (sup Φ/u_n → 1 as n→∞); C2 must be EXACT/tight at the interface, not
  a crude bound (VALLEY-TIGHT ban applies at the top edge of the sliver).
- Do NOT regress to any refuted object: covering radius, density count, per-subset WTC, single-target
  subset-sum density (all on the dead list; the last one newly refuted round 18).
- MANDATORY: gate C2 (the contraction constant) in exact Fraction on adversarial sliver profiles BEFORE
  any prose; if the residual does not telescope to `≤u_nL` (i.e. the per-scale contraction constant is
  not ≤ the scale ratio), report the refutation and STOP — do not ship a margin-dressed proof.
