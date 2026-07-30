## imo-2026-03

recursive-embedding-induction: revise
Target: For every n≥1, prove `oddrank(B) ≥ c(n) = 2^n/(2^{n+1}-1)` for every
Xiang-Yu response B against the geometric configuration A_n — i.e. fully close
Lemma PARITY-PAIR-ANCHOR/V'-GEN, completing the lower-bound half of the
minimax (combined with the certified tightness construction, Proposition 4,
this gives `min_B oddrank(B) = c(n)` for A = A_n exactly).
Technique: Strong induction on n via the self-similar structure of A_n
(certified Lemma 3), now split into two independently-closeable sub-cases per
this round's explorer's exhaustive small-case data.
Skeleton:
  1. (already certified) Lemma V'-GEN vertex reduction: the global minimizer
     of D(S∪T) has at most the free coordinates forced by the polytope's
     vertex structure — reduces to (i) pure-anchor configs, (ii) exactly-one
     free coordinate (Lemma FC, closed), (iii) two-or-more free coordinates
     tied across different split pieces ("cross-piece ties").
  2. NEW gap (a) target: prove every *reachable* anchor-only configuration
     (any budget b ≤ n, not just full budget) has D ≥ t_n. Reframe away from
     the abstract (c_1,...,c_n)-vector/M-parity formalism (which is genuinely
     false in the abstract, per the certified n=2 counterexample c=(0,4)) and
     onto the concrete **reachability** structure: because every anchor value
     t_i=2^{n-i} is a power of 2, the only anchor-exact split of an
     anchor-valued piece is an exact halving (sum of two distinct powers of 2
     is never itself a power of 2 — a one-line parity-of-binary-representation
     fact) — by Fact 1 of `lemmas/parity-pair-anchor.md`, P_1 is forced to
     split, and both P_1's residual tree and each T_i's own tree are
     independent **binary subdivision trees** of a power-of-two-valued piece.
     Prove by strong induction on n, peeling the root of P_1's binary tree
     (which splits into two level-(n-1) sub-pieces, one of which is —by Lemma
     3 — exactly a rescaled copy of A_{n-1}'s top piece, recursing), that
     every such tree-reachable leaf-multiset (at ANY budget ≤ n, not requiring
     full budget) satisfies D ≥ t_n. This sidesteps the M-parity case split
     entirely — parity was an artifact of the abstract-vector formalism, not
     of the actual game.
  3. NEW gap (b) target: prove genuine cross-piece-tied vertices (a free
     coordinate from a split of P_1 tied to a free coordinate from a split of
     the tail T_1, at a value strictly between two anchors) are never the
     global minimizer of D. Mechanism: at such a tie x=x' (x from piece π, x'
     from π'≠π), D is affine in x and in x' separately on the cell (certified
     Lemma D-INSERT gives the exact per-coordinate slope), so a two-variable
     local-extremum-of-an-affine-function argument shows the tied point
     cannot be a strict local min unless breaking the tie in *some* direction
     stays feasible and weakly decreases D — landing back in the
     already-closed single-free-coordinate case (Lemma FC) or the
     already-closed anchor-only case. Formalize this as a **domination
     lemma**: "if D is affine and non-constant in x near the tie (in either
     direction of freeing x from x'), moving x off the tie while holding x'
     fixed either strictly decreases D (contradiction to minimality unless we
     are already at the true min via the untied case) or is infeasible in
     both directions only at a boundary that is itself an anchor coincidence,
     not a genuine cross-tie" — the small-case exact-vertex data (n=2: best
     genuine cross-tie D=3 vs true min 1; n=3: best genuine cross-tie D=5/3 vs
     true min 1) shows the margin is large, so a clean one-directional
     perturbation suffices; no delicate boundary case is expected.
  4. Combine steps 2+3 with the already-closed pure-anchor, full-budget case
     (Lemma PARITY-PAIR-ANCHOR) and Lemma FC to conclude Lemma V'-GEN in full
     generality, hence Lemma PARITY-PAIR-GEN, hence the lower bound for A_n
     for every n and every Xiang-Yu response.
