# Round 17 explorer report — Region 3 closure (m=4 Case C residual)

Lens: can Strategy C_{23} alone close the residual Region 3 of the m=4
Case C 5-strategy menu, and does the closed-form algebraic argument
generalize? Scouting only — no proof attempted.

## Setup used (matches `universal-adversary-strategy.md`'s Round 16 build exactly)

`A=(p_1\ge t_1\ge t_2\ge t_3>0)`, `\Sigma=p_1+t_1+t_2+t_3`. Case C:
`p_1<\Sigma/2`. Region 3: `t_1<\tfrac4{15}\Sigma` AND
`t_1<S_{tail}/2` where `S_{tail}=t_1+t_2+t_3` (tail is `V_3`-Case-C for
itself). Target `c(3)\Sigma=\tfrac8{15}\Sigma`. Five strategies as defined
in the round-16 build:
```
StratA   = t_1 + V_3(t_2,t_3,p_1-t_1)
StratB   = p_1/2 + V_3(t_1,t_2,t_3)
StratC12 = t_2 + V_3(p_1,t_3,t_1-t_2)
StratC13 = t_3 + V_3(p_1,t_2,t_1-t_3)
StratC23 = t_3 + V_3(p_1,t_1,t_2-t_3)
```
`V_3` and `L_2` implemented verbatim from `lemmas/ptbi-threshold-reduction.md`
Cases A/B plus the certified round-9 Case C closure. Code re-implemented from
scratch in `fractions.Fraction` (exact) for discrete search and `numpy`/
`scipy.optimize.differential_evolution` (continuous, normalized `\Sigma=1`)
for the adversarial search. Scripts left at `/tmp/round-17/*.py`
(`region3_explore.py`, `region3_opt.py`, `region3_opt2.py`, `family_check.py`,
`c12_check.py`, `final_search.py`, `check_point.py`).

## 1. Headline verdict: Strategy C_{23} alone is NOT universal on Region 3

Random exact-`Fraction` search, 200,000 raw Case-C integer trials filtered to
Region 3 (17,992 landed in Region 3): **StratC23 alone exceeds the target in
4,355 of 17,992 trials (≈24%)**. So the task's working hypothesis — that
`StratC_{23}` by itself, with a general algebraic proof, closes Region 3 — is
**false**. Smallest exact counterexample to "C23 alone suffices":
`A=(937,457,390,142)`, `\Sigma=1926`, target `=5136/5=1027.2`, but
`StratC23=1079>1027.2`.

However: **the full `min` of all 5 strategies (exactly the menu already in
the round-16 outline) has zero violations** on Region 3 in every test run
this round:
- 17,431 random integer trials (exact `Fraction`): 0 violations.
- 26,000 more random integer trials, classified by which strategy uniquely
  wins: **when C23 fails, it is always StratA or StratB that rescues it**
  (2,217 / 2,005 cases respectively out of the 4,355 C23-failures sampled);
  StratC12/StratC13 were never the *unique* winner anywhere in Region 3 in
  these samples.
- A 60-restart `scipy.optimize.differential_evolution` adversarial search
  over the full continuous Region 3 (normalized `\Sigma=1`), directly
  maximizing `min(5 strategies) - target`, found a **maximum of exactly
  `0`**, attained only at the point `(t_1,t_2,t_3)=(4/15,1/5,2/15)\Sigma`,
  which is `A\propto(6,4,3,2)` — i.e. exactly the already-known extremal
  witness sitting on the Region 1/Region 3 boundary (excluded from Region 3
  itself since Region 3's defining inequality `t_1<\tfrac4{15}\Sigma` is
  strict). No interior violation was found anywhere.

**Conclusion: the existing 5-strategy `\min` menu (StratA, StratB, StratC12,
StratC13, StratC23 — nothing new needed) appears to be exactly sufficient for
Region 3 too**, but the proof cannot use StratC23 in isolation; it needs (at
minimum) a further case split inside Region 3 between "StratA/StratB already
finishes it" and "only StratC23 finishes it."

