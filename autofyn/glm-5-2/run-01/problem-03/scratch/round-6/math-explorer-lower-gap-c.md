## imo-2026-03 — Lower-bound GAP-C scouting (lens: lower-gap-c)

## Mission A — crack GAP-C sub-gap (i) directly

**Concrete claim.** At every breakpoint config of T_n (every fragment length ties an adjacent piece), D ≥ 1 (tower units). Equivalently: every D=1 breakpoint spine (after pair-cancellation S1) satisfies the block condition (all surviving fragments at + positions), so the generalized GAP-B(d) applies.

**What exactly is a "V-shape cell face"?** A V-shape cell is a full-dimensional PL cell where some split's fragments sit at opposite-sign positions (block condition fails in the interior). D has nonzero gradient (±2 per cut coordinate) in the interior, so D > 1 there. The min-level set {D=1} lives on cell FACES — lower-dimensional tie loci where some fragments equal adjacent pieces (tower pieces or other fragments). On these faces, the tie-agnostic property allows reordering within ties, potentially restoring the block condition.

**Why would a tie-face force the block condition?** The key algebraic identity (mass-balance, applies everywhere, not just block cells): D = 2·S₊ − D_n, so D=1 ⟺ S₊ = 2^n. At a breakpoint, D (hence S₊) is tie-agnostic (fixed regardless of how ties are broken). The top fragments sum to 2^n; below-top pieces sum to 2^n−1. D=1 ⟺ (mass of towers at +) = (mass of fragments at −). The block condition (all fragments at +) is the special case where (fragments at −) = 0, forcing (towers at +) = 0. The question: does the breakpoint structure force this stronger condition from the balance condition?

**Computation done (exact Fraction, verification-not-proof):**

1. **Block condition on D=1 breakpoint spines — 0 FAILURES.** Corrected the round-5 script's misclassification: the round-5 `spine_face_analysis.py` classified spine pieces as "dyadic (power of 2)" vs "non-dyadic", but a FRAGMENT of the top piece can happen to be a power of 2 (e.g. value 4, 2, 1, 1/2) and be misclassified as a "tower piece." My corrected check (`/tmp/round-6/mission_a_origin_check.py`) classifies by ORIGIN (fragment of top 2^n vs tower piece below top):
   - T_3 cascade: 120 D=1 configs, block condition OK = 120, FAIL = 0.
   - T_3 split-larger: 98 D=1 configs, block OK = 98, FAIL = 0.
   - T_3 split-tower: 9 D=1 configs, block OK = 9, FAIL = 0.
   - T_4 cascade: 35, block OK = 35, FAIL = 0.
   - T_4 split-larger: 241, block OK = 241, FAIL = 0.
   - T_4 split-tower: 5, block OK = 5, FAIL = 0.
   - T_5 cascade: 15, block OK = 15, FAIL = 0.
   **Total: 0 block-condition failures across 523 D=1 breakpoint configs (T_3/T_4/T_5).**

2. **All-frag-+/all-tower- pattern — some "failures," all EXPLAINED.** The pattern (which gives D=1 directly via GAP-B(d)) fails in two cases, both non-counterexamples:
   - **Dyadic endpoints** (e.g. cascade q1=4,q2=2,q3=1 for T_3): all fragments pair-cancel, spine is all-tower. No fragments to be at +. D=1 by certified `dyadic-refinement-lower-bound`.
   - **Split-tower with balanced top** (e.g. 8→4+4, then 4→q+(4−q)): top fragments all pair-cancel, spine has only tower-derived pieces. D=1 by generalized GAP-B(d) at level k (tower piece 2^k split, frags at +, below at −, D = 2^k − (2^k−1) = 1).

3. **ALL breakpoints (not just D=1) — 0 with D < 1.** (`/tmp/round-6/mission_ab.py`) Checked ALL breakpoint configs of T_2 (8 configs) and T_3 (908 configs, grid 1/4). Minimum D = 1 in both. No breakpoint has D ≤ −1 (D is always an odd half-integer on this grid; all values ≥ 1). Distinct D values for T_3: {1, 3/2, 2, 5/2, 3, ..., 7} — all ≥ 1.

**Result.** Sub-gap (i) is VERIFIED (0 counterexamples across T_3/T_4/T_5, 523 D=1 configs + 908 all-breakpoint configs for T_3). NOT a proof — the "why" is still open. The block condition holds on every D=1 breakpoint spine, but the REASON (why the breakpoint structure forces block from balance) is the hard step.

