# Round 6 — math-explorer (lens: genuinely different framing), imo-2026-03

## What I read
`results/imo-2026-03/current.md`, all six files in `results/imo-2026-03/approaches/`
(`geometric-dominance-construction`, `recursive-embedding-induction`,
`universal-adversary-strategy`, `potential-averaging-bound`,
`majorization-smoothing`, `equalization-potential-bound`), `knowledge_base.md`,
`crux_moves_documentation.md`, and queried the crux corpus
(`past_crux_moves_database.json` / `past_problems_database.json`, 2434 cruxes,
1026 problems) by keyword and by `domain=combinatorics`,
`subtopic=games-and-strategy` / `extremal-principle` / `invariants-and-monovariants`.

## Diagnosis of why the field is stuck in one framing

All three live approaches, and both dead ones, share the *same* underlying
object: the geometric configuration `A_n = {2^n,...,1}/D`, `oddrank`/`D`
(alternating-sum) as the value functional, and a "peel/exchange/insert one
element into a sorted list" mechanism, whether phrased as LP-vertex reduction
(`Lemma V'`), exchange moves (`Lemma X`), or cascading DOM/HALVE. Every
negative result found so far (Claim ★ false for `s≥3`; move-traps for
bounded-width exchanges; TAIL-SNIP insufficient; the averaging gate failing on
`(1/3,1/3,1/3)`; the LP/linear-functional obstruction in
`equalization-potential-bound`; the convex-kink-inside-min obstruction in
`majorization-smoothing`) is a negative result *about this one family of
mechanisms* — every one of them tries to certify the bound via a
**single-piece or two-piece local move plus induction on the sorted list**.
The recurring failure mode ("the correct response needs a coordinated,
jointly-optimized simultaneous split of ≥2 pieces at non-half ratios") is
itself evidence that no *local* single-move argument in this family will
close the gap — it's the same wall recurring at every entry point.

## Crux corpus findings (honest report: no direct hit)

I searched combinatorics `games-and-strategy` (39 cruxes), and broader
keyword sweeps (`stick`,`cut`,`claim`,`alternately`,`alternating sum`,
`majorization`,`minimax`,`LP duality`,`superincreasing`). **No problem in the
corpus is this exact game type** (mark-then-mark-then-alternately-claim). The
closest adjacent techniques found:

- `aimo-0117` — a two-player game where one side plays values forming a
  **dyadic (geometric, ratio-2) sequence so the largest strictly dominates
  the sum of all others**, exactly the domination mechanism already certified
  here as Lemma 2/Lemma S. Confirms the geometric-doubling idea is a known,
  reusable crux move elsewhere, but offers nothing beyond what's already in
  the population.
- `aimo-0718` (Elisa's treasure chests) — "**bound a greedy actor against an
  adversary that can block at most `r` objects** by pigeonholing on the
  `r+1` smallest objects: at least one of the smallest `r+1` is unblocked."
  This is a genuinely different *mechanism* (a counting/pigeonhole argument
  bounding the effect of a bounded-size adversary directly, no exchange
  moves, no LP vertices) — see Framing 3 below for how it might transplant.
- `aimo-0146` (university dinner degree problem) — "weighted sum of a sorted
  sequence, maximize by exchange-smoothing until few profiles survive" — same
  family as what's already been tried (Lemma V' is exactly this), not new.

No crux gave a ready-made theorem for "alternating claiming preceded by a
two-sided cutting phase," so any new framing below is genuinely being
adapted, not imported.

## Candidate new framings

### Framing 1 — Minimax over *mixed* (randomized) Xiang-Yu strategies (LP duality on the *true* infinite strategy space)

**Idea.** `equalization-potential-bound` proved that no single **rank-only
linear functional** `Σw_i p_i` can give a valid tight bound (Lemma D/E:
forced to the tautological constant `w_i≡c(n)`). `potential-averaging-bound`
proved that averaging **2–3 named, deterministic, budget-greedy** strategies
also fails. Neither result touches the actual von Neumann minimax object:
Xiang Yu's *full* mixed-strategy simplex over all combinatorial split-types
(not 2-3 hand-picked pure strategies, and not a rank-only linear weight on
`A`). The correct dual object is: for fixed `A`, is there a **probability
distribution over Xiang-Yu pure strategies** (each a legal ≤n-mark response)
whose *expected* `oddrank` is `≤ c(n)Σ(A)` for *every* `A` simultaneously?
By minimax/LP duality (finite game for each fixed combinatorial type-count,
since split ratios within a type are continuous but the value is
piecewise-linear — exactly Lemma V's structure), such a mixed strategy is
*guaranteed to exist* abstractly (minimax theorem) since we already know
`max_A min_B oddrank(B) = c(n)Σ(A)` is the claimed value; the open question
is only whether it has a *short, explicit* description, not whether it
exists. This reframes the whole upper bound as: **exhibit an explicit
randomization over the DOM/HALVE/TAIL-SNIP/two-piece moves already
discovered, weighted by a function of `A`'s shape, and show the expectation
inequality holds by a single unified computation** — rather than 2-3 fixed
candidates or exact-minimizer casework.

**How far it could plausibly get.** This is a genuine change of proof
*shape* (a probabilistic/expectation argument replacing exact-minimizer
casework), distinct from every current live approach. It directly targets
the diagnosed failure mode of `potential-averaging-bound` (which failed
*because* it used only 2-3 deterministic candidates, not a genuine
distribution) without duplicating `universal-adversary-strategy`'s exact
casework. Risk: finding the *right* mixing weights is itself potentially as
hard as the direct casework (the minimax theorem guarantees existence, not
an explicit clean formula) — this is real, comparable-difficulty work, not a
shortcut, and is honestly likely to hit the same "coordinated two-piece
regime" wall unless the mixing distribution is cleverly chosen to
average out that regime's interleaving pattern (plausible: an expectation
argument is exactly the right tool for "average behavior over interleaving
patterns," which is the thing that keeps defeating deterministic local
moves). Worth one exploratory outline slot; moderate-to-good chance of
producing *new* structural insight even if it doesn't fully close the gap
this round.

### Framing 2 — Continuous relaxation: `n` as a continuous parameter, calculus on `[0,1]`

**Idea.** Every current approach treats `n` and the mark budget as
irreducibly discrete/combinatorial (compositions, integer multiplicities,
LP vertices with integer block lengths). An entirely different route:
relax to the continuum limit — treat the "budget" as a continuous resource
`t∈[0,n]` and Liu Bang/Xiang Yu's choices as measures/functions on `[0,1]`,
derive an ODE or self-consistency functional equation for the extremal
configuration density directly (in the spirit of continuous "cake-cutting"
literature), then discretize/round at the end to recover the exact integer
answer `2^n/(2^{n+1}-1)`. The self-similarity already found
(`c(n)=2λ_n c(n-1)`, ratio-2 geometric structure) is exactly the kind of
fixed-point relation a continuous functional-equation approach would derive
*directly*, potentially without needing the block/parity casework that Lemma
PARITY-PAIR required.

**How far it could plausibly get.** This is attractive for *re-deriving*
already-proved facts (the `k=n` tail-untouched case, Lemma L) more cleanly,
but I judge it **unlikely to help with the two genuinely open gaps** (general
`k<n` with tail simultaneously refined; the coordinated two-piece upper-bound
regime), because those gaps are governed by exact integer/parity phenomena
(Lemma PARITY-PAIR's odd/even case split; the discrete "budget" interacting
with a specific finite mark count) that a continuum relaxation would average
away, not resolve — continuous relaxations are good at finding *candidate
optimal shapes* but this problem's hard part is proving no *discrete*
deviation (bounded number of marks) beats the shape, which is precisely a
non-continuum fact. Low-to-moderate priority; could be useful only as a
sanity/intuition tool alongside another framing, not as a standalone route.

### Framing 3 — Direct pigeonhole/counting argument on the mark budget (adapted from `aimo-0718`'s "adversary blocks ≤r objects" crux)

**Idea.** `aimo-0718`'s crux move: when a greedy actor faces an adversary
that can block at most `r` objects, pigeonhole on the smallest `r+1` objects
— at least one is always unblocked. Transplanted here: Liu Bang has `n+1`
pieces, Xiang Yu has only `n` marks. Rather than asking "how does Xiang Yu
best distribute his marks among pieces" (the question every current approach
asks), ask the *dual* counting question directly for the **upper bound**:
for an *arbitrary* configuration `A` with `m` pieces, since Xiang Yu has `n`
marks and needs (by the certified Lemma DOM-boundary-slack / "splitting into
`j` parts costs `j-1` marks") a specific number of marks to neutralize each
dominant piece, is there a clean **counting/charging inequality** — bounding
`oddrank(B)` below using only *how many* pieces exceed a threshold and how
many marks are available to touch them, not their exact values — that
avoids the "jointly-optimized non-half ratios" casework entirely? This is
different in kind from Lemma DOM/HALVE (which are exact identities for
*specific* split constructions) — it would be a genuine *inequality* argument
using only counts and a threshold, in the pigeonhole style.

**How far it could plausibly get.** Honestly, moderate skepticism: the
already-certified counterexamples (e.g. `universal-adversary-strategy`'s
`(4649/10000, 3042/10000, 2309/10000)` witness, where the optimum needs
*non-half*, jointly-tuned ratios) show that **any argument depending only on
counts/thresholds and not on the exact values will very likely be too weak**
— the current field's hardest-won lesson is that exact values (not just
"how many pieces are big") matter. This framing is worth a *quick* explicit
test against that witness (does *any* natural charging scheme reproduce
`4/7`-scale tightness there?) before committing real build effort; if it
fails on that witness immediately (plausible), it's a fast, cheap way to
rule out a whole family and should be reported as such rather than silently
dropped. Low-to-moderate priority, but cheap to falsify.

