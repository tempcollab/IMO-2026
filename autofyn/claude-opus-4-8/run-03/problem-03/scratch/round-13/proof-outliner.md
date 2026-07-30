## imo-2026-03

Two shared walls, one live vehicle each (no double-up per wall — single-gap trap, per role memory r11).
Both are `advance`: the reductions are certified; I re-plan the SINGLE open gap in each with a
concrete extremal/telescope skeleton using this round's explorer levers. f-partition-majorization
stays HELD (GAP B-MONO localisation still unrepaired — do not build).

---

merge-interleave-pattern: advance
Target: for every n, Liu's guaranteed share is c(n)=2^n/(2^{n+1}−1), i.e. minimax D = u_n. This slug
  owns the LOWER bound (Liu plays C_n ⇒ every ≤n-cut refinement has D ≥ 1), reduced (certified
  VERT-LOW+BLK+ATT) to GAP-EXTR; the upper bound is imported from breakpoint-vertex's §4B for the
  end-to-end claim.
Technique: minimal-counterexample over the FINITE vertex family + a vertex-restricted dyadic PEEL
  driven by BLK's box-face dichotomy (Fundamental Thm of LP already spent; now pure extremal
  induction on the block-structured vertex, NOT the continuum MID/ONE-REC route that stalled r7–r11).
  Spine = strong induction on n with a per-scale peel; the aimo-0333 exchange move is the fallback
  mechanism for the generic case.

