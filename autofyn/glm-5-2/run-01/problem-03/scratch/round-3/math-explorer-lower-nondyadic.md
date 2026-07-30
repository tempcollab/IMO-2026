# math-explorer — Lower-bound G1: non-dyadic multi-split (round 3, lens: lower-nondyadic)

Scope: close the lower-bound case (b-ii) NON-DYADIC multi-split of T_n (prove D ≥ 1 at every non-dyadic multi-split breakpoint config, all n≥2). Tower units throughout; T_n=(2^n,…,1), total D_n=2^{n+1}−1, target D≥1. Built on the certified PL+breakpoint reduction (`pl-breakpoint-minimum`), the dyadic lower bound (`dyadic-refinement-lower-bound`, §5), and the single-split bound (`single-split-top-lower-bound`, §4).

All numbers below are exact `Fraction` or dense float grid (explicit step). Scripts: `/tmp/round-3/nondyadic_breakpoint.py`, `odd_groups_and_plateau.py`, `min_odd_check.py`.

---

## Terrain

### What is settled (certified, importable)
- **PL+breakpoint reduction (`pl-breakpoint-minimum`).** Global min of D over all ≤n-mark refinements of T_n is attained at a **breakpoint (tie) config** — a vertex of the PL complex. D is continuous PL (affine per combinatorial type); compactness + vertex-of-polytope argument. This REDUCES G1 to "D ≥ 1 at every breakpoint config" but does NOT by itself bound anything.
- **Dyadic breakpoints (`dyadic-refinement-lower-bound`, §5).** Every all-balanced-splits refinement of T_n has D ≥ 1, equality at the balanced-pairs cascade {2^{n-1},2^{n-1},…,2,2,1,1,1}. Closed all n.
- **Single-split breakpoints (`single-split-top-lower-bound`, §4).** One split of the top 2^n → p+q: D is PL in q with slopes {0,−2} (non-increasing), min on the plateau q∈[2^{n-2},2^{n-1}] = D(T_{n-1}) ≥ 1. Closed all n (dyadic AND non-dyadic single splits).
- **Frontier recursion (`frontier-recursion`).** D(T_n)+D(T_{n-1})=2^n, closed form D(T_n)=(2^{n+1}+(−1)^n)/3 ≥ 1.

### Structure of breakpoint configs (NEW this round)
A **strong breakpoint** = every fragment (split product) ties an adjacent piece in the sorted order. Two structural facts:

**(S1) Equal-adjacent pieces CANCEL in the alternating sum.** a_i = a_{i+1} ⟹ contribution (−1)^{i+1}a_i + (−1)^{i+2}a_{i+1} = 0. Removing the pair preserves the sign of every other piece (positions shift by 2, sign unchanged). So **D(full) = D(after removing all adjacent-equal pairs)**.

**(S2) At a strong breakpoint, a NON-dyadic fragment (value ≠ 2^k) cannot tie a tower piece (all tower pieces are powers of 2).** So it must tie another non-dyadic fragment of the same value. The non-dyadic fragments form adjacent-equal GROUPS (size ≥ 2). If the group size is EVEN, it fully cancels (contributes 0); if ODD ≥ 3, one copy survives into the "spine".

**The spine** = the config after removing ALL adjacent-equal pairs (both dyadic and non-dyadic). It is a strictly-decreasing sequence of DISTINCT values. It contains powers of 2 (the un-paired dyadic pieces) and possibly some non-dyadic leftovers (one per odd-count non-dyadic group).

**Clean sub-result (EVEN-group strong breakpoints):** if every non-dyadic group has even count, the spine = distinct powers of 2 only. For a nonempty strictly-decreasing sequence of distinct powers of 2 (each ≥ 2× the next), the largest exceeds the sum of all smaller (geometric bound 2^{k_1} > Σ_{i≥2} 2^{k_i} = 2^{k_2+1}−1 < 2^{k_1}); and the spine is nonempty because the total mass D_n is ODD while pairs contribute EVEN mass, so the unpaired mass is odd ⟹ 2^0=1 is in the spine. Hence **D = (alternating sum of distinct powers of 2) ≥ 1** (integer > 0). **This closes G1 for even-group strong breakpoints.**

