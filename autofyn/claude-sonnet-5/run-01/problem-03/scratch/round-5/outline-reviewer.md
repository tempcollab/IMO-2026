# Outline review — imo-2026-03, round 5

Field reviewed: `recursive-embedding-induction` (advance), `geometric-dominance-construction`
(advance), `universal-adversary-strategy` (advance), `potential-averaging-bound` (new).

## recursive-embedding-induction — APPROVE

Target: whole theorem, lower-bound half (owns Lemma L, the `k=n` tail-untouched
sub-case, via peel-the-top-block strong induction on `n`).

- Reduction chain (Lemma V' → Lemma L) is already certified from round 4; this
  round's new step is a legitimate strong induction: peel the top block of
  multiplicity `c_1`, use Lemma D-INSERT to get its exact signed contribution
  to `D` (by parity of `c_1`), then apply the IH at `n-1` to the *rescaled*
  remainder, which by Lemma 3's self-similarity is genuinely a level-`(n-1)`
  instance. This is not circular — it inducts on a strictly smaller `n` with a
  proper base case (`n=1`, certified Lemma G0).
- Case coverage for the induction step is honestly declared incomplete
  ("not yet verified whether both sub-cases give a sufficient inequality") —
  this is a legitimate build-time gap, not an outline defect: the two cases
  (odd/even `c_1`) are exhaustive by construction (parity has only two
  values), so no case is silently missing from the *outline* itself.
- Watch-out about not falling back to a sums-only bound is correctly carried
  over from the round-2 counterexample (memory rule respected).

No fatal flaw. Proceed to build.

## geometric-dominance-construction — APPROVE, with a scoping note

Target: whole theorem, lower-bound half, via a single-unit exchange/local-move
argument on composition vectors of `p_1`, claimed to close ALL `0≤k≤n` at once
(of which `k=n` recovers Lemma L).

- I verified the outliner's claim that Lemma L (recursive-embedding-induction)
  and the `k=n` instance of this approach's "doubling family" conjecture are
  the same object: `C_n = {p_2,...,p_n,p_{n+1},p_{n+1}}` reduces via Lemma 2's
  identity `p_1-Σ_{i=2}^{n+1}p_i=p_{n+1}` to exactly Lemma L's canonical
  vector (`a_i=1` for `i<n`, `a_n=2`). Confirmed by direct substitution
  (`math-explorer-lemmaL.md`), so the outliner's claim is not hand-waved.
- The exchange-monotonicity claim itself (Step 2, "single-unit exchange never
  increases oddrank(merge), canonical vector is the unique local hence global
  minimum") is correctly flagged as untested — the outline says the fastest
  derisking check (numeric verification for `n` up to ~10) has "not yet been
  done." This is the right kind of open gap to send to a builder (a concrete,
  falsifiable numeric pre-check), not an unmotivated leap.
- Memory-rule compliance: correctly avoids retrying the 2-scalar/3-scalar
  abstraction already falsified this round for `s≥3` (Claim ★ counterexample).

**Coordination flag (per dispatch instruction).** Both this approach's Step 2
(exchange argument, general `k`) and recursive-embedding-induction's Step 2
(peel-the-top-block induction) are, at `k=n`, literal proofs of the *same*
underlying combinatorial statement (Lemma L / the doubling-family minimum at
`k=n`), attacked this round via two genuinely different mechanisms
(discrete-exchange/connectivity argument vs. strong induction with parity
case-split). Per the standing memory rule ("two approaches sharing one lemma
with distinct central novel mechanisms are legitimate rivals, not the
single-gap trap, when there's positive evidence the shared lemma is true" —
here backed by exact enumeration up to `n=7-8`), this is acceptable parallel
exploration, not the CLAUDE.md single-gap trap (neither approach is a bare
slice of the other's proof — each targets the *whole* lower-bound half via
its own route, and `geometric-dominance-construction`'s route additionally
must cover `k<n`, which `recursive-embedding-induction` does not attempt).
That said, this is real duplicated effort on the `k=n` instance specifically.
**Directive to the builders:** do NOT have both builders independently write
out a full symbolic proof of the `k=n` case in parallel to the end — each
should first spend a bounded amount of effort (numeric derisking: does the
claimed monotonicity/parity mechanism survive `n` up to ~10?) before
committing to the full write-up; if one lands a certified Lemma L first, the
other should import it by reference for its own `k=n` corollary rather than
re-deriving, exactly as `geometric-dominance-construction`'s own outline
already says ("import that result once certified rather than re-deriving").
If both land proofs independently, that's a bonus (cross-check), not a
conflict — but neither should re-do this if the other's proof is already
certified and available before it starts writing.

## universal-adversary-strategy — APPROVE

Target: whole theorem, upper-bound half, over arbitrary (non-geometric)
configs, via joint `(m,r)`-indexed cascading DOM/HALVE induction.

- DOM-boundary-slack (the `r=0` case costs `k-1` marks, not `k`) is a
  concrete, checkable mechanical fact, not a bare label; math-explorer's
  round-5 numerics independently confirm it on two examples (3- and 4-piece)
  — consistent with, not contradicting, the outline.
- Correctly identifies and does NOT paper over the newest sub-case: when
  neither DOM's nor HALVE's hypothesis fires (near-tied top two), the optimal
  move can skip the top and act on a deeper piece — this is flagged as an
  open case needing its own lemma, matching this round's explorer numerics
  exactly (a genuine, not manufactured, gap).
- Correctly avoids the round-3 memory trap of defaulting to "induction on `n`
  alone" — explicitly commits to the joint `(m,r)` induction.

No fatal flaw. Proceed to build; case (c) (near-tied top two) is the priority
target.

## potential-averaging-bound — CHANGES REQUESTED (feasibility gate, not a rejection)

Target: same upper-bound half, via a genuinely different proof *shape*
(additive/averaging: `min(strategy_1,strategy_2) ≤ average`, borrowed from
aimo-0198) rather than exact-minimizer casework.

- **Is this a real new framing, not a bypass?** Yes. It changes the logical
  structure of the argument, not just which threshold is used: instead of
  proving which of DOM/HALVE is truly optimal in each regime (what
  `universal-adversary-strategy` is doing), it tries to prove a *weaker,
  additive* statement that is sufficient regardless of which is truly
  optimal. This is exactly the kind of "genuinely different framing" the
  standing rule calls for when a field risks collapsing into one wall — it
  does not share `universal-adversary-strategy`'s case-by-case wall (the
  near-tied-top-two case) by construction, since it never needs to determine
  who wins that case, only that the average of two *available* strategies
  clears the bar.
