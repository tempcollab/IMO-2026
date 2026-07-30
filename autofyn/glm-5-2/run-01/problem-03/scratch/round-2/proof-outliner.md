# imo-2026-03 — proof-outliner field (round 2)

## imo-2026-03

Conjectured (verified n=1..4): `c(n) = 2^n/(2^{n+1}−1)`. Every approach targets the WHOLE
claim (lower bound: Liu's dyadic tower guarantees `D ≥ 1/D_n`; upper bound: Xiang caps every
Liu config at `D ≤ 1/D_n`; answer verified). Two load-bearing gaps remain from round 1:
(L-b) Xiang splits the tower's top piece — prove `D ≥ 1/D_n` for arbitrary fragmentation;
(U) general upper bound n≥2 — exhibit an adaptive Xiang strategy forcing `D ≤ 1/D_n` against
every Liu config. Certified lemmas importable from `results/imo-2026-03/lemmas/`: Lemma 0
(claim-game = odd-index, greedy optimal), tower-top-unsplit (case a, all n, no IH),
n1-base-both-bounds (c(1)=2/3), layer-cake-odd-index, D-equals-parity-integral,
closed-form-answer.

---

### tail-count: ADVANCE
Target: whole claim; this round closes lower-bound case (b) (top split) via the
variational/breakpoint/plateau route, and holds the upper-bound parity-coupling gap open.
Technique: `N(t)` tail-count integral + piecewise-linearity of `D` in split positions +
breakpoint-minimum + plateau argument. (Spine: the `ΔD = 2q − 2·O([0,q]) − 2·O((p,L])`
formula and the layer-cake identity `D = ∫(N mod 2)dt`.)
Skeleton:
  1. Reduce to `D* = max_L min_X D`, target `D* = 1/D_n` — by Lemma 0 (imported).
  2. Lower bound case (a) (top unsplit): `D ≥ 1/D_n` — by certified `tower-top-unsplit`
     (imported; no IH, dominance `2^n > 2^n−1`).
  3. Lower bound case (b) — Xiang splits the top piece into fragments. Formalize that `D`
     is **piecewise-linear** (slope in {−2,0,+2}) in each split position `q` within a fixed
     combinatorial type (sorted order) — by tracking how the sorted order changes as `q`
     varies; the breakpoints are where a fragment ties an adjacent tower piece.
  4. **Breakpoint-minimum**: a piecewise-linear function on a compact feasible region
     attains its global minimum at a breakpoint (where the type changes) or on a plateau
     touching a breakpoint — so WLOG the minimizer of `D` over all ≤n-mark refinements is a
     **breakpoint config** (every fragment ties an adjacent piece in sort order).
  5. **Dyadic breakpoints = frontiers**: the only way to split `2^k` into two powers of 2 is
     `2^{k−1}+2^{k−1}`, so dyadic breakpoint configs are exactly the balanced-split
     **frontiers**. Use the frontier recursion `D(T_m) = 2^m − D(T_{m−1})`, `D(T_0)=D(T_1)=1`
     (parity-flip on `[0,2^m]`), to show all frontiers give `D ≥ 1` (tower units).
  6. **Non-dyadic breakpoints (THE HARD STEP)**: show a non-dyadic breakpoint config lies on
     a **plateau** connecting to a dyadic breakpoint, so its `D` equals the `D` of a nearby
     dyadic breakpoint `≥ 1`. Mechanism: at a breakpoint the fragment `q` equals an adjacent
     piece `r`; the `ΔD` formula `2r − 2·O([0,r]) − 2·O((L−r,L])` depends on parity widths
     that are constant on the plateau, so `D` is flat between the non-dyadic breakpoint and
     the neighboring dyadic one.
  7. Upper bound n=1 (imported) + general-n parity-coupling gap stays open (recorded).
Key lemmas (claim + mechanism):
  - `ΔD = 2q − 2·O([0,q]) − 2·O((p,L])` — because the split flips parity on `[0,q]` (+1 to
    N) and `(p,L]` (−1 to N), and the integrand gain is `+1` where N was even, `−1` where odd.
  - Frontier recursion `D(T_m) = 2^m − D(T_{m−1})` — because the balanced split `2^m →
    2^{m−1}+2^{m−1}` flips parity on the entire `[0,2^m]`, so `D_new = 2^m − D_old`; the
    three copies of `2^{m−1}` sort to positions 1,2,3, the first two cancel, the third starts
    `T_{m−1}` at an odd index.
  - PL-minimum at a breakpoint — compactness + piecewise-linearity (knowledge base:
    "Piecewise-concavity smoothing").
