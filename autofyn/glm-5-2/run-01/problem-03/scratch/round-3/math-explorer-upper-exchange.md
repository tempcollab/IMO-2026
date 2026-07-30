# math-explorer (upper-exchange lens) — IMO 2026 P3, round 3

**Route:** upper-bound G1 wall — general-n (n≥3) "tower is the unique worst
Liu config" / exchange monotonicity. Goal: scout the terrain for proving it
(do NOT write the proof). All numbers from breakpoint-justified (Lemma B1)
exact-`Fraction`-verified optimizers in `/tmp/round-3/`.

---

## Terrain

### (1) The n=2 mechanism extracted — what makes a non-tower config EASIER

Reading `n2-upper-bound-complete.md` Part III + `majorization-upper.md` Part
III carefully, the load-bearing step is **NOT** a Robin-Hood/majorization
move. It is the **averaging bound** on the 2-piece rest:

  `min(b_1 − b_2, 2b_2 − b_1) ≤ (b_1 − b_2 + 2b_2 − b_1)/2 = b_2/2`.

After Xiang's adaptive first move (halve `a_1` in the dominant regime A/C,
pair `a_1 → {a_2, a_1−a_2}` in the non-dominant regime B1/B2), the game
reduces to an n=1 game on a **2-piece rest** `{b_1, b_2}`. The n=1 optimum is
`D(rest) = b_2` (halve, dominant) or `min(b_1−b_2, 2b_2−b_1)` (pair,
non-dominant); the averaging bound gives `D(rest) ≤ b_2/2` in the pairable
case. The bound then closes because **non-tower arithmetic forces `b_2 < 2/7`**:

- Regime C2: `a_1 < 4/7` and `a_1 ≥ 2a_2` ⇒ `a_3 ≤ a_2 ≤ a_1/2 < 2/7`, so
  `D = a_3/2 < 1/7` (strict). C1 is **vacuous** (`a_1+a_2+a_3 ≤ 7a_1/4 < 1`).
- Regime B2: `a_2 < 2/7` ⇒ `b_2 = min(a_1−a_2, a_3) ≤ a_2 < 2/7`, so
  `D ≤ b_2/2 < 1/7` (strict).
- Regimes A, B1 close by the n=1 IH `D(rest) ≤ R/3 ≤ 1/7`, equality iff the
  rest is `R·T_1`, i.e. iff the config is `T_2`.

**The precise exchange/transfer step:** there is no mass-transfer (Robin-
Hood) move. The mechanism is: **Xiang's first move cancels positions 1,2**
(either two equal halves, or two copies of `a_2`), reducing to a 2-piece
sub-game whose optimum is bounded by the **averaging bound** `≤ b_2/2`. The
tower is the unique worst because it is the unique config where `b_2` lands
*exactly* at the threshold `2/7` (the n=1 worst `T_1`), forcing equality;
every non-tower config has `b_2 < 2/7` strictly, giving strict inequality.

**What generalizes (and what does NOT):** the *cancel-then-recurse* pattern
generalizes (regimes A/B1 are certified for all n via the factorization U2/U3,
conditional on `W(n−1)`). The **averaging bound does NOT generalize** — for
n≥3 the rest after one mark has ≥3 pieces, and `min(…)/2` has no 3-piece
analog. The n=2 base is genuinely a base, not a template: the n≥3 wall is a
different shape.

### (2) Majorization / Schur-convexity — KILLED (decisive counterexamples)

I tested whether `D*(L) = min_Xiang D(L)` is monotone in the Lorenz
majorization order (A more-spread ⇒ `D*(A) ≥ D*(B)`, tower = maximal
element). **It is NOT.** Clean counterexamples at n=3 (`/tmp/round-3/majorization_monotone.py`):

| config A (more spread) | config B | A `>_maj` B? | D*(A) | D*(B) | violation |
|---|---|---|---|---|---|
| single `[1]` | tower `T_3` | yes (most majorizing) | **0** | 0.0667 | **0 < 0.0667** |
| `(0.6,.25,.1,.05)` | tower `T_3` | yes | **0.05** | 0.0667 | **0.05 < 0.0667** |
| `(9,3,2,1)/15` | tower `T_3` | yes | **0** | 0.0667 | **0 < 0.0667** |

