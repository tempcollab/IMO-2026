## imo-2026-03 (LOWER wall — Hall/transport matching lens)

### Setup recap (from ballot-matching.md + clipped-tau-family.md, verified consistent)
GAP MID-core ⟺ Σ_i c_i w_i ≥ 0 on the descending merge of an a=0 refinement S=F⊔B, where
w_i are gap lengths, c_i = 1[i odd] − S_i (S_i = signed partial sum of e_j=±1, +1 for F, −1 for
B). **Note c_i is always EVEN** (S_i ≡ i mod 2 by construction, so c_i = 1−S_i or −S_i, both even
integers) — this parity-of-c_i fact is not yet used anywhere in ballot-matching.md and is a free
structural handle. Credit set 𝒫={c_i>0}, debit set 𝒩={c_i<0}; need Σ𝒫 c_iw_i ≥ Σ𝒩|c_i|w_i.
Equivalently, via certified Lemma CLIP (τ-family), the τ=0 face of the transport form
Σ_{F even rank}v ≤ Σ_{B odd rank}v (order-statistic form, no c_i needed) — this is algebraically
the SAME statement, just packaged without the walk indices; useful as a cross-check but not a new
route.

### Distinct openings (three concrete framings for the matching/transport lever)

1. **Max-flow / min-cut (LP-duality) framing — recommended primary vehicle.** Because weights w_i
   are continuous lengths (not unit capacities), a literal finite Hall marriage theorem is the
   wrong tool; the right generalization is the **Gale–Hoffman feasibility theorem for
   transportation problems** (a weighted/fractional Hall condition): a flow saturating all debit
   supply within credit capacity exists iff for *every* debit-index set X, the credit reachable
   from X (under whatever adjacency the ladder allows) has total capacity ≥ debit(X). This directly
   explains WHY every single-threshold scalar reserve Φ(τ) (R10, dead) was too weak: Φ(τ) only
   checks the cut family {prefixes/threshold sets}, a strict sub-family of all possible cuts. The
   correct min-cut may be attained on a **non-prefix set** — e.g. a union of several dyadic bands
   with an untouched gap between them — which the R10 n=7 witness (Φ(8.944)=−2.07<0 while D=15.07)
   is consistent with: the local deficit at one band is masked by surplus a scalar running sum
   cannot "reach back" for. This is a genuinely different framing from the CLAUDE-dispatched
   endpoint-splitting recipe (below) — it is the honest statement of what "Hall feasibility" MEANS
   here, and the endpoint-splitting recipe is best understood as a *proof technique for verifying
   this min-cut condition*, not a separate structure.

