# Outline-reviewer report — round 6 — imo-2026-03

Read: `/tmp/round-6/proof-outliner.md`, all seven live approach files (full
text, including the round-6 edits in place), and `results/imo-2026-03/current.md`.

## Verdicts per approach

### `recursive-embedding-induction` — ADVANCE, top of field
Round 5's Lemma L (fully proved, reviewer-verified) is a genuine landmark —
confirmed by re-reading the proof and the reviewer's independent
re-derivation record in `current.md`. Round 6's PARITY-PAIR-GEN skeleton is
a sound, well-motivated direct generalization (not a repeat of the
already-falsified Claim ★ abstraction), correctly scoped down to `k=2`
first as a de-risking step, and correctly cedes the free-coordinate item to
its sibling rather than duplicating effort. No issues. Ranked #1.

### `universal-adversary-strategy` — ADVANCE
The round-6 correction (single-piece tie-split suffices for the round-5
witness, not a coordinated 2-piece move) is exactly the kind of self-audit
this population should reward — it prevents a wrong framing from being
built on. Lemma TIE-NECESSARY's proof sketch is a clean, direct application
of the already-certified interior-point obstruction (correctly reused, not
re-derived) to convert continuous optimization into a finite cell search;
Lemma PARTIAL-DOM is a mechanical extension of the certified Lemma DOM
proof technique. Both are legitimately low-risk. The flagged (not
assigned) even-`m` two-independent-ties phenomenon is honestly scoped as
future work, with a sound cross-approach question (does Lemma PARITY-PAIR
transfer). Ranked #2.

### `geometric-dominance-construction` — RE-SCOPE, confirmed
Verified the round-5 negative result (Lemma X + move-traps) is rigorous,
not a bare numeric failure, and that ceding Lemma L to the sibling (rather
than re-deriving) was the right call. The round-6 re-scoping to the "one
free coordinate" vertex case of Lemma V' is checked against
`recursive-embedding-induction`'s file: that approach's round-6 section
explicitly states "Gap (1) ... is not targeted this round by this
approach — it is being re-scoped as the primary target of
`geometric-dominance-construction` instead," confirming this is a genuine
cession, not a race condition or silent duplication. The target itself
(the uncovered "one free coordinate" vertices of the split polytope, as
opposed to the pure-anchor vertices Lemma PARITY-PAIR already covers) is a
real, non-trivial, well-defined gap distinct from PARITY-PAIR-GEN (that
targets the tail; this targets the split-of-`p_1` structure with tail
untouched) — not a duplicate. Approved to keep its slug alive at this
scope. Ranked #3 (no proof advance this round, but the round-5 negative
result plus correct coordination keeps it ahead of the weaker field
members).

### NEW `minimax-mixed-duality` — APPROVED, registered
Checked against the standing feasibility-gate rule and the diversity
requirement:
- **Genuine different framing, verified.** Every live and dead approach on
  file (recursive peel-induction, exchange moves, direct casework,
  rank-weight LP, cascading-candidate averaging, global concavity) is a
  **deterministic** local-move or single-functional mechanism. This
  approach's mechanism — an **`A`-dependent mixed strategy** whose
  expectation is bounded, with weights derived from a per-instance dual LP
  — is a structurally different proof device (a probabilistic/expectation
  argument, not a fixed rule or a fixed small candidate set). Confirmed
  this is not a relabeling.
- **Not a rehash of `equalization-potential-bound`.** That approach's
  object is a single, `A`-*independent* rank-weight functional over
  configuration space, proved impossible by the interior-point argument
  (Lemma D/E) because the conjectured optimum sits in the relative
  interior of the ordered simplex. `minimax-mixed-duality`'s object is a
  **per-`A`** distribution over *responses* to a fixed `A` — a different
  mathematical object living in a different space (the response polytope
  for fixed `A`, not the configuration simplex), so Lemma D/E's
  obstruction does not automatically transfer. The file states this
  distinction explicitly and correctly.
- **Not a rehash of `potential-averaging-bound`.** That approach's
  failure mode (verified: `A=(1/3,1/3,1/3)` forces every one of 3
  hand-picked, `A`-independent, budget-blind candidates above the bound)
  is diagnosed as a failure of *fixed, context-free* candidates. This
  approach's mixture weights are explicitly **derived from `A`** (Gap 2:
  solve the dual LP per instance, look for a closed-form pattern), which
  directly targets that diagnosed weakness rather than repeating it.
