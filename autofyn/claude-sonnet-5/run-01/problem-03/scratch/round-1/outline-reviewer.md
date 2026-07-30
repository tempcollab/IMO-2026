# Outline review — imo-2026-03, round 1

Context checked: `results/imo-2026-03/current.md` (unsolved, fresh workspace),
`/tmp/round-1/proof-outliner.md`, all three explorer reports, and the four
approach files in full. All four outlines correctly build on the shared
**claiming-phase reduction (Lemma 1)** — value of the alternating-claim
subgame on a fixed sorted piece-multiset = odd-rank sum — which the
math-explorer-gamevalue.md report already proves rigorously by strong
induction (exchange on `h(i) = f(S\{a_i})`, monotone in `i`). This is sound;
every approach correctly imports it rather than re-deriving it, and none of
them mistake it for the hard part of the problem.

I ran brute-force/numeric checks (Nelder–Mead over cut-split parameters,
multiple random restarts, exact-rational target comparison) to sanity-check
the load-bearing claims before ruling on each outline:

- Confirmed `c(2) = 4/7` and `c(3) = 8/15` against the geometric
  configuration numerically (matches the conjectured `c(n)=2^n/(2^{n+1}-1)`
  the explorers converged on; math-explorer-gamevalue.md's noisier n=2 search
  toward `3/5` should be treated as the explicitly-flagged-unreliable outlier
  it already admits to being — the other two explorers' exact-fraction
  witnesses are the trustworthy signal).
- Tested the "Xiang Yu concentrates cuts on the single largest piece"
  dominance claim (Lemma A / Lemma 3, shared by two approaches) on both the
  geometric config and an asymmetric config `(0.6,0.35,0.05)`: concentrating
  on the top piece **ties** for the Xiang-optimal value in every case tested
  (sometimes shared with adjacent-piece splits, never beaten). This is
  genuine positive evidence the lemma is TRUE as a *weak* dominance
  statement — good news for approaches 1 and 3.
