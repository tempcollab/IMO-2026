## imo-2026-03

Field this round = the two mandated vehicle-switches, one per wall, kept far apart in MECHANISM
(LOWER = explicit global transport certificate; UPPER = global confinement+count+density
invariant). Both explorers independently confirmed there is NO far-apart *second* vehicle per wall
(upper subset-sum-pigeonhole collapses to the same tree-realizable object; lower's only surviving
lever after R10 is matching/transport). Per the single-gap-trap Rule I do NOT double up. A third
slug would be a variation on one of these walls and would share its gap — I decline it deliberately.
parity-measure-potential (1754) is NOT built this round: its entire scalar-reserve family is dead
(R10); it stays live only as a reserve and only if repointed to a non-scalar object (= ballot-matching's
mechanism), so there is nothing new to build there.

---

ballot-matching: revise   (LOWER wall — re-plan GAP-HALL as an explicit transportation min-cut
certificate; supersedes the R8/R10 "prove feasibility abstractly" placeholder)

Target: the whole claim — minimax D = u_n = 1/(2^{n+1}−1), c(n)=2^n/(2^{n+1}−1), both bounds. This
approach's distinct end-to-end route: the lower bound's last residual GAP MID-core is proved by an
EXPLICIT weighted debit→credit transport (a global assignment / min-cut certificate), NOT any scalar
potential (whole family refuted R10). Upper bound imported from the field (whole-tail-peel + U0 close
a₁≥L/2 and m≤n; the valley upper residual is owned by breakpoint-vertex).

Technique: Gale–Hoffman transportation-feasibility / max-flow-min-cut (LP duality for the weighted
Hall condition) as the target theorem; aimo-0129 endpoint-splitting as the scale-by-scale verification
technique; aimo-0341 defect-Hall (maximal-deficient-set peel) as the fallback with the walk's forced
terminal descent as the deficiency budget.

Skeleton:
  1. Import certified reduction: by Lemmas R, M/T, TB, MID, ONE-REC, CLIP the lower bound residual is
     GAP MID-core ⟺ Σ_i c_i w_i ≥ 0 on the descending merge of any a=0 refinement S=F⊔B, where
     w_i = gap lengths, S_i = signed partial sum (+1 for F, −1 for B), c_i = 1[i odd] − S_i.
     Structural facts imported: every c_i is an EVEN integer (S_i ≡ i mod 2); credit set 𝒫={c_i>0},
     debit set 𝒩={c_i<0}; equivalently the CLIP τ=0 transport face Σ_{F even rank}v ≤ Σ_{B odd rank}v.
     — all certified, no re-proof.
  2. CHEAP-KILL PROBE FIRST (do before any flow construction, ~30 min numeric). Exploit that every c_i
     is even (unused handle). Test whether the SIGN PATTERN of c_i plus the forced terminal descent
     (S_m=|F|−|B|<0) already forces Σ c_i w_i ≥ 0 via an aimo-0752-style Abel-summed integrality/slack
     floor — i.e. without a full flow. If a numeric probe on n=3..5 a=0 witnesses shows the even-c_i
     Abel bound holds, promote it to the primary lemma; if it fails (expected, given non-prefix cuts),
     record and proceed to step 3. — Abel summation + integer-gap floor (knowledge_base §NT).
  3. State the transport target as a min-cut (the HONEST feasibility statement, and the explanation of
     why every scalar Φ(τ) failed): the debit→credit transport saturating all debit within credit
     capacity exists iff for EVERY debit-index set X (not just prefix/threshold sets), the credit
     reachable from X under the ladder adjacency has total capacity ≥ debit(X). — Gale–Hoffman /
     LP-duality for transportation problems, stated as a named classical fact (NOT in knowledge_base;
     cite explicitly per "name your tools").
  4. Define the ladder adjacency explicitly: a debit index i (walk ≥2 above baseline = F ran ahead
     among the top i pieces) is adjacent to the credit created by the next forced B-crossing (a −1
     step) at the SAME or COARSER dyadic scale. Lemma ONE-REC caps each dyadic scale-group G_j to ≤1
     F-fragment, so the debit that can accumulate before the next forced crossing is bounded by that
     one fragment's mass.
  5. Verify the min-cut condition by aimo-0129 endpoint-splitting (the verification technique, NOT a
     new object): given any hypothetical violating debit set X, split it at its COARSEST dyadic-scale
     member i* (the endpoint analogue). Bound the credit reachable from {i∈X : scale(i)≤j*} using
     ONE-REC's ≤1-fragment cap on scale j* alone; recurse to X minus its scale-j* part, which is a
     violating set for the STRICTLY SMALLER sub-ladder (ONE-REC part (i): scale-truncation B_{≤ℓ} is
     itself an admissible refinement of C_ℓ). — strong induction on dyadic scale, packaged as an
     endpoint split.
  6. Terminal absorption (aimo-0341 defect-Hall fallback if step 5's per-scale bound leaves residual
     debit): peel the MAXIMAL deficient band-cluster W as a single unit, delete W∪N(W), Hall holds on
     the complement (else W could be enlarged); the forced terminal descent S_m=|F|−|B|<0 is literally
     the deficiency term def(G) — every unpaired debit has a guaranteed home at the bottom scale.
  7. Conclude Σ c_i w_i ≥ 0 ⇒ D(S)≥1 ⇒ minimax D=u_n (with the imported upper bound).

