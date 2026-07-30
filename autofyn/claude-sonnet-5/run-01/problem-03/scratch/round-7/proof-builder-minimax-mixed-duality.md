# Build report — `minimax-mixed-duality`, round 7

## Task
Attempt a duality certificate over the full discrete tie-structure search
space (Lemma TIE-NECESSARY's structure), targeting the retargeted theorem
"the matching/assignment problem always has a solution `≤c(n)`" — the same
theorem `universal-adversary-strategy` is attacking this round by
matching-induction, but via a genuinely different technique. Mandated gate:
cheap numeric check against the two hard `m=5` witnesses from
`/tmp/round-7/math-explorer-menucoverage.md` (budget 4, `c(4)=16/31`)
before attempting the full argument.

## What was done
Rather than guessing an abstract dual weight vector first, ran the cheapest
possible test: pin down the *exact* winning tie-structure on both witnesses
using `scipy.optimize.differential_evolution` + `Nelder-Mead` polish, then
verify every candidate exactly in `fractions.Fraction` arithmetic (no
floating-point in the final claims). Scripts left at
`/tmp/round-7/dual_probe5.py` and `/tmp/round-7/verify_exact.py`.

## Result: the gate check succeeded numerically but the underlying finding is negative for the "independent technique" goal

**Positive, concrete, exactly-verified result:** both hard `m=5` witnesses
resolve to clean closed forms that beat `c(4)=16/31` exactly:
- `A=(4265,2536,1747,1014,438)/10000`: `oddrank = p_2+p_3+(p_4+p_5)/2 =
  5009/10000 = 0.5009 < 16/31`.
- `A=(3415,3023,1664,1404,494)/10000`: `oddrank = p_1/2+p_3+p_4+p_5/2 =
  2009/4000 = 0.50225 < 16/31`.

Both constructions decompose as (at most) two **disjoint, independent**
moves: a new composite "tie one fragment to the global minimum `p_m`, halve
the residual" (proposed as **Lemma TIE-MIN-HALVE**, proof sketched via the
same rank-shift technique as DOM/HALVE/SANDWICH but **not certified this
round** — flagged as an open item) applied to one piece, plus (in Witness 2
only) an ordinary already-certified Lemma PARTIAL-DOM tie applied to a
disjoint piece. This **overturns** the round-7 explorer's diagnosis that
these witnesses need "genuine 3-piece jointly-tuned coordination" — that
appearance was a numerical-optimizer artifact (a flat direction plus a
near-zero fragment converging slowly), not a real obstruction.

Also closed the outliner's specific request: checked Lemma SANDWICH's
hypothesis (`p_1<p_2+p_m`, `m` odd) on both witnesses exactly. Fails on
Witness 1 (`0.4265>0.2974`). Holds on Witness 2, but SANDWICH alone (1
mark) gives exactly `p_2+p_3+p_5=0.5181>16/31` — insufficient by itself,
confirming the menu gap is real and SANDWICH alone cannot close it.

**Honest negative finding, stated explicitly per the round's instruction:**
the gate check did **not** produce an independent duality/LP shortcut. What
it produced is a *more explicit instance of the same discrete search*
`universal-adversary-strategy` is already running — TIE-MIN-HALVE is a
mechanical generalization of that approach's own PARTIAL-DOM-RESIDUAL
composite (this round's Step 1 target for that approach), just with the
tie target widened to "the global minimum" rather than "an adjacent
piece". No `A`-independent (or simply-parametrized) certificate was found;
an informal attempt at a Farkas/Positivstellensatz-style global certificate
(valid on the whole simplex without case-splitting on `A`) did not turn up
anything even for these two witnesses' local cells. **This approach's
duality-certificate framing has now failed to produce independent leverage
in two consecutive rounds (6 and 7)** — recorded plainly in the approach
file, not glossed over.

## Recommendation for next round
- `universal-adversary-strategy` should pick up **Lemma TIE-MIN-HALVE**
  (stated with a proposed hypothesis in the approach file) as a candidate
  addition to its menu/induction toolkit — it is a natural generalization
  of the composite that approach is already certifying this round, and it
  closes both of this round's hard witnesses.
- The `minimax-mixed-duality` approach itself should be evaluated by the
  outline-reviewer for whether a third round without independent leverage
  should trigger retirement/merge into `universal-adversary-strategy` per
  the CLAUDE.md diversity rule — the file states this explicitly rather
  than asking to be kept alive by default.

## Files touched
- `/home/agentuser/repo/results/imo-2026-03/approaches/minimax-mixed-duality.md`
  — round-7 section appended (gate check, exact witnesses, TIE-MIN-HALVE
  proposal, honest convergence assessment). Status remains `partial`.
- No new file written to `lemmas/` — TIE-MIN-HALVE is **not certified**
  this round (proof sketch only), so per the file contract it stays inside
  the approach file, not the shared certified-lemma cache.
