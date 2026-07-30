# outline-reviewer — imo-2026-03 round 4

Field reviewed: tail-count (ADVANCE), majorization-upper (REVISE), lp-dual-certificate (NEW). Plus the held/established population (tower-induction, gaps-leftover, d-potential, self-similar, balanced-configs). Headline numerics re-verified `Fraction`-exact:

- **Max-bound falsification** `(7,6,5,3)/21`: Xiang's pairing refinement yields margin `D*=1/21`, `M/8=1/24`, ratio `8/7` — VIOLATION exact; target `1/D_n=1/15` NOT violated (`1/21<1/15`). The Max-bound conjecture is genuinely dead; the answer `c(n)=2^n/(2^{n+1}−1)` survives. ✓
- **Plateau NO-SADDLE transport** at the T_3 odd-minimizer `{4.75,4,2,2,1,1,0.25}`: margin `D=1` at minimizer, midpoint `{4.375,4,2,2,1,1,0.625}`, and dyadic `{4,4,2,2,1,1,1}`. The simultaneous transport stays at `D=1` end-to-end. ✓ (D here = alternating-sum margin, NOT odd-index sum — the explorer's units are consistent.)

---

## tail-count — APPROVE

The plateau NO-SADDLE finding is the strongest lower lead in 4 rounds and the strategy is sound. The mechanism (telescoping zero-gradient / block condition) is genuine affine algebra: on a PL cell where each split's two fragments sit at same-sign positions, the gradient of D w.r.t. each cut is 0 (mass transfers within the same sign), so D is constant on the cell — verified Fraction-exact at the spine-7, spine-3, and V-shape-boundary instances. This is the non-dyadic generalization of the certified `block-contribution-formula`, and it correctly explains WHY the V-shape only blocks LOCAL (single-coordinate) moves while the GLOBAL simultaneous transport sidesteps it (the transport moves along tie FACES where the block condition holds, around the V-shape gradient that points into cell interiors).

The three gaps are honestly tiered and the numerics are correctly labeled verification-not-proof (no round-2 numerics-as-proof violation):
- **GAP-A** (2-leftover transport, spine-3, `a+d=t+1 ⇒ D=1`): concrete, provable this round, dominant case (45/816 cascade minimizers). Good certified-lemma candidate. The mass identity is the spine-length-3 instance of `gaps-leftover-identity` + `pairing-leftover-bound` — the mechanism is named, not a bare label.
- **GAP-B** (telescoping block lemma, `D` constant on a block-condition cell): clean affine-algebra (gradient = 0), the scaffold. Fallback if the mass identity resists.
- **GAP-C** (star-shaped property — the G1-closer): the hard step, verified T_3 (816/816 cascade, 322/322 split-larger, 17/17 split-tower) and T_4 (165/165 cascade 3-split) but OPEN generally. Mechanism (block condition on cell faces + PL-vertex iteration) is stated, not numerics-dressed.

**One issue to flag to the builder (not blocking):** step 4's constancy argument says "equal to its value at any point — in particular at the dyadic endpoint IF THE CELL CONTAINS ONE." The "if" is load-bearing. Not every combinatorial type's cell contains a dyadic config; for cells that do not, the star-path must cross INTO a cell that does, and the block condition must hold on the crossed face. This is the heart of GAP-C and must be addressed explicitly — the builder should not assume every type cell is dyadic-touching. The outliner's watch-out ("cross-type config sharing does NOT work; each type needs its own dyadic attainer") gestures at this but the cell-without-dyadic-endpoint sub-case is the real combinatorial expense. Also the 17 "disconnected" split-larger boundary points need the explicit boundary handling the outliner names.

The "D = 2^n − (towers at −)" simple formula is correctly warned FALSE for longer spines — use the block condition, not a mass formula. LOCAL rebalancing correctly marked dead. APPROVE.

---

## majorization-upper — CHANGES REQUESTED

The Max-bound falsification is correct and the V(n)=M_2/2^{n-1} replacement is a sound conjecture (unique clean form both tight at tower, ratio 1.000, AND 0 violations n=3,4,5 per the explorer's full candidate scan; no other tested form achieves both). The closure V(n) + certified above-threshold factorization ⇒ `D*≤1/D_n` is clean and correctly scoped (V(n) only needed for below-threshold configs with `a_2 < 2^{n-1}/D_n`). MB-Dom (dominant halving) remains valid. The counterexample family is bounded (worst ratio 8/7) and the actual target is never violated — the answer stands.

**Issue 1 (fixable, must fix): the V(3) proof is INCOMPLETE — it only covers the NON-DOMINANT case.** Step 4 says "Pair `a_1→{a_2, a_1−a_2}` (1 mark: two copies of `a_2` cancel at positions 1,2)." This requires `a_1−a_2 ≤ a_2`, i.e. `a_1 ≤ 2a_2` — the NON-dominant regime. I verified the dominant case FAILS under pairing: for `(8,3,2,2)/15` (`a_1=8 ≥ 2·3=6`), pairing `a_1→{3,5}` puts the two `a_2=3`'s at positions 2,3 (the fragment `a_1−a_2=5` is largest), giving margin `5 = a_1−a_2`, NOT `≤ M_2/4 = 3/4`. The dominant case needs HALVING: `a_1→{a_1/2, a_1/2}`; since `a_1/2 ≥ a_2 ≥ a_3…` the two halves sit at positions 1,2 and cancel; the rest has max `a_2 = M_2`; the certified `n2-upper-bound-complete` gives `D(rest,2 marks) ≤ a_2/4 = V(3)`. ✓ (verified). So V(3) needs a **case split**: dominant → halve (this is the n=3 instance of MB-Dom); non-dominant → pair (outliner's step 4). The builder must add the dominant-case halving argument; without it the V(3) "rigorous proof" claim is false.

**Issue 2 (correctly flagged, keep):** MB-Pair was conditional on the Max-bound IH `W(n−1)`, which is now FALSE at level `n−1` for `n≥4`. The outliner correctly flags the recheck under `V(n−1)`. The builder must re-derive MB-Pair's bound under the V IH and mark whether the `a_3≤a_1/2` sub-case still closes.

**Issue 3 (honest labeling, keep):** V(n≥4) is a CONJECTURE. The mutual W/V recursion and the 3-mark pairing cascade (residual `= a_1−a_2 ≤ M_2`) are traced for the 11 violators but NOT proved. The outliner correctly labels GAP-U2 as open. The "simple pairing IH fails 37%" finding is a genuine guardrail (do not frame V(n) proof as "pair `a_1`, apply V(n−1)"). Good.

**Issue 4:** The outliner's claim "V(n) survives where Max-bound fails because `V(n) ≤ Max-bound(n−1)` applied to the rest" is right for non-dominant (pair) and dominant (halve) but should be stated for BOTH regimes, not just pairing.

The technique is right (adaptive Xiang strategy with a second-largest-piece bound is the natural Max-bound successor, piece-count-free, tight at tower). The spine revision is sound. CHANGES REQUESTED — fix the V(3) case split, recheck MB-Pair under V, keep V(n≥4) as honest conjecture.

---

## lp-dual-certificate — CHANGES REQUESTED (registered as NEW)

Genuinely-different MACHINERY: LP strong duality / Farkas separating-hyperplane, certifying `min D ≥ (dual objective)` per combinatorial type from the CONSTRAINT structure (bin-sum equalities + sort order), not by bounding D directly. The non-circularity claim CHECKS OUT: the dual objective is `Σ_t y_eq[t]·2^{n−t}` — a signed TOWER-VALUE sum, never the sorted positions. This is NOT the round-3 claim-game dual (weights `w` on pieces, which re-derived the odd-index sum and was correctly dismissed as circular). The LP-dual certifies a lower bound on Xiang's refinement-min from the bin-sum + sort constraints; it does not re-derive the odd-index. Verified the per-type LP is exact (any composition of a tower piece into `r≥1` positive parts is a valid split tree), and `pl-breakpoint-minimum` reduces the global min to a min over type-cell vertices, so certifying each vertex certifies the global min. The clean-types sub-case (step 5, `y_eq=(1,−1,…,−1)`, objective `2^n−(2^n−1)=1` via the top-bin pigeonhole condition) is a genuine certifiable sub-result — the dominance margin `1` realized as a Farkas certificate. This is real new machinery and a real 4th framing. REGISTER.

**Issue 1 (must fix — conceptual error in the outline): the "CHEAP KILL" reframe (step 4) is FALSE.** The outline claims "the wall reduces to 'the dual never goes nonpositive' — a much WEAKER claim than 'D≥1 at every breakpoint.'" This is wrong. By LP STRONG DUALITY, `min D = max (dual objective)`. So "a feasible dual cert with objective `≥ 1` exists for every type" is LOGICALLY EQUIVALENT to "`min D ≥ 1` for every type" — the original G1 claim. It is not weaker. The "cheap kill" is a relabeling of the wall, not a reduction. The builder must NOT be told the structural lemma is easy or weaker; it is the Farkas-negation of the primal claim, equal in difficulty. The integrality observation (signed tower sum's min positive value is 1) is real and useful — it means ANY feasible cert with nonneg objective gives `≥ 1` for free — but the load-bearing step is proving a nonneg-objective feasible cert EXISTS, which IS the wall.

**Issue 2 (the honest risk, correctly flagged by the explorer):** only 0–3% of odd types admit the single uniform cert `y_eq=(1,−1,…,−1)`; a FAMILY of sign-patterns is required. The structural lemma "a feasible sign-pattern (with nonneg objective) ALWAYS exists for every tower-refinement type" is the real theorem, and (by the strong-duality equivalence above) it is as hard as G1. The outline correctly labels this as GAP-LP2 (the crux). The value of the slug is that the LP-feasibility ANGLE may be more tractable than the primal PL-transport (linear algebra vs geometric star-shaped), and it yields a different certified sub-result (clean types). But it does NOT avoid the wall in the sense of making the problem easier — it restates the wall in dual language. The builder should pursue it as a diversifier with realistic expectations, not as a shortcut.

**Issue 3 (do not let numerics become proof):** the "LP primal min ≥ 1 over every sampled type cell (verified n=2,3,4, 1000+ types)" is EVIDENCE, not proof. The round-2 rule forbids presenting sampled-type numerics as a min-frontier/exchange proof. The builder must prove the structural lemma structurally, not cite the sampler.

**Issue 4:** strong duality requires the primal LP to be feasible and bounded below. The outline's note ("D≥0 on the feasible region — the sort constraints make the alternating sum of a sorted-descending sequence ≥ the last term ≥ 0") needs a real check: the alternating sum of a sorted-descending sequence of length `m` is `≥ 0` for even `m` (pairs cancel positively) but for ODD `m` it is `p_1 − (p_2−p_3) − … − p_m`, which is `≥ 0` since `p_1 ≥ p_2 ≥ p_3` ⇒ `p_1 ≥ p_2−p_3`, etc., and the last term `−p_m` is absorbed by `p_{m−1} ≥ p_m`. So `D ≥ 0` holds for both parities — the builder should state this cleanly. Boundedness follows.

Verdict: the technique is valid (LP duality is a legitimate lower-bound method), the machinery is genuinely orthogonal, the non-circularity holds, and there is a certifiable clean-types sub-result. But the "cheap kill" oversell must be corrected (it is equivalence, not reduction) and the builder must treat the structural lemma as the G1-equivalent crux, not a weaker target. CHANGES REQUESTED — register as a diversifier, correct the cheap-kill framing, prove clean types as the certified sub-result, attempt the structural lemma honestly.

---

## Field diversity note (for the orchestrator)

The three lower-bound slugs now span FOUR genuinely-different machineries: PL/variational transport (tail-count), block/spine parity (tower-induction), charging/matching (gaps-leftover), and LP/Farkas duality (lp-dual-certificate). This satisfies the round-3 "open a 4th genuinely-different framing" directive — the LP-dual is NOT a relabeling of the charging argument (different object: shadow prices on bin-sum constraints vs per-pair charges; different wall-language: linear-algebra feasibility vs global position-sign). Good diversification. Caveat: the LP-dual's crux is logically equivalent to G1 by strong duality, so if the PL transport (tail-count GAP-C) closes G1 first, the LP-dual's open crux becomes moot (it would inherit the result). The two lower builds are live in parallel without sharing a wall, satisfying the single-gap-trap rule.

The upper bound remains a single slug (majorization-upper) — correct per the never-two-upper-slugs rule. Its spine was falsified but the V(n) replacement is sound; no second upper slug is warranted.

---

## Ranking

Outcomes anchored: tail-count (advanced, plateau NO-SADDLE = strongest lower lead) leads. majorization-upper (partial, Max-bound spine FALSIFIED) drops below the steady lower slugs — its Elo should fall to reflect the falsification, though the sound V(n) replacement + provable V(3) keep it above the cold-start newcomer and the stuck slug. tower-induction (advanced, even-group closed, 3 certified lemmas) and gaps-leftover (advanced, 2 certified lemmas, crux open) hold their lower ranks. lp-dual-certificate enters cold-start, ranked against the established field (loses to all advanced slugs, beats the stuck d-potential and held self-similar). d-potential (circular, stuck) and self-similar (held/subsumed) stay low; balanced-configs retired at the floor.

Key head-to-head resolutions:
- tail-count beats majorization-upper (advanced + plateau breakthrough vs partial + falsified spine).
- tail-count beats tower-induction, gaps-leftover (NO-SADDLE transport mechanism is the new momentum; the other two are steady-but-stalled).
- tail-count beats lp-dual-certificate (established verified mechanism vs unproven newcomer).
- tower-induction beats majorization-upper (advanced vs partial — the Max-bound falsification is a real setback even with V(n) recovery).
- gaps-leftover beats majorization-upper (advanced vs partial, by the outcome anchor).
- majorization-upper beats lp-dual-certificate (V(3) provable + sound V(n) vs structural lemma equivalent to G1) and beats d-potential (active upper vs stuck).
- tower-induction beats gaps-leftover (3 certified lemmas + even-group closed vs 2 lemmas + crux open) — close, slight edge.
- lp-dual-certificate beats d-potential (genuine new framing vs circular/stuck) and beats self-similar (new active vs held stale).
- self-similar beats d-potential (subsumed-but-live vs circular-stuck).

---

## Per-role rule update

ALWAYS: when a slug's headline CONJECTURE is falsified mid-run (round 4: Max-bound `D*≤M/2^n` killed by `(7,6,5,3)/21`), drop its Elo below the steady-advance slugs even if it offers a sound replacement — the falsification is a real setback the ranking must reflect; the replacement's soundness keeps it above cold-start newcomers but not above slugs that never faltered (imo-2026-03, round 4).

ALWAYS: when an LP/Farkas-dual slug claims its wall is "weaker" or a "cheap kill," check strong duality — `min primal = max dual` makes "dual objective ≥ 1" EQUIVALENT to "primal min ≥ 1," not weaker. Flag the oversell; the value of a dual framing is a different ATTACK ANGLE and different certified sub-results, not a reduction in difficulty (imo-2026-03, round 4).

NEVER: approve a "V(3) provable from the certified n=2 base" claim without checking BOTH regimes — pairing `a_1` (non-dominant `a_1<2a_2`) puts two `a_2`'s at positions 1,2 and cancels, but in the DOMINANT case `a_1≥2a_2` pairing puts `a_1−a_2 ≥ a_2` at position 1 and the bound fails; the dominant case needs HALVING (the MB-Dom n=3 instance). The V(3) proof is a two-case split, not the single pairing move (imo-2026-03, round 4).

---

build set: tail-count, majorization-upper, lp-dual-certificate
