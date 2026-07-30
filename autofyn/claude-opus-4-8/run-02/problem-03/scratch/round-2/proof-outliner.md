## imo-2026-03

Shared context: the full spine is CERTIFIED (Lemma G, level-measure identity `D=λ{t:#pieces>t
odd}`, cut-flip; `lemmas/greedy-claim.md`, `lemmas/cut-flip.md`), the game is exactly reduced
to the discrepancy minimax `D* = max_Liu min_Xiang D = u = 1/(2^{n+1}−1)`, n=1 is fully solved,
and lower-bound Case A (top piece uncut ⇒ D≥u) is certified. Two shared walls remain: GAP L
(lower, Case B — top piece cut) and GAP U (upper, general n — Xiang's non-myopic ≤n-cut rule).
The three round-1 approaches all attack via explicit-strategy / explicit-cancellation in the
D-language, so they share both walls. Round 2 puts a genuinely different framing on the table
(concavity-lp) to break the shared-gap collapse, and re-mechanises the two stuck gaps after the
explorers REFUTED the previously-planned mechanisms.

---

concavity-lp: new
Target: `c(n)=2^n/(2^{n+1}−1)` end to end (both bounds), via `D* = u`.
Technique: piecewise-affine / LP-vertex structure ⇒ `f(p):=min_Xiang D` is CONCAVE on the Liu
partition simplex ⇒ a single first-order (KKT/subgradient) certificate at the dyadic partition
proves it is the global max. One local finite check replaces GAP U's per-partition case analysis
AND re-derives the lower bound — both bounds, one mechanism. This is the far-from-the-field
framing the shared-gap rule demands (no other approach invokes concavity or LP-vertex structure).
Skeleton:
  1. Reduce to `D*=u` — CERTIFIED spine (import).
  2. Vertex-optimality: `min_{≤n cuts} D = min_{S∈𝒮} g_S(p)`, `g_S` affine in `p`, `𝒮` finite —
     by cut-flip each free cut coord has slope ∈{0,±2}, optimum at a tie/pin boundary.
  3. Concavity: `f = min_S ĝ_S`, each `ĝ_S` a GLOBAL affine functional with `ĝ_S ≥ f` (envelope)
     ⇒ `f` concave on the simplex `Δ`.
  4. `f(dyadic)=u` — Case A (certified `D≥2b₁−1`) + explicit "all cuts on top"/"bisect pairs".
  5. KKT certificate at dyadic: convex weights `λ_S` over active strategies with `Σλ_S∇ĝ_S`
     CONSTANT (⊥ simplex tangent) ⇒ no feasible direction raises `f` (Gordan/LP duality).
  6. Concave `f` + stationary interior point ⇒ global max = u ⇒ `c(n)=(1+u)/2`. ∎
Key lemmas (claim + mechanism):
  - Affine-per-order-type — because `D=Σ ε_r·(length)` with the sign pattern `ε` fixed within
    one sorted order-type, so `D` is signed-linear in Liu lengths + cut positions.
  - Vertex-optimality — because a free cut coordinate has D-slope ∈{0,±2} (cut-flip), so it can
    be pushed to its order-type boundary without raising D; iterate over the ≤n disjoint cuts.
  - Global affine envelope `ĝ_S ≥ f` — because applying a FIXED strategy `S` to any `p` is a
    legal (not necessarily optimal) Xiang response, so its affine value dominates the min.
  - Constant-subgradient certificate — because `∇ĝ_S` is the effective sign-vector `ε^S`; the
    active responses at dyadic combine convexly to a constant (n=1: avg of "bisect big" and
    "pin median" gradients — reproduces the certified `p=1/3`).
Open gaps: C1 vertex-optimality for ≤n SIMULTANEOUS cuts (single-cut is a cut-flip corollary;
joint LP-vertex/finiteness is the work); C2 GLOBAL concavity over all of Δ (envelope extension +
control of reachable-order-type blow-up — lean on `ĝ_S≥f`, which needs no exact cell map); C3 the
KKT certificate at dyadic for general n (finite per n; the uniform-in-n active set + weights are
the hard step).
Cases to cover: interior maximizer only (dyadic strictly-sorted, all-positive ⇒ only Σp=1 active);
Liu `<n` marks = dominated face (certified D=0<u, skip KKT); n=1 consistency check first.
Watch out for: keep `ĝ_S ≥ f` (NOT `=`) — that inequality IS what gives concavity; missing an
active tie at dyadic breaks the constant-gradient combo (both "all-cuts-on-top" and "bisect-pairs"
appear active — include both); confirm dyadic is interior so no positivity/sorting multipliers.

induction-recursion: revise
Target: `c(n)=2^n/(2^{n+1}−1)` — this approach owns the lower bound Case B route (and carries the
upper bound as its own GAP-UB).
Technique: self-similar induction on n; unchanged route (top piece + scaled (n−1)-dyadic bottom).
REVISION: the round-1 gap mechanism — the STRICT bound `W(n−1,b) > u_{n−1}` for `b<n−1` — is
REFUTED (explorer: `b=1<n−1=2` at n=3 attains D=u EXACTLY). Replace it with an EXACT-VALUE
minimax recursion robust to equality.
Skeleton (revised gap only; spine + Case A unchanged, certified):
  1..5. (unchanged) reduction, Case A certified, Case-B exact identity
        `D = λ(O_top)+λ(O_bot)−2λ(O_top∩O_bot)`, `λ(O_bot)≥u` by scaled IH.
  6. Define `V(n,k):=min_{≤k cuts} D` on the n-dyadic; prove `V(n,n)=u_n` by strong induction via
     an EXACT recursion (not an inequality), split budget `k=a+b`, bottom = `σ·V(n−1,b)`.
Key lemmas (claim + mechanism):
  - Exact recursion `V(n,n)=u_n` — because equality is attained on a FLAT family of allocations,
    so a value recurrence closes where a strict inequality has vanishing slack; mirrors
    `u_n=u_{n−1}/(2+u_{n−1})`.
  - Rank-interleaving (recommended sub-mechanism) — because Lemma G makes D the alternating sum
    over the MERGED sorted order; tracking the T/B label string (top-descendants ≤g_n, bottom ≤
    g_n/2) bypasses the opaque `2λ(O_top∩O_bot)` cancellation term entirely.
Open gaps: GAP-LB.1 (interleaving recursion: signed merged-order sum ≥ u for all a+b≤n) OR
GAP-LB.2 (canonical-form exchange: any Case-B response transforms without decreasing D into the
self-similar split giving exactly u). GAP-UB (general upper bound) still open — defer to
dyadic-discrepancy / concavity-lp; do not duplicate.
Cases to cover: base n=0,1 done; Case A certified; Case B via the exact recursion; Liu `<n` marks
handled (bisect all ⇒ D=0).
Watch out for: do NOT chase the strict inequality again (refuted); the value is TIGHT with
equality on a family — any bound must be non-strict/equality-robust; keep the recursion on the
interleaving invariant, not on `O_top,O_bot` separately.

dyadic-discrepancy: advance
Target: `c(n)=2^n/(2^{n+1}−1)` — leader; owns direct constructive strategy for GAP U.
Technique: explicit adaptive Xiang strategy in the D/level-measure language.
Skeleton (advance GAP U with the round-2 concrete strategy; spine + Case A certified):
  1..3. (certified/unchanged) reduction, n=1 full, Case A.
  4. Xiang plays CLOSE-THE-LARGEST-PAIRING-GAP: pair sorted pieces (b1,b2),(b3,b4),…; each cut
     equalises the currently-largest pairing gap / pairs off the odd leftover; recurse on the
     updated order. Prove ≤n cuts give `D ≤ u` for every Liu partition.
Key lemmas (claim + mechanism):
  - Gap-greedy optimality (U.a) — exchange argument: no ≤n-cut allocation beats closing the
    largest pairing gap first (KB extremal principle / smoothing).
  - Residual ≤ u (U.b) — budget-vs-pieces pigeonhole in GAP form: n cuts for ≤n+1 pieces leaves
    exactly one pairing un-closed, residual gap ≤ u (on pairing-form gaps `b_{2i−1}−b_{2i}`, NOT
    literal equal tiers — that is why bisection-only fails).
Open gaps: GAP U = (U.a)+(U.b) above — strategy now concrete, the `D≤u` bound unproven. GAP L
(Case B) also open here; defer to induction-recursion.
Cases to cover: top-dominant regime (⇒ recursively split top), near-balanced regime (⇒ subdivide
small odd-leftover), ties, m<n+1, n=1 (reproduces certified threshold rule).
Watch out for: "cut only the top piece" is REFUTED as a universal rule (fails on near-balanced,
0.1615>1/7) — the strategy MUST be the regime-adaptive gap-greedy, not top-only; myopic
"reduce-D-most" is dead; greedy must be on GAPS, not on per-cut D reduction.

potential-certificate: RETIRE (recommendation to reviewer)
Rationale: it is the weakest near-duplicate — after its round-1 pivot it uses the SAME order-aware
level-set certificate as the other two and shares their exact GAP U/GAP L walls, so as a live
whole-problem attempt it adds no diversity. Its one distinct deliverable (NO separable per-piece
potential can certify the odd-rank functional — clean witness + LP infeasibility) is a COMPLETED
certified dead-end result, already recorded; nothing is lost by retiring. Its cut-budget/level-set
machinery is already certified and shared. Retiring it frees the slot so the field stays three
genuinely-distinct live framings (concavity-lp = LP/duality, induction-recursion = self-similar
induction, dyadic-discrepancy = explicit adaptive strategy) rather than four with a duplicate.
Alternative if the reviewer prefers to keep it live: repoint it to the rank-interleaving GLOBAL
framing (merged T/B label-string signed sum) for BOTH bounds — genuinely distinct from
induction-recursion's O_top/O_bot cancellation — but my recommendation is RETIRE.

---

Recommended field for ranking:
  - concavity-lp — NEW (the far-from-field framing that breaks the shared GAP U/GAP L wall)
  - induction-recursion — REVISE (swap refuted strict-inequality for exact-value recursion, GAP L)
  - dyadic-discrepancy — ADVANCE (concrete non-myopic close-the-largest-gap strategy, GAP U)
  - potential-certificate — RETIRE (near-duplicate; distinct result already banked)

Build-set suggestion (reviewer decides): concavity-lp (new, highest-leverage — one mechanism for
both bounds), induction-recursion (revised GAP L), dyadic-discrepancy (advance GAP U).