Key lemmas (claim + mechanism):
  - HALL-ENDPOINT (make-or-break): every violating debit set, split at its coarsest dyadic scale j*,
    has neighborhood credit ≥ its debit — because ONE-REC forces ≤1 F-fragment inside scale-group G_j,
    so the debit accruing before the next ladder-forced B-crossing is at most that one fragment's mass,
    which the crossing's −1 step repays; recursion on the truncated sub-ladder closes the rest.
  - GAP-TERMINAL: the transport is TOTAL (no debit unmatched at the bottom) — because the walk must end
    net-negative (S_m=|F|−|B|<0, since B refines the full ladder so |B| ≥ ladder length ≥ |F|), so the
    terminal descent supplies guaranteed credit = the def(G) budget of defect-Hall.
  - EVEN-c_i FLOOR (cheap-kill candidate, step 2): every c_i∈2ℤ, so Σ c_i w_i is a signed even-integer-
    weighted length sum; combined with S_m<0 an Abel-summed integrality bound MAY already force ≥0.
    (Probe; not assumed a theorem.)

Open gaps (the builder fills):
  - GAP-HALL / HALL-ENDPOINT — the make-or-break per-scale neighborhood-credit ≥ debit bound (step 5).
  - GAP-TERMINAL — rigorous terminal absorption (step 6).
  - FIRST ACTION (before either): construct ONE fully explicit transport map by hand / small LP
    (scipy.optimize.linprog or max-flow) on the sharpest known adversarial instance, the n=7 CLIP
    witness F={63.0119, 62.8559, 2.1322} with its 12-piece B, AND on n=3..5 random a=0 witnesses.
    The field has NO worked matching instance yet — exhibit the actual debit→credit assignment before
    the general proof. This empirically locates the true min-cut (prefix vs union-of-bands).

Cases to cover: a=0 (top-shredded) refinements with |F|≥3 only (|F|=2, 0≤g≤1, a≥1, Case (a),
trivial regime all closed and imported). Within that: the min-cut may sit on a NON-PREFIX set (union
of dyadic bands with an untouched gap between) — the certificate MUST handle non-prefix cuts (this is
exactly why the R10 n=7 witness broke every scalar Φ(τ), which only tests prefix cuts).

Watch out for:
  - RECURSION-COLLAPSE (the single-gap trap in disguise, flagged by the explorer). If the endpoint-
    split is unrolled as a literal induction on n via ONE-REC scale-by-scale, it becomes the SAME
    recursive skeleton as parity-measure-potential and dies on the same wall. The genuinely distinct
    content must be an EXPLICIT transport map (or explicit min-cut description) checkable by inspection
    on any instance — NOT an inductive proof that merely invokes Hall's name. If the build reduces to
    "induct on n," it has failed to switch vehicles.
  - Do NOT re-propose any scalar potential Φ(τ) (whole family refuted R10, prefix-cut-only, κ unbounded).
  - Do NOT assume the adjacency is bounded-degree/regular (aimo-0197 analogy is WEAK: the debit/credit
    graph is not regular here; check but do not rely on it).

