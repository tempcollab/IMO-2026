# Round-2 field — proof-outliner

## imo-2026-03

State of the problem: lower bound c(n) ≥ 2^n/(2^{n+1}−1) certified (`lemmas/ladder-resists.md`). Everything below is the upper bound, which is rigorously reduced (in `approaches/discrepancy-halving.md`, reviewer-verified) to **Claim U(m)**: any m-piece nonneg multiset, T = ΣA, β = T/(2^m−1), can be driven by ≤ m−1 Bisect/Match/FreeRetire cuts to Δ ≤ β. Open: Case 3 (a₁ < 2^{m−1}β, a₂ < 2^{m−2}β) + the a₁ = a₂ tie branch of Case 2.

**Headline of this outline (new, verified this round in exact/numeric arithmetic):** the Match/Bisect move chain realizes exactly the values |Σ cᵢaᵢ| for ternary sign vectors c ∈ {−1,0,+1}^m (Match chain = ±1 coefficients, Bisect = 0 coefficient, cut count z + (k−1) ≤ m−1 automatically for z zeros, k nonzeros). So the middle case is secretly a **ternary balancing / subset-sum-window problem**, not a move-selection heuristic problem. I verified: (a) on 8600+ random Case-3 instances (m = 4..7), min over admissible c of |Σca| ≤ 0.80β, never above β; (b) on 120 instances (m = 4,5), exhaustive move search always attains ≤ the ternary optimum (realizability holds). This also explains every hand example: (5,3,3,2)/13 optimum 0 = |5−3−0·3−2|; the greedy's failure was choosing signs greedily, not a flaw of the move vocabulary.

Two smaller kills, verified algebraically this round (both one-paragraph proofs, hand the mechanism to the builder):

