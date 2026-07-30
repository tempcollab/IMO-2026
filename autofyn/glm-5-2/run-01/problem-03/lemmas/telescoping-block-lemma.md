# Telescoping zero-gradient block lemma (GAP-B)

**Source:** `tail-count` §11, round 4. Non-dyadic generalization of `block-contribution-formula`.

## Statement

Let `M` be a refinement of the dyadic tower `T_n = (2^n, 2^{n-1}, ..., 2, 1)` (tower units, total `D_n = 2^{n+1}-1`) obtained by `≤ n` marks. Fix a combinatorial type `σ` (a strict total order of all `m` pieces), and let `C_σ` be the open PL cell where this order is strict (no ties).

**(a) Affinity.** `D = Σ_{i=1}^m s_i p_i` is affine in the cut positions on `C_σ`, where `s_i = (-1)^{i+1}` is the sign at position `i` (1-based) and `p_i` is the length of the `i`-th piece in sorted order.

**(b) Same-sign block ⇒ constant contribution.** For each split of a tower piece `V` into fragments `f_1, ..., f_r` (with `Σ_j f_j = V` by the partition/telescoping identity), if all fragments sit at positions of the same sign `s`, their combined contribution to `D` is `s · Σ_j f_j = s · V`, independent of the cut positions. If any two fragments sit at opposite-sign positions, the contribution depends on the cuts (gradient `±2` per cut coordinate).

**(c) Constancy (block condition).** If every split's fragments all sit at same-sign positions (the **block condition**), then `D` is CONSTANT on `C_σ`.

**(d) Direct value = 1.** If ALL fragments derived from the top piece `2^n` sit at `+` positions and ALL pieces derived from tower pieces below `2^n` (split or unsplit) sit at `−` positions, then
$$D = 2^n - (2^n - 1) = 1$$
on the whole cell `C_σ`, by (c) and the telescoping mass identity. No dyadic endpoint is needed.

## Proof

(a) On a fixed type, each piece's position (hence sign `s_i`) is fixed. Each piece length `p_i` is affine in the cut positions (each is either a constant — an unsplit tower piece — or an affine function of the cuts: `p = V − q` or `p = q`). `D = Σ s_i p_i` is a finite sum of affine functions, hence affine. (Knowledge-base: `pl-breakpoint-minimum` PL lemma.)

(b) The fragments of a split piece `V` satisfy `Σ_j f_j = V` (they partition `V`; each split replaces `V` by `f + (V−f)`, and iterative splitting preserves the partition sum — the telescoping identity). Their combined contribution to `D` is `Σ_j s_{i_j} f_j`. If `s_{i_j} = s` for all `j` (same sign), this is `s · Σ f_j = s · V`, a constant. If signs differ, the contribution is a non-constant affine function of the cuts: for a single split into `f_1 = V − q, f_2 = q`, the gradient is `∂D/∂q = −s_{i_1} + s_{i_2}`, which is `0` if same sign and `±2` if opposite (matching the single-split slope analysis of `single-split-top-lower-bound`).

(c) By (b), each split piece with uniform-sign fragments contributes a constant `(±V)` to `D`. Unsplit pieces contribute constants `(±2^k)`. So `D` is a sum of constants, hence constant on `C_σ`.

(d) The top piece `2^n` is split into fragments summing to `2^n` (telescoping, (b)). At `+` positions, they contribute `+2^n`. The tower pieces below `2^n` — `{2^{n−1}, ..., 2, 1}`, total mass `2^n − 1` — are either unsplit or further split; in either case, their fragments sum to `2^n − 1` (telescoping of each split tower piece). At `−` positions, they contribute `−(2^n − 1)`. By (c), `D` is constant on `C_σ`; its value is `2^n − (2^n − 1) = 1`. ∎

## Scope

This lemma proves `D = 1` (or `D` constant) on block-condition cells directly from the telescoping mass identity, without requiring the cell to contain a dyadic endpoint. It is the non-dyadic generalization of `block-contribution-formula`. Cells NOT satisfying the block condition (some split's fragments at opposite signs) are NOT settled by this lemma; those require the star-shaped transport (GAP-C, open) or another argument.

## Verification (not a proof step)

T_3 spine-7 cell `{a, 4, b, 2, c, 1, d}`: all 4 fragments at `+` (positions 1,3,5,7), all 3 tower pieces at `−` (positions 2,4,6). `D = (a+b+c+d) − (4+2+1) = 8 − 7 = 1`, independent of `(q_1, q_2, q_3)`. Verified `Fraction`-exact. The V-shape cell (`8→5+3`, then `5→4+1`): the split of `5` produces fragments `{4,1}` at positions 2 `(−)` and 5 `(+)` — opposite signs — block condition FAILS. ✓