Open gaps:
  - (G1) Step 6 — the plateau-connects-non-dyadic-to-dyadic claim. Verified n=3 (121 configs
    at D=1, only 1 dyadic, all on the same plateau), but the general proof that EVERY
    non-dyadic breakpoint lies on a plateau reaching a dyadic one is the open crux.
  - (G2) Multi-split compounding: after the first split `N(t)` is no longer the clean tower
    staircase, so `O([0,q])` for the second split is harder. The PL/breakpoint argument must
    handle ≥2 splits of the top (and splits of other pieces). The variational minimum is over
    ALL ≤n-mark refinements, not just single top-splits.
  - (U) Upper bound general n — parity coupling across thresholds (held open).
Cases to cover: single top-split (balanced regime q≈2^{n−1} is the tight case); unequal
single split; multi-split of top; splits of non-top pieces.
Watch out for: the crude bound `D_rest ≤ largest rest piece` degenerates exactly at the
balanced minimum — do NOT revive it (round-1 dead end); the PL argument must use the `ΔD`
formula's parity structure, not the crude bound. Avoid the B3 circularity (checking every
type ≤ bound IS the bound) — the plateau argument must be a genuine structural/continuity
claim, not a type enumeration.
Imported lemmas: Lemma 0, tower-top-unsplit, layer-cake-odd-index, D-equals-parity-integral,
n1-base-both-bounds, closed-form-answer.
Why distinct: the only approach whose lower-bound engine is the `N(t)`-integral /
piecewise-linearity-in-split-position framing; handles parity structurally via the ceiling
and the `ΔD` formula, not via sorted-list self-similar IH.

---

### tower-induction: REVISE
Target: whole claim; this round REPLACES the self-similar IH lower-bound engine (which
bottomed out on the unequal/multi-split interleaving) with the **frontier recursion** as a
cleaner lower-bound scaffold, and keeps the upper-bound induction gap honest.
Technique: binary-tree / frontier framing + parity-flip recursion `D(T_m)=2^m−D(T_{m−1})` as
the lower-bound engine (absorbing what would have been a standalone `frontier-recursion`
slug — explorer A judged it a scaffold, not standalone; folding it here avoids the shared
non-dyadic-breakpoint wall with `tail-count`). Upper bound stays the dominance-case-split
induction with the below-threshold gap open (NOT built as a rival to `majorization-upper`).
Skeleton:
  1. Reduce via Lemma 0 (imported); tower `T_n = (2^n,…,1)/D_n`.
  2. Lower bound case (a) (top unsplit) — certified `tower-top-unsplit` (imported).
  3. Lower bound case (b-i) (balanced top split, one mark): `D → D(T_{n−1})` by the
     parity-flip identity (frontier recursion base) — conditionally closed in round 1;
     THIS round extract it as a standalone importable lemma and prove the recursion
     `D(T_m)=2^m−D(T_{m−1})` rigorously for all m.
  4. Lower bound case (b-ii) (unequal single split) + (b-iii) (multi-split): REVISE the
     engine. Instead of the self-similar IH (which can't control the fragment-rest
     interleaving), use the **frontier-minimum lemma**: among all balanced-split frontiers
     of `T_n` (expand a subset of levels, each `2^k→2^{k−1}+2^{k−1}`), the minimum `D` among
     those with topmost unexpanded level m is `D(T_m) ≥ 1`. Then argue (as a GAP) that
     arbitrary (unbalanced, multi-) splits reduce to a frontier via an exchange/convexity
     step: unbalanced single splits are AS GOOD (plateau) but not better; unbalanced
     multi-splits are STRICTLY WORSE for Xiang — so the minimizer is a frontier.
  5. Upper bound n=1 (imported); general-n induction: dominant case set up (halving L when
     `L ≥ 2·a_2`), non-dominant case left as explicit GAP (note: `majorization-upper` carries
     the upper-bound attack this round; this slug's upper-bound section is a fallback, not the
     primary upper-bound route).
Key lemmas (claim + mechanism):
  - `D(T_m) = 2^m − D(T_{m−1})`, `D(T_0)=D(T_1)=1` — balanced split flips parity on all of
    `[0,2^m]`; three copies of `2^{m−1}` at positions 1,2,3, first two cancel.
  - Frontier-minimum `= D(T_m)` (verified n=3..6, NOT yet proved) — expanding all levels
    above m (cascading down) gives `D(T_m)`; the claim "expanding all above m is optimal" is
    the exchange/monotonicity step (GAP).
  - Sign-budget identity `D(M) = 1/D_n + 2(O_{R'} − E_F)` (round 1) — reformulation, keeps
    the interleaving crux visible as `O_{R'} ≥ E_F`.
