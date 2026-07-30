# imo-2026-03 — tracking file (proof-reviewer owned)

## Status
solved

**Answer: c(n) = 2^n / (2^{n+1} − 1).**

Solved by approach `discrepancy-halving` (round 3 build, round 4 review — APPROVE). Both directions proved and reviewer-verified:
- Lower bound: certified `lemmas/ladder-resists.md` (round 2).
- Upper bound: certified `lemmas/reduction-to-um.md` + `lemmas/um-proof.md` (round 4), with `lemmas/um-easy-cases.md` as independent corroboration of the tight regimes.

Reviewer verification (round 4): Lemma B re-derived from scratch; Lemma W's walk re-implemented independently with hard assertions on every invariant — 4,800 exact-arithmetic instances m = 1..8, zero failures; ladder lower bound re-attacked with Nelder–Mead over all cut allocations (n = 1..3: min Δ = u exactly, never below); Lemma G re-checked against a full game tree; end-to-end check on 400 random Liu partitions n = 1..5 (reply legal, ≤ n cuts, Δ ≤ u every time); n = 1 value 2/3 re-proved by hand.

## Approaches tried
- **discrepancy-halving** — **WORKED — full solution.** Round 1: lower bound (Theorem L, certified round 2 as `ladder-resists`); upper bound reduced to Claim U(m), boundary cases proved. Round 3: U(m) closed in full generality by Lemma B (balancing pigeonhole on subset sums) + Lemma W (two-pile walk realizability), superseding the case analysis. Round 4: reviewed and APPROVED.
- **tie-structure-variational** — live infrastructure contributor: `greedy-claiming` and `tie-structure` lemmas certified from it; its own variational route no longer needed (problem solved).
- **discrepancy-halving-bands** — twin of the winner; its Case-3b band mechanism mooted by Lemma B. No longer needed.
- **dyadic-recursion-induction** — folded round 2 (C(m) slack invariant not easier; greedy violates C(3) on (5,3,3,2)/13).
- Recorded dead ends (kept for the record): parity-XOR top-rung induction; integrality of pinned replies (false: 4 → 4/3+4/3+4/3); plain greedy match-or-bisect for U(m) (fails sharp constant on (5,3,3,2)/13).

## Current best

Complete solution: c(n) = 2^n/(2^{n+1}−1), both bounds proved. See Full proof below.

Certified lemma cache: `lemmas/greedy-claiming.md`, `lemmas/threshold-identity.md`, `lemmas/ladder-resists.md`, `lemmas/tie-structure.md`, `lemmas/reduction-to-um.md`, `lemmas/um-proof.md`, `lemmas/um-easy-cases.md`.

## Full proof

**Answer: c(n) = 2^n/(2^{n+1} − 1)** (answer_type `expression`; n = 1 gives 2/3, n = 2 gives 4/7, both independently verified).

### 0. Certified infrastructure

