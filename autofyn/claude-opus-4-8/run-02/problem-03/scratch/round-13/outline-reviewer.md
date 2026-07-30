# Outline Review — imo-2026-03, Round 13

Sole open wall is GAP L (lower bound, Case B) ⟺ certified `I_n ≤ 0`, split into `(★)` base slice
(`b=0`, `F'=L`) + the `b`-lift. UB done/certified — untouched. I verified the load-bearing numerics
myself (exact `Fraction`, scripts `/tmp/verify.py`, `/tmp/verify_neg.py`).

---

## peel-scale-rank-induction (advance) — APPROVE (leader, kept live)
Target: whole problem via base-slice `(★)` by weak-majorization / HLP tail-charge on the ladder.
- Sound: `(★-id)`, `(FLOOR)`, peel reduction all certified. WM ON THE LADDER is verified true
  (0/20k my run + explorer's 0/1.8e5) and survived a fresh adversarial red-clustering search — so
  the base-slice WM route is legitimate (it is ONLY the off-ladder generalization that is refuted,
  correctly dropped).
- Open gap unchanged: GAP-P1′-a, the uniform-in-`t` tail-charge (§11.4). The base-slice explorer is
  explicit that this route "has not advanced past stating the target more strongly" — no charging
  function is exhibited. Still the highest-Elo live line and the machinery home, so keep it, but be
  aware it did NOT advance this round.
- Correctly DROPS §11.5's WM-IH `b`-lift (refuted off the ladder, blift explorer 477/12000 +
  1321/60000). Do NOT reopen it. Verdict CHANGES-REQUESTED-class (partial, gap remains).

## ladder-abel-pairing (advance) — APPROVE, but NOT in build set
Target: `(★)` via Abel/parity rung-telescope, positional dual to peel.
- Sound skeleton, imports the same certified reduction. `(m₀≤1)` and `(DOM)` are correct.
- ISSUE (diversity): the base-slice explorer finds abel and peel §11 "are at the SAME place" — both
  bottom on "one odd rung dominates its whole lower tail," differing only in packaging (global
  tail-sum vs pairing rewrite). Step 3 (the rung-telescoped inequality) and step 4 (the global
  parity closer) are both ASSERTED, not built; "parity of `ΣL` forces residual ≥0" gives only
  integrality, not sign, as written. Real but same-wall as peel — building both wastes budget this
  round. Keep live, do not build.

## ladder-length-deficient-induction (NEW) — APPROVE, REGISTERED, BUILD
Target: `(★)` via mutual induction on ladder length `m` (`P_m` deficient-total coupled to `Q_m`
complementary-parity). Genuinely far from value-domination / Abel — a two-branch length induction
with a parity role-swap, living inside `π_0` vs a ladder.
- I re-verified both lemmas exactly: `(P_m)` 0 fails / 20k per `m=1..6`, `(Q_m)` 0 fails / 20k per
  `m=1..6`, BOTH tie-break conventions. The per-part `≤2^m` cap in `(Q_m)` is load-bearing —
  dropping it fails ~9% at `m=2` (matches the outliner's ~8.6%). Constraints are real, not artifacts.
- Structure is sound: `(P_m)` Branch 1 (pair-removal → `(P_{m-1})`) and Branch 2 (role-swap →
  `(Q_{m-1})`) are the explorer's proven probe3/probe9 identities. The SOLE open gap is the `(Q_m)`
  recursion (step 4) — a clean, self-contained, isolated inequality with the constant
  `2^{m+1}−1−ΣR` tracked across a two-branch (up-to-two-reds) peel. This is the most tractable and
  most-advanced base-slice route (per the explorer, the only opening that advanced this round).
- Build directive: carry BOTH caps (part-count AND total, resp. `≤2^m`) at every recursion level and
  re-verify each branch re-satisfies them; preserve the per-part cap in the `(Q_m)` step. Do NOT let
  it collapse to a positional running-margin scan (refuted).

## qlayer-charge-induction (NEW) — RETHINK, NOT REGISTERED (fatal flaw)
Claimed to be the independent `b`-lift specialist/hedge (numeric negative-layer loaded IH, no ladder).
**Its declared step-1 reduction is INVALID: it proposes to prove a statement that is FALSE.**
- Step 1: from certified `(POS)` `P ≤ S_π` it concludes "suffices to prove `(NEG) Q ≥ S_π` for every
  `π_0`." Sufficiency is real (`Q≥S_π ⇒ Q≥P ⇒ I_n≤0`), but `(NEG)` is not a hypothesis one may hope
  to prove — **it is false.** I checked exactly (`/tmp/verify_neg.py`, faithful feasible peels with the
  correct dyadic-scale `F'` structure and budget `a_0+b≤n`):
  - `Q ≥ S_π` FAILS 50–77% of feasible configs across `n=1..6` (n=1: 9986/20000, n=6: 15464/20000).
  - It fails STRUCTURALLY at the entire tie family (`I_n=0`, `D̃=1`): the simplest tie
    `π_0={1,1}, F'={1}` gives `Q=0` but `S_π=1`; `π_0={2,2}, F'={2,1}` gives `Q=0`, `S_π=2`. At every
    tie `Q=P`, and `S_π>P` generically, so `Q≥S_π` is false exactly at the extremal configs the
    approach must handle.
- Root cause: `(POS)` bounds `P` from above by a `π_0`-ONLY quantity `S_π` that is generically far
  larger than the actual `P` (because `F'` cancellation shrinks the true positive layers). Decoupling
  `P` from `F'` throws away the very cancellation that makes `I_n≤0` true — this is a re-entry of the
  banned "decoupled/scalar-summary of one side" trap in `(POS)` clothing. The step-2 design object is
  worse (`Q≥Φ≥max_{π_0}S_π` is even stronger and equally impossible).
- Verdict RETHINK: return to the outliner. The `b`-lift needs a route that bounds `Q` against the
  ACTUAL `P` (both `π_0`- and `F'`-coupled), not against `S_π`. Do NOT register; junk stays out.

## coupled-cut-descent (RETIRE) — marked dead
Single-cut co-varying `b→b−1` descent rigorously refuted R12 (`n=5`, `π_0={16,16}`, `D̃(F)=3` but min
reachable `D̃=5`). Ranked as a loss to every live sibling. Lemma TIE / Lemma ΔM salvage is the
builder's/reviewer's to bank; the mechanism is dead. allocation-vertex-corner already dead (R11),
re-anchored as a loss this round.

---

## Field-level flags for the orchestrator
1. **The `b`-lift (GAP-P1′-b) now has NO live route.** coupled-cut-descent dead, WM-IH refuted
   off-ladder, and qlayer (the sole proposed `b`-lift specialist) is doomed at its reduction. Even if
   `(★)` is fully proven this round, the whole problem does NOT close — the general-`b` lift remains
   open. NEXT ROUND MUST seed a genuinely new `b`-lift framing (blift-explorer opening 1 —
   rank/parity-aware charge tailored to `π_0`'s even-rank breakpoints, NOT a value-sorted threshold
   family — or opening 3 done correctly: bound `Q` against the true coupled `P`, not `S_π`).
2. **Base-slice diversity is thinner than it looks.** peel §11 and ladder-abel share ONE wall (the
   uniform tail-charge) per the explorer. ladder-length is the only genuinely distinct and only
   advancing base-slice mechanism. So effective diversity on `(★)` this round = 2 (length-induction +
   value/Abel-cluster), not 3.
3. Plateau continues (R3–R13) but ladder-length isolates `(★)` to one clean recursion — the sharpest
   base-slice handle yet.

build set: ladder-length-deficient-induction, peel-scale-rank-induction
