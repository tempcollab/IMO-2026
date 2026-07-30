# Lemmas D & E: interior-point obstruction to linear/LP relaxations

**Status:** certified (round 1). Source: `equalization-potential-bound.md`.
Standard, self-contained polytope facts; reviewer re-checked the proofs
line by line — both are correct as stated with no gaps. Certified as
reusable background facts (they do NOT by themselves establish anything
about `c(n)` — see the caveat at the end on how they were actually applied).

## Lemma D (an interior maximum forces a linear functional to be constant)

**Statement.** Let `P` be a polytope of dimension `d ≥ 1` (nonempty relative
interior in its affine hull), and let `f(x) = Σ w_i x_i` be an affine-linear
functional (restricted to the affine hull of `P`). If `f` attains its
maximum over `P` at a point `x* ∈ relint(P)`, then `f` is constant on all
of `P`.

**Proof.** Work inside the affine hull `H` of `P` (dimension `d`); `f`
restricted to `H` is affine in `d` free coordinates with gradient `g ∈ R^d`
(as a function on `H`). Suppose `g ≠ 0`. Since `x* ∈ relint(P)`, there is
`ε_0 > 0` such that the ball of radius `ε_0` around `x*`, within `H`, lies
entirely in `P`. Set `ε = ε_0/(2‖g‖)` and `x' = x* + εg ∈ P` (valid since
`‖x'-x*‖ = ε‖g‖ < ε_0`). Then `f(x') = f(x*) + ε‖g‖^2 > f(x*)`, contradicting
maximality of `x*`. Hence `g = 0`, i.e. `f` is constant on `H`, in particular
on `P`. ∎

## Lemma E (the ordered simplex; the geometric point is a strict interior point)

**Statement.** `Δ_n := {p ∈ R^{n+1} : p_1 ≥ p_2 ≥ ⋯ ≥ p_{n+1} ≥ 0, Σp_i = 1}`
is an `n`-dimensional polytope, and any point of `Δ_n` satisfying every
defining inequality *strictly* (in particular the geometric configuration
`p*_i = 2^{n+1-i}/(2^{n+1}-1)`) lies in its relative interior.

**Proof.** `Δ_n` sits inside the hyperplane `H = {Σp_i=1}` (dimension `n`),
cut out by `p_i ≥ p_{i+1}` (`i=1,...,n`) and `p_{n+1} ≥ 0`. It is the convex
hull of the `n+1` points `V_k = (1/k,...,1/k,0,...,0)` (`k` copies of `1/k`
then zeros), `k=1,...,n+1`: any `p ∈ Δ_n` is `Σ_k λ_k V_k` with
`λ_k = k(p_k - p_{k+1}) ≥ 0` for `k < n+1` and `λ_{n+1} = (n+1)p_{n+1} ≥ 0`
(checked coordinate-by-coordinate via Abel summation; `Σλ_k = 1`). The
differences `V_k - V_{k+1}` (`k=1,...,n`) are linearly independent, so these
`n+1` points affinely span `H`, giving `dim(Δ_n) = n`. For a polytope cut out
by finitely many linear inequalities inside its affine hull, a point at which
every defining inequality holds strictly automatically has a full-dimensional
neighborhood (within the affine hull) still satisfying every inequality,
hence lies in the relative interior. Since `2^{n+1-i}` is strictly decreasing
in `i`, every inequality is strict at `p*`, so `p* ∈ relint(Δ_n)`. ∎

## Caveat on how these lemmas were actually applied in `equalization-potential-bound.md`

These two lemmas are certified as valid *standalone* facts. The specific
application in that approach file — deriving that no non-trivial rank-only
linear weight vector `w` can give a valid, tight bound for `V(A)` — additionally
assumes as a premise that `V(p*) = c(n)` exactly (the geometric configuration's
minimax value truly equals the conjectured `c(n)`, not merely `≤ c(n)`). That
premise is **not yet established** by any approach in this population (only
the `k=0` sub-case and the exact-equality *upper* witness, Proposition 4, are
proved so far — see `geometric-configuration-facts.md`). The reviewer flags
this as an open dependency of the impossibility argument, not a flaw in Lemma
D or E themselves, which stand on their own.
