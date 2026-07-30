# Proof review — round 4, imo-2026-03, slug `discrepancy-halving`

## Verdict: APPROVE — Status: solved

**Answer: c(n) = 2^n/(2^{n+1} − 1).** The builder's claimed `solved` status is correct. The full proof (lower bound = certified `ladder-resists`; upper bound = reduction + Claim U(m) via Lemma B + Lemma W) is complete and rigorous. `current.md` now carries Status `solved` and the Full proof.

Goal Progress: **SOLVED — run goal met.** `results/imo-2026-03/current.md` Status = solved; discrepancy-halving recorded `verified-milestone` (round 4, Elo 1547, stale flag set). Ranking implication: siblings (bands, tie-structure-variational, dyadic) are now corroboration/fold candidates, not needed rivals; no further build sets required.

## What I attacked and how

The single load-bearing step is **Claim U(m)** (every m-piece multiset can be driven to Δ ≤ T/(2^m−1) with m−1 cuts) — the entire upper bound. Its two new lemmas were re-derived and stress-tested independently of the builder's code:

1. **Lemma B (balancing pigeonhole) — re-derived from scratch.** If no disjoint nonempty P, N has |ΣP − ΣN| ≤ β, then for any S ≠ S′ the difference f(S) − f(S′) equals Σ_{S∖S′} − Σ_{S′∖S}; the three cases (N = ∅ using each piece > β; P = ∅ symmetric; both nonempty using the negated hypothesis) are exhaustive and each yields strict > β. So the 2^m subset sums are pairwise > β apart, forcing range > (2^m−1)β = T against range ≤ T. Airtight; the strictness bookkeeping (strict separation vs. the ≤ β conclusion) is exactly right — the lemma is the contrapositive, so ≤ β is what survives.
2. **Lemma W (two-pile walk) — independently re-implemented** (`/tmp/round-4/verify_um.py`) exactly per the proof text, in exact Fractions, with hard assertions on every claimed invariant: carrier length = |q| after sign flips (the builder's flagged pressure point — verified, including the Match(y, carrier) sub-case where new carrier = y − q = |new q|), unreachability of empty-pile states 1 and 2, the state-3 bound 0 < q < s ≤ β (P′ ≠ ∅) / q = s (P′ = ∅), retired pieces forming exactly-tied pairs, Match strictness, Δ(final S) = Δ(A_end), and cut budget ≤ m−1. **4,800 instances, m = 1..8 (ties, zeros, rationals, ladder-like, near-equal), 2,963 landing in Branch 2 — zero failures.** The mass-accounting proofs of states 1–3 also check by hand (state 1 uses ΣN ≤ ΣP from the WLOG s ≥ 0; state 2 uses positivity of unconsumed N-pieces).
3. **Cut count** — re-derived: #cuts(walk) = #Matches ≤ #consumed − #designations ≤ #consumed − 1 (the first consumed piece is a designation since q = 0 initially); endgame bisects exactly the m − #consumed unconsumed pieces. Total ≤ m − 1. The multiple-fresh-designation worry (builder's pressure point 3) is a non-issue: designations cost 0 cuts, so more of them only lowers the count.
4. **Reduction legality** — every Bisect/Match cut is at an interior point of an existing physical piece (midpoint; distance S with 0 < S < L), hence a fresh mark distinct from all prior marks; zeros are never cut (moves require positive arguments); ≤ n cuts; stopping early legal. Δ(S) = Δ(A_end) by iterated (T3). Checked end-to-end on 400 random Liu partitions, n = 1..5: reply always legal, Δ ≤ u.
5. **Lower bound re-attack** (per role rule): Nelder–Mead minimization of Δ over ALL Xiang cut allocations against the ladder, n = 1, 2, 3 — minimum exactly u each time, never below (`/tmp/round-4/verify_ladder_and_game.py`). The `ladder-resists` tree/mass argument also re-read line by line (component counting, no loops in a tree component, partner distinctness, surplus 2^r − (2^r − 1) = 1): sound.
6. **Lemma G re-check**: full memoized game tree vs. odd(S) on 60 random multisets with ties/zeros — exact match.
7. **Answer verification** (compute_and_prove, answer_type expression): n = 1 re-proved by hand (2/3); n = 2 = 4/7 consistent with grid search and the ladder attack; algebraic identity (1+u)/2 = 2^n/(2^{n+1}−1) checked.

Edge cases audited: T = 0; m = 1 (Branch 2 vacuous since a₁ = T = β); zeros only reachable in Branch 1 (Branch 2 requires all > β); exact ties (routed through FreeRetire everywhere — Match's strictness never violated); Liu using < n+1 pieces (zero-padding, T4); Xiang using < n cuts (legal). Branches and walk sub-cases are exhaustive and disjoint. No circularity: U(m) is proved directly, not by induction on the target; the reduction uses only certified T1/T3/T4 and Corollary R. No crux-move citations; every step proved in-repo.

## Scores

- **Correctness: 10/10.** Every step re-derived or independently machine-verified; zero discrepancies found.
- **Completeness / rigor: 10/10.** All cases present and settled; every invoked tool named and certified; answer stated and verified.
- **Progress: 10/10.** Closes the last open gap (U(m) middle case + tie sub-case) and with it the whole problem.

## Lemma certifications

- `lemmas/reduction-to-um.md` — **CERTIFIED** (padding, tied-pair bookkeeping, cut legality re-checked; stamp added).
- `lemmas/um-proof.md` — **CERTIFIED** (Lemma B re-derived; Lemma W independently re-implemented with invariant assertions, 4,800 instances clean; stamp added).
- `lemmas/um-easy-cases.md` — **CERTIFIED** (not load-bearing; base cases, Cases 1/2/tie/3a re-checked by hand, incl. x₂ ≥ 0 feasibility via m ≤ 2^{m−1} and the chain-equality escape; stamp added).

## Files touched

- `results/imo-2026-03/current.md` — Status → **solved**, Full proof written (reviewer-owned).
- `results/imo-2026-03/lemmas/{reduction-to-um,um-proof,um-easy-cases}.md` — certification stamps.
- `record_outcome(discrepancy-halving, round 4, verified-milestone)` — recorded.
- Verification scripts: `/tmp/round-4/verify_um.py`, `/tmp/round-4/verify_ladder_and_game.py`.

## Routing note for the orchestrator

The run's goal is met. No re-dispatch needed for this slug. Siblings need no further builds; if a wrap-up round runs, it should only commit `results/imo-2026-03/` and stop.