- **But it is self-flagged as failing in its simplest form.** The outline
  itself states a first numeric spot-check found the naive average of the
  FLAT (non-cascading) DOM/HALVE values violates the target bound exactly in
  the region where neither DOM's nor HALVE's hypothesis fires — i.e., the
  proposed fix (Step 4, "must use cascading forms") is not yet verified to
  work, and the outline itself concedes a third candidate may be needed. Per
  the standing rule ("when an approach self-flags a possible fatal
  invalidity, take it seriously — CHANGES REQUESTED with a concrete
  falsifiability gate, not a rubber-stamp APPROVE"), this cannot be a plain
  APPROVE.
- **Directive to the builder:** treat round 5 as an explicit feasibility
  probe, exactly as the outline's own "Open gaps" section proposes. Before
  writing any inductive proof: numerically test (exact-`Fraction` or
  high-precision, n=2..5, several configs including the near-tied-top-two
  region already found to break the flat average) whether
  `(cascading-DOM value + cascading-HALVE value)/2 ≤ c(n)Σ(A)` holds. If it
  fails anywhere, do not force a proof — report the counterexample and
  either construct the needed third candidate strategy explicitly (targeting
  exactly the near-tied region) or report this framing as a documented
  negative result. Do not silently fall back to exact-minimizer casework
  (per the outline's own warning) — that would collapse it into a copy of
  `universal-adversary-strategy` and lose the diversity value.

Registered into the population (`register_approach`, cold-start Elo).

## Field diversity assessment

Two independent halves are covered by genuinely different techniques:
lower bound (`geometric-dominance-construction`'s exchange argument vs.
`recursive-embedding-induction`'s peel-induction — both reduce to the same
`k=n` crux `Lemma L` but via different mechanisms, flagged above) and upper
bound (`universal-adversary-strategy`'s exact cascading casework vs.
`potential-averaging-bound`'s additive/averaging shape — genuinely different
proof structures, not variations of one framing). This is healthy diversity;
no sign of a field-wide single-wall collapse this round. The one real
duplication risk is the `k=n` Lemma L crux shared by the two lower-bound
approaches, addressed via the coordination directive above rather than by
cutting either.

## Ranking

Folded round-4 outcomes (`geometric-dominance-construction` advanced,
`recursive-embedding-induction` advanced, `majorization-smoothing`
confirmed dead-end) and round-2 outcome (`universal-adversary-strategy`
advanced, stagnant since) into Elo via `update_ranking`, anchoring the new
`potential-averaging-bound` against established approaches (beats the
confirmed-dead `majorization-smoothing` and the stagnant `equalization-
potential-bound`, loses to the three actively-advancing approaches).
Post-update order: `geometric-dominance-construction` (1594) >
`recursive-embedding-induction` (1587) > `universal-adversary-strategy`
(1532) > `potential-averaging-bound` (1482) > `majorization-smoothing`
(1424, dead-end, kept as negative-result record only) >
`equalization-potential-bound` (1380, stagnant since round 1).

build set: geometric-dominance-construction, recursive-embedding-induction, universal-adversary-strategy, potential-averaging-bound
