## imo-2026-03

Field for round 7. Answer CONFIRMED c(n)=2^n/(2^{n+1}−1), minimax D=u_n=1/(2^{n+1}−1). Import
all 10 certified lemmas from `results/imo-2026-03/lemmas/` (R, M/T, P, PEEL, SPLIT, ONE, TB, DM,
U0, whole-tail-peel) — never re-prove. The whole field lives on exactly TWO residual gaps:
- **LOWER GAP L2-exch:** μ(O_F∩O_B) ≤ (D(F)+D(B)−1)/2, i.e. D(S)≥1, in the balanced overlap band
  |D(F)−D(B)|<1, D(F)>0, S=F⊔B (F = top-scale fragments summing to 2^n, ≥2 parts all ≤2^{n-1};
  B a refinement of C_{n-1}). Residual content is strictly |F|≥3 (|F|=2 closed). Closes BOTH
  former lower gaps at once.
- **UPPER GAP U-VALLEY:** for the full-budget balanced valley {m=n+1, a₁<L/2, a₂<β_nL, β_n→1/4},
  Xiang forces D ≤ u_nL. Genuinely adaptive (every deterministic DM rule off 4×–25×); mass-
  threshold refuted.

The two lower routes have now shared this one inequality for 3 rounds — plateau. Per the
shared-gap-break rule I keep the two live lower routes but **re-plan each toward a genuinely
different mechanism** (monovariant-split vs structural IH), and add one **new** lower framing
(reachable-pattern extremal) far from both. Upper: advance the VERT finitization AND open the
new restricted-subset-sum pigeonhole. Five approaches, kept far apart by mechanism.

---

### induction-peel: revise (lower exchange via aimo-0298 minimal-scale split-and-average)
Target: minimax D=u_n, hence c(n)=2^n/(2^{n+1}−1) — both bounds end to end (upper §4A closed for
a₁≥L/2; this revision closes the lower exchange, leaving only the shared upper valley, deferred to
the upper slugs).
Technique: strong induction on piece count with a **split-and-average monovariant** modeled on the
certified crux `aimo-0298` (IMO-SL 2019 C9), replacing the un-written "adjacent-pair exchange."
Skeleton:
  1. Import reduction to LB(n): min{D(S): S refines C_n, ≤n cuts} ≥ 1. — Lemmas R, M, TB (certified).
  2. TB + trivial regime + Case (a) + |F|=2 already closed. Residual: S=F⊔B, |F|≥3, all pieces
     ≤2^{n-1}, D(F)>0, |D(F)−D(B)|<1; prove D(S)≥1 profile-independently. — current file §3.3.
  3. Order the ≤2^{n-1}-bounded pieces of S descending; assign each the dyadic scale ⌊log₂⌋ of its
     gap to the next piece. Locate the **minimal-scale run** of sorted-adjacent pieces (the tightest
     cluster). — direct, mirrors aimo-0298's minimal-D pair selection.
  4. Split the run's members by parity of position into classes E and O; form the two SMALLER
     multisets S_O = R∪O and S_E = R∪E (R = pieces outside the run), each with strictly fewer
     pieces and ≤ n−1 cuts, so each satisfies IH LB(n−1): D(S_O), D(S_E) ≥ 1. — induction hypothesis.
  5. Combine: express D(S) via Lemma SPLIT against the run, and lower-bound it by the average
     ½(D(S_O)+D(S_E)) plus the run's own contribution, using that the minimal-scale run is a
     superincreasing-type cluster (two adjacent gaps at scale d sum to ≥ scale d+1, exactly Lemma
     ONE one level down). Conclude D(S) ≥ 1. — the split-and-average step, the one hard step.
Key lemmas (claim + mechanism):
  - Minimal-scale run is sorted-adjacent and its two flanking gaps each ≥ its scale — because any
    non-adjacent pair spans ≥ two gaps each ≥2^d, so |xᵢ−xⱼ|≥2^{d+1} (superincreasing, = Lemma ONE
    recursed); this is what makes E,O legitimate smaller instances (aimo-0298 crux transferred).
  - D(S) ≥ ½(D(S_O)+D(S_E)) on R's contribution, and each of O,E loses exactly one scale in its
    reduced instance — because deleting the complementary class removes the minimal-scale neighbour,
    dropping N(t)'s parity toggle on exactly the run's band (Lemma T), so the cross term only helps.
  - The floor is exactly 1 (attained by the below-/above-insertion canonical layouts, §3.3 exact
    telescoping D=(2^n−1)−w=f₁−1 and D=1) — so the induction target is tight, not slack.
