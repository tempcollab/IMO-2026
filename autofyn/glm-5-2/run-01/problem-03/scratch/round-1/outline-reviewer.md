# imo-2026-03 — outline-reviewer report (round 1)

## Preamble / sanity checks performed

- **Conjectured answer `c(n)=2^n/(2^{n+1}−1)` numerically solid.** Verified n=2,3 tower resistance under the *correct* ≤n-mark budget (each mark splits one piece into two): worst observed odd-index = target *exactly* (n=2: 4/7, n=3: 8/15), no violations in 5000+ random + adversarial (split-largest) trials per n. The earlier "violations" in my first run were an artefact of using more than n splits.
- **Layer-cake identity `odd-index sum = ∫ ceil(N(t)/2) dt` verified** on 2000 random multisets, 0 mismatches. The spine of `tail-count` is sound.
- **False-lemma counterexample reproduced.** `{3,1}/4` (superincreasing: 3>1) split `3→1.5+1.5` gives odd-index `1.5+1=0.625 < 0.75 = a_1`. So the generic "superincreasing ⇒ refinement can't drop odd-index below the top piece" lemma is FALSE. The dyadic tower `T_1=(2,1)/3` split `2→1+1` gives odd-index `2/3 = a_1` (holds) — confirming the *full dyadic tower* is special, not just any superincreasing sequence.
- **Parity-interleaving bug found in `tower-induction` / `self-similar` lower bounds (see below).** When the top piece is left unsplit, the whole's odd-index sum = `top + (EVEN-index of rest)`, not `top + (odd-index of rest)`. The IH lower-bounds the rest's *odd*-index, which gives an UPPER bound on the rest's even-index (rest-total fixed) — wrong direction. The lower-bound self-similar induction needs correct parity bookkeeping; the sketched mechanism points the IH at the wrong quantity.

## False-lemma audit (dispatch requirement)

None of the five approaches leans on the false generic lemma — the outliner's corrected-fact header was heeded. `tower-induction` and `self-similar` invoke the tower's *exact* `2^k = 1 + (sum of smaller)` self-similarity, not generic superincreasing dominance. `d-potential` uses the explicit tower-saturation config. `tail-count` uses the tower's `N(t)` step structure. `balanced-configs` imports Lemma L. All clear. The minimax explorer's original "superincreasing ⇒ odd-index ≥ top piece" conjecture is dead and does not leak into any approach file.

---

## Approach 1: `tower-induction` — CHANGES REQUESTED (build)

**Framing sound.** Self-similar induction on n for the lower bound (tower resists refinement) and a dominance case split for the upper bound is the right main line — the natural formalization of the outliner's corrected self-similarity observation and the verified n=1,2,3 behaviour.

**Issues the builder must close:**

