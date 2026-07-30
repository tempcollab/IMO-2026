# Build report — geometric-dominance-construction, round 8

## Task
Second, independent route to gap (b) of `recursive-embedding-induction`'s
Lemma V'-GEN (cross-piece tied free coordinates): explicit slope
computation on the D-INSERT cell, per this round's outliner/outline-
reviewer assignment. Cross-verification of `recursive-embedding-
induction`'s parallel route to the same sub-gap this round.

## Result: Status = partial (real, substantive new progress; gap
sharpened, not fully closed)

Proved a new lemma, **Lemma CROSS-TIE-AFFINE**: for any cluster of `k≥2`
mutually tied free coordinates from distinct split pieces of `A_n`, `D` is
affine in the shared tie value with an explicit computable integer slope
`M` (derived from a closed-form per-piece sign/rank formula), so an
interior tie is never a *strict* local minimizer of `D` — pushing to a
boundary of the affine cell weakly decreases `D`.

Discovered and proved a new structural fact along the way — **the
self-meeting-point-is-an-anchor fact**: for any piece of `A_n` split into
exactly 2 parts, the value at which its two parts coincide
(`top_π/2`) is *always itself an anchor* (a one-line consequence of
`t_i=2t_{i+1}`, previously unstated). This shows the affine-slope
reduction lands on a **zero-residue, fully anchor-resolved
configuration** whenever the tied coordinate is the majority (larger)
part of a 2-part piece, or belongs to a piece with ≥3 parts (the latter
exactly reproducing `recursive-embedding-induction`'s already-closed
well-separated single-free-coordinate case as the `k=1` special case of
the new formula).

**Honest residual gap, precisely isolated (narrower than the prior "any
cross-tie" framing):** when the tied coordinate is the *minority*
(smaller) part of a 2-part piece, in a bracket strictly deeper than that
piece's own natural halving level, pushing to the winning *external*
anchor endpoint can leave the companion part at a fixed but generically
**non-anchor** value — a genuinely new residue phenomenon not present in
the narrower Proposition K/Lemma FC setting (there `π=P_1` always has
`≥n+1≥3` parts for `n≥2`, so this subtlety never arose). This is not
closed this round. One concrete numeric probe (`n=5`) found the slope
identically `0` in this residual sub-case (non-competitive, `D=21≫t_5=1`
— far from threatening the bound), consistent with but not a proof of
harmlessness in general.

**Reconciliation check (mandated by the outline-reviewer):** compared this
route's conclusions against `recursive-embedding-induction`'s parallel
tree-peeling/shared-block route to the same gap. **No disagreement
found.** Both independently conclude ties are never strict minimizers and
both independently arrive at the same "even-multiplicity shared block"
reduction mechanism in the closed sub-case — a genuine cross-verification,
not a re-derivation of the same proof.

## Files updated
- `results/imo-2026-03/approaches/geometric-dominance-construction.md`:
  new "Round 8" section (full statement, proof, and honest gap of Lemma
  CROSS-TIE-AFFINE and the self-meeting-point fact); Status/Approaches
  tried/Current best updated at the top of the file.
- `results/imo-2026-03/lemmas/cross-tie-affine.md`: new certified-lemma
  proposal (both results, full proofs, honest scope statement).

## Verification performed
- `/tmp/verify_formula.py`: 5000 random exact-`Fraction` trials of the
  pairwise (`k=2`, no companion) affine formula `D(y,y')=D(C_bg)+σ|y-y'|`
  — zero mismatches.
- `/tmp/verify_n2.py`, `/tmp/verify_n3.py`: reproduced the round-8
  math-explorer's exact `n=2,3` cross-tie examples from scratch, confirmed
  `D(v)` is exactly affine (`D=-2v+C` in both cases) and that the true
  minimum sits at the anchor-snapped endpoint (`D=t_n`), not the interior
  tie (whose value, `D=3` in both cases, matches the explorer's report
  exactly).
- `/tmp/verify_residue.py`: one representative `n=5` instance of the
  residual (minority-part, deep-bracket) sub-case; slope `M=0`, `D=21`,
  far from the target `t_5=1` — non-competitive in this instance.

## What remains
The precise remaining content of gap (b) is now: does the
"minority-part, deep-bracket" residue sub-case of a cross-tie ever produce
`D<t_n`? This is narrower and better-isolated than before this round
(previously "any genuine cross-tie" was open; now only this one specific
residue phenomenon is). Recommend next round either (a) extend Lemma
CROSS-TIE-AFFINE's argument recursively (the residue, once fixed, is
itself just an ordinary value in the merge — likely amenable to the
already-certified Insertion Lemma or a further induction on `n`), or (b)
check whether `recursive-embedding-induction`'s shared-block mechanism
handles this exact sub-case already (their write-up did not separately
flag it, so it may or may not already be covered).
