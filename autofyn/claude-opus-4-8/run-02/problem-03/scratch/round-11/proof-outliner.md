## imo-2026-03

Field this round: advance the leader on the extremal-base-case lead (cut-tree explorer),
open ONE genuinely far-apart new slug on the discrete-allocation-corner lead (loaded-IH
explorer). Both import the certified FLOOR reduction (GAP L ⟺ I_n:=∫_{(0,θ)}⌊M/2⌋ ≤ 0,
M=N_{π_0}−N_{F'}, θ=2^{n−1}) but reach the wall by different ROUTES: the leader by a
recursive peel down to a FIXED extremal comparison object (uncut ladder L); the new slug
by a non-recursive finite LP-vertex classification of the whole allocation space. Upper
bound is DONE/certified — NO approach touches it. telescope stays PARKED (machinery home,
no builder).

---

peel-scale-rank-induction: advance
Target: GAP L (lower bound) for all n — for every dyadic refinement F=⊎_{j=0}^n π_j with
  Σa_j≤n, D̃(F)≥1; with certified lemmas/upper-bound.md this closes c(n)=2^n/(2^{n+1}−1).
Technique: strong induction on n via the top-scale peel + certified FLOOR reduction, now
  routed through the EXTREMAL BASE CASE b=0 (all budget on π_0, F' forced to the uncut
  ladder L={2^{n−1},…,2,1}). The lever is L's own dyadic dominance
  2^{n−j} > Σ_{i>j} 2^{n−i} at every scale (aimo-0117-style, banked round 1). This is a
  non-profile, cut-tree-origin route — not caught by the R8 equivalent-to-target meta.
Skeleton:
  1. Import FLOOR (lemmas/floor-half-reduction.md): GAP L ⟺ I_n=∫_{(0,θ)}⌊M/2⌋ ≤ 0,
     equality (D̃=1) exactly at the tie. Import PEEL/(SD)/(DIFF)/Invariant I and Case A
     (a_0=0, closed) from lemmas/peel-difference-bound.md. — certified, no re-derivation.
  2. **Base case b=0 (KEY, most tractable — prioritize).** When b=0, F' is the UNCUT
     ladder L={2^{n−1},…,2,1}, and I_n≤0 becomes the fixed-object statement
     **D̃(π_0 ⊎ L) ≥ 1 for every partition π_0 of 2^n into ≤ n+1 parts.** Prove by a
     THIRD nested peel: split off L's own top element θ=2^{n−1} and induct on n on the
     FIXED ladder, using dominance 2^{n−j} > Σ_{i>j}2^{n−i}. The (DIFF) bound
     D̃(π_0⊎L) ≥ |D̃(π_0)−D̃(L)| already closes everything except the thin near-balance
     shell D̃(π_0) ≈ D̃(L) (L's alternating sum is large: 1,3,5,11,21,… for n=1..5), so
     the residual to settle by dominance is small. — GAP (see below).
  3. **Reduction-to-base.** The maximum of I_n over the whole feasible family at fixed n
     is attained at b=0 (explorer finding 2: n=4 slice-maxima −3.69,−0.55,−0.281,−0.295,0
     for b=4..0, extremum exactly at b=0). Given this, GAP L for all F reduces to step 2.
     Mechanism: F' is always a refinement of L got by b cuts; the loaded IH on F' (a
     genuine dyadic refinement, D̃(F')≥1 AND its count-function g=N_{F'} is a
     ladder-refinement staircase) forces the vertex-optimum of I_n to sit at b=0. — GAP.
  4. Combine 2+3 ⇒ I_n≤0 for all feasible F ⇒ D̃(F)≥1 ⇒ GAP L ⇒ c(n) with the certified UB.
Key lemmas (claim + mechanism):
  - **Ladder-dominance base case** D̃(π_0⊎L)≥1 for all partitions π_0 of 2^n into ≤n+1
    parts — because at each dyadic scale L's part 2^{n−j} strictly exceeds the sum of all
    smaller ladder parts (Σ_{i>j}2^{n−i}=2^{n−j}−1), so inserting π_0's ≤n+1 parts (total
    2^n) can shift each odd/even merged rank by at most one ladder step and the alternating
    sum cannot drop below the single-unit floor; the third nested peel of θ against π_0
    plus the (n−1)-ladder IH makes this rigorous. Only the near-balance shell
    D̃(π_0)≈D̃(L) needs the dominance; (DIFF) closes the rest.
  - **Reduction-to-base (slice-max monotone in b)** sup_{feasible, given n,b} I_n is
    non-increasing in b, extremum at b=0 — because a further cut inside F' deepens the
    negative layers of M at the co-varying optimum. NOTE this is the SLICE-MAX statement
    (π_0 co-varies), NOT the pointwise fixed-π_0 monovariant, which is FALSE (R11 finding
    1, ~30% violations — banked dead end). Must be proven as an extremal-over-slice fact.
Open gaps: step 2 (ladder-dominance base — the concrete new deliverable, propose as a
  promotable lemma once proven) and step 3 (reduction-to-base slice-max monotonicity).
  Prioritize step 2: it is a clean self-contained fixed-object inequality.
Cases to cover: base case b=0 (step 2); inductive b>0 via step 3. Case A (a_0=0) already
  closed (certified). Base cases n=0,1 done.
Watch out for: (i) pointwise per-cut monotonicity holding π_0 FIXED is FALSE — do NOT use
  it (banked R11). (ii) merging even tie-blocks toward L can RAISE D̃ ({4,2,½,½}:2→3,
  banked R10) — the reduction must add cuts, never merge. (iii) do NOT reduce F' to a
  scalar/aggregate summary (refuted R3–R4/R7/R9); the loaded IH must read g=N_{F'}'s
  staircase shape. (iv) the near-balance shell in step 2 is where dominance is load-bearing
  — enumerate it, do not wave it through with (DIFF).

---

allocation-vertex-corner: new
Target: GAP L (lower bound) for all n — D̃(F)≥1 for every feasible dyadic refinement F;
  with certified UB this closes c(n)=2^n/(2^{n+1}−1). (Same whole claim, different route.)
Technique: certified FLOOR reduction + a NON-RECURSIVE finite classification of the
  discrete allocation space a=(a_0,…,a_n), Σa_j≤n, via the extremal/vertex principle
  (certified Lemma V: ≤n+1 distinct values at a minimizing cell-vertex). This is
  genuinely far from the leader: no induction on n, no fixed comparison object — it
  bounds I_n over each allocation cell and prunes the tie set to a low-dimensional CORNER
  of a-space (a_0 large / b:=Σ_{j≥1}a_j small), which the explorer's numerics pin exactly
  (tie reached only at a=(3,0,0,0,0),(4,0,0,0,0),(1,2,0,0,0); a=(0,4,0,0,0) is far at
  I_n≈−5). Operates on the ALLOCATION, not a static profile of the final multiset, so it
  is NOT the R8-dead measure/merged-order/sequential/genfn family, and NOT the R10-dead
  GAP-IMR integer-minimizer engine (Lemma V is used to bound a corner, not to claim an
  integer minimizer).
Skeleton:
  1. Import FLOOR: GAP L ⟺ I_n≤0. For each fixed allocation a, sup over positions of I_n
     equals (1−inf_positions D̃)/2, and inf D̃ is attained at a cell-vertex with ≤n+1
     distinct values (Lemma V, lemmas/odd-block-vertex.md). So sup_a I_n is a finite max
     over vertices. — certified.
  2. **Allocation-monotone bound (KEY GAP).** sup_positions I_n(a) ≤ φ(b), with φ
     non-increasing in b=Σ_{j≥1}a_j and φ(b)<0 for b≥1 (only b=0 can reach the tie).
     Mechanism: moving one unit of budget from π_0 into F' adds a −1 step to M below the
     new fragment's scale; via the LAYER form
     I_n=Σ_k(λ{M≥2k}−λ{M≤−(2k−1)}), the extra fragment strictly increases the odd-threshold
     negative side more than the even-threshold positive side (the even-vs-odd asymmetry
     that is the arithmetic source of the missing ½). — GAP: prove φ exists and is monotone.
  3. Base corner b=0: identical fixed-object target D̃(π_0⊎L)≥1 (shared with the leader —
     import as a lemma once certified there). — GAP (shared).
  4. Small finite corner b∈{1,…,b*}: with a_0 large, finitely many vertex classes; settle
     each by dominance + Lemma V vertex enumeration. — GAP (finite, explicit).
  5. Combine 2+3+4 ⇒ I_n≤0 for every allocation a ⇒ GAP L ⇒ c(n).
Key lemmas (claim + mechanism):
  - **Vertex-finiteness of the allocation optimum** (Lemma V, certified): for fixed a,
    sup_positions I_n is attained at a ≤(n+1)-distinct-value cell-vertex — an LP
    active-constraint count. Makes the per-cell optimization a finite check.
  - **Allocation-monotone φ(b)** sup I_n(a) decreases as budget leaves the top scale —
    because each below-top cut converts an even-threshold contribution into an
    odd-threshold one in (LAYER), and the odd side is the larger. This is the crux: it
    reduces the continuum problem to the finite corner {a_0 large, b small}.
Open gaps: step 2 (allocation-monotone φ — the engine of the pruning), step 3 (ladder
  base, shared), step 4 (finite corner b=1,2).
Cases to cover: partition of a-space by b; base b=0; finite corner small b; all large-b
  cells killed by φ. Enumerate the corner explicitly (explorer: only a_0-heavy a reach 0).
Watch out for: (i) the CLAUDE.md rule "no scalar-summary-of-Z fill" — φ(b) is a summary of
  the ALLOCATION, permissible ONLY if the corner is then verified case-by-case against the
  TRUE recursive shape (Lemma V vertices), NOT asserted from the count alone. (ii) do NOT
  slide into the GAP-IMR integer-minimizer claim (dead R10) — Lemma V here bounds a corner,
  it does NOT assert an integer minimizer. (iii) cross-k cancellation at near-tightness is
  multi-k, not per-k (loaded-IH explorer Route C witness a=(1,2,0,0,0): pos[1] balanced by
  neg[1]+neg[2]) — φ's derivation must survive cross-k, do not assume a single-k pairing.

---

induction-recursion-telescope: advance (PARKED — no builder this round)
Target: GAP L (machinery reference only).
Note: leader/machinery home; owns (△)/(△⋆)/(△△)/(⊞) but those give only D̃≥0 (off by ½,
  proven equivalent to target R8). Keep live as the certified cross-check for the two
  active approaches' identities; do NOT dispatch a builder. Its (△⋆) localization is the
  measure-form cross-check of the leader's FLOOR/LAYER work.

Build set: peel-scale-rank-induction, allocation-vertex-corner
