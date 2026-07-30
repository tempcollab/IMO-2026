# Lemma: um-proof (Claim U(m), proved in full generality)

*Proposed by the discrepancy-halving builder, round 3. **CERTIFIED by the proof-reviewer, round 4**: Lemma B re-derived from scratch (the three comparison cases are exhaustive and each strict; range of 2^m pairwise->β-separated sums exceeds T); Lemma W's walk re-implemented independently from the proof text with hard assertions on every invariant — carrier length = |q| after sign flips, unreachability of empty-pile states 1–2, the state-3 bound 0 < q < s ≤ β, retired pieces forming exactly-tied pairs, Match strictness, cut budget ≤ m−1 — 4,800 exact-arithmetic instances m = 1..8 (2,963 landing in Branch 2), zero failures; mass-accounting arguments for states 1–3 verified by hand. This is the complete upper-bound engine; it supersedes `um-easy-cases.md` (kept as corroboration). Source of truth: `approaches/discrepancy-halving.md` §2 (identical content). Imports T3/T4 of the certified `lemmas/threshold-identity.md`. Moves as in the certified `lemmas/reduction-to-um.md`.*

## Statement

**Claim U(m).** Let A be any multiset of m ≥ 1 nonnegative reals, T = ΣA, β := T/(2^m − 1). Using at most m − 1 cuts, the Bisect/Match/FreeRetire move process can reach an active multiset A_end with Δ(A_end) ≤ β. (Hence, with the retired tied pairs restored, a final position with Δ ≤ β.)

Tightness: on the ladder A = (2^{m−1}, …, 2, 1)β no move sequence does better than Δ = β (certified `lemmas/ladder-resists.md`, scaled).

## Proof

If T = 0, all entries are 0: stop immediately, Δ(A) = 0 = β. Assume T > 0, so β > 0. Two exhaustive branches.

**Branch 1: some entry aᵢ ≤ β.** Bisect every other positive entry (≤ m − 1 of them, 1 cut each); leave aᵢ and all zeros active. Then A_end = {aᵢ} ∪ {zeros} and Δ(A_end) = aᵢ ≤ β by T3/T4 of `threshold-identity`. Cuts ≤ m − 1. ✔

**Branch 2: every entry > β** (so all are positive).

### Lemma B (balancing pigeonhole)

*If a₁, …, a_m > β > 0 and Σaᵢ = T = (2^m − 1)β, then there are disjoint nonempty index sets P, N ⊆ [m] with |Σ_P a − Σ_N a| ≤ β.*

**Proof.** Suppose instead that every disjoint nonempty pair (P, N) has |Σ_P a − Σ_N a| > β (⋆). Consider the 2^m subset sums f(S) = Σ_{i∈S} aᵢ ∈ [0, T]. For S ≠ S′ put P := S ∖ S′, N := S′ ∖ S (not both empty); then f(S) − f(S′) = Σ_P a − Σ_N a, and exhaustively:
- N = ∅, P ≠ ∅: f(S) − f(S′) = Σ_P a > |P|β ≥ β (each piece > β);
- P = ∅, N ≠ ∅: f(S′) − f(S) > β symmetrically;
- both nonempty: |f(S) − f(S′)| > β by (⋆).

So all 2^m values are pairwise > β apart. Sorting them v₀ < ⋯ < v_{2^m−1},
v_{2^m−1} − v₀ = Σ_{j=0}^{2^m−2}(v_{j+1} − vⱼ) > (2^m − 1)β = T,
contradicting v₀ ≥ 0, v_{2^m−1} ≤ T. ∎

### Lemma W (two-pile walk realizability)

*Let A consist of m positive pieces and P, N ⊆ A be disjoint nonempty sub-multisets with s := |ΣP − ΣN| ≤ β. Then ≤ m − 1 cuts reach A_end with Δ(A_end) ≤ β.*

**Proof.** WLOG ΣP − ΣN = s ≥ 0 (else swap). Let Z := A ∖ (P ∪ N). Maintain: unconsumed sub-multisets P′ ⊆ P, N′ ⊆ N; the running signed sum q := Σ(consumed P) − Σ(consumed N); and the invariant *"all consumed pieces have become retired exactly-tied pairs, plus — iff q ≠ 0 — one active piece of length |q| (the carrier)"*. Initially P′ = P, N′ = N, q = 0. Each step consumes exactly one piece:

- **q = 0:** take x ∈ P′; designate it the carrier (no move, 0 cuts); q ← x > 0.
- **q > 0:** take y ∈ N′ (if N′ = ∅, stop — see below). If y < q: Match(carrier, y), carrier ← q − y [1 cut]. If y > q: Match(y, carrier) — cut y into (q, y − q), retiring {sub-piece q, old carrier}; carrier ← y − q [1 cut]. If y = q: FreeRetire(carrier, y) [0 cuts]. In each sub-case q ← q − y, and the carrier length is |q| whenever q ≠ 0. Match legality (strict inequality, positive arguments) holds in the sub-case used; equality routes through FreeRetire.
- **q < 0:** symmetric with x ∈ P′; q ← q + x.

By construction q always equals Σ(consumed P) − Σ(consumed N), and the walk halts within |P| + |N| steps. Empty-pile analysis (all pieces positive; ΣN = ΣP − s ≤ ΣP):

1. *q < 0 with P′ = ∅* is unreachable: it gives Σ(consumed N) = ΣP + |q| > ΣP ≥ ΣN ≥ Σ(consumed N), a contradiction.
2. *q = 0 with P′ = ∅, N′ ≠ ∅* is unreachable: it gives Σ(consumed N) = ΣP = ΣN + s ≥ ΣN, yet an unconsumed positive piece of N forces Σ(consumed N) < ΣN.
3. *q > 0 with N′ = ∅* is the one reachable stop: unconsumed P-mass = ΣP − (ΣN + q) = s − q; if P′ ≠ ∅ this is > 0, so 0 < q < s ≤ β.

Terminal positions: everything consumed (q = s; carrier of length s ≤ β if s > 0, none if s = 0), or state 3 (carrier of length q < β plus unconsumed P′). In either case, bisect every unconsumed piece (P′ and Z; each an original positive piece, so Bisect is legal), one cut each. Then A_end = {carrier} or ∅, and Δ(A_end) ≤ β.

Cut count: each consumed piece is consumed by exactly one of fresh designation (0 cuts), Match (1 cut), FreeRetire (0 cuts), and the first consumed piece is a fresh designation, so the walk uses ≤ #consumed − 1 cuts; the endgame uses m − #consumed bisects. Total ≤ m − 1. ∎

### Conclusion

In Branch 2, Lemma B supplies the split and Lemma W realizes it: Δ ≤ β within m − 1 cuts. Branches 1 and 2 are exhaustive, so U(m) holds for every m ≥ 1. ∎

## Verification record (checks, not proof steps)

32,000 random instances, m = 1..8 (ties, zeros, ladder-like and adversarial shapes): move-by-move simulation with legality assertions; cut budget ≤ m − 1 and Δ ≤ β in every instance. Exact-arithmetic spot checks: ladder (8,4,2,1)β (Branch 1, Δ = β, tight); (5,3,3,2)·(T/13) (P = {5}, N = {3,2}: 2 cuts, Δ = 0); (7,7,7,7,3)·(T/31); equal pieces; near-ladders.
