# proof-builder report — universal-adversary-strategy (round 13)

## Task recap
Verify the outline-reviewer's numeric finding (plain Move 1 alone
suffices in Case (b) — tail-dominant Case-C configurations), and if
confirmed, prove it rigorously, closing Lemma HALF-BOUND together with
Case (a) from the round-13 outline.

## What I did
1. Independently re-implemented the certified Round-12
   `solve(A,budget)` recursion from scratch (`fractions.Fraction`,
   memoized) and reproduced the outline-reviewer's numeric claim exactly
   (0/1729+ failures for plain Move 1 in Case-(b) instances).
2. Traced the actual winning move sequence on concrete witnesses
   (including a new `m=6` "hereditarily dominant tail" witness I built,
   `A=(0.40,0.35,0.15,0.07,0.02,0.01)`) and **counted real elementary
   splits used**. Found the traced optimal path uses **6** splits for an
   `m=6` (5-mark-budget) instance — one mark over budget.
3. Diagnosed the root cause: `solve(A,budget)`'s `budget` parameter
   tracks only *nested Move-3 (tail-snip) uses*, not real marks — Move 1
   and Move 2 never decrement it, and Move 3 increases `|A|` without
   being charged. This silently grants Xiang Yu one extra free mark per
   Move-3 use, meaning the Round-12 gate "PASS" and the round-13
   outline's Case (a) claim were both evaluated against an
   over-generous, non-faithful model of the real game.
4. Built the corrected `solve2(A,marks)` (single real-marks pool,
   decremented by every move; Move 2 costs `j*` or `j*-1` marks per the
   already-certified DOM-boundary-slack). Re-ran the gate with the
   correct budget `marks=|A|-1`:
   - Genuinely dominant `m=3` configs now correctly FAIL to reach
     `Sigma/2` (confirmed against an independent `scipy` continuous
     brute-force optimizer over the literal constrained game — matches
     exactly, `0.51` with 2 marks, `0.5` needs 3).
   - **Found a genuine counterexample to Case (a)'s claimed "closes
     trivially via Move 1 + IH"**: `A=(0.45,0.20,0.15,0.12,0.08)`, tail
     `T=(0.20,0.15,0.12,0.08)` is honestly Case-C-for-itself (Case a),
     yet `solve2(T,3)=7/25=0.28 > Sigma(T)/2=11/40=0.275`.
   - Brute-force diagnosed the missing move: the true optimum on `T`
     (`0.275`, needs only 2 marks) splits `p_1=0.20` at a **non-half**
     ratio `(0.12,0.08)`, tying it exactly to the **non-contiguous**
     tail subset `{0.12,0.08}` (skipping `0.15`), while independently
     halving `0.15`. This is exactly the already-certified but
     existence-unproven Lemma PAIR-VALUE's general subset-matching
     regime — the long-flagged Hall/donor-matching existence question
     from rounds 9/11/12, shown here to be unavoidable even in the
     "easy" Case (a).

## Verdict
Status remains `partial`. This round does **not** close Lemma
HALF-BOUND or Case C. It makes two honest findings, both recorded in
detail in `results/imo-2026-03/approaches/universal-adversary-strategy.md`
under the new "Round 13 build" section:
- A previously-undetected mark-accounting bug in the entire Round-12
  `solve(A,budget)` formalization (not just the specific Move-3 issue
  the outline-reviewer flagged for Case b) — this invalidates the trust
  basis of the Round-12 gate "PASS" until re-checked with the corrected
  `solve2(A,marks)` accounting given in the file.
- Once corrected, even Case (a) (previously assumed trivial) requires
  the still-open general subset-matching existence question for Lemma
  PAIR-VALUE — narrowing/sharpening, not resolving, the true remaining
  gap. A new concrete witness (`A=(0.45,0.20,0.15,0.12,0.08)`) is
  recorded for the next round to test any future subset-matching
  existence proof against.

No new lemma was proved gap-free enough to certify to `lemmas/` this
round (the corrected `solve2` accounting is a diagnostic/methodological
fix, not a standalone theorem). File written:
`/home/agentuser/repo/results/imo-2026-03/approaches/universal-adversary-strategy.md`.

## Recommendation for next round
Replace the Round-12 `solve(A,budget)` recursion with `solve2(A,marks)`
before any further gate run or proof attempt. Focus directly on the
Hall-type subset-matching existence question for Lemma PAIR-VALUE
(possibly via the `aimo-0063` Hall-deficient-set-deletion technique
already flagged in Round 12 but never attempted) — this is now
confirmed to be the actual crux of Case C, not a bookkeeping detail.
