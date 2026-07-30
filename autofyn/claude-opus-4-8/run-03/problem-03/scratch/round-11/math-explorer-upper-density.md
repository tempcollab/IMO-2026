## imo-2026-03 (lens: UPPER wall as restricted density/pigeonhole among tree-realizable signed subset sums)

- Distinct openings (all target GAP U-cover: R_{n+1} meets [0,u_n], u_n=1/(2^{n+1}-1)):
  1. **Confinement lemma (new, cheap, provable — do this first).** For the descending
     include/skip DP `R_0={0}, R_i=R_{i-1}∪{|v-a_i|:v∈R_{i-1}}` (sorted `a_1≥…≥a_{n+1}`), a
     one-line strong induction gives **max(R_i) ≤ a_1 for every i**: `|v-a_i| ≤ max(v,a_i)`,
     and inductively `v≤a_1`, `a_i≤a_1` (since `a_i` is sorted below `a_1`), so `max(v,a_i)≤a_1`.
     Base `max(R_1)=a_1`. This is NOT in the current lemma set (only the weaker `ρ_i≤a_i/2`
     covering-radius on `[0,a_i]` was tried/refuted-as-insufficient) — a clean global bound
     `R_{n+1}⊂[0,a_1)⊂[0,L/2)` for ALL i simultaneously, easy to certify, worth adding as a
     lemma even though it alone doesn't close the gap (see caveat below).
  2. **Count-doubling / injectivity strengthening (the genuinely new lever for this lens).**
     Numerically (see Small-case notes) `|R_{n+1}|=2^{n+1}` EXACTLY on every one of 1200+ random
     valley profiles tested (n=3..6) — i.e. the include/skip map is *injective* (no accidental
     coincidences) on valley profiles, so `R_{n+1}` genuinely has `2^{n+1}` distinct points
     packed into `[0,a_1)` with `a_1<L/2`. Combined with opening 1, this gives by a **pure
     pigeonhole on gaps** (2^{n+1} points spanning an interval of length `<L/2`, hence
     `2^{n+1}-1` gaps averaging `<L/(2(2^{n+1}-1)) = u_n·L/2`): SOME pair of *consecutive*
     reachable values is `≤u_n·L/2` apart. **Caveat (must flag to outliner): this only proves a
     small GAP between two elements of R_{n+1}, not a small MINIMUM element** — the budget is
     already exhausted (all n+1 pieces used), so there is no extra move available to take that
     pair's difference. This is exactly the subtlety that makes the naive pigeonhole insufficient
     and is the real content still missing: a proof must show the near-0 gap actually occurs
     *adjacent to 0* (or a genuinely different argument that produces a *value*, not a gap).
     Still, injectivity + the a_1-confinement is new usable structure not previously in the
     approach file — the natural next move is to try to prove `|R_i|=2^i` by induction (when can
     `|v-a_i|` coincide with an existing element of `R_{i-1}∪{|w-a_i|}`? only if `v+w=2a_i` for
     some pair, or `v=a_i+w`/`v=a_i-w` — a genuinely checkable, finite condition per step) and
     see whether the valley caps `a_1<L/2, a_2<β_nL` are exactly what rule out collisions.
  3. **Recursive minpos tracking (an alternative to covering radius).** Define
     `m_i := min{R_i \ {0}}` (smallest positive reachable value after `i` steps). `m_i ≤
     dist(a_i, R_{i-1})` always (take `v∈R_{i-1}` closest to `a_i`; `|v-a_i|` is small).
     This is essentially the R10 `ρ_i` covering-radius idea reused with the target point fixed
     at `a_i` instead of "any t"; it was refuted as insufficient ALONE (saturates at
     `a_{n+1}/2≫u_n`). The genuinely unexplored refinement: bound `m_i` using not just the
     *single* closest point but the **local density of R_{i-1} in a neighborhood of `a_i`** —
     since `|R_{i-1}|=2^{i-1}` points are spread over `[0,a_1)` (opening 2), if several of them
     cluster within a shrinking window around `a_i`, then several candidate `|v-a_i|` values are
     small simultaneously; only ONE needs to survive to the end without being "spent." This is a
     genuine two-parameter (count × confinement) induction, not yet formulated as a clean
     invariant — flag to outliner as the concrete next attempt, distinct from both the refuted
     `ρ_i≤a_i/2` and the refuted bounded-depth move-search.
  4. **Complete-sequence / Euclidean-algorithm framing.** Lemma BL's mechanism (`r<s_k≤a_2`, no
     abs-flip while running value stays ≥0) is exactly the classical fact that a *descending
     caterpillar* on a sequence obeying a "complete sequence" condition (each term ≤ sum of the
     smaller remaining terms, roughly) stays bounded by the next term used — a Euclidean-algorithm
     flavor. The valley profile does NOT satisfy this globally (that's why BL alone only lands
     `r<β_n L`, one dyadic band, and further greedy iteration was rigorously refuted in R9/R10).
     Not a new lever beyond what's certified, but worth naming explicitly as the reason the
     "good" case (dyadic-like decay) is easy and the valley is hard: the residual difficulty is
     precisely quantifying how far the valley profile deviates from a complete/superincreasing
     sequence, and using that deviation's *cumulative* effect (not per-step) to still land near 0.

