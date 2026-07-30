# Fresh-framing scouting report (round 15) — imo-2026-03

**Mandate:** the top approaches (`universal-adversary-strategy` and its
satellites) have bottomed out for 4+ rounds (11–14) on one specific
sub-gap inside the `(marks,|A|)` recursive-induction framing: **Lemma
SLACK-COVER**, a general "does a non-contiguous subset-match exist"
existence theorem needed to close Case C (general `m≥4`). Three
independent non-constructive averaging/pigeonhole attempts at this exact
lemma have failed (`case-c-slack-covering` round 14 — exact algebraic
refutation of the whole one-level-averaging-plus-coarse-IH family, every
`m≥4`; `potential-averaging-bound` — falsified by exact counterexample;
`equalization-potential-bound` — proved any linear/rank-only weighting
degenerates to a tautology). Per CLAUDE.md's diversity rule, patching
Case C again inside the same recursive-construction framing is very
likely to hit the same wall one step later. This report proposes fresh
framings for the **whole problem** that are structurally far from (a) the
`solve2`/(marks,|A|)-recursion + move-menu framing, and (b) the
LP/averaging/duality framing (already tried three times —
`minimax-mixed-duality`, `potential-averaging-bound`,
`equalization-potential-bound`, `relaxed-adversary-transfer`, `majorization-
smoothing` — and all five retired/RETHINK/unsolved, each independently
diagnosed as either collapsing back into the same casework or being
provably too weak / non-concave / configuration-independent).

I did **not** attempt any proof; I read `current.md` (rounds 9–14 in
full), skimmed all 11 files in `approaches/`, `knowledge_base.md`, and
queried the crux corpus (`past_crux_moves_database.json`) for
`games-and-strategy`, and free-text for flow/greedy/exchange/Hall-adjacent
techniques.

## Why the two LP-shaped and one tree-shaped alternatives already tried don't count as "genuinely different" going forward

For calibration, so the outliner doesn't re-open these under a new name:
- **Linear/rank-only weighting + concavity** (`majorization-smoothing`,
  `equalization-potential-bound`): both proved, by different routes, that
  any config-independent linear certificate is either false (non-concave
  `V`, exact convex-kink mechanism identified) or tautological (Lemma D:
  an interior conjectured optimum forces the weight vector to be the
  trivial constant). This rules out **any** single global linear/affine
  dual certificate, not just the ones tried.
- **Mixed-strategy/duality over Xiang Yu's move distribution**
  (`minimax-mixed-duality`): two rounds, explicit search for an
  `A`-independent dual/Positivstellensatz-style certificate, found none;
  every witness needed a *different* case-dependent explicit combinatorial
  choice — i.e. the duality dressing added no leverage over direct
  casework.
- **Relax the mark-budget itself** (`relaxed-adversary-transfer`): proved
  the relaxed value `V_∞=1/2` is exactly config-independent (Theorem
  V-INF) — the relaxation throws away all `A`-dependence before any
  truncation step could use it. Structural, not a near-miss.
- **Tree/anchor formalism reuse for Case C** (`universal-adversary-
  strategy` round 11, Route A): a genuine quantifier-shape mismatch
  (existential-response vs. universal-response) plus no discrete
  power-of-2 anchor lattice for generic reals — ruled out as a structural
  dead end, not a numeric near-miss.

So five distinct "avoid the casework" ideas are down. The two proposals
below are chosen specifically because neither is a linear certificate,
a mixed-strategy/duality object, a budget relaxation, or a discrete-tree
reuse — they attack the *existence* question (Lemma SLACK-COVER) with
tools from a different part of combinatorics: **defect/deficiency Hall
theory** (an exact, quantitative fallback when the naive Hall condition
provably fails — which is exactly what happened here) and **exchange-
argument / local-improvement optimality** (a technique that proves a
*specific* explicit strategy is optimal without ever proving an abstract
matching exists).

---

## Framing 1 (primary recommendation): Defect-Hall / König-deficiency existence, with the leftover absorbed by an explicit correction term

