## imo-2026-03 — lens: bypass the merged-order/discrepancy reduction for GAP L (lower-bound Case B)

### Summary verdict up front
I did **not** find a clean bypass that skips the merged-order/discrepancy reduction entirely and
lands directly on `D̃≥1`. The reduction itself (Lemma G -> level-measure -> cut-flip -> discrepancy
minimax -> top/bottom split via the Structure Lemma) is forced by the problem's own structure (a
stick can only be cut, never merged, so Y and Z are genuinely disjoint sub-multisets sharing a cut
budget) — any attack still has to confront a "compensation must be global across scales" fact, which
three rounds of work have now nailed down precisely (`(♠≥0)` / `E(F)≤2^n−1`). What I *can* offer are
several genuinely different top-level framings that route around the specific *shape* of the current
wall (top/bottom recursive split + merged order), even though they cannot avoid the underlying
combinatorial fact. I recommend the outliner seed at least one of these as a structurally distinct
approach, per the plateau rule.

### Distinct openings

**1. Dual-signed-sum / "reflection" of the certified upper-bound proof — promising but needs a real
restriction, NOT a free bypass.**
The certified `lemmas/upper-bound.md` proves GAP U via: (a) Realizability Lemma / Theorem R — any
`ε∈{−1,0,1}^m` sign pattern is achievable as an *effective* total using `≤m−1` cuts (pin/bisect ops);
(b) subset-sum pigeonhole picks a small nonzero `ε`; (c) `D(physical)=D(effective)≤effective total`.
The natural "reflection" for the lower bound would be: *for Liu's specific dyadic partition, no
matter which physical cuts Xiang makes (not just pin/bisect), `D̃` cannot be driven below the
**minimal nonzero `{−1,0,1}`-signed sum of the dyadic weights**, which is exactly `1`* (this minimal
signed sum for `{1,2,…,2^n}` is `1`, matching sharpness noted in `upper-bound.md`). This would be a
literal dual of the certified upper bound and would **completely bypass** the Case B/top-bottom split.
**I checked this directly and it is FALSE for general (non-dyadic) Liu partitions** — e.g. `n=1`,
Liu picks `(0.9,0.1)` (a bad, non-optimal choice), Xiang cuts `0.9→(0.5,0.4)`, final `{0.5,0.4,0.1}`,
`D̃=0.5−0.4+0.1=0.2`, while the original signed-sum bound would predict `≥ℓ1−ℓ2=0.8`. So "cutting
cannot reduce D below the original pieces' minimal signed sum" is false in general — cutting a large
piece genuinely creates NEW, smaller elements that can produce a much smaller signed sum than any
combination of the *original* pieces. **This kills the naive dual as a general theorem**, but it does
NOT kill the idea when restricted to Liu's *actual* dyadic choice with the cut budget properly
accounted for (which is exactly the induction the field is already running) — so this is a **partial
opening**: worth trying to reformulate the theorem as "the minimal signed sum of the *final fragment
multiset* (not the original pieces) is bounded below by 1, given only `≤n` total cuts on the dyadic
`{1,…,2^n}`" — but that is very close to restating the target itself (`D̃=` the specific `{−1,+1}`-ish
alternating sum already, cf. `(♦)`/`ψ`), so it likely does not actually escape the merged-order
machinery — just re-derives it in signed-sum language. Flag as: **interesting reformulation
candidate, not a proven bypass; the naive general form is refuted (new dead end, worth recording)**.

**2. Amortized/sequential-cut potential — attacks the cuts as an ORDERED sequence, not a top/bottom
split.** All three live approaches split the final multiset by *origin* (which dyadic ancestor piece
a fragment descends from) and reduce to a Structure-Lemma recursion. A genuinely different framing:
process Xiang's `≤n` cuts **one at a time in the order Xiang actually makes them** (or, for the proof,
in decreasing order of the piece cut), and track a *running invariant* `Φ_k := D̃(\text{current
multiset after }k\text{ cuts}) - r_k` for some explicit "reserve" `r_k` that starts at some value tied
to `u_n` and is *repaid* by later cuts — in the spirit of the amortized-induction move used in
crux `aimo-0019` ("maintain a linear potential bounding cumulative resource by a constant times
progress, charging each advance against the pieces it absorbs"). This is different in kind from the
current top/bottom recursion: it is a monovariant over the *cut sequence*, not over *fragment origin*.
The Cut-Flip Lemma already gives the exact per-cut effect (`|ΔD|≤2min(x,ℓ−x)`, and the *exact* toggle
set `[0,x)∪[ℓ−x,ℓ)` — not just the bound), which is under-used by the current field (only the bound
is used, e.g. in the Cut-Budget corollary); a genuinely sequential argument exploiting the *exact*
toggle-set geometry (not just its measure) across Xiang's `≤n` cuts, charging each cut's negative
effect against the width it can possibly reach, could be a structurally different route to `D̃≥1`. I
did **not** verify this beyond the observation that the tool (exact Cut-Flip toggle sets) exists and
is certified but is not the backbone of any of the three live approaches — worth flagging to the
outliner as unexplored terrain, not as a working proof.

**3. Direct strategy-stealing on Liu's choice of partition (not on Xiang's cuts) — checked, does not
bypass.** One might hope for a strategy-stealing argument: assume some Xiang response to the dyadic
partition beats `c(n)`, then show Liu could have used a *different* partition to do at least as well,
deriving a contradiction with the (separately proven, certified) upper bound. But the upper bound is
already proven for *every* Liu partition (GAP U is closed for all n, unconditionally), so this kind of
swap argument cannot add information beyond what GAP U already gives; it does not touch Case B. Not a
new opening — recording so nobody retries it.

