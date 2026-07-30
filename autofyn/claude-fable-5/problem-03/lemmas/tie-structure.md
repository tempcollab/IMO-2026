# Lemma: tie-structure (pinned-minimizer / finite-catalog lemma, V1–V4)

*Proposed by the tie-structure-variational builder, round 1 (§2–§3 of that approach file, where the full proofs live). **CERTIFIED by the proof-reviewer, round 2**: the compactification (V1), the cell decomposition + LP-vertex argument (V2), the cut-count-minimality elimination of zero sub-pieces (V3), and the finite-catalog corollary (V4) were each re-checked; the n = 1 instantiation (§6 of the approach file) reproduces c(1) = 2/3 end-to-end and matches brute-force numerics.*

## Statement

Fix a Liu partition a = (a₁ ≥ … ≥ a_k > 0), Σ a_j = 1, k ≤ n+1, and let V(a) := inf over Xiang's legal replies x (≤ n cuts) of odd(S(a,x)).

**(V1)** The infimum is attained (compactify each reply space D_m; odd(S(·)) is piecewise affine and Lipschitz; degenerate cuts are value-equivalent to fewer cuts by zero-padding).

**(V3, pinned minimizer)** There is a minimizer with cut-count vector m, M := Σ m_j ≤ n, at which **all sub-pieces are strictly positive** and the M cut positions satisfy M linearly independent active equations, each of the form
- (ii) sub-piece = sub-piece (same or different cut pieces), or
- (iii) sub-piece = uncut Liu piece.

**(V4, finite catalog)** For each pinned type τ (cut counts, equation set, weak order of sizes) the equations determine the reply uniquely and its value f_τ(a) is an affine function of a; hence V(a) = min{ f_τ(a) : τ feasible at a } — a minimum of finitely many (n-dependent) affine functionals.

## Proof

In full in `approaches/tie-structure-variational.md` §2–§3 (Lemmas V1, V2, V3, Corollary V4). Summary of the mechanism: the tie hyperplane arrangement {s_α = s_β} ∪ {s_α = 0} cuts D_m into cells on which the sort order is constant, so f = odd(S(·)) is affine per cell; the fundamental theorem of linear programming puts a minimizer at a cell vertex, where M independent constraints are active; choosing the minimizer with minimal total cut count kills all form-(i) (zero sub-piece) activations via zero-padding equivalence.

## How to use it

- Reduces "every Xiang reply" to a finite structured catalog — e.g., for the lower bound one only needs to beat pinned tie-system replies.
- Caution (recorded failure): pinned sub-pieces need NOT be integer multiples of any unit — cutting a rung of size 4 into 4/3 + 4/3 + 4/3 is a legal pinned reply. No integrality shortcut exists.
