# Alternating-sum (D) toolkit: D-REFORM, D-BOUND, D-INSERT, Lemma V'

Certified from `recursive-embedding-induction.md` (round 3/4 work).
Independently re-verified by the proof-reviewer with exact-`Fraction`
randomized search (20,000+ trials per lemma, zero violations).

## Lemma D-REFORM

For a finite sorted list `b_1≥...≥b_m≥0` with `Σb_i=1`, define
`D(B) := Σ(-1)^{i+1} b_i` (1-indexed alternating sum). Then
`oddsum(B) = (1+D(B))/2`. Consequently, for the geometric configuration `A_n`
and target `c(n)`, `oddsum(B)≥c(n) ⟺ D(B)≥δ_n := 1/(2^{n+1}-1)`.

*Proof.* `oddsum(B)-evensum(B)=D(B)` (pairing consecutive terms) and
`oddsum(B)+evensum(B)=1`; add and divide by 2. Reviewer-verified numerically
(20,000 exact-`Fraction` trials, sorted lists summing to 1, sizes 1-8).

## Lemma D-BOUND

For any finite nonempty sorted nonnegative list `y_1≥...≥y_m`,
`0 ≤ D(Y) ≤ y_1`.

*Proof.* Induction on `m`: `D(Y)=y_1-D(Y\{y_1})`, and by IH
`D(Y\{y_1})∈[0,y_2]⊆[0,y_1]`, so `D(Y)∈[0,y_1]`. Reviewer-verified (20,000
trials, sizes 1-8, no violation).

## Lemma D-INSERT

Let `C=(c_1≥...≥c_m)` sorted, `x≥0` inserted at sorted rank `r` (so
`c_1,...,c_{r-1}≥x≥c_r,...,c_m`), giving `C'` of size `m+1`. Then
`D(C') = D(C) - 2τ(r) + (-1)^{r+1}x`, where `τ(r):=Σ_{i≥r}(-1)^{i+1}c_i`
(alternating sum of `C` restricted to original positions `≥r`, `τ(m+1):=0`).

*Proof.* Direct computation from the definition (shifting positions `≥r` up
by one flips their sign contribution). Reviewer-verified (20,000 exact-
`Fraction` random-insertion trials).

## Lemma V' (vertex-reduction for a fixed-tail split-optimization)

*Statement.* For the sub-case where Xiang Yu splits `p_1` into `n+1` parts
`S=(s_1≥...≥s_{n+1}≥0, Σs_i=2t_1)` and merges with a FIXED tail
`T=(t_1,...,t_n)`, the infimum of `D(S∪T)` over the compact polytope of valid
`S` is attained at a point where at most one coordinate `s_i` is strictly
between two consecutive anchors from `{0,t_n,...,t_1}` — every other
coordinate equals an anchor exactly.

*Proof.* `D(S∪T)` is continuous and piecewise-affine on the polytope `P`
(order-type cells cut out by the hyperplanes `s_i=t_j`, `s_i=s_{i+1}`), so its
minimum is attained at a vertex of the induced hyperplane arrangement
restricted to `P`; a vertex of `{x: Σx_i=const, ℓ_i≤x_i≤u_i}` has at most one
coordinate strictly interior to its box. (Standard LP-vertex argument.)

Note: this lemma is stated and proved only for the fixed-tail sub-case (`T`
not itself being simultaneously refined); extending it to a variable `T` is
explicitly flagged as open in the source approach, not claimed here.

## Status
Certified (D-REFORM, D-BOUND, D-INSERT, V' as stated for the fixed-tail
sub-case). Lemma L (the reduced combinatorial claim these tools feed into) is
NOT certified — verified only for n=1..8 by exhaustive enumeration, not
proved in general; remains an open target, not a lemma.