- Tested concavity of `V(p)` (majorization-smoothing's Lemma C, the
  approach's entire selling point) at `n=2` with `p1=(0.7,0.2,0.1)`,
  `p2=(0.34,0.33,0.33)`, midpoint `(0.52,0.265,0.215)`: got
  `V(p1)=0.55`, `V(p2)=0.50`, `V(mid)=0.52 < (0.55+0.50)/2 = 0.525`.
  **This is a clean, well-converged numeric counterexample to concavity.**
  Re-ran with 5x more optimizer restarts, same clean values — not
  optimizer noise.

## geometric-dominance-construction — APPROVE

Right technique (construct + matching adversary, tied by induction), and the
numerics above directly support both load-bearing pieces:
- Lemma 2 (top-piece domination via the geometric series identity) is a
  clean, already-complete algebraic fact — no issue.
- Lemma 3 (cut-concentration dominance) is currently open but my numeric
  checks support it as a *true weak-dominance* fact (ties, never beaten) in
  two configurations — this de-risks the approach's central open gap
  meaningfully, though it is still not a proof. The builder must still supply
  a genuine exchange argument (e.g. an explicit swap lemma on the odd-rank
  functional), not just cite these numerics.

Issues to fix while building (real but fixable — not fatal):
- Step 2's case analysis ("how the guarantee survives arbitrary cut
  distributions across the tail") is asserted but not carried out. Given
  Lemma 3, this should reduce to: cuts on the top piece only weaken its
  dominance in a way controlled by the induction hypothesis on the tail —
  spell this out, don't wave at "recursively."
- Step 3(b)'s "Xiang Yu splitting p1 alone reduces to an (n)-mark sub-instance
  of the same game" needs the same rigor as Lemma B in
  recursive-embedding-induction — currently just sketched, don't let the
  builder treat it as free once Lemma 3 is in hand.
- State explicitly (as the outline promises to) that piece *order* along the
  stick is irrelevant to the claiming value — cheap to state, easy to forget
  in the write-up.

## equalization-potential-bound — CHANGES REQUESTED

Genuinely different framing (global LP/weighting vs. case-split), valuable
for diversity. But the outline itself flags the fatal risk clearly: the
weights `w_i` are derived as "worst-case response to THIS configuration,"
which makes the LP linearization circular — you cannot maximize a linear
functional whose coefficients are defined via the arg-max you're solving for,
without an independent fixed-point argument. As written, Step 4 concedes this
is unresolved. This is not yet a proof strategy, it's a promising *shape* of
upper bound with an unresolved existence question at its core: does a single
configuration-*independent* weight vector `w_i` (depending only on rank, not
on the specific `p`) actually dominate `oddrank(B)` for every `A` and every
Xiang-Yu response `B`? That must be established (or refuted) directly — by
exhibiting the universal weights and proving the inequality for a genuinely
adversarial `A` (not the geometric one), not by reading them off the n=1
crossing point and assuming they generalize.
Change required: before any further construction work, the builder must
either (a) prove such a universal `w_i` exists and dominates for at least one
non-geometric test configuration, or (b) if the shared-budget coupling makes
this provably impossible, mark this dead-end explicitly per the outline's own
instruction, rather than silently patching around it.

## recursive-embedding-induction — CHANGES REQUESTED (approve to build with a gate)

Right general shape (recursion-first, treats c(n-1) as a black box) and a
useful independent check on the conjectured closed form — real diversity
value even though it shares Lemma A with geometric-dominance-construction
(my numerics above support Lemma A, lowering the "both die together" risk
CLAUDE.md warns about). The outline's own instruction to hand-check Lemma B
concretely at n=2 *before* investing in the general proof is exactly right —
keep that as a hard gate, not optional: if the self-duality fails even once
at n=2, this approach's Step 3 is a confirmed dead end and should be reported
as such (which sub-case broke), not patched. Do not let the builder skip
straight to the general algebra without doing this cheap check first.

## majorization-smoothing — RETHINK

The central mechanism (Lemma C: `V(p)` is concave, hence global optimality is
"nearly free" via KKT) is **numerically falsified**: `V` at the midpoint of
two feasible configurations is strictly below the average of `V` at the two
endpoints (0.52 vs 0.525, well-converged, n=2). A concave function cannot do
this. This kills the approach's actual selling point — without concavity,
Step 4 collapses into exactly the same laborious region-by-region case
enumeration that approaches 1 and 3 already have to do, except without their
concrete domination/recursion mechanisms to organize it. The outline itself
anticipated this failure mode and offered a fallback, but the fallback isn't
a distinct approach anymore — it's a strictly worse-organized version of the
existing casework approaches. This should go back to the outliner: either
(a) find a genuinely different global argument that doesn't require
concavity (e.g. a weaker structural property that still forces the
stationarity system to the geometric point, such as showing `V` restricted to
each fixed combinatorial "attack-type" region is linear and enumerating the
(bounded) vertex set directly — which is really the same casework as
approach 1, so this wouldn't add diversity), or (b) replace this line with a
framing genuinely far from all three surviving approaches (e.g. an
information-theoretic/entropy argument, or a direct probabilistic/averaging
argument over Xiang Yu's response space) rather than patching calculus onto a
result that isn't concave. Do not build this outline as written — the
concavity gap is not a fixable technical lemma, it appears to be false.

## Diversity assessment

After removing majorization-smoothing, the surviving field of three is not
fully independent: geometric-dominance-construction and
recursive-embedding-induction share Lemma A/3 (now numerically de-risked, so
this is an acceptable shared building block rather than the single-gap
trap — both approaches have *distinct* central novel mechanisms built on top
of it: explicit domination case-analysis vs. self-dual recursion).
equalization-potential-bound is the one framing genuinely far from the other
two (global LP bound, no case-split, no induction) and is worth keeping alive
despite its self-flagged circularity risk — a fast negative result there
(confirming the circularity is unfixable) is itself valuable this early.
Flag for the orchestrator: if by round 3 both geometric-dominance-construction
and recursive-embedding-induction are still stuck on the same tail-case-split
step, that will be the "shared framing" wall CLAUDE.md warns about, and a
genuinely different framing (not a calculus reskin of the casework, unlike
majorization-smoothing) should be introduced.

## Verdicts summary
- geometric-dominance-construction — APPROVE
- equalization-potential-bound — CHANGES REQUESTED
- recursive-embedding-induction — CHANGES REQUESTED
- majorization-smoothing — RETHINK (send back to outliner; concavity lemma
  numerically false)

build set: geometric-dominance-construction, recursive-embedding-induction, equalization-potential-bound
