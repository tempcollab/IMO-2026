# Outline-review report — round 7 (imo-2026-03)

## Ground-truth cross-check

Read `current.md` and the relevant approach/lemma files directly (not just
the outliner's summary). Confirmed accurate:

- Proposition K (`k=n`, tail-untouched lower-bound sub-case) is **fully
  closed for every `n`**, via Lemma L (`lemmas/parity-pair-lemma-L.md`,
  `recursive-embedding-induction`) + Lemma FC
  (`lemmas/lemma-V-prime-free-coordinate.md`,
  `geometric-dominance-construction`), both independently reviewer-verified
  per `current.md`'s round-6 catch-up review.
- `universal-adversary-strategy`'s round-6 lemmas (PARTIAL-DOM certified in
  full; TIE-NECESSARY's disjunctive conclusion sound but `dim(Q)=0` branch
  write-up flawed) match the approach file's own "Approaches tried" entry
  verbatim.
- `minimax-mixed-duality`'s Lemma SANDWICH is certified
  (`lemmas/sandwich-split.md`); its LP-duality-over-named-menu framing was
  honestly diagnosed as not shortcutting casework.
- `geometric-dominance-construction` has no open target of its own left —
  Lemma FC closed its assigned scope; the outliner correctly does not
  re-nominate it for a fresh target without instruction.
- Standing-dead approaches (`majorization-smoothing`,
  `equalization-potential-bound`) and the retired
  `potential-averaging-bound` are correctly excluded from any revival by
  the outliner — no attempt to sneak them back in.

The two remaining gaps are correctly and sharply isolated exactly as
`current.md` states: (1) lower bound, general `0≤k<n` with tail
simultaneously refined (Lemma PARITY-PAIR-GEN); (2) upper bound, arbitrary
configurations, general `n≥2` (menu-coverage / matching-assignment
optimality).

## Gate decisions

**`recursive-embedding-induction` — APPROVED, advance.** Step 1 (Lemma
PARITY-PAIR-ANCHOR) is a legitimate, low-risk mechanical assembly of
already-certified Lemma PARITY-PAIR + Lemma 3 — correctly scoped as "should
close outright." Step 2 (Lemma V'-GEN / peeling induction) is honestly
flagged as unproved with two explicit named risks (the vertex-generalization
claim itself, and the un-ruled-out two-simultaneous-free-coordinate case).
No unjustified leap — the outliner requires the builder to *check*, not
assume, the generalization. Approved as written.

**`universal-adversary-strategy` — APPROVED, advance.** Two cheap
compositional lemmas (PARTIAL-DOM-RESIDUAL, MULTI-HALVE) are genuine
mechanical compositions of certified tools with concrete witnesses to
reproduce — good de-risking discipline. The TIE-NECESSARY `dim(Q)=0` fix is
correctly scoped as a bookkeeping correction, not new mathematics. Step 3's
retarget from "grow the menu" to "prove the matching/assignment theorem" is
the right move — flagged explicitly as exploratory/partial, not oversold.
Approved.

**`minimax-mixed-duality` — APPROVED, advance.** Retargeting the duality
framing at the general discrete search (not the fixed named menu) is a
legitimate distinct technique on the same retargeted theorem as
`universal-adversary-strategy`, which is the correct way to keep two
approaches on one theorem without them collapsing into duplicates — LP/
duality vs. direct casework-induction are genuinely different proof shapes.
The mandated cheap numeric gate (check the dual weighting against the two
recorded `m=5` witnesses before committing to a general proof) is properly
sequenced before the expensive work. Approved.