2. **aimo-0129-style endpoint-splitting (the dispatched recipe) — a verification technique, not a
   new object.** aimo-0129's Hall check reduces "check |N(S)|≥|S| for every S⊆G_h" to "split S by
   its two EXTREME members (leftmost/rightmost hole) and bound via the two longest sticks on each
   side" — i.e. it never checks all subsets directly, only a canonical 2-parameter family generated
   by extremes. Direct translation here: given a hypothetical violating debit set X (Σ_X|c_i|w_i >
   reachable credit), split X at its **coarsest dyadic-scale member** i* (i.e. the member closest to
   the top of B's ladder, scale j* = ⌊log2 of the corresponding piece⌋), and bound the credit
   reachable from {i ∈ X : scale(i) ≤ j*} using Lemma ONE-REC's ≤1-fragment-per-scale cap on THAT
   scale alone — recursing to X minus its scale-j* part, which is a violating set for the STRICTLY
   SMALLER sub-ladder (Lemma ONE-REC part (i), scale-truncation is itself an admissible refinement
   of C_{ℓ}). This is a genuine strong induction on the scale, dressed as an endpoint-split; it
   converges to the recursion in framing 3 below.

3. **aimo-0341 defect-Hall (peel-the-maximal-deficient-set) — the honest fallback if 1/2 stall.**
   aimo-0341's crux is: when the raw bipartite graph does NOT satisfy Hall's condition everywhere,
   take the MAXIMAL deficient set W (|N(W)|<|W|, chosen maximal), delete W ∪ N(W), and Hall's
   condition automatically holds on the complement (else W could be enlarged) — this is the
   textbook defect/König form of Hall (Hall's theorem's deficiency version, `|N(S)|≥|S|-def(G)`
   for every S iff a matching of size `|X|-def(G)` exists). Translated: IF a scalar/local per-scale
   accounting genuinely fails on some worst-case scale-band (matching the R10 refutation pattern),
   the correct move is not to patch that band's local inequality but to **peel off the maximal
   deficient band-cluster as a single unit**, verify it is absorbed by the walk's forced TERMINAL
   descent (GAP-TERMINAL: S_m = |F|-|B| < 0, so the walk *must* end net-negative and every unpaired
   debit is guaranteed a home at the bottom), and apply the per-scale Hall bound only to what
   remains. This reframes GAP-TERMINAL not as an afterthought but as literally the deficiency term
   `def(G)` of the defect-Hall theorem — worth stating explicitly as a named quantity.

### Candidate technique(s)
Gale–Hoffman transportation feasibility / max-flow-min-cut (framing 1) as the target theorem;
aimo-0129 endpoint-splitting (framing 2) as the technique to verify the min-cut condition
scale-by-scale without checking all 2^m subsets; aimo-0341 defect-Hall peeling (framing 3) as the
fallback if the per-scale bound alone is insufficient, with the walk's forced terminal descent
(S_m<0) as the natural "deficiency budget."

### Cheap-kill candidates
- **Parity of c_i (even integers).** Not yet exploited. A quantization/integrality argument in
  the spirit of aimo-0752 (Abel-summed slack sequence + integer-gap floor) may give a cheap partial
  bound: since every c_i is even, Σc_iw_i is a signed sum of even-integer-weighted lengths; check
  whether the SIGN PATTERN of c_i alone (independent of exact walk value) already forces a floor
  via the "walk ends net negative" fact — worth a 30-minute numeric probe before committing to a
  full flow argument.
- **Recursion collapse risk (structural pitfall, not a kill but a warning).** Both framing 2 and
  framing 3, when unrolled, become a strong induction on the dyadic scale of B — essentially the
  SAME recursive skeleton as parity-measure-potential's induction on n (Case A/a=1/a=0). If the
  outliner builds ballot-matching by literally inducting scale-by-scale via ONE-REC, it risks
  landing on THE SAME wall as parity-measure (single-gap trap in disguise). The genuinely distinct
  content must be the FLOW/TRANSPORT certificate itself (an explicit assignment of debit mass to
  credit mass, checkable by inspection on any instance) — not a re-derivation of MID-core via
  induction on n dressed in matching language. Flag this explicitly to the outliner: the build
  must produce an EXPLICIT transport map (or explicit min-cut description), not an inductive proof
  that merely invokes Hall's name.

### Knowledge-base entries to use
- `knowledge_base.md` §Combinatorics: "Hall's marriage theorem / SDR" (bipartite `X,Y`, Hall's
  condition `|N(S)|≥|S|` — cited explicitly, this is the base tool).
- No explicit max-flow-min-cut / Gale-Hoffman entry exists in knowledge_base.md — this generalization
  is NOT currently named there; the outliner should state it and cite it as a named classical fact
  (LP duality for transportation problems / generalized Hall) if used, per the "name your tools" rule.

### Analogous past problems (cruxes)
- **aimo-0197** (`problem_id`) — bounded-degree double-count: BOTH sides of the bipartite graph are
  exactly 3-regular, so Hall's condition is FREE by a one-line degree count (`3|S|` edges from `S`,
  each token absorbs ≤3, so `|N(S)|≥|S|`). **Analogy is WEAK for our problem**: our bipartite
  debit/credit structure is NOT regular (debit/credit weights vary continuously and the "degree"
  — how many scales a given debit can reach — is not uniformly bounded a priori). Useful only as
  the aspirational best case (if a regularity property of the ladder could be found, the whole
  proof collapses to one line) — worth a quick check whether ONE-REC's ≤1-per-scale cap can be
  upgraded to a genuine degree-regularity statement, but no evidence yet that it can.
