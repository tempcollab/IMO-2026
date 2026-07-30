# Outline review — imo-2026-06, round 1

Verified the outliner's example data by direct simulation (python, greedy generation):
- a_1=15: confirmed tail difference pattern has period T=8 summing to L=30 (matches outliner claim).
- a_1=105: confirmed tail period T=58 summing to L=210 (matches outliner claim).

**Important finding that sharpens the outliner's flagged risk into a confirmed fact:** for a_1=15,
S=primes(a_1)={3,5}, L0=15. The actual minimal period uses L=30=lcm(2,3,5) — prime 2 (not a factor
of a_1) is provably pulled into the periodic structure. I checked directly: the true diff-cycle
(2,4,6,6,4,2,3,3, sum 30) does **not** collapse to any period-4 sub-pattern summing to 15 (2+4+6+6=18
≠ 15), so the process is genuinely *not* determined by a_n mod 15 alone — it depends on parity
(mod 2) too. So any approach whose finite state/modulus is built purely from S = primes(a_1) is
**not just "possibly too coarse" but demonstrably insufficient** to pin down the true eventual
recursion. This is the load-bearing content the outliner flagged as a "watch out" risk; treat it now
as a required fix, not a residual risk, for every approach that builds its state from primes(a_1) alone.

## core-signature-pigeonhole — CHANGES REQUESTED

Sound skeleton, cleanly separates the easy sufficiency direction (step 4) from the hard necessity
direction (step 5, "No-Escape Lemma"), and correctly self-flags the S-too-coarse risk. But:
- **Fix required, not optional:** as shown above, S must be redefined as (or enlarged to) the true
  set of primes that ever become "permanently active" in the process — not just primes(a_1). The
  chain-stabilization pigeonhole in step 2 is stated over the *fixed* poset P(S)\{∅} for
  S=primes(a_1); if the real active prime set is larger, that pigeonhole argument needs to be run
  over the correct (a priori unknown, to-be-shown-finite) prime set instead. The builder must either
  (a) prove the eventually-active prime set is finite and bounded in terms of a_1 (this is new
  content, not in the current skeleton), or (b) restructure the whole signature argument around an
  adaptively-growing S. State this explicitly as an added lemma, not folded silently into step 5.
- Step 5's proposed mechanism ("a fixed extra prime q can only rescue boundedly many indices") is
  named but not proven, and its own sub-claim (b) is explicitly marked open by the outliner — keep
  as an open gap, this is fine for a first pass, but the builder must not hand-wave past it.
- Case coverage: prime-power base case is fine as sanity check; general case is the substantive one,
  correctly identified.

## growth-bound-density — CHANGES REQUESTED (strongest of the four)

- Step 3's bound a_{n+1}-a_n ≤ L0 = ∏(primes of a_1) is **fully rigorous and independently
  verifiable**: the next multiple of L0 after a_n is divisible by every prime of S, hence
  automatically meets every possible nonempty D_i ⊆ S regardless of signature bookkeeping. I re-
  checked this argument step by step — it holds with no missing case. This should be certified as a
  standalone lemma in `results/imo-2026-06/lemmas/` once a builder writes it up, since it's
  technique-independent and reusable by the other approaches.
- Step 4 (finite window of length L0 + residue mod M determines the whole future) inherits the same
  flaw identified above: a window of S-profiles (S=primes(a_1) only) cannot see prime 2's role, so
  as literally stated this window is not sufficient — same required fix as core-signature-pigeonhole
  (the window's alphabet needs to be built over the correct expanded active-prime set, or M must be
  enlarged to include small primes outside S that the L0-bound's own proof doesn't rule out). Flag
  this precisely to the builder rather than letting "window sufficiency" pass as a technical detail.
- This approach's decomposition (rigorous bound now, periodicity gap isolated later) is cleaner than
  the sibling's, and gives the population one clean, certifiable lemma even if the harder half stalls
  — this is why it ranks first this round.

## monovariant-telescoping — CHANGES REQUESTED, kept for diversity, lowest priority to build