Open gaps: step 5 (the split-and-average inequality D(S)≥½(D(S_O)+D(S_E))+run-term). This is the
sole remaining lower-bound content; closing it closes L2-exch for both live lower routes.
Cases to cover: |F|=3,4,…; degenerate check |F|=2 must reproduce the closed D(S)=D(T) case;
run of length 2 (single minimal pair) vs longer runs.
Watch out for: enforcing the cut budget (|F|−1)+c_T ≤ n−1 one level down when invoking IH (the
explorer flagged that an un-budgeted checker manufactures false counterexamples); the crude cap
μ(O_F∩O_B)≤min(D(F),D(B)) is provably too loose (D(F)=D(B)=1 gives true D(S)=2, cap gives 0) — the
split-and-average MUST carry the SPLIT cross term, not the min-cap.

### parity-measure-potential: revise (lower exchange via a STRENGTHENED structural IH)
Target: minimax D=u_n, both bounds via the measure identity D=μ{N odd}; distinct from
induction-peel by attacking the master inequality's IH itself, not the exchange.
Technique: strengthen the induction hypothesis from the scalar `D(B)≥1` to a **structural
gap-occupancy invariant** on the odd-set O_B, then bound μ(O_F∩O_B) gap-by-gap.
Skeleton:
  1. Import SPLIT master D(S) ≥ |D(F)−D(B)| (certified route) — closes |D(F)−D(B)|≥1 already.
  2. Residual balanced band: need μ(O_F∩O_B) ≤ (D(F)+D(B)−1)/2. The scalar IH D(B)≥1 feeds only
     the min-cap, which is proven insufficient here. — current file GAP L2-exch.
  3. Strengthen IH: prove by induction on n that for any ≤(n−1)-cut refinement B of C_{n-1}, the
     odd-set O_B, read against the dyadic gaps (2^{n-2-i},2^{n-1-i}) of C_{n-1}'s own recursion,
     meets each gap in a single interval and its total in each gap is controlled — a per-gap
     occupancy vector, not just its total measure D(B). — new inductive invariant.
  4. Since O_F ⊆ [0,2^{n-1}) also decomposes across these gaps (Lemma ONE recursed: ≤ one large
     F-excursion per gap), bound μ(O_F∩O_B) = Σ_gaps μ(O_F∩O_B∩gap) gap-by-gap, each term ≤ half
     the sum of that gap's F- and B-contributions minus the telescoping deficit. Sum to
     (D(F)+D(B)−1)/2. — gap-wise accounting.
Key lemmas (claim + mechanism):
  - Structural invariant: O_B meets each dyadic gap of C_{n-1} in ≤ one interval — because B refines
    a superincreasing ladder, so within each gap at most one B-piece can straddle it (Lemma ONE
    applied recursively to each tail scale).
  - Gap-wise overlap: μ(O_F∩O_B∩gap_k) ≤ ½(d_F,k + d_B,k) − ε_k with Σε_k = 1 — because on each
    gap the two odd-sets are single intervals whose overlap is maximised only when nested, and the
    "−1" global deficit is the telescoping Σt_k−Σg_k=1 distributed one unit total across gaps.
Open gaps: the structural IH itself (step 3 — that the per-gap occupancy invariant is inductively
preserved under a cut), and the gap-wise summation (step 4) recovering the exact −1/2 deficit.
Cases to cover: gaps holding 0, 1, or (impossible by invariant) ≥2 B-intervals; the top gap where
an F-excursion may exceed 2^{n-2}.
Watch out for: the explorer's warning that the master inequality may be UNCLOSABLE from D(B)≥1
alone — the whole point of this slug is that the fix is UPSTREAM (richer IH), so do NOT fall back to
sharpening the overlap cap in isolation. Keep this far from induction-peel: no monovariant/adjacent-
swap here, purely the structural-IH + gap accounting.

### breakpoint-vertex: advance (upper valley via VERT → explicit tie-pattern bound)
Target: minimax D=u_n, both bounds. VERT + TB already close the base/trivial/Case(a) lower and the
a₁≥L/2 upper unconditionally; advance the two `-fin` residuals, primarily GAP U-fin.
Technique: cash out the PROVEN Theorem VERT (optimal Xiang refinement is a polytope vertex with
≤n+1 distinct part-values) into an **explicit finite tie-pattern enumeration** for the balanced
valley, bounded via SPLIT + U0.
Skeleton:
  1. Import VERT, VERT-C: optimal response uses ties/bisections, ≤n+1 value-classes; peel even
     classes (Lemma P) to a core of distinct values. — certified in file.
  2. In the valley (m=n+1, a₁<L/2, a₂<β_nL), U0(b) says full cancellation needs budget ≥ m=n+1;
     with n cuts Xiang is exactly ONE mark short → exactly one core leftover ρ survives, D=ρ. —
     Lemma U0 + DM piece-count (each DM move drops piece count by 1).
  3. Write ρ as the value at each admissible vertex/tie-pattern: an explicit affine function of A
     over the finite set of combinatorial types τ (cut allocation) × tie-graphs. Minimise over
     patterns; show min ≤ u_nL using SPLIT's exact cross term. — VERT-licensed finite check.
  4. Induction on n persists (VERT finitizes WITHIN one step, does not remove the recursion, per
     explorer): the residual after peeling reduces to an (n−1)-instance closing by IH. — recursion.
