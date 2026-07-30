## imo-2026-03

Context for the reviewer. The UPPER BOUND is fully proven & certified (`lemmas/upper-bound.md`) for
all n — untouched here. The ONLY open wall is GAP L (lower bound, Case B), certified-reduced to a
single non-strict combinatorial inequality with three equivalent forms:
- (△⋆): `λ_{(0,θ)}{M odd} ≥ ∫_{(0,θ)}M = 1−β`, M=N_Y−N_Z, total mass ≤1;
- (♠≥0): `Σ_{z∈Z odd-pos} z ≥ Σ_{y∈Y even-pos} y`;
- self-contained §9: `E(F) ≤ 2^n−1` for F=⊎_{j=0}^n π_j any simultaneous refinement of {1,…,2^n}
  with split-budget Σa_j ≤ n. Equality ATTAINED (tie configs) — target is NON-STRICT.
REFUTED / do-not-seed: scalar/aggregate summary of Z; local 1-1 value/width injection {Y even}→{Z odd};
top-down/top-anchor reserve of Z; global budget-count (O_B≥E_A termwise); the "cut can't push D̃ below
min signed-sum of ORIGINAL Liu pieces" dual. Compensation is GLOBAL and bottom-inclusive.

Probe this round (grounds the field): on the tight witnesses W1 (n=5, D=8.8, maxc=2) and W2
(n=4 tie, D=1, maxc=3), a left→right greedy nonneg-block tiling of the merged list DOES cover the
whole list — the T-run deficit at c≥2 is repaid by the LOW tail where Z's small parts drive c very
negative. On a slack case W3 (D=2.345) the surplus precedes the deficit, so one-directional greedy
fails there. Direction caveat is real; block-tiling exists but needs a two-sided / budget-bounded
window. This pins the hard step for approach A.

Field: 3 to build (A advance, B new, C new) + 1 retirement (induction-recursion). The three build
approaches are FAR APART in framing: merged-order block-decomposition (A) vs ordered-cut amortized
monovariant (B) vs static-partition double-count/generating-function with no measure language (C).

---

induction-recursion-telescope: advance
Target: c(n)=2^n/(2^{n+1}−1); specifically close GAP L (Case B lower bound) ⇒ D*=u ⇒ whole problem.
Technique: merged-order signed-sum machinery (its own certified (♦)/(♠)/(△⋆)/Structure Lemma) +
  NEW concrete mechanism — greedy bounded-window NONNEGATIVE-BLOCK TILING (crux aimo-0626), a
  many-to-one net-block domination (explicitly NOT the refuted 1-1 injection §10).
