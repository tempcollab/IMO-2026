## imo-2026-03 (UPPER WALL lens)

- **Distinct openings surfaced (for the outliner to pick among — genuinely different mechanisms, not
  variations of the refuted recursion):**
  1. **Two-move adaptive-choice induction (NEW, partially checked numerically, see below).** Instead
     of a fixed single move (MATCH(a1,a2) or DELETE(a1)) followed by IH, search over the *finite* set
     of all C(n+1,2)+(n+1) elementary single MATCH/DELETE moves for ONE whose result either (a) lands
     in the *already unconditionally closed* dominant regime a1'≥L'/2 of the (n)-piece problem
     (whole-tail-peel, no IH needed), or (b) admits Lemma-VS's own single-move certificate one level
     down. This is a genuine "look ahead 2 levels, pick the best of finitely many candidates" argument
     — different in kind from a fixed deterministic rule (which VS/round-9 rigorously killed) because
     it existentially quantifies over the move, not the profile. Numerically it succeeds on 100% of
     valley profiles for n=2,3,4 and ~98% for n=5, but genuinely FAILS (~1.9% of tested profiles, all
     near-uniform 6-piece profiles) at n=5 — so as a single clean two-level lemma it is not yet
     sufficient; the near-uniform tail needs a third ingredient (even-multiplicity/simultaneous pairing,
     consistent with memory rule 18). Still, "existential single-move-then-recurse, not deterministic
     single-move" is a genuinely different proof shape from anything built so far (round 9's refutation
     was of *deterministic recursions*, not of this existential-search form) and deserves being logged
     as a candidate the outliner has not yet tried.
  2. **Sum-of-squares / potential-function monovariant (aimo-0796 style), NOT the crude ρ<a2 bound
     already cited, but the actual mechanism behind it.** aimo-0796's crux tracks $S_k=\sum x_i^2$ under
     a repeated "balanced-partition ±1" update and shows $S$ is a strict monovariant forced by a
     partition-gap bound; the valley's covering claim is a *static* single-shot version of the same
     shape (find one subset with small signed-gap), not the *iterated* ±1 process — so the direct
     analogy only supplies the already-known crude bound. However, the PROOF TECHNIQUE inside it (an
     induction on $n$ appending the new element to whichever side is currently smaller, keeping the
     partial gap in $[0,a)$) is exactly the shape of a recursive one-sided KK/greedy pass, which is
     ALREADY refuted here (band-landing / flip-if-helps overshoot up to 11.4×). So this crux, while
     the closest literal analogue in the corpus, does **not** transfer new power — it reproduces a
     mechanism already ruled insufficient. Flagging this explicitly so the outliner does not waste a
     round rediscovering it.
  3. **Weight function $w(S)=\sum_x 2^{-r_S(x)}\le1$ (aimo-0298 "scales" lemma), applied to a
     DIFFERENT quantity than the one already refuted for the LOWER wall.** For the lower wall this
     split-and-average argument was rigorously refuted (fails ~28–45% of budget-enforced refinements,
     round 7). It has *not* been tried on the upper covering claim. Speculative opening: assign each
     piece $a_i$ a "scale count" = the number of distinct dyadic bands (à la Lemma ONE-REC's scale
     ladder) it participates in, and try to bound $\min\mathcal R(A)$ via a weighted count instead of a
     direct covering argument. This is untested and may hit the same wall (the technique is fundamentally
     an averaging/induction-on-size argument, similar in spirit to opening 1) — report as a candidate,
     not a validated lever.
  4. **Discrepancy-theory / dispersion angle — checked and largely a dead alley.** Classical covering
     radius / dispersion results (Beck–Fiala, three-distance theorem, Steinitz rearrangement lemma) are
     built for either (a) {0,1}-matrix row-sum discrepancy, or (b) fractional parts of an arithmetic
     progression mod 1, or (c) vector rearrangement in $\mathbb R^d$ keeping partial sums bounded — none
     matches the actual object here, which is a *finite reachable set under repeated absolute-difference
     with skip*, order-statistic-capped (only $a_1,a_2$ bounded, not a general discrepancy hypothesis).
     No corpus problem or classical theorem was found that directly gives "a reachable
     include/skip-difference set meets a target interval" as a black box; the corpus's closest matches
     (aimo-0796, aimo-0298) are both same-shape induction/potential arguments already covered above, not
     black-box coverage theorems. **Conclusion: there is no ready-made external theorem to import; the
     covering claim needs a bespoke inductive argument built from the problem's own recursion $u_n =
     u_{n-1}/(2+u_{n-1})$, not a classical discrepancy citation.**

- **Candidate technique(s):** strong induction on $n$ with an *existentially quantified* first move
  (search over the finite move set for one that reaches the unconditionally-closed dominant regime or a
  VS-certified one-level-down reduction), PLUS a separate closing argument for the residual near-uniform
  case (must exploit simultaneous multi-piece even-cancellation, not pairwise merges) — i.e. the correct
  proof is likely a case split: {∃ a good single move} ∪ {near-uniform ⇒ direct even-cancellation /
  explicit dyadic-adjacent construction}, mirroring the field's own diagnosis that a fixed rule always
  fails on the near-uniform tail (memory rules 12, 18).

