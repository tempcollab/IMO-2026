# outline-reviewer — IMO 2026 P3 (imo-2026-03), round 3

Reviewed the outliner's field (tail-count ADVANCE, tower-induction ADVANCE,
gaps-leftover NEW, majorization-upper REVISE) against the problem, the 13
certified lemmas, the round-2 ranking, the three round-3 explorer reports,
and the rigor/single-gap-trap rules. Verified key claims by hand + `python3`
(`Fraction`-exact) before approving.

## Field review

### tail-count — APPROVE
Whole-claim lower-bound spine (cites `majorization-upper` for the upper bound).
Sound: imports 8 certified lemmas; case (a)/(b-i)/(b-ii-dyadic) all closed and
cited. NEW this round is well-formed:
- **2-split sub-case** (`D ≥ D(T_{n-2}) ≥ 1`): I verified the n=3 grid exactly
  (`Fraction`, step 1/8, both same-piece-split and two-different-pieces cases):
  min D = 1 = D(T_1), attained at the dyadic cascade `{4,4,2,2,2,1}` (split
  8→4+4, 4→2+2). The mechanism (D as explicit PL in the two cut points; the
  min plateau touches the dyadic cascade where `dyadic-refinement-lower-bound`
  applies) is plausible and certifiable. Highest-confidence concrete progress.
- **Even-group pair-cancellation** (S1/S2 + spine geometric dominance): the
  mechanism is rigorous — adjacent-equal pairs cancel in the alternating sum
  (sign-agnostic, verified by hand); even-count non-dyadic groups fully cancel;
  the spine is distinct powers of 2; the largest exceeds the sum of all smaller
  (`2^{k_1} > 2^{k_2+1}−1`); the spine is nonempty (total mass D_n is ODD,
  pairs contribute EVEN mass ⇒ an unpaired 1 survives). This is a clean
  certifiable sub-result that closes G1 for even-group strong breakpoints
  INDEPENDENTLY of the global exchange.
- **Plateau-connectivity (GLOBAL exchange)**: correctly flagged as the HARD
  STEP / GAP. The V-shape obstruction is honestly noted (local rebalancing
  fails; the exchange must be multi-coordinate). Verified the V-shape: T_3,
  8→5+3 then 5→(5−q)+q: q=1⇒D=1, q=2⇒D=3, q=2.5⇒D=2 (rebalancing to balanced
  INCREASES D from 1 to 2 — qualitative point holds). NOTE: the explorer
  reported q=2.5 ⇒ D=3; the exact value is D=2 (minor arithmetic slip, does not
  affect the obstruction).
Cases covered (single-split closed, 2-split closeable, k≥3 G1 open, even-group
vs odd-group, PL-vertex vs strong bp). Avoids the round-2 dead ends (V-shape
rule). APPROVE — the 2-split lemma and even-group sub-result are certifiable
regardless of whether the global exchange closes.

### tower-induction — APPROVE
Whole-claim lower-bound spine (block/parity machinery). Sound: imports the
certified F-block/F-rec/F-min lemmas; the even-group sub-result is re-derived
from the block viewpoint (acknowledged overlap with tail-count step 6 — fine,
it is the genuinely different derivation route). The NEW non-dyadic spine
generalization (Route D) honestly flags that the block formula applies ONLY to
dyadic refinements and that the sign of a non-dyadic leftover depends on
global parity (witness `{4.75,4,0.25}` D=1 vs `{4,7/3,2}` D=11/3) — no uniform
"leftover contributes +" rule. The odd-count spine bound is flagged as the
open GAP with the splitting-tree bookkeeping as the candidate mechanism.
Genuinely different machinery (block/parity vs PL/variational) on the same G1
wall — keep diverse, do NOT retire. APPROVE — the even-group sub-result is
certifiable; the odd-count spine bound is an honest GAP.

