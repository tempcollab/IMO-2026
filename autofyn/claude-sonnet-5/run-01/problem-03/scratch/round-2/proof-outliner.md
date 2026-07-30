## imo-2026-03

### Population decisions this round

- `geometric-dominance-construction` — **revise** (mark-fungibility extension to close k≥1).
- `recursive-embedding-induction` — **revise** (same extension, but this file already carries
  Lemma 3 / self-similarity and Proposition 4 as its spine — it is the more natural home for
  the fix; treat these two revisions as *twins on the same gap with different scaffolding*,
  not duplicates, since `geometric-dominance-construction`'s Lemma-2-first style and
  `recursive-embedding-induction`'s Lemma-3-first style may each make the fungibility argument
  easier to phrase — worth letting both builders attempt it once, they are cheap given the
  shared certified lemma base).
- `equalization-potential-bound` — **keep alive, reclassify explicitly as a conditional
  negative result**, not advanced this round (no new gap-closing work assigned; its value is
  as a certified structural fact — Lemma D/E — ruling out one shortcut mechanism). Its Status
  should stay `partial` with the explicit caveat already on file; do not mark it `dead` since
  the reviewer's own note says the impossibility claim isn't fully closed either way yet, and
  the file's Lemma D/E are reused as background by the new upper-bound approach below.
- `majorization-smoothing` — **advance** (nominate for the build set). It is an existing,
  distinct-framing, unbuilt skeleton (concavity/smoothing on the continuous value function);
  math-explorer-newframing.md independently converged on essentially the same "KKT/Lagrangian
  on the simplex" idea as the most actionable alternative if the extension stalls, and
  math-explorer-upper-bound.md's opening 3 also lands on the same concavity idea. Advancing it
  gives the population a second independent line of attack on BOTH remaining gaps (k≥1 AND the
  arbitrary-config upper bound) via one mechanism, at low cost since the skeleton already exists.
- **New approach: `universal-adversary-strategy`** — opens the untouched upper-bound-over-
  arbitrary-configurations gap, modeled on crux `aimo-0560`'s "fixed responder strategy caps
  the mover regardless of mover's choice" template, per math-explorer-upper-bound.md's opening 1
  (primary recommendation) combined with opening 2 (Lemma-3 generalization off the geometric
  sequence). This is a genuinely different top-level target than the three lower-bound-focused
  approaches (they all fix `A = A_n`; this one ranges over ALL `A`), so it is real diversity,
  not a technique variant.

---

### geometric-dominance-construction (revise)

Target: For every `n`, `c(n) = max_A min_B oddrank(B) = 2^n/(2^{n+1}-1)`, full proof (both
directions).

Technique: Direct construction (geometric `A_n`) + adversary-response domination, now extended
with a **mark-fungibility reduction** built on the certified doubling identity `p_i = 2p_{i+1}`
(Lemma 3) instead of a fresh per-`k` case split.

Skeleton:
  1. Import Lemma 1 (claiming-phase value = oddrank), Lemma 2, Lemma 3, Proposition A — all
     certified in `lemmas/`.
  2. Import Proposition 4 (Xiang Yu can force exactly `c(n)` against `A_n`, all `n`) — certified,
     gives `min_B oddrank(B) ≤ c(n)` for `A = A_n`.
  3. **New: Lemma F (mark fungibility).** Claim: for the geometric configuration `A_n`, any
     Xiang-Yu response that spends `k ≥ 1` of his `n` marks splitting `p_1` and `n−k` marks
     splitting the tail is *dominated* (in the sense of giving Xiang Yu at most as good a result,
     i.e. `oddrank(B) ≥ c(n)` still holds) by treating one of those top-splitting marks as
     "transferred": because `p_1 = 2p_2` exactly (the `i=1` instance of the doubling identity
     underlying Lemma 3), any split of `p_1` into parts can be re-expressed as producing an extra
     copy of (a piece comparable to) `p_2`, folding the resulting merged multiset into exactly the
     combinatorial shape Proposition 4 already analyzes — by <=n-fold repetition of this folding,
     reduce the general `k` case to the `k=n` case, which is exactly Proposition 4's construction
     (already proved to hit `c(n)` on the nose, never below).
     — mechanism, concretely: show that for ANY split `s_1,...,s_{k+1}` of `p_1` (`Σs_i=p_1`)
     merged with ANY Xiang-Yu-reachable tail refinement `T` of `{p_2,...,p_{n+1}}` using `n-k`
     marks, `oddrank({s_i}∪T) ≥ oddrank({p_2,p_2,...})` for the specific "doubled" multiset
     Proposition 4 constructs with `n` marks all on `p_1` — i.e. prove a **merge-monotonicity /
     exchange inequality**: moving a mark's "location" from inside the top piece to inside the
     tail (or vice versa) while preserving total mark count never lowers `oddrank` below `c(n)`,
     using the interleaving-domination principle already exhibited by hand at `n=2,k=2` in this
     approach's own gate check (recursive-embedding-induction's proof) — generalize that
     order-type argument to hold for ARBITRARY `k` and ARBITRARY simultaneous tail-splitting via
     an induction on `k` (not on `n`): base case `k=0` is Proposition A; inductive step shows
     that increasing `k` by 1 (moving one mark from the tail into the top piece, in the worst
     case for Liu Bang) cannot decrease `oddrank(B)` below the `k-1` bound, by an exchange
     argument using `p_1=2p_2` to compare the two mark placements directly.
  4. Conclude `min_B oddrank(B) = c(n)` exactly for `A = A_n` (Steps 2+3 combine: ≤ from
     Proposition 4, ≥ from Lemma F extending Proposition A to all `k`).
  5. (Deferred to `universal-adversary-strategy`, not re-attempted here) the upper bound over
     arbitrary `A` — this approach's Step 5 explicitly imports that result rather than
     re-deriving it, to avoid duplicated work.