- Candidate technique(s): a joint induction tracking **(confinement bound, reachable-set size,
  local density near the next pivot)** simultaneously — a genuine 3-parameter strengthened
  invariant, since each single-parameter version (covering radius alone: R10-refuted; bounded-
  depth move search alone: R10-refuted; raw pigeonhole-on-gaps alone: opening 2's caveat) is
  provably insufficient in isolation. This is squarely a "strengthen the induction hypothesis"
  move (Pólya / KB "Generalize" heuristic) rather than a new external theorem.

- Cheap-kill candidates: the confinement lemma `max(R_i)≤a_1` (opening 1) is a genuine cheap,
  easily-provable structural fact not yet in the lemma set — certify it first, it costs nothing
  and sharpens every subsequent argument's interval from "unspecified" to `[0,a_1)⊂[0,L/2)`.
  Also worth a cheap check: does the injectivity `|R_{n+1}|=2^{n+1}` claim (opening 2) ever FAIL
  on adversarial (non-random) valley profiles, e.g. profiles with exact rational ties designed to
  collide? I did not adversarially search for a counterexample to injectivity this round (only
  random sampling) — the outliner/builder should NOT assume injectivity is a theorem; treat it as
  a conjecture to verify harder (deterministic/adversarial search) before building on it, exactly
  per the "verify surprising numeric claims with a fine/adversarial search, not just random
  sampling" standing rule.

- Knowledge-base entries to use: `Pigeonhole / extremal principle`, `Erdős–Szekeres /
  injectivity-coordinate pigeonhole (C1)` pattern (map to distinct-pair coordinates then
  pigeonhole a bounded grid — structurally the same shape as "confine + count + pigeonhole" I'm
  proposing here), `Kronecker/Weyl equidistribution + three-distance-theorem` gap-splitting
  entries (loose structural analogy only — a single fixed rotation `α` repeatedly splits the
  largest arc; our process instead reflects about a NEW pivot `a_i` each step, so it's not a
  literal application, just the same "gap-refinement" spirit — do not force it as a citation).
  `Constructive vs. existence` / `strengthen the induction hypothesis` general heuristics.

- Analogous past problems (cruxes):
  - **aimo-0715** (combinatorics/number_theory, size-bounding via dyadic valuation): extremal
    sequence construction using `v_2` to force a UNIQUE maximal-valuation index in every window,
    so any signed partial sum over the window is a nonzero odd multiple of a power of 2 — this is
    the SAME mechanism as certified Lemma ONE / ONE-REC (superincreasing ⇒ at most one large
    fragment per dyadic scale). Genuinely analogous in spirit (per-scale uniqueness argument) but
    it's a NON-existence/extremal-construction proof, not a density/pigeonhole covering proof —
    useful as a pattern for "assign each element a scale, argue uniqueness per scale," not as a
    direct template for the covering claim itself.
  - **aimo-0298** (IMO "scales" problem, already used/certified via ONE-REC): potential
    `w(S)=Σ2^{-r_S(x)}≤1`, proved by strong induction merging the two closest-value items at each
    step. Same "merge nearest pair, telescope a potential" flavor as our caterpillar process, but
    it merges the CLOSEST pair (adaptive order) whereas our `R_i` process uses a FIXED descending
    order — a structural difference the outliner should note if reusing this pattern (adaptive
    reordering might be exactly the missing ingredient: none of the fixed-order recursions have
    worked, R9/R10).
  - No corpus problem found that directly proves a "restricted/tree-realizable signed subset-sum
    is dense near 0" result — searched `pigeonhole` subtopic (both combinatorics and
    number_theory, 46 entries) and free-text `subset sum / discrepancy / difference / merge`
    across all domains; nothing matches the specific restricted-family density claim. This appears
    to be genuinely open olympiad-novel content, not a retrievable crux.

