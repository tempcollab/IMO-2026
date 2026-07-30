# Build report — coupled-cut-descent (imo-2026-03, round 12)

## Status: partial (central mechanism REFUTED)

## Headline
The specified co-varying single-cut descent for GAP-P1′-b is **refuted at `n=5`**. I proved all the
supporting machinery rigorously, but Step 3 (the descent lemma) is FALSE for the move class.

## What I proved rigorously
- **Lemma CM** — the coupled move (within-scale `F'`-merge + free `π_0` repartition into `a_0+2`
  parts) is feasibility- and budget-preserving, `b→b−1`, `a_0+b` conserved. Full proof.
- **Lemma ΔM** — exact effect on `M`: `ΔM = 1_{(0,x)} − 1_{[y,x+y)} + 1_{(0,u_1)} − 1_{[u_2,u)}`.
  Full proof; exact-`Fraction` verified 0 mismatches / 117 000 checks.
- **Lemma TIE** — `D̃=1 ⟹ I_n=0`, so ties are automatically on the good side and the "tie carve-out"
  is *vacuous for the bound* (the induction needs only a non-strict move; ties need no move). This
  corrects the outline premise that the tie family is the real obstruction — it is not.

## The refutation (Prop REFUTE)
Exact enumeration of the full Case-B family:
- `n=3`: 0 failures. `n=4`: 1 failure, and it is a tie (needs no move) → move suffices at `n=4`.
- `n=5`: **8 failures, several non-tie** (`D̃=3`). Explicit witness: `π_0={16,16}`, top rung
  `2^4` cut as `{10,4,2}`, other rungs uncut; `D̃(F)=3`, but the min `D̃` reachable by ANY specified
  move is `5 > 3`. Broadening the freed cut (`a_0+1`-or-`a_0+2` parts) still leaves 7 failures.
The explorer only tested `n=4`, where the sole failure is a tie — which is why the approach looked
viable. It is not: at `n≥5` genuine non-tie configs have no non-increasing single-cut coupled move.

## Structural reason
Failing configs all have `π_0` with equal large parts (`{16,16}`, `{16,8,8}`) and a finely-cut top
rung. A single within-scale merge cannot repair the discrepancy, and `a_0+2` parts of `π_0` are too
few to re-match `F'`. The correct target `F^*` exists in the `(a_0+1,b−1)` slice, but reaching it
needs a GLOBAL re-choice of `F'` ⇒ equivalent to `min_{slice} D̃ ≥ 1`, which is the theorem (circular).

## Recommendation to the orchestrator/outliner
- Retire the co-varying **single-cut** descent family (this approach's mechanism is dead by Prop
  REFUTE, exact `n=5`). Elo should drop; mark `last_outcome=dead-end`.
- The finding confirms the slice-reduction explorer: **`b` is the wrong reduction variable** (flat
  slice-max, zero slack, and now a hard non-tie refutation). Fold `b=0` back into the `n`-peel /
  loaded-IH induction (peel §11.5); do NOT re-seed any `b`-slice descent.
- Salvage: Lemma ΔM and Lemma TIE are clean, reusable, and worth certifying.

## Verification artifacts
`/tmp/verify.py` (FLOOR + slice minima n=4), `/tmp/verify2.py`,`/tmp/verify4.py` (full descent test
n=3,4,5), `/tmp/verify5.py` (target-slice existence), `/tmp/verify6.py` (best-reachable = 5 for the
witness), `/tmp/verify7.py` (broadened move still fails), `/tmp/verify8.py` (ΔM formula, n=5 CE).
All exact `Fraction`.

## Spec concerns
- The outline (and prior explorer/reviewer) framed the tie family as the *only* obstruction and the
  descent as `1395/1396`-good. That is a `n=4`-only artefact. At `n=5` the mechanism has **non-tie**
  failures — the descent is not near-total, it is genuinely broken. The reviewer's dispatch said "if
  the descent resists, leave it as an explicit gap; do not overclaim" — I have gone further and
  *refuted* it with an exact counterexample, so the slug should be treated as dead, not merely stalled.
