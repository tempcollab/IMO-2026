# Outline review — round 2 (imo-2026-03)

Field state: lower bound certified (`lemmas/ladder-resists.md`); everything reduced to Claim U(m) Case 3 + the a₁ = a₂ tie branch. The outliner proposes: advance the leader with three new keys, copy it for a second Case-3b fill, re-target tie-structure-variational at a static proof of U(m), and fold dyadic-recursion-induction. I verified the load-bearing algebra by hand and the numeric claims independently.

## Independent verification performed this round

- **Tie branch a₁ = a₂ ≥ 2^{m−2}β (outline step 2):** re-derived by hand. FreeRetire (0 cuts) + one zero-pad gives an (m−1)-piece instance with T′ = T − 2a₂ ≤ (2^m−1)β − 2^{m−1}β = (2^{m−1}−1)β, so U(m−1) yields Δ ≤ β with m−2 ≤ m−1 cuts. Correct; legitimate strong induction (U(m−1) with zeros allowed — the claim is stated for arbitrary nonneg multisets, so no special zero-handling caveat is even needed beyond "never cut a zero piece", already in the twin's reduction). CLOSES the tie sub-gap.
- **Case 3a, a₁ ≥ (2^{m−1}−1)β (outline step 3):** re-derived by hand. Δ = |2a₁ − T|; upper side 2·2^{m−1}β − (2^m−1)β = β from a₁ < 2^{m−1}β, lower side (2^m−1)β − 2(2^{m−1}−1)β = β from the 3a threshold. Feasibility x₂ = a₁ − Σ_{i≥3}aᵢ ≥ 0: the outliner's counting contradiction checks out (infeasibility forces a₂ < β, hence T < (2^{m−1}+m−1)β ≤ (2^m−1)β = T, using m ≤ 2^{m−1} for m ≥ 2). The outliner's threshold correction of the middle-case explorer's gloss is right — the explorer's 2a₁ − T ≤ β covers only one sign; the (2^{m−1}−1)β floor is what caps T − 2a₁. One realizability point the outline leaves implicit but which I verified holds: **final feasibility implies chain feasibility** — the running remainder r_k = a₁ − Σ_{i=3}^{k}aᵢ equals Σ_{i>k}aᵢ + x₂ ≥ a_{k+1}, so every Match in the sorted chain is legal (equalities route through FreeRetire). Builder: state this one line explicitly. CLOSES Case 3a.
- **U(3) corollary:** checked — for m = 3 in Case 3, a₁ < 3β would force a₂ > 2β, contradicting a₂ < 2β; so Case 3a covers all of Case 3 at m = 3. With the tie branch and U(1), U(2) already done, **U(3) is fully closed** once steps 2–3 are written.
- **Ternary window claim (Case 3b):** independent numeric check, 5100 random Case-3b instances (m = 4..7): worst min over admissible ternary c of |Σca|/β = 0.727 (m=4), 0.654 (m=5), 0.411 (m=6), 0.241 (m=7). Confirms the outliner's ≤ 0.80β and shows slack *growing* with m — good news for the dense-branch/averaging arguments; the tight regime is genuinely confined to Cases 1–2, which are proved.
- **Realizability of the ternary optimum:** exhaustive move search (Bisect/Match/FreeRetire, ≤ m−1 cuts) on 60 random Case-3b instances at m = 4: the true optimum is ≤ the ternary optimum every time; U(4) never violated. Consistent with the outliner's 120-instance check.
- **Bands hand example (6.5, 3.9, 2.8, 1.8)β:** re-derived — split 2.8 → 2.6+0.2, split 6.5 → 3.9+2.6, Bisect 1.8; 3 cuts, Δ = 0.2β. Correct. **Greedy by-rank cover failure (5.77, 3.46, 3.46, 2.31)·(T/15):** re-derived — covering a₁ by a₂, a₃ leaves {2.31, 1.15} with 1 cut, best Δ = 1.16β > β, while the chosen cover {a₂, a₄} = 5.77 exactly gives Δ = 0. Correct; the "cover must be chosen" warning is real.
- **Fold evidence for C(m):** re-checked — greedy on (5,3,3,2)/13 gives Liu = 1/2 + (1/13)/2 = 7/13 ≈ 0.5385 > C(3) bound max(5/13, 1/2 + 5/(13·16)) ≈ 0.5240. So C(m)'s slack does not dodge the move-selection problem. Confirmed.

## Verdicts

### discrepancy-halving — advance: APPROVE

Whole attempt (answer + both bounds), right technique, and the round's three keys (tie branch, Case 3a, U(3)) are verified above — they are one-paragraph proofs the builder just has to write. The ternary reframing of Case 3b is a genuine structural insight, not a heuristic: the move vocabulary realizes exactly the admissible signed sums within budget m−1 automatically (z + (k−1) = m−1). Notes for the builder:

1. **Step 4 (ternary realizability) must carry an explicit smallness hypothesis.** Not every mixed signed sum is reachable (a residual can never exceed the current max — the outline's own |5+3−1| example). The clean sufficient condition to aim for, mirroring the Case-3a argument: the sorted interleaved chain is legal whenever every partial signed sum stays in [0, current max]; prove the chosen witness c from step 5 admits such an ordering. Do not cite "all signed sums reachable."
2. **Step 5 dense branch:** the standard density lemma is correct as stated (by downward induction: if aᵢ ≤ Σ_{j>i}aⱼ + β for all i, subset sums of {aᵢ..a_m} are β-dense in [0, tail]), but the *window* form needs the super-increasing level located relative to T′/2 — pin exactly which levels must be non-super-increasing for the window [(T′−β)/2, (T′+β)/2] to be hit. The sparse branch (super-increasing level ⟹ ladder-like top) is the honest open work; it is correctly flagged, not hidden.
3. Side-task confirmed: certify `lemmas/reduction-to-um.md` and `lemmas/um-easy-cases.md` (Cases 1, 2 incl. tie, 3a, U(m ≤ 3)) so the siblings import instead of re-prove.
4. Keep numerics chunked with frequent prints (round-1 kill).

### discrepancy-halving-bands — copy: APPROVE (copy executed)

Legitimate use of the copy rule: one proven shared prefix (through Case 3a), one gap (Case 3b), two genuinely different fills (subset-sum window/ternary dichotomy vs band-pigeonhole potential). Copy executed in the ranker (inherits Elo/counts); I wrote the twin's body at `results/imo-2026-03/approaches/discrepancy-halving-bands.md` per the copy rule — builder starts from there and does NOT re-prove steps 1–3. Issues to close while building:

1. **The potential argument is the make-or-break** (step 3 of the divergent plan). An in-band Match remainder can exceed β (band width 2^kβ) — the potential must count band drops, not "remainder ≤ β". State the potential precisely and prove the m−1 budget suffices, or prove the process only stalls in the distinct-band state.
2. **Distinct-band stall:** the cover-then-Bisect handler needs an existence proof for the covering subset within budget (the by-rank cover provably fails — see verification). This is where this twin and its sibling are closest (a distinct-band profile is ladder-like, cousin of the sibling's super-increasing sparse branch) — flagged as residual shared-wall risk; acceptable because the two mechanisms for *reaching* the stall differ and each has an independent fallback, but if BOTH twins bottom out on the ladder-like stall next round, that is a shared-gap plateau and the orchestrator should demand a foreign framing.
3. If the tail-min fallback (step 5) is adopted, all cases must be re-proved at the strengthened invariant (standing rule from round 1).

### tie-structure-variational — revise: APPROVE (with a hard kill criterion)

The re-target is the right call and the proof-reviewer's routing note endorsed exactly this: keep the field's only non-move-process framing, point its certified static machinery (V1–V4, LP vertex) at U(m) itself. It is a whole attempt (imports ladder-resists + the U reduction, then proves U(m) statically). Honest about steps 3–4 being fresh. Issues:

1. **Step 3 (ternary structure theorem) is the make-or-break** — and note its payoff is real even in partial form: if pinned optima of the subgame are exactly ternary matching structures, it *proves the siblings' reframing lossless* and independently confirms their case analysis. The V3 cut-count-minimality port must be checked, not asserted "verbatim" — the subgame's reply space (≤ m−1 cuts on a fixed multiset, no outer sup) differs from the original in exactly the place V3's padding-embedding argument lives. Builder: write the port in full.
2. **Step 4 must not degenerate into per-region certificates.** The alt-upper explorer's warning is correct and the outline itself adopts it as the kill criterion: if by end of build the route is re-deriving Cases 1/2/3a-style regional certificates, that is the same wall in convex-analysis clothing — record the kill and fold next round. Hold to it.
3. Record the retired outer-sup route in the file's `## Approaches tried` (the outline promises this; make sure it lands).

### dyadic-recursion-induction — fold: ACCEPTED

Evidence verified (see above): never built; Cases A/B/C are exactly U(m)'s Cases 1/2/3a; Case D is the same wall in the same move-process framing; the one distinct lever (C(m) slack invariant) fails to be easier — greedy violates C(3) on (5,3,3,2)/13, so proving C(m) needs the same smart selection, and its induction reintroduces the two-variable split. Keeping it would violate field diversity for zero expected value; the copy is the better third slot. Fold handling: not registered for build; down-ranked in the Elo (3 losses recorded); NOT hard-retired per ranker policy — if the field ever needs a slack-invariant line again it can be revived with a new mechanism. **Proof-reviewer: please record in `current.md`'s dead-end list: "C(m) slack invariant (dyadic-recursion): not easier — greedy violates C(3) on (5,3,3,2)/13; same selection problem as the sharp bound." The slug file's `## Approaches tried` should note the fold (builder of discrepancy-halving may add the one line, or the proof-reviewer at review time).**

## Diversity check

Three live lines, three mechanisms for the one remaining gap: subset-sum/ternary dichotomy (dense/sparse), band-pigeonhole potential, and static LP/pinned-catalog + averaging. The twins share their spine by design (sanctioned copy) and have a cousin-shaped hard branch (ladder-like stall vs super-increasing sparse) — watch for a joint plateau there; tie-structure-variational is the genuinely foreign framing insurance. The reserve (probabilistic first-moment on the 0.73β–0.80β slack) is correctly benched, and my numerics (slack grows with m) make it a credible promotion if both fills stall.

## Ranking actions taken

- `copy_approach`: discrepancy-halving → discrepancy-halving-bands (inherits Elo 1500.0, expanded 1, selected 1); body file written.
- `update_ranking` (5 comparisons, anchored to round-1 outcomes + fold evidence): each live line beats dyadic-recursion-induction (advanced/proven-prefix vs never-built + debunked lever); discrepancy-halving beats tie-structure-variational (one verified lemma from finishing vs fresh unproven route) and beats its twin (it owns the round's verified closures; the twin's fill is untested).
- Resulting Elo: discrepancy-halving 1547.3; discrepancy-halving-bands 1500.6; dyadic-recursion-induction 1480.0; tie-structure-variational 1472.2. All stale flags cleared.

build set: discrepancy-halving, discrepancy-halving-bands, tie-structure-variational
