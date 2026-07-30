# Build report — induction-peel (round 7)

Status: **partial** (no advance on GAP L2-exch; the assigned mechanism is refuted and pronounced a dead end).

## Spec concerns (top-level)
The round-7 revise plan for this slug — write the missing lower exchange step as the **aimo-0298
split-and-average monovariant** — has a genuine structural flaw and cannot work for our potential
`D = μ{t: N(t) odd}`. I verified this on **budget-enforced, valid** `|F|≥3` refinements of `C_n`
(not unconstrained samples; the explorer's harness warning is respected), Lemma-M evaluation:

1. **Averaging inequality is false for D.** `D(S) ≥ ½(D(S_O)+D(S_E))` fails on **26,772 / 95,770
   (~28%)** valid refinements (n=4), worst deficit ≈ −0.99. aimo-0298 works only because its
   potential `w = Σ 2^{−r(x)}` is an *additive, mass-free, per-element* sum with a termwise bound;
   `D` is a global parity-measure with no termwise structure — deleting the complementary parity
   class reshuffles the sort and flips parities far from the run.
2. **S_O, S_E are not valid IH instances.** They are sub-multisets that neither sum to `2^n−1` nor
   refine `C_{n-1}`, and carry less mass, so `D(S_O)` or `D(S_E) < 1` occurs (233 cases). IH
   LB(n−1) (a *mass* statement) cannot be invoked on them. aimo-0298 inducts on raw `|S|` with a
   dimensionless potential; our `D≥1` has no mass-free reformulation.
3. **Gap is unclosable from `D(B)≥1` alone.** The clean sufficient condition `μ(O_F∩O_B) ≤ D(F)/2`
   fails on **62,304 / 95,770 (~65%)**, worst excess 2.95. Confirms the explorer's opening #1: fix
   must be **upstream** (a structural invariant on where `O_B` sits vs the ladder), not a sharper
   downstream overlap cap.

## What I closed / added
- **§3.4 (new):** rigorous, data-backed refutation of the split-and-average route, recorded as a
  dead end so no future round retries it.
- Re-confirmed (budget-enforced sweeps, n=2–5, 3×10⁵ each) that the **target D(S)≥1 is correct and
  tight** (min D = 1.00003 / 1.00027 / 1.00004 / 1.07, zero violations) — the gap statement is right,
  only the mechanism is wrong.
- Confirmed the **minimal-scale-run adjacency** sub-fact (two gaps each ≥2^d sum to ≥2^{d+1};
  = Lemma ONE one level down) is correct and reusable — it just can't carry an averaging argument
  for a parity-measure.

## What remains (unchanged, precisely localised)
- **GAP L2-exch** (S = F⊔B, |F|≥3, all pieces ≤2^{n-1}, |D(F)−D(B)|<1): open. This slug's
  monovariant-split route is now dead. Route it to `parity-measure-potential` (structural per-gap IH
  on O_B) or `merge-interleave-pattern` (reachable-word extremality).
- **GAP U-VALLEY** (upper balanced): unchanged, other slugs.

Everything else in the file stands rigorous and unchanged: reduction (R/M/P), recursion, base
cases, PEEL/SPLIT/ONE/TB, band decomposition, Case (a), trivial regime of (L⋆), the |F|=2 sub-case,
both exact telescoping identities, and the entire upper dominant case §4A (contains the tight dyadic
input, so c(n)=2^n/(2^{n+1}−1) is confirmed exact on the extremal configuration).

## Lemmas proposed
None new this round. (The refutation is negative; the reusable sub-facts PEEL/SPLIT/ONE/TB/HALF are
already certified.)

## Recommendation for the orchestrator
This slug's assigned mechanism is exhausted for L2-exch. Either (a) keep it live only as the carrier
of the already-proven upper §4A + closed lower sub-cases while the exchange is delegated to the two
other lower routes, or (b) re-plan it (RETHINK) onto a genuinely different lower mechanism next
round. Do not re-dispatch split-and-average.