Open gaps:
  - (G1) Frontier-minimum lemma: prove "expanding all levels above m is optimal" — the
    non-monotonicity of expansion (expanding level 3 alone INCREASES D for n=4) blocks a
    naive monotone argument; needs an exchange step.
  - (G2) Unbalanced→frontier reduction: show unbalanced multi-splits are strictly worse for
    Xiang (so the minimizer is a frontier). Asymmetry: single unbalanced = plateau (as good),
    multi unbalanced = strict (worse) — the reduction is non-trivial. THIS is the shared
    sub-step with `tail-count`'s non-dyadic-breakpoint gap; be honest it is the same wall
    viewed from the frontier side.
  - (U) Upper bound general n — dominant recurrence doesn't factor through `c(n−1)`;
    non-dominant "mark nothing" too weak. Held open (fallback only).
Cases to cover: balanced cascade (tight); single unequal split; multi-split; non-top splits.
Watch out for: the round-1 parity-interleaving bug is FIXED in case (a) by the
`D(M)=A−D(R')` sign flip — do NOT reintroduce a wrong-direction IH on the rest's odd-index;
the frontier recursion must track the alternating `D` directly. Do NOT build a separate
`frontier-recursion` slug (explorer A: scaffold not standalone; shares the
non-dyadic-breakpoint wall with `tail-count`).
Imported lemmas: Lemma 0 (cleanest sign-correct proof lives here), tower-top-unsplit,
n1-base-both-bounds, closed-form-answer.
Why distinct: the binary-tree / frontier framing is a different language from `tail-count`'s
integral/PL framing — its engine is the parity-flip recursion on the tower staircase, not
the `ΔD` formula. The two lower-bound routes converge on the same non-dyadic sub-step but
attack it from opposite machinery (frontier monotonicity vs. plateau continuity).

---

### majorization-upper: NEW
Target: the WHOLE claim, but this round's load-bearing contribution is the UPPER bound
(Xiang caps every Liu config at `D ≤ 1/D_n`); the lower bound is cited from the certified
lemmas + the advancing `tail-count`/`tower-induction` slugs.
Technique: extremal/exchange — "the dyadic tower `T_n` is the UNIQUE worst Liu config" +
config-adaptive pairing. Absorbs explorer B's dominant-factorization + pairing lemmas as
PROVEN scaffolding (clean cases) and explorer C's parallel-halving-saturates-tower as the
witness. The monotonicity/exchange step is THE hard step. (Spine: majorization / exchange
monotonicity of `min_Xiang D`, with the tower as the maximal element.)
Skeleton:
  1. Reduce via Lemma 0 (imported); target `D* = 1/D_n`.
  2. LOWER bound: cite `tower-top-unsplit` (case a) + the advancing lower-bound slugs for
     case (b). The tower `T_n` is Liu's witness config.
  3. UPPER bound — witness against the tower: prove (mechanically) the **parallel-halving
     lemma**: splitting each of the tower's `n` largest pieces in half (one mark each) yields
     the balanced-pairs config `{2^{n−1},2^{n−1},…,1,1,1}/D_n` with `D = 1/D_n` exactly (by
     the dyadic identity `2^k = 2·2^{k−1}`; verified n=1..5). This is Xiang's upper-bound
     witness against the tower — the symmetric twin of the lower-bound equality config.
  4. UPPER bound — clean cases (PROVEN scaffolding from explorer B, to be written up and
     certified as lemmas):
     (a) **Dominant case** (`L ≥ 2·a_2` AND `L ≥ 2^n/D_n`): halve `L` → `D(total)=D(rest)`,
         `R ≤ D_{n−1}/D_n`, induction closes via `(2^n−1)/D_{n−1} = 1`. EXACT, verified n=2..7.
     (b) **Non-dominant case B1** (`L < 2·a_2`, `a_2 ≥ 2^{n−1}/D_n`): pair `L→(a_2, L−a_2)`,
         two copies of `a_2` cancel at positions 1,2, `R' = 1−2·a_2 ≤ D_{n−1}/D_n`,
         induction closes. Verified 0 failures n=2,3.
  5. UPPER bound — THE HARD STEP (the exchange): prove the tower is the UNIQUE worst Liu
     config. For every `L ≠ T_n`, Xiang has ≤n adaptive marks with `D < 1/D_n` (often `D=0`
     for n=2). Mechanism to prove: a **smoothing/exchange monotonicity** — moving any
     consecutive ratio `b_k/b_{k+1}` toward the dyadic 2:1 only INCREASES `min_Xiang D`; the
     dyadic ratio 2 is hardest because it forces the pairing cascade to continue all the way
     down, accumulating the maximal residual `1/D_n`. When `b_k/b_{k+1} > 2`, split `b_k`
     asymmetrically to match `b_{k+1}`; when `< 2`, split `b_{k+1}`. Formalize via the
     `D = ∫(N mod 2)dt` residual language: Xiang's n marks create n canceling pairs leaving
     one unpaired residual; the tower's dyadic structure forces the residual to be exactly
     `1/D_n`, any ratio deviation lets Xiang reduce it strictly.
  6. Below-threshold regime (cases C, B2: `L < 2^n/D_n`, n≥3) — the residual gap. Fallback
     mechanism (NOT a rival slug): a strengthened two-variable IH `D ≤ f(R,M,n)` tighter
     when the max piece M is small, OR the max-reduction argument (each mark halves the max,
     after n marks max < 1/D_n so D ≤ max < 1/D_n) — the tension is small-max-reduction
     coincides with small-D, and proving the coincidence is the gap. Computationally
     verified (0 violations n=2,3); structurally easier than the dominant case.
  7. Verify the answer `c(n)=2^n/D_n` by substitution (import `closed-form-answer`).