- **Tie sub-case a₁ = a₂ (≥ 2^{m−2}β) CLOSES:** FreeRetire(a₁,a₂) [0 cuts], pad the remaining m−2 pieces with one zero, apply U(m−1) [needs m−2 ≤ m−1 cuts ✓]: Δ ≤ (T−2a₂)/(2^{m−1}−1) ≤ ((2^m−1)β − 2·2^{m−2}β)/(2^{m−1}−1) = β. (Zero-padding harmless: appending a 0 never changes Δ, and the certified strategy never needs to cut a zero piece.)
- **Case 3a: a₁ ≥ (2^{m−1}−1)β CLOSES by full MultiMatch** (correcting the middle-case explorer's threshold — his |2a₁−T| ≤ β gloss covers only the sign 2a₁ ≥ T; the correct self-contained condition is a₁ ≥ (2^{m−1}−1)β): split a₁ into copies of a₃,…,a_m plus x₂ = a₁ − Σ_{i≥3}aᵢ [m−2 cuts]; all pairs (xᵢ,aᵢ) tie; Δ = |x₂ − a₂| = |2a₁ − T| ≤ β since 2·2^{m−1}β − T = β (upper side, from a₁ < 2^{m−1}β) and T − 2(2^{m−1}−1)β = β (lower side). Feasibility x₂ ≥ 0 is automatic here: if 2a₁ + a₂ < T with a₁ ≥ (2^{m−1}−1)β then a₂ < β, forcing T < (2^{m−1}+m−1)β ≤ (2^m−1)β = T for m ≥ 2 — contradiction. **Corollary: m = 3 has no residual middle case (a₁ > 3β always there), so U(3) is fully closed.**

Remaining true gap after these: **Case 3b: a₁ < (2^{m−1}−1)β, a₂ < 2^{m−2}β, m ≥ 4** — attacked below via the ternary reframing.

---

discrepancy-halving: advance
Target: c(n) = 2^n/(2^{n+1}−1) — full problem (lower bound imported from `lemmas/ladder-resists.md`; upper bound via U(n+1)).
Technique: move-process induction on U(m), now reformulated as ternary balancing (subset-sum window) + a super-increasing dichotomy.
Skeleton:
  1. Import certified lemmas (greedy-claiming, threshold-identity, ladder-resists) and the file's proved reduction Target U ⟸ U(n+1) — unchanged.
  2. Close the a₁ = a₂ tie branch of Case 2 — by FreeRetire + zero-pad + U(m−1), algebra above (verified exact).
  3. Close Case 3a (a₁ ≥ (2^{m−1}−1)β) — by full MultiMatch, algebra + feasibility proof above (verified exact); note this subsumes/absorbs dyadic-recursion's "Case C duplicate-and-remainder" idea. Record U(3) fully closed.
  4. **Ternary realizability lemma (new, load-bearing):** for active A = {a₁ ≥ … ≥ a_m} and any c ∈ {−1,0,+1}^m with k ≥ 1 nonzeros (mixed signs if k ≥ 2) and |Σca| ≤ a_max·(safety hypothesis to be pinned by the builder — numerics suggest the sorted prefix chain suffices whenever |Σca| ≤ β < a₁), some Match/Bisect/FreeRetire sequence with (m−k) + (k−1) = m−1 cuts ends with Δ = |Σca| — because a Match chain processing the +pieces and −pieces in sorted interleaved order keeps the running piece equal to a partial signed sum ≥ 0, and Bisect deletes each 0-coefficient piece for 1 cut. (Beware: NOT every mixed signed sum is reachable — e.g. |5+3−1| = 7 > max on (5,3,1) is not; the lemma must carry a smallness hypothesis. Verified reachability of the ternary *optimum* on 120 exhaustive-search instances.)
  5. **Balancing Claim B(m) (the reframed gap):** in Case 3b there exists admissible c with |Σcᵢaᵢ| ≤ β. Equivalent form: some subset S ⊆ {1..m} (after discarding a set Z, |Z| ≤ m−1) has Σ_S ∈ [(T'−β)/2, (T'+β)/2] where T' = T − Σ_Z. Mechanism — **subset-sum gap dichotomy**: the subset sums of a descending multiset miss an interval of length > β only where some level i is super-increasing by more than β (aᵢ > Σ_{j>i}aⱼ + β).
     - Dense branch: no such level near the window ⟹ a subset sum lands in the window ⟹ done by step 4.
     - Sparse branch: a super-increasing level exists ⟹ the multiset is ladder-like above that level (each piece exceeds its tail); use the exact ladder calculus (the 2^r − (2^r−1) = 1 arithmetic already in ladder-resists / Cases 1–2) to handle the top pieces by Bisect/mirror moves and recurse into the tail with the induction hypothesis. This branch is the honest open work; it is structurally the regime where Cases 1/2-type moves are known to be exactly right.
  6. Assemble: U(m) for all m by strong induction (base m ≤ 3 closed); conclude c(n) ≤ 2^n/(2^{n+1}−1); combine with ladder-resists; state and verify the final answer at n = 1 (2/3) and numerically n = 2, 3.
Key lemmas (claim + mechanism):
  - Tie-branch lemma — because FreeRetire is free and a₂ ≥ 2^{m−2}β makes T−2a₂ ≤ (2^{m−1}−1)β, exactly the U(m−1) budget after a zero-pad.
  - Case-3a MultiMatch — because the residual gap is intrinsically |2a₁−T|, and (2^{m−1}−1)β ≤ a₁ < 2^{m−1}β traps it in [−β, β]; feasibility from a counting contradiction (2^{m−1}+m−1 ≤ 2^m−1).
  - Ternary realizability — because a sorted Match chain computes nested |·−·| = a signed prefix sum, and each Bisect deletes one piece per cut; budget always exactly m−1.
  - Balancing Claim B(m) — because subset sums of {a₂..a_m} are β-dense unless a level is super-increasing by > β, and super-increasing structure is exactly the ladder regime already mastered.
Open gaps: step 4's precise smallness hypothesis; step 5's sparse branch (the only conceptually open piece); write-up of steps 2–3.
Cases to cover: m ≤ 3 base; Case 1; Case 2 (a₁>a₂ and a₁=a₂); Case 3a; Case 3b dense; Case 3b sparse; zero pieces and exact ties throughout.
Watch out for: the sign gloss in the explorer's Case-3a claim (T−2a₁ side needs a₁ ≥ (2^{m−1}−1)β, not just feasibility); reachable values are ≤ current max (don't cite "all signed sums reachable"); Match requires strict L > S > 0 — route equalities through FreeRetire; keep all numeric verification chunked with frequent prints (a round-1 agent was killed for silence).
Builder side-task (shared infrastructure, per field policy): certify into `lemmas/` (i) `reduction-to-um.md` — the padding/move-process/tied-pair reduction Target U ⟸ U(n+1); (ii) `um-easy-cases.md` — Cases 1, 2 (incl. tie branch), 3a and U(m) for m ≤ 3. Siblings then import both.

