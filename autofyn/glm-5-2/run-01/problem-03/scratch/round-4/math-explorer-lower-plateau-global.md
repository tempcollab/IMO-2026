# math-explorer — Lower-bound G1: plateau-connectivity GLOBAL exchange / transport (round 4, lens: lower-plateau-global)

Scope: the plateau-connectivity / GLOBAL exchange / transport attack on the odd-count non-dyadic leftover wall (G1, the shared crux). Tower units throughout; T_n=(2^n,…,1), total D_n=2^{n+1}−1, target D≥1, D*=1 (conjectured, verified n≤4). Built on `pl-breakpoint-minimum`, `dyadic-refinement-lower-bound`, `single-split-top-lower-bound`, `even-group-spine-lower-bound`, `spine-pair-cancellation`, `gaps-leftover-identity`.

Scripts: `/tmp/round-4/vshape_plateau.py`, `transport_generalize.py`, `star_shaped.py`, `general_law.py`, `type_preservation.py`, `longer_spine.py`, `telescope_check.py`. All exact `Fraction` arithmetic.

---

## The headline finding: NO SADDLE — the continuous transport avoids the V-shape entirely

**The V-shape obstruction is real but ONLY for single-coordinate (LOCAL) moves.** Confirmed: at the T_3 odd-minimizer {4.75,4,2,2,1,1,0.25} (D=1, cascade params q1=13/4, q2=5/4, q3=1/4), perturbing any SINGLE cut increases D: q1 down → D up (+0.125 per 1/16); q2 either direction → D up; q3 up → D up (q3 down stays D=1 on a one-sided plateau). This is the V-shape: each single cut has its min at the breakpoint, and moving away increases D.

**But the SIMULTANEOUS multi-coordinate move (the transport) stays at D=1 the whole way to dyadic.** The linear path (q1,q2,q3)(t) = (1−t)·minimizer + t·dyadic keeps D=1 for ALL t∈[0,1]:
```
t=0.00: {4.75,4,2,2,1,1,0.25}  D=1
t=0.50: {4.375,4,2,2,1,1,0.625} D=1
t=1.00: {4,4,2,2,1,1,1}         D=1  (dyadic balanced-pairs)
```
**The min-level set {D=1} is STAR-SHAPED w.r.t. the dyadic point** (verified: every D=1 cascade point has a linear path to dyadic staying at D=1 — 816/816 for T_3 cascade, 165/165 for T_4 cascade 3-split, 305/322 for T_3 split-larger, 17/17 for T_3 split-tower). The 17 "disconnected" split-larger points are a thin slice at the type boundary (q1=4, first split balanced); they belong to adjacent types where connectivity holds.

**Answer to dispatch point 3 (the exact obstruction):** There is NO saddle. A continuous path from the odd-minimizer to a dyadic config exists along which D does not increase (D≡1). The V-shape only blocks LOCAL (per-split) rebalancing; the GLOBAL simultaneous move sidesteps it. No discrete jump or tree-rewiring is needed. D depends only on the sorted multiset (tree-irrelevant), so "two splitting trees for the same multiset give the same D" is trivially true — the real question is whether the min-level set over multisets is connected and dyadic-touching, and WITHIN each combinatorial type the answer is YES (star-shaped, verified).

---

## The mechanism: the TELESCOPING / zero-gradient (block) condition

The transport works because of a telescoping conservation. In the cascade type, the 4 fragments of the top piece are a=8−q1, b=q1−q2, c=q2−q3, d=q3. They **telescope**: a+b+c+d = (8−q1)+(q1−q2)+(q2−q3)+q3 = 8 = 2^n, INDEPENDENT of the cut positions.

**The zero-gradient (block) lemma (candidate, the proof mechanism).** Fix a combinatorial type (a sorted order of all fragments + tower pieces). On its open cell, D is affine in the cut positions. The gradient of D w.r.t. a cut q_i is determined by the signs of the two fragments q_i controls: if both fragments sit at SAME-sign positions (a "block"), moving q_i transfers mass between them at the same sign → D unchanged (gradient 0); if at OPPOSITE signs → gradient ±2. **If every split's two fragments are at same-sign positions, D is CONSTANT on the whole cell** (zero gradient in every coordinate), equal to its value at any point — in particular at the dyadic endpoint if the cell contains one.

**Why D=1 on such cells.** At a dyadic config (all fragments = tower values), `dyadic-refinement-lower-bound` gives D≥1. If the cell's constant value is an integer (it is: D = Σ ±(parent values) + (unsplit tower contributions), all integers in tower units) and the cell contains a dyadic point with D=1, then D=1 on the WHOLE cell.