Skeleton:
  1. Import (♦): `D̃−1 = Σ_i ψ(c_i)Δw_i`, ψ(c)=1[c odd]−c, ψ(c)≥0 ⇔ c≤1, ψ(c)<0 ⇔ c≥2, Δw_i≥0
     — CERTIFIED (§3, this file).
  2. Goal Σ_i ψ(c_i)Δw_i ≥ 0. Partition the merged index set {1..m} into consecutive blocks
     B_1,…,B_r (a tiling), each with block-sum Σ_{i∈B_t} ψ(c_i)Δw_i ≥ 0; sum ⇒ done — by additivity.
  3. Tiling rule: each block is anchored at a maximal T-run (indices with c_i≥2, the ONLY negative
     terms) and EXTENDED to include the adjacent surplus mass (c_i≤0 intervals) needed to cover its
     deficit — extended to BOTH sides (the probe shows the surplus may sit above OR below the run in
     value) within a window whose length is a priori bounded by the local cut-budget — by the tiling
     construction + Structure Lemma budget accounting.
  4. Block-sum nonnegativity: within each block the T-run deficit Σ_{c_i≥2}(c_i−1[c_i odd])Δw_i is
     ≤ the enclosed anchor surplus Σ_{c_i≤0}(1[c_i odd]−c_i)Δw_i — by a NET (summed) comparison over
     the block, never a per-part injection (so §10's refutation does not apply).
Key lemmas (claim + mechanism):
  - Budget-bounded window: a T-run reaching c=k≥2 costs k−1 net extra T-tokens (fragments) above a
    perfect alternation, and Σ_j a_j ≤ n caps the TOTAL extra tokens — because a prefix with c_i=k
    forced k−1 more Y-fragments than Z-parts above height w_i, and every extra fragment beyond the
    zigzag skeleton consumes one unit of the Σa_j≤n split budget (Structure Lemma §5). So there are
    only ≤n excursion-tokens total; each bad block is finite and budget-charged.
  - Net-block domination (the crux, survives §10): a length-Δ T-run at value ≈v is repaid by Z-odd
    mass from SEVERAL dyadic scales SUMMED (witness §10: Y_even=14.1 repaid by ΣZ_odd=18 across three
    scales) — a block-sum inequality, exactly the object that survived the injection counterexample.
Open gaps: Steps 3–4 — proving a valid nonneg-block tiling ALWAYS exists (two-sided window, budget
  bound). This is the ONE hard step. The (♦)/(♠)/(△⋆)/Structure/Termwise machinery it builds on is
  all certified.
Cases to cover: maxc≤1 already closed (Lemma T, certified); only maxc≥2 remains — this is exactly the
  set of configs that HAVE a T-run to anchor a bad block, so the tiling is only needed there.
Watch out for: the direction trap (probe W3) — a one-directional left→right greedy is INSUFFICIENT;
  the window must reach surplus on either side. Do NOT regress to a 1-1 value/width injection (§10
  dead). Do NOT summarize Z by a scalar. Keep the domination a NET block-sum.

---

cut-sequence-potential: new
Target: c(n)=2^n/(2^{n+1}−1); close GAP L by showing D̃(F)≥1 for every ≤n-cut Case-B response.
Technique: amortized/sequential POTENTIAL over Xiang's ORDERED cut sequence (crux aimo-0019 frontier
  potential), using the EXACT Cut-Flip toggle-set geometry (certified `lemmas/cut-flip.md`) — a
  monovariant over cut MOVES, structurally orthogonal to the fragment-origin recursion and to the
  merged-order measure of A.
Skeleton:
  1. Order Xiang's cuts as a sequence of ≤n single-part splits, F_0={1,…,2^n} → F_1 → … → F_k=F
     (process in decreasing order of the part cut, for the proof). — by Structure Lemma / any fixed
     processing order.
  2. Base: D̃(F_0)=Σ(−1)^{i−1}2^{n−i}=(2^{n+1}+(−1)^n)/3 ≥ 1 for all n (exact geometric alt-sum,
     e.g. n=2:{4,2,1}⇒3, n=3:{8,4,2,1}⇒5) — by direct computation. Start is well ABOVE 1.
  3. Per-cut effect: cutting a part of length L into (x,L−x) toggles level-parity EXACTLY on
     [0,x)∪[L−x,L), so ΔD̃ = ±2·(exact toggled measure), |ΔD̃| ≤ 2min(x,L−x) — CERTIFIED (Cut-Flip).
  4. Define a reserve r_k = r(F_k, remaining budget n−k) with r_0 = D̃(F_0)−1 and r_k = 0 at the tie
     extremum, such that Φ_k := D̃(F_k) − 1 − r_k satisfies ΔΦ ≥ 0 at every cut; then
     Φ_final = D̃(F)−1 ≥ Φ_0 = 0. — by the amortized charging invariant.
Key lemmas (claim + mechanism):
  - Amortized reserve (the crux): each cut's DROP in D̃ is charged against reserve RELEASED by that
    same cut — because a cut of a part of length L can lower D̃ by at most the width it toggles, and
    that toggle sits inside [0,x)∪[L−x,L) whose measure is repaid by the reserve r attached to the
    part's size and the ≤ (remaining budget) future cuts it enables — the aimo-0019 "charge each
    frontier advance against the pieces it absorbs" shape, adapted to the exact toggle set (not just
    its measure bound, which alone is too weak — see risk).
Open gaps: Step 4 — CONSTRUCTING the reserve r_k. This is the ONE hard step and the whole content.
Cases to cover: none beyond the single monovariant, IF the reserve is right; the tie extremum must
  give equality (r drives to 0 exactly), matching the non-strict target.