**Key idea.** The current gap, precisely: given sorted `A=(p_1,...,p_m)`
with `p_1<Σ(A)/2` (Case C) and a mark budget `m-1`, Xiang Yu needs to tie
`p_1` (or some top block) to a subset of the remaining pieces whose sum
matches, possibly non-contiguously — this is literally a bipartite
"does a subset with the right sum/rank profile exist" question, i.e. a
Hall's-theorem/SDR existence claim (already named in `knowledge_base.md`,
"Hall's marriage theorem / SDR"). All three failed attempts tried to
prove the **full** Hall condition holds for every configuration via
averaging/pigeonhole over sums — and `case-c-slack-covering`'s round-14
work shows this is **exactly, algebraically false** in the worst case
(the uniform-tail family has a negative margin `margin(m) =
(2^m(3-m)-2)/(2(2^m-2)(2^m-1)(m-1)) < 0` for every `m≥4` — not a near
miss, a clean sign flip).

The fix this framing proposes: **don't require the full matching to
exist. Use the deficiency (defect) form of Hall's theorem** — for any
bipartite family, there is always a matching saturating `|X| -
def(X)` vertices, where `def(X) = max_{S⊆X}(|S|-|N(S)|)` is the maximum
Hall-condition violation. This is the crux-corpus technique used in
`aimo-0341` (subtopic `induction-and-construction`, domain
`combinatorics`): *"When a covering lower bound needs each object
assigned to a distinct slot but the full assignment graph may violate
Hall's condition, take a maximum-deficiency argument: peel off the
largest deficient subset, apply Hall to the remainder, then build the
missing/leftover part coordinate-by-coordinate by hand."* The analogous
plan here:
1. Show the "matching graph" for Lemma SLACK-COVER (candidate ties between
   `p_1`/top block and tail subsets, or more generally between any two
   "sides" of the recursive matching problem) has **bounded deficiency**
   — not zero deficiency (which is what the three failed attempts
   effectively needed and which is false), but a deficiency bounded by an
   explicit small quantity (ideally a constant, or `O(1)` independent of
   `m`, or shrinking geometrically). This is a *weaker*, more tractable
   claim than "Hall's condition holds everywhere" — it only requires
   bounding the *worst* violation, not ruling out all violations.
2. Apply defect Hall to get a partial match covering all but a bounded
   "leftover" residual of pieces/value.
3. Handle the leftover directly: since the induction already carries a
   strict-inequality slack margin at every step (`c(m-1)Σ` vs. the
   achieved value — this is exactly the same kind of slack
   `case-c-slack-covering` was trying to spend, but that round showed a
   *specific* one-level-averaging spending mechanism is provably
   insufficient), the goal is to show the bounded defect-Hall leftover is
   small enough to be absorbed by whatever slack margin *does* survive
   once the correct (non-averaged) inductive value is used — i.e. combine
   defect-Hall's quantitative leftover bound with the exact recursive
   value machinery `universal-adversary-strategy` already has (Lemma
   PAIR-VALUE, Lemma BLOCK-RECURSE, Lemma DOUBLE-INSERT-MATCH-VALUE — all
   independently certified), rather than trying to re-derive a new
   averaging inequality from scratch.

**Why this might close the gap where averaging failed.** The three failed
attempts all tried to prove a **zero-slack existence statement**
(a match/cover exists, full stop) using **coarse, one-shot inequalities**
(sum-based pigeonhole, one-level averaging). Defect Hall reframes the
target as a **quantitative deficiency bound** (how far from a perfect
match, not whether one exists), which is a strictly different — and
often much easier — thing to bound: deficiency bounds are typically
proved by a direct combinatorial argument on the *structure* of the
neighborhood sets (e.g. sorted-order interval arguments, using that `A`
is sorted descending, which the current move-menu already exploits for
BLOCK-RECURSE/contiguous matches), not by a global averaging inequality
over all of `A`. It directly targets the diagnosis in `current.md`
(round 14): *"the correct proof must engage with the recursive value of
the leftover, not just its achievable-sum coverage"* — defect Hall is
precisely a leftover-quantification tool, not a covering-existence tool,
so it is aimed at exactly the reframed target the round-14 review
identified, using a genuinely different theorem (König/Hall-deficiency)
than anything tried so far.