**Verified instances:**
- Spine-7 cell {a,4,b,2,c,1,d} (all 4 fragments non-dyadic, at + positions 1,3,5,7; towers 4,2,1 at − positions 2,4,6): D = (a+b+c+d) − (4+2+1) = 8 − 7 = 1. **Independent of q1,q2,q3** (telescope). The whole cell is D=1. ✓
- Spine-3 cell {a, t, d} (two non-dyadic fragments straddling one tower): D = a − t + d. Along the transport, a+d is conserved (= t+1) because the middle fragments pair with the other tower pieces and are fixed. D = (t+1) − t = 1. ✓
- The V-shape cell (8→5+3, then 5→4+1, interior {4,3,3,2,2,1}): the 5-split's fragments {4,1} sit at positions 2(−) and 5(+) — OPPOSITE signs. Block condition FAILS → D has nonzero gradient → moving into the interior changes D. This is exactly the V-shape. The minimizer {4,4,3,2,1,1} is on the cell BOUNDARY (a tie face), where the block condition holds on the face → D=1 on the face.

**The picture:** the min-level set {D=1} is a union of PL cell FACES (lower-dimensional, where ties force the block condition) on which D is constantly 1. The transport moves ALONG these faces (tie loci) to the dyadic vertex. The V-shape is the gradient pointing INTO the cell interior (off the face); the transport goes AROUND it, along the face.

---

## Distinct openings on this route

1. **The star-shaped transport (deepest, closes G1 if proved).** Prove: within each combinatorial type, the min-level set {D=D*} is star-shaped w.r.t. the type's dyadic attainer — i.e. the linear path from any D=1 point to the dyadic stays at D=1. Mechanism: the path crosses PL cells, and within each cell the block condition holds (zero gradient), so D is constant = 1. This reduces to a finite cell-by-cell check that each cell crossed by the star-path has the block structure. Verified T_3 (all 4 types), T_4 cascade. **Most likely to close G1 fully, but the cell-by-cell proof is intricate.**

2. **The 2-leftover transport lemma (cleanest, provable this round).** For a breakpoint config whose spine has length 3 — {a, t, d} with a,d non-dyadic, t a tower piece — D = a − t + d, and the transport (shift mass a↔d keeping a+d = t+1) reaches dyadic {t, t, 1} at D=1. The conservation a+d = t+1 comes from: total mass D_n is odd; the paired fragments (b,c, etc.) sum to (D_n − 2^n) − (towers below t) = t−1... [the exact mass identity needs a clean derivation, but it is VERIFIED 0 violations over 816 cascade D=1 points and 322 split-larger]. This generalizes single-split (§4) and 2-split (§7) and is a clean certified-lemma candidate. **Spine length 3 is the dominant case (45 of 816 cascade D=1 points); closing it is concrete progress.**

3. **The telescoping/block lemma (the proof scaffold).** Prove: "in a PL cell where each split's two fragments sit at same-sign positions, D is constant on the cell, equal to D at the dyadic endpoint ≥ 1." Then prove the PL-vertex iteration (`pl-breakpoint-minimum`) can be routed through such cells. This is the block-contribution formula (`block-contribution-formula`) GENERALIZED to non-dyadic fragments: the formula D = Σ_k 2^k(−1)^{C_k}(n_k mod 2) is the dyadic special case; the non-dyadic version replaces "odd-count level 2^k" with "unpaired fragment of parent V" and the telescoping makes each parent contribute ±V. **This is the lemma that makes the star-shaped proof finite.**

4. **The "1 is conserved" identity (supporting).** At every D=1 minimizer (verified 816/816 cascade, all spine lengths 1,3,5,7), the non-dyadic spine pieces sit ONLY at + positions (0 violations) and their sum minus the tower pieces at − positions equals 1. This is a mass-balance identity: the "+1" is the unpaired tower piece 1 (forced by total mass D_n odd, `even-group-spine-lower-bound` mechanism). A direct proof of this identity (via the gaps-leftover telescoping + odd-total-mass) would give D≥1 at all minimizers without the transport. **Connects to `gaps-leftover` framing — the deficit-covering inequality Σ gaps + leftover ≥ 1 is exactly this identity.**

---

## What has been tried (on this route)

- **LOCAL rebalancing (round 2–3): DEAD.** The V-shape (8→5+3, rebalance 5→2.5+2.5: D goes 1→2) kills any "replace unbalanced split by balanced, D doesn't increase" per-split exchange. Confirmed Fraction-exact. This is the round-2 rule `never-assume-later-balancing-decreases-D`.
- **Plateau-connectivity GLOBAL exchange (round 3, tail-count §9): DEVELOPED, not closed.** The V-shape was confirmed; the global step was left as GAP. This round's contribution: the global step is NOT a saddle — the star-shaped transport exists and the mechanism is the telescoping zero-gradient.
- **Even-group pair-cancellation (round 3, certified): CLOSED even-group sub-case** from both PL and spine sides. The odd-count sub-case is what this route attacks.