---

breakpoint-vertex: revise   (UPPER wall — re-plan GAP U-cover as a global confinement×count×density
invariant on the reachable set; supersedes the R10-refuted fixed-depth move lemma)

Target: the whole claim — for every n, largest guaranteed c is c(n)=2^n/(2^{n+1}−1), minimax D=u_n,
both bounds. Distinct end-to-end route: the upper bound's last residual GAP U-cover (does the
descending include/skip reachable set R_{n+1} meet [0,u_nL]?) is closed by a GLOBAL density/pigeonhole
invariant on R_i — a joint (confinement × count × local-density) strengthened induction — NOT any
recursion/greedy (R9-refuted) and NOT any fixed/bounded-depth move lemma (R10-refuted, required depth
Θ(n)). Lower bound imported from the field (VERT + TB close it down to GAP L-fin, owned by the lower
vehicle).

Technique: strengthen-the-induction-hypothesis (Pólya "Generalize") — a 3-parameter joint invariant
on the reachable set R_i = R_{i-1} ∪ {|v−a_i| : v∈R_{i-1}}; confinement bound + injective count +
local density near the next pivot, telescoped to a small VALUE (not merely a small gap). Pigeonhole /
extremal principle + Erdős–Szekeres injectivity-coordinate shape (knowledge_base §Combinatorics).

Skeleton:
  1. Import certified: VERT (optimal Xiang refinement is an LP vertex, ≤n+1 distinct values), RL
     (achievable leftovers 𝓡(A) = tree-realizable signed subset sums, respecting the tree constraint),
     BL (first crossing lands r∈[0,β_nL)), ESF-1/ESF-2 (subset-caterpillar realizability = the R_i
     recursion), U0 (m≤n ⇒ D=0), whole-tail-peel (a₁≥L/2 closed). Residual = GAP U-cover in the
     balanced valley {m=n+1, a₁<L/2, a₂<β_nL}: show R_{n+1} meets [0,u_nL].
  2. CONFINEMENT lemma (new, cheap — certify first, it costs nothing and sharpens every later interval).
     For all i: max(R_i) ≤ a₁. One-line strong induction: |v−a_i| ≤ max(v,a_i); inductively v≤a₁ and
     a_i≤a₁ (sorted), so max(v,a_i)≤a₁; base max(R_1)=a₁. Hence R_{n+1} ⊂ [0,a₁) ⊂ [0,L/2). This is
     NOT the refuted ρ_i≤a_i/2 covering-radius; it is a clean global confinement. Certifiable now.
  3. COUNT lemma: |R_i| = 2^i (the include/skip map is injective on valley profiles). A collision
     |v−a_i| = an existing element requires v+w=2a_i or v=a_i±w for some pair v,w∈R_{i-1} — a finite,
     checkable per-step condition; the valley caps a₁<L/2, a₂<β_n are conjectured to be exactly what
     rule these out. ADVERSARIAL CHECK REQUIRED before building on it (RANDOM-only evidence so far,
     1200+ profiles, |R_{n+1}|/2^{n+1}=1.000). Gap.
  4. Density: 2^{n+1} distinct points confined to [0,a₁) ⊂ [0,L/2) give 2^{n+1}−1 gaps averaging
     < L/(2(2^{n+1}−1)) = u_n·L/2, so some consecutive pair of reachable values is ≤ u_n·L/2 apart.
     — pure pigeonhole on gaps.
  5. GAP→VALUE conversion (the make-or-break — pigeonhole ALONE is insufficient, recorded R10: a small
     GAP between two reachable points is NOT a small element, and the budget is exhausted so no extra
     move takes the difference). Two routes to try, in order:
       (a) Show the near-0 gap occurs ADJACENT to 0 — i.e. min(R_{n+1}\{0}) itself is ≤ u_nL, not just
           some interior gap. Anchor: R_i always contains 0 (empty include), and BL already lands a
           first value r<β_nL; track the smallest positive reachable value m_i := min(R_i\{0}).
       (b) 3-parameter JOINT induction (confinement × count × local density near the pivot). Bound
           m_i using not the single closest point of R_{i-1} to a_i but the LOCAL DENSITY of R_{i-1}
           in a shrinking window around a_i: since 2^{i-1} points are spread over [0,a₁), several
           candidate |v−a_i| are small simultaneously, and only ONE must survive unspent to step n+1.
           Telescope the joint invariant to m_{n+1} ≤ u_nL.
  6. Conclude min(R_{n+1}) ≤ u_nL ⇒ (R-UV, ESF-2) Xiang forces D≤u_nL in the valley ⇒ (with imported
     a₁≥L/2 and m≤n) minimax D=u_n.