### The obstruction: ODD-count non-dyadic groups EXIST and can be MINIMIZERS
- **Odd-group strong breakpoints exist (D ≥ 1, but not minimizers):** T_3, 3 cascading splits 8→x+(8−x)→x+(8−2x)→x+(8−3x) with 8−3x = 2^k (tower tie). For x=7/3 (k=0): config {4,7/3,7/3,7/3,2,1,1}, D=11/3, spine {4,7/3,2}, D(spine)=11/3. For x=4/3 (k=2): D=5/3, spine {2,4/3,1}. For T_4 x=5 (k=0): spine {8,5,4,2}, D=5. All D ≥ 1 but the spine has a non-dyadic leftover, so the "distinct powers of 2" dominance argument FAILS.
- **Odd-group MINIMIZERS exist (D = D* = 1):** the 3-split grid of T_3 (step 0.25, 9557 configs) has **321 configs with an odd non-dyadic group attaining D = 1 = D***. Example: {4.75, 4, 2, 2, 1, 1, 0.25} (lone 4.75=19/4 and lone 0.25=1/4), D = 4.75−4+2−2+1−1+0.25 = 1. Spine = {4.75, 4, 0.25}, D(spine)=1 — non-dyadic leftovers on BOTH sides of the tower piece 4. **So the pair-cancellation argument is INSUFFICIENT to close G1**: odd-group configs can be the global minimizer.