**4. Self-contained restatement as a pure existence/injection combinatorics problem (already surfaced
by induction-recursion-telescope §9, but worth flagging as the cleanest possible "fresh eyes"
entry point for a genuinely new approach-slug):** *For every way of writing `{1,2,…,2^n}
= ⊎_{j=0}^n π_j` (`π_j` a partition of `2^{n−j}` into `a_j+1` parts, `Σa_j≤n`), the odd-rank sum of
the merged multiset is `≥2^n`.* This statement has **no reference to games, cutting, or discrepancy
language** at all — it is pure extremal combinatorics on partitions of powers of two under a shared
"total splits ≤n" budget. Because it is self-contained, it is the best candidate for a fresh
combinatorial (rather than analytic/measure-theoretic) proof: e.g. a direct double-counting /
generating-function argument on the *number of odd positions* contributed by each dyadic scale, or an
explicit bijective/injective argument bounding how much of scale `2^{n−j}`'s mass can land at even
merged rank. This is NOT solved here — it is the existing residual, just re-flagged as a place where
a combinatorics-flavored (rather than measure/analysis-flavored) attack might succeed where the
measure-theoretic merged-order argument has plateaued. Recommend as the best "different framing"
candidate for a genuinely new slug.

### Candidate technique(s)
- Reflection/duality with the certified Realizability Lemma / Theorem R (opening 1) — refuted in
  general form, but the reformulation in terms of the *final* fragment multiset's signed sum might be
  worth one round if phrased as pure combinatorics rather than re-deriving `(♦)`.
- Amortized/sequential potential over the ordered cut sequence, using the *exact* Cut-Flip toggle-set
  geometry (opening 2) — unexplored; the tool exists (certified `cut-flip.md`) but is not the backbone
  of any current approach.
- Double-counting / generating-function attack on the self-contained partition-refinement restatement
  (opening 4) — the cleanest "fresh framing," recommended for a new slug.

### Cheap-kill candidates
None obvious beyond what's already used (parity of N(t), the C3 domination bound, the pigeonhole on
subset sums). No new quick structural prune found this round.

### Knowledge-base entries to use
`knowledge_base.md` was consulted; the load-bearing entries already in play (Lemma G / greedy-claim,
level-measure identity, cut-flip/cut-budget, C3 domination) are the right ones. I did not find a
knowledge_base entry beyond these that supplies a genuinely new mechanism (no dedicated
"potential-function games" or "strategy-stealing" entry exists there distinct from what's already
imported).

### Analogous past problems (cruxes)
Queried `combinatorics` × `games-and-strategy` (39 cruxes) and cross-cutting `dyadic`/`discrepancy`/
`signed sum`/`pigeonhole`/`greedy` keyword hits across combinatorics+algebra.
- **`aimo-0117`** (Jesse/Tjeerd stone-box game) — technique: *assign values as a two-sided geometric
  (dyadic) sequence so the largest strictly exceeds the sum of all others*, maintained via an
  adaptive invariant ("largest power sits in the target box") that is repaired reactively each time
  the opponent perturbs it. **Thematically resonant** (dyadic domination is exactly our C3/Case-A
  mechanism) but **mechanistically not transferable**: that game is a sequential, alternating,
  adaptive placement game (Jesse reacts move-by-move to Tjeerd), whereas our game has Xiang choosing
  all `≤n` marks *simultaneously* after seeing Liu's marks, with no further interaction before the
  cutting/claiming phase. So there is no "reactive invariant-repair" structure to exploit here — flag
  as resonance, not a working reduction.