**`relaxed-adversary-transfer` — APPROVED, register as new.** Checked this
against the single-gap-trap mandate specifically: is it a genuine
structurally different mechanism, or a rename of the menu-composition
approaches? Verdict: genuine. The three live upper-bound approaches
(`universal-adversary-strategy`, `minimax-mixed-duality`,
`geometric-dominance-construction`, when it had an upper-bound target) all
share **enumerate configuration types, exhibit a matching named move**
(DOM/HALVE/SANDWICH/PARTIAL-DOM/...) as the underlying mechanism — even
`minimax-mixed-duality`'s LP framing operates over that same named-move
space. `relaxed-adversary-transfer` instead proposes **relax the game to
unlimited splits, solve/compute the relaxed optimum in closed form, then
prove a truncation/transfer lemma** — a mechanism with no enumeration of
named moves at all. This is a legitimate different-mechanism import
(`aimo-0560` gardener–lumberjack surrogate-adversary pattern), not a
rename. The outliner correctly gates the first build to the cheap numeric
step (compute `V_∞(A)` on 2–3 small configurations) before any transfer-
lemma attempt, and correctly flags the honest-stop condition if the
relaxation needs unboundedly many marks to approach. Registered at cold-
start Elo 1500.

One caveat for the builder to state explicitly in the file (per the
outliner's own instruction, reinforced here): if the cheap gate's Step 3
outcome turns out to be "the `∞`-mark optimum is achieved at a finite
anchor-tie configuration," that specific sub-finding *converges* with
`universal-adversary-strategy`'s target (both would then be proving "the
discrete tie-search is complete") — that convergence is fine as a
cross-check but must not be written up as if `relaxed-adversary-transfer`
independently closes the gap in that scenario; the file must state which
proof (if either) is actually load-bearing.

**`geometric-dominance-construction` — kept live, no build slot.** No new
target assigned this round; correctly excluded from the build set rather
than force-fed unrelated work.

**Standing dead/retired, confirmed not revived:** `majorization-smoothing`
(RETHINK, structural non-concavity proof, correct), `equalization-
potential-bound` (stagnant, conditional dead-end, not touched),
`potential-averaging-bound` (retired from build slots per standing rule —
excluded even though its own file leaves it nominally `partial` rather than
formally RETHINK; the retirement stands regardless of that internal
labeling).

## Ranking

Updated via `mcp__approach-ranker__update_ranking` (10 pairwise comparisons,
clearing staleness on all 7 existing approaches) and registered
`relaxed-adversary-transfer` via `register_approach`. Resulting order
(best-first):

1. `recursive-embedding-induction` — 1661.5 (owns the sharpest, best-
   isolated remaining lower-bound gap; strongest track record)
2. `geometric-dominance-construction` — 1585.0 (this round's biggest single
   result, Lemma FC closing Proposition K — `verified-milestone`)
3. `universal-adversary-strategy` — 1549.0 (broadest certified toolkit;
   PARTIAL-DOM fully verified, TIE-NECESSARY sound modulo a flagged
   write-up fix)
4. `minimax-mixed-duality` — 1479.0 (one solid new lemma, SANDWICH;
   framing honestly diagnosed as not yet a shortcut)
5. `relaxed-adversary-transfer` — 1500.0 (new, cold-start)
6. `potential-averaging-bound` — 1437.2 (retired from build; real negative
   result on file)
7. `majorization-smoothing` — 1404.3 (confirmed dead-end)
8. `equalization-potential-bound` — 1384.1 (conditional, stagnant)

## Build set for round 7

Dispatch one proof-builder per slug below, each targeting exactly the
scope the outliner assigned:

- `recursive-embedding-induction` — Lemma PARITY-PAIR-ANCHOR (should close)
  + Lemma V'-GEN / peeling induction attempt.
- `universal-adversary-strategy` — certify PARTIAL-DOM-RESIDUAL and
  MULTI-HALVE, fix TIE-NECESSARY's `dim(Q)=0` write-up, retarget to the
  matching/assignment induction theorem.
- `minimax-mixed-duality` — duality-certificate attempt on the general
  discrete search, gated by the cheap numeric check against the two `m=5`
  witnesses.
- `relaxed-adversary-transfer` — cheap numeric gate on the `∞`-mark
  relaxation first (2-3 small configurations); truncation lemma only if the
  gate result supports it; state explicitly if/when it converges with
  `universal-adversary-strategy`'s target.

build set: recursive-embedding-induction, universal-adversary-strategy, minimax-mixed-duality, relaxed-adversary-transfer
