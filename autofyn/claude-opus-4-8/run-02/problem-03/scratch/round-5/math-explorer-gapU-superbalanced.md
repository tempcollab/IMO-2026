## imo-2026-03 — lens: GAP-U super-balanced residual ℓ₁ < Σ/2 (Case iii-b / U-B)

### Recap of the wall (verified by re-reading, not re-derived)
RT(k): m ≤ k+1 pieces ℓ₁≥…≥ℓ_m>0, total Σ, Xiang has ≤k "removal ops" (bisect: −ℓ_i,
1 op; generalized-pin ℓ_j into ℓ_i: −2ℓ_j, 1 op; free-delete an exact-equal pair: 0
ops), wants effective total ≤ u_kΣ (⇒ D ≤ u_kΣ via D ≤ total). Cases (i) ℓ₁≥c(k)Σ and
(ii) 2ℓ₂≥c(k)Σ: proven ∀k (one op + IH). Case (iii-a) Σ/2≤ℓ₁<c(k)Σ: proven ∀k via the
certified **Pivot/accumulator Lemma** (`lemmas/pivot-lemma.md`): pin every other piece
into ℓ₁ in decreasing order, residual = 2ℓ₁−Σ < u_kΣ exactly, tight at ℓ₁=c(k)Σ, and
= 0 right at ℓ₁=Σ/2. **Both twins bottom on region B: ℓ₁<Σ/2** — accumulator (and
every other tested fixed rule) overshoots by 2×–20× for k≥3; ground-truth solver
stays ≤0.72–0.88·u_kΣ there (R4 numerics), so region B is genuinely sub-extremal but
no proof exists.

### Distinct openings (ranked by how genuinely different they are from what's already tried)

**Opening 1 — the "mesh of reachable residuals" argument (from crux aimo-0292, 2nd solution).**
This is a **proof-strategy shift**, not another schedule. Instead of exhibiting one
canonical deterministic op-sequence (accumulator, chained-pin, pairwise-tournament —
all tried and refuted in region B), prove EXISTENCE of a good residual by bounding the
*gaps* in the set of values reachable via legal op-sequences. The template
(`aimo-0292`, IMO-SL-style "blocks of weight ≥1, total 2n" problem): sort pieces
increasingly, build up the achievable-value set incrementally `S_k = S_{k-1} ∪
(x_k+S_{k-1})`, and show by an averaging/pigeonhole contradiction that consecutive
elements of `S_k` are never more than a fixed gap apart (`x_k ≤ prefix-sum + gap`,
else the total budget is exceeded). Transplanted to our setting: define the reachable-
effective-total set `R(M)` for a partial op-budget, and directly bound its mesh near 0
using the SORTED-INCREASING order of the k+1 pieces plus the total-Σ constraint,
instead of trying to hit "0" with one hand-picked pivot chain. This sidesteps the
"which piece do I pin into which" design problem entirely — it's an existence argument,
not a construction. Concretely worth trying: is it true that in Case (iii-b) the
achievable-total set (under the actual bisect/pin/free-delete semantics, which realize
exactly the SIGNED sums `|Σ ε_iℓ_i|` reachable by SOME legal binary combination order,
`ε_i∈{0,±1}`) always has a point within `u_kΣ` of 0? The mesh technique proves such
existence claims by contradiction on a sorted prefix, which is a different mechanism
than "pick pivot = largest and subtract."

**Opening 2 — widen the induction hypothesis with an extra free parameter, à la
aimo-0292's 1st solution (induction loading).** That solution's actual mechanism:
remove the LARGEST item `x` (not smallest), using the AVERAGE bound `x ≥ s/n`
(pigeonhole on the total, not order statistics) to control the remainder
`s−x ≤ (n−1)/n · s`, then applies the IH not to the fixed target range but to a
WIDENED range `[−2, s−x]`, and glues the two halves (`[−2,s−x]` from excluding `x`,
`[x−2,s]` from including it) by checking the two intervals overlap. This is the
generic "strengthen the induction hypothesis" tactic (`knowledge_base.md` line
227–228: "induction loading"), but the KEY transferable trick is HOW: pigeonhole via
the AVERAGE `Σ/(k+1)` (always true, no case split needed) rather than sorted-order
facts about ℓ₁,ℓ₂ specifically, combined with covering an INTERVAL of targets (not
just proving one point is hit) so the two sub-cases' images overlap and splice. This
differs from the already-refuted 1-parameter reserve potential (`aimo-0340` route,
which failed because "recursion depends on ℓ₂,ℓ₃ individually") — here the extra
parameter is the TARGET WINDOW, not a scalar reserve tied to a single piece; it may
give the two-parameter degree of freedom the field has been missing. NOT yet attempted
in this problem — worth a careful transcription attempt.

