# Lemma: cyclic-successor (iterating least-greater-than on a periodic set)

## Status
DUPLICATE — merge into `lemmas/periodic-set-iteration.md` (the canonical, CERTIFIED version). This file states the same theorem with the same proof; it is correct but redundant. Kept for traceability; do not import from here.

## Statement
Let `L ≥ 1` be an integer and `B ⊆ Z` be a nonempty set that is `L`-periodic (`B + L = B`). For `x ∈ B` define
```
f(x) := min(B ∩ (x, ∞))           (the next element of B strictly after x; well-defined since x+L ∈ B).
```
Then for **any** starting point `x_0 ∈ B`, the orbit `x_{k+1} = f(x_k)` satisfies
```
x_{k+T} = x_k + L   for every k ≥ 0,
```
where `T := |{ r mod L : r ∈ B }|`. The orbit is a single cycle: there is no pre-period (periodicity holds from `k = 0`), and each residue of `B mod L` is visited exactly once per period.

## Proof
Let `R_0 := { r mod L : the residue class r meets B } ⊆ Z/LZ`. By `L`-periodicity, `B` is the full preimage of `R_0`: `B = { x ∈ Z : x mod L ∈ R_0 }`. Enumerate `R_0` in increasing order in `[0, L)` as
```
r_1 < r_2 < ... < r_T,     and set r_{T+1} := r_1 + L  (for bookkeeping).
```

**Well-definedness on residues.** Suppose `x' ≡ x (mod L)`, say `x' = x + kL`. By `L`-periodicity, `B ∩ (x', ∞) = (B ∩ (x, ∞)) + kL`, so `f(x') = f(x) + kL`. Consequently:
- `f(x') ≡ f(x) (mod L)`, so `φ(r) := f(x) mod L` depends only on `r = x mod L`;
- the gap `f(x') - x' = f(x) - x`, so `g(r) := f(x) - x` depends only on `r = x mod L`.

**`φ` is the cyclic successor.** Take `x ≡ r_i`. The residues of `B` strictly larger than `r_i` within the same period are `r_{i+1}, ..., r_T` (this list is empty when `i = T`).
- If `i < T`: the smallest element of `B` greater than `x` has residue `r_{i+1}`, so `φ(r_i) = r_{i+1}` and `g(r_i) = r_{i+1} - r_i`.
- If `i = T`: the next element of `B` after `x` lies in the next period, at residue `r_1`; so `φ(r_T) = r_1` and `g(r_T) = r_1 + L - r_T`.

Thus `φ(r_i) = r_{i+1}` cyclically (with `r_{T+1} = r_1`): `φ` is a single `T`-cycle permutation of `R_0` (a bijection).

**Lift.** Starting from `r_{i_0}` (the residue of `x_0`), the residue orbit is `r_{i_0} → r_{i_0+1} → ... → r_{i_0}` (cyclically), returning to `r_{i_0}` after exactly `T` steps. The total lift over one full cycle is
```
∑_{j=1}^{T} g(r_j)
  = (r_2 - r_1) + (r_3 - r_2) + ... + (r_T - r_{T-1}) + (r_1 + L - r_T)
  = L.
```
So `x_T = x_0 + L`. Since `φ` is a bijection on `R_0` (a single cycle with no tail), the same holds from every `k`: `x_{k+T} = x_k + L` for all `k ≥ 0`. ∎

## Notes
- The conclusion is from `k = 0` (no pre-period) — the strength needed for `imo-2026-06`'s "for every `n ≥ 1`".
- Requires only that `B` is a fixed nonempty `L`-periodic set; the hard part of `imo-2026-06` is showing the greedy *coincides* with `f` on such a `B` (the "B1" gap), which is outside this lemma.

## Scope / reusability
The lift-and-from-`n=1` engine for `bounded-diff-finite-state`, `periodic-set-iteration`, `hitting-set-monovariant`, and `bijection-from-n1`. Conditional on the relevant approach's stabilization step.