Key lemmas (claim + mechanism):
  - CONFINEMENT: max(R_i)≤a₁ for all i — because |v−a_i|≤max(v,a_i) and both v,a_i ≤ a₁ (v by IH, a_i
    by sorting). Cheap, provable, certify this round even though it alone doesn't close the gap.
  - COUNT: |R_{n+1}|=2^{n+1} (injective include/skip) — because a collision forces v+w=2a_i for a pair
    in R_{i-1}, which the valley caps a₁<L/2, a₂<β_n exclude. VERIFY ADVERSARIALLY first (not a theorem
    yet — random-only; the problem's history has produced false "always true" from random sampling).
  - GAP→VALUE (the crux): the ≤u_n·L/2 gap can be realized AS a reachable value near 0, via a joint
    confinement×count×local-density induction on m_i=min(R_i\{0}) — because local clustering of the
    2^{i-1} confined points near each pivot a_i produces several small |v−a_i| simultaneously and one
    survives unspent. OPEN — this is the make-or-break.

Open gaps (the builder fills):
  - GAP-COUNT — adversarially verify then prove |R_i|=2^i (the injectivity/collision-exclusion from
    the valley caps).
  - GAP-U-cover / GAP→VALUE — the confinement+count+density joint invariant telescoping to a small
    VALUE m_{n+1}≤u_nL (step 5). This is the actual residual.
  - CONFINEMENT (step 2) is immediately provable and should be certified as a shared lemma this round.

Cases to cover: balanced valley {m=n+1, a₁<L/2, a₂<β_nL} only (dominant a₁≥L/2 closed by whole-tail-peel;
m≤n closed by U0). Value 0 is admissible (even cancellation), so "meets [0,u_nL]" includes reaching 0
exactly — the near-all-equal sub-case where R_{n+1}∋0 is handled by that.

Watch out for:
  - THE GAP≠VALUE SUBTLETY (explorer's explicit caveat, recorded R10). Do NOT present the step-4
    pigeonhole as a full proof — it yields a small gap between two reachable points, not a small
    element, and the budget is exhausted so no move can take that difference. The GAP→VALUE conversion
    (step 5) is mandatory; a build that stops at step 4 is incomplete, not solved.
  - Do NOT assume COUNT/injectivity is a theorem — adversarial/deterministic search first (standing
    rule: verify surprising numeric claims with a fine/adversarial search, random sampling has misled
    this problem before).
  - Do NOT re-propose any fixed/bounded-depth move lemma (R10, required depth Θ(n)) or any single-pass
    greedy/recursion (R9, overshoot ≤11.4×). The invariant must be GLOBAL.
  - Do NOT re-propose ρ_i≤a_i/2 covering-radius alone (R10, saturates at a_{n+1}/2≫u_n; natural
    induction only gives a_{i-1}/2). CONFINEMENT (max(R_i)≤a₁) is the distinct, provable replacement.

---

Build set: ballot-matching, breakpoint-vertex   (exactly two builders, one per wall — do NOT double
up per the single-gap-trap Rule; parity-measure-potential held as non-scalar reserve only).