Watch out for: RISK of collapse to the refuted global budget-count — a crude Σ|ΔD̃| ≤ 2Σmin(x,L−x)
  bound is INSUFFICIENT (D̃ can legitimately fall all the way to 1, a decrease of D̃(F_0)−1). The
  reserve MUST be repaid cut-by-cut using the EXACT toggle-set geometry, not a summed magnitude bound.
  If after one build the reserve cannot be made monovariant, this collapses to budget-count (dead) and
  should be RETHOUGHT — flag early.

---

even-rank-doublecount: new
Target: c(n)=2^n/(2^{n+1}−1); close GAP L via the self-contained restatement E(F)≤2^n−1.
Technique: PURE combinatorial double-counting / generating-function on partitions of powers of two
  under a shared split budget — NO game, NO cutting, NO merged-order MEASURE language. Genuinely
  fresh framing (bypass opening 4; crux aimo-0155 roots-of-unity / aimo-0509 genfn as tools).
Skeleton:
  1. State the self-contained claim (§9, certified equivalent to GAP L): for F=⊎_{j=0}^n π_j, π_j a
     partition of 2^{n−j} into a_j+1 parts, Σa_j ≤ n, the even-rank sum E(F) ≤ 2^n−1 (⇔ O(F)≥2^n).
     — by §9 equivalence (certified).
  2. Encode each part by (value, dyadic-scale j) and build a bivariate/scale-graded generating object
     tracking rank-parity contribution per scale: how much mass of scale 2^{n−j} can land at EVEN
     merged rank. — by a counting identity per scale.
  3. Bound the even-rank mass contributed by each scale: scale j can push at most (its part-count −1)
     worth of "displacement" into even ranks, and Σ_j (part-count −1) = Σ_j a_j ≤ n caps total
     displacement; convert to E(F) ≤ 2^n−1. — by a scale-by-scale double count.
Key lemmas (claim + mechanism):
  - Scale-graded even-rank bound (the crux): the excess of E(F) over the "perfect zigzag" value
    2^n−1 is a sum over scales of a per-scale defect controlled by a_j, and Σa_j≤n forces the total
    ≤0 — because inserting one extra fragment at scale j shifts the parity-role of exactly the parts
    below it, a displacement paid for by one budget unit; the roots-of-unity filter at x=−1 recovers
    O−E=D̃ and a SECOND grading variable q marking scale j lets the target read as a coefficient/
    evaluated inequality in q (probe n≤3 first — cheap-kill).
Open gaps: Steps 2–3 — the scale-graded identity and its bound. ONE hard step: making the per-scale
  double-count exact (or the two-variable genfn inequality). The equivalence Step 1 is certified.
Cases to cover: uncut scale (a_j=0, top piece) gives its part at odd rank 1 — recovers C3/Case A
  free; the budget Σa_j≤n uniformly covers Cases A and B.
Watch out for: the "(♣) is not pointwise" wall (1[M odd]≤M fails pointwise, only after integration) —
  a naive single-variable coefficient argument will hit it; the SECOND (scale) grading must be
  genuinely used. CHEAP-KILL first: hand/sympy-compute the n=2 and n=3 bivariate genfn on the worked
  examples (§4,§6); if no clean identity in ~30 min, downgrade this slug — it is the most speculative.
  Do NOT reintroduce a scalar summary of Z (refuted) — the scale grading must keep each scale's parts.

---

induction-recursion: RETIRE (do not build)
Reason: budget-count route (O_B ≥ E_A, i.e. termwise |A_2j|≤|B_{2j−1}|) is REFUTED with an explicit
  witness (round 7); the builder itself escalated for a different framing. Its sequential intent is
  now carried, in a genuinely different (amortized, exact-toggle) form, by the NEW cut-sequence-potential
  slug. Keep the file as a recorded dead end; do not dispatch a builder. If cut-sequence-potential's
  reserve also collapses to budget-count, that confirms the whole sequential-count family is dead and
  the field should lean on A (tiling) and C (double-count).

---

Build set: induction-recursion-telescope, cut-sequence-potential, even-rank-doublecount
