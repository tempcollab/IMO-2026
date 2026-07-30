# Round 11 — proof-reviewer report (imo-2026-03)

## Scope
Independently re-verified, from scratch (exact `Fraction`/symbolic
arithmetic, not trusting either builder's report), the two slugs built
this round: `universal-adversary-strategy` and
`case-c-secondary-extremality`. Both target the sole remaining gap of the
whole problem: Claim PTBI's Case C (`p_1<\Sigma(A)/2`) of the general
upper-bound induction, for general piece-count `m\ge4`.

## `universal-adversary-strategy` — verdict: CHANGES REQUESTED

**Claim 1 (Route A structural mismatch).** Read
`lemmas/tree-bound-multicluster.md` in full myself. Confirmed: its
statement is `D(B)\ge\tau_m` for *every* forest Xiang Yu can build against
the one fixed geometric configuration `A_n` (anchors `\tau_l=2^{m-l}`) —
a universal-over-responses bound for a fixed adversarial config, not an
exists-a-response-for-every-config statement. Its proof mechanism
(Reductions R1/R2, telescoping over a discrete power-of-2 anchor lattice)
has no analogue when Case C's residuals are generic reals. The builder's
"quantifier direction reversed / no discrete lattice" argument is
structurally sound on independent reading — Route A is correctly ruled
out, not just untested.

**Claim 2 (Route B refutation).** Independently re-derived and re-ran the
generalized 2-simultaneous-top-level-pair construction
(`match(p_1,p_2)`, `match(p_3,p_4)`, reattach residuals + tail, invoke IH
at `m-2`) with fresh exact-`Fraction` code
(`/tmp/round-11/verify_gate.py` covers the tie-count side;
`/tmp/route_b2_check.py`, re-run fresh, covers this side):
- On the known hard `m=5` witness `A=(1826,1563,1520,1514,765)/7188`:
  reproduced `lhs\approx0.51028 < rhs\approx0.51613`, margin
  `\approx0.00585` — **exactly matches** the builder's reported number.
- On the near-uniform-tail family `p_1=0.499`, tail uniform: reproduced
  **strict violations for every `m` tested from 4 to 100**
  (`m=6`: margin `\approx-0.01204`; `m=20`: margin `\approx-1.2\times10^{-6}$,
  still negative; `m=50,100`: negative down to floating-point noise floor)
  — matches the builder's claims exactly, confirmed independently.
- Also re-ran the "honesty check" (`/tmp/true_opt_check2.py`, fresh):
  Nelder-Mead confirms the same uniform-tail witness is closed by
  Lemma PARTIAL-DOM (budget concentrated on subdividing `p_1` alone),
  reaching `\approx0.5$, comfortably under target — so the refutation is
  specifically of the fixed 2-pair template, not evidence Case C fails at
  this witness.
- Verified `c(k)` strictly decreasing (`/tmp/route_a_sanity.py`, re-run) —
  the monotonicity fact underlying the "near-uniform-tail is hardest"
  argument.

**Conclusion.** Both routes are real, correctly-diagnosed negative
results, not false progress or hand-waved failures. This narrows what any
future fixed-template Case C construction must satisfy (must handle both
the 2-pair-plus-halve witness and the long-adaptive-chain witness
simultaneously) — legitimate if negative progress. Case C for `m\ge4`
remains open. **Route: CHANGES REQUESTED** — re-dispatch this slug's
builder to continue; the rest of the approach (lower bound, Cases A/B,
`m\le3`) stays certified and untouched.

## `case-c-secondary-extremality` — verdict: RETHINK

Independently reproduced the builder's exact-`Fraction` computation from
scratch (`/tmp/round-11/verify_gate.py`) on the `m=5` witness
`A=(1826,1563,1520,1514,765)/7188`, budget 4, target `c(4)=16/31`:

- **Construction A** (match/match/match/self-halve chain): final multiset
  `1563,1563,1514,1514,263,263,251,251,6` (4 tied pairs + 1 singleton),
  `oddrank = 1199/2396` exactly — reproduced independently, matches
  builder exactly.
- **Construction B** (three independent self-halves of `p_1,p_2,p_5`,
  `p_3,p_4` untouched): final multiset
  `913,913,781.5,781.5,1520,1514,382.5,382.5,0` (3 tied pairs + 3
  singletons), `oddrank = 1199/2396` — **exactly equal to Construction A**,
  reproduced independently.
- **Algebraic identity check**: independently re-derived both value
  formulas symbolically. `oddrank_A = p_2+p_4+r_1+(p_5-r_1)/2+r_3`
  (`r_1=p_1-p_2`, `r_3=p_3-p_4`) simplifies term-by-term to
  `p_1/2+p_2/2+p_3+p_5/2`. `oddrank_B = p_3+p_1/2+p_2/2+p_5/2` by direct
  inspection of the sorted order. **Identical expression** — confirmed
  this is not a numeric coincidence of this witness's numbers but an
  unconditional algebraic identity, exactly as the builder claimed.

**Assessment of the conclusion drawn.** The builder's own diagnosis is
correct: the tied-pair-count statistic does narrowly select the right
branch on this test (4 vs 3 pairs) but *only because* the two competing
constructions are provably value-equivalent by direct algebra — so
"maximize tied-pair count" supplies no leverage independent of computing
each construction's closed form, which is exactly the open question
`universal-adversary-strategy`'s Routes A/B are already attacking. This is
the same convergence failure mode `minimax-mixed-duality` hit (flagged
explicitly in this slug's own pre-registered risk section). No forward
proof progress was made or claimed. **Route: RETHINK** — matches the
builder's own honest recommendation, independently confirmed rather than
rubber-stamped.

## `current.md` updates
- Prepended a Round 11 review note under `## Status` (still `partial`,
  no change) summarizing both independent re-verifications and the two
  routing decisions.
- Added two `## Approaches tried` entries (one per slug) recording the
  round-11 outcome and pointing back to the Status note for detail.
- No change to `## Current best` / `## Full proof` — no new certified
  lemma or proof content was produced this round; both results are
  negative/diagnostic.

## Ranking tool
Recorded via `mcp__approach-ranker__record_outcome`:
- `universal-adversary-strategy`: outcome `partial`, round 11.
- `case-c-secondary-extremality`: outcome `dead-end`, round 11.

## Scripts used for independent verification (all re-run fresh this round)
- `/tmp/round-11/verify_gate.py` (new, written by reviewer) — exact
  `Fraction` re-derivation of Constructions A/B and their tie.
- `/tmp/route_b2_check.py`, `/tmp/true_opt_check2.py`,
  `/tmp/route_a_sanity.py` (builder's own scripts, re-run unmodified to
  confirm reproducibility, not just re-read as text).
