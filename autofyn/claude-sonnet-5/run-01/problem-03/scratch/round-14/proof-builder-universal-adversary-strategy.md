## imo-2026-03 — proof-builder report, universal-adversary-strategy, round 14

### Task
Rebuild the certified recursion with correct real-mark accounting (single
shared counter, every move charged, cap `m-1`), add Move 0 (skip-if-tied,
checked anywhere) as a genuine zero-cost move, attack the subset-match
existence question (Lemma SLACK-COVER) via a from-scratch induction (not an
`aimo-0292` import), and make explicit how the covering induction interacts
with the recursive mark budget.

### What was done
1. Defined and implemented `solve2(A,marks)` exactly per the round-14
   outline's spec: one shared real-mark counter, initialized to `|A|-1`,
   decremented by the true cost of every move (Move 1/halve: 1; Move
   3/tail-snip: 1; Move 2/subset-match: `|S|` or `|S|-1` at the exact
   residual boundary; Move 0/skip-tie: 0).
2. **Proved and certified Lemma FREE-TIE-REDUCTION** (new lemma file,
   `results/imo-2026-03/lemmas/free-tie-reduction-move0.md`): for any
   sorted list with an even-multiplicity tied run of length `2j` anywhere
   (not just a top prefix), `oddrank(A) = jv + oddrank(A')` exactly, at
   zero cost, where `A'` is `A` with the run deleted. Proved from scratch
   via the pairing argument (each pair of the run straddles exactly one odd
   and one even rank, and the even-length deletion preserves parity for
   everything before/after the run). This directly fixes the outline-
   reviewer's flagged scope gap (the outline's Move 0 only checked top-
   prefix ties).
3. Re-verified well-foundedness of `solve2` including Move 0, using
   `(marks,|A|)` lexicographic with `marks` primary (Move 0 leaves `marks`
   fixed but strictly shrinks `|A|`; every other move strictly decreases
   `marks`, and Move 2's only zero-cost sub-case is already caught by
   Move 0 first, so it never needs separate zero-cost handling).
4. **Numerically verified (exact `fractions.Fraction`, script `/tmp/
   solve2.py`)** the corrected menu (Move0-general + Move1 + Move2-any-
   subset + Move3) against three witnesses:
   - `A=(26,21,10)/57` (m=3): `solve2 = 31/57 ≈ 0.5439 ≤ c(2)=4/7` —
     reproduces the round-13-reviewer's independently-found true 2-mark
     optimum exactly, this time from a proved move menu rather than a
     numeric optimizer alone.
   - `T=(0.20,0.15,0.12,0.08)` (m=4): `solve2 = 11/40 = Σ/2` exactly, via
     the non-contiguous match `{0.12,0.08}` (skipping `0.15`) that the
     old contiguous-only menu could not express.
   - `A=(965,965,958,482)` (m=4, new witness): `solve2 = 1685 = Σ/2`,
     well under target `5392/3≈1797.3`. Move 0 fires on the pre-existing
     tie `965=965` (banks 965 for free), leaving the whole 3-mark budget
     for the dominant sub-instance `(958,482)`, closed by two Move-1
     halvings. Confirms Move 0 is genuinely load-bearing.
   - The round-12 `m=8` witness was attempted but the reference
     implementation (exhaustive `2^|tail|` subset search at every
     recursion level) **timed out** (>5 min, no result) — recorded
     honestly as untested, not a finding either way.
5. **Attacked Lemma SLACK-COVER from scratch.** Derived a genuine (not
   imported) analogue of `aimo-0292`'s mesh bound using the problem's own
   structure (`t_i ≤ p_1` for every tail element, since `A` is sorted with
   `p_1` the max), giving a bounded-gap prefix-sum argument. **Found this
   bound is not the missing ingredient**: it only proves a size-only
   covering statement (some affordable subset is within `p_1` of the
   target), which the T=(0.20,0.15,0.12,0.08) witness already shows is
   insufficient — the contiguous prefix match satisfies any such mesh
   bound yet is provably suboptimal; the real obstruction is that the
   *chosen* subset's cost must also leave enough remaining budget for the
   leftover's own recursive value to meet the target, i.e., the existence
   claim needed is a joint covering-plus-recursive-value statement, not a
   pure subset-sum covering statement. Made this interaction with the mark
   budget fully explicit: any correct Lemma SLACK-COVER must be proved as
   an inductive step *inside* the same `(marks,|A|)` induction, not as a
   free-standing lemma on `T` alone. **This lemma is NOT closed this
   round** — reported honestly as the sole remaining gap, more precisely
   characterized than before.

### Certified this round
- `results/imo-2026-03/lemmas/free-tie-reduction-move0.md` — Lemma
  FREE-TIE-REDUCTION, proved in full, general position, general even
  multiplicity.

### Status of `universal-adversary-strategy`
`partial`. Real progress (correct recursion, Move 0 fixed and generalized,
three witnesses verified, SLACK-COVER's true difficulty precisely
characterized), but Case C for general `m≥4` remains open — Lemma
SLACK-COVER is unproved.

Files touched:
- `/home/agentuser/repo/results/imo-2026-03/approaches/universal-adversary-strategy.md`
  (new "Round 14 build" section appended)
- `/home/agentuser/repo/results/imo-2026-03/lemmas/free-tie-reduction-move0.md`
  (new)
- `/tmp/memory/proof-builder.md` (2 new rules appended)