Key lemmas (claim + mechanism):
  - "One mark short" leftover: at m=n+1, n cuts, the simultaneous even-pairing vertex leaves exactly
    one uncancelled core value ρ with D=ρ — because DM moves each reduce piece count by 1 and U0(b)'s
    full-cancel needs one more mark than available.
  - ρ ≤ u_nL at the optimal tie-pattern — because the SPLIT cross term between the paired classes and
    the leftover telescopes to the dyadic bound (the valley's worst case sits on the extremal
    profile, matching §3's tight dyadic input).
Open gaps: GAP U-fin (step 3 — the profile-independent min-over-patterns ≤ u_nL, currently a finite
per-n check, not a uniform proof); GAP L-fin shares induction-peel's exchange.
Cases to cover: the combinatorial types τ (compositions of ≤n into ≤n+1 parts) and tie-graphs — must
argue the min is achieved at the even-pairing type, not enumerate all by hand.
Watch out for: sequential/cascading single-piece bisection is refuted (4.7×); pairing must be
SIMULTANEOUS. VERT gives a per-n finite family, NOT an n-independent closed form — expect the
induction to carry the n-dependence.

### subset-sum-pigeonhole: new (upper valley via restricted subset-sum pigeonhole)
Target: minimax D=u_n, c(n)=2^n/(2^{n+1}−1), both bounds — a complete rival attempt whose DISTINCT
contribution is a pigeonhole proof of the upper valley; lower bound imported from certified
machinery (reduction + TB), deferring the shared lower exchange.
Technique: **restricted subset-sum / number-partitioning pigeonhole**. The denominator 2^{n+1}−1 is
exactly the pigeonhole gap-count for the 2^{n+1} subset sums of n+1 numbers — a genuinely new
framing, far from every DM-induction and every mass/measure route (never tried; distinct from the
refuted mass-threshold subset-cover).
Skeleton:
  1. Reduce to full-budget valley (m=n+1, else U0 gives D=0 with ≤n cuts). — Lemma U0(c).
  2. The 2^{n+1} subset sums of {a₁,…,a_{n+1}} lie in [0,L]; pigeonhole ⇒ two subsets differ by
     ≤ L/(2^{n+1}−1)=u_nL; their symmetric difference gives a nonzero signed combination
     Σε_i a_i with |Σε_i a_i| ≤ u_nL. — classical subset-sum pigeonhole.
  3. A sequence of n DM (MATCH/DELETE) moves on n+1 pieces yields one leftover ρ = |Σε_i a_i| for
     the ε-pattern realised by that differencing tree, with D(final)=ρ (Lemma P/PEEL). So the
     achievable D-values are exactly the differencing-tree-realizable signed combinations. — DM +
     PEEL identity.
  4. Characterize the realizable sign-pattern family (tie it to VERT's tie-graph / binary-
     differencing-tree family) and run the pigeonhole RESTRICTED to that family, forcing an
     achievable ρ ≤ u_nL. — the new lever.
Key lemmas (claim + mechanism):
  - D-achievability = differencing-tree realizability: Xiang's ≤n-cut leftover ρ ranges over
    {|Σε_i a_i| : ε a tree-realizable ±1 pattern} — because each MATCH subtracts one current piece
    from another (a ± combination) and DELETE zeroes one, exactly a binary differencing tree.
  - The realizable family is large enough (or structured enough) that pigeonhole over it still
    forces a gap ≤ u_nL — candidate mechanism: augment the ~2^n realizable magnitudes with one
    free DELETE (dropping to n numbers, restoring the factor 2), or exploit sortedness/monotonicity
    of the realizable value set so consecutive achievable sums are ≤ u_nL apart.
Open gaps: **the achievability–deficit** (HARD, flag prominently): the explorer verified numerically
that only ~HALF of ±1 patterns are tree-realizable (2^{n-2} of 2^{n-1} for n=4), so a NAIVE
restricted pigeonhole over ~2^n achievable values gives only gap ≤ u_{n-1}L — short by a factor ≈2.
The approach lives or dies on closing this factor-2 deficit (via the DELETE-augment or a
monotone-consecutive-sums argument). This is the single make-or-break step.
Cases to cover: whether the realizable family size is exactly half for all n (explorer conjecture,
tested only n=4) — must be proven, not assumed; the boundary where a DELETE is spent.
Watch out for: do NOT conflate with the refuted mass-threshold subset-cover (a single-threshold
search) — this is a full sorted-subset-sum-gap pigeonhole, distinct. Every claimed ρ MUST be
exhibited as a legal ≤n-cut response (achievability), or the pigeonhole is vacuous.

### merge-interleave-pattern: new (lower exchange as a reachable-pattern extremal problem)
Target: minimax D=u_n, both bounds — complete attempt; DISTINCT contribution is a combinatorial
proof of the lower exchange (D(S)≥1) treating F and B symmetrically, NOT via SPLIT and NOT via a
value-exchange monovariant.
Technique: encode the descending merge of F and B as a binary interleaving **pattern** (string);
D(S) is a fixed linear functional of the pattern and the values; reduce "D(S)≥1" to an extremal
claim over the patterns REACHABLE under the cut budget (|F|−1)+c_T ≤ n−1.
Skeleton:
  1. Reduce to S=F⊔B balanced band as in the other lower slugs (import TB, ONE, closed cases). —
     certified.
  2. Read the merged descending order of F∪B as a word w∈{F,B}*; D(S)=Σ(−1)^{rank+1}·value is a
     linear functional L_w(values). — direct from Lemma R.
  3. Characterize which words w are REACHABLE: the cut budget bounds |F|+|B| and the ladder
     structure of B (superincreasing gaps) forces the B-letters into a fixed relative order and
     limits how many F-letters fit between consecutive B-letters. — combinatorial constraint.
  4. Over reachable (w, values), minimise L_w: show the minimum is the canonical one-F-per-gap
     word with the telescoping value exactly 1, and any deviation raises L_w. — extremal-pattern
     argument (reachable-pattern polytope vertices).
Key lemmas (claim + mechanism):
  - Reachable words = those with ≤1 F-letter strictly inside each B-gap plus a bounded overflow —
    because two F-fragments in one gap sum below the gap's upper tail value yet each exceeds the
    lower, contradicting the sum constraint Σ F = 2^n with the ladder gaps (superincreasing).
  - min L_w over reachable words = 1, attained at the canonical interleave — because L_w is linear
    in the values on each fixed word and the reachable-value polytope's vertices are the canonical
    telescoping layouts (Σt_k−Σg_k = (2^n−1)−(2^n−1)+1 = 1 exactly).
Open gaps: the reachable-word characterization (step 3) and that its minimum is the canonical
interleave (step 4). This is a THIRD independent attack on L2-exch, far from monovariant-split
(induction-peel) and structural-IH (parity-measure).
Cases to cover: words with an overflow F-letter above the top gap; empty gaps.
Watch out for: this must NOT collapse into induction-peel's adjacent-swap (which slides values) —
here the object is the discrete WORD and its reachability, an extremal/counting argument. Enforce
the budget or the reachable set is over-counted (false minima, per explorer's harness warning).

---

### Rationale for the outline-reviewer (candidate slugs)

Five slugs, kept far apart by MECHANISM, two per remaining gap plus a bridge:

- **LOWER GAP L2-exch — three independent mechanisms** (the wall has plateaued 3 rounds; per the
  shared-gap-break rule, diversify rather than route around):
  - `induction-peel` (revise): split-and-average monovariant modeled on the certified crux
    aimo-0298 — the concrete, corpus-backed way to WRITE the missing exchange step.
  - `parity-measure-potential` (revise): the fix is UPSTREAM — strengthen the IH to a structural
    per-gap occupancy invariant (explorer opening #1: the master inequality may be unclosable from
    D(B)≥1 alone). Genuinely different from a monovariant.
  - `merge-interleave-pattern` (new): reachable-pattern extremal / counting — a different top-level
    target ("which interleavings are reachable"), far from both.
- **UPPER GAP U-VALLEY — two independent mechanisms:**
  - `breakpoint-vertex` (advance): cash out the PROVEN Theorem VERT into an explicit tie-pattern
    bound; the finitization lever the task calls for.
  - `subset-sum-pigeonhole` (new): the restricted subset-sum pigeonhole the explorer surfaced
    (2^{n+1}−1 = pigeonhole gap-count) — genuinely new territory; hard step is the factor-2
    achievability deficit, flagged honestly.

Recommended build priority if slots are limited: `induction-peel` (most concrete lower mechanism)
and `breakpoint-vertex` (advance, ready) first; then `subset-sum-pigeonhole` (highest-novelty
upper) and `parity-measure-potential` (structural IH); `merge-interleave-pattern` as the diversity
bet to break the lower plateau. No slug re-treads a recorded dead end (greedy/single-peel,
mass-threshold subset-cover, deterministic DM rules, "WLOG single top cut" all avoided).

candidate slugs: induction-peel (revise), parity-measure-potential (revise), breakpoint-vertex
(advance), subset-sum-pigeonhole (new), merge-interleave-pattern (new)
