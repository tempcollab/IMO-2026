# Build report — `recursive-embedding-induction`, round 7

## Target
Round-7 outline's two-step plan for Lemma PARITY-PAIR-GEN: (1) Lemma
PARITY-PAIR-ANCHOR (anchor-only closure for all `k`, all tail
distributions — outline expected this to be a cheap corollary of the
existing Lemma PARITY-PAIR), (2) Lemma V'-GEN (multi-free-coordinate vertex
reduction, peeling induction reusing Lemma D-INSERT / Lemma FC).

## What was actually found and proved

**Step 1 was not the free corollary the outline expected — closing it
required a genuine new lemma, now proved.** Checking carefully: Lemma
PARITY-PAIR (as certified) requires every anchor value `t_1,...,t_n` to
appear at least once in the merged multiset. But when a tail piece `T_i` is
itself split, its own baseline copy of `t_i` can vanish entirely (replaced
by finer sub-splits), and I constructed an explicit, budget-feasible
example (`n=4`: split `T_1` once and `P_1` with 3 marks, using all 4 marks,
kills `t_1` from the merged multiset entirely) showing this genuinely
happens within budget — so the literal certified lemma does not cover every
anchor-only strategy.

**Fix: Lemma PARITY-PAIR-GENERAL** (new, `lemmas/parity-pair-general.md`,
certified). Strictly generalizes Lemma PARITY-PAIR by dropping the `c_i≥1`
requirement: for any `c_1,...,c_n≥0` (zeros allowed) with `M:=Σc_i` odd,
`D≥t_n`. Proof is the *identical* strong induction on `n` (Case A/B on
parity of `c_1`), citing the same certified block formula and Lemma
D-BOUND — the induction never actually needed `c_i≥1`. Independently
verified by exhaustive enumeration, `c∈{0,...,4}^n`, `n=1..7`, 97,648
vectors, zero violations (`/tmp/verify_ppg.py`).

**Lemma PARITY-PAIR-ANCHOR** (new, `lemmas/parity-pair-anchor.md`,
certified for full budget). Using Lemma PARITY-PAIR-GENERAL: for every
`n≥1`, every anchor-only strategy using Xiang Yu's **full** budget of `n`
marks gives `D(B)≥t_n` — total piece count is always `2n+1` (odd,
unconditionally), so the generalized lemma applies directly, covering
every `k` and every tail distribution including genuine gaps. This is a
complete, unconditional theorem for full budget.

**Honestly flagged gap (Step 1 residual): partial-budget anchor-only
strategies.** When Xiang Yu uses `b<n` marks, `M=(n+1)+b` may be even, and
Lemma PARITY-PAIR-GENERAL gives no information — moreover the *abstract*
combinatorial statement "M even ⟹ D≥t_n" is provably FALSE in general (a
counterexample is recorded), so this can't be fixed by further abstract
generalization; it needs the game's mark-cost structure. A randomized
simulator (`/tmp/verify_game.py`, n=1..6, 30,000 trials each, including
partial-budget strategies) found zero violations, and hand-checked
extension chains show D decreasing monotonically to exactly t_n at full
budget — suggestive of an "extension-monotonicity" principle that would
close this gap, but a direct proof attempt (tracking sign changes in the
block formula under one extension move) showed the naive approach doesn't
obviously bound the net change. Left open, precisely stated, not
overclaimed.

**Step 2 (Lemma V'-GEN): proved in the "well-separated" case.** Set up the
joint polytope (product over split pieces, since each piece's own sum
constraint is independent of the others) and showed D is linear (not just
affine) within any fixed sort-order cell, so when every free coordinate's
sorted-order neighbors are anchors (not free coordinates from a *different*
piece — "well-separated"), the joint minimization decomposes into
independent per-piece LP-vertex problems, each exactly Lemma V's own
certified mechanism — giving ≤1 free coordinate per split piece, i.e.
Lemma V'-GEN holds in this case.

**Genuinely open sub-case identified precisely: cross-piece ties.** If a
free coordinate's neighbor is a free coordinate from a *different* piece
(no anchor between them), pushing it to that boundary doesn't resolve to
an anchor — it merges the two into a shared undetermined value. I
identified the needed mechanism (treat the tied pair as a shared
multiplicity-2 block, analogous to Lemma PARITY-PAIR-GENERAL's own even-block
handling) but did not work out the resulting recursive bookkeeping — this
is new content, correctly left open rather than hand-waved. No concrete
instance of a genuine (non-flat-face) cross-piece-tied vertex was searched
for this round.

**Peeling induction**, set up formally: well-founded induction on the total
free-coordinate count `F`, reusing Lemma D-INSERT exactly as Lemma FC does
(the affine-in-one-coordinate argument doesn't need any sum constraint to
hold for the hypothetical endpoint values — same technique as Lemma FC's
own proof). Each peel step preserves the total mark budget exactly
(relocating a cut, not adding/removing marks). Consequence: for
well-separated, full-budget configurations, the induction fully reduces to
the proved anchor-only full-budget theorem — **the well-separated,
full-budget sub-case of Lemma PARITY-PAIR-GEN is closed**, modulo whether
well-separation can fail in practice.

## Net result

Two new certified lemma files (`lemmas/parity-pair-general.md`,
`lemmas/parity-pair-anchor.md`), a substantially expanded round-7 section in
`approaches/recursive-embedding-induction.md`, and the Status header
updated. Lemma PARITY-PAIR-GEN itself is **not** fully proved — two
precisely-isolated gaps remain (partial budget; cross-piece coordinate
ties), both narrower and more actionable than the round-6 skeleton's single
monolithic "Case B, genuinely open." The majority of the target's content
(full-budget, well-separated strategies) is now proved, not merely planned.
No overclaiming: Status remains `partial`.

## Files touched
- `results/imo-2026-03/lemmas/parity-pair-general.md` (new)
- `results/imo-2026-03/lemmas/parity-pair-anchor.md` (new)
- `results/imo-2026-03/approaches/recursive-embedding-induction.md` (Status
  header updated; new "Round 7" section appended before "Full proof")
