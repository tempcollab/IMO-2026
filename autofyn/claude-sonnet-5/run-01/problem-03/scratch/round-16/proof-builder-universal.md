# proof-builder report — universal-adversary-strategy, round 16

## Task
Complete the m=4 Case C closure of Claim PTBI per the round-16-v2 outline
(approved by outline-reviewer): construct min(StratA, StratB, StratC_12,
StratC_13, StratC_23) and prove it meets target c(3)*Sigma throughout Case C
for m=4, using the certified 3-case V_3 theorem and Lemma DOUBLE-INSERT.

## Result: partial, real progress, gap not fully closed

Wrote to `results/imo-2026-03/approaches/universal-adversary-strategy.md`
("Round 16 build" section, plus two new promotable lemmas at the end of the
file). Status remains `partial`.

**What is now fully, rigorously proved (hand algebra, not just numerics):**

1. **Lemma V3-BOUND**: `V_3(x,y,z) <= c(2)(x+y+z)` unconditionally for any
   sorted triple — a clean re-derivation of the round-9 "m=3 solved in
   full" result as a single inequality, usable as a black box.

2. **Region 1** (`t_1 >= (4/15)Sigma`): Strategy A alone closes this region.
   Exact algebra: StratA <= (4/7)Sigma - t_1/7, decreasing in t_1, equals
   c(3)*Sigma exactly at t_1 = (4/15)Sigma. This boundary is EXACTLY where
   the outline-reviewer's extremal witness A=(6,4,3,2) sits (t_1=4,
   Sigma=15, 4*15/15=4 exactly) — confirming this region's boundary is the
   true tight locus, not an arbitrary cut.

3. **Region 2** (`t_1 < (4/15)Sigma` AND tail is DOM/Case-B for itself,
   i.e. `t_1 >= (Sigma-p_1)/2`): Strategy B alone closes this region, with
   a clean uniform strict margin >= Sigma/60. Includes a non-trivial
   sub-lemma (Step 2a): whenever t_1 < (4/15)Sigma, the tail can NEVER be
   in V_3's Case A (proved via a chain of fraction inequalities,
   4/15 < 2/7 < 4/7 * (S_tail/Sigma) since S_tail > Sigma/2 in Case C).

Both regions independently re-verified this round with a fresh 200,000-trial
exact-Fraction random search restricted to their union: zero violations.

**What remains open (Region 3):** `t_1 < (4/15)Sigma` AND the tail is
genuinely in V_3's Case C for itself. Here Strategy B's loose bound
provably fails (needs p_1+t_1 >= (4/5)Sigma, which Region 3's hypotheses do
not give). Strategy C_ij is needed. I worked one fully explicit interior
example (A proportional to (1,1,1,0.9)) showing:
- the natural shortcut "StratC's base triple {p_1, t_k, r} is always DOM"
  is FALSE in general (found a concrete case where it lands in the base's
  own Case-C branch instead),
- but the target is still met there (1.95x vs target 2.08x, ~6% margin),
  via that harder branch.

This is honest, non-overclaimed partial progress: the previously-fully-open
~15-way case split is now reduced to one precisely-characterized residual
locus (not "the rest of Case C" vaguely), with the reason the natural
shortcut fails identified concretely, but no closed-form proof of Region 3
was completed in the time available.

## Certification candidates
Two new lemmas proposed at the end of the approach file for reviewer
certification: Lemma V3-BOUND, and Lemma m=4-REGION-A/REGION-B (the Region
1 and Region 2 closures). Both are fully proved and independently spot-
checked numerically (200,000 trials, zero violations).

## Files touched
- `results/imo-2026-03/approaches/universal-adversary-strategy.md` (Status
  section entry added; full "Round 16 build" write-up inserted at the top
  of "Current best"; two promotable lemmas + verdict appended at end of
  file).

## Scripts used (not committed, scratch only)
- `/tmp/v3def.py` — exact-Fraction V_3/L_2/5-strategy implementation,
  reproduces all three outline witnesses exactly (1859,931,619,611) ->
  2014<=2144; (6,5,4,2) -> 9<=136/15; (6,4,3,2) -> 8=8 exactly.
- Inline region-restricted 200,000-trial random search (Region 1 union
  Region 2), zero violations.