**Opening 3 — 2-adic / integer recast specifically restricted to region B (not the
whole problem).** Run-state already ruled out a GLOBAL 2-adic recast as circular
(R4, orthogonal explorer). But that verdict was for the WHOLE upper bound; it was not
re-tested narrowly on region B, where all pieces are "sub-dominant" (ℓ₁<Σ/2) and the
extremal (dyadic) configuration sits exactly on the region-A/B boundary, not inside B.
Since the dyadic partition (Liu's actual construction) is never itself in region B,
region B is a purely "generic/interior" sub-case with NO known tight example — this
is consistent with Finding 2's 72–88% slack. A restricted-region LP/duality check
(NOT the refuted global concavity-lp, but one confined to the affine slice
`ℓ₁<Σ/2, max piece bounded`) has not been tried; flagged as a cheap thing to numerically
gate before investing in a hand proof — if `f` restricted to region B alone IS locally
concave/has a clean LP certificate (unlike the global landscape), that's a genuinely
different route than any schedule-based argument. UNTESTED this round — recommend a
quick numerical concavity check on region B alone before committing.

**Opening 4 (weaker, fallback) — chase only a CRUDE sufficient bound, not the tight
one.** Per R4 Finding 2, region B's true optimum has ≥12–28% slack below u_kΣ at
tested k (and the slack seems to GROW with k, e.g. up to ~72-88% used-fraction meaning
28%+ slack at k=3,4). This means region B does NOT need an exact closed-form ψ(k,β)
matching u_kΣ at any boundary (unlike region A, which is tight at ℓ₁→c(k)Σ but region
B never touches that point) — any strategy with a comfortable constant-factor safety
margin suffices. Concretely: try bisecting the TWO largest pieces ℓ₁,ℓ₂ (2 ops) and
applying RT(k−2) to the remainder of total Σ−ℓ₁−ℓ₂. Quick arithmetic check (below)
shows this does NOT always work as a clean induction on its own (remainder can still
exceed the needed fraction), but combined with the region-B constraint `2ℓ₂<c(k)Σ`
(inherited from failing Case (ii)) it is close — worth a numeric gate before writing it
up. This is technique-level, not framing-level, so treat as a fallback only if
Openings 1–3 stall.

### Cheap-kill / numeric gates to run before committing a builder to any of these
- For Opening 1: numerically build `R(M)` for small k (k=3,4) on region-B instances via
  the existing ground-truth solver (`/tmp/round-4/rt_search.py`) and check the MESH
  (max gap between consecutive reachable totals near 0) — if the mesh itself is ≤u_kΣ
  as a structural fact (not just the specific minimum found), the mesh proof template
  transplants cleanly; if the mesh is much larger and it's only the *specific* minimum
  that happens to land close, the analogy is weaker and Opening 2 should be preferred.
- For Opening 3: a 200–500 point Nelder-Mead/grid concavity check of `f` restricted to
  `{ℓ₁<Σ/2}` alone (k=3,4) — cheap, decides whether Opening 3 is worth a full LP writeup.
- For Opening 4: check numerically whether `bisect ℓ₁,ℓ₂ then apply IH to remainder`
  ever fails region-B instances (quick script) — if it already fails on many instances,
  drop it in favor of Openings 1–2.

### Candidate technique(s)
- Opening 1: **mesh-of-reachable-sums / incremental subset-sum covering** (distinct
  from the refuted "min |±signed sum| over ALL pieces, no zeroing" route — that route
  forced every piece into the combination; the mesh technique naturally allows
  "zeroing" a piece by simply not adding it to the running set at that step, matching
  Xiang's bisect option).
- Opening 2: **induction loading / strengthened IH with an extra free target-window
  parameter**, using an AVERAGE-based (pigeonhole) rather than ORDER-based peel step.
- Opening 3: region-restricted LP/concavity certificate (untested, cheap to gate).

### Knowledge-base entries to use
- `knowledge_base.md` lines 227–228: "Generalize: a stronger, cleaner statement is
  sometimes easier to prove by induction (induction loading / strengthening the
  hypothesis)" — directly the mechanism behind Opening 2.
- `knowledge_base.md` lines 108/188: "Pigeonhole / extremal principle" — the
  average-based peel step (`ℓ₁≥Σ/(k+1)`) needed for Opening 2's widened IH.
- (Already imported, do not re-derive) Invisible-Pair Lemma, Residual-Total Theorem,
  Pivot/accumulator Lemma — all certified in `lemmas/`.

### Analogous past problems (cruxes)
- **aimo-0292** (combinatorics, `induction-and-construction`) — "n blocks each ≥1,
  total 2n; hit every target r∈[0,2n−2] within a window of 2 using a subset." TWO
  solutions in the corpus, both genuinely transferable:
  - Solution 1 crux: *"Strengthen the claim before inducting: replace the rigid
    boundary value with an inequality and widen the free parameter's range so the IH
    applies to the smaller instance; peel the LARGEST item (not smallest), using the
    AVERAGE bound `x≥s/n` to control the remainder, then splice the two half-ranges
    (exclude/include x) by checking they overlap."* This is Opening 2 above — genuinely
    different from the current top-piece-vs-rest case split (which always uses ℓ₁ vs
    ℓ₂ as ORDER STATISTICS, never the average bound, and never widens the target).
  - Solution 2 crux: *"Build the achievable-sum set incrementally
    `S_k=S_{k-1}∪(x_k+S_{k-1})` and bound its mesh by a pigeonhole contradiction on a
    sorted prefix."* This is Opening 1 above.
  Very close structural analogy (fixed-budget covering of a target range from a
  bounded-weight multiset) — recommend the outliner read the full solution text
  (`past_problems_database.json`, `aimo-0292`) before building either opening.
- **aimo-0340** (combinatorics, `invariants-and-monovariants`) — already flagged (R4):
  disjunctive/reserve-buffer invariant; ALREADY TRIED at the 1-parameter level and
  refuted here ("recursion depends on ℓ₂,ℓ₃ individually," per run_state). Do not
  re-attempt the 1-parameter version; a genuine 2+-parameter generalization (matching
  Opening 2's two-parameter window) is untested and could still work.
- aimo-0117 (flagged in R4 as a mismatch/corpus data error) — do not use.

### Prior progress
Unchanged from `current.md`/approach files: RT reduces GAP U to Case (iii); Cases
(i),(ii) and (iii-a) `Σ/2≤ℓ₁<c(k)Σ` proven ∀k (Pivot/accumulator Lemma, certified).
Region B `ℓ₁<Σ/2` open; numerically true with 12–28%+ slack (k=2..4), non-monotone
across generic rays (R4 Finding 3), greedy/black-box provably insufficient (R3/R4).

### Dead ends (do not retry)
- Fixed deterministic pivot schedules on region B: accumulator (2ℓ₁−Σ, only works
  ℓ₁≥Σ/2), pin-against-smallest, pairwise-difference tournament, half-bisect-else-
  accumulate — ALL refuted for k≥3 in region B (R4 empirical gate, `dyadic-
  discrepancy-euclid.md` §5.4 table). Do not propose another fixed simple schedule.
- Greedy "remove-max-total" / black-box single-move + RT(k−1): proven to telescope
  above u_k for k≥3 (R3/R4).
- Global concavity/KKT/LP certificate over the WHOLE landscape: refuted R2 (12/60
  midpoint violations). Opening 3 above is a NARROWER, untested restriction to region
  B only — do not confuse this with the refuted global claim.
- 1-parameter reserve potential (`aimo-0340`-style, scalar reserve tied to one piece):
  refuted R4, does not close ℓ₁<Σ/2 because the recursion genuinely depends on ℓ₂,ℓ₃
  individually, not just on a scalar summary.
- Min `|Σε_iℓ_i|` over ALL pieces with ε_i=±1 forced (no zeroing/discard option):
  refuted, ratio up to ~19u_k, because the true optimum needs to DISCARD (bisect) some
  pieces rather than fold everything into a ± combination. (Note: this is NOT the same
  search space as the mesh technique of Opening 1, which naturally allows zeroing.)
- "Sup over Case (iii) attained as a monotone boundary limit along any ray": refuted,
  f is not globally monotone in ℓ₁ within Case (iii) (R4 Finding 3); any compactness-
  style argument must handle the jagged piecewise-linear structure, not assume
  monotonicity.

### Small-case / intuition notes (all labeled conjecture/numerical, from R4 unless noted)
- Region B never contains the extremal (dyadic) configuration — the dyadic partition
  sits exactly on the region-A/B boundary (ℓ₁=c(k)Σ>Σ/2 for all k≥1, since c(k)→1/2⁺
  from above). This is a STRUCTURAL fact (not just numerical): c(k)=2^k/(2^{k+1}−1)>1/2
  for all k≥1 (verified algebraically: 2^{k+1}>2^{k+1}−1). So region B is provably an
  "interior, non-extremal" region — consistent with why every tested schedule has slack
  there and supports Opening 4's "crude bound suffices" framing.
- (Numerical, R4, unverified by me directly this round but consistent with the
  algebraic fact above) sup_{region B} f(k,·)/u_k ≈ 0.72–0.88 for k=2..4, i.e. genuine
  slack, not a knife-edge case — reinforces that region B does not need a sharp bound,
  only *some* sufficient one, favoring Openings 1/2/4 (existence-style or crude-bound
  arguments) over hunting an exact tight schedule.
