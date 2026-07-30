## imo-2026-03

Two isolated walls, each reduced to one clean claim, each now proven to need a GLOBAL/foresight
object (every single-pass/greedy/recursion route on BOTH walls refuted, R8+R9). The field below puts
ONE advance-vehicle per wall on its concrete new global object, plus ONE far-apart-mechanism
revised reserve per wall (so no wall is a single slug — single-gap-trap Rule). All four mechanisms
are distinct: LOWER = amortized potential (parity-measure) vs Hall/transport certificate
(ballot-matching); UPPER = existential two-level search (breakpoint-vertex) vs explicit even-
cancellation construction (valley-differencing-construction). Imports: all 19 certified lemmas
(reduction-odd-rank, measure-identity, cancelling-pair, PEEL, SPLIT, top-scale-dichotomy,
whole-tail-peel, TB, DM, U0, MID, RL, VS, OSR, OSR-cap, ESF-1, ESF-2, ONE-REC, BL).

---

parity-measure-potential: advance   [LOWER wall]
Target: c(n)=2^n/(2^{n+1}−1), both bounds; this vehicle owns the LOWER bound end to end via the
  measure identity D=μ{N(t) odd}. Whole residual is GAP MID-core (below); everything else certified.
Technique: whole-ladder foresight potential + amortized charging induction over dyadic scale-groups
  (aimo-0019 "ink game" template) — NOT a running-scan reserve (all of those refuted R9).
Skeleton:
  1. Import (certified): LB reduces to MID-core ⟺ ∫_0^{2^{n−1}} φ(g) ≥ 0, φ(c)=1[c odd]−c,
     g=N_F−N_B integer step function, ∫g=1, negative mass exactly on {g≥2}, residual |F|≥3. — by
     Lemma MID + R9 φ-reformulation.
  2. Define the whole-ladder RESERVE: R_F(τ) := Σ_{f∈F, f≤τ} f = 2^n − A(τ), A(τ)=Σ_{f>τ} f. This is
     F-MASS still queued below τ (a foresight quantity), NOT a count N_F(τ) — every refuted R9 reserve
     (ρ_k, ψ(g(τ))) was count-only, blind to queued mass. — by explorer-lower opening 1.
  3. Build the two-term potential Φ(τ) := R↓(τ) + κ·h(R_F(τ)), R↓(τ)=∫_τ^{2^{n−1}} φ(g), h monotone
     (linear or quadratic), κ a scale constant. Target: Φ(0) = ∫φ(g), and Φ(2^{n−1})=0. — by construction.
  4. AMORTIZED INVARIANT (the spine): scan τ top-down through the dyadic scale-groups G_j of B
     (certified Lemma ONE-REC: B_{≤ℓ}=⊔_{j≤ℓ}G_j is itself an admissible refinement of C_ℓ, each G_j
     has ≤1 fragment >2^{j−1}). Prove Φ does not decrease across each G_j because every unit of {g≥2}
     deficit created while scanning through G_j is CHARGED against the mass 2^j that G_j contributes
     (its scale budget) — exactly as aimo-0019 charges ink spent against interval length covered. — by
     amortized charging induction over G_j, using Lemma ONE-REC's per-scale ≤1-fragment cap.
  5. Conclude Φ(0)=∫φ(g)≥Φ(2^{n−1})=0, hence MID-core, hence D(S)≥1, hence the lower bound. Tightness
     (D=1 attained by the dyadic doubling cascade) already certified.
Key lemmas (claim + mechanism):
  - RESERVE-MONOTONE (make-or-break): Φ(τ) is non-increasing in τ across each G_j — because the
    {g≥2} band a scale-group can create has total length ≤ (its F-mass 2^j)/2, so the amortized charge
    R_F absorbs the φ<0 mass this group can generate; the ≤1-fragment cap (ONE-REC) is what bounds the
    overshoot g can reach WITHIN one scale before the next forced B-crossing (−1 step) repays it.
  - φ-sign identity (certified R9): φ≥0 ⟺ g≤1, φ<0 ⟺ g≥2 — so the reserve only needs to absorb the
    {g≥2} mass, and {g≥2} is exactly where B has fallen ≥2 behind F, which the ladder forces to be
    transient at every scale.
Open gaps: step 4 RESERVE-MONOTONE — the amortized charge inequality (the correct κ, h and the
  per-G_j charging bound). This is the ONLY open step; steps 1–3,5 are import+definition. Builder must
  first grid-search κ,h numerically (explorer flagged untested) against the a=0 refinement generator,
  then prove the per-scale-group charge inequality profile-independently via ONE-REC.
Cases to cover: |F|≥3 only (|F|=2 and 0≤g≤1 already closed inside MID); h∈{linear, quadratic}.
Watch out for: (i) do NOT let the reserve degrade to a count-only function of g(τ) — it MUST be the
  mass R_F(τ), or it re-hits the refuted ψ(g(τ)) wall; (ii) the half-integer witness F={½,½,½},B={½}
  (D=0 via even multiplicity, ΣF−ΣB=1, |F|=3) shows any structure-FREE ballot argument is FALSE — the
  charge MUST use the ladder (ONE-REC), integrality alone is insufficient (memory rule R9);
  (iii) the invariant is amortized (charged against progress), not a pointwise running bound — a
  pointwise Φ≥0 at every τ may FAIL; only the end-to-end telescoped inequality Φ(0)≥Φ(2^{n−1}) is claimed.

