## imo-2026-03 (lens: upper wall after mass-telescope death; DSUM no-go; collision route)

- **Distinct openings surfaced:**
  1. **[DEAD — verified this round] "Late-index automatic decay" route.** Idea: since
     `dist(a_i,R_{i-1}) ≤ a_1·2^{-(i-1)}` (DSUM's per-step claim) and `a_1<L/2` in the valley, at
     `i=n+1` this gives `a_1·2^{-n} < (L/2)·2^{-n} = L/2^{n+1} < u_n = L/(2^{n+1}-1)` automatically —
     which would prove the upper bound with ZERO extra work. **I exact-fraction tested the per-step
     claim directly and it is FALSE**: for `n=3` (4 pieces), thousands of random valley profiles
     violate `dist(a_i,R_{i-1}) ≤ a_1·2^{-(i-1)}` at `i=3,4` (e.g. one witness has
     `d=450718873/9350224937 > bound=1371596529/37400899748`). The per-step "covering radius halves
     every reflection" claim in the DSUM proof sketch is only valid when the fold point lands near the
     center of the current interval (`a_2≈a_1/2`, etc.); for skewed `a_2` (close to `0` or `a_1`) the
     covering radius after one reflection is `max(a_2,a_1-a_2)/2`, which can be close to `a_1/2`, NOT
     `a_1/4`. So there is no way to squeeze a per-index geometric bound below `u_n` — this route is
     dead, confirmed by direct counterexample, not just "unproven."
  2. **[Aggregate DSUM bound itself: holds numerically, but its stated proof is unsound — flag before
     certifying].** I directly tested the AGGREGATE claim `Σ_i dist(a_i,R_{i-1}) ≤ a_1(2-2^{-n})`
     (bypassing the flawed per-step lemma) on 3000 random valley profiles per `n=2..6`: it holds with
     worst ratio `0.93` (no violations found). So the aggregate inequality is very likely TRUE (strong
     numeric evidence, not proof), but **the proof sketch on file (chaining the false per-step bound) is
     invalid as written** — before certifying Lemma DSUM, the builder must either (a) find a genuinely
     different proof of the aggregate sum bound (e.g. an amortized/telescoping argument on total
     interval length rather than per-step covering radius), or (b) demote it to "numerically supported,
     not proved." Recommend flagging this to the outline-reviewer: DSUM's NO-GO conclusion (mass-
     telescope is arithmetically impossible) is still probably correct since `(n+1)u_n→0` alone already
     kills GAP-TELE without needing DSUM's sum bound at all — so the NO-GO stands on the `(n+1)u_n→0`
     argument alone; DSUM's sum-telescope should be re-labeled "conjectured, not certified."
  3. **Collision route — genuinely trivial, not a separate hard case.** I checked the all-equal valley
     profile `a_i=1/(n+1)` exactly: `dist(a_1,R_0)=a_1` (index 1, always equality — no help), but
     `dist(a_2,R_1)=min(a_2,|a_2-a_1|)=min(a,0)=0` **immediately** at `i=2`, since `a_2=a_1` exactly.
     So whenever ANY two of the `a_i` coincide (or, more generally, whenever some `a_i` lands exactly
     on a previously-reachable value), `min_i dist=0≤u_n` trivially, in ONE step. This is not a
     "regime requiring separate machinery" — it is a measure-zero degenerate boundary case, already
     subsumed by continuity. **Genuine opening:** use this to justify a **WLOG-genericity reduction**:
     since the target `min_{∅≠T} descKK(T) ≤ u_nL` is a closed condition (an infimum of continuous
     functions of `A`, hence upper-semicontinuous... actually `descKK` values are continuous in `A`, and
     the min over the finite set of nonempty `T`/sign-patterns is continuous), it suffices to prove it
     on a dense set of profiles (e.g. `Q`-linearly-independent / no exact coincidences), and take limits.
     This buys nothing new logically but tells the outliner NOT to spend effort on "handling collisions
     separately" — collisions are strictly easier, not a genuine second case; all remaining difficulty
     is in the **generic (spread) valley profile**, where no two reachable-set values ever coincide
     exactly and the pigeonhole must be earned honestly.
  4. **LP-duality / extremal-certificate framing (the genuinely different upper attack).** Reframe
     Prop UV as a **minimax**: `max_{A∈valley} min_{∅≠T,ε tree-realizable} |Σ_{i∈T}ε_i a_i|`, and ask
     what the worst-case `A` looks like. Standard extremal/smoothing logic: if `A*` is a maximizer and
     the minimizing `(T,ε)` is *unique* at `A*`, then perturbing `A*` slightly in the direction that
     increases that one signed sum (keeping the valley constraints and `ΣA=L` fixed) would strictly
     increase the min — contradicting maximality — UNLESS the valley/simplex boundary is active. This
     is the standard "at the extremal profile, multiple achievers must be tied (or a boundary
     constraint binds)" argument used in many extremal olympiad/LP arguments. It gives a genuinely
     different route to Prop UV: characterize the extremal `A*` by a **tie/balance condition** among
     several nonempty-subset signed sums, rather than by tracking one reachable-set DP forward. I
     conjecture (untested this round, flagged as a candidate only) that the dyadic ladder
     `a_i=2^{n+1-i}/(2^{n+1}-1)` is the UNIQUE such tied extremal point (consistent with the reported
     "tight only at the dyadic boundary, worst ratio 0.75 elsewhere" — i.e. away from dyadic the min
     drops noticeably below `u_n`, exactly what an interior-maximum tie condition would produce). This
     is the "potential-free / LP-duality" escalation the R13 recommendation called for, and it attacks
     the WHOLE valley at once rather than a forward DP recursion — genuinely far from the five dead
     families (covering-radius, density/COUNT, greedy recursion, bounded-depth escape, mass-telescope).
  5. **valley-differencing-construction (elo 1517, never built) — worth building, but scope it
     correctly.** As named, this slug sounds like it would give an EXPLICIT Karmarkar-Karp
     differencing-tree construction with a telescoping leftover bound. Caveat from my probing: a
     naive "always match the two largest surviving pieces" (classical KK heuristic) is exactly the
     kind of single deterministic policy ALREADY REFUTED in R9 (greedy band-landing / drop-one /
     flip-if-helps all overshoot `u_nL`, up to `11.4×`). So a construction slug must NOT re-propose
     plain greedy KK-differencing on the full multiset — it needs to combine DELETE (subset choice,
     certified essential by Lemma RL/VS) with a *non-greedy*, foresight-based choice of which subset
     and which tree order to use, e.g. built explicitly from the sorted `a_i` via the **dyadic-ladder
     comparison**: guess the subset/tree that would be optimal AT the extremal dyadic profile, and
     show it still achieves `≤u_nL` when perturbed off dyadic (a stability/robustness argument, which
     is essentially opening 4 in constructive form). Worth building, but only if paired with an
     explicit non-greedy recipe — a bare "greedy KK differencing" restatement will die exactly as R9's
     mechanisms did.

