## imo-2026-03

FIELD PRINCIPLE (single-gap-trap): exactly ONE vehicle per wall in the build set.
Build set recommendation: **{parity-measure-potential, breakpoint-vertex}** (one advance per
wall). The two revised reserves (ballot-matching, valley-differencing-construction) are put on the
table ranked-and-ready but are NOT built this round — they activate next round only if the
matching owner stalls. Do NOT build a reserve alongside its wall's owner (duplicate lever).

NEW NEGATIVE FACTS established this round (hand to reviewer/builder — they prune levers):
- **Suffix-Abel sign is DEAD too.** The bottom-up companion of the refuted prefix monovariant —
  Q_j = Σ_{i≥j} c_i ≤ 0 (c_i = 1[i odd]−S_i) — FAILS on 10643/12000 admissible walks (~89%).
  Combined with F1 (prefix P_k≥0 fails ~27%), **no one-pass sign monovariant works in EITHER
  direction**. The parity-measure lever below must be a genuinely 2-D/global object (strengthened-IH
  scale potential), NOT a value-Abel or index-Abel single-sign argument.
- **The ladder structure of B is LOAD-BEARING (confirms Lemma ONE is mandatory).** F={0.5,0.5,0.5},
  B={0.5} satisfies ΣF−ΣB=1, |F|=3, yet the combined multiset has 0.5 at multiplicity 4 (even) so
  D(S)=0 < 1. This is a genuine counterexample to the *structure-free* claim "ΣF−ΣB=1, |F|≥3 ⇒
  D≥1"; it is excluded from the game only because admissible B refines the superincreasing dyadic
  ladder C_{n-1} (half-integer values are unreachable). CONSEQUENCE: every lower-wall proof MUST
  invoke Lemma ONE recursed; a pure signed-walk / ballot argument that never touches the ladder
  cannot succeed. (My earlier all-integer adversarial sweep found "worst = 0" only because
  integrality accidentally excludes the half-integer witnesses — do not trust integer-only sweeps
  as evidence the ladder is unnecessary.)

---

parity-measure-potential: advance   [LOWER wall vehicle — build]
Target: the whole claim c(n)=2^n/(2^{n+1}−1) (minimax D=u_n), both bounds, via the measure identity
  D=μ{t:N(t) odd}. Lower bound is the residual; upper cases a₁≥L/2 already closed in this file.
Technique (spine): strong induction on ladder depth with a STRENGTHENED IH carrying a cross-scale
  reserve — a global potential Φ preserved under peeling the top dyadic gap via Lemma ONE recursed.
  This is the one live lower lever after prefix (F1) AND suffix (this round) sign monovariants both
  died; it is genuinely global (not per-scale-local, which is refuted 20–75%).
Skeleton:
  1. Import R, M/T, P, SPLIT, ONE, TB, MID, OSR, OSR-cap. By TB+MID the lower bound reduces to
     GAP MID-core: a=0 refinement S=F⊔B, ΣF=2^n, ΣB=2^n−1, B refines C_{n-1}, |F|≥3 ⇒ D(S)≥1,
     equivalently Σ_i c_i w_i ≥ 0 on the descending merge (Lemma OSR). — certified reductions.
  2. Peel the TOP dyadic gap G_top=(2^{n-1},2^n]. By Lemma ONE recursed, at most one final piece
     lies in G_top (it is the F-fragment f₁ of the shredded top), and B contributes nothing above
     2^{n-1}. — Lemma ONE.
  3. Define the strengthened potential Φ_k on the sub-ladder truncated at scale 2^{n-1-k}:
     Φ_k = D(S∩(0,2^{n-1-k}]) − ∫_{(0,2^{n-1-k}]} g + ρ_k, where ρ_k ≥ 0 is the RESERVE = credit
     carried down from coarser scales (the amount by which higher scales overshot their local ∫g).
     Claim: Φ_k ≥ 0 for all k, by induction descending k → k+1. — the reserve ρ_k is exactly what
     repairs the refuted per-gap-local statement: local deficit at scale k is covered by ρ_k, and
     ρ_{k+1} = ρ_k + (local surplus at scale k) ≥ 0 stays nonnegative because Lemma ONE bounds the
     per-scale F-excess by ≤1 fragment.
  4. At the bottom scale ρ absorbs into the terminal descent S_m=|F|−|B|≤0 (Fact F2), giving
     Φ_0 = D(S) − 1 ≥ 0. — telescoping the reserve to the base ladder (n=0,1 base cases certified).
Key lemmas (claim + mechanism):
  - Reserve-monotonicity: ρ_{k+1} ≥ ρ_k − (local deficit_k), and local deficit_k ≤ ρ_k — because
    Lemma ONE recursed caps the F-fragments entering gap k at ≤1, so the one-step overshoot of the
    signed walk within gap k is bounded by the credit already banked from strictly-coarser scales
    (this is the precise global object the two dead one-pass signs failed to be).
  - Base identity: on a sub-ladder with no interior F-fragment, D=∫g exactly (Σ_{odd}w telescopes
    to the mass) — the OSR-cap regime S_k≤1, already certified.
