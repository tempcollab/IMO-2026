## imo-2026-03

### Lens
Dedicated search for a genuinely different technique class to replace
`minimax-mixed-duality` (RETHINK, 2 rounds no independent leverage — every
construction it found collapses into `universal-adversary-strategy`'s
discrete tie-structure casework) and to double-check `relaxed-adversary-transfer`
really is dead (it is — see below). Searched: crux corpus
`combinatorics/games-and-strategy` (39 items), `linear-algebra-method` (16),
`generating-functions` (12), `probabilistic-method` (4), plus keyword sweeps
across all domains for "alternating/rank/potential/reachability/budget", and
`knowledge_base.md`'s Combinatorics / General Proof Methods / Monotone
Subsequences sections.

### Distinct openings

**A) (Primary candidate — genuinely different proof *shape*) Dynamic
per-move potential with a free tunable parameter, à la crux `aimo-0198`
(IMO liar's-guessing-game).** In `aimo-0198` part (b), Amy (the adversary)
is bounded not by finding one fixed candidate strategy, nor by averaging 2-3
named candidates (which is exactly what `potential-averaging-bound` tried
and which failed here), but by tracking a **single scalar potential**
`Φ = Σ_i λ^{m_i}` over the *whole* live candidate population, with a **free
parameter `λ`** chosen *after* deriving the per-step recursion, and a
single per-step inequality of the `min(A,B) ≤ (A+B)/2` shape (the adversary
picks the *cheaper* of exactly two successor potentials) that telescopes
over all `k` moves into a clean closed-form bound. Two features make this
structurally different from every dead/converged approach on file:
  - It is **sequential/order-dependent** — the potential is tracked through
    Xiang Yu's marks *one at a time*, each move's effect bounded relative to
    the *current* state, not solved as one shot against the *final*
    configuration `B` (unlike `minimax-mixed-duality`'s per-`A` mixture over
    final response *types*, and unlike `universal-adversary-strategy`'s
    direct casework on the final tie-structure).
  - It has a **free parameter `λ`** giving one extra degree of freedom that
    neither `equalization-potential-bound` (a single *static*, `A`-independent
    rank-weight functional, proved impossible by Lemma D/E) nor
    `potential-averaging-bound` (a fixed, parameter-free average of exactly
    2–3 named deterministic candidates, refuted on `(1/3,1/3,1/3)`) had
    available.

  **Concrete sketch to adapt (not a proof — first thing a builder must
  check before committing).** Process Xiang Yu's `≤n` marks in some fixed
  order (e.g. always attack the current largest untouched piece). At each
  step define a potential `Φ_t` built from the *current* sorted remaining
  multiset with a geometric per-rank discount `λ^{rank}` (`λ` free). Try to
  show: for *any* single split move available at step `t`, the *best*
  available move (min over the two "natural" successor potentials —
  analogous to Amy's yes/no split into `Φ_1, Φ_2` with `Φ_1+Φ_2` fixed)
  satisfies `Φ_{t+1} ≤ ρ(λ)·Φ_t` for a ratio `ρ(λ)<1` independent of the
  actual piece values. If such a uniform per-step contraction exists, `n`
  steps give `Φ_n ≤ ρ(λ)^n Φ_0`, and tuning `λ` to match the known closed
  form `c(n)=2^n/(2^{n+1}-1) = 2^n / Σ_{i=0}^n 2^i` (a partial geometric sum
  — note this *is* exactly the form a tuned-`λ` telescoping bound produces)
  would give the bound directly, with **no per-`A` vertex/tie-structure
  casework at all**.

  **Honest risk (flag for the builder, do not skip this gate).** The
  hardest part of the existing proof is not "bound one move's effect"
  (already solved exactly by DOM/HALVE/SANDWICH/PARTIAL-DOM/TIE-MIN-HALVE)
  — it is **choosing which piece to attack and in what order**, i.e. exactly
  the sequential decision problem `universal-adversary-strategy`'s
  peel-and-recurse (Claim PTBI) construction already is. There is a real
  chance this potential framing is just PTBI re-described in potential-function
  language, the same fate that befell `minimax-mixed-duality`. **Mandatory
  cheap-kill before opening a full approach on this**: pick the two hardest
  known witnesses on file (`A=(4265,2536,1747,1014,438)/10000` and
  `A=(3415,3023,1664,1404,494)/10000`, both `n=4`, from
  `minimax-mixed-duality`'s round-7 gate check) and check numerically
  whether *any* single choice of `λ` makes a naive "always attack current
  largest, `min(A,B)≤(A+B)/2`-style" contraction bound beat `c(4)=16/31` on
  both — if it needs a *different* `λ` or a *different* attack-order rule per
  witness, this collapses into casework exactly as before and should be
  reported honestly as another convergence, not forced into `partial`.

**B) (Secondary, more speculative) Order-type sandwiching / interpolation,
à la crux `aimo-0594`.** That problem needs to show a rank-only,
domination-respecting, transitive comparison rule is pinned by a single
coordinate; its load-bearing move is to **sandwich an arbitrary pair between
auxiliary configurations that are order-isomorphic to a small set of
already-"calibrated" instances**, using an epsilon-shift plus transitivity
to transport the calibrated verdict to the arbitrary pair. Adapted here:
instead of proving the upper bound for *every* configuration `A` by
identifying its exact winning tie-structure, try to **sandwich an arbitrary
`A` between two calibrated configurations** (e.g. a "locally geometric"
config known to attain `c(n)` and a nearby dominated/dominating config)
using a monotonicity lemma (if `A' ⪯ A` coordinatewise in some order-type
sense then `min_B oddrank(B)` is monotone), reducing the general-`A`
upper bound to finitely many calibrated cases. **Caveat:** this problem's
objective (`oddrank`, driven by real-valued piece lengths, not pure order
type/ranks of `2n` labeled cards) is much less purely combinatorial than
`aimo-0594`'s setting, and no monotonicity lemma of the needed shape is
currently on file (worth checking: is `min_B oddrank(B)` even monotone
under a natural majorization/domination order on `A`? `majorization-smoothing`'s
already-proved concavity-failure result is adjacent evidence this may fail
too — a genuine risk, not yet tested). Weaker candidate than (A); flag only,
do not treat as ready to build without a fast numerical monotonicity check
first.

**C) (Targeted, not a new proof *shape* but a different tool for a specific
open sub-gap) Linear/generating-function reachability encoding for
Lemma PARITY-PAIR-ANCHOR's remaining "partial-budget, `M` even" gap.**
`current.md`'s own diagnosis of this gap: "needs game-reachability, not
just abstract combinatorics" — i.e. the question is which *anchor-multiplicity
vectors* are actually reachable by Xiang Yu using *exactly* `M` (even, `<`
full budget) marks against a fixed anchor set, not a claim that holds for
all abstract multisets. Crux corpus has a real pattern for exactly this
kind of question: `aimo-0542` and `aimo-0281` (both `linear-algebra-method`,
outside `games-and-strategy`) encode "which states are reachable by a
bounded number of moves from a fixed move-set" as an integer/`F_2`-linear
system (min Hamming weight / integer combination existence), turning a
combinatorial reachability question into linear algebra. This is a
plausible, narrowly-scoped tool to try on gap (a) specifically (not a
replacement for `minimax-mixed-duality`, but worth flagging to whichever
approach owns that gap, i.e. `recursive-embedding-induction`).

### Candidate technique(s)
- (A) Dynamic geometric-discount potential with a free contraction
  parameter, adapted from crux `aimo-0198`'s move-count-bounding argument;
  KB pointer: "Invariants & monovariants" (Combinatorics section) and
  "Induction: pick the right variable" (General Proof Methods) — this is a
  *monovariant with a tunable rate*, a specialization not explicitly in the
  KB text but consistent with its Invariant/monovariant entry.
- (B) Order-type sandwiching/transitivity bridge, adapted from crux
  `aimo-0594`.
- (C) Linear-algebra reachability encoding, adapted from cruxes `aimo-0542`,
  `aimo-0281`.

### Cheap-kill candidates
- For (A): the numeric gate described above (single-`λ` contraction test on
  the two hardest `n=4` witnesses) — run this **before** opening a full
  approach file; if it needs witness-dependent `λ` or attack order, report
  convergence honestly rather than building it out.
- For (B): a fast numerical check of whether `min_B oddrank(B)` is monotone
  under any natural per-piece majorization/domination order on `A` (sample
  a few `A, A'` pairs with `A' ` a "coordinatewise more extreme" version of
  `A`, check the response-values move the expected direction). Given
  `majorization-smoothing`'s confirmed non-concavity, expect this to be
  fragile; treat a single clean counterexample as a kill.
- For (C): none needed beyond the existing precise scoping already done by
  `recursive-embedding-induction` — this is ready to hand off directly.

### Knowledge-base entries to use
- "Invariants & monovariants" (Combinatorics section, `knowledge_base.md`)
  — the general category (A) specializes.
- "Hall's marriage theorem / SDR" (Combinatorics section) — not obviously
  applicable here (no bipartite matching-saturation structure identified),
  checked and set aside.
- No LP-duality-specific or generating-function-specific KB entry exists;
  `knowledge_base.md`'s "General Proof Methods" section only has generic
  induction/casework/invariant entries, already fully exploited by the live
  approaches.

### Analogous past problems (cruxes)
- `aimo-0198` (IMO liar's-guessing-game, `probabilistic-method`) — crux
  move "bound a greedy minimizer's outcome by the average of its two
  available options, `min(A,B)≤(A+B)/2`, to get a clean recursive bound on
  the potential." **Best candidate found this round** — genuinely different
  proof shape (sequential potential with tunable parameter) from everything
  currently on file, though its adaptability here is *unverified*, flagged
  honestly as risky (see cheap-kill above). This is the crux the round-5
  memory rule (#19 in `/tmp/memory/math-explorer.md`) already flagged as
  "unexplored" — `potential-averaging-bound` (round 5) tested only the
  *static-average* reading of it and failed; the *dynamic/sequential*
  reading with a free parameter has not yet been tried.
- `aimo-0594` (order-only rule pinned to one coordinate, `extremal-principle`)
  — sandwiching/transitivity technique, weaker analogy (see caveats above),
  offered as a secondary option only.
- `aimo-0560` (gardener/lumberjack, `games-and-strategy`) — already tried
  and killed as `relaxed-adversary-transfer`; **do not revive**, confirmed
  dead by independent reading of its file this round (Theorem V-INF: the
  ∞-mark relaxation is config-independent, needs `n+1` not `n` marks, and
  bounds from the wrong direction — a clean, structural, correctly-proved
  negative result, not a weak attempt).
- No other crux in `games-and-strategy`, `linear-algebra-method`,
  `generating-functions`, or `probabilistic-method` (combinatorics domain)
  resembles this problem's alternating-claim / stick-cutting structure
  closely enough to be a genuine analogy — consistent with round 6/7
  explorers' same finding; this round's broader keyword sweep (alternating,
  rank, reachability, budget, potential) across all three domains did not
  surface anything closer than the three listed above.

### Prior progress
See `current.md` for the full state. Headline: lower bound's `k=n`
tail-untouched sub-case (Proposition K) fully closed; tail-refined lower
bound narrowed to two isolated sub-cases (partial-budget even-`M`
anchor-only; cross-piece tied free coordinates), both owned by
`recursive-embedding-induction`. Upper bound over arbitrary configurations:
casework toolkit (DOM, HALVE, MULTI-HALVE, PARTIAL-DOM, PARTIAL-DOM-RESIDUAL,
TAIL-SNIP, SANDWICH, DOUBLE-INSERT, TIE-NECESSARY, proposed-not-certified
TIE-MIN-HALVE) closes both hardest known `n=4` witnesses, but the general
theorem (Claim PTBI, "peel + recurse + halve is always ≤ c(n)") is not
proved, owned by `universal-adversary-strategy`.

### Dead ends (do not retry)
- `minimax-mixed-duality`'s specific mechanism (per-`A` mixed distribution
  over named response *types*, weights sought via LP dual at worked
  examples) — 2 rounds, zero independent leverage, everything it found
  reduces to `universal-adversary-strategy`'s casework. Verified by reading
  the file this round; the honest self-assessment is correct, not
  overclaimed.
- `relaxed-adversary-transfer` (relax Xiang Yu's mark budget to `∞`) —
  structurally degenerate (Theorem V-INF), config-independent, wrong-direction
  inequality. Verified correct this round; do not revive the "relax the
  budget" mechanism on any axis without a genuinely new idea for *what* to
  relax (this file itself notes relaxing something *other* than the mark
  count, e.g. "let Xiang Yu see Liu Bang's marks before committing," is
  already true in the real game and not a relaxation at all — no fresh
  relaxation axis was identified).
- `equalization-potential-bound` (single static, `A`-independent rank-weight
  functional) — proved impossible in principle (Lemma D/E interior-point
  obstruction forces `w≡c(n)`, tautological). Note this does **not** rule
  out opening (A) above, since (A)'s potential is dynamic/sequential and
  per-move, a different mathematical object from a static functional on
  `A`-space — this distinction is exactly the one `minimax-mixed-duality`'s
  own file draws (correctly) between itself and `equalization-potential-bound`.
- `potential-averaging-bound` (fixed 2-3 deterministic candidates, averaged,
  no tunable parameter, no sequential structure) — refuted on
  `A=(1/3,1/3,1/3)`, all 3 candidates individually exceed `c(2)`. This is
  the *static* reading of the `aimo-0198`-adjacent idea; opening (A) is
  explicitly the *dynamic, tunable-parameter* reading that this round's
  search identifies as untested, not a re-run of the same thing.

### Small-case / intuition notes
- `c(n) = 2^n/(2^{n+1}-1) = 2^n / Σ_{i=0}^n 2^i` — this is literally "top
  weight over total weight" of a dyadic (partial-geometric-sum) weighting.
  This numeric form is exactly the shape a *tuned-`λ` telescoping potential
  bound* would naturally produce (conjecture/intuition only, not verified) —
  a structural reason to think (A) is at least *plausible* in form, even
  though the hard sequential-decision content (which piece to attack, in
  what order) is unverified to actually admit a uniform per-step
  contraction ratio. This is the main reason (A) is ranked above (B) and
  (C) as the primary candidate for a genuinely new approach slug this round.
- No new small-case computation was run this round (the existing file
  record already has extensive `n=1..8`, `m=5` witness-level verification);
  this round's work was corpus/framing search, not fresh numerics, per the
  dispatch's explicit lens.