- **Feasibility gate.** Per the standing rule that new approaches need a
  falsifiability/soundness check before a full build effort, this
  skeleton correctly does **not** claim the hard step (Gap 3, the
  expectation inequality) is easy — it is explicitly flagged as "possibly
  as hard as direct casework," and the plan scopes the first build pass to
  the *exploratory* gaps (formalize the finite-type decomposition; search
  numerically for a closed-form weight pattern on two known hard witnesses)
  before committing to Gap 3. This is exactly the right shape for a
  first-round new approach: cheap to falsify, not yet oversold. Von
  Neumann-style existence of *some* dual object is not in question; what's
  open is explicitness, which is honestly stated. Registered at the
  cold-start Elo.
- **Lower-bound scope honestly limited.** Gap 4 correctly flags that the
  mixed-strategy device is primarily an upper-bound tool and defers to
  `recursive-embedding-induction` for the lower bound rather than silently
  dropping half the theorem — acceptable under CLAUDE.md's whole-problem
  requirement since the file states the scoping explicitly rather than
  hiding it.

Registered via `register_approach`.

### `potential-averaging-bound` — RETIRED this round (not in build set)
Outliner's retirement recommendation is correct and I am acting on it.
Re-verified the round-5 record: the feasibility gate was executed properly
and failed with a clean exact counterexample; the file's own round-5 note
already conditioned continued life on "a further attempt at a budget-aware
third candidate," and no such attempt was made this round (per its own
round-6 note, correctly self-reported rather than silently carried
forward). Its diagnosed fix is structurally identical to what
`universal-adversary-strategy` is now proving directly (Lemma
TIE-NECESSARY / PARTIAL-DOM), and its diversity role (a genuinely
different upper-bound proof shape) is now better filled by
`minimax-mixed-duality`, which is an actual expectation argument rather
than 2–3 fixed deterministic candidates. Kept in the ranking pool (ranked
last of the active four, reflecting its Elo) but **not included in the
build set** — no further build slot unless a future round proposes a
genuinely new, non-duplicative mechanism. Not hard-deleted (per the
ranker's design, a losing approach is down-sampled, not destroyed), so it
remains available for revival if warranted.

### `majorization-smoothing` — confirmed still dead, not re-litigated
Left untouched, per the orchestrator's explicit instruction and my own
independent read of round 4's non-concavity proof (a convex kink nested
inside a min — a structural obstruction, not a numeric artifact). Correctly
excluded from the build set again.

### `equalization-potential-bound` — stagnant, correctly excluded
Round-1 record stands (Lemma D/E interior-point obstruction against any
`A`-independent rank-weight functional). Not touched, not in the build set.

## Ranking update

Registered `minimax-mixed-duality` at the cold-start Elo (1500, no
comparisons yet — it has no build outcome to rank against). Folded round-5
outcomes into Elo for the four approaches with fresh (`stale: true`)
records, ordered by round-5 substance (recursive-embedding-induction's
proved Lemma L > universal-adversary-strategy's two new general lemmas >
geometric-dominance-construction's rigorous-but-non-advancing negative
result > potential-averaging-bound's failed gate):

- `recursive-embedding-induction`: 1587 → **1627**
- `geometric-dominance-construction`: 1594 → **1571**
- `universal-adversary-strategy`: 1532 → **1550**
- `potential-averaging-bound`: 1482 → **1448**

All four cleared of `stale`. `equalization-potential-bound` (1380) and
`majorization-smoothing` (1424) untouched, correctly excluded from this
round's comparisons (dead, not competing for build slots).

## Build-set decision

Confirmed the outliner's recommendation. Four slugs, each with a
concrete, non-overlapping, well-scoped target this round:

1. `recursive-embedding-induction` — Lemma PARITY-PAIR-GEN, scoped to
   `k=2` tail-refined.
2. `universal-adversary-strategy` — Lemma TIE-NECESSARY and Lemma
   PARTIAL-DOM.
3. `minimax-mixed-duality` — first exploratory pass, Gaps 1–2 only (finite-
   type decomposition + empirical weight-formula search on the two known
   hard witnesses), not yet Gap 3.
4. `geometric-dominance-construction` — the "one free coordinate" vertex
   case of Lemma V'.

`potential-averaging-bound` retired from build slots this round (not
deleted). `majorization-smoothing` and `equalization-potential-bound`
correctly excluded (dead/stagnant).

build set: recursive-embedding-induction, universal-adversary-strategy, minimax-mixed-duality, geometric-dominance-construction