- Prior progress: (from `results/imo-2026-03/current.md` + `approaches/breakpoint-vertex.md`)
  GAP U-cover is fully reduced (certified, no gaps upstream) to: does `R_{n+1}` (the descending
  include/skip reachable set) meet `[0,u_n]`? Lemma BL certified (first crossing lands
  `r∈[0,β_nL)`, one dyadic band). R10's `ρ_i≤a_i/2` covering-radius invariant is UNPROVEN and
  insufficient alone. `subset-sum-pigeonhole.md` (elo lower, dormant since R7-8) targets the SAME
  object under a slightly different name (`𝓡(A)`, Lemma RL's tree-realizable family, which is the
  UNION over all orderings/subsets, a superset of the fixed-order `R_{n+1}` used by
  breakpoint-vertex) — confirmed below this is the same wall, not a distinct framing.

- Dead ends (do not retry):
  - ANY fixed/bounded-depth existential move lemma (R10: required depth Θ(n), failures not
    localized to near-uniform).
  - ANY single-pass greedy/recursion (band-landing recursion, flip-if-helps, drop-one — R9,
    overshoot up to 11.4×).
  - The naive UNRESTRICTED `2^{n+1}`-subset pigeonhole (Lemma RL: not all `{0,±1}` patterns are
    tree-realizable — invalid).
  - The one-sided ESF-1 (subtract-from-top) family alone (R8: explicit `n=2` counterexample
    `{9/20,7/25,27/100}`, bottoms at `17/100>u_2`).
  - `ρ_i≤a_i/2` covering-radius alone (R10: saturates at `a_{n+1}/2≫u_n` on near-uniform;
    natural induction only gives the weaker `a_{i-1}/2` anyway).
  - Pure gap-pigeonhole (opening 2 above) ALONE does not finish the proof — it proves a small gap
    between two points of `R_{n+1}`, not a small element; flagging this now so no one wastes a
    round presenting it as a full proof.

- Small-case / intuition notes (all CONJECTURE / numeric evidence, not proof):
  - Confirmed `max(R_i)≤a_1` is an easy exact induction (not just numeric — the one-line proof is
    in opening 1; treat as provable, not conjectural).
  - `|R_{n+1}|=2^{n+1}` exactly (injective include/skip map, no coincidences) on 1200+ random
    valley profiles, n=3..6, ratio `|R_{n+1}|/2^{n+1}=1.000` with zero deviation — strong but
    RANDOM-only evidence (per the standing rule, needs an adversarial/deterministic re-check
    before being trusted, since random sampling has previously produced false "always true"
    impressions in this problem's history).
  - `max(R_{n+1})/[(2^{n+1}-1)·u_n]` ≈ 0.4998–0.4999 essentially exactly `1/2` across n=3..6 (300
    trials each) — consistent with `max(R_{n+1})≈a_1≈L/2` at the boundary and confirms opening 1's
    bound is essentially tight, not slack.
  - `min(R_{n+1}\{0})/u_n` (worst case over ~300 valley trials) = 0.775 (n=3), 0.634 (n=4), 0.445
    (n=5), 0.430 (n=6) — i.e. the actual minimum positive reachable value stays comfortably below
    `u_n` with a shrinking (not growing) ratio as `n` increases, consistent with the Covering
    claim being TRUE with growing slack, not a knife-edge — mild evidence that a robust
    (not delicately tight) argument should exist, encouraging the count/density approach over a
    tight extremal one.