### PL-vertex ≠ strong breakpoint
The PL reduction lands the min at a VERTEX of the PL complex (each split's SMALLER fragment pinned at 0/balanced/tie). But the LARGER fragment (parent − q) of a split may be LONE (not tied) at a vertex. Concrete: {4,4,3,2,1,1} (q1=4 balanced, q2=1 ties tower 1) is a PL-vertex with a lone larger-fragment 3 — NOT a strong breakpoint. So "iterate to a strong breakpoint" is not automatic; the lone larger-fragment requires sliding a DIFFERENT coordinate to eliminate, and the V-shape obstruction (below) shows this is not always a local decrease.

### 2-split sub-case is cleanly closable (NEW partial result)
The 2-split min of D over refinements of T_n is **D(T_{n-2}) = (2^{n-1}+(−1)^{n-2})/3 ≥ 1** (NOT D(T_{n-1}) — the earlier claim was wrong), attained by the dyadic cascade 2^n→2^{n-1}+2^{n-1}→(one 2^{n-1})→2^{n-2}+2^{n-2}. Verified exactly n=3,4,5,6 (min=1,3,5,11 resp., all = D(T_{n-2})). The min-level set always contains this dyadic config. **The 2-split sub-case of G1 is closeable via the plateau-to-dyadic argument** (the dyadic attainer sits inside the min-level set; §5 gives D ≥ 1).

---

## Routes

### Route A — pair-cancellation + "minimizers have even groups" (CLEANEST if the lemma holds)
**Idea.** Prove: (i) at every minimizer breakpoint, non-dyadic groups are EVEN (so the spine = distinct powers of 2); (ii) the spine dominance argument gives D ≥ 1. Route A inherits the clean sub-result above.
**Hard step.** (ii) is clean. (i) is FALSE as stated — odd-group minimizers exist (321 of them for T_3 3-split). So Route A must instead prove **D(spine) ≥ 1 for spines with non-dyadic leftovers** (a strictly-decreasing mix of powers of 2 and non-dyadic values arising from the splitting tree). No clean bound found: the non-dyadic leftovers sit at + or − positions depending on global parity (e.g. 4.75@+ , 0.25@+ in {4.75,4,0.25} give D=1; but 7/3@− in {4,7/3,2} gives D=11/3). The "largest dominates" fails (4.75 < 2·4). A sign-bookkeeping argument tied to the splitting tree is needed but not evident.
**Likelihood.** Medium. The clean sub-result is a real partial; the odd-group spine bound is the open sub-step.

### Route B — plateau connectivity / global exchange (DEEPEST, closes G1 if it works)
**Idea.** Prove the min-level set {D = D*} always contains a DYADIC config. Then §5 (`dyadic-refinement-lower-bound`) directly gives D* ≥ 1. This is exactly tower-induction's "G2: unbalanced ≥ balanced" wall — same gap, opposite machinery.
**Hard step.** LOCAL rebalancing FAILS (round-2 V-shape warning, confirmed): 8→5+3 then 5→4+1 gives D=1; rebalancing the second split to 5→2.5+2.5 gives D=3 (INCREASES D). So the exchange "replace unbalanced split by balanced, D doesn't increase" is FALSE per-split. The required exchange is GLOBAL (a multi-coordinate deformation keeping D = D*), not a sequence of local rebalancings. No proof found; the V-shape is the obstruction to the natural induction.
**Likelihood.** Low-medium. This is the research-prize route; if closed it unifies the whole lower bound, but the V-shape makes the global step genuinely hard. Suggest pairing it with Route C as a fallback.

### Route C — direct case analysis on 2-breakpoint, then induct on split count (MOST TRACTABLE for concrete progress)
**Idea.** Compute D explicitly as a function of the two cut points for each 2-split combinatorial type (which piece is split second). Show min ≥ D(T_{n-2}) ≥ 1 (the 2-split sub-case, already numerically confirmed and the dyadic attainer is identified). Then handle 3-split by conditioning on the first two splits and using the 2-split result + single-split lemma as scaffolding, escalating to a "k-split min ≥ D(T_{n-k}) ≥ 1" induction (the natural extension of the frontier recursion to unbalanced multi-split).
**Hard step.** The induction "k-split min ≥ D(T_{n-k})" — the V-shape shows the second split's min is NOT at its balanced point after an unbalanced first split, so the clean "each balanced split reduces T_n → T_{n-1}" recursion does NOT extend to unbalanced. The 2-split base (k=2) works because the dyadic attainer is in the min-level set; the inductive step for k≥3 needs the plateau-connectivity of Route B or a direct 3-breakpoint case analysis.
**Likelihood.** Medium-high for k=2 (closeable this round as a certified lemma). Low-medium for k≥3 (hits the same V-shape wall).

### Route D — spine geometry for odd-group leftovers (SUPPORTING, not standalone)
**Idea.** Characterize where non-dyadic spine leftovers sit relative to the tower pieces and prove their net contribution keeps D ≥ 1. Observations: leftovers come from splitting-tree "ends" (top fragment and cascading-residual fragment); in {4.75,4,0.25} the two leftovers 4.75+0.25 = 5 straddle tower 4 and D = 5−4 = 1; in {4,7/3,2} the leftover 7/3 sits between 4 and 2 with D = 6−7/3 = 11/3.
**Hard step.** The sign of a leftover's contribution depends on global parity (its position in the spine), and there is no uniform "leftover contributes +" rule. A full solution here would essentially solve G1.
**Likelihood.** Low as a standalone route; useful as a lemma-source for Route A.

---

## Numerics (concrete D values at non-dyadic vs dyadic breakpoints)

### n=3, T_3=(8,4,2,1), D(T_3)=5, D(T_2)=3, D(T_1)=1, D*=1
| config | type | D | spine | D(spine) |
|---|---|---|---|---|
| {4,4,2,2,1,1,1} | dyadic balanced-pairs | 1 | {1} | 1 |
| {4,4,2,2,2,1} | dyadic 2-split cascade | 1 | {2,1} | 1 |
| {4,3,3,2,2,1} | non-dyadic strong bp, EVEN group (3:2) | 3 | {4,2} | 3 |
| {4,7/2,7/2,2,1,1} | non-dyadic strong bp, EVEN group | 2 | {4,2} | 2 |
| {5,4,2,2,1,1} | PL-vertex, LONE 5 (not strong) | 1 | {5,4} | 1 |
| {4,4,3,2,1,1} | PL-vertex, LONE 3 (not strong) | 1 | {4,3} | 1 |
| {4,7/3,7/3,7/3,2,1,1} | non-dyadic strong bp, ODD group (7/3:3) | 11/3 | {4,7/3,2} | 11/3 |
| {2,4/3,4/3,4/3,1,...} | non-dyadic strong bp, ODD group (4/3:3) | 5/3 | {2,4/3,1} | 5/3 |
| {4.75,4,2,2,1,1,0.25} | odd-group MINIMIZER (D=D*=1) | 1 | {4.75,4,0.25} | 1 |

**Key contrast:** dyadic breakpoints reach D*=1; non-dyadic EVEN-group strong bps have D∈{2,3,...} > D*; ODD-group strong bps have D∈{5/3,11/3,...} > D*; but ODD-group NON-strong (PL-vertex) configs {4.75,4,2,2,1,1,0.25} REACH D*=1 with a non-dyadic spine. So the min-level set is a large plateau containing dyadic, even-group, AND odd-group configs.

### n=4, T_4=(16,8,4,2,1), D(T_4)=11, D(T_3)=5, D(T_2)=3
- 2-split min D = 3 = D(T_2) (dyadic attainer {8,8,4,4,4,2,1}). Verified grid n=4.
- Non-dyadic strong bps (even group): {8,6,6,4,4,2,1} D=7 spine {8,4,2,1}; {8,7,7,4,2,2,1} D=5 spine {8,4,1}.
- Odd-group strong bps: x=8/3 spine {4,8/3,2,1} D=7/3; x=14/3 spine {8,14/3,4,1} D=19/3; x=5 spine {8,5,4,2} D=5.

### n=5,6 — 2-split min = D(T_{n-2}) confirmed
n=5: min=5=D(T_3). n=6: min=11=D(T_4). All ≥ 1.

### Plateau connectivity (n=3, 2-split, grid 1/12)
- D=1 plateau has 91 configs (split-smaller-fragment case) + 194 (split-larger case). The dyadic attainer {4,4,2,2,2,1} (q1=4,q2=2) IS in the plateau. So the min-level set contains a dyadic config. ✓ (consistent with Route B, but not a proof).

### V-shape obstruction (confirmed)
8→5+3, then split 5 → (5−q)+q: q=1 (tie, {4,4,3,2,1,1}) D=1; q=1.5 D=2; q=2 ({4,3,3,2,2,1}) D=3; q=2.5 (balanced, {4,2.5,2.5,2,1,...}) D=3. So D as a function of q is V-shaped with MIN at q=1 (a tie), NOT at the balanced point q=2.5. Rebalancing locally INCREASES D from 1 to 3. **This kills any "replace unbalanced by balanced" local exchange.**

### No counterexample to D ≥ 1
Across all grids (2-split n=3,4,5,6; 3-split T_3 step 0.25 = 9557 configs; exact Fraction tests of constructed strong bps), **no config has D < 1**. The plateau lead "D ≥ 1 everywhere" is intact; only the PROOF is missing.

---

## Recommendation

The outliner should advance the lower bound along TWO complementary slugs:

1. **Certify the 2-split sub-case as a lemma** (`two-split-lower-bound`): D ≥ D(T_{n-2}) ≥ 1 for every 2-mark refinement of T_n, all n≥2, with the dyadic cascade as the attainer. This is concrete, fully verified, and gives the outliner a clean certified building block. The proof: reduce 2-split breakpoints to the two structural types (split-smaller, split-larger), compute D as explicit PL in the two cut points, observe the min plateau touches the dyadic cascade where §5 applies. **This is the highest-confidence concrete progress this round.**

2. **Advance `tail-count` (PL/variational) on the 3-split + general case via Route B (plateau connectivity)**, framed as a GLOBAL exchange: prove the min-level set {D = D*} contains a dyadic config (not a per-split rebalancing — the V-shape rules that out). The mechanism to pursue: the PL-vertex iteration slides along ZERO-gradient directions (plateaus) until reaching a vertex where ALL coordinates are pinned; show this terminal vertex can be chosen dyadic (by routing the slide through dyadic-friendly directions). Pair with the even-group pair-cancellation sub-result as the fallback if the global step only reaches an even-group strong breakpoint.

3. **Keep `tower-induction` on the SAME wall** (its G2 = tail-count's G1, confirmed) but push its block-contribution formula toward a NON-dyadic generalization: track fragment values mod the tower skeleton and attempt a sign-bookkeeping bound on the spine (Route D). This is the genuinely different machinery (block/parity vs PL/variational) and should NOT be retired.

**Do NOT open a third lower-bound slug.** Routes A–D all bottom out on the same shared step (the global exchange / spine bound); a third slug would be a single-gap trap (CLAUDE.md). The two existing slugs (tail-count, tower-induction) already span the two machineries (PL vs block/parity); the outliner should diversify WITHIN them (Route B for tail-count, Route D for tower-induction) rather than spawning a rival.

**Honest assessment:** G1 is a genuine wall. The pair-cancellation gives a clean partial (even-group strong bps) but odd-group MINIMIZERS exist, so it does not close G1. The plateau-connectivity lead (Route B) is the most likely to close it but requires a non-local exchange argument that the V-shape makes subtle. The 2-split sub-case is the one piece that is cleanly closeable this round.