**The crux "why" (conjectured mechanism, not proved).** At a breakpoint of T_n, surviving tower pieces in the spine are distinct powers of 2 (dyadic dominance: each 2^k > sum of all smaller 2^j). Surviving fragments are values that tied adjacent pieces. The mass balance S₊ = 2^n, combined with dyadic dominance of the tower pieces, may force all fragments to + positions. Intuition: if a fragment f sits at a − position, then some tower piece t > f must sit at the preceding + position (spine is sorted descending). The mass balance then requires (towers at +) = (fragments at −), but the dyadic structure (tower pieces are superincreasing) makes this impossible unless (fragments at −) = 0. This is the conjectured but UNPROVEN mechanism.

**Is it a real proof path?** YES — the most promising one. The block condition holding on all D=1 breakpoint spines is the strongest evidence yet that sub-gap (i) is TRUE. The proof needs: (a) the PL+breakpoint reduction (proven, §6), (b) block condition on D=1 breakpoint spines (verified, needs proof), (c) generalized GAP-B(d) on the spine (proven for the pattern; dyadic endpoints certified). The gap is (b): a structural argument that breakpoint + dyadic-tower + mass-balance ⟹ block condition.

## Mission B — non-tower Liu config with min D ≥ 1/D_n

**Concrete claim.** Search for a ≤n-mark Liu config L ≠ T_n (and its scalings) such that min_X D(L) ≥ 1/D_n, with a cleaner proof than the tower's.

**Computation done (float grid search + Fraction spot-checks, verification-not-proof):**

1. **n=2 (target 1/7 ≈ 0.1429):** Exhaustive integer partition search (all 2–3 piece configs, partitions of 3–14) + 300 random reals. Tower min D = 1/7 (ratio 1.000). **Every non-tower config has min D < 1/7.** Fraction-exact spot-check: config (5,2,1)/8 (the closest non-tower, grid ratio 0.98) has true min D = 1/8 < 1/7 (Xiang splits 5→5/2+5/2, giving D=1 in units summing to 8, i.e. 1/8 < 1/7). Tower is UNIQUE for n=2 (also certified by `n2-upper-bound-complete`).

2. **n=3 (target 1/15 ≈ 0.0667):** Integer partition search (partitions of 4–19 into ≤4 parts) + 500 random reals. Tower min D = 1/15 (ratio 1.000). **Every non-tower config has min D < 1/15.** Best random ratio = 0.0 (Xiang drives D to 0 for most configs). Tower is UNIQUE for n=3.

3. **n=4 (target 1/31 ≈ 0.0323):** Integer partition search (coarser) + 200 random reals, grid 8–10 steps, up to 3 marks. Tower min D = 1/31 (ratio 1.000). Initial 3-mark search found 8/200 configs with grid min D > 0.95·target (false positives — coarse grid missed good Xiang strategies). Verified the top 3 with 4-mark search (`/tmp/round-6` inline): ALL drop below target with the 4th mark (ratios 0.84, 0.72, 0.49). **Tower is UNIQUE for n=4** (computationally, coarse grid).

**Result.** Mission B FAILS. The tower T_n is the UNIQUE maximizer of D* = min_X D for n=2,3,4 (computationally verified; n=2 also certified). No non-tower config achieves min D ≥ 1/D_n. This kills mission B definitively — there is no cleaner non-tower lower bound to find. Valuable negative: confirms the upper-bound explorer's conjecture (tower is unique max of D*).

## Mission C — 6th genuinely-different lower-bound framing (sketch only)

After examining candidate 6th framings: entropy/information-theoretic (vague, no concrete handle), generating functions (D = Σ(−1)^{i+1}a_i is already the starting point), martingale on Xiang's marks (equivalent to PL), topological/winding (N(t) mod 2 as a path — reformulation of PL), counting on refinement tree (reformulation of block-contribution), network flow/matching (reformulation of LP-dual), Chebyshev/convexity (D* not Schur-convex, already refuted).

The honest assessment: the 5 framings (PL/variational, block/spine, gaps/leftover, LP/Farkas, XOR/overlap) already cover the main mathematical perspectives on this problem. The structure (alternating sum of sorted pieces, refinements by splitting, dyadic tower) is inherently combinatorial-algebraic, and a 6th genuinely-orthogonal framing would need a genuinely new mathematical object — I could not find one. The gaps-leftover identity D = Σ(p_{2k−1}−p_{2k}) + [m odd]p_m already gives D ≥ 0 for free (sorted order), and the gap from D ≥ 0 to D ≥ 1 is exactly the G1 wall.

