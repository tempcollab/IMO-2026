## imo-2026-03 (lens: generating-function / potential-free transform reformulation)

- Distinct openings:
  1. **The Z-transform unification (LOWER wall, new object).** Define, for the certified MID
     setting (g = N_F−N_B on (0,L), L=2^{n-1}), the one-variable transform
     `Z(z) := ∫_0^L z^{g(t)} dt` (well-defined for z≠0 since g is a piecewise-constant
     integer-valued step function; for z<0 read z^g via sign(z)^g·|z|^g, or just work with the
     equivalent finite sum over the segments of constancy — no branch issues since g∈ℤ).
     Then:
     - `Z(1) = L` (trivial, total length).
     - `Z'(1) = ∫_0^L g(t) dt = 1` — this is exactly certified **Lemma MID part (b)** (the mass
       identity ΣF−ΣB=1), recovered as the *derivative at z=1*.
     - `Z(-1) = ∫_0^L (-1)^{g(t)} dt = L − 2·μ{g odd}` — so **GAP MID-core** (`μ{g odd} ≥ 1`) is
       *exactly* the statement `Z(-1) ≤ L−2`.
     So the two certified halves of Lemma MID (mass identity + parity-measure identity) become
     the value and derivative of ONE analytic object at z=1, and the open residual becomes a
     single evaluation `Z(-1) ≤ L−2`. This is the roots-of-unity/character-sum move (the
     `1[g odd] = (1−(−1)^g)/2` character), generalized from the discrete mod-2 tuple-counting
     setting (see crux aimo-0155 below) to a continuous integral-of-a-step-function setting. It
     is a genuinely different TOP-LEVEL OBJECT from the vertex-polytope / LP-dual / word /
     matching objects (all six dead): it is a transform of the *whole* configuration, not a
     vertex, not a scalar running potential over τ, not a matching. **This does NOT trivially
     violate the "no additive scalar reserve" ban** — Z(z) is a fixed global functional
     evaluated at a fixed point z=−1, not a running/foresight potential Φ(τ) over a moving
     threshold τ; it has no free parameter to tune along a scan.
  2. **Recursive/self-similar functional-equation opening.** B is itself (by certified Lemma
     ONE-REC / recursed-dyadic-dichotomy) a refinement of C_{n-1}, hence recursively splits as
     `B = F_B ⊔ B_B` with `F_B` = fragments of the top piece 2^{n-1} of C_{n-1} (ΣF_B = L) and
     `B_B` a refinement of C_{n-2}, confined to (0, L/2). This gives a **two-band structure**: on
     `(L/2, L)`, `g(t) = N_F(t) − N_{F_B}(t)` (B_B pieces are all ≤ L/2, invisible up there); on
     `(0, L/2)`, `g(t) = [N_F(t) − N_{F_B}(t)] − N_{B_B}(t)`. This is exactly the certified
     **top-band-decomposition (TB)** content, now recast as a candidate for a *product/recursive
     formula* for Z(z) (Z_n(z) in terms of an "upper-band factor" and a residual `Z_{n-1}`-type
     object on the smaller scale). This is the closest thing to a genuinely new recursive lever
     — self-similar induction on n via a transform identity, not via vertex/matching machinery.
  3. **A discrepancy/exponential-sum framing of the SAME object**, importing "roots-of-unity
     filter" technique (aimo-0155) more literally: since B is a fixed dyadic ladder recursively
     built from doublings, `Z(z)` for the extremal/worst F might telescope via a product formula
     analogous to `∏(1+z^{2^k})`-type dyadic generating functions (binary-expansion generating
     functions), which are classical and have known root-of-unity behavior. Untested — flagged
     as a thing to try, not confirmed.