Key lemmas (claim + mechanism):
  - Reachability lemma (gap a): every anchor-only Xiang-Yu configuration at
    any budget ≤ n is realized by independent binary subdivision trees on
    P_1 and each T_i, because a power-of-two value has no anchor-exact split
    other than exact halving (no two distinct powers of 2 sum to a power of
    2 — direct binary-carry argument).
  - Tree-peeling induction (gap a): D ≥ t_n for every tree-reachable
    leaf-multiset, by peeling P_1's root split and applying Lemma 3's
    self-similarity to recurse into an (n-1)-instance — because the root
    split of P_1 (forced, Fact 1) produces one part that is an exact rescaled
    A_{n-1}-top-piece copy of the whole level-(n-1) subproblem.
  - Cross-tie domination lemma (gap b): a genuine cross-piece tie is never
    the global D-minimizer, because D is affine (not constant) in each of the
    two tied free coordinates independently (Lemma D-INSERT), so at least one
    perturbation direction that breaks the tie stays feasible and weakly
    decreases D, reducing to the already-solved single-free-coordinate case.
Open gaps: both (a) and (b) are precisely isolated but NOT yet proved — this
round's explorer only gives exhaustive small-n numeric evidence (n≤4 for (a),
n≤3 for (b)), not a general n proof; the builder must actually write the
induction/domination arguments.
Cases to cover: gap (a) covers every budget b≤n (not just full budget);
gap (b) covers every number of tied cross-piece coordinates (the report only
checked pairs of tied coordinates explicitly — if ≥3-way ties are reachable
at larger n they must also be ruled out, even though not observed in the
n≤3 exhaustive checks).
Watch out for: (1) the abstract M-parity statement is genuinely FALSE in the
abstract vector formalism (certified counterexample c=(0,4) at n=2) — do NOT
try to patch Lemma PARITY-PAIR-GENERAL directly; the fix must go through
reachability, exactly as this outline specifies. (2) "extension-monotonicity"
(D decreases monotonically as more marks are spent) is NOT needed and is not
even the cleanest true statement (the n=3 minimizer uses only 2 of 3 marks) —
do not accidentally assume it. (3) gap (b)'s domination argument must handle
the case where breaking the tie in one direction is infeasible (hits another
constraint) — check both directions, not just one.

universal-adversary-strategy: revise
Target: For every n≥1 and every Liu Bang configuration A (any m≤n+1 pieces,
not just the geometric A_n), prove Xiang Yu has a response B using ≤n marks
with `oddrank(B) ≤ c(n)·Σ(A)` — the general upper bound over arbitrary
configurations (completing Claim PTBI).
Technique: Strong induction on m (piece count) via a new fully-recursive
construction ("PDR" / Lemma BLOCK-RECURSE) that strictly generalizes the
already-certified Lemma PARTIAL-DOM/PARTIAL-DOM-RESIDUAL to full recursive
re-optimization of the leftover residual.
Skeleton:
  1. Formalize and PROVE Lemma BLOCK-RECURSE: given sorted A=(p_1≥...≥p_m),
     tail T=(p_2,...,p_m), for any 1≤j≤k=m-1 with p_1≥S_j (tail prefix sum)
     and r:=p_1-S_j, form the PARTIAL-DOM split of p_1 into (t_1,...,t_j,r),
     merge with the full tail T, THEN recursively re-optimize the leftover
     multiset {r}∪U (U = unmatched tail t_{j+1},...,t_k) as its own
     independent subproblem using the remaining m-1-j marks. Prove exactly:
     `oddrank(final) = S_j + oddrank(optimal response to {r}∪U)`, regardless
     of how deep the recursive refinement of {r}∪U goes.
  2. Prove budget conservation is automatic: each recursive call on a
     size-m' sublist assumes exactly m'-1 marks, telescoping to exactly m-1
     total at the top level — state this explicitly as a one-line induction
     on recursion depth, not asserted without proof.
  3. Prove by strong induction on m (the actual Claim PTBI): the minimum over
     the finite candidate set {BLOCK-RECURSE over all valid j, peel+halve/
     DOUBLE-INSERT, MULTI-HALVE, TAIL-SNIP (odd m), SANDWICH (odd m)} is
     ≤ c(m-1)·Σ(A) for every sorted A of size m. Base case m=1,2 direct;
     inductive step reduces via BLOCK-RECURSE's exact identity to bounding
     the recursive subcall by the induction hypothesis at size m-j (or
     m-j-1 if the residual itself gets absorbed), then closing the resulting
     finite algebraic optimization (max over A of min over the finitely many
     closed-form candidate expressions) — this is a finite, algebraically
     tractable optimization since each candidate is a fixed closed-form
     linear/piecewise expression in the sorted p_i's, not an open search.
  4. Verify exact equality at the geometric extremal configuration A_n for
     every n (already numerically confirmed by the explorer for n=1..7) as a
     sanity/tightness check that the induction's bound is not slack.