- **Cheap-kill candidates:**
  - The "MATCH the two largest pieces $(a_1,a_2)$, then recurse" fixed rule: REFUTED numerically here
    (fails to escape the (n−1)-valley on 5–34% of random valley profiles for $n=3..5$, growing with
    $n$) — do not let the outliner assume this natural-looking fixed pairing is a valid single step.
  - The "any single move landing in the *pure unconditional* dominant regime $a_1'\ge L'/2$" test:
    REFUTED as a standalone sufficient mechanism (fails 39–92% of the time for $n=4,5,6$ — the
    near-uniform profile is exactly where it fails, e.g. $n=6$: $(0.259,0.215,0.177,0.151,0.124,
    0.054,0.020)$-type near-uniform profiles). Confirms memory rule 18's diagnosis extends to this
    specific mechanism too.
  - The "existential single move escaping to EITHER dominant-(n-1) OR VS-certified-(n-1)" test: much
    stronger (100% success $n\le4$, ~98% at $n=5$) but STILL genuinely fails on a small residual set of
    near-uniform 6-piece profiles (e.g. $(0.2896,0.1761,0.1676,0.1370,0.1275,0.1023)$-type, all pieces
    within a factor ~2.8 of each other) — so this two-level lookahead is necessary-but-not-sufficient;
    a third case (near-uniform simultaneous pairing) is still required on top of it.

- **Knowledge-base entries to use:** none of `knowledge_base.md`'s generic entries were found to add
  new leverage beyond what's already imported (R/M/P/PEEL/SPLIT/ONE/TB/DM/U0/RL/VS/ESF-1/ESF-2/BL); the
  problem's residual is bespoke enough that the KB's standard theorems (pigeonhole, extremal principle,
  double counting) only reproduce moves already tried (subset-sum pigeonhole is exactly the refuted
  naive-pigeonhole route per Lemma RL).

- **Analogous past problems (cruxes):**
  - `aimo-0796` (IMO, "the sequence contains an element $\ge n/2$"): crux = sum-of-squares potential
    under repeated min-partition-gap update, itself built on an induction lemma ("append new element to
    the smaller side, gap stays in $[0,a)$"). Genuinely analogous in SHAPE (both are about forcing a
    small signed-partition-gap of a bounded sequence), but its underlying construction is exactly the
    one-sided greedy-append mechanism already REFUTED here (overshoots up to 11.4×) — useful as
    confirmation of what NOT to re-derive, not as a new lever.
  - `aimo-0298` (IMO, "scales" / dyadic distance classes): crux = weight function $w(S)=\sum 2^{-r_S(x)}
    \le1$ via split-and-average induction on adjacent minimal-scale pairs. Already tried (and refuted,
    round 7) for the LOWER wall's exact analogue; untested for the upper covering claim but structurally
    the same averaging-induction shape, so low independent confidence it survives — flag as a low-
    priority speculative opening (item 3 above), not a strong recommendation.
  - No problem in the corpus was found that states or proves a genuine "reachable include/skip
    difference set covers a small target interval" as a standalone theorem; report this negative
    finding so the outliner does not spend a round searching further in this direction.

- **Prior progress:** Lemma BL (certified) locates the first crossing subset with residual
  $r\in[0,\beta_nL)$ in $n$ moves; the Covering claim ($R_{n+1}$ meets $[0,u_nL]$) is the exact open
  residual. ALL single-pass/deterministic recursions (greedy band-landing, flip-if-helps, drop-one) are
  rigorously refuted (overshoot up to $11.4\times$, round 9).

- **Dead ends (do not retry):**
  - Fixed deterministic single-pass recursion on the reachable set (any form) — refuted round 9,
    reconfirmed here via the MATCH$(a_1,a_2)$-then-recurse test (5–34% failure, growing with $n$).
  - Naive unrestricted $2^{n+1}$-subset pigeonhole (Lemma RL: not all $\{0,\pm1\}$ patterns are
    tree-realizable — invalid).
  - One-sided ESF-1 subtraction-from-$a_1$ family alone (round 8 explicit counterexample).
  - The pure "escape to unconditional dominant regime via one single move" test — refuted here
    (39–92% failure for $n=4,5,6$, worst on near-uniform profiles).

- **Small-case / intuition notes (all CONJECTURE / numerical, not proof):**
  - The two-level existential-move-then-VS-certificate test succeeds on ~98–100% of random valley
    profiles for $n\le5$ but has a genuine small residual concentrated on *near-uniform* profiles
    (all $n+1$ pieces within a narrow ratio band) — this residual class is exactly the one flagged
    repeatedly in memory (rules 12, 18) as needing simultaneous multi-piece even-cancellation rather
    than any pairwise move. A viable proof shape: **prove the two-level existential-move lemma handles
    the non-near-uniform bulk, and handle near-uniform profiles by a separate explicit even-cancellation
    construction** (e.g. if all pieces lie in a factor-2 band, pair up pieces by a sorted/interleaved
    matching to drive many differences to exactly 0 or near-0, exploiting the even-multiplicity
    corrector Lemma U0's mechanism at one remove). This is a genuinely new two-case skeleton candidate,
    distinct from a single global covering invariant — worth offering to the outliner as an alternative
    to "one clean covering/dispersion inequality," which may not exist as a single uniform statement.
  - No classical covering/dispersion theorem (three-distance, Beck–Fiala, Steinitz) was found to apply
    directly; confidence is now fairly high (though not proof) that GAP U-cover needs a bespoke
    two-case (generic vs. near-uniform) inductive argument built from this problem's own recursion,
    not an imported black-box inequality.
