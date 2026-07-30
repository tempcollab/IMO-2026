# Build report: geometric-dominance-construction, round 9

## Assignment

Attack the same last remaining lower-bound sub-case that
`recursive-embedding-induction` is also attacking this round (cross-piece
tied free coordinate, minority part of a 2-part piece, deep bracket,
companion possibly non-anchor), via a genuinely distinct mechanism: a
direct D-BOUND two-term split at the winning endpoint, per this
approach's own round-9 plan (as opposed to the other approach's
tree/forest-extension route).

## Result: sub-case CLOSED, via a simpler and stronger mechanism than planned

The plan anticipated needing Lemma CROSS-TIE-AFFINE's affine/endpoint
reduction combined with a crude D-BOUND split, with an honest fallback if
the crude estimate proved too weak. What actually worked is simpler and
gives a **stronger** result:

1. **Lemma TWO-BLOCK** (new, fully general, no geometric structure): for
   any sorted nonnegative list and threshold `v`, splitting into `Y`
   (`>v`) and `Z` (`≤v`), `D(list) ≥ (b_1-b_2) - v·[|Y| odd]`, where
   `b_1,b_2` are `Y`'s two largest elements. Proved by a *double*
   application of the already-certified Lemma D-BOUND (peel `Y`'s top
   element, bound the remainder by D-BOUND; separately bound `D(Z)` by
   D-BOUND). Two lines, no new machinery.

2. **Structural Lemma**: for the residual configuration (any set `S` of
   `≥2` pieces of `A_n`, each split into exactly 2 parts sharing a common
   tie value `v` playing the *minority* role in every one — exactly the
   open sub-case), the two globally-largest merged pieces are always
   `b_1 = 2t_1 - ε_0·v`, `b_2 = t_1 - ε_1·v` (`ε_0,ε_1` flag whether the
   top piece / `T_1` are among the split pieces). Proved by direct
   domination case-checks (not just verified numerically).

3. **Main Theorem**: combining 1 and 2, `D(B) ≥ t_n` unconditionally for
   every `n≥1`, every such `S`, and — notably — **every** legal `v` in the
   minority range, not just Lemma CROSS-TIE-AFFINE's D-minimizing
   endpoint. This is strictly stronger than what was asked (the plan only
   needed the endpoint value), and it means this sub-case doesn't actually
   need CROSS-TIE-AFFINE's affine/convexity machinery at all — the direct
   estimate works pointwise throughout the tie's interior.

## Verification (exact-Fraction Python throughout)

- `10,731` exhaustively enumerated small-`n` instances (`n=1..6`, every
  subset `S` with `|S|≥2`, a dense 50-point grid of `v`) — zero
  violations of `D(B)≥t_n`.
- `21,600` randomized instances (`n` up to `12`, random `S`, `v` pushed to
  within 0.1% of its supremum `q`) — zero violations.
- `14,400` further randomized checks confirming the `(b_1,b_2)` structural
  formula matches the actual two largest sorted elements exactly — zero
  mismatches.
- Mandatory reconciliation: reproduced `recursive-embedding-induction`'s
  own cited numeric witnesses (`n=4` symmetric two-minority tie; `n=6`
  external-anchor-snap, `k=1,3,4`) from scratch and confirmed the
  structural formula and resulting bound match those exact numbers — no
  disagreement between the two independent routes.

All scripts left in `/tmp` (`gd_check.py`, `gd_caseB.py`, `gd_general.py`,
`gd_general2.py`, `gd_general3.py`, `gd_diagnose.py`, `gd_stress.py`,
`gd_final_check.py`, `gd_verify_formula.py`).

## What's closed, what's honestly left

Closes the "all-minority, all-exactly-2-parts" cross-tie scenario — which
*is* the previously-open residual sub-case — unconditionally for every
`n≥1`. Combined with the already-certified Lemma CROSS-TIE-AFFINE
(majority-part / ≥3-part sub-cases) and `recursive-embedding-induction`'s
well-separated single-free-coordinate case, this closes gap (b) except for
one narrow, not-separately-verified edge: a `≥3`-part piece with more than
one of its own coordinates independently tied at different values
simultaneously. This is flagged honestly (believed reducible to the
covered cases by peeling one coordinate at a time, but not carried out or
checked as its own claim this round) rather than claimed as closed.

## Files updated

- `results/imo-2026-03/approaches/geometric-dominance-construction.md` —
  new round-9 "Approaches tried" entry, updated "Current best", full
  "Round 9" writeup (Lemma TWO-BLOCK, Structural Lemma, Main Theorem,
  reconciliation, honest scope), new "Promotable lemmas (round 9
  additions)" section. Status remains `partial` (the overall problem still
  needs the upper-bound half and the one narrow edge case noted above).
- `results/imo-2026-03/lemmas/two-block-residue-close.md` — new certified
  lemma file with full proofs and verification detail.
