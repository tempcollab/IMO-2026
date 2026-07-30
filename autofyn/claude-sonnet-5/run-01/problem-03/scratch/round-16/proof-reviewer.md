# Round 16 proof review — imo-2026-03

## Scope
Sole built slug this round: `universal-adversary-strategy` (round-16 build,
"m=4 Case C, 5-strategy closure — two regions proved, one residual open").
`recursive-embedding-induction` was advanced unchanged by the outline-
reviewer (no build, no diff — confirmed via `git diff --stat`, only
`universal-adversary-strategy.md` and `.ranking.json` touched this round).
No review of `recursive-embedding-induction` is needed (nothing new to
review; its status is unchanged from round 15/prior).

## What was claimed
A two-region partition of the `m=4` Case C region (`p_1<\Sigma/2`) for
Claim PTBI's 5-strategy menu `V_4(A)=\min(\mathrm{StratA},\mathrm{StratB},
\mathrm{StratC}_{12},\mathrm{StratC}_{13},\mathrm{StratC}_{23})`:

- **Region 1** (`t_1\ge\tfrac4{15}\Sigma`): Strategy A alone closes it,
  `StratA\le\tfrac47\Sigma-\tfrac{t_1}7`, decreasing, exactly hitting target
  at `t_1=\tfrac4{15}\Sigma` (the known extremal witness `A=(6,4,3,2)`).
- **Region 2** (`t_1<\tfrac4{15}\Sigma` AND tail is `V_3`-Case-B/DOM for
  itself): Strategy B alone closes it with margin `\ge\Sigma/60`.
- **Region 3** (residual, `t_1<\tfrac4{15}\Sigma` AND tail is genuinely
  `V_3`-Case-C for itself): OPEN, honestly reported as such. One explicit
  interior example (`A\propto(1,1,1,0.9)`) shows the target is still met
  there via `StratC_{23}`'s harder (non-DOM) branch, but no general proof.

## Independent verification performed

I wrote a fresh, from-scratch Python script (`/tmp/verify.py`, exact
`fractions.Fraction` arithmetic throughout — not the builder's script) that
independently re-implements:
- `c(k) = 2^k/(2^{k+1}-1)`,
- `L_2(u,v)` (the certified `n=1` theorem),
- `V_3(x,y,z)` (all three branches, cross-checked line-by-line against
  `lemmas/ptbi-threshold-reduction.md` Cases A/B and the round-9 "`m=3`
  solved in full" Case C closure `min(x+z/2, y+L_2(x-y,z))` — I traced the
  Case-C formula back to its origin in the approach file's own round-9
  section (TAIL-SNIP `=x+z/2`, BLOCK-RECURSE_1 `=y+L_2(x-y,z)`, both
  matching exactly),
- `StratA`, `StratB`, `StratC_{12}`, `StratC_{13}`, `StratC_{23}` exactly as
  stated in the round-16 build.

**Results (all independently reproduced, none merely re-run from the
builder's script):**

1. **Lemma V3-BOUND**: `V_3(x,y,z)\le c(2)(x+y+z)` — 200,000 random-integer
   trials, **zero violations**.
2. **Extremal witness `A=(6,4,3,2)`**: `\Sigma=15`, `c(3)\Sigma=8`,
   `StratA(6,4,3,2)=8` — exact equality, confirmed.
3. **Region 1/Region 2/Region 3 exhaustive, disjoint partition** of `m=4`
   Case C, confirmed by direct classification over 300,000 random
   sorted-descending trials restricted to `p_1<\Sigma/2`: 199,320 fell in
   Region 1 (defined `t_1\ge\tfrac4{15}\Sigma`), 1,069 in Region 2 (elif
   `t_1\ge S_{\mathrm{tail}}/2`), 49,737 in Region 3 (else) — every trial
   classified into exactly one region, confirming no gap and no
   double-counting in the case split as stated.
4. **Region 1 closure**: zero violations of `StratA\le c(3)\Sigma` across
   all 199,320 Region-1 trials. Independently re-derived the affine bound
   `StratA\le\tfrac47\Sigma-\tfrac{t_1}7` by hand (using `t_2+t_3+r=
   \Sigma-2t_1` where `r=p_1-t_1`) and confirmed it equals `c(3)\Sigma`
   exactly at `t_1=\tfrac4{15}\Sigma` (`\tfrac{56}{105}=\tfrac8{15}`,
   `\gcd(56,105)=7`).
5. **Region 2 closure**: zero violations across all 1,069 Region-2 trials
   (a narrow region, hence the small natural sample size — still fully
   conclusive since the claim is a closed-form algebraic inequality, not a
   numeric fit). Independently re-derived Step 2a (`t_1<\tfrac4{15}\Sigma
   \implies` tail can never be `V_3`-Case-A) via the chain `\tfrac47
   S_{\mathrm{tail}}>\tfrac27\Sigma>\tfrac4{15}\Sigma` — confirmed the
   fraction comparison `\tfrac27=\tfrac{30}{105}>\tfrac{28}{105}=
   \tfrac4{15}` by hand. Independently re-derived `StratB=p_1/2+t_1<
   \tfrac\Sigma4+\tfrac4{15}\Sigma=\tfrac{31}{60}\Sigma<\tfrac{32}{60}
   \Sigma=c(3)\Sigma`, margin `\ge\Sigma/60`.
6. **Named witness `A=(6,5,4,2)/17`**: reproduced `StratA(6,5,4,2)=9`,
   target `c(3)\cdot17=\tfrac{136}{15}\approx9.067`, `9\le\tfrac{136}{15}`
   — matches the builder's exact reported values. Confirmed this witness
   sits in Region 1 (`t_1=5\ge\tfrac4{15}\cdot17=\tfrac{68}{15}\approx
   4.53`).
7. **Named witness `A=(1859,931,619,611)`**: reproduced `\Sigma=4020`,
   target `2144`, and the full 5-strategy `\min = 2014` (via `StratC_{23}`
   specifically — `StratA=2161`, `StratB=StratC_{12}=StratC_{13}=4319/2`,
   `StratC_{23}=2014`), `2014\le2144` confirmed exactly. Confirmed this
   witness sits in **Region 3** (`t_1=931<1072=\tfrac4{15}\cdot4020` and
   `931<1080.5=S_{\mathrm{tail}}/2`), i.e. it is genuinely in the *open*
   region, closed only by the min over all 5 strategies (not by the
   certified Region-1/2 lemmas alone) — consistent with, not contradicting,
   the round-16 build's own honest scoping.
8. **Interior Region-3 example `A=(10,10,10,9)`** (scaling `A\propto
   (1,1,1,0.9)`): reproduced `\Sigma=39`, target `\tfrac{104}5=20.8`,
   `StratC_{23}=\tfrac{39}2=19.5`, `19.5\le20.8` confirmed exactly. Confirmed
   region membership (`t_1=10<\tfrac4{15}\cdot39=\tfrac{52}5=10.4`;
   `S_{\mathrm{tail}}/2=\tfrac{29}2=14.5>t_1=10`, so genuinely Region 3).
9. **Full 5-strategy `\min` over all 49,737 sampled Region-3 trials**: zero
   violations of `\min(5\text{ strategies})\le c(3)\Sigma` — consistent
   with, but (as the builder correctly states) not a proof of, Region 3
   being closeable in general.

No error found anywhere in the algebra, the case-boundary bookkeeping, the
mark-cost accounting (`1+(\le2)\le3=m-1` for each strategy — traced against
the certified `V_3` budget of `\le2` marks), or the reported witness values.

## Overclaim check

The Status is correctly stated as `partial` throughout (approach file and
builder report both). No `solved` claim is made for `m=4` Case C, for
general `m\ge4`, or for the whole problem. Region 3 is explicitly and
precisely characterized as open — not papered over as "the rest of Case C"
vaguely, and not silently absorbed into an implicit "verified numerically
so it's fine" claim: the builder explicitly states no closed-form proof of
Region 3 was completed. General `m\ge5` is not addressed this round and the
write-up does not claim otherwise. This matches CLAUDE.md's rigor rule
("distinguish 'we have proved X' from 'we conjecture X'") correctly.

## Lemma certification

- **Lemma V3-BOUND** (`lemmas/v3-bound.md`, newly written by me with the
  full proof and the round-16 independent verification recorded) —
  CERTIFIED. Sorry-free (prose, not Lean, but no unproved step), statement
  correct and no stronger than proved (it is explicitly a *loose* corollary
  of the exact `V_3` theorem), reusable as a clean black box.
- **Lemma m=4-REGION-A/REGION-B** (`lemmas/m4-region-a-region-b.md`, newly
  written by me) — CERTIFIED, with an explicit scope caveat at the top of
  the file (covers only Region 1 `\cup` Region 2 of `m=4` Case C, NOT
  Region 3) so no future round mistakes it for a full `m=4` Case C closure.

## Verdict

**CHANGES REQUESTED** for `universal-adversary-strategy`. Real, fully
rigorous, independently re-verified progress (two new certified lemmas,
genuine narrowing of the `m=4` Case C case split from "entirely open,
`\le15`-way" to "one precisely-characterized residual region, Region 3").
The whole problem remains `partial` — this does NOT approve the slug, since
Region 3 is unclosed and general `m\ge5` is untouched, both required for
`solved` on this problem's actual claim (Claim PTBI's Case C for all
`m\ge4`, which is itself only a piece of the still-larger upper-bound gap
for the whole `imo-2026-03` problem). No downgrade warranted either — this
is genuine positive progress, not a plateau or a dead end.

`results/imo-2026-03/current.md` updated: new round-16 review section
prepended (before the round-15 section), new bullet added to
"## Approaches tried" summarizing the round-16 build. `## Status` remains
`partial` (unchanged — correct, since the whole-problem claim is untouched
by a partial `m=4` Case C closure).

`record_outcome` called: `universal-adversary-strategy`, round 16,
outcome=`advanced`, note recorded.

## New rule learned this round
See `/tmp/memory/proof-reviewer.md` update: when a builder's construction
recurses into an already-certified sub-theorem (here, `V_3`, the `m=3`
theorem) via a "loose corollary" bound, always trace the sub-theorem's
own case formulas back to their original certified source (here,
`lemmas/ptbi-threshold-reduction.md` plus the round-9 "m=3 solved in full"
narrative in the approach file itself) and cross-check line-by-line, rather
than trusting the round's own restatement of the formula — this is cheap
and catches transcription errors in imported black-box formulas, which a
pure "test the final inequality" check might not surface if the error
happens to cancel out on the specific witnesses tested.