- **aimo-0129** (`problem_id`) — endpoint-splitting Hall verification on two families of maximal
  sticks: **genuinely analogous** (a continuous/weighted analogue), see framing 2 above. The
  closest structural match in the corpus: extremal-member splitting to avoid checking all subsets.
- **aimo-0341** (`problem_id`) — defect-Hall / maximal-deficient-set peeling for a covering lower
  bound via CRT-grid encoding: **analogous in TECHNIQUE (the deficiency-Hall pattern)**, not in
  subject matter (it's a totally different problem, AP covering of ℤ). Cited only for the reusable
  proof pattern (framing 3), not as a source of any problem-specific content.
- **aimo-0752** — Abel-summed slack sequence + integrality gap floor: not a matching problem at all,
  but flagged as a possible CHEAP-KILL probe (see above) exploiting c_i's evenness; likely a
  secondary lever, not the primary matching mechanism.

### Prior progress
GAP MID-core reduced (certified, via Lemma MID + CLIP + OSR) to the clean order-statistic transport
form `Σ_{F even rank}v ≤ Σ_{B odd rank}v` (τ=0 face). ballot-matching.md has a skeleton (credit/debit
sets defined, "Hall/feasibility condition" stated in prose) but NO explicit transport map has been
constructed and NO Hall/min-cut condition has been verified even in a single nontrivial case (n=3,
|F|=3). This is the most concrete, actionable next step: build ONE fully explicit worked example
(e.g. n=4 or n=5, |F|=3, a hand-built B) and exhibit the actual assignment/flow by hand before
attempting the general proof — the field has no worked instance of the matching yet.

### Dead ends (do not retry)
- ALL additive scalar reserves Φ(τ) (single-threshold, both count- and mass-based) — REFUTED R10,
  n=7 witness, required κ unbounded in n. Framing 1 above explains WHY: Φ(τ) only tests the
  prefix-cut sub-family, not all cuts — do not re-propose any one-parameter running potential.
- The outliner's original "single-interval-per-dyadic-gap" invariant on O_B — REFUTED R7 with an
  explicit witness (`B={1,1.865,2,2.135,2.915,5.085}`, 2 intervals in gap (2,4)).
- Fixed/bounded-depth existential-move lemmas — this is an UPPER-wall dead end (R10), not directly
  relevant here, but the general lesson (bounded-depth arguments fail when required "reach" grows
  with n) applies as a caution against any matching scheme that only connects debit to credit
  within a FIXED number of scales.

### Small-case / intuition notes (conjectural, numerically informed)
- The n=7 CLIP witness (`F={63.0119,62.8559,2.1322}`, 12-piece B) is the sharpest known adversarial
  instance and should be the FIRST test case for any proposed transport map — if an explicit
  assignment can be exhibited by hand on this instance (verifying the debit is fully absorbed by
  reachable credit under the ladder-adjacency the outliner defines), that is strong evidence the
  mechanism is real; if it fails there too, the "matching via local scale-adjacency" idea likely
  needs the same non-local (union-of-bands) cut structure that framing 1 predicts is necessary.
- No new small-case computation was run this round (time budget spent on corpus/lemma reading);
  recommend the builder's first action be a direct numeric construction of the transport map on
  n=3..5 random a=0 witnesses via a small LP/max-flow solver (scipy.optimize.linprog or a simple
  greedy) to empirically locate where the true min-cut sits — this is cheap (minutes) and will
  either find the right cut family or immediately falsify "local scale-adjacency only" (framing 2
  alone) in favor of needing framing 3's global deficiency peel.
