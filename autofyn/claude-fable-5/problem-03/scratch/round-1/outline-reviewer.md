# Outline review — imo-2026-03, round 1

Field: three fresh approaches, all targeting the whole claim c(n) = 2^n/(2^{n+1}-1) end to end (construction AND cap). Framings are genuinely distinct — recursive/inductive, potential-scalar, variational/structural — so the field is not in the single-gap trap; they share only the greedy-claiming lemma (a settled-looking exchange argument, appropriate as shared infrastructure, to be certified once in `lemmas/greedy-claiming.md`).

## Verification I ran

- Exact rationals (n = 1..8): c(n-1)(1-c(n)) = c(n)/2 and 1/2 + c(n)/2^{n+1} = c(n) both hold — the two identities Cases A/B and the C(m) candidate lean on are real, with zero slack as claimed.
- Case-split exhaustiveness of A/B/C/D over (a1, a2): verified logically (if a2 >= c/2 -> B; else if a1 >= c then a2 < c/2 <= a1/2 -> A; else a1 >= 1/2 -> C, else D). Sound.
- Brute-force grid search of the n = 2 game: ladder value ~ 0.5714 = 4/7 (confirms the conjectured answer); five Case-D partitions (a1 < 1/2, a2 < 2/7) all have Xiang replies well below the C(2) cap max(a1, 1/2 + a1/8) — no counterexample to the strengthened hypothesis.
- Slope claim in tie-structure Step 2: moving a cut changes the two sub-pieces by +-dt; d(Liu)/dx = [sub1 odd-rank] - [sub2 odd-rank] in {-1, 0, +1}. Correct as stated.
- Discrepancy identity: Liu - Xiang = sum of (a_{2i-1} - a_{2i}) + a_{2n+1} with zero padding; with Liu + Xiang = 1 gives Liu = 1/2 + Delta/2. Correct; Delta >= 0 termwise so Liu >= 1/2 is indeed free.

No approach repeats a recorded dead end (the refuted (n+1)/(2n+1) formula and equal-piece openings appear only as recorded warnings, not as strategies).

## dyadic-recursion-induction — CHANGES REQUESTED

Right technique, strongest concrete footing (three pre-verified exact identities, Cases A-C essentially mechanized). Fixable issues for the builder:

1. **Step 4, Case D / C(m) restructures the whole induction (main issue).** If the strengthened claim C(m) "cap <= max(a1, 1/2 + a1/2^{m+1})" is adopted, the induction hypothesis changes — Cases A, B, C must then be re-proved to deliver the *strengthened* cap, not merely <= c(n). Spot-check for Case A: bound a1/2 + c(n-1)(1-a1) minus a1 has slope 1/2 - c(n-1) - 1 < 0 and vanishes at a1 = c(n), so <= a1 for a1 >= c(n) — it goes through, but each case needs this done explicitly. Also state C(m) scale-invariantly, since it will be applied to the tail instance scaled by (1-a1).
2. **Step 3, j >= 1 sub-case is under-specified.** "Recurse on the (n-1)-ladder formed by the untouched rungs" is imprecise: if Xiang's cuts land in middle rungs, the untouched rungs are an arbitrary subset of {2^n, ..., 1} units, NOT a scaled dyadic ladder D_{n-1}. The induction must be set up on a claim general enough to cover subset-of-rungs multisets (or induct on a different parameter). This is the real content of G1 — the current sketch would not build as written.
3. Minor: in Cases A/B, state that all sub-pieces of the refined tail stay <= the top pair value (they only shrink), so pair-collapse legitimately applies to the *refined* multiset, not just the tail partition.
4. Case C's remainder-interleaving is actually clean: iterate pair-collapse from the top; after all pairs collapse, only r remains, so Liu = (1-a1) + r = a1 exactly. The builder should write it via iterated Step 2 with an explicit tie-breaking convention — this sub-gap of G2 is essentially closed.

## discrepancy-halving — CHANGES REQUESTED

The reformulation (Steps 1-2) is exact and is genuine progress on its own. The two hard cores are honestly flagged. Issues:

1. **GAP U: the naive halving invariant is insufficient as literally stated.** "n cuts drive Delta to ~a1/2^n" fails for a1 near 1 (1/2^n > 1/(2^{n+1}-1)); the first bisection there exploits self-pairing and drops the residual to ~(1-a1)-scale, which is why the true constant involves the sum constraint. Before grinding, the builder must state the correct potential/invariant (what exactly halves, and against what baseline) and verify it on the ladder (where every step is tight) AND on a1-near-1 partitions.
2. **GAP L: keep the flow/matching form.** The file itself correctly notes per-rung accounting is unsound (an uncut small rung can pair against an equal sub-piece of a cut large rung). Any draft that slips back to per-rung bookkeeping should be self-rejected. Also honor the file's own warning: no integrality/parity-in-units argument — cuts are real-valued.
3. Minor: the potential must be defined on the final sorted multiset or proved monotone under insertions (the file flags this — keep it as a stated lemma, not a remark).

## tie-structure-variational — CHANGES REQUESTED

Highest risk, highest payoff; the framing is genuinely different from the siblings and worth one builder. Issues:

1. **GAP T:** the slope computation is right, but the termination monovariant ("each move increases the number of ties") must survive simultaneous re-sorting; moving to the *nearest* pattern boundary is the right move — make the monovariant precise (e.g. lexicographic: ties count, then something that rules out cycling at slope-0 moves).
2. **GAP C is the make-or-break:** the catalog must be proved exhaustive AND stay manageable (polynomial-ish or recursively organized). Honor the file's own kill criterion: if the catalog explodes into the induction approach's casework, this slug should be declared a dead end rather than duplicated effort — that overlap is the one way this field collapses to one framing.
3. Degenerate/boundary replies (a cut sliding to an endpoint = Xiang using fewer cuts) must be first-class catalog entries, not an afterthought — the minimizer may be on that boundary.

## Ranking and selection

All three registered fresh at 1500. Ranked head-to-head on concreteness of footing and how well-scoped the remaining gaps are:

- dyadic-recursion-induction > discrepancy-halving (three exact identities verified, three of four upper-bound cases mechanized, one well-scoped hard gap vs. two symmetric hard cores)
- dyadic-recursion-induction > tie-structure-variational (same, vs. four open gaps and a known blow-up risk)
- discrepancy-halving > tie-structure-variational (exact reformulation already banked vs. everything still open)

Post-update Elo: dyadic-recursion-induction 1531, discrepancy-halving 1500, tie-structure-variational 1469.

All three go to builders this round: round 1 information value is high, the framings are far apart, and each has a concrete first task (certify greedy-claiming once for the field — first builder to touch it writes `lemmas/greedy-claiming.md`; the others import).

## Field-diversity note for the orchestrator

Healthy for round 1: three distinct framings, one shared (low-risk) lemma. Watch next round: if both dyadic-recursion's G1 and discrepancy-halving's GAP L stall on the *same* obstruction (accounting for an uncut rung pairing against sub-pieces of cut rungs — the two gaps are secretly cousins), that is a shared wall forming; the answer would be a genuinely different framing (e.g. strategy-stealing/symmetrization or a direct weight-function certificate), not another route within these two.

build set: dyadic-recursion-induction, discrepancy-halving, tie-structure-variational