Key lemmas (claim + mechanism):
  - Lemma BLOCK-RECURSE: the duplicated matched block {t_1,t_1,...,t_j,t_j}
    (from PARTIAL-DOM's construction) dominates every element of the
    leftover {r}∪U, both before AND after any further recursive refinement
    of the leftover (splitting only shrinks values, never lets a leftover
    fragment exceed t_j), so the block always occupies exactly the top 2j
    ranks of the final merged list — an EVEN rank-shift, which by the
    certified D-INSERT/alternating-sum mechanism preserves parity exactly,
    making the leftover's contribution to oddrank exactly its own
    standalone oddrank, unconditionally, no matter how the recursive call
    further splits it.
  - Claim PTBI inductive step: the finite candidate menu's minimum tracks
    c(m-1) exactly at the geometric extremal point (not merely bounds it)
    because BLOCK-RECURSE with the "canonical" j exactly reproduces the
    tightness construction (Proposition 4) recursively — the induction's
    slack is zero at the hardest instance, which is why a finite menu
    (not exhaustive search) suffices.
Open gaps: Lemma BLOCK-RECURSE itself is NOT yet proved (only numerically
verified, m=3..9, thousands of trials, zero failures) — the "leftover always
dominated before and after further refinement" claim needs an actual
induction-on-refinement-depth proof, not just spot-checks. The full Claim
PTBI induction (step 3) is not yet carried out algebraically — this is the
main remaining work; the explorer's evidence is strong but this is still a
conjecture, not a theorem, until the max-over-A-of-min-over-menu inequality
is proved in closed form.
Cases to cover: m odd vs even (TAIL-SNIP/SANDWICH only apply for odd m);
the base cases m=1 (trivial) and m=2 (already fully closed via n=1's
complete proof) must anchor the induction; the case where NO valid j exists
for BLOCK-RECURSE (p_1 < p_2, i.e. j=0 only) must fall back correctly to
peel+halve/MULTI-HALVE/TAIL-SNIP/SANDWICH.
Watch out for: the recursive call's own optimal response to {r}∪U might
itself need BLOCK-RECURSE recursively — the induction is on m via strong
induction (assume the claim for all m'<m), not merely "one level deep";
don't let the builder secretly assume the leftover subproblem is solved by
a non-recursive one-shot lemma. Also: verify the "dominates before and after
refinement" claim carefully at the boundary where r ties exactly with some
element of U (a degenerate case the numeric trials may not have hit exactly).

geometric-dominance-construction: advance
Target: Same overall lower-bound target as recursive-embedding-induction —
`oddrank(B) ≥ c(n)` for every Xiang-Yu response B against A_n — reassigned
this round to independently attack gap (b) (cross-piece tied free
coordinates) using this approach's own certified toolkit (Lemma D-INSERT,
Lemma FC's "one free coordinate" mechanism), as a second, independent route
to the same statement recursive-embedding-induction is also attacking.
Technique: Direct application of the already-certified Lemma FC's affine-
per-coordinate machinery to the two-tied-coordinate case, rather than the
tree-peeling/induction machinery recursive-embedding-induction is using —
genuinely different proof mechanism (local perturbation/exchange on an
explicit affine cell) even though it targets the identical open sub-gap, so
this is valuable cross-verification (per the standing rule: when two
approaches converge on proving the same statement, the faster one's result
gets imported by the other, but running both increases confidence and
catches write-up errors).
Skeleton:
  1. Restate the cross-tie cell explicitly: two free coordinates x (from a
     split of P_1) and x' (from a split of T_1), tied x=x', with D affine in
     each on the cell (already established via D-INSERT, same mechanism
     that proved Lemma FC).
  2. Compute the two partial "slopes" ∂D/∂x and ∂D/∂x' explicitly in terms
     of the cell's fixed rank structure (a direct rank-counting computation
     using the certified D-INSERT formula).
  3. Case on the signs of the two slopes: if breaking the tie by increasing
     x (decreasing x') or vice versa weakly decreases D while staying
     feasible, do so — reducing to Lemma FC's single-free-coordinate case.
     Handle the boundary case where one direction is infeasible (hits
     another anchor/tie) explicitly, not by assertion.
  4. Conclude cross-tie vertices are always dominated by (i.e. give D no
     lower than) a single-free-coordinate or anchor-only configuration,
     closing gap (b) as a corollary of Lemma FC.
Key lemmas (claim + mechanism):
  - Cross-tie domination via affine perturbation: identical target statement
    to recursive-embedding-induction's gap (b) lemma above, proved via
    explicit slope computation on the D-INSERT cell rather than an abstract
    "some direction is feasible" argument — a concretely computable check.
Open gaps: not yet proved — this round's target is to actually carry out the
slope computation and case analysis; the explorer's n=2,3 exact-vertex data
(best genuine cross-tie D=3 and 5/3 respectively, vs true min 1) is strong
supporting evidence but not a proof for general n.
Cases to cover: n=2 and n=3 exact cases already numerically verified by the
explorer — the builder should reproduce these as concrete sanity checks
before attempting the general-n argument.
Watch out for: if this approach's route and recursive-embedding-induction's
route reach different conclusions on gap (b), that is a red flag requiring
reconciliation before either is trusted — do not let both stand uncritically
if they disagree.

minimax-mixed-duality: retire (no build this round)
Rationale: the round-8 new-framing explorer identified a candidate dynamic/
sequential geometric-discount potential (Opening A, adapted from crux
aimo-0198) but explicitly flagged a MANDATORY cheap numeric gate (test a
single tunable λ against both hardest known n=4 witnesses) that was NOT run
this round — the explorer's report says "I did not attempt this proof" and
frames the gate as something "a builder must check before committing," not
something already passed. Per the dispatch instruction, since the gate has
not been demonstrated to pass, do not open a new approach on this framing
this round and do not force a low-quality diversity slot. Additional
structural reason to expect collapse: c(n) = 2^n/(2^{n+1}-1) is NOT a pure
geometric sequence in n (ratios 2/3, 4/7, 8/15, 16/31 do not share a common
ratio, only approach 1/2 in the limit), so a single fixed contraction rate ρ
in a telescoped bound Φ_n ≤ ρ^n Φ_0 cannot exactly reproduce c(n) for every n
without ρ itself depending on n — which is exactly the n-dependent recursive
relation c(n)=2λ_n c(n-1) already on file (Lemma G1, round 2), suggesting
Opening A would at best re-derive existing machinery in different language,
the same fate as this approach's prior two rounds. minimax-mixed-duality
itself (the LP-mixed-duality framing) is not rebuilt this round — 2
consecutive RETHINKs with zero independent leverage, now a 3rd round with no
new mechanism proposed to revive it. Recommend the outline-reviewer formally
retire this slug (or fold its one reusable output, Lemma SANDWICH, as
already-imported into universal-adversary-strategy's menu, which it already
is).

Notes for outline-reviewer: this round's build set should prioritize
recursive-embedding-induction and universal-adversary-strategy — both are
the closest to full closure on file (per current.md and this round's
explorer evidence: gap (a)/(b) exhaustively clean for n≤4/n≤3 respectively;
BLOCK-RECURSE clean for m=3..9 with zero numeric failures). If both close
this round or next, Status could move toward `solved` — but neither Lemma
BLOCK-RECURSE, the tree-peeling induction, nor the cross-tie domination
lemma is actually proved yet; all remain the builders' real work, not
foregone conclusions. geometric-dominance-construction's parallel attempt on
gap (b) is optional cross-verification, not required for closure if
recursive-embedding-induction's own route succeeds first.
