# Lemmas (Merged-order layer identity `(△△)` + budget-height `H`) — CERTIFIED round 8

**Source:** approaches/induction-recursion-telescope.md §15c–d.
**Reviewer status:** verified (algebra re-derived independently; both exact).

## Lemma H (budget-height cap)
In the merged descending list of `F=Y⊎Z`, the prefix imbalance `c_i:=#T−#B` in `w_1..w_i`
satisfies `max_i c_i ≤ |Y|`. (Proof: `c_i ≤ #{Y-parts among w_1..w_i} ≤ |Y|`.) By the Structure
Lemma `|Y|=a_0+1≤n+1`, so `maxc≤n+1`. Caps excursion *height*, not window length.

## Identity `(△△)` (layer restatement)
For the integer profile `M=N_Y−N_Z` on the merged order, writing `M^+=max(M,0)`, `M^-=max(−M,0)`:
```
∫ (⌊M^+/2⌋ − ⌈M^-/2⌉) dt = ½∫M − ½∫1[M odd] dt = ½∫M − ½ D̃.
```
**Proof.** For integer `k≥0`: `⌊k/2⌋=k/2−½·1[k odd]`, `⌈k/2⌉=k/2+½·1[k odd]`. So
`⌊M^+/2⌋−⌈M^-/2⌉ = (M^+−M^-)/2 − ½(1[M^+ odd]+1[M^- odd]) = M/2 − ½·1[M odd]` (since exactly one
of `M^+,M^-` is nonzero, and `1[M^+ odd]+1[M^- odd]=1[M odd]` at every `t`). Integrate. ∎

## Consequence (why merged-order measure forms are circular for the residual)
With `∫M=1` (Case B), `(△△)` shows the summed-layer form `Σ_kλ(A_{2k})≤Σ_kλ(B_{2k−1})`, the
position-parity `(♠≥0)`, and the localized `(△⋆)` are all pure measure-algebra restatements of
`D̃≥1`. The trivial layer bound `⌊M^+/2⌋≤M^+/2`, `⌈M^-/2⌉≥M^-/2` gives only `D̃≥0` (off by `½`).
So any reshuffle/tiling of the profile `M` in isolation cannot supply the missing `½`: the dyadic
budget `Σa_j≤n` must enter **non-locally**. (Companion negative result, cached: a consecutive
nonneg-block tiling of `Σψ(c_i)Δw_i` exists iff the total is `≥0` — circular — and has no bounded
local window certificate; both-directional greedy fails, minimal witness
`n=3,Y=(3.382,2.553,2.065),Z=(4,1.042,1,0.958)`, sole deficit `−2.046` exceeds each adjacent
surplus. Do NOT re-attempt merged-order block/window/matching closures.)
