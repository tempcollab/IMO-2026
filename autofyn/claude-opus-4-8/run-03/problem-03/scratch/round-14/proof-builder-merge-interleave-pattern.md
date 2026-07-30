# Build report — merge-interleave-pattern (LOWER wall, GAP-EXTR), Round 14

## Verdict: PARTIAL — mandatory gate FAILED; the LP-dual/sparse-Farkas MECHANISM is REFUTED.
The underlying CLAIM (min L_T ≥ 1 at every vertex) is CONFIRMED and further de-risked to n=5,
but the proposed vehicle (a closed-form sparse Farkas certificate + odd-block collapse) does
NOT exist. Per the hard constraints ("if the gate FAILS, report and STOP — do NOT ship a fake
proof"), I did not write prose closing GAP-EXTR. I record rigorous refutations + one new
rigorous structural lemma.

## Gate results (scipy HiGHS + exact hand-check of the load-bearing coefficient identity)

**CLAIM holds (good news):** min L_T = 1.000000 at n=3, n=4, n=5 across all sampled types/words;
NO vertex with L_T < 1. GAP-EXTR is now numerically confirmed at n=5 (prior explorer only had
partial n=5). Example n=5 minimiser: F-type |F|=3, k=(1,1,3,1,2), vertex
{12,12,8,8,8,8,2,2,1,1,1}, L_T = 1.

**Gate condition (i) — sparse dual pattern "±1 equality multipliers + a single order-inequality
with multiplier 2": FAILS.** The extracted optimal duals VARY by type — some use one order-slack
×2, some use FOUR order-slacks ×1, some use a box multiplier. There is NO uniform closed-form
sparse certificate. Moreover I proved the specific "±1 equalities" form is *rigorously
impossible* for the mandated non-canonical n=4 witness (F={6,6,4}, tail level-3 split {3,3,2},
sorted {6,6,4,4,3,3,2,2,1}, L_T=1):
 - The witness vertex is strictly box-interior (all 0<v_i<2^{n-1}=8), so by complementary
   slackness EVERY optimal (=certifying) dual has zero box multipliers.
 - Coefficient matching on the order chain then forces (summing all m position-equations,
   telescoping the chain multipliers) the two identities Σ_g y_g·rhs_g = 1 and
   Σ_g y_g·|group g| = [m odd].
 - rhs_g are the distinct powers {2^0,…,2^n}; the signed-power equation Σ ±2^k = 1 has a UNIQUE
   ±1 solution y_F=+1, y_{tail}=−1 (binary uniqueness: the positive-signed rhs must sum to 2^n,
   only {2^n}=F works). That choice gives Σ y_g|g| = |F|−|B| = 3−6 = −3 ≠ [9 odd]=1.
   Contradiction. So NO ±1-equality certificate exists for this type. (The actual optimal dual is
   y = e_{L0} (+1 on the value-1 group only) with FOUR order-slack multipliers ×1 at positions
   1,3,5,7 — verified by LP and by the explicit identity
   L_T−1 = (v_9−1) + Σ_{k∈{1,3,5,7}}(v_k−v_{k+1}).)

**Gate condition (ii) — "every box-free vertex has ≤ one odd-size block": FAILS.** Box-free
vertices with up to 5 odd blocks occur (n=5), INCLUDING at tight L_T=1 vertices. Clean explicit
counterexample at n=4: F={6,6,4}, tail C_3 with level-3 (value 8) split into {4,4}, others uncut;
sorted {6,6,4,4,4,4,2,1}, box-free, L_T = 6−6+4−4+4−4+2−1 = 1, block sizes [2,4,1,1] — TWO odd
singleton blocks {2} and {1}. This refutes both the "≤1 odd block" collapse AND the explorer's
"the odd residual block is pinned to the smallest scale (value 1)" conjecture (here one odd block
has value 2).

## Why this kills the vehicle (not just the sparsity)
The certificate-existence question is, by strong LP duality, EXACTLY equivalent to GAP-EXTR — it
is a loss-free reframing (like VERT-LOW itself), not a reduction. The ONLY thing that would have
made it a genuine lever is a *closed-form, uniform, provable* multiplier pattern. Both proposed
handles for that (sparse ±1/×2 dual; odd-block collapse to a single scalar) are now refuted. The
exact box-free characterization I derived (∃ y with Σ y_g rhs_g=1, Σ y_g|g|=[m odd], and the chain
prefix-sums z_k = Σ_{l≤k}(s_l − y_{g(l)}) ≥ 0) IS rigorous, but proving y always exists is
equivalent to the claim — no free lunch. So the LP-dual/exchange-smoothing vehicle provides no
lever beyond restating GAP-EXTR. It should be retired for the LOWER wall, exactly as the
scalar-reserve and structured-matching vehicles were.

## New RIGOROUS content (proposed for certification)
1. **Lemma DUAL-CHAR (box-free chain-certificate characterization).** For a box-free type T, a
   Farkas certificate of L_T≥1 using only the equalities and the order chain exists iff ∃ real y_g
   with Σ_g y_g rhs_g = 1, Σ_g y_g |g| = [m odd], and z_k := Σ_{l≤k}(s_l − y_{g(l)}) ≥ 0 for all k
   (s_l = (−1)^{l+1}). Proof: coefficient matching + telescoping (in approach file). This is a
   correct, reusable structural fact — but it is loss-free equivalent to GAP-EXTR, so cannot close
   it alone.
2. **Refutation R14a:** ±1-equality certificates are impossible (proof above, airtight via
   complementary slackness at the box-interior n=4 witness). Records the dead sub-family.
3. **Refutation R14b:** box-free vertices can have ≥2 odd blocks, including at L_T=1 (explicit
   n=4 witness {6,6,4,4,4,4,2,1}); the odd-block-collapse is dead.

## Recommendation to the orchestrator/outliner
The LP-dual/sparse-Farkas LOWER vehicle joins the dead lower families (scalar-reserve, structured
matching, prefix/termwise monovariant, f-partition localisation, canonical-ATT). The dual is
loss-free equivalent to GAP-EXTR with no uniform provable pattern. The LOWER wall needs a
genuinely different framing that is NOT a reframing of "min L_T over the vertex polytope." Two
candidates not yet tried as a PROOF engine: (a) a direct dyadic-scale induction on the measure
identity D = μ{g odd}, ∫g=1 using ONE-REC per scale as a *structural* (not facet, not dual) fact —
the block-parity picture (even blocks = Lemma-P cancelling pairs) reduces L_T to the alternating
sum over odd blocks, but there can be several odd blocks at several scales, so the induction must
track odd-block mass across scales; (b) aimo-0493-style dyadic-tagging bound on how many odd
blocks can co-occur and their forced total ≥ 1. Neither is de-risked; flag honestly.

## Spec concerns
None new. Answer c(n)=2^n/(2^{n+1}−1), minimax D=u_n unchanged and re-confirmed at n=5.