### gaps-leftover — APPROVE (with a fixable scope gap — see note)
NEW slug, the genuinely-different lower-bound framing the orchestrator asked
for. Verified the core identity `D = Σ(p_{2k-1}−p_{2k}) + p_{2n+1}` by hand
(trivial telescoping of the alternating sum of a sorted-desc sequence of
length 2n+1; confirmed `Fraction`-exact on a sample). The proof object
(charging/matching against the tower's self-similar dyadic sizes) is
third-party to the PL-integral (`tail-count`) and block-formula
(`tower-induction`) machinery — confirmed far enough to count as a new framing,
not a duplicate. The "1 is a conserved quantity" is correctly flagged as
CONJECTURE (numerics), not proof. APPROVE as a population member.

**Scope gap the builder MUST close while building:** the identity holds ONLY
when `m = 2n+1` (Xiang uses EXACTLY n marks ⇒ odd piece count). The lower
bound must hold for EVERY ≤n-mark refinement, including fewer marks (where m
is even or smaller — then the alternating sum has NO leftover, ending at
`−p_m`). The lower-bound minimizer is NOT always at exactly n marks (the V-
shape shows splitting can INCREASE D; for n=2 the min D=1 is attained at both
1-mark and 2-mark configs). The builder must either (a) cite the certified
single-split/dyadic lemmas for the small-mark-count cases and restrict the
charging argument to the full-n-mark odd-m case, arguing the intermediate even-
m cases reduce to one of these, or (b) derive the even-m form of the identity
(`D = Σ(p_{2k-1}−p_{2k})` with no leftover) and charge it separately. This is a
missing-case gap (fixable), not a wrong-technique flaw — the framing stands.

### majorization-upper — APPROVE
Whole-claim upper-bound spine. REVISED correctly: the majorization/Schur-
convexity route is DROPPED (the explorer gave decisive counterexamples —
single piece `(1)` is most-majorizing yet `D*=0`; `D*` is not Schur-convex; I
confirm this kills Karamata here). The new spine is the **Max-bound conjecture
`D*(L) ≤ M/2^n`** (M = largest Liu piece, piece-count-free). Confirmed:
- **Exactly ONE upper-bound slug** — no single-gap-trap violation (round-2
  rule). The Max-bound unifies G1 and G2 (the non-dominant below-threshold
  wall); the three lower-bound slugs cite this slug for the upper bound.
- The Max-bound is a CONJECTURE (0 violations over 2860+ configs, tight
  uniquely at the tower where `M = 2^n/D_n ⇒ M/2^n = 1/D_n`), correctly marked
  as GAP, not presented as proven. A conjecture-backed route is a valid
  population member; the non-dominant sub-step is an explicit GAP, not a hidden
  leap.
- The DOMINANT case (`a_1 ≥ 2a_2`) is a clean one-line halving induction
  (verified the logic: halve a_1, new max = M/2, halves cancel at positions
  1,2, apply W(n−1) piece-count-free). The NON-DOMINANT case (`a_1 < 2a_2`,
  especially `a_3 > a_1/2`) is the crux — the simple induction genuinely
  breaks there (verified: pairing leaves rest'-max = a_3 which can exceed
  a_1/2, witness `(0.4,0.35,0.25)`). The two-variable IH `D* ≤ f(M, M_2, n)`
  is the candidate mechanism, flagged as GAP. The self-similar recurrence
  narrative (F1) is folded in as an inductive organizer, reducing single-gap
  risk. APPROVE — the dominant case + n=2-certified scaffolding is certifiable
  independently; the non-dominant two-variable IH is the honest open GAP.

### d-potential — HOLD (not in build set)
Held, no builder. Potential Φ=D shown circular; no concrete Φ. Certified
outputs already harvested. Keep live for ranker diversity.

### self-similar — HOLD
Subsumed by `tower-induction`'s frontier recursion. Held.

### balanced-configs — RETIRED
B3 circular; B1 harvested into `majorization-upper`. Stays retired.

## Ranking

Cleared the stale flags on the three round-2-built slugs and anchored the new
`gaps-leftover` (cold-start 1500) to real opponents. Head-to-head comparisons
fed to `update_ranking` (anchored to last outcomes: all three round-2 slugs =
`verified-milestone`/partial; `gaps-leftover` = no outcome yet):

- tail-count > tower-induction (leader certified the most lower-bound sub-cases:
  single-split + dyadic + PL-breakpoint; both share G1 but tail-count carries
  more certified progress + the certifiable 2-split/even-group sub-results)
- tail-count = majorization-upper (draw — different bounds; tail-count has more
  certified sub-cases for all n, majorization-upper has the single strongest
  milestone = n=2 upper bound COMPLETE; complementary, neither dominates)
- tail-count > d-potential, > self-similar, > balanced-configs, > gaps-leftover
  (proven leader vs held/retired/unproven-new)
- majorization-upper = tower-induction (draw — majorization has n=2-complete +
  the high-upside Max-bound lead; tower-induction has the general-n F-min close;
  strong on different axes)
- majorization-upper > d-potential, > self-similar, > balanced-configs,
  > gaps-leftover (n=2 proven + Max-bound lead vs stuck/subsumed/retired/unproven)
- tower-induction > d-potential, > self-similar, > balanced-configs,
  > gaps-leftover (round-2 certified progress vs held/subsumed/retired/unproven)
- gaps-leftover > d-potential (fresh framing with verified identity + open gap
  vs a stuck/circular potential with no concrete Φ), > self-similar, >
  balanced-configs
- d-potential > self-similar (certified round-1 outputs vs subsumed/no outcome),
  > balanced-configs
- self-similar > balanced-configs

Resulting Elo order (live first):
1. tail-count — 1643.5
2. majorization-upper — 1580.5
3. tower-induction — 1567.3
4. gaps-leftover — 1504.2 (new, anchored fairly — not sunk for being new, not
   inflated above proven progress)
5. d-potential — 1484.3 (held, declining — stuck/circular)
6. self-similar — 1396.1 (held, subsumed)
7. balanced-configs — 1324.3 (retired)

**Field-diversity note for the orchestrator:** the three lower-bound slugs
(tail-count, tower-induction, gaps-leftover) all hit the SAME G1 wall (non-dyadic
multi-split, `D ≥ 1` at every non-dyadic breakpoint). This is acceptable THIS
round because the framings are genuinely different (PL/variational vs
block/parity vs charging/matching) and each has a certifiable independent sub-
result — but if all three return next round STILL on G1 with no sub-case
closed, that is the shared-gap-plateau signal: tell the next outliner to put
≥1 approach on a framing far from the lower-bound-D≥1 reduction entirely (e.g.,
a direct saddle / LP-dual / algebraic-invariant route), not a fourth lens on
the same wall.

## Build set

All four nominated slugs approved (gaps-leftover with the scope-gap note
above; the builder closes it while building). d-potential and self-similar
HELD, balanced-configs RETIRED.

build set: tail-count, tower-induction, gaps-leftover, majorization-upper