**Main risks.**
- The deficiency bound itself might not be uniformly small (could grow
  with `m`) — this needs to be checked computationally first (a cheap
  numeric gate: compute `def(X)` for the actual candidate matching graphs
  on the known hard witnesses, e.g. the uniform-tail family and the `m=5`
  witness `A=(1826,1563,1520,1514,765)/7188`, before investing in a general
  proof) exactly as the outline-reviewer's prior mandatory-gate discipline
  requires for this run.
- Turning a deficiency bound into a *value* bound (not just a
  cardinality/count bound) requires care: standard defect Hall bounds how
  many vertices go unmatched, but here the quantity that matters is the
  *oddrank sum contribution* of the unmatched leftover, which is a
  weighted, order-sensitive quantity, not a plain count — the "build the
  miss coordinate-by-coordinate" step in `aimo-0341`'s technique will need
  a genuinely new argument adapting deficiency-Hall from a
  cardinality-existence statement to a value/sum statement. This is real,
  non-trivial work, not a drop-in reuse.
- Needs an explicit, checkable definition of the bipartite graph
  (candidate ties vs. candidate subset sums) before defect can even be
  computed — this must be set up carefully to match exactly what
  Lemma PAIR-VALUE/SLACK-COVER actually needs, reusing (not re-deriving)
  the already-certified value identities (`lemmas/pair-value.md`,
  `lemmas/double-insert-match-value.md`) as the "value of a match" oracle.

---

## Framing 2: Explicit canonical greedy strategy + adjacent-exchange optimality proof (bypass existence entirely)

**Key idea.** Instead of proving an abstract matching *exists*
(Hall/SDR-style), **define one single, fully explicit, deterministic
algorithm** for Xiang Yu (a function of the sorted vector `A` alone, no
case-by-case choice of "which subset to match") and prove **directly**
that no alternative Xiang Yu strategy beats it, via a **local
adjacent-exchange argument** — the technique used in scheduling-theory
optimality proofs (e.g. LPT-rule / exchange-argument proofs that a
greedy order is optimal) and explicitly present in the crux corpus:
`aimo-0003` (subtopic `invariants-and-monovariants`): *"Reduce an
'invariant under all orderings/permutations' claim to invariance under a
single adjacent transposition, since adjacent transpositions generate all
permutations."* Concretely:
1. Define a canonical greedy rule, e.g. **"process pieces from smallest
   to largest; maintain a running deficit `d` (initially 0); for each
   piece `p_i` in increasing order, if `d>0` first apply it to reduce `d`
   towards 0 (a partial tie), otherwise start a new tie targeting the
   current largest untouched piece"** — a fully mechanical, one-pass rule
   with no subset-existence question, since it never needs to "find a
   subset summing to X"; it always acts on the next available piece in
   sorted order, and any leftover mismatch becomes the new deficit
   carried forward (a single running scalar, not a search over subsets).
2. Prove optimality **not** by showing it's the best among all
   strategies from scratch, but by an **exchange/no-local-improvement**
   argument: take *any* other Xiang Yu strategy, and show a single
   elementary swap (of which two pieces get tied together, or reordering
   two adjacent ties) can only weakly decrease Liu Bang's total (weakly
   improve Xiang Yu's outcome) when it moves the strategy one step closer
   to the canonical greedy rule — the standard "exchange doesn't hurt"
   lemma from scheduling theory, applied here to pairs of ties rather than
   pairs of scheduled jobs. Chaining swaps (finitely many, since the
   configuration is finite) shows the canonical rule dominates every
   strategy.

