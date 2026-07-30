# Lemma: um-easy-cases (U(m) — boundary cases and small m, by direct moves)

*Proposed by the discrepancy-halving builder, round 3. **CERTIFIED by the proof-reviewer, round 4**: base cases, Cases 1–2 (incl. the tie branch's zero-pad bookkeeping), and Case 3a's feasibility (x₂ ≥ 0 via m ≤ 2^{m−1}), chain-strictness r_k = x₂ + Σ_{i>k}aᵢ ≥ a_{k+1} with the equality escape, and both sides of |2a₁ − T| ≤ β re-checked by hand; not load-bearing (superseded by `um-proof.md`) but correct as stated. **Status note:** superseded as a load-bearing step by the general proof in `lemmas/um-proof.md`, which closes U(m) with no case analysis; kept because (a) it independently corroborates the constant in the tight regimes, (b) the outline-reviewer requested it as shared infrastructure, (c) the sibling approaches reference these cases. Moves and notation as in `lemmas/reduction-to-um.md`; Δ, tied-pair invariance (T3), zero-padding (T4) from the certified `lemmas/threshold-identity.md`.*

## Setting

A = a₁ ≥ a₂ ≥ … ≥ a_m ≥ 0, T = ΣA > 0, β := T/(2^m − 1). **Claim U(m):** ≤ m − 1 cuts reach Δ ≤ β. Throughout this file U is proved by strong induction on m: the statements below establish the base cases and the induction step in the listed regimes, assuming U(m′) for all m′ < m ("IH"). (The regimes 1, 2, 3a below do **not** exhaust all instances for m ≥ 4 — the remaining regime is covered by `um-proof.md`.)

## Base cases

**U(1).** A = {a₁}, β = T/(2¹−1) = T = a₁. Stop with 0 cuts: Δ = a₁ = β. ✔

**U(2).** T = 3β. If a₁ ≥ 2β = 2^{m−1}β this is Case 1 below. Otherwise a₁ < 2β forces a₂ = T − a₁ > β; also a₂ ≤ a₁. If a₁ = a₂: FreeRetire, Δ = 0 ≤ β, 0 cuts. If a₁ > a₂ > 0: Match(a₁, a₂) leaves {a₁ − a₂} with a₁ − a₂ < 2β − β = β, 1 cut. ✔ (a₂ = 0 would force a₁ = T = 3β ≥ 2β, i.e. Case 1.)

## Case 1 (top-heavy): a₁ ≥ 2^{m−1}β, m ≥ 2

a₁ ≥ T/m > 0, so Bisect(a₁) is legal [1 cut]; apply IH = U(m−1) to A ∖ {a₁} (total T − a₁, budget m − 2):
Δ ≤ (T − a₁)/(2^{m−1} − 1) ≤ ((2^m − 1)β − 2^{m−1}β)/(2^{m−1} − 1) = β. ✔

## Case 2 (strong second): a₂ ≥ 2^{m−2}β, m ≥ 2

**Sub-case a₁ > a₂.** Then a₂ > 0 and Match(a₁, a₂) is legal [1 cut], leaving {a₁ − a₂} ∪ (A ∖ {a₁, a₂}): m − 1 pieces of total T − 2a₂, budget m − 2. By IH,
Δ ≤ (T − 2a₂)/(2^{m−1} − 1) ≤ ((2^m − 1)β − 2·2^{m−2}β)/(2^{m−1} − 1) = β. ✔

**Sub-case a₁ = a₂ (tie branch).** FreeRetire(a₁, a₂) [0 cuts] leaves A′ := A ∖ {a₁, a₂}, m − 2 pieces, total T′ = T − 2a₂, with the full budget m − 1 still available. Pad A′ with one zero entry to m − 1 pieces (harmless by T4; the strategy of IH never cuts a zero). Apply IH = U(m−1) to the padded A′ (budget m − 2 ≤ m − 1 available):
Δ ≤ T′/(2^{m−1} − 1) ≤ ((2^m − 1)β − 2·2^{m−2}β)/(2^{m−1} − 1) = β. ✔
(For m = 2: A′ = ∅, Δ = 0 directly.)

## Case 3a: a₂ < 2^{m−2}β and (2^{m−1} − 1)β ≤ a₁ < 2^{m−1}β, m ≥ 3

**Full MultiMatch.** Set x₂ := a₁ − Σ_{i≥3} aᵢ = 2a₁ + a₂ − T.

*Feasibility x₂ ≥ 0.* Suppose x₂ < 0, i.e. T > 2a₁ + a₂. Then a₂ < T − 2a₁ ≤ T − 2(2^{m−1} − 1)β = β. Hence every aᵢ (i ≥ 2) is < β, and
T = a₁ + Σ_{i≥2} aᵢ < 2^{m−1}β + (m − 1)β ≤ (2^m − 1)β = T,
using m ≤ 2^{m−1} (valid for all m ≥ 1, by induction: 1 ≤ 1, and m+1 ≤ 2m ≤ 2^m for m ≥ 1). Contradiction. So x₂ ≥ 0.

*The move chain.* Cut a₁ successively into sub-pieces a₃, a₄, …, a_m, x₂ via Match moves against the (still active) pieces a₃, …, a_m in order, skipping any aᵢ = 0 (a zero needs no match and no cut). After matching a₃, …, a_k the running remainder is r_k = a₁ − Σ_{i=3}^{k} aᵢ = x₂ + Σ_{i>k} aᵢ ≥ a_{k+1} (chain feasibility: the remainder always contains x₂ ≥ 0 plus the unmatched tail, so every Match's strict inequality r_k > a_{k+1} holds unless r_k = a_{k+1}). If equality r_k = a_{k+1} occurs, then x₂ = 0 and a_{k+2} = … = a_m = 0; FreeRetire(r_k, a_{k+1}) instead, and the active set becomes {a₂} ∪ {zeros}: Δ = a₂ = |x₂ − a₂|, same value as below, with fewer cuts. Generic count: matching the positive pieces among a₃ … a_m costs ≤ m − 2 cuts and retires each pair (aᵢ, aᵢ); the final active set is A_end = {x₂, a₂} (plus zeros), and no further move is needed: Δ(A_end) = |x₂ − a₂| = |2a₁ − T| directly (alternating sum of two entries; zeros harmless by T4). Total ≤ m − 2 ≤ m − 1 cuts.

*The bound.* Upper side: 2a₁ − T < 2·2^{m−1}β − (2^m − 1)β = β. Lower side: T − 2a₁ ≤ T − 2(2^{m−1} − 1)β = β. Hence Δ = |2a₁ − T| ≤ β. ✔

## Corollary: U(3) closed by Cases 1–3a alone

m = 3, T = 7β. If a₁ ≥ 4β: Case 1. If a₂ ≥ 2β (with tie or not): Case 2. Otherwise a₁ < 4β and a₂ < 2β; then a₁ = T − a₂ − a₃ ≥ 7β − 2·2β = 3β = (2^{3−1} − 1)β, so Case 3a applies. With bases U(1), U(2), the strong induction closes for all m ≤ 3. ∎

## What this file does **not** cover

For m ≥ 4 the regime a₁ < (2^{m−1} − 1)β, a₂ < 2^{m−2}β ("Case 3b") is not handled here; it is covered — along with everything above, uniformly — by `lemmas/um-proof.md` (balancing pigeonhole + two-pile walk).