- **Lemma G and Corollary R** (`lemmas/greedy-claiming.md`, certified round 2): the alternating claiming game on a final multiset S has exact value odd(S) (odd-rank sum of the descending sort) for the first player; consequently
  c(n) = sup_a inf_x odd(S(a,x)),
  where a ranges over partitions of 1 into ≤ n+1 positive parts (Liu Bang's pieces; only the size multiset matters) and x over Xiang Yu's legal replies (≤ n cuts at interior points of Liu's pieces, all marks distinct), S(a,x) the resulting multiset of sub-piece lengths.
- **Threshold identity** (`lemmas/threshold-identity.md`, certified round 2): with Δ(S) := p₁ − p₂ + p₃ − ⋯ (descending alternating sum),
  (T1) odd(S) = (ΣS + Δ(S))/2; (T3) Δ(S ∪ {x,x}) = Δ(S) for any x ≥ 0; (T4) zero entries change neither odd nor Δ.
- **Theorem L** (`lemmas/ladder-resists.md`, certified round 2): Liu Bang's dyadic ladder (2^n, 2^{n−1}, …, 2, 1)·u with u := 1/(2^{n+1}−1) satisfies Δ(S) ≥ u for every legal Xiang reply (tree/mass argument on the pairing multigraph over rungs), and the mirror reply attains Δ = u. Hence **c(n) ≥ (1+u)/2 = 2^n/(2^{n+1}−1)**.

By (T1) with ΣS = 1, Liu's value on S is (1 + Δ(S))/2, so c(n) = 1/2 + (1/2)·sup_a inf_x Δ(S(a,x)), and the claimed answer is equivalent to sup_a inf_x Δ = u. Theorem L gives "≥"; it remains to prove:

**Target U.** For every Liu partition a₁ ≥ … ≥ a_k > 0 (k ≤ n+1, Σ = 1), Xiang has a legal reply with Δ(S) ≤ u.

### 1. Reduction to a multiset move process (`lemmas/reduction-to-um.md`, certified round 4)

Pad a with zeros to exactly m = n+1 entries (harmless by (T4); zeros are bookkeeping and are never cut). Xiang builds his reply as moves on an *active multiset* A (initially the padded partition); each move uses ≤ 1 cut and *retires* pieces never touched again:

- **Bisect(L)** [1 cut], L > 0 active: cut L at its midpoint; retire the exactly-tied pair (L/2, L/2); A ← A ∖ {L}.
- **Match(L, S)** [1 cut], L > S > 0 both active: cut L at distance S from an end into (S, L−S); retire the exactly-tied pair {new sub-piece S, old piece S}; A ← A ∖ {L, S} ∪ {L−S}.
- **FreeRetire(L, L)** [0 cuts], two equal active pieces: retire both; A ← A ∖ {L, L}.

Every cut is at an interior point of an existing physical piece, hence a fresh mark distinct from all previous marks; a sequence of ≤ n cut-moves is a legal Xiang reply (stopping early is legal). The final multiset is S = (all retired tied pairs) ∪ A_end, and by (T3) applied once per retired pair, Δ(S) = Δ(A_end). Therefore Target U follows, with m = n+1, T = 1, β = u, budget m−1 = n, from:

**Claim U(m).** *Let A be any multiset of m ≥ 1 nonnegative reals, T = ΣA, β := T/(2^m − 1). Using at most m − 1 cuts, the moves above can reach an active multiset A_end with Δ(A_end) ≤ β.*

### 2. Proof of Claim U(m) (`lemmas/um-proof.md`, certified round 4)

If T = 0, stop immediately: Δ = 0 = β. Assume T > 0, so β > 0. Two exhaustive branches.

**Branch 1: some entry aᵢ ≤ β.** Bisect every *other* positive entry (≤ m − 1 of them, one cut each); leave aᵢ and all zeros active. Then A_end = {aᵢ} ∪ {zeros}, and Δ(A_end) = aᵢ ≤ β by (T3)+(T4). ✔ (The tight ladder (2^{m−1},…,2,1)β lands here with Δ = β exactly, matching Theorem L's tightness.)

**Branch 2: every entry > β** (so all positive; forces m ≥ 2 since m = 1 has a₁ = T = β).

**Lemma B (balancing pigeonhole).** *If a₁, …, a_m > β > 0 and Σaᵢ = T = (2^m − 1)β, there exist disjoint nonempty P, N ⊆ [m] with |Σ_P a − Σ_N a| ≤ β.*

*Proof.* Suppose every disjoint nonempty pair has |Σ_P a − Σ_N a| > β (⋆). The 2^m subset sums f(S) = Σ_{i∈S} aᵢ lie in [0, T]. For S ≠ S′ put P := S ∖ S′, N := S′ ∖ S (not both empty); f(S) − f(S′) = Σ_P a − Σ_N a, and exhaustively: N = ∅ gives Σ_P a > |P|β ≥ β (each piece > β); P = ∅ symmetrically; both nonempty gives > β by (⋆). So all 2^m values are pairwise > β apart; sorting them v₀ < ⋯ < v_{2^m−1},
v_{2^m−1} − v₀ > (2^m − 1)β = T, contradicting v₀ ≥ 0, v_{2^m−1} ≤ T. ∎

**Lemma W (two-pile walk realizability).** *If P, N ⊆ A are disjoint nonempty sub-multisets of the m positive pieces with s := |ΣP − ΣN| ≤ β, then ≤ m − 1 cuts reach A_end with Δ(A_end) ≤ β.*

*Proof.* WLOG ΣP − ΣN = s ≥ 0. Let Z := A ∖ (P ∪ N). Maintain unconsumed piles P′ ⊆ P, N′ ⊆ N, the running sum q := Σ(consumed P) − Σ(consumed N), and the invariant: all consumed pieces have become retired exactly-tied pairs plus — iff q ≠ 0 — one active *carrier* of length |q|. Steps (each consumes one piece):
- **q = 0:** take x ∈ P′, designate it the carrier (no move, 0 cuts); q ← x.
- **q > 0:** take y ∈ N′ (if N′ = ∅ stop — see state 3). If y < q: Match(carrier, y), carrier ← q − y. If y > q: Match(y, carrier), carrier ← y − q. If y = q: FreeRetire(carrier, y). In all sub-cases q ← q − y and the carrier length is |q| whenever q ≠ 0; Match's strict inequality holds in the sub-case used, equalities route through FreeRetire.
- **q < 0:** symmetric with x ∈ P′; q ← q + x.

Empty-pile accounting (all pieces positive; ΣN = ΣP − s):
1. *q < 0 with P′ = ∅* is unreachable: it forces Σ(consumed N) = ΣP + |q| > ΣP ≥ ΣN ≥ Σ(consumed N).
2. *q = 0 with P′ = ∅, N′ ≠ ∅* is unreachable: it forces Σ(consumed N) = ΣP ≥ ΣN, yet an unconsumed positive piece of N forces Σ(consumed N) < ΣN. Hence at q = 0 either the walk continues or P′ = N′ = ∅ and it ends with Δ contribution 0.
3. *q > 0 with N′ = ∅* is the one reachable stop: unconsumed P-mass = ΣP − (ΣN + q) = s − q; if P′ ≠ ∅ this is > 0, so 0 < q < s ≤ β; if P′ = ∅ then q = s ≤ β.

Terminal position: at most one active carrier of length ≤ β, plus the unconsumed pieces P′ ∪ Z. Bisect every unconsumed piece (each an original positive piece). Then A_end = {carrier} or ∅, so Δ(A_end) ≤ β.

Cut count: each consumed piece is consumed by a designation (0 cuts), a Match (1 cut) or a FreeRetire (0 cuts), and the first consumed piece is a designation, so the walk uses ≤ #consumed − 1 cuts; the endgame bisects the m − #consumed unconsumed pieces. Total ≤ m − 1. ∎

*Conclusion of Branch 2.* Lemma B supplies the split, Lemma W realizes it: Δ ≤ β within m − 1 cuts. Branches 1 and 2 are exhaustive, so **U(m) holds for every m ≥ 1**. ∎

### 3. Assembly

For any Liu partition a (padded to m = n+1 entries, T = 1, β = u), Claim U(n+1) gives a move sequence with ≤ n cuts reaching Δ ≤ u; by Section 1 this is a legal reply x with Δ(S(a,x)) ≤ u. Hence by (T1), inf_x odd(S(a,x)) ≤ (1+u)/2 for every a, i.e. c(n) ≤ (1+u)/2 = 2^n/(2^{n+1}−1). Combined with Theorem L (c(n) ≥ 2^n/(2^{n+1}−1)):

**c(n) = 2^n / (2^{n+1} − 1).** ∎

*Answer verification.* n = 1: 2/3 (hand proof: Liu cuts (2/3, 1/3); any Xiang cut leaves Δ ≥ 1/3; conversely U(2) caps every Liu partition at Δ ≤ 1/3). n = 2: 4/7 (matches the round-1 grid search and the reviewer's Nelder–Mead attack: min Δ against the ladder (4,2,1)/7 is exactly 1/7). Algebraically (1 + 1/(2^{n+1}−1))/2 = 2^n/(2^{n+1}−1). ✓
