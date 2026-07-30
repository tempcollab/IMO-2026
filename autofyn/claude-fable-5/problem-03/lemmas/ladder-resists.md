# Lemma: ladder-resists (Theorem L — the complete lower bound c(n) ≥ 2^n/(2^{n+1}−1))

*Proposed by the discrepancy-halving builder, round 1 (Theorem L of that file). **CERTIFIED by the proof-reviewer, round 2**: the tree/mass argument re-derived independently step by step (edge/vertex counts, existence of a tree component, partner distinctness, the surplus 2^r − (2^0+⋯+2^{r−1}) = 1), and stress-tested numerically — Nelder–Mead minimization of Δ over ALL cut allocations against the ladder for n = 1, 2, 3 finds minimum exactly u, never below. This is the entire lower bound of imo-2026-03; import as a black box.*

## Statement

Let u = 1/(2^{n+1}−1). Let Liu Bang cut the stick into the **dyadic ladder** of n+1 pieces with lengths 2^n u, 2^{n−1} u, …, 2u, u (rung k has length 2^k u, k = 0, …, n; n interior marks). Then for every legal reply of Xiang Yu (≤ n further distinct marks), the final multiset S satisfies Δ(S) ≥ u; hence (by `threshold-identity` and `greedy-claiming`) Liu Bang's value is ≥ (1+u)/2 = 2^n/(2^{n+1}−1). Therefore

**c(n) ≥ 2^n/(2^{n+1}−1).**

Moreover Xiang's mirror reply (cut rung k into two halves 2^{k−1}u, for k = 1, …, n) achieves Δ = u exactly (n tied pairs plus the residual rung 0, tied-pair invariance), so the ladder guarantees exactly this value.

## Proof

Work in units of u: rung k has mass 2^k; we must show Δ(S) ≥ 1.

By Corollary R (`greedy-claiming`), each Xiang mark either sits at a stick endpoint (adds a zero piece — harmless by zero-padding, discard it) or lies in the interior of exactly one rung (it must be distinct from Liu's marks, which are the rung boundaries). Let c_k ≥ 0 be the number of Xiang marks interior to rung k and C := Σ c_k ≤ n. Rung k splits into c_k + 1 **fragments**, positive reals summing to 2^k. S is the multiset of all fragments; m := |S| = (n+1) + C ≤ 2n+1.

**Step 1 (consecutive pairing).** Sort S as p₁ ≥ … ≥ p_m (fixed tie-breaking). If m is odd, append a phantom piece 0 homed at a phantom vertex ⊥ of mass 0; the list now has even length 2q. Pair consecutively: P_i = {p_{2i−1}, p_{2i}}, gap g_i := p_{2i−1} − p_{2i} ≥ 0. Then Σ_i g_i = Δ(S) (the phantom turns a trailing +p_m into the gap p_m − 0).

**Step 2 (pairing multigraph).** Let G have vertex set {rungs 0, …, n} (plus ⊥ if used) and one edge per pair, joining the home vertices of its two pieces (a loop if both are fragments of one rung). Then deg(rung k) = c_k + 1 ≥ 1 (loops count twice), deg(⊥) = 1, and

- m even: m = n+1+C ≤ 2n+1 and even forces m ≤ 2n, so #edges = m/2 ≤ n < n+1 = #vertices;
- m odd: #edges = (m+1)/2 ≤ (2n+2)/2 = n+1 < n+2 = #vertices.

Every connected component of a multigraph satisfies #edges ≥ #vertices − 1; since totals give #edges < #vertices, **some component T has #edges = #vertices − 1**, i.e. T is a tree (connected, acyclic — no loops, no parallel edges). Every vertex of G has degree ≥ 1, so T is not an isolated vertex: |T| ≥ 2.

**Step 3 (mass surplus at the top of the tree).** Vertex masses (rung k ↦ 2^k, ⊥ ↦ 0) are pairwise distinct. Let r be the vertex of T of largest mass; since |T| ≥ 2 and only ⊥ can have mass 0, r is a real rung. Every other vertex of T is ⊥ or a rung of smaller label, so

mass(T ∖ {r}) ≤ 2^0 + ⋯ + 2^{r−1} = 2^r − 1.

Let f₁, …, f_{c_r+1} be the fragments of rung r (sum 2^r). Each f_i lies in exactly one pair; that pair is an edge incident to r, hence an edge of T, and its other piece π(f_i) is homed at a vertex of T ∖ {r} (a partner cannot be another fragment of r: that pair would be a loop, impossible in a tree). Distinct fragments lie in distinct pairs, so the π(f_i) are distinct pieces, all homed in T ∖ {r}; since all masses are nonnegative,

Σ_i π(f_i) ≤ (total mass of pieces homed in T ∖ {r}) = mass(T ∖ {r}) ≤ 2^r − 1.

Hence Σ_i (f_i − π(f_i)) = 2^r − Σ_i π(f_i) ≥ 1. Each summand is ≤ |f_i − π(f_i)| = the gap of its pair, and the pairs involved are distinct; all gaps are ≥ 0, so

Δ(S) = Σ_{all pairs} g ≥ Σ_i (f_i − π(f_i)) ≥ 1.

Reverting units: Δ(S) ≥ u, and Liu's value = (1 + Δ)/2 ≥ 2^n/(2^{n+1}−1). ∎

No integrality of Xiang's cuts is used anywhere: fragments are arbitrary positive reals; the only arithmetic input is the super-increasing property of {2^k}.