Open gaps: step 3 (define ρ_k in closed form and prove reserve-monotonicity — the make-or-break);
  step 4 terminal absorption (ρ_0 vs S_m≤0 accounting). Steps 1–2 are certified imports.
Cases to cover: |F|=2 (certified), 0≤g≤1 / S_k≤1 (OSR-cap certified) — residual is max_k S_k≥2,
  |F|≥3 only.
Watch out for: (a) do NOT reintroduce any one-pass sign monovariant (both directions dead this
  round); the reserve ρ_k is essential and must be nonneg-inductive, not a single prefix/suffix sum.
  (b) MUST use Lemma ONE (half-integer counterexample above shows a structure-free argument is
  false). (c) per-dyadic-gap LOCAL compensation is refuted — the induction's IH must be strengthened
  with ρ_k, a plain gap-by-gap induction will fail 20–75%.

---

breakpoint-vertex: advance   [UPPER wall vehicle — build]
Target: the whole claim c(n)=2^n/(2^{n+1}−1); upper bound in the balanced valley
  {m=n+1, a₁<L/2, a₂<β_nL}, β_n=2^{n-1}/(2^{n+1}−1), is the residual (a₁≥L/2 closed by whole-tail-peel).
Technique (spine): VERT vertex-finiteness + an EXISTENTIAL scale-recursion "band-landing"
  pigeonhole — peel a₁ against a subset T of the survivors whose sum lands one dyadic band below,
  then recurse the RESIDUAL (not a₁) two scales down. Existential/pigeonhole mode (distinct from the
  constructive valley-differencing reserve).
Skeleton:
  1. Import R, M, U0, whole-tail-peel, Reduction R-UV, RL, VS, ESF-1, ESF-2. R-UV reduces the valley
     bound to the Subset-KK claim: ∃ nonempty subset T with descending-KK caterpillar value ≤ u_nL.
     — certified.
  2. Band-landing lemma. Sort survivors descending a₂≥…≥a_{n+1}. The descending partial sums
     Σ_{i≤k}a_i move in steps of size a_k ≤ a₂ < β_nL = 2^{n-1}u_nL. The dyadic target band relative
     to a₁ has width ≥ 2^{n-1}u_nL. Since each step is < the band width, the partial sums cannot jump
     OVER the band: some prefix sum Σ_T lands inside the band (2^{n-2},2^{n-1}] (scaled) so that
     |a₁ − Σ_T| lands in the next lower dyadic band. — discrete intermediate-value (step-size <
     band-width). THIS is where a₂<β_nL is used.
  3. Two-step compound recursion. Form r = |a₁ − Σ_T| (one abs-flip on the caterpillar; two-sided,
     mandatory per the n=2 witness). The instance {r} ∪ (survivors∖T) has sum in the correct range
     to be a valid (n−1)-scale sub-instance; its Subset-KK value telescopes down to ≤ u_nL by
     induction on the number of dyadic scales. — induction on scales; budget stays ≤n (Lemma VS
     forbids a single-move IH, so the compound subset-peel+residual-recurse is used, not one
     DELETE/MATCH).
Key lemmas (claim + mechanism):
  - Band-landing: some descending prefix sum of survivors lands in the target dyadic band — because
    the max step a₂ < β_nL is strictly below the band width, so no band is skipped (discrete IVT).
  - Compound-move budget-legality: subset-peel (form Σ_T as a tree, |T|−1 cuts) + residual recurse
    uses exactly the n cuts, never exceeding budget — because ESF-2 gives the caterpillar as a
    tree-realizable ≤n-move DELETE/MATCH family.
Open gaps: step 2 band-landing rigor (step-size vs band-width, edge cases where Σ_T straddles the
  band boundary); step 3 that the residual instance is a genuine (n−1)-scale instance the IH applies
  to (the ratio target — NOT an O(a) bound; aimo-0796 is off by 2^{n-1} and is at most a base-case
  block, not the mechanism).
Cases to cover: full-budget valley only (U0 closes m≤n); a₁≥L/2 closed (whole-tail-peel).
Watch out for: (a) Lemma VS proves NO single move admits an IH(n−1) certificate — the recursion
  MUST be the two-step compound (subset-peel + residual-recurse), never a single DELETE or MATCH.
  (b) two-sided abs-flip is mandatory (one-sided ESF-1 refuted by n=2 witness {9/20,7/25,27/100});
  keep the |v_{j-1}−a_j| flip in the caterpillar. (c) do NOT invoke a raw 2^{n+1}-pattern pigeonhole
  (Lemma RL: only tree-realizable signed sums are reachable, a strict subset).

---

