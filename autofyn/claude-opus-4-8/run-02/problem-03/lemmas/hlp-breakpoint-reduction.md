# Lemma: HLP breakpoint reduction of weak majorization

General (dyadic-free) tool. Let `BO, RE` be finite nonnegative multisets and
`Φ(t) := Σ_{v∈BO}(v−t)^+ − Σ_{w∈RE}(w−t)^+` for `t≥0`.

**(a) Ramp characterisation.** `BO ≻_w RE` (weak majorization: `Σ_{top k}BO^↓ ≥ Σ_{top k}RE^↓ ∀k`)
`⟺ Φ(t) ≥ 0 ∀ t≥0`. (Hardy–Littlewood–Pólya; the `⟸` direction proven from scratch by taking
`t = RE^↓_k`: `Σ_x(x−t)^+ ≥ Σ_{top k}BO − k·t` and `Σ_y(y−t)^+ = Σ_{top k}RE − k·t`.)

**(b) Breakpoint reduction.** `Φ` is continuous piecewise-linear, `Φ(t)=0` for `t≥max(BO∪RE)`,
right-slope `Φ'(t)=N_{RE}(t)−N_{BO}(t)`, and at each value `v` the slope jumps by
`mult_{BO}(v)−mult_{RE}(v)`. Upward (convex) kinks occur only where `mult_{BO}(v)>mult_{RE}(v)`, in
particular only at `v∈BO`. A concave kink cannot be a strict local minimum, and `Φ→0` at the top;
so `min_{t≥0}Φ` is attained at `t=0` or a value `v∈BO`. Hence
```
   BO ≻_w RE   ⟺   [ ΣBO ≥ ΣRE ]  ∧  [ Φ(b) ≥ 0  ∀ b ∈ BO ].
```
This collapses a "for all thresholds `t`" weak-majorization goal to a FINITE check at the values of
the majorizing multiset.

## Specialisation to P3's base slice (this problem)
With `BO`=blue-odd rungs, `RE`=red-even values in the merge of `π_0` (Σ=2^n) with the uncut ladder
`L`: the top-rung instance `Φ(θ)=0` holds **unconditionally** (by `m₀≤1`: at most one red exceeds
`θ`, and it sits at rank 1 = odd, contributing 0 to RE; no blue-odd or red-even value exceeds `θ`).
Each residual `Φ(b_i)≥0` (`i≥2`) is, by the shift identity
`Φ(b_i)=[ΣBO(P_i)−ΣRE(P_i)] − b_i(|BO(P_i)|−|RE(P_i)|)`, a shifted `(★)`-type inequality on the
scaled ladder `2b_i·L_{i−1}` against a deficient red total — **the same deficient-ladder object
proven by `base-slice-star.md`** (the `(P_m)/(Q_m)` recursion). So the WM/HLP route and the
length-induction route are provably the same wall.

## Reviewer verification (round 13, exact `Fraction`, independent)
`(WM) ⟺ Φ≥0 at all breakpoints`: 0 mismatches / 920 configs; global min of `Φ` at `t=0` or a
`BO`-value: 0 exceptions; `Φ(θ)=0`: 0 exceptions (n=2..6, integer partitions).

## Status
Parts (a),(b) FULLY PROVEN and certified (round 13, general majorization facts). `Φ(θ)=0` certified.
NOTE: the residual rung inequalities `Φ(b_i)≥0` (`i≥2`) — equivalently the deficient self-similar
`(★)` — are what `base-slice-star.md` proves; this lemma is the reduction/bridge, not itself the
closure of the base slice.

Origin: `approaches/peel-scale-rank-induction.md` §11.6 (round 13). Self-contained.