The single piece `(1,0,0,0)` is the **most majorizing** config of all (it
majorizes everything), yet `D* = 0` (Xiang splits into equal pieces,
`D=0`). The tower `T_n` is **interior** to the majorization order, not an
extremum: configs more spread than the tower (larger top piece) are EASIER
for Xiang, and configs less spread (more uniform) are also easier. `D*`
peaks at the tower, an interior point — so `D*` is **not Schur-convex or
Schur-concave**. This confirms the round-2 scout's suspicion and kills Route
(a) (Karamata/majorization) decisively. The `knowledge_base.md` "Schur"
entry is the generic inequality, not a majorization-monotonicity theorem,
and no convex function is being summed, so Karamata does not apply.

**Implication:** the "tower is the worst" statement (G1) is TRUE (verified
n=1..4) but it is **not** a consequence of majorization monotonicity. The
right characterization of "worst" is the dyadic self-similar structure
(`2^k:2^{k-1}` ratios forcing the pairing cascade to propagate fully),
NOT "most spread." Do not pursue majorization.

### (3) The M/2^n conjecture — the clean unified target (STRONG, verified)

I discovered and stress-tested a **piece-count-free strengthening** that
implies G1 for the below-threshold regime and unifies G1/G2:

> **Conjecture (Max-bound).** `D*(L) ≤ M / 2^n`, where `M = a_1` is the
> largest piece of the Liu config. (Any piece count, total 1.)

**Evidence** (`/tmp/round-3/m_over_2n_fast.py`, breakpoint+grid cross-checked
identical on samples): **0 violations** over 2860 configs (n=2: 500, n=3:
300+10 adversarial, n=4: 60) + 2000 heavy non-dominant n=2 + 10 adversarial
non-dominant n=3. **Tight uniquely at the tower**: `T_n` has
`M = 2^n/D_n`, so `M/2^n = 1/D_n = D*(T_n)` (ratio exactly 1.000 at
n=2,3,4). Worst non-tower ratio: 0.987 at a near-tower config `[0.5722,
0.2866, 0.1412]` ≈ `T_2` — i.e. the bound is approached only by the tower
itself.

**Why it is the prize:** if `D* ≤ M/2^n` holds for all configs, then for
every below-threshold config (`M < 2^n/D_n`), `D* < 1/D_n` strictly —
closing G2 (regimes C/B2 for n≥3) in one stroke. Combined with the
**certified** dominant factorization (regimes A/B1, which handle
`M ≥ 2^n/D_n`), this closes the full upper bound `D* ≤ 1/D_n` for all n.
So the Max-bound + the certified factorization = G1 solved.

**The simple induction (works for DOMINANT, breaks for non-dominant):**
- Base n=0: `D ≤ a_1 = M` (alternating sum of a sorted-desc sequence is
  `≤` its first term — because `-a_{2k} + a_{2k+1} ≤ 0`). ✓
- Step `W(n−1) ⇒ W(n)`: given max `M = a_1`.
  - **Dominant (`a_1 ≥ 2a_2`):** halve `a_1 → {a_1/2, a_1/2}`. New max
    `= a_1/2 = M/2` (since `a_1/2 ≥ a_2`). The two halves cancel (positions
    1,2). By `W(n−1)` on the new multiset (piece-count-free!): `D ≤
    (M/2)/2^{n-1} = M/2^n`. ✓ **One-line.**
  - **Non-dominant (`a_1 < 2a_2`):** halving `a_1` puts the halves at
    positions 3,4 (after `a_2`); they still cancel, giving `D = D({a_2, a_3,
    …})` with new max `a_2`. By IH: `D ≤ a_2/2^{n-1}`. But we need `≤
    a_1/2^n`, i.e. `a_2 ≤ a_1/2` — **contradicts non-dominant** (`a_2 >
    a_1/2`). Pairing `a_1 → {a_2, a_1−a_2}` leaves rest'-max `= a_3` (when
    `a_3 > a_1−a_2`), and `a_3` can exceed `a_1/2` (witness `(0.4, 0.35,
    0.25)`, `a_3=0.25 > 0.20=a_1/2`). **The simple induction breaks.**

So the Max-bound's hard step is exactly the **non-dominant case with
`a_3 > a_1/2`** — the optimal move there is **adaptive** (trace shows: pair
`a_1↔a_2` leaving fragment `a_1−a_2`, then halve `a_3`; OR halve `a_1` to
land mid-list when `a_1/2` sits between `a_2` and `a_3`); no single rule
(`/tmp/round-3/trace_nondom.py`). The conjecture still holds there (verified)
but the proof needs more than "halve the max."