- **Candidate technique(s):** LP/extremal tie-condition (minimax with unique-vs-multiple-achiever
  argument) — genuinely new; explicit non-greedy KK-differencing construction robust near the dyadic
  extremal point; continuity/genericity reduction to dispose of collisions cheaply.

- **Cheap-kill candidates:**
  - Collisions (any repeated value among `a_i`, or `a_i` landing on a prior subset-KK value) give
    `dist=0` in one step — dispose of this measure-zero case immediately by continuity; do not spend a
    separate lemma on it.
  - The per-step geometric-decay claim in DSUM is directly falsifiable (I found explicit rational
    counterexamples at `n=3`) — do not let a builder cite "dist(a_i,R_{i-1})≤a_1·2^{-(i-1)}" as
    proven; only the AGGREGATE sum bound survives numerically.

- **Knowledge-base entries to use:** I did not find a knowledge_base.md entry specific to
  Karmarkar–Karp differencing or discrepancy minimax; the relevant generic tools already in play are
  the certified DM/P/RL/ESF-1/ESF-2 lemmas (differencing-tree realizability) — these remain the
  correct vocabulary for any construction slug. For the LP-duality opening, look for a generic
  "extremal/smoothing exchange argument" or "Lagrangian tie condition at an interior extremum" entry
  in knowledge_base.md if present (I did not confirm one by name — the outliner should grep
  knowledge_base.md for "smoothing", "exchange argument", "extremal principle", "compactness" before
  building this).

