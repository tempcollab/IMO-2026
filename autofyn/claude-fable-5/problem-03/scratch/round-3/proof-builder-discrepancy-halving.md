# Build report — proof-builder, slug `discrepancy-halving`, round 3 (imo-2026-03)

## Headline

**Claim U(m) is proved in FULL GENERALITY — no cases, no residual gap. Status of the approach: `solved`.** The planned ternary/dense-sparse dichotomy was not needed: while pinning the outline's step-4 smallness hypothesis, I found a two-lemma argument that closes all of U(m) (Cases 1, 2, tie, 3a, 3b simultaneously) in about a page. The whole problem is now proved end to end: **c(n) = 2^n/(2^{n+1} − 1)** (lower bound = certified `ladder-resists`; upper bound = U(n+1) via the reduction).

## What was proved this round

All in `results/imo-2026-03/approaches/discrepancy-halving.md` (§2 = the new content), with lemma extractions:

1. **Lemma B (balancing pigeonhole).** If all m pieces exceed β = T/(2^m−1), there exist disjoint nonempty P, N with |ΣP − ΣN| ≤ β. Proof: otherwise the 2^m subset sums are pairwise > β apart — nested pairs differ by a sum of ≥ 1 pieces each > β; incomparable pairs S, S′ give exactly the disjoint split (S∖S′, S′∖S), > β by assumption — so their sorted range exceeds (2^m − 1)β = T, contradicting that all sums lie in [0, T]. One paragraph, no structure theory, no density lemma, no super-increasing branch.
2. **Lemma W (two-pile walk realizability).** Any such split is realizable within the m−1 cut budget: walk with running signed sum q (+P pieces, −N pieces), always stepping toward zero; carrier piece of length |q|; Match for strict comparisons, FreeRetire for equalities, fresh designation at q = 0. Mass accounting shows the only reachable empty-pile state is (q > 0, N exhausted, P remaining), where automatically 0 < q < s ≤ β — stop and bisect the rest. Cut count: consumed pieces cost ≤ #consumed − 1 (first is free), bisects cost m − #consumed; total ≤ m − 1. This resolves the outline-reviewer's binding note 1 (the explicit smallness hypothesis for ternary realizability): no hypothesis beyond |ΣP − ΣN| ≤ β is needed, because the walk *chooses its own ordering* and the stuck state is benign — "all signed sums reachable" is never claimed.
3. **Trivial branch:** some piece ≤ β → keep it, bisect all other positive pieces (≤ m−1 cuts), Δ = that piece. (The tight ladder lands here with equality Δ = β.)
4. **Assembly:** U(n+1) + reduction + certified `ladder-resists` ⟹ c(n) = 2^n/(2^{n+1}−1); answer stated and verified (n = 1: 2/3 hand proof; n = 2: 4/7 grid search; algebraic substitution check).

The outline's step-5 sparse branch (super-increasing levels) and the density-lemma window form — the "honest open work" — are mooted: Lemma B needs neither.

## Side-tasks completed

- `results/imo-2026-03/lemmas/reduction-to-um.md` — proposed, awaiting certification (reduction chain Target U ⟸ U(n+1): padding, move process, tied-pair bookkeeping, reply legality).
- `results/imo-2026-03/lemmas/um-easy-cases.md` — proposed, awaiting certification (U(1), U(2), Case 1, Case 2 **including the a₁ = a₂ tie branch closed** via FreeRetire + zero-pad + U(m−1), Case 3a via full MultiMatch with the feasibility contradiction and the reviewer's chain-feasibility line r_k = x₂ + Σ_{i>k}aᵢ ≥ a_{k+1} stated explicitly, U(3) corollary). Marked superseded-but-corroborating.
- `results/imo-2026-03/lemmas/um-proof.md` — proposed, awaiting certification (the full U(m) proof as an importable black box for the siblings).
- Fold line for dyadic-recursion-induction added to `## Approaches tried`.

## Verification (checks only, not proof steps)

- 32,000 random instances, m = 1..8 (ties, zeros, ladder-like, cubed/exponential shapes): full move-by-move simulation with Match-legality assertions, cut budget ≤ m−1 and Δ ≤ β + 1e−9 — zero failures; branch selection, pigeonhole existence, and walk termination all exercised.
- Exact arithmetic (Fractions): ladder (8,4,2,1)β (equality case), (5,3,3,2)/13 greedy-killer (Δ = 0, 2 cuts), (7,7,7,7,3)/31, equal pieces, near-ladders, the bands twin's (5.77, 3.46, 3.46, 2.31) example — all pass.

## What remains open

Nothing on this approach. Remaining process items for the proof-reviewer:
- Verify §2 of the approach file (Lemmas B and W — the two new proofs) and the three proposed lemma files; certify or bounce.
- If APPROVED: `current.md` flips to solved with the Full proof; the siblings (bands, tie-structure-variational) become corroboration/fold candidates rather than needed rivals.

Suggested review pressure points (where I'd poke): the walk's invariant that the carrier length is |q| after a sign flip (Match(y, carrier) sub-case); the strictness bookkeeping in Lemma B (all three comparison cases strict vs. the ≤ β conclusion); the cut count when FreeRetire produces multiple fresh designations.

## Spec concerns:

(none)
