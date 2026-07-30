# Round 11 — proof-builder report: case-c-secondary-extremality

## Status
unsolved (no proof progress). **Recommend RETHINK.**

## What was done

Per this slug's mandate, ran the cheap feasibility gate *before* attempting
any exchange-argument machinery: tested whether the known true optimal
Xiang-Yu response on the hard `m=5` witness
`A=(1826,1563,1520,1514,765)/7188` (budget 4, target `c(4)=16/31`) is
distinguished among all global-minimum responses by a candidate secondary
statistic (number of exactly-tied Lemma PAIR-VALUE pairs, max possible 4
pairs + 1 single on 9 final pieces).

Exhaustively searched all 70 mark-allocation vectors for this witness
(`scipy.optimize.differential_evolution` + Nelder-Mead per allocation),
then verified the two most interesting findings exactly with
`fractions.Fraction` arithmetic (no floating-point trust).

## Key finding: the gate technically passes but exposes a deeper obstruction

**The global optimum on this witness is not achieved by an essentially
unique response** — at least 17 of the 70 allocations tie at the exact
global minimum. Two structurally unrelated constructions were verified
exactly:

- **Construction A** (matching/residual chain — the one the round-11
  construction-lens explorer hand-reconstructed): `match(p_1,p_2) +
  match(p_3,p_4) + match(p_5\text{-part},r_1) + self\text{-}halve(p_5-r_1)`.
  Final multiset `1563,1563,1514,1514,263,263,251,251,6`: **4 tied pairs +
  1 single**. `oddrank=1199/2396` exactly.
- **Construction B** (pure recursive-halving cascade, unrelated mechanism):
  `self-halve(p_1), self-halve(p_2), self-halve(p_5)` (one mark wasted on a
  degenerate `0`), leaving `p_3,p_4` completely untouched. Final multiset
  `913,913,781.5,781.5,1520,1514,382.5,382.5,0`: **3 tied pairs + 3
  singles**. `oddrank = 1199/2396` — **exactly the same value**, confirmed
  with `Fraction` arithmetic, not floating point.

**This exact tie is not numerology — it's a provable algebraic identity.**
Simplifying both constructions' value formulas symbolically:
`oddrank_A = p_2+p_4+r_1+(p_5-r_1)/2+r_3 = p_1/2+p_2/2+p_3+p_5/2` and
`oddrank_B = p_3+p_1/2+p_2/2+p_5/2` — the **identical expression**,
whenever both constructions' rank orderings hold simultaneously (not a
coincidence of this witness's numbers).

Construction A does have more tied pairs (4 vs 3), so the secondary
statistic narrowly *would* select the correct branch on this one test —
but only because the two constructions turn out to be value-equivalent by
direct algebra, which we can already check by computing each closed form.
**The statistic supplies no independent leverage for identifying the right
closed-form value in general** — proving "the tie-maximal response always
meets the target" for general `m` would still require deriving a closed-form
bound like `p_1/2+p_2/2+p_3+p_5/2 \le c(4)\Sigma`, which is exactly what
`universal-adversary-strategy`'s Route A/B are already trying to do. The
second layer of extremality re-poses the same open question rather than
bypassing it — precisely the failure mode this slug's own "Honest risk
assessment" section warned about in advance.

A further, unresolved complication: some allocations (e.g. `(1,0,1,0,2)`)
have their own internal flat direction (splitting `p_3` anywhere in a range
leaves both fragments at *odd* global ranks, so the split contributes its
full undivided value regardless of where it's cut — not a PAIR-VALUE tie at
all), meaning "the max-tied-pair response" isn't even well-posed without
first canonicalizing which point of a flat cell to count ties in.

## Recommendation

**RETHINK.** The gate did exactly what it was supposed to: it caught, before
any investment in exchange machinery, that this proof shape reduces to the
same open closed-form question the primary approach already owns — the
`minimax-mixed-duality` failure mode CLAUDE.md and this slug's own risk
section anticipated. No genuinely new secondary statistic avoiding this was
found this round. Unless a future round identifies a statistic that
provably does *not* require already knowing the closed-form value (no
candidate found here), this slug should be retired rather than kept alive
as a near-duplicate of the primary approach.

## Files
- `results/imo-2026-03/approaches/case-c-secondary-extremality.md` — updated
  with full gate findings (Status remains `unsolved`).
- `/tmp/round-11/gate_check.py` — allocation-by-allocation numeric scan.
- Exact `Fraction` verification run inline (see file for the reproducible
  session).