**Why this might close the gap where averaging/matching-existence
failed.** This sidesteps Lemma SLACK-COVER's existence question
*entirely* — there is no "does a subset exist" step, because the greedy
rule always acts on the literal next piece in sorted order and carries
any imbalance forward as a scalar deficit, never searching for an exact
non-contiguous subset match. The proof burden shifts from a global
existence/covering statement (which needs to hold for *every*
configuration simultaneously, and is exactly what's been refuted in
one-shot averaged form) to a **local, pairwise comparison** (does
swapping these two adjacent moves help or hurt?) — a fundamentally
different and typically much more tractable proof shape, standard in
scheduling/assignment optimality theory and distinct from every framing
tried in this run so far (not a linear certificate, not a mixed
strategy, not a budget relaxation, not a tree-anchor reuse, not an
existence/matching proof).

**Main risks.**
- The canonical "smallest-to-largest running-deficit" rule must actually
  achieve `oddrank(B) ≤ c(m-1)Σ(A)` on the known hard witnesses **before**
  any optimality proof is attempted — this is a cheap, mandatory
  feasibility gate (exactly the run's established discipline): compute
  the deficit-carry algorithm's value on the uniform-tail family (the
  exact refutation witness from `case-c-slack-covering` round 14) and the
  `m=5` witness `A=(1826,1563,1520,1514,765)/7188`, and confirm it beats
  target *before* investing in the exchange-argument proof. If the greedy
  rule itself already misses the target on some witness, this framing is
  dead on arrival and should be abandoned immediately, exactly as
  `case-c-slack-covering` was correctly retired the moment its mechanism
  failed algebraically.
- Exchange arguments are usually easiest for *linear/additive* objectives;
  `oddrank` is a rank-selection functional (which rank a piece lands on
  depends discontinuously on ties elsewhere) — the "does this swap help"
  step needs to handle the same odd/even-rank discontinuity that broke
  `majorization-smoothing`'s concavity attempt (a convex kink from which
  element a tied pair pushes to odd vs. even rank). This is the same
  underlying combinatorial subtlety in a new guise, not a free pass — the
  exchange lemma must be proved to actually be monotone across that kink,
  which is real, unverified work.
- Risk of silently reconstructing the same casework: if "does this swap
  help" ends up needing the same case analysis on tie/rank parity that
  `solve2`'s Move 0–3 menu already encodes, this collapses into a
  relabeling of the existing framing (the failure mode already diagnosed
  for `case-c-secondary-extremality` and `minimax-mixed-duality`) — must
  be checked explicitly at the first build gate, not assumed away.

---

## Recommendation for the outliner

Open **Framing 1 (defect-Hall/deficiency)** as the primary new approach —
it targets the round-14-identified precise reframing ("a joint
covering-plus-recursive-value statement," not a pure covering bound) with
a named, different theorem (König/Hall deficiency) rather than another
averaging variant, and it can reuse the already-certified value lemmas
(PAIR-VALUE, BLOCK-RECURSE, DOUBLE-INSERT-MATCH-VALUE) as building
blocks instead of re-deriving them. Its first build should be a cheap
numeric feasibility gate (compute the actual deficiency of the candidate
matching graph on the two known hard witnesses) before any general proof
effort, exactly per this run's established discipline for new
mechanisms.

Consider **Framing 2 (exchange-argument greedy)** as a second, more
speculative slot if capacity allows — it is farther from the existing
field (no existence/matching content at all) but carries a real risk of
quietly re-deriving the same tie/rank casework; its first build must
include the same kind of mandatory cheap gate (does the explicit greedy
rule even hit the target value on the known hard witnesses) before any
exchange-argument proof effort is invested.

Both proposals are explicitly *not* variations of the recursive
`(marks,|A|)` construction, *not* linear/LP dual certificates, *not*
mixed-strategy/duality objects, and *not* discrete tree-anchor reuse —
they are the two remaining named combinatorial-existence/optimality
techniques (crux corpus: `aimo-0341`'s defect-Hall move; `aimo-0003`'s
adjacent-transposition move) not yet tried on this problem.