ballot-matching: revise   [LOWER reserve — RANK & READY, do NOT build this round]
Target: the whole claim; distinct contribution is a non-inductive certificate proof of GAP MID-core.
Technique (spine): explicit weighted debit→credit TRANSPORT on the signed walk with a Hall
  feasibility condition — genuinely different MECHANISM from parity-measure's induction (static
  certificate, no induction on n).
Re-plan of the open gap (why revised): the round-9 explorer + my numerics kill the naive
  per-scale-local Hall route. Per-dyadic-gap local compensation is FALSE (20–75%) and the
  "compensation distance" grows with n, so the transport graph needs LONG-RANGE edges (a debit at
  scale k repaid by credit arbitrarily far down). Therefore:
  - GAP-HALL (revised): do NOT verify Hall per-scale. Verify it via a SUFFIX-CUMULATIVE degree
    bound — for every dyadic threshold τ, cumulative debit above τ ≤ cumulative credit reachable at
    or below τ — proved by the aimo-0129/aimo-0197 bounded-degree double-count ADAPTED to a
    suffix-summed degree (each credit unit at scale j absorbs debits from ALL coarser scales, total
    degree bounded by the number of scales above it, which Lemma ONE recursed caps at ≤1
    F-fragment per scale). The double-count is over the suffix, not the single scale.
  - GAP-TERMINAL (unchanged): terminal descent S_m=|F|−|B|≤0 (F2) supplies the guaranteed bottom
    credit that absorbs residual debit; the transport is total.
Key lemma: suffix-cumulative Hall — cumulative debit above τ ≤ (#scales above τ) ≤ cumulative
  reachable credit — because Lemma ONE recursed bounds F-excess per scale by ≤1, so accumulated
  overshoot above any τ is at most the number of ladder gaps above τ, each guaranteed a −1
  B-crossing (credit) below.
Open gaps: GAP-HALL suffix-cumulative form; GAP-TERMINAL. Far-apart from parity-measure (transport
  certificate vs strengthened-IH potential) — activate next round if parity-measure stalls on ρ_k.
Watch out for: MUST use the ladder (half-integer counterexample); the transport edges are
  long-range, so the aimo-0129/0197 pattern needs the suffix-summed (not per-scale) adaptation —
  a naive nearest-scale bounded-degree argument is already refuted by the growing compensation
  distance.

---

valley-differencing-construction: revise   [UPPER reserve — RANK & READY, do NOT build this round]
Target: the whole claim; distinct contribution is an EXPLICIT deterministic Xiang algorithm bounding
  the valley leftover, dual to breakpoint-vertex's existential vertex/pigeonhole route.
Technique (spine): constructive subtractive-Euclidean differencing recipe + a drop-one DELETE
  family, analyzed by a remainder-size monovariant — kept far from breakpoint-vertex's existential
  band-landing pigeonhole by being an explicit algorithm with a proven bound, not an existence claim.
Re-plan of the open gap (why revised): the loose "keep every piece while r>0" DELETE rule
  (GAP-DELETE-RULE) is made deterministic via the explorer's opening-2 drop-one family and analyzed
  by opening-3's subtractive-Euclidean framing (the abs-flip chain r_k=|r_{k-1}−a_k| IS the
  subtractive Euclidean step):
  - GAP-DELETE-RULE (revised): the DELETE set is exactly one element — run descending KK on each of
    the n+1 drop-one subsets A∖{a_i}; the recipe outputs the best. Deterministic, budget-legal
    (|T|−1 matches + 1 delete = n at full budget). Numerically probe drop-one sufficiency first
    (explorer's cheap structural check) before the full recursion.
  - GAP-CHAIN (revised): bound the chain leftover by a subtractive-Euclidean remainder monovariant —
    r_k strictly descends through the dyadic bands, and a₁<L/2 (rest-sum > a₁) guarantees the chain
    never gets stuck positive; the remainder telescopes to ≤ u_nL matching the dyadic cascade
    2^n−2^{n-1}−…−1 = 1 = u_n(2^{n+1}−1). Not the raw aimo-0796 bound (off by 2^{n-1}); a genuine
    telescoping remainder bound.
Key lemma: Euclidean-remainder descent — after subtracting the k-th survivor, r_k ≤ (remaining
  survivor sum scaled to the next band) — because each abs-flip is a subtractive Euclid step and the
  drop-one choice removes the one piece that would otherwise stall the descent.
Open gaps: GAP-CHAIN telescoping bound; GAP-DELETE-RULE drop-one sufficiency (probe numerically
  first). Activate next round if breakpoint-vertex's band-landing stalls.
Watch out for: drop-one may be insufficient for some valley profiles (VS forces ≥2 coordinated
  cuts in the hardest sub-region) — if the numeric probe shows drop-one fails, fall back to the
  ≥2-delete family; do NOT ship the recipe on a spot-check (profile-independence mandatory).