Skeleton:
  1. Block-parity reduction of the objective (near-proven, promote to Lemma). At a vertex v of P_T
     partition the m coordinates into p ≤ n+3 equal-value blocks (BLK). An even-length block is a
     union of Lemma-P cancelling pairs at consecutive odd/even positions ⇒ contributes 0 to L_T; an
     odd-length block flips the running-position parity. Hence
        L_T(v) = w_1 − w_2 + w_3 − w_4 + … ,
     where w_1 > w_2 > … > w_q are the DISTINCT values of the ODD-length blocks in descending order,
     signs alternating starting +. — by Lemma P (cancelling-pair, certified) + a one-line
     running-parity induction. So GAP-EXTR ⟺ this alternating sum of odd-multiplicity values ≥ 1.
  2. Minimal counterexample. Suppose GAP-EXTR fails; take n minimal, then (finite family) a vertex
     v* of some P_T with L_T(v*) < 1. By step 1 and n minimal, every strictly-smaller-n vertex has
     alternating value ≥ 1.
  3. Box-face dichotomy (BLK: the box supplies ≤ 2 active constraints — top v=2^{n-1}, bottom v=0).
     Case (a-bottom): some coordinate = 0. Delete it — it contributes 0 to L_T and 0 to every group
     sum — yielding a vertex of a polytope of the SAME n but strictly fewer pieces; iterate to a
     positive-coordinate vertex, so WLOG no zero coordinate. [reduction, low risk]
     Case (a-top): some coordinate = 2^{n-1}. This is a full top-scale fragment. Peel it together
     with its dyadic partner using the certified top-band decomposition (Lemma TB): removing the
     pinned top block drops L_T by an INTEGER (a cancelling pair removes 0; an unpaired top value
     removes exactly 2^{n-1} ≥ 1) and leaves a vertex of the P_{T'} for a strictly smaller ladder
     C_{n−1} (group sums Σgroup_j=2^j for j<n−1 are untouched; the top group re-normalises). Apply
     the induction hypothesis (n minimal) to the residual vertex ⇒ residual alternating value ≥ 1 ⇒
     L_T(v*) ≥ 1, contradiction. [THIS peel-and-recurse is the main GAP — see Key lemmas]
  4. Generic case (b): no box face active, so rank is saturated by the (E) group-sum equalities
     plus ties alone ⇒ p = n+1 distinct blocks, one degree of freedom per group. Characterize:
     each block value is pinned by the superincreasing ladder (2^j > Σ_{i<j}2^i) to a sub-sum of the
     dyadic scales, forcing the canonical "one fragment per dyadic level, tail uncut" layout (the ATT
     family and its word-permutations). For that shape the alternating sum telescopes: consecutive
     dyadic scales pair off as cancelling pairs, leaving the residual unit ⇒ L_T = 1 exactly,
     contradicting L_T(v*) < 1. [second GAP — the characterization]
  5. Cases (a) and (b) exhaust vertices (BLK gives ≤ 2 box faces; either ≥1 is active → (a), or none
     → (b)). Both contradict L_T(v*) < 1 ⇒ no counterexample ⇒ GAP-EXTR holds for all n ⇒ D ≥ 1 ⇒
     lower bound c(n) ≥ 2^n/(2^{n+1}−1). Combined with the imported upper bound and ATT tightness,
     minimax D = u_n exactly.

Key lemmas (claim + mechanism):
  - Block-parity objective: L_T(v) = alternating sum of the odd-multiplicity distinct values,
    descending, starting +. — because even-length equal-value blocks are Lemma-P cancelling pairs
    (net 0) and each odd-length block toggles the running-position parity, so the surviving signs
    alternate. (This collapses L_T to exactly the μ{g odd} content but on a FINITE block object — it
    is the vertex-native restatement, provable now, and should be certified separately.)
  - Vertex-peel (the load-bearing GAP): a top-box-active coordinate v_i = 2^{n-1} can be removed with
    its group so that the remaining coordinates form a vertex of the (n−1)-ladder polytope P_{T'} and
    L_T = L_{T'} + δ with δ ∈ {0} ∪ [2^{n-1}, ·]. — because TB (certified) splits D = e + D_low at the
    threshold 2^{n-1} and, on a vertex, the pinned top block is either a cancelling pair (δ=0, drops a
    +/− pair) or an unpaired top value (δ = its own value ≥ 2^{n-1}); the residual coordinates still
    satisfy the lower-scale group-sum equalities, so they form a genuine smaller-n vertex. The precise
    budget/type re-indexing (that P_{T'} is a valid MID-core type at n−1) is what the builder must nail.
  - Generic-vertex characterization (second GAP): every box-free (p=n+1) vertex is a canonical
    one-fragment-per-dyadic-scale layout. — because with no box face the only active constraints are
    the n+1 group-sum equalities + ties; the superincreasing property 2^j > Σ_{i<j}2^i forbids a block
    from straddling two dyadic groups (two coincident cross-group values would over/under-shoot a group
    sum), pinning one free value per group; the sorted result is the ATT ladder ⇒ telescopes to 1.

Open gaps:
  - GAP-EXTR-PEEL (step 3, top-box case): the vertex-restricted PEEL-and-recurse — that removing a
    2^{n-1}-pinned block yields a valid smaller-n MID-core vertex with L dropping by an integer ≥ 0.
    This is the main content; builder must verify the type re-indexing and budget accounting exactly.
  - GAP-EXTR-GEN (step 4): the generic (box-free) vertex characterization + its telescoping =1. Should
    be machine-checked at n=5 FIRST (explorer conjecture: worst vertices at n=3,4 are exactly ATL
    permutations) before prose — per numeric-gate rule.
  - Optional parallel probe (concrete, untried per explorer opening 4): extract the LP dual
    (active-constraint multipliers) at the n=3,4 worst vertices, look for a closed-form pattern
    (inverse-dyadic-weight multipliers), and try to write down an explicit dual-feasible certificate
    λ with Σλ·(constraint) ≤ L_T − 1 identically for general n. A valid dual point would close
    GAP-EXTR outright without the induction; a cheap computational check the builder can run.
Cases to cover: box-bottom (delete-zero), box-top (peel-and-recurse), box-free generic (characterize
  + telescope). BLK guarantees these three exhaust all vertices.
Watch out for:
  - Do NOT reintroduce ONE-REC as a binding facet (refuted r12: implied by (E)+positivity).
  - Do NOT use the integrality shortcut (132 non-integer vertices at n=3, all D>1) or "D constant
    across words" (Case (a) gives D=2^{n-1}).
  - The critical band has margin →0 as f_1→2^{n-1}; the peel's δ must be tracked exactly (a crude
    δ≥0 that loses the "−1" is fatal, exactly as the crude D(S')≤max bound failed before).
  - A single LOCAL exchange giving a scalar inequality in isolation is warned-against (r10/r11 lower
    levers died that way); the peel must be a GLOBAL vertex→smaller-vertex reduction (which it is).

---

breakpoint-vertex: advance
Target: for every n, minimax D = u_n = 1/(2^{n+1}−1), i.e. c(n)=2^n/(2^{n+1}−1). This slug owns the
  UPPER bound (Xiang forces D ≤ u_n on any profile), reduced (certified FGR + R-COV' sufficiency) in
  the balanced valley to the first-gap pigeonhole μ_{n+1} = min_{1≤i≤n+1} dist(a_i, R_{i−1}) ≤ u_n L.
  The lower bound is imported from merge-interleave for the end-to-end claim.
Technique: seeded/generalized strong induction on a residual "seed" r (a discrepancy/telescope on the
  distance sequence that spends Σa_i = L and BOTH caps a_1<L/2, a_2<β_n L jointly), NOT a
  covering-radius/max-gap bound (whole family exhausted r10+r12) and NOT a fixed greedy recursion
  (refuted r9, ≤11.4×). The induction invokes the FULL upper-bound theorem EXISTENTIALLY on a strictly
  smaller instance (Lemma VS forces ≥2 moves before IH), which is what distinguishes it from every
  dead deterministic rule.

Skeleton:
  1. Land a first residual (imported). By certified Lemma BL there is a subset T={a_1,…,a_k} with
     r_1 := |a_1 − Σ_{i∈T∖1} a_i| ∈ [0, β_n L), realized by ESF-1 in k moves. β_n L = 2^{n−1} u_n L —
     a factor 2^{n−1} too big; the residual must be refined down.
  2. Generalized seed statement (the induction target). SEED(p): given a seed value r ≥ 0 and pieces
     b_1 ≥ … ≥ b_p (a sub-instance carved from the valley, mass M = r + Σb_j, budget p cuts), with the
     seed-domination hypothesis r ≤ b_1 and the valley caps inherited, the descending include/skip
     process starting from r reaches a positive value ≤ u_p · M within p moves. Base p=0: r itself,
     and the tight dyadic profile forces r = u_0·M with equality (sanity: the mechanism must be tight,
     no +ε slack — explorer note).
  3. Inductive step (existential, ≥2 moves before IH — the GAP). From seed r and remaining pieces,
     pick (adaptively, NOT a fixed rule) two pieces b_i, b_j to MATCH/fold so the new residual
     r' = ||r − b_i| − b_j| (or the appropriate 2-move fold) satisfies r' ≤ (u_{p−2}/u_p·-scaled)
     threshold AND the sub-instance {r', remaining p−2 pieces} still satisfies the seed-domination
     hypothesis; invoke SEED(p−2) existentially on it. The factor-2-per-level contraction of the
     dyadic extremizer (explorer opening 3: the fold map v↦|v−a| is the slow/subtractive Euclidean
     step, tight at the all-2× ladder) is what makes the arithmetic balance.
  4. Telescope closure via Σa_i = L (the discrepancy engine). Show the seed threshold at each level is
     enforced by the running mass budget: if NO admissible 2-move fold met the threshold at some
     level, the untouched pieces would have to be mutually "far" (each dist(a_i,R_{i−1}) > u_n L),
     which — summed against Σa_i = L and the caps a_1<L/2, a_2<β_n L — forces Σa_i > L, contradiction.
     This is the telescope, NOT a packing/covering-radius count: it charges each far piece against the
     total mass L directly, so it sees the min-distance (first gap) and never the max gap.
  5. Chain steps 1–4: r_1 ∈ [0, β_n L) seeds SEED at level ≈ n−1; the induction drives it to ≤ u_n L
     within the remaining budget ⇒ μ_{n+1} ≤ u_n L ⇒ (R-COV', certified) the upper bound in the valley
     ⇒ combined with the imported dominant case a_1 ≥ L/2 (certified whole-tail-peel), D ≤ u_n for all
     profiles. With the imported lower bound, minimax D = u_n exactly.

Key lemmas (claim + mechanism):
  - SEED(p) generalized induction (load-bearing GAP): reachable-from-seed-r value ≤ u_p·M in p moves.
    — because folding a piece against the seed contracts the residual toward 0 and the dyadic ladder
    is the unique slowest (factor-2/continued-fraction) extremizer, so u_p is exactly the worst
    contraction rate; the existential IH (some good 2-move fold exists) sidesteps the refuted fixed
    greedy rules. The RIGHT seed threshold + mass scaling is the open technical core (12 rounds of
    induction attempts failed on exactly this parametrization — must be pinned by machine check first).
  - Mass-telescope discrepancy (step 4): ¬(some dist(a_i,R_{i−1}) ≤ u_n L) ⇒ Σa_i > L. — because a
    piece far (> u_n L) from the whole prior reachable set {0}∪R_{i−1} contributes a definite mass
    increment that cannot be "reused"; summing the increments against the caps overshoots L. This is
    the genuinely-new lever distinct from covering radius: it bounds the FIRST gap via the SUM, not
    the max gap via packing.
  - (Alternative fill for the same GAP, if SEED scaling resists) restricted-density lemma for
    difference-trees (explorer opening 2): near 0 specifically, the local density of tree-realizable
    values on [0,a_1] is ≥ (2^{n+1}−1)/a_1, using ALL small a_i (i≥3) as binary-refinement digits —
    NOT the global multiset count (refuted r11). Kept as a same-slug backup mechanism, not a new slug.

Open gaps:
  - GAP-SEED (steps 2–3): the exact generalized statement — seed threshold, mass scaling M, and the
    seed-domination invariant that makes SEED(p−2) a legal IH instance. MUST be exact-fraction
    machine-checked on hundreds of valley profiles per n=2..7 BEFORE prose (numeric-gate rule; r9–r12
    each killed a bad recursion in one round this way). Verify the budget arithmetic (k moves for BL +
    2 per level ≤ n total) balances.
  - GAP-TELE (step 4): the mass-telescope inequality Σ(far increments) > L. Cheap to state; the exact
    charging constant against the two caps is the content.
Cases to cover: dominant a_1 ≥ L/2 (imported, closed); balanced valley (steps 1–5). The valley is the
  ONLY residual (Lemma VS pins the boundary at a_1<L/2, a_2<β_n L exactly).
Watch out for:
  - NOT a covering-radius / max-gap bound (one-cap r10, two-cap r12, windowed, exact-point — ALL dead,
    saturate 3–5·u_n). The telescope must charge against Σa_i=L, never against max consecutive gap.
  - NOT a fixed deterministic recursion (greedy band-landing / flip-if-helps / drop-one refuted r9,
    ≤11.4×; the n=2 witness A={9/20,7/25,27/100} needs the abs-flip subset {a_2,a_3}). The IH must be
    EXISTENTIAL (some fold exists), consuming ≥2 moves (Lemma VS).
  - NOT set-count/density pigeonhole on R_{n+1} (r11: |R_{n+1}|=2 on all-equal profile; multiset-gap
    does not convert to value). The density backup must be LOCAL near 0 using the small a_i as digits,
    not a global count.
  - The mechanism must be TIGHT at the dyadic ladder a_i=2^{n+1-i}/(2^{n+1}−1) (equality μ_{n+1}=u_n),
    so any "generic +ε slack" argument is automatically wrong — the extremizer has zero slack.

---

f-partition-majorization: HELD (do not build)
Reason: GAP B-MONO (min_B D(F,B) ≥ 1 per fixed F) still risks being MID-core restated unless the
  exchange step localises the minimising B to one aligned config; c_B=0 is NOT WLOG (42.8% of B-cuts
  strictly lower D at n=5, explorer-proven r12). Its single-gap localisation was the refuted premise;
  it is not repaired this round. Keep in the population, do not put in the build set.