- Candidate technique(s): roots-of-unity/character-sum filter (turn a parity indicator into an
  evaluation at z=−1 of a generating transform); combined with the already-certified dyadic
  self-similarity (ONE-REC / TB) to attempt a recursive functional equation for `Z_n(-1)` in
  terms of `Z_{n-1}(-1)`. This is a genuinely different vehicle from the ranked-word/vertex
  polytope, LP-dual, matching, and scalar-potential-over-τ families — but it is built from
  exactly the same certified facts (Lemma M, MID, ONE-REC, TB), so there is real risk it is just
  those facts in new notation (see "where it breaks" below).

- Cheap-kill candidates: **Test whether Z(-1) obeys a clean two-band recursive formula** (e.g.
  `Z_n(-1) = f(F, F_B) · (something involving Z_{n-1}(-1) on the sub-ladder)`) on a handful of
  explicit n=3,4,5 witnesses before investing further — if no such recursion exists (the top-band
  and bottom-band Z-values don't combine multiplicatively/additively in a closed way), the
  transform reformulation reduces to a tautological restatement of already-certified MID, and
  should be abandoned quickly (same failure mode as the LP-dual "reframing not reduction"
  diagnosis of R14).

- Knowledge-base entries to use: none in `knowledge_base.md` named "generating function" /
  "roots of unity" (grep returned nothing) — this technique must be imported wholesale from the
  crux corpus, not cited from the KB. Certified lemmas MID, M (measure-identity), ONE-REC
  (recursed-dyadic-dichotomy), TB (top-band-decomposition) are the exact certified facts the
  transform repackages.

- Analogous past problems (cruxes): filtered `domain=combinatorics`/`algebra`,
  `subtopic=generating-functions` (12 cruxes total). Best match:
  - **aimo-0155** (`subtopic=generating-functions`, combinatorics): "Encode a parity-weighted
    count under a modular sum-constraint as a signed generating function run through the
    roots-of-unity filter, turning the even-minus-odd difference into one sum over the modulus's
    roots of unity." Problem: color 75/100 elements red, ask which n make ≥half of the
    sum-≡0-mod-100 n-tuples have an even number of red coordinates. Crux move: `X−Y =
    (1/100)Σ_ω (B(ω)−R(ω))^n` over 100th roots of unity, exploiting `R(ω)+B(ω)=0` for ω≠1. This
    is the closest analogue to opening (1) above — the "extract even/odd via evaluation at −1 (or
    roots of unity)" move — but the underlying combinatorial engine (a discrete alphabet {1..100}
    with an honest finite abelian group / DFT structure) is quite different from our continuous
    step-function-on-a-dyadic-ladder setting; the analogy is at the *level of the trick*
    (roots-of-unity filter for parity), not at the level of the combinatorial object. Genuinely
    useful as the naming/justification of the move, not as a template to copy verbatim.
  - Other 11 generating-function cruxes (aimo-0001 q-analog permutation statistics, aimo-0050
    bivariate torus polynomial, aimo-0509/aimo-0649/aimo-0685/aimo-0855/aimo-0966) are all
    discrete-alphabet / polynomial-coefficient arguments (roots-of-unity filters mod m, Nullstellensatz,
    cyclotomic divisibility) — none directly resembles a continuous integral-of-a-step-function
    parity-measure inequality with a *fixed real-valued* dyadic ladder constraint. None is a
    strong template; they only confirm the "roots-of-unity/character parity trick" is a known,
    reusable move, which supports opening (1) but does not hand it to us pre-solved.
  - Checked `games-and-strategy` and `extremal-principle`/`invariants-and-monovariants` subtopics
    briefly via the run's prior explorer history (rounds 1–14 already mined those heavily for
    this exact problem); did not re-query, per dispatch to focus on the generating-function lens.

- Prior progress: unchanged from `current.md` — answer confirmed `c(n)=2^n/(2^{n+1}−1)`,
  `D=u_n=1/(2^{n+1}−1)`. 29 certified lemmas stand. LOWER wall = GAP MID-core / GAP-EXTR
  (`μ{g odd}≥1` for `|F|≥3`, ⟺ min L_T≥1 at every vertex), de-risked true to n=5, **no live
  vehicle** (6 lower families dead). UPPER wall = first-gap pigeonhole `μ_{n+1}≤u_n`, proven
  asymptotically tight with NO margin (VALLEY-TIGHT), 6 upper families dead including
  mass-telescope discrepancy (R13) — the closest prior attempt to a "transform" idea for the
  upper wall, already dead.