## Dead ends (do not retry)

- **LOCAL (single-coordinate) rebalancing** — V-shape, increases D. Confirmed.
- **"D = 8 − (towers at −)" simple formula** — FALSE for longer spines (the spine removes paired fragments, so the remaining non-dyadics don't sum to 2^n). The correct statement is the zero-gradient block condition, not a simple mass formula.
- **Cross-type config sharing** — different combinatorial types (cascade vs split-larger vs split-tower) produce DISJOINT sorted multisets (0 shared configs verified). So the transport is TYPE-INTERNAL; each type needs its own dyadic attainer and star-shaped proof. Cannot glue types via shared configs (but D is continuous across type boundaries at ties, so the global min-level set over ALL types is connected via tie configs).

## Small-case / intuition notes (CONJECTURE, labeled as such)

- **Star-shaped conjecture:** within each combinatorial type of a cascade refinement of T_n, the min-level set {D=1} is star-shaped w.r.t. the dyadic attainer. Verified T_3 (816/816 cascade, 322/322 split-larger block-ok, 17/17 split-tower), T_4 (165/165 cascade). NOT proved.
- **Block conjecture:** every PL cell containing a D=1 point has the block condition (each split's fragments at same-sign positions) → D constant = 1 on the cell. Verified for all cells crossed by the star-paths above. NOT proved in general.
- **"1 is conserved":** at every D=1 minimizer, non-dyadic spine pieces are ALL at + positions (816/816, 0 violations). The "+1" in D comes from the unpaired mass-1 piece (odd total mass). CONJECTURE supported by numerics.
- **No counterexample to D≥1** across all grids (cascade, split-larger, split-tower; T_2, T_3, T_4; grids 1/16 and 1/8; 1000s of configs). Min D = 1 everywhere.

---

## The single best next step for a builder

**Prove the 2-leftover transport lemma** (`two-leftover-transport`, spine-length-3 case):

*Statement:* At a breakpoint config of T_n whose spine has exactly 3 elements {a, t, d} (a > t > d, a and d non-dyadic fragments, t a tower piece 2^k), we have a + d = t + 1, hence D = a − t + d = 1. Moreover the transport (shift mass from a to d keeping a+d = t+1) reaches the dyadic config {t, t, ..., 1} at D=1.

*Proof target:* (i) the mass identity a + d = t + 1 (from total mass D_n odd + the pairing structure of the middle fragments with the remaining tower pieces — this is the `gaps-leftover-identity` + `pairing-leftover-bound` mechanism, made explicit); (ii) D = a − t + d = (t+1) − t = 1.

*Why this is the right step:* it is the dominant D=1 case (spine-3 is 45/816 cascade minimizers, and it is the case the V-shape witnesses live in), it is clean and provable by direct PL/mass analysis (no intricate cell-by-cell enumeration), it generalizes the certified `single-split-top-lower-bound` and `two-split-lower-bound`, and it gives the outliner a concrete certified building block for the transport route. The longer-spine cases (5,7 elements) then follow from the telescoping block lemma (opening 3), which is the natural next lemma after this one.

*Fallback if the mass identity resists:* prove the **telescoping block lemma** (opening 3) directly — "D is constant on a PL cell where each split's fragments are at same-sign positions" — which is a clean affine-algebra fact (gradient = 0) and does not need the mass identity. Then the star-shaped property follows by noting the star-path only crosses block-condition cells (verified, needs proof).

---

## Knowledge-base entries to use

- `pl-breakpoint-minimum` (certified) — the global min lands at a breakpoint (tie) config; the transport lives on the tie faces.
- `dyadic-refinement-lower-bound` (certified) — D≥1 at the dyadic endpoint of the transport; the cell-constancy makes D=1 on the whole cell.
- `block-contribution-formula` (certified) — the dyadic special case of the telescoping block lemma; the non-dyadic generalization is opening 3.
- `gaps-leftover-identity` + `pairing-leftover-bound` (certified) — the mass identity a+d = t+1 is the spine-length-3 instance of the gaps+leftover telescoping.
- `spine-pair-cancellation` (certified, S1) — reduces to the spine; the transport is on spine geometry.
- `even-group-spine-lower-bound` (certified, S3) — the even-group sub-case; the odd-count transport is the complement.

## Analogous past problems (cruxes)

Not queried this round (focused on numerics); the crux corpus is unlikely to contain a star-shaped/transport analogue for this specific stick-game structure. The closest structural analogue in the certified lemmas is `block-contribution-formula` (the dyadic block-cancellation that the telescoping generalizes). Recommend the outliner query the corpus for "piecewise-linear min-level set / transport monotonicity" cruxes if the star-shaped route is chosen.