1. **Lower-bound Lemma L, case (a) — WRONG-DIRECTION IH (load-bearing).** The sketch claims "top unsplit → occupies slot 1 (odd), rest (rescaled T_{n−1}) contributes ≥ 2^{n−1}/D_{n−1} by IH." But when the top piece is unsplit and largest, the whole's odd-index sum = `top + (rest's EVEN-index sum)` (slots 1,3,5,… = top, r_2, r_4,…), NOT `top + (rest's odd-index sum)`. The IH lower-bounds the rest's *odd*-index; since rest-total is fixed, that gives an *upper* bound on the rest's even-index — the wrong direction for lower-bounding the whole. The builder must either (i) prove a lower bound on the rest's even-index directly (a different lemma, not the IH of the same statement), or (ii) re-architect the induction to track both parities or to induct on a stronger two-variable statement (e.g. a simultaneous lower bound on odd- and even-index sums of the tower under refinement). This is the genuine crux of the lower bound; the n=2,3 numerics say it is true, but the mechanism as written does not yield it.

2. **Lower-bound Lemma L, case (b) — unjustified sub-claim.** "Every fragment ≥ 2^{n−1} (the second piece) occupies a top slot" is false as a universal: Xiang can split `2^n` into `{2^{n−1}+ε, 2^{n−1}−ε}` (both ≥ second piece, fine) OR into many small fragments (some < 2^{n−1}, falling below the second piece in sort order) OR into `{2^n−δ, δ}`. The case-(b) argument must handle arbitrary fragmentations of the top piece, including tiny fragments that get buried among the smaller tower pieces. The outline honestly flags case (b) as the load-bearing hard step — good — but the proposed mechanism ("fragments ≥ 2^{n−1} lock top slots") does not cover all fragmentations. Fix: a full case analysis on the largest fragment, or a direct `N(t)`-style argument.

3. **Upper-bound Lemma U, case (ii) — known wall.** The non-dominant branch (`L < 2^n/D_n`) with "mark nothing" is acknowledged false (many small equal pieces give odd-index ≈ 1/2 + small, which for small n exceeds the target since `2^n/D_n − 1/2 = 1/(2D_n)` is tiny). The outline suggests borrowing from `d-potential`. The builder must produce a real sub-argument for case (ii) — pairing, a weight bound, or an active (non-"mark-nothing") response. Flagging this as a gap is fine; leaving it as "then it follows" is not.

4. **Avoid the recorded dead end.** The naive "always halve the largest piece" Xiang strategy is dead (fails for near-equal Liu configs). The case split must route non-dominant configs to a *different* response. The outline's case (ii) is exactly where this dead end bites — the builder must not silently revive "halve the largest" in case (ii).

**Verdict:** right technique, fixable (hard) gaps. Build it. The lower-bound parity fix is the priority.

---

## Approach 2: `d-potential` — APPROVE (build)

**Framing sound and genuinely different.** A weight/potential `Φ` upper-bounding the alternating sum `D`, with a per-mark decay, is a legitimate monovariant attack on the *upper bound* (the hard direction) — the one framing that could give the upper bound cleanly if `Φ` exists. Knowledge base "Invariants & monovariants" supports the technique. The tower-saturation lower bound (the equality config `{2^{n−1},…,1,1}/D_n` gives `D = 1/D_n` exactly, verified) is a concrete computational anchor, not a hand-wave.

**Issues / warnings for the builder:**

1. **Produce a concrete `Φ` early.** The whole approach is vapor until `Φ` is defined. The builder's first task is to write down an explicit candidate `Φ` (the outline suggests base-2 weighted sum `Σ 2^{-i}·(stuff)`) and verify `Φ ≥ D` on examples. If no candidate survives small-case testing by mid-build, pivot or merge — do not spend the round on a potential that does not exist.

2. **The `−1` in `2^{n+1}−1` is the crux.** Naive halving-per-mark gives `2^n` (too strong; the tower achieves `1/D_n > 1/2^{n+1}`, so `1/2^n` is unattainable and the lemma would be false). The potential must capture the residual `1/D_n` the tower holds — the three-1 terminal of the equality config is where the `−1` enters. Pin this concretely.

3. **`Φ = D` is not progress.** If the only candidate is `Φ = D` itself, the decay lemma collapses to "Xiang reduces D," which is the upper bound restated. The builder must use a `Φ` strictly dominating `D` (a genuine relaxation), or the approach is circular.

4. **Upper-bound only?** The lower bound here is "tower saturates Φ" — this presupposes `Φ` is defined and is a valid upper bound on `D`. If `Φ` works for the upper bound, the lower bound comes for free; if `Φ` is only a lower-bound witness, it does not help the upper bound. Keep the upper bound as the primary target.

**Verdict:** high-ceiling, high-variance. The technique is right and the gap (existence of `Φ`) is the research question itself. Build it; gate on a concrete `Φ` by mid-build.

---

## Approach 3: `tail-count` — APPROVE (build)

**Framing sound and the most distinct of the five.** The layer-cake identity is verified (0 mismatches). This is the only approach whose lower-bound mechanism is *not* the self-similar sorted-list induction (which has the parity-interleaving bug) — instead the integral `∫ ceil(N(t)/2) dt` handles parity *structurally* via the ceiling, which may sidestep the case (a)/(b) parity trap that dogs `tower-induction` and `self-similar`. The aimo-0127 crux (per-threshold tail-count cap) is a reasonable hint to adapt, not cite.

**Issues / warnings for the builder:**

1. **Lower bound in `N(t)` language — prove it, don't inherit.** The outline says this "re-proves Lemma L in the N(t) language — distinct from tower-induction's sorted-list induction." Good — but the builder must actually give the `N(t)`-argument for tower resistance (splitting a piece shifts `N(t)` by `+1` on `[0,q]` and `−1` on `(p,L]`; show the ceiling-weighted integral cannot drop below the tower value). This is the promising half; do not reduce it to "Lemma L holds" by citation.

2. **Upper bound — the parity-coupling obstruction is the crux.** `N(t)` depends on the GLOBAL sorted order; splitting one piece re-sorts and shifts parities at many thresholds simultaneously. The aimo-0127 crux had *independent* per-threshold control; here the thresholds are coupled. The builder must either (i) find a sub-range structure where parities decouple, or (ii) use a different per-mark bookkeeping (e.g. track the net change `Δ∫ceil(N/2) ≤ 0` for the chosen split and telescope). If neither works, the upper bound fails and the approach becomes a lower-bound specialist.

3. **The `2^{n+1}−1` denominator** must emerge from the layer-cake of the tower: the threshold levels `2^k/D_n` and the parity structure of `N(t)` at each layer. Verify this concretely for n=3 in the build.

**Verdict:** best bet for a clean lower bound (parity handled by the ceiling, not by fragile induction) and a distinct upper-bound mechanism. Build it.

---

## Approach 4: `self-similar` — CHANGES REQUESTED (HOLD — do not build this round)

**Framing elegant for the lower bound, fatal-as-written for the upper bound.** The tower's rest `(2^n−1)/D_n` rescaled is exactly `T_{n−1}` (verified: `(2^n−1)/D_n · D_{n−1}/(2^n−1) = … = T_{n−1}` units). This is the cleanest lower-bound rescaling. BUT:

1. **Lower bound shares the parity-interleaving bug with `tower-induction`.** Lemma S case "Xiang ignores top → odd-index ≥ top + (rest bound)" has the same wrong-direction IH problem (whole odd-index = top + rest-*even*, IH bounds rest-*odd*). The builder must fix this exactly as in `tower-induction`. So for the lower bound, `self-similar` is not a fix for `tower-induction` — it has the *same* load-bearing gap, just expressed via a cleaner rescaling identity. It is not more advanced on the lower bound; it is the same lower bound in prettier dress.

2. **Upper bound is `tower-induction`'s case (ii) wall in disguise.** The outline admits: "the rest IS an (n−1)-subgame is only literally true for the TOWER rest, not for an arbitrary Liu config's rest." The self-similar reduction is exact for the tower, but the upper bound must handle ARBITRARY Liu configs, whose rest is not a rescaled tower. The suggested mitigation ("tower is worst case for Xiang — any non-tower config is easier") is itself the hard extremal claim = `tower-induction`'s case (ii). So `self-similar`'s upper bound bottoms out on the *same* wall as `tower-induction`.

**Why hold, not build:** Building both `tower-induction` and `self-similar` spends two parallel builders on the same lower-bound parity gap and the same upper-bound wall — the single-gap trap the orchestrator warns about. `self-similar` does not diversify the field's wall. Hold it in reserve: if `tower-induction`'s lower-bound parity fix succeeds, `self-similar` becomes redundant; if it fails, `self-similar` won't save it (same gap). Deploy `self-similar` next round only if the lower bound needs its cleaner rescaling identity as a scaffold, or if the upper-bound wall is cracked elsewhere and a clean lower-bound write-up is wanted.

**Verdict:** CHANGES REQUESTED — the approach is a legitimate whole attempt with a sound lower-bound *identity*, but it must (a) fix the parity-interleaving gap (shared with `tower-induction`) and (b) find a genuinely non-tower upper-bound reduction, not the extremal "tower is worst" claim. Registered (survivor), but held out of the build set this round to avoid the shared-wall trap.

---

## Approach 5: `balanced-configs` — CHANGES REQUESTED (HOLD — do not build this round)

**Technique partially sound, but B3 is circular.** Lemma B1 (piecewise-linearity ⇒ min at a tie/breakpoint) is sound — supported by knowledge base "Piecewise-concavity smoothing" (min at a breakpoint). This lemma is genuinely useful and could be exported as a shared lemma (Xiang's optimum is attained at a balanced refinement). BUT:

1. **Lemma B3 is the upper bound restated, not proved.** "Structurally verify, for every balanced refinement type, that odd-index sum ≤ 2^n/D_n" — this IS the upper bound. The approach proposes to prove the upper bound by checking every type satisfies the upper bound. Unless the "structural comparison to the dyadic balanced type" is a real monotonicity/exchange argument (not a type-by-type numerical check), this is circular. The outline admits B3 "may be the upper bound restated" — it is, as written.

2. **Type explosion.** The number of balanced combinatorial types grows rapidly with n; a structural (non-enumerative) argument is needed, and the outline does not have one. Without it, the approach only survives small n.

**Why hold, not build:** This is the riskiest framing (the outliner agrees — recommends reserve). Its one solid output (Lemma B1: optima are at balanced configs) is better treated as a *lemma to be proved once and imported* by the other approaches (it constrains Xiang's optimum to balanced refinements, useful for `d-potential`'s decay and `tail-count`'s threshold structure). Deploy next round as a scaffold / small-n verification if the four main lines stall on the upper bound, or harvest Lemma B1 into the shared lemma cache.

**Verdict:** CHANGES REQUESTED — B3 must be made non-circular (a real structural comparison, not the bound checked against itself). Registered (survivor) but held out of the build set.

---

## Field diversity assessment

The field does NOT collapse to one framing — good.
- **Lower-bound mechanisms:** three distinct — self-similar sorted-list induction (`tower-induction`, `self-similar` — these two are close, sharing the parity gap), `N(t)` integral (`tail-count` — handles parity via ceiling, most promising), potential saturation (`d-potential`).
- **Upper-bound mechanisms (the crux):** four distinct — dominance case split + induction (`tower-induction`), potential per-mark decay (`d-potential`), `N(t)` parity-telescoping (`tail-count`), finite-type structural check (`balanced-configs`). The walls are DIFFERENT (case-ii, Φ-existence, parity-coupling, B3-circular) — the field does not share one wall.
- **Shared-wall warning:** `tower-induction` and `self-similar` share BOTH the lower-bound parity gap AND the upper-bound case-(ii) wall. This is the one cluster of overlap; I hold `self-similar` to avoid spending two builders on one wall.

The hardest direction (UPPER bound, Xiang's adaptive strategy against arbitrary Liu configs) is attacked by four distinct mechanisms. The lower bound's parity interleaving is a genuine crux that the `tail-count` framing is best placed to sidestep.

---

## Ranking

All five approaches registered fresh (cold-start Elo 1500, no outcomes yet). Ranked by intrinsic promise for cracking BOTH bounds (lower via dyadic tower self-similarity / `N(t)` / potential saturation; upper via adaptive strategy / induction / potential / parity-telescoping). Pairwise comparisons, anchored to the gap analysis above:

- `tail-count` > `tower-induction` — cleaner lower-bound mechanism (verified layer-cake identity handles parity via the ceiling; `tower-induction`'s sorted-list IH has the wrong-direction parity bug).
- `tail-count` = `d-potential` (draw) — both have a distinct, plausible upper-bound mechanism with a hard but genuine gap; `tail-count` has the cleaner lower bound, `d-potential` the higher upper-bound ceiling.
- `d-potential` > `tower-induction` — more distinct upper-bound attack (the crux direction); `tower-induction`'s case (ii) is a known wall.
- `tower-induction` > `self-similar` (slight) — `tower-induction` attempts the upper-bound case (ii) directly; `self-similar`'s upper bound is the same wall in disguise, and its lower bound shares the same parity gap (not a fix).
- `tail-count` > `self-similar` — distinct upper-bound mechanism; `self-similar`'s upper bound is a wall and lower bound shares the parity bug.
- `d-potential` > `self-similar` — attacks the upper bound directly; `self-similar` stalls there.
- `self-similar` > `balanced-configs` — `self-similar` has a clean lower-bound identity; `balanced-configs`' B3 is circular.
- `tower-induction` > `balanced-configs` — whole attempt vs. circular B3.
- `d-potential` > `balanced-configs`; `tail-count` > `balanced-configs`.

Expected ordering (best→worst) after the K=32 update: **`tail-count` ≈ `d-potential` > `tower-induction` > `self-similar` > `balanced-configs`**.

---

## Registrations

All five approaches are survivors (none cut — no RETHINK). All are new, so all are registered fresh at cold-start Elo 1500:

- `tower-induction` — dyadic tower resists refinement (lower) + induction on n with dominance case split (upper); wall = non-dominant upper-bound case + lower-bound parity interleaving.
- `d-potential` — alternating-sum D with a base-2 weight potential Φ≥D that Xiang decays per mark to 1/D_n; wall = the exact potential giving the −1 in 2^{n+1}−1.
- `tail-count` — odd-index sum = ∫ceil(N(t)/2)dt; Xiang's splits shift N(t) parity per threshold, telescoping to the bound; wall = coupled global parities.
- `self-similar` — tower rest rescales to T_{n−1}; recurrence c(n)=top piece for both bounds; wall = upper bound for non-tower configs (rest is not a subgame).
- `balanced-configs` — piecewise-linearity ⇒ Xiang optimum at balanced (tie) refinements ⇒ finite types ⇒ structural check ≤ dyadic type; wall = B3 circular / type explosion.

No branching requested by the outliner this round (confirmed: no existing approaches to copy at round 1; the outliner's branching recommendation is explicitly "None at round 1").

---

## Build set

Three builders, one per slug — the three most distinct upper-bound mechanisms plus the cleanest lower-bound route. `self-similar` and `balanced-configs` held in reserve (shared-wall / circularity risks; deploy next round if the upper bound stalls on all three).

build set: tail-count, d-potential, tower-induction
