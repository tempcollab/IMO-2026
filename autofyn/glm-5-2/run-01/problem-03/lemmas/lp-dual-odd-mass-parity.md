# LP-dual odd-total-mass parity (D=0 infeasible)

**Source:** `lp-dual-certificate` §5b, round 5. LP / parity framing.

## Statement

On any type-cell of a `≤ n`-mark refinement of the dyadic tower `T_n` (tower units, total `D_n = 2^{n+1}−1`), no feasible point has `D = 0`. Combined with `D ≥ 0` on the feasible region (`gaps-leftover-identity` / LP-1), this gives `min D > 0` strictly.

**Scope note.** Rigorous and n-independent. Does NOT close GAP-LP2 / G1: `min D` is real (the per-type LP is not totally unimodular — verified `min D = 5/3` for n=3, `13/3` for n=4), so ruling out `0` does not rule out `min D ∈ (0,1)`. It is a genuine sub-result: it shows `max (dual objective) > 0`, i.e. a feasible dual cert with strictly positive objective always exists.

## Proof

By the certified `gaps-leftover-identity`,
$$D = \sum_{k=0}^{\lfloor m/2\rfloor -1} (p_{2k} - p_{2k+1}) \;+\; \mathbf 1_{m\text{ odd}}\cdot p_{m-1},$$
(0-based, phantom-zero padding for even `m`). Every term is `≥ 0` (the pairs telescope with `p_{2k} ≥ p_{2k+1}` from the sort order, and `p_{m−1} ≥ 0`). Hence `D = 0` forces every term to be `0`:
- `p_{2k} = p_{2k+1}` for every `k` with `2k+1 ≤ m−1`;
- if `m` is odd, `p_{m−1} = 0`.

So the sorted multiset is entirely adjacent-equal pairs `(v_0, v_0), (v_1, v_1), …, (v_r, v_r)`, plus (if `m` odd) a trailing `0`. The total mass is
$$2(v_0 + v_1 + \cdots + v_r) \;[+\, 0] \;=\; \text{an even real number}.$$
But the total mass of any refinement of `T_n` equals the bin-sum total
$$D_n = 2^{n+1} - 1,$$
which is **odd**. Contradiction. So no feasible `p` (refinement) has `D = 0`. With `D ≥ 0` (LP-1), `min D > 0`. ∎

## Dependencies

`gaps-leftover-identity` (the telescoping `D = Σ gaps + leftover`), `pl-breakpoint-minimum` (the cell / global-min reduction).