Key lemmas (claim + mechanism):
  - Parallel-halving saturates the tower: `D = 1/D_n` exactly — by `2^k = 2·2^{k−1}`, each
    halved piece lands adjacent to the next tower piece, creating the balanced-pairs config
    whose unpaired residual is the bottom `1/D_n`.
  - Dominant factorization `D(total)=D(rest)`, `R ≤ D_{n−1}/D_n` — the two halves `L/2,L/2`
    occupy positions 1,2 (cancel) because `L/2 ≥ a_2`; the rest starts at position 3 (odd,
    same parity); `(2^n−1)/D_{n−1}=1` closes the arithmetic.
  - Pairing cancellation (non-dominant B1): two copies of `a_2` at positions 1,2 cancel
    because `a_2 ≥ L−a_2` and `a_2 ≥ a_3`.
  - Tower-is-hardest (CONJECTURE, verified n=1..4): the exchange monotonicity — the crux.
Open gaps:
  - (G1) THE exchange/monotonicity step (step 5): prove "moving any ratio toward dyadic 2:1
     increases `min_Xiang D`." This is the load-bearing hard step. Risk: the B3 circularity
     (checking every type ≤ bound IS the bound) — the builder must produce a GENUINE
     monotonicity/smoothing argument, not a type enumeration. The n=2 evidence is strong
     (every non-tower config admits D=0, not just <1/7), but the general-n exchange is open.
  - (G2) Below-threshold regime n≥3 (step 6): the strengthened IH or max-reduction
     coincidence. Computationally verified; structurally easier than the dominant case but
     not yet proved.
  - (G3) Adaptive-pairing specification for non-tower n≥3: the cascade structure is more
     intricate than n=2 (where every non-tower admits D=0); the residual is nonzero and the
     pairing strategy must be explicitly specified and proven to leave residual ≤ 1/D_n.
