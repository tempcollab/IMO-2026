# Approach: discrepancy-halving-bands

Twin of `discrepancy-halving` (copied round 2 by the outline-reviewer; `copied_from: discrepancy-halving`). Shares the entire certified spine — the reduction Target U ⟸ U(n+1), the move vocabulary (Bisect / Match / FreeRetire), Cases 1, 2 (incl. the a₁ = a₂ tie branch), and Case 3a (full MultiMatch) — and diverges only on the one remaining gap, **Case 3b**. Do NOT re-prove the shared prefix here: import it from the twin's file and, once certified, from `lemmas/reduction-to-um.md` and `lemmas/um-easy-cases.md`.

## Status
partial

## Approaches tried
- (round 2, copy) Created as the second fill of the single remaining gap (U(m) Case 3b). Nothing built yet on the divergent part.

## Current best

Everything in `approaches/discrepancy-halving.md` up to and including Case 3a (see that file; lower bound certified in `lemmas/ladder-resists.md`). Remaining gap here as there: **Case 3b — a₁ < (2^{m−1}−1)β, a₂ < 2^{m−2}β, m ≥ 4.**

## Target (the whole claim)

**Answer: c(n) = 2^n/(2^{n+1}−1).** Lower bound imported from `lemmas/ladder-resists.md`; upper bound via Claim U(m) (see twin for the statement and reduction).

## Divergent plan for Case 3b: dyadic bands

Setting: A = (a₁ ≥ … ≥ a_m), T = ΣA, β = T/(2^m−1), all pieces < (2^{m−1}−1)β (Case 3b), budget m−1 cuts, target Δ ≤ β.

1. **Dust termination (lemma).** Δ(S) ≤ max(S) for every multiset — the alternating sum of a decreasing nonnegative sequence is ≤ its first term (telescoping). Hence if the active set ever has all pieces ≤ β, stop: Δ ≤ β with 0 further cuts.
2. **Band pigeonhole (lemma).** Call [2^k β, 2^{k+1}β), k = 0, …, m−2, the dyadic bands, and [0, β) the dust. In Case 3b all pieces < 2^{m−1}β, so if all m active pieces are > β (i.e. none is dust), two of the m pieces share one of the m−1 bands; Matching them leaves a remainder < 2^k β, i.e. strictly below the shared band.
3. **Budget/potential argument (the open work).** Show by a potential (candidate: Σ over active pieces of ⌈log₂(piece/β)⌉, or a band-profile ordering) that iterating "Match an in-band pair; Bisect stragglers; stop at all-dust" always fits in m−1 cuts. Danger case: the process stalls with all >β pieces in **distinct** bands (ladder-like profile).
4. **Distinct-band stall handler: cover-then-Bisect.** Match a₁ exactly against a *chosen* subset of the smaller pieces with one split crossing piece (cost = (#covered) cuts including the crossing split; retires 2a₁ of mass), then Bisect the remaining >β stragglers, then dust termination. Hand-verified instance: (6.5, 3.9, 2.8, 1.8)β — split 2.8 → 2.6 + 0.2, split 6.5 → 3.9 + 2.6, both pairs tie, Bisect 1.8; total 3 cuts, Δ = 0.2β. **Warning (verified):** the greedy *by-rank* cover fails — on (5.77, 3.46, 3.46, 2.31), T = 15β, covering a₁ by a₂, a₃ leaves a residual 2-piece instance {2.31, 1.15} with 1 cut whose best Δ = 1.16β > β. The cover subset must be chosen (here {a₂, a₄} works exactly: 3.46 + 2.31 = 5.77, then Bisect a₃, Δ = 0). Proving the right cover always exists within budget is part of the open work.
5. **Fallback if the potential leaks:** the tail-min invariant Δ ≤ min_j T_j/(2^j−1) (T_j = sum of the j smallest active pieces) as a strengthened induction hypothesis — if adopted, ALL cases must be re-proved at the strengthened strength (outline-reviewer rule, round 1).

## Open gaps
- The potential/budget argument of step 3 (in-band Match drops a band but the remainder can still exceed β — band width is 2^kβ, not β; count band drops, not "remainder ≤ β").
- The distinct-band stall: prove the cover-then-Bisect handler (step 4) always fits the budget, or that the stall state recurses into the induction hypothesis.
- Interface with the strong induction on m (which sub-instances invoke U(m′), m′ < m, and with what budget).

## Cases to cover
Same global enumeration as the twin (m ≤ 3 base; Cases 1, 2 incl. tie, 3a) — imported, not re-proved. Within 3b: "two >β pieces share a band" vs "all >β pieces in distinct bands"; zero pieces and exact ties throughout (route equalities through FreeRetire; Match needs strict L > S > 0).