---

## Routes (each: idea, hard step, likelihood)

### Route (a) — Karamata / Schur-convexity on the Liu config
**DEAD.** `D*` is not Schur-convex (counterexamples above). The tower is
interior to majorization. Do not pursue. Likelihood of closing G1: **0**.

### Route (b) — Config-adaptive PAIRING strategy (characterize the residual)
**Idea.** Xiang's marks create canceling pairs (each pair fills adjacent
odd+even slots). After n marks, one "residual" piece remains unpaired; prove
residual `≤ 1/D_n` for every config, with equality iff tower. Use the
`D = ∫(N(t) mod 2) dt` language: the residual is the measure of the
unpaired-interval set.
**Hard step.** The pairing is **adaptive** (depends on the full ratio
vector); the residual is a complicated function of the config. No fixed
pairing achieves the bound (round-2: parallel-halving fails on 59/500 n=2
non-towers). Characterizing the residual cleanly enough to prove `≤ 1/D_n`
universally is the open problem — and it is essentially G1 itself.
**Likelihood: medium-low as a standalone route** — it re-states G1 in
residual language without reducing it. The Max-bound (Route c) subsumes it:
proving `residual ≤ M/2^n` is the concrete target.

### Route (c) — The Max-bound `D* ≤ M/2^n` (strengthened, piece-count-free IH)
**Idea.** Prove `D* ≤ M/2^n` by induction on n. Dominant case is a one-line
halving induction (above). The bound implies G1 for below-threshold configs
(`M < 2^n/D_n`); the certified factorization handles `M ≥ 2^n/D_n`. This
UNIFIES G1 and G2 — they are the same wall (non-dominant below-threshold),
and the Max-bound is the single statement that kills both.
**Hard step.** The non-dominant sub-case `a_3 > a_1/2` (where pairing
leaves rest'-max `= a_3 > M/2`, breaking the one-step halving induction).
The optimal move is adaptive; the induction needs either (i) a **two-variable
IH** `D* ≤ f(M, M_2, n)` tracking both the max `M = a_1` and the second-max
`M_2 = a_2` — pairing removes both `a_1, a_2`, so the bound in terms of
`(M, M_2)` can tighten; or (ii) a clever invariant showing the residual
`a_1 − a_2` (the pairing fragment) plus `a_3`'s contribution is `≤ M/2^n`.
**Likelihood: HIGH (the best bet this round).** The conjecture is strongly
verified, the dominant case is trivial, and the non-dominant sub-case is a
concrete, bounded problem (not an infinite type-enumeration). The two-
variable IH is the natural next strengthening.

### G2's two-variable IH — converges with Route (c)
The round-2 G2 lead ("strengthen to `D ≤ f(R, M, n)` tracking rest-total R
and max piece M") and the Max-bound Route (c) are **the same target**: both
need to handle the non-dominant below-threshold case by tracking more than
just the rest total `R` (the loose `R/D_{n-1}` overshoots there). The
Max-bound `D* ≤ M/2^n` is the *cleanest* two-variable form (depends only on
max, not rest-total — even stronger). The outliner should NOT open separate
G1/G2 slugs (single-gap trap — they share the non-dominant wall); open ONE
slug on the Max-bound.

---

## Numerics

### D* vs majorization (n=3) — monotonicity VIOLATED (kills Route a)
Tower `T_3 = (8,4,2,1)/15`, `D* = 1/15 ≈ 0.0667`.
- single `[1]`: majorizes `T_3`, `D* = 0` (VIOLATION).
- `(0.6, 0.25, 0.1, 0.05)`: majorizes `T_3` (partial sums 0.6>0.533,
  0.85>0.8, 0.95>0.933), `D* = 0.05 < 0.0667` (VIOLATION).
- `(9,3,2,1)/15`: majorizes `T_3`, `D* = 0` (VIOLATION).
7 violations total among 12 sampled configs. `D*` is not Schur-convex.

### Max-bound `D* ≤ M/2^n` — 0 violations, tight at tower
| n | configs tested | violations | worst `D*/(M/2^n)` (non-tower) | tower ratio |
|---|---|---|---|---|
| 2 | 500 random + 2000 non-dominant + 10 adversarial | 0 | 0.987 (near-tower) | 1.000 |
| 3 | 300 random + 10 adversarial | 0 | 0.662 | 1.000 |
| 4 | 60 random | 0 | 0.232 | 1.000 |

### Pairing-achievement (n=2, all `/7` non-tower configs): `D* = 0`
`(5,1,1)/7, (3,3,1)/7, (3,2,2)/7, (5,2)/7, (4,3)/7, (6,1)/7` — all `D*=0`
(Xiang drives `D` to zero). Tower alone holds `D=1/7`. (Confirms round-2.)

### Optimal-move trace (adversarial non-dominant, n=2) — adaptive, no fixed rule
- `(0.4, 0.35, 0.25)`, `a_3=0.25 > a_1/2=0.20`: **pair** `a_1→{0.35, 0.05}`
  (tie to `a_2`), then **halve** `a_3=0.25→{0.125,0.125}`. Final
  `{0.35,0.35,0.125,0.125,0.05}`, `D=0.05 = a_1−a_2` (the residual fragment).
  `M/2^n = 0.10`; `D*/(M/2^n) = 0.5`.
- `(0.42, 0.30, 0.28)`, `a_3=0.28 > a_1/2=0.21`: **halve** `a_1→{0.21,0.21}`,
  halves land at positions 3,4 (cancel), `D = a_2−a_3 = 0.02`. One mark
  suffices. `M/2^n=0.105`; ratio 0.19.
- `(0.45, 0.28, 0.27)`: halve `a_1`, `D = a_2−a_3 = 0.01`. Ratio 0.089.

**The non-dominant optimal move is NOT uniform** (pair-then-halve in one
case, halve-to-middle in another). This is why the simple induction breaks
and the two-variable IH is needed.

---

## Recommendation

**Open ONE slug** (or advance `majorization-upper` with this as its new
spine) on the **Max-bound `D* ≤ M/2^n`** (piece-count-free strengthened IH),
NOT separate G1/G2 slugs. Rationale:
- It is the cleanest unified target — G1 and G2 share the same wall
  (non-dominant below-threshold configs), and the Max-bound kills both at
  once. Two slugs would hit the same wall and die together (single-gap trap,
  round-2 rule).
- The **dominant case is a one-line halving induction** (proven here at
  scout level): halve `a_1`, new max `= M/2`, apply `W(n−1)`.
- The **non-dominant `a_3 > a_1/2` sub-case is THE crux** — attack it via a
  **two-variable IH** `D* ≤ f(M, M_2, n)` (the pairing move removes `a_1, a_2`
  together, so a bound in `(M, M_2)` can be tighter than one in `M` alone).
  Concrete sub-target: prove `D* ≤ M/2^n` for non-dominant configs by
  induction where the IH tracks `(max, second-max)`. The base n=2 is already
  certified (`n2-upper-bound-complete`).
- The M/2^n bound is **tight uniquely at the tower**, so it cannot be
  improved — it is the right statement.

**G1 vs G2 this round:** they are the SAME target (the non-dominant
below-threshold wall). Do not split. The Max-bound is the better framing
than "exchange monotonicity" (which is killed by the majorization
counterexample) — frame the slug as "strengthened piece-count-free IH
`D* ≤ M/2^n`," with the two-variable refinement as the non-dominant
sub-step.

**Dead end to avoid:** majorization / Schur-convexity / Karamata — `D*` is
not Schur-convex (decisive counterexamples). Do not frame the induction as
"tower is the most-spread / most-majorizing config."

**Prior progress to build on (certified, importable):** `n2-upper-bound-
complete` (n=2 base, the averaging-bound mechanism), `parallel-halving-
saturates-tower` (the equality witness `D(T_n)=1/D_n`), `pl-breakpoint-
minimum` (B1 — Xiang optimum at a tie refinement, justifies the breakpoint
search), `claim-game-odd-index` (Lemma 0), `D-equals-parity-integral`
(residual-integral language for Route b if the outliner wants a fallback).

**Honest risk note:** the Max-bound is a CONJECTURE (strongly verified, not
proved). The non-dominant `a_3 > a_1/2` case is where it could still fail
in general (it holds in all 2860+ tests, but no proof yet). The outliner
should mark the non-dominant sub-step as an explicit GAP and have the
builder attack it with the two-variable IH; if it resists, the fallback is
Route (b)'s residual-integral characterization. The dominant case +
factorization is certifiable independently as proven scaffolding regardless.