- Genuinely different top-level object (per-prime valuation depth vs. global signature-family
  combinatorics) — worth keeping in the population purely for framing diversity per CLAUDE.md's
  anti-collapse rule.
- However it is the least developed: no monovariant has actually been found (step 1/2 explicitly says
  "weights/direction TBD — open"), so there is no verified mechanism yet, only an aspiration. This is
  weaker than a "lemma named without mechanism" — it's a *lemma not yet even conjectured concretely*.
  Not fatal for round 1 (still early), but the builder should be told: either find and verify a
  concrete Φ(n) with a proven monotonicity direction in the first pass, or report back that no such
  monovariant exists in this form, rather than spending the round elaborating around the gap.
- Step 4 (extension to primes outside a_1) already correctly anticipates the exact issue confirmed
  above by simulation — good self-awareness, but it's exactly the same finite-active-prime-set
  question that core-signature-pigeonhole and growth-bound-density also need. Not an escape from the
  shared wall, just approached from a different direction.

## covering-construction-induction — CHANGES REQUESTED but not in this round's build set

- Sub-strategy (a) (refinement-by-induction) is explicitly and correctly self-flagged by the outliner
  as equivalent in difficulty to the No-Escape Lemma — not new content, a relocation of the same gap.
- Sub-strategy (b) (minimal-counterexample from greedy's own minimality) is a genuinely different
  proof *shape*, and is worth keeping registered for the population, but as written it is pure
  aspiration ("the actual contradiction argument... has not been found") with no candidate mechanism
  at all — weaker right now than core-signature-pigeonhole's No-Escape Lemma, which at least has a
  proposed (if unproven) mechanism. Not doomed/wrong-technique, so not a RETHINK, but not worth a
  build slot this round when growth-bound-density and core-signature-pigeonhole are more developed
  and hit the identical wall with more machinery already in place.
- Case coverage (prime-power base case) is fine and correctly trivial.

## Cross-cutting: shared-gap diagnosis (flag for orchestrator)

Three of the four approaches — core-signature-pigeonhole, growth-bound-density, and
covering-construction-induction — all build their finite state from **S = primes(a_1) only**, and I
have now *confirmed by direct computation* (not just suspected) that this S is too small to
determine the true eventual period: the minimal period for a_1=15 needs prime 2, absent from
primes(15). All three reduce to essentially the same underlying question — "what is the true
finite set of primes that eventually become permanently active in the greedy process, and why is
it finite/boundable at all" — dressed in three different proof vocabularies (pigeonhole on
signatures, bounded-gap + finite window, explicit covering-system refinement). This is not yet a
3-round plateau (this is round 1), so RETHINK is premature, but the orchestrator should watch this
closely: if next round all three report back with the same unresolved "why is the active prime set
finite" gap and no new mechanism, per CLAUDE.md's shared-gap-plateau rule the round after should
open a genuinely different top-level framing (e.g., directly bound which primes q > all primes of
a_1 can ever become permanently active, using something like: q can only join if the greedy is
repeatedly forced past a huge gap of q-avoiding candidates, which ties to an explicit
density/counting argument on q itself — this is a candidate NEW framing, distinct from all four
current ones, worth handing to a math-explorer next round regardless of whether the current build
set closes anything).

monovariant-telescoping is the only approach not built around S=primes(a_1) as its base object, so
it remains the field's best diversity anchor even though it is the least mechanically developed.

## Ranking rationale

Ranked growth-bound-density first (its L0-bound lemma is independently verified rigorous, ready to
certify), core-signature-pigeonhole second (cleanest structure, most explicit but same open gap,
drew with growth-bound-density), covering-construction-induction third (drew with
core-signature-pigeonhole on the shared-gap point but its own novel sub-strategy (b) is undeveloped),
monovariant-telescoping last (no mechanism found yet, purely aspirational skeleton) — but kept, not
cut, for framing diversity.

build set: growth-bound-density, core-signature-pigeonhole, monovariant-telescoping