---

breakpoint-vertex: advance   [UPPER wall]
Target: c(n)=2^n/(2^{n+1}−1), both bounds; this vehicle owns the UPPER bound end to end via VERT
  finiteness + DM/leftover machinery. Whole residual is the valley Covering claim (below).
Technique: strong induction on n with a TWO-CASE split (generic vs near-uniform), NOT one uniform
  covering inequality — the explorer's key structural finding is that no single covering statement
  holds across all valley profiles.
Skeleton:
  1. Import (certified): upper bound reduces to the balanced valley {m=n+1, a₁<L/2, a₂<β_nL}, and
     there to the Covering claim: descending include/skip reachable set R_{n+1} meets [0,u_nL]
     (value 0 admissible via even cancellation). — by Reduction R-UV + Lemmas RL, VS, BL.
  2. CASE GENERIC (profile NOT near-uniform): existential two-level move lemma. Over the FINITE set of
     C(n+1,2)+(n+1) single MATCH/DELETE moves, exhibit ONE whose result either (a) lands in the
     already-UNCONDITIONALLY-closed dominant regime a₁'≥L'/2 of the (n)-piece problem (whole-tail-peel,
     no IH), or (b) admits Lemma VS's own single-move certificate one level down. Existentially
     quantified over the MOVE (not the profile) — genuinely distinct from the refuted deterministic
     single-rule recursions. — by finite move-search + certified whole-tail-peel / VS.
  3. CASE NEAR-UNIFORM (all n+1 pieces within a fixed ratio band): a separate explicit simultaneous
     even-cancellation construction — pair pieces by a sorted/interleaved matching to drive many
     differences to exactly 0, exploiting the even-multiplicity mechanism (Lemma U0) at one remove, so
     the reachable value drops to 0≤u_nL. — by explicit construction (housed in full detail in the
     far-apart reserve valley-differencing-construction; this case cites it).
  4. Verify the two cases PARTITION every valley profile (the near-uniform threshold is chosen so the
     generic case's two-level lemma is provably available outside it). — by the case-boundary lemma.
Key lemmas (claim + mechanism):
  - TWO-LEVEL-MOVE (make-or-break, generic case): outside the near-uniform band, some single move
    escapes to a₁'≥L'/2 or a VS-certificate — because a non-near-uniform profile has a dominant gap
    between two consecutive pieces, and MATCHing across it (or DELETEing above it) concentrates enough
    mass to clear the a₁'≥L'/2 threshold one level down. (Numerically 100% n≤4, ~98% n=5; the ~1.9%
    failures are exactly the near-uniform tail, handled in Case 3 — so the case split is forced by the
    data, not cosmetic.)
  - NEAR-UNIFORM-CANCEL: if all pieces lie in a factor-≈2 band, a sorted-interleaved even pairing sends
    ≥⌊(n+1)/2⌋ differences to 0 — because equal-size adjacency in a narrow band makes |a_i−a_{i+1}|
    telescope below u_nL, and the residual is a single small piece absorbable by DELETE within budget.
Open gaps: step 2 TWO-LEVEL-MOVE (prove the escape exists profile-independently outside the near-
  uniform band), step 3 NEAR-UNIFORM-CANCEL (prove the even-cancellation reaches ≤u_nL — delegated to
  valley-differencing-construction), and step 4 (the case-boundary partition lemma — the threshold must
  be explicit and make BOTH cases provable).
Cases to cover: generic vs near-uniform (partition of the full-budget valley); the near-uniform
  boundary must be pinned by an explicit ratio threshold, not left qualitative.
Watch out for: (i) do NOT re-propose any deterministic single-move rule (MATCH(a₁,a₂), always-DELETE-a₁,
  drop-one) — ALL refuted (VS + R9, overshoot up to 11.4×); the generic case is EXISTENTIAL over moves;
  (ii) a single uniform covering inequality across all valley profiles almost certainly does NOT exist
  (explorer: no classical dispersion/discrepancy theorem applies) — the two-case split is the point,
  do not collapse it; (iii) value 0 IS admissible (even cancellation), so near-uniform need not reach a
  small positive leftover, just 0 — this is what makes Case 3 tractable.

---

ballot-matching: revise   [LOWER wall — far-apart mechanism, second lower lever]
Target: c(n)=2^n/(2^{n+1}−1), both bounds; distinct contribution is a NON-inductive certificate-style
  proof of GAP MID-core (Σ c_i w_i ≥ 0 on the signed merge-walk), so the lower wall has two independent
  attacks that will not die together.
Technique: Hall's marriage theorem VERIFIED BY EXPLICIT ENDPOINT-SPLITTING of the candidate violating
  set (aimo-0129 template) — NOT an abstract max-flow/min-cut, and NOT the parity-measure induction.
Revision (re-plan of the open GAP-HALL): the R8 skeleton left GAP-HALL as "prove the debit→credit
  transport is feasible at every dyadic scale" with no method. Replace that with aimo-0129's concrete
  Hall-verification move:
  1. Debit set 𝒩={i: c_i<0} (walk ≥2 ahead of baseline), credit set 𝒫={i: c_i>0} (walk ≤baseline);
     GAP MID-core ⟺ Σ_𝒫 c_i w_i ≥ Σ_𝒩|c_i|w_i (total credit ≥ total debit). — imported (certified MID
     walk encoding).
  2. Bipartite "debit→later-credit" graph; by Hall it suffices that every candidate violating debit set
     has enough reachable credit. — by Hall's marriage theorem (KB: Hall/SDR).
  3. HALL CHECK BY ENDPOINT-SPLITTING (the new mechanism): given ANY candidate violating debit set,
     split it by its COARSEST dyadic-scale member (the aimo-0129 leftmost/rightmost analogue) and bound
     the reachable credit directly using Lemma ONE-REC's per-scale ≤1-F-fragment cap — a scale-by-scale
     explicit endpoint argument, NOT a general flow inequality. — by aimo-0129 endpoint-splitting.
  4. GAP-TERMINAL: the walk ends at S_m=|F|−|B|<0 (B large by the ladder), guaranteeing terminal credit
     absorbs residual debit. — by the forced terminal descent.
Key lemmas (claim + mechanism):
  - HALL-ENDPOINT (make-or-break): every candidate violating debit set, split at its coarsest scale
    G_j, has neighborhood credit ≥ its debit — because within G_j at most ONE F-fragment sits (ONE-REC),
    so the debit accumulated before the next forced B-crossing is bounded by that one fragment's mass,
    which the crossing's −1 step (a credit index) exactly repays.
Open gaps: GAP-HALL via HALL-ENDPOINT (the scale-by-scale neighborhood bound), GAP-TERMINAL.
Cases to cover: |F|≥3; the split at coarsest vs finer scales (induction down the ladder).
Watch out for: shares the TARGET inequality (MID-core) with parity-measure — kept live ONLY as the
  distinct-mechanism (matching-certificate vs amortized-induction) second lever; if the reviewer judges
  it too close, prune to parity-measure. Do NOT re-import the aimo-0156 Abel-suffix move (same refuted
  suffix-reserve shape).

---

valley-differencing-construction: revise   [UPPER wall — far-apart mechanism, second upper lever]
Target: c(n)=2^n/(2^{n+1}−1), both bounds; distinct contribution is an EXPLICIT constructive Xiang
  response for the near-uniform valley, existential-free — the constructive dual of breakpoint-vertex's
  existential search, so the upper wall's residual near-uniform tail has a second independent attack.
Technique: explicit simultaneous even-cancellation construction (sorted-interleaved pairing), NOT the
  refuted greedy sorted-difference chain (its GAP-CHAIN greedy hope is pruned R9).
Revision (re-plan of GAP-CHAIN/GAP-DELETE-RULE, whose greedy recursion is dead): narrow this slug's
  scope to the NEAR-UNIFORM case only (the residual breakpoint-vertex delegates), and replace the loose
  greedy chain with an explicit pairing recipe:
  1. Near-uniform valley: all n+1 pieces within an explicit factor-≈2 band. — by the case-boundary
     threshold shared with breakpoint-vertex step 4.
  2. Sort descending; PAIR adjacent pieces (a₁,a₂),(a₃,a₄),… by MATCH, sending each |a_{2i−1}−a_{2i}|
     to a small residual; the narrow band forces every such difference below u_nL. — by explicit
     construction on certified DM/P.
  3. The ≤1 leftover odd piece is DELETEd (bisect-and-cancel) within budget, and the many near-0
     differences even-cancel (Lemma U0 mechanism), giving reachable value 0 or ≤u_nL. — by Lemma U0.
Key lemmas (claim + mechanism):
  - INTERLEAVE-CANCEL (make-or-break): in a factor-≈2 band the sorted-adjacent pairing gives every
    |a_{2i−1}−a_{2i}| ≤ (band ratio −1)·a_{2i} ≤ u_nL, and the residuals telescope — because adjacency
    in a sorted narrow band minimizes each pairwise gap, matching the dyadic cascade's tight u_nL.
Open gaps: INTERLEAVE-CANCEL (prove the pairing residual ≤u_nL profile-independently for the near-
  uniform band); the explicit band threshold (must coincide with breakpoint-vertex step 4).
Cases to cover: near-uniform only (generic delegated to breakpoint-vertex); n+1 even vs odd (leftover
  piece parity).
Watch out for: do NOT resurrect the greedy descending-difference chain over ALL survivors (refuted,
  overshoot 7.5×) — this revision is a SIMULTANEOUS pairing (U0-style), not a sequential chain. Keep the
  scope to near-uniform; the generic bulk is breakpoint-vertex's, so the two upper slugs stay far apart.