discrepancy-halving-bands: copy-of discrepancy-halving
Reason for the copy (per the copy rule): one gap — Case 3b — with **two viable, genuinely different fills**; run both. The twin owns the alternative fill; everything through step 3 is identical (import, don't re-prove).
Target: same — c(n) = 2^n/(2^{n+1}−1), end to end.
Technique: same U(m) spine; Case 3b filled by dyadic-band pigeonhole + dust termination instead of the subset-sum dichotomy.
Skeleton (divergence from the twin starts at Case 3b):
  1–3. As in discrepancy-halving (import the certified lemma files the twin's builder produces; do not duplicate).
  4. **Dust termination fact:** Δ(S) ≤ max(S) for every multiset — because the alternating sum of a decreasing nonneg sequence is ≤ its first term. Hence if Xiang ever reaches an active set with all pieces ≤ β, he stops: Δ ≤ β with 0 further cuts.
  5. **Straggler accounting:** Bisect retires a piece entirely (both halves tie), so "Bisect every remaining piece > β and stop" costs #{active pieces > β} cuts. From m pieces, any sequence of j Matches leaves m−j active; total cuts j + #stragglers ≤ m−1 iff at least one Match nets a remainder ≤ β or some piece is already ≤ β.
  6. **Band pigeonhole (alt-upper explorer's handle, not yet in any file):** in Case 3b all pieces < 2^{m−1}β; the m pieces sit in the m−1 dyadic bands [2^k β, 2^{k+1}β), k = 0..m−2, plus dust — if all m pieces are > β, two share a band, and Matching them yields a remainder smaller by ≥ one band. Iterate: each in-band Match strictly reduces the profile; show by a potential argument (e.g. Σ over active pieces of ⌈log₂(piece/β)⌉) that the budget m−1 always suffices to reach the all-dust state — OR that the process stalls only in a distinct-band (ladder-like) configuration, which is handled by cover-then-Bisect: match a₁ exactly against {a₂,…} with one split crossing piece (cost c−1 cuts, retires 2a₁ of mass), then Bisect stragglers, then dust termination — verified by hand on (6.5, 3.9, 2.8, 1.8)β: cuts 3, Δ = 0.2β.
  7. Fallback if the potential argument leaks: the tail-min invariant Δ ≤ min_j T_j/(2^j−1) as strengthened induction hypothesis (already sketched in the approach file).
Key lemmas (claim + mechanism):
  - Δ ≤ max(S) — telescoping of the alternating sum.
  - Band pigeonhole — m pieces > β, m−1 bands below 2^{m−1}β.
  - Potential/budget lemma — each cut either retires a >β piece (Bisect) or drops a band (in-band Match); total band-mass is finite and bounded by the case constraints.
Open gaps: the potential argument in step 6 (the distinct-band stall is the danger); the exact interface between cover-then-Bisect and the induction.
Cases to cover: same enumeration as the twin; within 3b: "two pieces share a band" vs "all >β pieces in distinct bands".
Watch out for: in-band Match remainder can still exceed β (band width 2^kβ, not β) — the potential must count band drops, not "remainder ≤ β"; greedy *descending* cover provably fails ((5.77, 3.46, 3.46, 2.31), T = 15β: residual instance violates the U(2) budget) — the cover subset must be *chosen*, not taken by rank; don't re-prove the twin's steps 1–3.

tie-structure-variational: revise
Verdict on the old route: its §8 kill criterion has half-fired — GAP M(a) is moot (ladder-resists certified) and GAP M(b) is confirmed same-wall duplication of the induction casework. **Do not fold the slug; re-target it** per the proof-reviewer's routing note: its certified static machinery (V1–V4, LP-vertex principle) is the field's only non-move-process framing, and the field must not collapse to one framing. Abandon the outer-sup route (record it in the file as retired).
Target: c(n) = 2^n/(2^{n+1}−1) — full problem, via: import ladder-resists (lower bound) + import `reduction-to-um` (once certified) + a **static pinned-catalog proof of U(m)**.
Technique: LP/vertex (variational) analysis of the fixed-multiset subgame — no adaptive move process, no induction over moves.
Skeleton:
  1. Fix m and the multiset A. Xiang's reply space for the U(m) subgame = allocations of ≤ m−1 cuts with real positions inside pieces; Δ(final) is piecewise-linear in the cut positions — by the same cell decomposition as certified V2.
  2. Pinning: the minimum of Δ over the reply polytope is attained at a reply where every cut is pinned by tie equations (each sub-piece tied to another sub-piece or an uncut piece) — port of certified V2/V3 to the subgame (V3's cut-count-minimality argument transfers verbatim; cite `lemmas/tie-structure.md`).
  3. Classify pinned optima: the tie graph's components are anchored at the values a₁,…,a_m; show every pinned optimal reply is equivalent to a **ternary matching structure** — each piece carries a coefficient in {−1,0,+1} (fully matched into ties, deleted by self-tie/bisection, or the residual carrier) and the pinned value is |Σcᵢaᵢ|. This *proves the ternary reduction is lossless* (the twin approaches only need sufficiency; this route establishes the structure theorem, and would independently confirm the whole Case analysis).
  4. Existence of a good tie system: min over admissible c of |Σca| ≤ β — proved not by casework but by an averaging/exchange argument over the finite catalog (e.g. pair each c with its refinements; or LP duality: exhibit a dual certificate on the catalog polytope). Numerical ground truth from this round: the min is ≤ 0.80β on 8600+ random Case-3 instances, so slack exists for an averaging argument in the middle regime (only Cases 1/2 are tight, and those are already proved by moves).
  5. Combine: U(m) for all m; conclude as in the siblings.
Key lemmas (claim + mechanism):
  - Subgame pinning — LP vertex principle on a piecewise-linear objective (certified V2/V3 pattern, re-instantiated).
  - Ternary structure theorem — components of the tie graph either pair off inside themselves (coefficient 0), tie fully across (±1 canceling), or carry the residual; because a tie component's sub-pieces are equal by value, its Δ-contribution telescopes.
  - Catalog bound — averaging/duality over the finite type family, using the middle-regime slack.
Open gaps: all of steps 3–4 (this is a fresh route); step 3 is the make-or-break.
Cases to cover: within the classification — components anchored at one value vs several; degenerate/zero pieces; m ≤ 3 sanity re-derivation.
Watch out for: the alt-upper explorer's warning stands — a *pointwise per-region certificate* hunt is the same wall in convex-analysis clothing; the value of this route is the structure theorem + averaging, NOT re-deriving Cases A–D. If by end of build the route has reproduced the induction casework, that is this slug's full kill criterion: fold it next round (its lemmas are already donated to `lemmas/`).

dyadic-recursion-induction: fold (recommendation to the outline-reviewer — retire this slug)
Decision and evidence (recorded so it is not re-opened casually):
  - Never built (round-1 builder interrupted); nothing certified lives only here.
  - Its Cases A/B are exactly U(m)'s Cases 1/2 (proved, being certified into `um-easy-cases`); its Case C "duplicate-and-remainder" is exactly the full MultiMatch now closing Case 3a; its Case D is exactly Case 3b — the same wall, same framing (move-process induction), violating the field-diversity rule for keeping it as a rival.
  - Its one distinct lever — the slack invariant C(m): Liu ≤ max(a₁, 1/2 + a₁/2^{m+1}) — does NOT dodge the selection problem: verified this round that plain greedy violates C(3) on (5,3,3,2)/13 (greedy Liu value 7/13 ≈ 0.5385 > C(3) bound ≈ 0.5240), so proving C(m) needs the same smart move selection as the sharp bound; and the alt-upper explorer independently found its induction re-introduces the two-variable split. Slack without a new mechanism is not a framing.
  - Salvage: nothing to migrate — the recursion identity c(n) = c(n)/2 + c(n−1)(1−c(n)) is already recorded in the siblings; note the fold in the slug file's `## Approaches tried` and in current.md's dead-end list ("C(m) slack invariant: not easier — greedy violates C(3); same selection problem").
If the reviewer prefers to keep a third live framing instead of the copy, the priority order is: keep the copy (highest expected value — the leader is one lemma from finishing) > keep this slug. Do not run both this slug and the copy.

---

## Reserve idea (bench, not a slug this round)
Probabilistic/first-moment reply (alt-upper opening 3): randomize the subset choice in the balancing step and bound E|Σca|. Only viable in the slack regime (Case 3b, where min ≤ 0.80β); pointless at the tight boundary. If both Case-3b fills stall next round, promote this with a concrete randomization (random signs conditioned on the window — Hoeffding-type concentration has room since pieces < 2^{m−2}β).

## Suggested build set (for the outline-reviewer's decision)
discrepancy-halving, discrepancy-halving-bands, tie-structure-variational — with discrepancy-halving's builder also certifying `lemmas/reduction-to-um.md` and `lemmas/um-easy-cases.md` for the siblings to import.
