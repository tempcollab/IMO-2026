# LP-dual even-k single-adjacent interleaving lower bound

**Source:** `lp-dual-certificate` §5d, round 5. LP strong duality (corrected sign convention).

## Statement

For a combinatorial type of a `≤ n`-mark refinement of `T_n` (tower units, total `D_n = 2^{n+1}−1`) in which exactly one bin `t* ≥ 1` is interleaved, its two pieces sit at adjacent positions `(k, k+1)` with `k` **even** (0-based), and every other bin is clean (all pieces at one position parity) with the top bin (bin 0) at `+1` parity, the minimum of `D = Σ_{j=0}^{m−1} (−1)^j p_j` over the type-cell is `≥ 1`.

## Proof

Use the corrected dual (LP-2). Set `y_eq[t*] = 0`, `y_eq[t] = s_t` (the common parity of clean bin `t`) for `t ≠ t*`, and `y_ub ≡ 0` except the mountain is a single unit bump `m_k = 1`, `m_j = 0` for `j ≠ k` (with sentinels `m_{−1} = m_{m−1} = 0`). The dual feasibility inequality (★) is
$$m_j - m_{j-1} \;\le\; d_j := (-1)^j - y_{\text{eq}}[b(j)], \qquad j = 0,\dots,m-1.$$

**Clean runs.** At a clean position `j`, `y_eq[b(j)] = s_{b(j)} = (−1)^j`, so `d_j = 0`. (★) reads `m_j − m_{j−1} ≤ 0`: the mountain is nonincreasing through clean runs. With `m_{−1} = 0` it stays `0` up to position `k`; after position `k+1` it returns to `0` and stays to `m_{m−1} = 0`.

**At the interleaving (`k` even).** `(−1)^k = +1`, `(−1)^{k+1} = −1`, `y_eq[t*] = 0`, so `d_k = +1`, `d_{k+1} = −1`.
- (★) at `j = k`: `m_k − m_{k−1} ≤ 1`, and `m_{k−1} = 0` (clean run before), so `m_k ≤ 1`.
- (★) at `j = k+1`: `m_{k+1} − m_k ≤ −1`, i.e. `m_k ≥ m_{k+1} + 1 ≥ 1` (since `m_{k+1} ≥ 0`).

So `m_k = 1` (saturating both inequalities), `m_{k+1} = 0`, and the mountain `m = (0,…,0,1,0,…,0)` is nonneg, sentinel-0, and satisfies (★) everywhere (equality at `k, k+1`, slack-free elsewhere). Feasible. ✓

**Objective.** `Φ = y_eq[0]·2^n + Σ_{t ≥ 1, t ≠ t*} s_t·2^{n−t} + 0·2^{n−t*}`. With `s_0 = +1` (top bin at `+1` parity; forced by the `D ≥ 0` mass contradiction of LP-3) and `s_t ∈ {±1}`:
$$\Phi = 2^n + \sum_{t\ge 1, t\ne t^*} s_t\, 2^{n-t} \;\ge\; 2^n - \sum_{t\ge 1} 2^{n-t} = 2^n - (2^n - 1) = 1,$$
(the `0` on `t*` only removes a term; worst case all other non-top bins at `−1`, giving exactly `1`). ✓

By LP strong duality (LP-1), `min D ≥ Φ ≥ 1` on the cell. ∎

**Parity note.** The `k`-even restriction is load-bearing: for `k` odd, `d_k = −1` and (★) at `j = k` gives `m_k ≤ m_{k−1} − 1 < 0`, violating `m ≥ 0` for the single-bump cert. An odd-`k` adjacent interleaving requires a compensating interleaving elsewhere — part of the open GAP-LP2.

## Scope

A narrow sub-class of interleaved types (single adjacent 2-piece interleaving at even `k`, rest clean). Verified scipy (`subclass_verify.py`): `b = (0,1,2,2)` n=2 gives `min D = 2`, cert obj `2`; `b = (0,1,2,2,3)` n=3 gives `min D = 5`, cert obj `5` (mountain `m = (0,0,1,0)`). General interleaved types (multiple / non-adjacent / odd-`k` interleavings) require the full structural sign-pattern feasibility lemma GAP-LP2 — G1-equivalent by strong duality, OPEN.

## Dependencies

LP-1 (primal bounded below `D ≥ 0`, strong duality), LP-2 (corrected dual, inequality ★, nonneg mountain `m ≥ 0` / `y_ub ≤ 0`), `pl-breakpoint-minimum` (cell reduction).
