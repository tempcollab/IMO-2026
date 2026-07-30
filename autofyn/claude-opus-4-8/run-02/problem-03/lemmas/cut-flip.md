# Cut-Flip / Cut-Budget Lemma (parity of the level function under a single cut)

**Status:** CERTIFIED (proof-reviewer, round 1). Proof re-derived and verified
numerically (|ΔD| ≤ 2·min(x,L−x) held on 3000 random split experiments; the
toggle-set description matches).
**Proved in:** `approaches/induction-recursion.md` §3 and
`approaches/potential-certificate.md` (Lemma C2), round 1.

## Setup

For a finite multiset of positive parts, let `N(t) := #{parts of length > t}` for
`t > 0`. By the Level-Measure identity (see `greedy-claim.md`, integral form) the
first player's advantage is `D = λ{ t>0 : N(t) is odd }` and Liu's total is `(1+D)/2`.

## Statement (Cut-Flip)

Replacing one part of length `L` by two parts `x` and `L−x` with `0 < x ≤ L−x`
changes the parity of `N(t)` **exactly** on the set

    S = [0, x) ∪ [L−x, L),      λ(S) = 2x = 2·min(x, L−x),

and leaves the parity unchanged for all other `t`.

## Proof

The single operation adds to `N(t)` the increment
`δ(t) = 1[t<x] + 1[t<L−x] − 1[t<L]` (two new parts appear, the old part `L`
disappears). By intervals (using `x ≤ L−x`):

- `0 ≤ t < x`:   `δ = 1+1−1 = +1`  (odd → parity flips);
- `x ≤ t < L−x`: `δ = 0+1−1 = 0`   (parity unchanged);
- `L−x ≤ t < L`: `δ = 0+0−1 = −1`  (odd → parity flips);
- `t ≥ L`:        `δ = 0`.

Parity flips iff `δ(t)` is odd, i.e. exactly on `[0,x) ∪ [L−x, L)`, of measure `2x`. ∎

## Corollary (Cut-Budget)

Toggling the indicator `1[N odd]` on a set of measure `2x` changes its integral by at
most that measure, so a single cut satisfies `|ΔD| ≤ 2·min(x, L−x)`.

## Corollary (Bisection = keep a sub-multiset)

If Xiang **bisects** every piece in a set `S` of Liu's pieces (each `ℓ` into `ℓ/2,ℓ/2`,
flip-set `[0,ℓ)`) and leaves the complement `T = S^c` whole, then the resulting
discrepancy is exactly `D(T)`, the discrepancy of the sub-multiset `T`. (Midpoints are
interior, hence automatically distinct from Liu's marks.) This corollary is what
**refutes** any bisection-only Xiang strategy: it can only reach `min_{∅≠T} D(T)`, which
exceeds `u` for n ≥ 2 (numerically ≈ 0.165 > 1/7 at n=2).

## Domination corollary (C3)

For any multiset with largest part `b₁`, `D ≥ 2b₁ − 1`, since
`D − (2b₁−1) = 2b₃ + 2b₅ + ⋯ ≥ 0` (using `D = b₁−b₂+b₃−⋯` and `Σbᵢ = 1`).