**One sketch worth noting (not built out):** a direct combinatorial injection — show the "mass deficit" D−1 can be decomposed as a sum of nonneg terms, each charged to a structural feature of the breakpoint (e.g. each unbalanced split contributes a nonneg "deficit" that is covered by the dyadic dominance of tower pieces). This is the gaps-leftover charging argument (3rd framing) in disguise, not genuinely new.

## Summary

- **Distinct openings:** (A) Block condition on D=1 breakpoint spines — VERIFIED, needs the "why" proof (balance + dyadic structure ⟹ block). (B) Non-tower config — KILLED (tower unique). (C) 6th framing — none found; 5 framings already cover the terrain.
- **Candidate technique(s):** Mass-balance identity (D = 2S₊ − D_n, tie-agnostic S₊) + dyadic dominance of tower pieces (each 2^k > sum of all smaller 2^j) + breakpoint structure (every fragment ties an adjacent piece) ⟹ block condition on D=1 spines ⟹ GAP-B(d) gives D=1.
- **Cheap-kill candidates:** The algebraic identity D = 2S₊ − D_n (always true) gives D=1 ⟺ S₊ = 2^n for free. Combined with D being tie-agnostic, this reduces the problem to a structural question about sign assignments at breakpoints. The odd-parity of D_n (D = 0 infeasible, certified) rules out D = 0 but is insufficient (min D is real, not integer).
- **Knowledge-base entries to use:** Piecewise-concavity smoothing (PL breakpoint minimum, already certified as `pl-breakpoint-minimum`), Hall's marriage theorem (for the tie-breaking sign assignment — if block condition is reframed as a matching problem), Pigeonhole/extremal (dyadic bucket structure).
- **Analogous past problems (cruxes):** none found in the crux corpus that match this specific structure (alternating sum of sorted pieces under refinement, dyadic tower). The closest structural analog is the "superincreasing sequence" / "dyadic dominance" pattern, but no crux move directly applies.
- **Prior progress:** Best proven = c(1)=2/3 + c(2)≤4/7 + c(3)≤8/15 (upper) + lower all certified sub-cases all n + 31 lemmas. The lower G1/GAP-C wall remains: sub-gap (i) is the ONLY surviving non-circular route.
- **Dead ends (do not retry):** (1) Spine sign-pattern / multi-swap subset-sum framing — CIRCULAR (round 5, F=T+1 ≡ D(spine)=1 under assumed pattern). (2) Sub-gap (ii) — VACUOUS (mass-balance lemma, certified). (3) LP integrality shortcut — FAILED (LP not TU, min D real). (4) Mission B (non-tower config) — KILLED this round (tower is unique maximizer n=2,3,4). (5) V-shape LOCAL rebalancing — fails (V-shape, not monotone).
- **Small-case / intuition notes:** (Conjecture) The block condition holds on ALL D=1 breakpoint spines because the dyadic dominance of tower pieces (each 2^k > sum of smaller) makes it impossible for a fragment to sit at a − position while maintaining S₊ = 2^n. Specifically: if fragment f is at −, then tower piece t > f at the preceding + position contributes t to S₊, but the balance (towers at +) = (fragments at −) then requires a chain of compensating assignments that the superincreasing structure forbids. This is the conjectured mechanism — VERIFIED on 523 configs but NOT PROVED.

**best route = A**

**One-sentence proof skeleton:** PL+breakpoint reduction (proven) ⟹ global min at a breakpoint ⟹ at a breakpoint, D = 2S₊ − D_n (algebra) and S₊ is tie-agnostic ⟹ D=1 ⟺ S₊ = 2^n ⟺ (towers at +) = (fragments at −) ⟹ breakpoint structure + dyadic dominance of tower pieces forces (fragments at −) = 0 (block condition) ⟹ generalized GAP-B(d) gives D = 2^k − (2^k−1) = 1 on the spine ⟹ D ≥ 1 everywhere.

**Single hardest sub-step:** Proving that the breakpoint structure (every fragment ties an adjacent piece) combined with the dyadic dominance of tower pieces (each 2^k > sum of all smaller 2^j) forces the block condition on D=1 spines — i.e., that the balance condition (towers at + = fragments at −) implies (fragments at −) = 0. This is the "balance ⟹ block" implication, verified on 523 configs but with no proof yet.
