## imo-2026-03

Round-4 field. Situation is settled and must NOT be re-derived: answer `c(n)=2^n/(2^{n+1}−1)`,
reduction `c(n)=(1+D*)/2` with `D*=u_n=1/(2^{n+1}−1)`, and the certified spine (Lemma G,
level-measure identity `D=λ{t:N(t) odd}`, Cut-Flip, Invisible-Pair, removal-ops + Residual-Total
Theorem, threshold block-decomposition `(★)`, `(★★)`, half-total single-crosser `(◇◇)`) are all
PROVEN and importable. n=1,2 fully solved. Exactly two walls remain, one per live approach, each
reduced to a precise residual sub-case. The orthogonal explorer confirmed NO genuinely different
top-level framing exists (scale-invariance ≡ induction-recursion's recursion; surrogate-adversary ≡
dyadic-discrepancy's RT; 2-adic recast is circular/unconstructed). So I do NOT open a cosmetic third
framing. I put up **two pairs of twins**: each wall gets two builders installing two *distinct*
mechanisms, so a shared-gap plateau cannot collapse either wall to one idea.

---

### Wall GAP U (upper bound) — reduced to RT Case (iii), the balanced regime `max(ℓ₁,2ℓ₂)<c(k)Σ`

Proven dead here (do NOT retry): greedy "remove-max-total"/black-box single-move+RT(k−1)
(telescopes to `2/((k+1)(k+2))>u_k` for k≥3); amortized-halving `W=2^{-#cuts}` standalone (off by
~2×); naive directional-monotonicity/compactness (f is jagged, non-monotone, Finding 3).

---

dyadic-discrepancy: revise
Target: For every n and every Liu partition of 1 into ≤n+1 pieces, Xiang with ≤n cuts forces
  D ≤ u_n — i.e. the full upper bound `c(n) ≤ 2^n/(2^{n+1}−1)` (whole problem's upper half).
Technique: Residual-Total induction (RT), closing the sole open Case (iii) by a **disjunctive
  reserve-buffer invariant** (aimo-0340 template) that replaces the fragile single inequality.
Skeleton:
  1. Import certified spine: RT reduction, Cases (i) dominant + (ii) balanced-top proven for all n
     (one removal op + RT(k−1)). — done, `dyadic-discrepancy.md §4.5`.
  2. In Case (iii) all pieces are small: ℓ₁<c(k)Σ and every ℓ_i<c(k)Σ/2. Observe the residual after
     ANY removal op is itself balanced (new top piece ≤ ½·max(ℓ₁,2ℓ₂)) — this post-move
     sub-extremality is the slack RT(k−1) fails to credit. — by the op bounds already in §4.5.
  3. Strengthen the IH from the single clause "residual ≤ u_kΣ" to a **two-clause disjunctive
     invariant** carried across the induction:
       (a) residual total ≤ u_kΣ;  OR
       (b) residual ≤ u_{k−1}Σ′ AND a *reserve* of ≥1 further untouched piece all < Σ′/2 survives,
     chosen so the exact balanced transition where (a) is about to fail is caught by (b)'s reserve.
     — by adapting aimo-0340's disjunctive-invariant-with-reserve crux.
  4. Show one balanced removal op preserves the disjunction and, on the branch where (a) would break,
     the reserve piece guarantees a second bite whose combined effect beats u_k. — by (★★)-style
     bookkeeping + the recursion factor u_k/u_{k−1}=1/(2+u_{k−1}).
  5. Close: the disjunction at k=0 collapses to residual ≤ u_0Σ=Σ; unwind to D ≤ u_n. — by
     strong induction on k.
Key lemmas (claim + mechanism):
  - Post-move balance: after a removal op in Case (iii), the new multiset is balanced relative to its
    own total — because a pin/bisect on small pieces produces a new max ≤ ℓ₂ ≤ ½·max(ℓ₁,2ℓ₂) < ½c(k)Σ,
    so RT(k−1) is applied to a strictly sub-extremal instance and yields < u_{k−1}·(new total).
  - Reserve invariant: the disjunction (a)∨(b) is self-restoring under one op — because whenever
    clause (a)'s margin u_kΣ−residual is about to go negative, the balanced regime guarantees a
    reserve piece < Σ′/2 exists (there are k+1 pieces, none dominant), which clause (b) tracks and
    which absorbs exactly that transition; this is aimo-0340's mechanism transplanted (a cut-budget
    process where a single survival inequality breaks at one transition, fixed by a two-clause
    invariant carrying a reserve).
  - Slack sufficiency (fallback within this slug): a NON-tight bound suffices — Case (iii) interior
    has ≥12–28% slack (Finding 2), so the reserve need only recover an O(δ_k) deficit, not match u_k
    exactly; if the exact disjunction resists, prove instead "two chained ops beat u_k by a constant
    factor when ℓ₁<c(k)Σ."
Open gaps: Step 3–4 — deriving the *exact* second clause (b) and its reserve, and verifying the
  self-restoring transition, is the research step. Steps 1,2,5 are bookkeeping / already certified.
Cases to cover: only Case (iii) (n≥3); (i),(ii),n≤2 already proven. Sub-split step 4 on whether the
  op is a pin (ℓ₁>ℓ₂) or a free-delete (ℓ₁=ℓ₂).
Watch out for: (a) do NOT let the invariant degrade to plain greedy — the reserve clause must
  actively carry extra structure, or it telescopes to 2/((k+1)(k+2)) and fails at k=3; (b) the
  recursion factor is 1/(2+u_{k−1}), NOT exactly ½ — using ½ overshoots by ~2× (Finding 4); (c)
  verify the disjunction holds with EQUALITY on the dyadic boundary (it must, since dyadic is tight).

---

dyadic-discrepancy-euclid: copy-of dyadic-discrepancy
Target: Same whole-problem upper half — for every n, Xiang forces D ≤ u_n — via an explicit
  deterministic Xiang schedule instead of a strengthened IH.
Technique: **Chained-pin / Euclidean-subtraction schedule** (Finding 1) — a concrete canonical
  op-sequence proven to reach residual total ≤ u_kΣ in Case (iii), a constructive dual to the
  reserve-invariant twin.
Skeleton:
  1. Import RT reduction + Cases (i),(ii) (certified). Only Case (iii) remains.
  2. Define the canonical schedule S: **repeatedly pin the current LARGEST piece against the current
     SMALLEST available piece** (generalized-pin `ℓ_max → {ℓ_min, ℓ_max−ℓ_min}`, delete the equal
     pair), a "greedy-Euclidean" rule — NOT the refuted max-total greedy. Each pin removes only
     2ℓ_min from the total but transforms ℓ_max ↦ ℓ_max−ℓ_min ("long division" on the top piece).
  3. Track the running total r_j and top piece under S; show the top piece decays like a
     continued-fraction remainder while the total sheds 2ℓ_min per step. — by an explicit recurrence
     on (r_j, top_j).
  4. Prove: after ≤k pins under S, r_k ≤ u_kΣ whenever max(ℓ₁,2ℓ₂)<c(k)Σ. — by bounding the
     Euclidean remainder chain against the dyadic worst case.
  5. Conclude D ≤ residual ≤ u_n (RT).
Key lemmas (claim + mechanism):
  - Euclidean decay: pinning ℓ_max against ℓ_min keeps the residual multiset balanced AND drives the
    top fragment down by ℓ_min each step — because ℓ_max−ℓ_min stays ≥ the next ℓ_min in the balanced
    regime, so the top remains the pivot for the next pin, exactly as continued-fraction subtraction
    keeps reducing the larger argument; the chain never "wastes" a cut deleting a small piece
    outright (contrast the refuted max-greedy, which peels the largest chunk and stalls).
  - Schedule bound: the total after the k-pin chain is maximized (over Case (iii)) at the dyadic
    partition, where it equals u_kΣ exactly — because the dyadic ratios 1:2:…:2^k are the fixed point
    of the Euclidean pin-recurrence, so any non-dyadic Case (iii) instance sheds total strictly
    faster and lands below u_kΣ (Finding 2's slack).
Open gaps: Steps 3–4 — the explicit (r_j, top_j) recurrence and the "dyadic is the worst case for
  the chain" bound. Explorer traced the chain on only ONE instance (k=3), so Step 4 is a genuine
  research step, NOT yet a verified rule.
Cases to cover: Case (iii) only. Handle the schedule's termination (when ≤1 piece remains) and the
  branch where a pin produces a new equal pair (free delete, saves a cut).
Watch out for: (a) VERIFY the "pin largest against smallest" rule on many Case (iii) instances
  (k=3,4) with the ground-truth solver `/tmp/round-4/rt_search.py` BEFORE committing — one trace is
  not a rule; the optimal sequence in Finding 1 was `pin(ℓ₁,ℓ₃)→…→pin(·,ℓ₂)`, so the exact pivot
  order may be "against ℓ₃ first," not strictly smallest — pin down the correct canonical order
  empirically. (b) Do NOT reintroduce max-total greedy — refuted.

---

### Wall GAP L (lower bound) — reduced to Case-B residual GAP-LB′, the doubly-balanced region
### `y₁<2^{n−1}+1` AND `|D_top^<−D_bot|<1−D_top^>`, needing `2λ(O_Y^<∩O_Z) ≤ D_top^<+D_bot+D_top^>−1`

Proven dead here (do NOT retry): one-sided confinement of O_Z / O (odd-set reaches near 0 already at
n=1); ANY scalar/aggregate strengthening of Z (sum, altsum, D_bot≥1) — the reformulation
`D̃ ≥ sum(Y)−sum(Z)` is FALSE for scalar-summarized Z (three counterexamples, probes 5–7); strict
domination `W(n−1,b)>u_{n−1}`. The bound genuinely needs Z's origin as a recursive dyadic-cut
response, and it is TIGHT (D̃=1 attained), so no loose estimate suffices.

---

induction-recursion: revise
Target: Liu's dyadic partition {2^k u_n} forces D ≥ u_n against every ≤n-cut Xiang response —
  i.e. the full lower bound `c(n) ≥ 2^n/(2^{n+1}−1)` (whole problem's lower half).
Technique: Case-B induction closed by an **exchange / degenerate-boundary argument** — prove WLOG at
  the D̃-minimum one top-fragment vanishes, collapsing a top cuts to a−1 and bottoming out at Case A.
Skeleton:
  1. Import certified spine: reduction to D̃≥1 in integer units, Case A (a=0) done, threshold
     decomposition (★), (◇◇), (★★); Case B closed on `{y₁≥2^{n−1}+1}∪{|D_top^<−D_bot|≥1−D_top^>}`.
     Only the doubly-balanced residual remains.
  2. The doubly-balanced region (Y,Z both confined to (0,θ], sums 2θ and 2θ−1) is a compact
     parameter simplex (cut positions in closed bounded sets); D̃=λ(O_Y△O_Z) is continuous. So D̃
     attains a global minimum over the CLOSED region (fragments allowed to be 0). — by compactness +
     continuity of the level-measure functional.
  3. **Exchange lemma:** at any minimizer, the smallest top-fragment y_min can be pushed to 0 without
     increasing D̃ (shrink y_min, feeding its mass into merging with the adjacent top-fragment). —
     the research step; strongly supported by numerics: EVERY observed minimizer drives y_min→0.
  4. A top-fragment of length 0 means Xiang effectively spent a−1 cuts on the top. So the minimizer
     lies in the a−1 stratum; induct downward on a. — by the exchange reducing the cut budget.
  5. Base of the downward induction: a=1 with y_min→0 means x→0, i.e. the top piece is essentially
     uncut ⇒ Case A ⇒ D̃≥1. — already proven.
Key lemmas (claim + mechanism):
  - Compact minimizer: min D̃ over the closed doubly-balanced region is attained — because D̃ is a
    continuous (piecewise-linear) function of the finitely many cut positions on a compact simplex.
  - Vanishing-fragment exchange: shrinking the smallest top-fragment y_min→0 is D̃-non-increasing —
    because in the balanced region y_min sits at the bottom of the merged sorted list, where its
    contribution to the alternating level-sum is a boundary term of definite sign; removing it (and
    re-merging its adjacent T-fragment) cannot raise λ(O_Y△O_Z). This is a LOCAL, single-direction
    exchange, so Finding 3's global non-monotonicity does NOT obstruct it.
  - Downward-a induction: Case B with a top cuts reduces to a−1 cuts, terminating at a=0 (Case A) —
    because a degenerate (length-0) fragment is a top cut that was never used, freeing the budget.
Open gaps: Step 3 (the exchange lemma) is the sole research step — proving y_min→0 is
  D̃-non-increasing. Steps 1,2,4,5 are certified / bookkeeping.
Cases to cover: the exchange must handle (i) y_min interior to Y's sorted order vs (ii) y_min the
  global-smallest piece (below all of Z); numerics show every minimizer has y_min at/near 0, but the
  proof must cover both. Also handle ties (two equal smallest fragments).
Watch out for: (a) the exchange direction must be proven monotone for D̃ specifically — do NOT invoke
  global monotonicity (refuted, Finding 3); it is a single-coordinate boundary argument. (b) Ensure
  the merged-adjacent fragment stays in (0,θ] after absorbing y_min's mass (else it leaves the region
  and the induction breaks). (c) The reduction a→a−1 must not smuggle extra cut budget onto Z.

---

induction-recursion-telescope: copy-of induction-recursion
Target: Same whole-problem lower half — Liu's dyadic forces D ≥ u_n — via a merged-order telescoping
  decomposition instead of an exchange argument.
Technique: **Head/tail telescoping + bounded-T-run mass**, closed by a two-level joint induction on
  Z's OWN recursive dyadic cut-tree (Z = Y′⊎Z′ at threshold θ/2), NOT collapsing Z to the scalar
  D_bot≥1.
Skeleton:
  1. Import the certified spine (as above); only doubly-balanced GAP-LB′ remains.
  2. Merge Y∪Z into one descending sorted list; label each entry T (top-fragment) or B
     (bottom/Z-part). By Lemma G's signed-sum, D̃ = alternating sum along the merged order.
  3. Decompose D̃ = [telescoped head] + [alt-sum of tail], where the head is the maximal
     alternating T,B,T,B,… prefix (uses up all of Y) and the tail is leftover Z below the smallest
     T-part. On the head, the alternating sum telescopes to sum(Y_head)−sum(Z_head); the tail
     alt-sum is ≥0 (level-measure identity on a sorted descending list, Lemma-G argument). — by the
     merge-order telescoping identity (Finding, gapL report).
  4. Reduce GAP-LB′ to the single combinatorial sub-claim: the head covers Z-mass ≤ sum(Y)−1, i.e.
     Y's parts are never "trapped" below too much Z-mass, so head total ≥ 1.
  5. Prove Step 4 by strong induction on Z's recursive structure: Z arises from cutting the (n−1)-
     dyadic, so Z = Y′⊎Z′ at threshold θ/2 with Z′ a further recursive response; this bounds Z's
     local density (Z cannot have a long run without a fresh dyadic anchor value), which forbids long
     "T-runs" that would let Y's mass collapse. — the research step, a two-level joint induction.
Key lemmas (claim + mechanism):
  - Head/tail split: D̃ = [sum(Y_head)−sum(Z_head)] + [tail alt-sum ≥0] — because the merged
    alternating sum telescopes exactly on strictly-alternating stretches, and any trailing same-label
    block contributes its own nonneg internal alt-sum (consecutive-pair grouping, the certified
    Lemma-G monotonicity argument).
  - Bounded T-run mass: against the dyadic-derived Z, Y's T-runs carry total mass ≤ (|T-run|−1)·anchor
    — because Z's cut-tree places a dyadic anchor value within bounded rank distance, so consecutive
    T-fragments cannot all pack close together without a Z-part interleaving; this is exactly the
    structural fact scalar D_bot≥1 CANNOT supply (probes 5–7 refute the scalar version), and it needs
    Z's recursive origin. Proven by recursing on Z=Y′⊎Z′ at θ/2.
Open gaps: Step 5 (bounded-T-run via Z's cut-tree) is the research step; the explorer could not close
  it — the two-level joint induction is the recommended, unverified mechanism. Steps 1–4 are
  certified / the clean telescoping decomposition.
Cases to cover: merge orders with (i) leading T,T (no top cancellation, discrepancy carried by Z's
  tail — e.g. n=3 a=1 b=2 gave Y=(4,4)) vs (ii) strict alternation then Z-tail (n=3 a=2 b=1). Both
  observed at minimizers; both must be covered.
Watch out for: (a) do NOT attempt Step 4 as a free-standing two-multiset lemma — FALSE for arbitrary
  bounded Z (three counterexamples on record); it MUST invoke Z's cut-tree. (b) The T-run bound is
  where a counterexample-style loss hides (a T-run of near-equal values contributes ~0, not its sum);
  the induction must show the dyadic Z structure prevents such runs. (c) Keep equality-robust: D̃=1 is
  attained, so every inequality must hold with equality on the extremal zigzag family.

---

## Proposed field for the reviewer

Four approaches, two twins per open wall — each pair installs two *distinct, both-viable* mechanisms
so neither wall can plateau on a single idea. No orthogonal third framing (explorer confirmed none
exists; a cosmetic slug would only duplicate a wall).

1. **dyadic-discrepancy** — revise (GAP U Case (iii) via disjunctive reserve-buffer invariant,
   aimo-0340). Research step: derive the second clause + reserve.
2. **dyadic-discrepancy-euclid** — copy-of dyadic-discrepancy (GAP U Case (iii) via explicit
   chained-pin / Euclidean schedule). Research step: the (r_j,top_j) recurrence + "dyadic is worst
   case." Distinct from #1: concrete deterministic strategy vs strengthened IH. Verify the pivot
   rule on the solver first.
3. **induction-recursion** — revise (GAP-LB′ via exchange/degenerate-boundary: WLOG y_min→0,
   induct a→a−1 to Case A). Research step: the vanishing-fragment exchange lemma.
4. **induction-recursion-telescope** — copy-of induction-recursion (GAP-LB′ via head/tail
   telescoping + bounded-T-run mass, two-level joint induction on Z's cut-tree). Research step:
   the T-run bound from Z's recursive structure. Distinct from #3: merged-order signed-sum induction
   vs compactness/exchange on the level-measure functional.

Honest labeling: every one of the four residual gaps is a genuine RESEARCH step (not bookkeeping);
each approach's remaining spine (imports, RT/threshold decompositions, base cases) is certified or
routine. Both walls are numerically true and tight, so no loose estimate closes them.

build set: dyadic-discrepancy, dyadic-discrepancy-euclid, induction-recursion, induction-recursion-telescope