- Dead ends (do not retry, per run_state Rules — verified consistent with certified lemma files):
  additive scalar reserve/potential over τ (R9/R10, incl. clean mass-above Φ(τ), CLIP-certified as
  exact-but-insufficient — κ unbounded in n); structured transport/matching (R11); prefix/termwise
  monovariant (R8); f-partition single-gap localisation (R12); the entire vertex-polytope/LP-dual
  framing (R12/R14, DUAL-CHAR proves any certificate ⟺ GAP-EXTR — reframing not reduction);
  covering-radius one/two-cap, dispersion/density/COUNT, greedy recursion, bounded-depth escape,
  mass-telescope discrepancy, margin/extremal-tie (all UPPER, R9–R14). **Important note for the
  outliner**: the Z(z) transform I'm proposing evaluates `Z(-1)` — a SINGLE fixed point, not a
  scan over τ — so it is not literally the banned "additive scalar reserve Φ(τ)"; but if the only
  way to bound `Z(-1)` turns out to be via the τ-derivative machinery (essentially CLIP/OSR
  restated), it inherits the same "κ unbounded" failure mode. This must be checked early by the
  builder, not assumed away.

- Small-case / intuition notes (numeric, sympy/exact-fraction; all CONJECTURE-level confirmation
  of identities, not proofs of the open inequality):
  - Verified exactly (Fraction arithmetic) on 4 explicit n=3,4 witnesses (`F={3,3,2},B=C_2`;
    `F={7,6,3},B=C_3` plain and refined `8→{5,3}`; `F={5,5,5,1},B=C_3`; `F={6,6,4}`,
    `B` refined `4→{2,2},8→{4,4}`): in every case `Z'(1)=∫g=1` exactly and
    `μ{g odd}=(L−Z(-1))/2` exactly — the Z-transform identity holds as expected (it is an exact
    algebraic restatement of certified Lemma M + MID, so this is not surprising, just a sanity
    check that the bookkeeping is right).
  - I did NOT find (in the time budget) a clean closed-form recursive/product formula for `Z_n(-1)`
    from the two-band split (opening 2/3) — this is the actual make-or-break test the next
    round's builder must run FIRST, before investing in the transform framing. If it fails
    (no clean recursion), this opening likely collapses to a notational repackaging of
    already-certified MID/TB, the same fate as the vertex-polytope and LP-dual reframings.
  - The make-or-break claim to hand the outliner: **does `Z_n(-1)` (equivalently `μ_n{g odd}`)
    satisfy a genuine recursive inequality/identity in terms of `Z_{n-1}(-1)` restricted to the
    sub-ladder `(0,L/2)`, driven by the top-band value `N_F(t)−N_{F_B}(t)` on `(L/2,L)`?** If yes,
    this is a NEW induction vehicle (transform-based, distinct from vertex/matching/potential) for
    GAP MID-core. If no — if the cross term between the top band and the recursive bottom band
    is exactly as intractable as the SPLIT cross-term `μ(O_F∩O_B)` that MID was originally built
    to eliminate — then this framing should be abandoned quickly, consistent with the run's
    repeated "reframing not reduction" pattern.
  - For the UPPER wall: I could NOT find a natural way to apply the same Z-transform (it is built
    on the STATIC parity-measure object `D(S)=μ{N odd}`, not on the ADAPTIVE tree-realizable
    reachable-set object that the upper wall needs). The upper wall's closest prior attempt at a
    "transform" idea (mass-telescope discrepancy, R13) is already dead. I would flag the upper
    wall as NOT well-served by this lens — recommend the outliner keep the upper wall on
    breakpoint-vertex/an exact-tight lever (per the R15 dispatch's item (iii)), and use this
    generating-function opening ONLY for the LOWER wall.
