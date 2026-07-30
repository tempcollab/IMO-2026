# LP-dual clean-types lower bound (GAP-LP1)

**Source:** `lp-dual-certificate` Lemma LP-3, round 4. LP strong duality / Farkas framing.

## Statement

For every **clean** combinatorial type of a `≤ n`-mark refinement of the dyadic tower `T_n` (tower units, total `D_n = 2^{n+1}−1`) — i.e. a type in which each bin's pieces all share a single position parity — the minimum of `D = Σ_{k=0}^{m-1} (−1)^k p_k` over the type-cell is `≥ 1`. By `pl-breakpoint-minimum` (the global min is a min over type-cell vertices), this closes the clean-types sub-case of G1 for all `n`, both parities of `m`.

## Proof

**The per-type LP.** Fix a combinatorial type (bin assignment `b: {0,...,m−1} → {0,...,n}` and sort order). The bin-partition LP on the type-cell is:
$$\min\, D(p) = \sum_k (−1)^k p_k \quad \text{s.t.}\quad \sum_{k: b(k)=t} p_k = 2^{n-t}\;\forall t,\quad p_k \ge p_{k+1},\; p_k \ge 0.$$
This LP is **exact** (not a relaxation): every LP-feasible `p` is realizable as a split tree (any composition of `2^{n-t}` into `r ≥ 1` positive parts is realizable by splitting off one piece at a time), and every realizable refinement is LP-feasible. The number of marks is `m − (n+1) ≤ n`.

**Boundedness (`D ≥ 0` on the feasible region).** By `gaps-leftover-identity`, `D = Σ_{k}(p_{2k} − p_{2k+1}) + [m \text{ odd}] p_{m−1}` (0-based, phantom-zero padding for even `m`). Each pair `p_{2k} − p_{2k+1} ≥ 0` (sorted), `p_{m−1} ≥ 0`; so `D ≥ 0` for both parities. LP strong duality applies: `min D = max (dual objective)`.

**The dual.** Dual variables: `y_eq[t]` (free, one per bin-sum equality) and `y_ub[k] ≥ 0` (one per sort inequality `p_k − p_{k+1} ≥ 0`). The dual objective is `Φ(y) = Σ_t y_eq[t] · 2^{n−t}`, a signed tower-value sum. By LP strong duality, `min D = max Φ`.

**Clean-type certificate.** For a clean type, set `y_ub ≡ 0`, `y_eq[t] := s_t` (the common parity of bin `t`, `s_t ∈ {+1, −1}`; empty bins set `y_eq = 0`). Stationarity: `y_eq[b(k)] = s_{b(k)} = (−1)^k` (bin `b(k)` is clean, piece `k` is in it, so `(−1)^k = s_{b(k)}`). With `y_ub = 0`, all dual constraints hold with equality. Feasible. ✓

**Top bin at `+1`.** Suppose `s_0 = −1`: all top-bin fragments (mass `2^n`) at `−` positions, so `+` positions contain only non-top pieces (mass `≤ 2^n − 1`). Then `D = (mass at +) − (mass at −) ≤ (2^n − 1) − 2^n = −1 < 0`, contradicting `D ≥ 0`. So `s_0 = +1` for any realizable clean type. ✓

**Objective `≥ 1` (dyadic dominance).** With `s_0 = +1`:
$$Φ = 2^n + \sum_{t \ge 1} s_t \, 2^{n-t} \;\ge\; 2^n - \sum_{t \ge 1} 2^{n-t} = 2^n - (2^n - 1) = 1,$$
since `Σ_{t≥1} 2^{n−t} = 2^n − 1` (geometric series; the same tower-dominance as `tower-top-unsplit` and `even-group-spine-lower-bound`, in dual form). ✓

**Conclusion.** For every clean type, the dual cert `y_ub = 0, y_eq[t] = s_t` is feasible with objective `Φ ≥ 1`. By LP strong duality, `min D ≥ 1` on the cell. By `pl-breakpoint-minimum`, the global min over all refinements is a min over type-cell vertices; `D ≥ 1` at every clean-type breakpoint. ∎

## Scope

"Clean" is a genuine but restricted sub-class: each bin monochromatic in position parity. This closes the clean-types sub-case of G1 for all `n`. Interleaved types (some bin at both parities) are NOT settled by this lemma; they require the structural sign-pattern feasibility lemma (GAP-LP2, open — and, by LP strong duality, logically equivalent to the full G1 claim, not a weaker target).

## Dependencies

`pl-breakpoint-minimum` (global min = min over type-cell vertices), `gaps-leftover-identity` (for `D ≥ 0` / boundedness).
