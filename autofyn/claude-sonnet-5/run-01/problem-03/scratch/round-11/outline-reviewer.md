# Round 11 — outline-reviewer report

## Status of the whole problem (unchanged)

Lower bound fully closed (round 10) — not touched, not re-opened. The
entire remaining gap is `universal-adversary-strategy`'s Claim PTBI Case C
(`p_1<\Sigma(A)/2`), general piece-count `m\ge4`. `m\le3` fully closed.

## Review verdict on this round's two touched approaches

### `universal-adversary-strategy` (revised) — APPROVE the revision, with a correction applied

The Round 11 plan (Lemma MATCH-HALVE-EXISTS, Routes A/B) is well-scoped and
correctly imports round-11's genuine findings (exact reconstruction of the
`m=5` hard-witness optimum; the greedy-matching refutation; the
Hall-transplant-doesn't-fit finding). **However, Route B as written
contains a real mathematical error, caught and fixed this round.**

**The error.** Route B claims that peeling `p_1`-`p_2` into a matched pair
(1 mark) and reattaching the residual `r=p_1-p_2` into the tail gives a
size-`(m-1)` instance to which the induction hypothesis applies at
**full strength `c(m-1)`** (not the "weaker" `c(m-2)`), and that this is
what lets it dodge Round 10's already-proven-insufficient `g(v)` single-
peel-then-bare-IH trap. This is false: Claim PTBI's own statement (restated
at line ~814 of the file: size-`k` list, `\le k-1` marks, target
`c(k-1)\Sigma`) fixes the target index to `size-1`. The reattached tail has
size `m-1` (one residual `r` plus `m-2` original elements), so applying the
IH to it — however the peel was performed — can only license `c((m-1)-1) =
c(m-2)`, never `c(m-1)`. There is no bookkeeping trick that boosts this;
the index is determined by size alone.

**Verified numerically this is not pedantry — it reproduces the exact
Round-10 dead end on the exact witness Route B proposes to test against.**
On `A=(1826,1563,1520,1514,765)/7188` (`m=5`, `c(3)=8/15`, `c(4)=16/31`):
```
p_2 + c(3)(\Sigma-2p_2) = 18647/35940 ≈ 0.51884 > c(4) = 16/31 ≈ 0.51613.
```
Fails, by a margin of the same sign and size as Round 10's `g(v)`
shortfall — because this is structurally the same "one pairing, then bare
`(m-2)`-strength IH" shape (matching `p_1`-`p_2` instead of halving `p_1`),
and the round-11 explorer's own reconstruction of the true `m=5` optimum
independently confirms one pairing is not enough: it needed **two**
simultaneous top-level pairs (`p_1`-`p_2` *and* `p_3`-`p_4`) before any
residual/self-halve step. (For the record: Route B's literally-stated but
erroneous `c(m-1)`-version gives `37815/74276≈0.50911<c(4)`, which is
exactly why the write-up looked like it worked — it silently used too
strong an IH.)

**Action taken:** appended a correction section directly to
`results/imo-2026-03/approaches/universal-adversary-strategy.md` (after the
Round 11 plan) recording this exactly, with the numeric check, so the next
builder does not re-derive or rediscover it. Recommendation baked in:
**Route A (TREE-BOUND-MULTICLUSTER reuse check) is now the clear primary
route; Route B should not be attempted as literally written** — it is only
viable if generalized to "match ≥2 simultaneous top-level pairs before
invoking the IH," which is a different, harder, not-yet-formulated claim.

This is a revision (not a new slug), correctly scoped, no diversity
violation. **Verdict: keep live, build set, Route A prioritized.**

### `case-c-secondary-extremality` (new) — APPROVE, register as backup

Genuinely distinct proof shape (contradiction via a second layer of
extremality, aimo-0438-style) from both of `universal-adversary-strategy`'s
routes (construction / direct induction), correctly scoped to Case C only,
explicitly avoids duplicating the lower bound, Cases A/B, `m\le3`, and the
two already-RETHINK'd framings (`minimax-mixed-duality`,
`relaxed-adversary-transfer`). Its mandated first step (cheap feasibility
gate: check whether the known reconstructed true optimum on the hard
witness is itself distinguished by the candidate secondary statistic,
*before* building exchange machinery) is exactly right per CLAUDE.md's
"prove, don't conjecture" and "honest negative result" rules — mirrors how
`majorization-smoothing` and `potential-averaging-bound` correctly reported
clean negatives rather than forcing false progress.

**Registered** via `register_approach` (was not yet in the ranker sidecar).
Cold-start Elo 1500, now 1495.6 after ranking below.

**Verdict: APPROVE, register, add to build set as backup.**

## Ranking actions

Registered `case-c-secondary-extremality`. Ran `update_ranking` with:
- `universal-adversary-strategy` beats `case-c-secondary-extremality` (live
  primary with certified lemmas and genuine, if incomplete, progress vs. an
  unattempted backup) → universal-adversary-strategy 1582.8→1595.1
- `case-c-secondary-extremality` beats `equalization-potential-bound`
  (weakest live entry, an overclaimed/conditional dead end per its own
  reviewer note) → equalization-potential-bound 1359.7→1349.3
- `case-c-secondary-extremality` draws `potential-averaging-bound` (both
  underdeveloped backups with self-flagged near-duplication risk)

Resulting order (top of field): `recursive-embedding-induction` (1662,
stale/lower-bound-complete) > `geometric-dominance-construction` (1624,
stale) > `universal-adversary-strategy` (1595, **live, primary**) >
`relaxed-adversary-transfer` (1497, dead-end) > `case-c-secondary-extremality`
(1496, **new, live backup**) > `potential-averaging-bound` (1456,
partial/near-dup) > `minimax-mixed-duality` (1445, dead-end) >
`majorization-smoothing` (1376, dead-end) > `equalization-potential-bound`
(1349, dead-end).

No copies requested this round (the outliner did not ask for a branch; the
two candidate routes A/B live inside one slug's revision, which is correct
— they are alternative *fill-ins* for the same gap, not yet two viable
proof shapes both worth independent population slots. If Route A's
structural check comes back negative next round while Route B remains
unfixed, consider copying `universal-adversary-strategy` into a
Route-A-only and a fixed-Route-B-only slug at that point, not before).

## Build set

Two builders, one per slug:

1. **`universal-adversary-strategy`** — attempt Route A first (state Case
   C's existence claim in TREE-BOUND-MULTICLUSTER's forest/tree language,
   check whether the certified multiplier bound forces `oddrank(B)\le
   c(m-1)` directly). Do **not** attempt Route B as literally written (see
   correction above) — if pursuing a peel-and-reattach idea at all, it must
   first be generalized to matching `\ge2` simultaneous top-level pairs
   before invoking the IH, and checked algebraically against the round-10/
   11 hard witness before any full write-up.

2. **`case-c-secondary-extremality`** — run the mandated cheap feasibility
   gate first (does the known true optimum on the hard witness maximize
   the candidate secondary statistic among all TIE-NECESSARY minimizers?);
   only proceed to the exchange-argument machinery if it does, and report a
   clean negative (not forced progress) if it does not.

**build set: universal-adversary-strategy, case-c-secondary-extremality**
