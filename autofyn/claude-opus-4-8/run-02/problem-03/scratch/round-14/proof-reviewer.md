# Proof-reviewer report — imo-2026-03 (IMO 2026 P3), Round 14

Sole open wall reviewed: the b-lift (GAP-P1′-b) — derive general-`b` `I_n≤0` (`D̃(π_0⊎F')≥1`) from
the PROVEN/certified base slice `(★)`. Upper bound + Case A + `(★)` are DONE/certified and were NOT
re-reviewed. Two slugs built this round; both honestly report they hit the shared overlap wall. I
independently verified every claimed identity (exact `Fraction`, script `/tmp/verify.py`).

## Independent verification (all 0 fails)
| claim | result |
|---|---|
| (I1′) clean split-rung form (split-rung) | **FALSE** — witness `m=2,R={1},ρ_1={3/2,1/2},Z'={1}`: true `Δ_2=3/2`, clean form `3` (matches builder's 3931/4000) |
| (†) split-rung peel `D̃(R⊎ρ_1⊎Z')=D̃(R⊎Z')+D̃(ρ_1)−2λ(O_{ρ_1}∩O_{R⊎Z'})` | TRUE 0/4000 (= certified SD/PEEL) |
| (I3′) generalized red-peel `D̃(R⊎Z)=y−D̃((R∖y)⊎Z)`, blue`≤θ`, `y=maxR>θ` | TRUE 0/2048 |
| ABSORB `Δ(R,Z)=θ+Δ(R⊎π_1,Z')` | TRUE 0/3000 (multiset regrouping) |
| MAXPEEL `D̃(P)=max(P)−D̃(P∖max(P))` | TRUE 0/5000 |

I also confirmed the absorb "tautology" algebra: `R̄⊎F''=π_0⊎F'` as multisets ⇒ the reduced statement
`Δ_m(R̄,F'')≥−θ` is literally the target `D̃(π_0⊎F')≥1`; and the rescaled bound `min(0,2^m−ΣR̄)=−2θ`
is strictly weaker than the trivial `D̃≥0` bound `−θ−½` (by `θ−½`). Both builders' negatives are
honest and correct — this is NOT a rubber-stamped "we hit the wall."

---

## Slug 1: split-rung-mutual-induction

**Verdict: RETHINK.  True Status: unsolved (as an engine).**  Builder's recorded Status `partial` is a
slight over-label — the load-bearing outline identity is FALSE and the honest version is a verbatim
re-encoding of the certified GAP-P1 wall, so as a b-lift engine it is unsolved/broken, not
"progressing partial." (The banked lemma below is the only surviving value.)

- Correctness: 5/5. Every stated fact is correct; the FALSE identity is correctly identified as false.
- Completeness/rigor: 4/5. Honest, precise, no hidden gaps.
- Progress toward closing the wall: 1/5. The route provably re-encodes the shared overlap wall.

Why RETHINK: the mechanism the outline hinged on (a CLOSED alternating-sum sign-flip correction) is
factually wrong; the true correction is the odd-set overlap `I_S=λ(O_{ρ_1}∩O_{R⊎Z'})` = GAP-P1
verbatim. Dropping `I_S` telescopes to a vacuous bound. The framing cannot close; back to the outliner.

## Slug 2: absorb-rescale-induction

**Verdict: RETHINK.  True Status: unsolved (as an engine).**  Recorded Status `partial` is acceptable
as a label but the engine is broken: ABSORB on this instance is a tautology (advances no bound), the
proposed rescaled closer is strictly weaker than doing nothing, and its only scale-reduction step runs
through split-rung's `(I1′)` — so it is not even independent of Slug 1.

- Correctness: 5/5. Tautology and weaker-than-trivial claims independently confirmed.
- Completeness/rigor: 4/5. Honest, exact, correctly identifies non-independence.
- Progress toward closing the wall: 1/5. Reduces to the split-rung wall; no new closing content.

Why RETHINK: the rescaled deficient-bound engine (GAP-A1/A2) is provably weaker than the trivial
measure bound, so it cannot inject the missing ½; the framing cannot close as posed.

---

## Lemma certification

**CERTIFIED:** `results/imo-2026-03/lemmas/top-peel-general.md` — the general top-peel
`D̃(P)=max(P)−D̃(P∖max(P))` (absorb's MAXPEEL) together with its arbitrary-blue red-peel corollary
`(I3′)` (split-rung). Both are correct, exactly verified (0 fails), and reusable; I merged them into
one master lemma since MAXPEEL subsumes (I3′). Both are immediate consequences of Lemma G's
alternating-sum form and strictly generalize the certified (I3) (blue`=L_m` only) in
`base-slice-star.md`. The file explicitly flags them as bookkeeping tools, NOT a closer (they reduce
`ΣR` but not the dyadic scale, and leave the split-top-rung overlap wall open).

The split-rung `(†)` identity is a direct corollary of already-certified SD/PEEL + Lemma G — not
separately certified, but noted so no future round re-proposes the FALSE clean `(I1′)`.

## Meta for the orchestrator (diversity collapse)
Both b-lift approaches bottom out on the SAME object — the split-top-rung odd-set overlap
`λ(O_{ρ_1}∩O_{R⊎Z'})` = GAP-P1. They are not independent (absorb's only closer is split-rung's
`(I1′)`); under the single-gap rule they die together. Per CLAUDE.md's shared-gap rule, next round the
outliner MUST seed ≥1 genuinely different b-lift framing attacking the overlap term with a NON-scalar
loaded invariant on `F'`'s recursive cut-tree — not another top-rung peel. `current.md` updated
(Status stays `partial`; both slugs recorded RETHINK/unsolved; R14 meta added).

Round routing: split-rung-mutual-induction → RETHINK; absorb-rescale-induction → RETHINK.
No APPROVE. Whole problem remains `partial` (UB + `(★)` + Case A certified; b-lift open).