Cases to cover: dominant (near-tower, hardest); non-dominant B1 (clean); below-threshold
C/B2 (n≥3, the residual gap); far-from-tower (all pieces small, spare marks → pair all).
Watch out for: the B3 circularity trap — the exchange must be a real monotonicity, not a
type-by-type check. The "tower is worst" claim is verified computationally but the monotonicity
proof is the research question — do NOT present the numerics as a proof. Do NOT open a
separate `inductive-upper` slug (shared wall with this one per the diversity instruction);
B's strengthened-IH stays a FALLBACK within step 6. Avoid the naive "always halve largest"
dead end (fails near-equal configs) — the strategy is config-adaptive (halve dominant, pair
non-dominant, exchange non-tower).
Imported lemmas: Lemma 0, layer-cake-odd-index, D-equals-parity-integral (for the residual
language), closed-form-answer, n1-base-both-bounds, tower-top-unsplit (lower-bound cite);
TO CERTIFY this round: parallel-halving-saturates-tower, dominant-factorization,
pairing-cancellation-non-dominant, and Lemma B1 (Xiang's optimum at a balanced/tie
refinement — harvested from the retired `balanced-configs` slug, imported to restrict
Xiang's optimum to balanced refinements).
Why distinct: the ONLY upper-bound-first approach, and the only one whose spine is
extremal/exchange monotonicity (tower as unique worst) rather than per-mark decay
(`d-potential`), parity telescoping (`tail-count`), or self-similar induction
(`tower-induction`). Its hard step (exchange monotonicity) is a different wall from the
below-threshold IH and the parity-coupling — the field's upper-bound walls are now
genuinely far apart.

---

### d-potential: HOLD (do not build this round)
Target: whole claim via a per-config potential `Φ ≥ D` with per-mark decay.
Status: Φ programme genuinely STUCK. `Φ = D` shown circular (witness `T_1`: D stays 1/3
under the optimal mark, but `2/D+1 = 7` — the recursion `1/c(n)=1+1/(2c(n−1))` is a fact
about the GAME VALUE, not a per-config D decaying under one mark). No concrete non-circular
Φ exhibited; the "−1" in `2^{n+1}−1` lives at game-value level, not per-config decay. All
certified outputs (Lemma 0, closed-form recursion, n=1 base, Case A) are already in the
shared lemma cache — re-building gains nothing new unless a concrete Φ appears.
Recommendation: HOLD (registered, not built). Its certified lemmas stay importable. If the
`majorization-upper` exchange route cracks the upper bound, d-potential is superseded; if
both upper-bound routes stall, revisit d-potential next round with a **game-value potential**
(`Φ(L) = min_Xiang D(refine(L))`, which satisfies the decay by definition) as a possible
pivot — but that collapses toward the inductive route, so it is a last resort, not this
round's build.
Why distinct (even held): the only per-config-weight-function framing; kept as a reserve
framing in case the exchange/inductive upper-bound routes both fail.

---

### self-similar: HOLD (do not build this round)
Target: whole claim via the tower rest rescaling `T_{n−1}`.
Status: round-1 reviewer held it for the shared-wall trap (lower-bound parity gap shared
with `tower-induction`; upper bound = `tower-induction`'s case-(ii) wall in disguise). Its
one asset — the clean rescaling identity (tower rest = exact `T_{n−1}`) — is now absorbed
into `tower-induction` as the frontier-recursion scaffold. A separate build duplicates
`tower-induction`'s lower-bound work.
Recommendation: HOLD (registered, not built). Deploy only if `tower-induction`'s
frontier-revamped lower bound fails AND the rescaling identity is needed as a standalone
scaffold — but the frontier recursion already subsumes it.
Why distinct (even held): the cleanest rescaling identity; kept as scaffolding reserve.

---

### balanced-configs: RETIRE as build target; harvest Lemma B1
Target: was whole claim via piecewise-linearity ⇒ optima at balanced refinements ⇒ finite
types ⇒ structural check.
Status: B3 (the structural check) is CIRCULAR (checking every type ≤ bound IS the bound;
type explosion kills enumeration). The slug is NOT a viable whole attempt. BUT Lemma B1
(piecewise-linearity ⇒ Xiang's optimum is attained at a balanced/tie refinement) is sound,
certified by the round-1 reviewer, and genuinely useful: it restricts Xiang's continuous
optimization to a discrete search over balanced-split types.
Recommendation: RETIRE as a build target. HARVEST Lemma B1 into the shared lemma cache as
a candidate lemma; the `majorization-upper` builder certifies it as part of its build
(it imports B1 to restrict Xiang's optimum to balanced refinements, enabling the
exchange/monotonicity step to focus on balanced types only). Do NOT build B3-circular.
Why distinct (retired): its solid output (B1) lives on as an importable lemma; the framing
itself is subsumed by `majorization-upper`'s exchange route.

---

## Field summary

Build set (3 builders, one per slug):
- **tail-count** (ADVANCE) — lower-bound case (b) via variational/breakpoint/plateau.
- **tower-induction** (REVISE) — lower-bound case (b) via frontier recursion (absorbs the
  would-be `frontier-recursion` slug).
- **majorization-upper** (NEW) — upper bound via tower-is-worst exchange/adaptive pairing;
  absorbs B's dominant/pairing lemmas as scaffolding, certifies Lemma B1.

Holds: d-potential (Φ stuck), self-similar (subsumed by tower-induction).
Retired: balanced-configs (B3 circular; harvest B1).

The three build slugs attack DIFFERENT walls: tail-count = non-dyadic-breakpoint plateau
(lower bound, integral language); tower-induction = frontier monotonicity (lower bound,
tree language); majorization-upper = exchange monotonicity (upper bound, extremal
language). The lower-bound slugs converge on a shared sub-step (non-dyadic↔dyadic
reduction) but from opposite machinery; the upper-bound slug's wall (exchange monotonicity)
is far from both. No two slugs share a single wall.

branching requested: none.