- **`aimo-0019`** (paint-the-line game with `1/2^m` ink budgets) — technique: *bound a family of
  dyadic pieces of pairwise-distinct sizes by twice the largest* (our C3-style domination) plus *an
  amortized linear potential charging each "frontier advance" against the pieces it absorbs*. This is
  the source of opening (2) above — a genuinely different *amortized-over-the-move-sequence* proof
  shape, distinct from the current top/bottom Structure-Lemma recursion. Worth adapting: not directly
  analogous in game structure, but the proof *technique* (charge each move against a bounded resource,
  processed as a sequence, not by static partition) is a candidate mechanism nobody has tried yet.
- **`aimo-0296`** (angle-ordering, `±1`-signing recast) — technique: recast a splitting target as a
  `±1` signed sum; conceptually similar to the already-used `(♦)`/`ψ(c)` merged-order signed-sum
  machinery, so **not a new angle** — just confirms the signed-sum framing is a standard move, not
  evidence of an escape route.
None of the three constitutes a solved analogue close enough to import a finished argument; the best
of them (`aimo-0019`) supplies a *proof-shape* worth trying (sequential amortized charging) rather
than a specific lemma to borrow.

### Prior progress
As recorded in `current.md`/both induction-* approach files: upper bound (GAP U) is fully proven and
certified for all n. Lower bound Case A is proven. Lower bound Case B is closed except for the
residual `(♠≥0)` ⇔ `E(F)≤2^n−1` ⇔ `(△⋆)`, which is proven closed on the whole `maxc≤1` region
(Termwise Lattice Lemma T, certified) including every tight (`D̃=1`) configuration; the only open part
is `maxc≥2`, verified with 0 violations numerically but not proven, and known to require a genuinely
**global**, bottom-inclusive count-parity argument across `Z`'s recursive dyadic cut-tree (not a
local matching, not a scalar summary, not a top-down reserve — all three mechanisms are rigorously
refuted, see below).

### Dead ends (do not retry) — verified, not just copied
- **Local anchor-matching / value-width-dominating injection** `{Y even-pos}→{Z odd-pos}`
  (telescope §10): refuted on 21% of Case-B configs; explicit witness
  `n=5, Y=(17.9,14.1), Z=(11.418,8,4.582,4,2,1)`. Confirmed the logic of the refutation is sound (a
  single large `Y`-part can only be dominated by the *sum* of several smaller `Z`-odd parts across
  scales, not by any one anchor) — do not resurrect.
- **Top-down reserve of `Z`** (`λ{t>τ:N_Z odd}≥λ{t>τ:N_Z even,N_Z>0}`) (telescope §14): refuted,
  7306/4·10⁵ violations; the tie config `n=4,Y=(8,3,3,2),Z=(8,2,2,2,1)` shows the whole surplus can
  sit in the near-`0` band. Confirmed correct — the surplus is bottom-inclusive/global, not bankable
  from the top.
- **Scalar/count summary of Z** (both induction slugs, multiple probes): refuted — `(GAP-LB′-run)` is
  false if `Z` is replaced by an arbitrary multiset with the same sum and `altsum≥1`.
- **My own naive "dual signed-sum" idea (opening 1 above, checked this round)**: the claim "cutting
  cannot push `D̃` below the minimal nonzero `{−1,0,1}`-signed sum of the *original* Liu pieces" is
  FALSE in general (counterexample: non-dyadic Liu partition `(0.9,0.1)`, one cut to `(0.5,0.4)`,
  gives `D̃=0.2 < 0.8`). New dead end — record so nobody wastes a round re-deriving it as a free
  general theorem; it would need heavy restriction to the fragment multiset (not the original pieces)
  to have any chance, and doing so likely just re-derives the existing `(♦)` machinery.

### Small-case / intuition notes (conjecture, not proof)
- All existing numerics (0 violations across `≥4·10^5` configs, `n≤6`) strongly support `D̃≥1`
  everywhere, with the true infimum on `maxc≥2` being exactly `1` (attained at the tie config, not
  strictly `>1` as an earlier round mistakenly reported before tie-normalization). This is *strong*
  numerical evidence the theorem is true and tight — but it is conjecture-grade, not proof-grade, for
  the residual region.
- The self-contained restatement (opening 4) — `E(F)≤2^n−1` for any simultaneous refinement of
  `{1,…,2^n}` with total cut budget `≤n` — is, on reflection, probably the single most "textbook
  extremal combinatorics"-shaped restatement of the whole residual, and might respond better to a
  pure counting/generating-function argument by someone NOT already anchored in the measure-theoretic
  merged-order language. This is my strongest recommendation for where to point a genuinely fresh
  approach-slug.