Key lemmas (claim + mechanism):
  - **Lemma F (mark fungibility / induction on k)** — because the doubling identity `p_1=2p_2`
    (and its recursive echo throughout the self-similar tail, Lemma 3) lets any top-split be
    re-expressed as an equivalent tail-split of the *next* level down, so the "which piece gets
    how many marks" case split collapses to a single induction variable `k` rather than a
    combinatorial explosion over interleaving patterns — this is the concrete mechanism the
    k-gap explorer's numerics (flat family of k≥1 optima) point to.

Open gaps: Lemma F itself — the merge-monotonicity/exchange step, proved only at `n=2,k=2` so
far (by exhaustive order-type casework in `recursive-embedding-induction`'s gate check); needs
a genuinely general (all `n`, all `k`, simultaneous tail-splitting) argument, ideally by
induction on `k` using the doubling identity as suggested, not by re-running order-type
casework at each `n`.

Cases to cover: `k = 0` (done, Proposition A), `k = 1,...,n` (open, Lemma F target) — including
the case where the remaining `n−k` marks are themselves spent adversarially on the tail
(simultaneous splitting), which is the part not yet handled even at `n=2`.

Watch out for: do not let the builder just re-verify Lemma F numerically at another small `n`
and call it done — the outline-reviewer flagged this exact risk pattern before (per-`n` hand
checks are not a proof of the general claim). The induction must be on `k` (or equivalently on
"number of marks touching the top"), with an explicit inductive step, not a case enumeration
whose size grows with `n`.

---

### recursive-embedding-induction (revise)

Target: same as above — full proof of `c(n) = 2^n/(2^{n+1}-1)` for the geometric-construction
lower bound; this approach owns Lemma 3 / Proposition 4 and is the natural home for the
self-similarity-based version of the fungibility fix.

Technique: Strong induction on `n`, using the self-similar embedding `tail(A_n) = λ_n · A_{n-1}`
(Lemma 3) as the spine, now extended to directly induct through the k≥1 case rather than
treating it as a separate combinatorial gap from the n-recursion.

Skeleton:
  1. Import Lemma 1, Lemma 2, Lemma 3, Proposition A, Proposition 4 (all certified).
  2. **New: Lemma G (self-similar reduction of the k≥1 case).** Reformulate the k≥1 lower
     bound as an instance of the SAME induction that already proves Proposition 4's tightness:
     since `tail(A_n) = λ_n · A_{n-1}` exactly (Lemma 3), any Xiang-Yu response that splits `p_1`
     with `k` marks and the tail with `n-k` marks can be viewed, after rescaling by `1/λ_n`, as a
     response to the *level-(n-1) subproblem* `A_{n-1}` using some `k'` marks derived from `k`
     plus a piece coming from `p_1`'s split — set up the exact rescaling identity that turns the
     "top piece contributes an extra term" bookkeeping into a clean recursive relation
     `oddrank(B) = c(n) + λ_n·(oddrank_{n-1}(B') - c(n-1))`-type identity (to be derived exactly,
     not assumed — this is the concrete calculus the explorer's "doubling folds top-split into
     extra copy of p_2" observation suggests), then apply the induction hypothesis
     `oddrank_{n-1}(B') ≥ c(n-1)` to conclude `oddrank(B) ≥ c(n)`.
  3. Base case `n=1` (or `n=0`) checked directly (already available from explorer hand
     computations: `c(1)=2/3`, both k=0 and k=1 sub-cases verified by hand).
  4. Conclude the full lower bound `min_B oddrank(B) ≥ c(n)` for `A=A_n`, for all `n`, all `k`,
     by strong induction on `n` (not on `k` — this is the intended DIFFERENCE from the sibling
     revision above, giving the outline-reviewer two independent routes to the same lemma to
     hedge against either induction variable stalling).
  5. Combine with Proposition 4 for equality; defer the arbitrary-`A` upper bound to
     `universal-adversary-strategy`.

Key lemmas (claim + mechanism):
  - **Lemma G (recursive rescaling identity)** — because Lemma 3's exact identity
    `p_{i+1} = λ_n p'_i` lets ANY final multiset `B` arising from a k≥1 response be decomposed
    as (the rank-1 element, exactly `c(n)`, contributed by whichever piece survives from the
    top-split-or-doubling) plus `λ_n` times a multiset that is itself a valid Xiang-Yu response
    to `A_{n-1}` — turning the two-variable case split (`n`,`k`) into a one-variable induction
    on `n` alone, with `k` absorbed into "how the top piece's mass gets redistributed into the
    rescaled subproblem."

Open gaps: making the rescaling identity in Lemma G precise and proving it holds for the FULL
range of how Xiang Yu might split `p_1` (not just the specific doubling split found optimal
numerically) — i.e. proving the decomposition is valid (gives a correct lower bound) for every
`k`-way split of `p_1`, not merely exhibiting it for the optimal one. This is the crux of what
was NOT done this round.

Cases to cover: induction base case(s) `n=0,1`; inductive step must handle every `k` from `0`
to `n` uniformly (that is the point of doing induction on `n` instead of `k`).

Watch out for: this is a genuine alternative decomposition of the SAME gap as
`geometric-dominance-construction`'s Lemma F — the two are not meant to be graded as duplicates;
if one stalls (e.g. the rescaling identity in Lemma G doesn't cleanly emerge), the other
(induction on `k`, Lemma F) is the fallback, and vice versa. Flag to the reviewer that these are
intentionally parallel attacks on one gap via different induction variables, per the copy/twin
spirit of the process (not a literal copy, since the two files already differ substantially in
scaffolding).

---

### universal-adversary-strategy (new)

Target: The OTHER half of the problem, untouched by any live approach: prove
`max_A min_B oddrank(B) ≤ c(n)` for EVERY Liu Bang configuration `A` (not just the geometric
`A_n`) — i.e. Xiang Yu has a strategy, against ANY `A`, guaranteeing `oddrank(B) ≤ c(n)`.
Combined with the lower bound (from the other approaches, imported), this completes
`c(n) = 2^n/(2^{n+1}-1)`.

Technique: **Universal (`A`-independent-in-form) recursive adversary strategy**, modeled on the
crux `aimo-0560` (IMO 2022 P6) template — "replace case-by-case analysis of the mover's choice
with one fixed responder rule, then prove a uniform cap." Here the rule: Xiang Yu always attacks
the CURRENT largest piece of `A`, recursively, splitting it in a ratio that reduces the residual
problem to a smaller instance — mirroring Proposition 4's construction but starting from an
arbitrary sorted `p_1 ≥ ... ≥ p_m` instead of the geometric sequence. Explicitly reject the
"relax Xiang Yu's mark budget" surrogate (confirmed dead end by math-explorer-newframing.md:
extra marks beyond `n` strictly help Xiang Yu below `c(n)`, so budget can't be the relaxed
parameter) — the surrogate/relaxation here must relax SHAPE (which piece gets attacked) not
BUDGET.

Skeleton:
  1. Import Lemma 1 (claiming-phase reduction — applies verbatim to any `A`, not just geometric).
  2. **Cheap-kill / WLOG reduction (Lemma H):** Liu Bang uses exactly `n` marks (`n+1` pieces) —
     using fewer marks is never better (explorer's numeric check, `n=2`: 2-piece configurations
     cap out at `V=0.5 < c(2)`); prove this rigorously by an exchange argument (splitting any
     piece of a sub-maximal-count configuration into two strictly increases Liu Bang's
     achievable value against optimal Xiang-Yu play, or does not decrease it — needs a short
     monotonicity lemma, likely easy given Lemma 1's structure: adding a piece to A only adds a
     move Xiang Yu need not use).
  3. **Cheap-kill (Lemma I, "top-heavy configs are cheap"):** if `p_1 ≥ 1/2` in a given `A`,
     Xiang Yu is structurally forced to touch `p_1` (else `oddrank(B) ≥ p_1 ≥ 1/2`, but we must
     separately show `1/2 < c(n)` is false for checking the OTHER direction is not needed here —
     actually use this only to prune: any config with `p_1` far from `c(n)` is easy to cap, per
     explorer's cheap-kill note) — narrows the interesting regime to `p_1` near `c(n)`.
  4. **Core Lemma J (universal recursive adversary strategy).** Define Xiang Yu's rule
     recursively: given current configuration `A = {p_1 ≥ ... ≥ p_m}` and a mark budget `r`,
     split `p_1` into `p_1 - p_2` (residual) plus `p_2` (a duplicate of the current second piece,
     if `p_1 > p_2`, using 1 mark), then recurse on the new configuration with budget `r-1` — an
     exact generalization of Proposition 4's construction (which does this against the specific
     geometric ratios). Prove by strong induction on `m` (number of pieces) or on the budget `r`
     that this rule caps `oddrank(B) ≤ c(n)` for every starting `A` — the key computation:
     show the resulting `oddrank` after this "shave the top down to match the second piece"
     move is a NON-INCREASING function of applying the rule, and that after `n` applications the
     configuration has been forced into (or below) the shape where Proposition-4-style tightness
     applies.
  5. Conclude `max_A min_B oddrank(B) ≤ c(n)`, combine with the imported lower bound (from
     `geometric-dominance-construction` / `recursive-embedding-induction`, once Lemma F/G close)
     to get `c(n) = 2^n/(2^{n+1}-1)` exactly, both directions, DONE.
  6. State and verify the answer explicitly for small `n` (`n=1: 2/3`, `n=2: 4/7`, `n=3: 8/15`)
     as the required answer-verification step (per CLAUDE.md rigor rules for problems with an
     explicit answer).

Key lemmas (claim + mechanism):
  - **Lemma H (full-budget WLOG)** — because adding an extra piece to Liu Bang's configuration
    only adds an option Xiang Yu need not exploit and possibly shifts rank parities in Liu
    Bang's favor; monotonicity under refinement of `A` itself (dual to Xiang Yu's refinement of
    `A` into `B`).
  - **Lemma J (recursive shave-to-second-place strategy caps every A)** — because repeatedly
    reducing the top piece to match the (formerly) second piece exactly reproduces the
    doubling/geometric structure that Proposition 4 shows is tight against `A_n`, and doing this
    against an ARBITRARY starting configuration can only move it closer to (never further from)
    the worst case for Liu Bang — the mechanism is a potential-function argument: define
    `Φ(A) := p_1 - Σ_{i≥2}p_i` (top-piece surplus, cf. Lemma 2) and show the shave move
    non-increases a bound built from `Φ`.

Open gaps: Lemma J is the whole new mathematical content — not yet proven, only motivated by
analogy with Proposition 4 and by the explorer's numerics (Nelder-Mead converging to `A_n` from
every random start, no perturbation improving `V`). This is real, substantial, unattempted work.
Lemma H is likely easy but not yet written out.

Cases to cover: none extra beyond the induction on `m`/`r`, but the builder must handle the
degenerate case where `p_1 = p_2` (tie) and where fewer than `n` marks are needed to reach the
capped shape.

Watch out for: do NOT reuse the refuted "relax the mark budget" surrogate (dead end, confirmed
numerically twice this round: extra marks let Xiang Yu drive `oddrank` down to `1/2`, well below
`c(n)`) — any surrogate/domination step here must preserve Xiang Yu's exact budget `n` and only
vary the SHAPE of his allowed moves.

---

### equalization-potential-bound (keep, no change this round)

Target: unchanged — was originally framed as a negative result (no rank-only linear functional
gives a tight LP shortcut). No new work assigned this round; Status stays `partial` with the
existing caveat (the impossibility claim depends on the still-open general lower bound). Its
certified Lemma D/E (interior-point-forces-constant, geometric point is strict interior point of
`Δ_n`) are explicitly reusable background for `universal-adversary-strategy`'s Lemma H/cheap-kill
step (both concern the geometry of the ordered simplex). Do not advance or revise this round;
revisit once the lower bound (Lemma F/G) is closed, at which point its "dead end" claim can
finally be checked unconditionally.

---

### majorization-smoothing (advance)

Target: unchanged (existing skeleton) — `c(n) = max_A min_B oddrank(B)` via a smoothing/
concavity argument on the value function, proven WITHOUT induction or explicit adversary
construction. Nominate for the build set as-is: its Step A (Lemma C, concavity of `V(p)` as a
lower envelope of finitely many linear functionals) is the most promising unattempted piece —
both `math-explorer-upper-bound.md` (opening 3) and `math-explorer-newframing.md` (opening 3,
KKT/Lagrangian) independently flagged this exact mechanism as the best alternative if the
extension approaches stall, giving cross-validation from two independent explorers. Builder
should prioritize verifying (or refuting) Lemma C's concavity claim first — per its own file's
"Watch out for," this needs the two-level minimax (Xiang Yu's continuous split params vs.
combinatorial type) to be reduced carefully to a genuine min-of-linear-functions before claiming
concavity.

Open gaps: unchanged from the existing file (Lemma C, Lemma D, the region-enumeration fallback).

---

## Build set recommendation
`geometric-dominance-construction`, `recursive-embedding-induction`, `universal-adversary-strategy`,
`majorization-smoothing`
(`equalization-potential-bound` left un-advanced this round, per above.)