### Framing 4 — Entropy-style potential, structurally different from both `equalization-potential-bound`'s linear functional and `majorization-smoothing`'s concavity claim

**Idea.** Both dead approaches tried a single *global scalar functional* of
`A` — a linear rank-weighted sum (killed by the interior-point/constant-
functional obstruction, Lemma D/E) and *concavity of `V(A)` itself* (killed
by the convex-kink-inside-min mechanism). A genuinely different scalar
functional shape — e.g. a **strictly convex** potential like `-Σ p_i log p_i`
(entropy) or `Σ p_i²` — was not tried. Since `majorization-smoothing`'s own
finding was that `V(A)` contains a *convex* kink nested inside a min, a
convex (not linear, not concave) candidate potential is at least not
immediately ruled out by either existing negative result.

**How far it could plausibly get.** Weak — this is speculative and I did not
find any concrete reason to expect an entropy potential to interact well
with `oddrank`'s combinatorial (rank-parity) definition; `oddrank` is
piecewise-linear-in-values-for-fixed-order-type, and there's no known reason
a strictly convex potential's extremal points would align with the
geometric-doubling optimum. I list this only for completeness/diversity;
recommend **not** allocating a build slot to it without first doing a cheap
numeric check (does `c(n)` fall out as a stationary point of any natural
convex potential on `Δ_n` under the known constraint structure?) — if that
quick check fails, drop it immediately.

## Recommendation for the outliner

Of the four, **Framing 1 (mixed-strategy / minimax LP duality over the true
infinite pure-strategy space)** is the strongest candidate for a genuinely
new build slot: it is conceptually far from "peel one element / exchange one
move / LP-vertex on one composition," it directly targets the diagnosed
weakness of the already-tried averaging attempt (too few, too rigid
candidates) rather than repeating it, and a partial result (e.g., an explicit
mixing rule that closes the near-tied-top-two / coordinated-two-piece regime
specifically, even if not all of `k<n`) would be new information regardless
of whether it fully closes the theorem. **Framing 3** is worth a cheap
5-minute numeric falsification check against the existing hard witness
before any real build effort. **Framings 2 and 4** are lower priority;
mention only if the outliner wants a fourth, more speculative diversity slot.