- **Analogous past problems (cruxes):** I filtered the crux corpus (combinatorics domain, subtopics
  `processes-and-algorithms`, `extremal-principle`, `games-and-strategy`, `pigeonhole`) for
  differencing/partition/discrepancy keywords. The two closest hits are:
  - `aimo-0836` (China): board process erasing `a,b` and writing `a+b,|a-b|` — same differencing
    *operation* as our DELETE/MATCH, but the target question (can the board reduce to exactly 2
    numbers) is a reachability/invariant question, not a discrepancy-minimization bound. The crux move
    ("pair up so both sum and difference are already on the board") is not directly transferable to a
    discrepancy inequality, but confirms the differencing-tree vocabulary is standard.
  - `aimo-0913` (Croatia, Fibonacci difference-covering set): a forest/graph lower-bound + anchored
    construction for covering a target difference set — structurally about *realizing* prescribed
    differences with few base elements, a different flavor (extremal set-covering, not adversarial
    minimax over an unknown continuous profile).
  - **No genuine analogue found** for the actual crux needed here (a tight adversarial minimax bound
    over a continuum of profiles for a restricted signed-subset-sum/differencing value). Recommend not
    forcing either corpus match into the outline; the LP-duality/extremal-tie idea (opening 4) is not
    drawn from the corpus, it is a generic extremal-principle technique.

- **Prior progress:** As in `current.md`/`breakpoint-vertex.md` — Reduction R-COV' (certified),
  Lemma FGR (certified), Lemma CONF/MD2 (certified), the honest residual is
  `min_{∅≠T} descKK(T) ≤ u_nL`. Five upper-wall mechanism families dead (covering-radius, density/COUNT,
  greedy recursion, bounded-depth escape, mass-telescope discrepancy). DSUM's aggregate inequality is
  numerically solid but its filed proof sketch is unsound (see above) — recommend NOT certifying DSUM
  as-is; either reprove the sum bound honestly or restate the NO-GO conclusion as following from
  `(n+1)u_n→0` alone (which does NOT need DSUM at all).

- **Dead ends (do not retry):** covering-radius (one-cap R10, two-cap R12); dispersion/density/COUNT
  (R11); greedy recursion (R9, incl. band-landing/flip-if-helps/drop-one); bounded-depth escape (R10);
  mass-telescope discrepancy (R13); and NEW this round — the "late-index automatic geometric decay"
  shortcut (`dist(a_i,R_{i-1})≤a_1·2^{-(i-1)}` used termwise to beat `u_n` directly) is refuted by
  explicit rational counterexample at `n=3`, so do not let any builder assume this per-step bound.

- **Small-case / intuition notes (conjectural, from numeric probing):**
  - The aggregate sum bound `Σdist(a_i,R_{i-1}) ≤ a_1(2-2^{-n})` held with worst ratio `0.93` over
    15000 random valley profiles (`n=2..6`) — strong evidence it is a true theorem, just needs a
    different (non-per-step) proof.
  - Collisions (`a_i` repeating or landing exactly on a prior reachable value) always give an
    immediate `dist=0`, confirmed exactly on the all-equal profile `a_i=1/(n+1)`: `dist(a_2,R_1)=0`.
  - The reported "worst ratio 0.75, tight at the dyadic ladder" pattern for the true target
    `min_{∅≠T}descKK(T)/u_n` is exactly the signature of an interior-maximum extremal profile with a
    tie condition among several achieving subsets — supporting the LP-duality/extremal-tie conjecture
    (opening 4) as the most promising genuinely-new direction, though this is my own reading of the
    existing numeric evidence, not independently re-verified by me at scale this round.