## 2. A new interior witness: exact 5-way tie at `A\propto(8,4,3,2)`

Restricting the adversarial search to the strict interior (`t_1\le
0.95\cdot\tfrac4{15}\Sigma`, well away from the Region 1 boundary) found the
tightest interior point at `(t_1,t_2,t_3)\propto(4,3,2)`, `p_1\propto8`,
i.e. `A=(8,4,3,2)`. Exact check (`Fraction`):
```
Sigma = 17,  t_1/Sigma = 4/17 ≈ 0.2353 < 4/15 (Region 3 ✓, strictly interior)
StratA = StratB = StratC12 = StratC13 = StratC23 = 9   (ALL FIVE TIE EXACTLY)
target = c(3)*17 = 136/15 ≈ 9.0667
margin = 136/15 - 9 = 1/15  (Σ=1 normalization: margin = 1/255)
```
This is a genuinely new, load-bearing witness: **all 5 strategies coincide
exactly** at this point, and the shared value meets the target with margin
`1/15\cdot\Sigma/17=1/255\cdot\Sigma`. It sits on the natural 1-parameter
family `A=(p_1,4,3,2)` (fixed tail, varying `p_1`) together with the known
extremal `A=(6,4,3,2)`. Scanning that whole family (`/tmp/round-17/family_check.py`,
`p_1` from `4.0` to `8.8` in steps of `0.2`, all values landing in Case C):
margin is **strictly positive everywhere except at `p_1=6` where it is
exactly `0`** (the known extremal point, Region 1's boundary) — margin
decreases monotonically to `0` as `p_1\to6^-` from inside what would be
Region 3, then increases again for `p_1>6`. This is strong corroborating
evidence (not proof) that `A=(6,4,3,2)` is the unique global tight point over
*all* of Case C for `m=4`, and Region 3's interior has uniform strict slack.

## 3. Where does StratC12 / StratC13 ever matter?

A separate `differential_evolution` search over the *entire* Case C domain
(not just Region 3) tried to find a point where `StratC12` (resp. `StratC13`)
is strictly less than `min(StratA,StratB,StratC13,StratC23)` (resp. the
`C12`-swapped version). Found one for `C12`: `t_1\approx0.294\Sigma>
\tfrac4{15}\Sigma`, i.e. **in Region 1, not Region 3** — and there `StratA`
already ties it exactly (`StratA=StratC12=0.50000\Sigma<`target), so this
does not show `C12` doing independent work. No point was found (`margin`
found `\approx -10^{-16}`, i.e. numerically zero) where `C13` is the unique
winner. **Working conclusion: inside Region 3 specifically, only StratA,
StratB, and StratC23 ever appear to be load-bearing; StratC12/StratC13 look
dispensable there** (though this is empirical, not proved — a future round
should not assume it without checking whether some other example shows
C12/C13 needed).

## 4. Sketch of what an algebraic proof of Region 3 would need (for the outliner/builder)

Based on the winner distribution above, a natural 2-way sub-split of Region 3
suggests itself (not proved, just structurally suggested by the data):

- **Region 3a** (`t_1` close to `\tfrac4{15}\Sigma`, e.g. the ~2,200 "only A
  wins" sample points all cluster with `t_1/\Sigma\in[0.23,0.2667)`): the
  same style of *loose* bound used for Region 1 (`StratA\le\tfrac47\Sigma-
  \tfrac{t_1}7`, via Lemma V3-BOUND on `(t_2,t_3,p_1-t_1)`) is monotone
  decreasing in `t_1` and — since it is exactly `c(3)\Sigma` at `t_1=
  \tfrac4{15}\Sigma$ — is automatically `\le c(3)\Sigma` for *all*
  `t_1\le\tfrac4{15}\Sigma`, i.e. **Region 1's own proof, as already written,
  literally covers Region 3 too for the `StratA` branch — no new argument
  needed for the cases where StratA wins.** (This is worth double-checking
  algebraically next round: Lemma m=4-REGION-A's proof of `StratA\le
  \tfrac47\Sigma-\tfrac{t_1}7` never used `t_1\ge\tfrac4{15}\Sigma`, only
  used it to conclude the RHS is `\le c(3)\Sigma`; for `t_1<\tfrac4{15}\Sigma`
  the RHS is `>c(3)\Sigma`, so the *loose* StratA bound is not automatically
  enough — matches what we see numerically: StratA meets target on some but
  not all of Region 3.)
- **Region 3b** (the residual where StratA's loose bound fails): need
  either StratB's *exact* value (not the loose Region-2-style bound, which
  the round-16 write-up already showed is algebraically insufficient) or
  StratC23's exact value. The `(8,4,3,2)`-type family above suggests trying
  a **tighter exact algebraic identity for `\min(StratB,StratC23)`** as a
  function of `(p_1,t_1,t_2,t_3)` restricted to Region 3, since numerically
  they are frequently *equal or very close* (e.g. at `(8,4,3,2)/17` all 5
  coincide; at `(10,10,10,9)` StratB=StratC23=39/2 exactly). This exact
  coincidence at multiple witnesses is suspicious and worth investigating:
  it may indicate `StratB=StratC23` identically on part of Region 3's
  Case-C-for-the-base sub-branch, which if provable algebraically would
  collapse the needed case analysis.
- The base triple of `StratC23`, `(p_1,t_1,t_2-t_3)`, needs its own `V_3`
  regime tracked (as the round-16 write-up already flags) — confirmed again
  this round that the base is *not* always in the convenient DOM/Case-B
  regime (e.g. at `(10,10,10,9)` and `(8,4,3,2)` the base lands in Case C
  for itself too).

**No closed-form general inequality was derived this round** — this is
scouting, not proof. The concrete, reusable numeric assets for whoever
attacks this next: the exact witness `A=(8,4,3,2)` (all-5-tie, margin
`1/255\Sigma`), the exact witness `A=(937,457,390,142)` (StratC23-alone
fails by `259/1926\cdot\Sigma\approx0.0135\Sigma`... actually check: target
`5136/5=1027.2`, `StratC23=1079`, so C23 alone *overshoots* by `51.8`, i.e.
`\approx2.7\%` of `\Sigma`), and the fixed-tail family `A=(p_1,4,3,2)`
showing the unique global tight point is exactly `p_1=6` (Region 1's
boundary), not anywhere in Region 3's interior.

## 5. Brief note on general m≥5 (per instructions, kept short)

Not deeply explored this round (Region 3 was the focus), but one structural
observation worth flagging: the m=4 "3-region split" (Region 1: `t_1`
large, closed by a single loose recursive bound; Region 2: tail is
`V_3`-Case-B, closed by `StratB`'s loose bound; Region 3: tail is
`V_3`-Case-C, needs exact/tie strategies) is naturally **inductive in
shape** — Region 1/Region 2's proofs both reduce `m=4` to the *already
certified* `m=3` theorem via a loose `c(m-2)`-style bound, exactly the
pattern that would generalize: for general `m`, split on whether `t_1` is
"dominant enough" (loose bound via the certified `(m-1)`-theorem) vs. not
(needs exact/tie strategies recursing into the `(m-1)`-theorem's own
Case C). This suggests next round could try to set up the **same 3-region
inductive skeleton one level up (`m=5`, tail is the certified `m=4`
theorem)** rather than reinventing case analysis from scratch — but the
"Region 3" analogue at `m=5` would need `\mathrm{StratC}_{ij}`-style
tie-strategies matching against a size-3 (not size-2) tail, and the number
of such subset-tie strategies grows combinatorially with `m` (this is
exactly the open Lemma SLACK-COVER content, proved *necessary* at `m=6` in
round 15). So the "does the m=4 3-region trick generalize" question is
plausible but **not tested this round** — it is a genuine open angle worth
a dedicated explorer/outliner pass next round, distinct from Region 3
closure itself.
