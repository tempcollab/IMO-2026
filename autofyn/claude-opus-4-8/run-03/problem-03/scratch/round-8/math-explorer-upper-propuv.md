## imo-2026-03 — lens: UPPER-BOUND wall / Prop UV

- **Distinct openings surfaced:**
  1. *Restricted-pigeonhole-with-repair* (subset-sum-pigeonhole route): don't pigeonhole the full
     $2^{n+1}$ signed subset sums; instead spend one DELETE to shrink to a family where the
     remaining $2^n$ (or fewer) tree-realizable sums *are* dense enough, i.e. characterize exactly
     which subset-size / drop choice restores the pigeonhole density lost to GAP-ACH.
  2. *Direct explicit construction, valley-specific* (bypasses pigeonhole/counting entirely):
     use the two valley hypotheses $a_1<L/2$, $a_2<\beta_nL$ constructively — e.g. drop (DELETE)
     some suffix of small pieces, then run a Karmarkar–Karp-style ("largest-two-differencing")
     chain on the surviving prefix, using the size constraints to bound the chain's overshoot by
     induction on the number of surviving pieces. This is the differencing-tree analogue of
     Lemma RL/VS's own machinery, made constructive rather than existential/pigeonhole.
  3. *VERT-vertex finite-search route* (breakpoint-vertex's own tool): since Theorem VERT already
     shows the optimal Xiang response over *any* input $A$ collapses to $\le n{+}1$ distinct
     values (tie-pattern search), attack Prop UV as a finite combinatorial optimization over
     tie-patterns directly, rather than re-deriving it via DM/RL language.

- **Candidate technique(s):** restricted/tree-realizable signed-subset-sum discrepancy bound;
  Karmarkar–Karp-type greedy differencing with a DELETE-repair step; LP-vertex tie-pattern
  enumeration (Theorem VERT) as a finiteness reduction, not a bypass.

- **Cheap-kill candidates:** none found that avoid the combinatorics — this is a genuine
  discrepancy-bound gap, not a bookkeeping error. One useful *cheap sanity filter*: the KK chain
  over the FULL support (no DELETE) is already known (R7, machine-checked) to fail on 214/516
  valley profiles at up to $7.5\times$ overshoot — so any candidate construction MUST use DELETE
  non-trivially; a "no-DELETE" construction can be discarded immediately without re-testing it.

- **Knowledge-base / lemma entries to use:** certified Lemmas P, DM (elementary-reductions), RL
  (leftover-realizability), VS (valley-sharpness), Theorem VERT, U0 (even-multiplicity-corrector),
  whole-tail-peel. `knowledge_base.md` general pigeonhole/discrepancy entries (if present) should
  be checked by the outliner for a named subset-sum-discrepancy bound (I did not find a
  problem-specific KB entry beyond the generic pigeonhole idea already exploited).

- **Analogous past problems (cruxes):**
  - **aimo-0796** (IMO-style Iran problem, `combinatorics`/`invariants-and-monovariants` +
    `induction-and-construction`): proves by induction "if all $|x_i|<a$, one can 2-partition into
    $I,J$ with $|\sum_I x_i - \sum_J x_j| < a$" by processing elements ONE AT A TIME (any order)
    and always appending the new element to whichever side keeps the running gap smaller. This is
    the closest genuine analogue: a *greedy sequential-append* discrepancy bound with the same
    shape as what's needed for Prop UV (bound a signed-sum discrepancy using per-element bounds).
    **Caveat:** it bounds gap by the max $|x_i|$ appended at each step (an $O(a)$ bound, not
    matching our $O(u_nL)$ exact ratio target), and it does not have RL's "differences only, no
    sums" tree-realizability restriction — the analogy is in proof *technique* (induction +
    always-improve-the-worse-side), not a directly transplantable result. Adapt, don't cite.
  - Searched explicitly for "Karmarkar-Karp" / "differencing algorithm" / "merge two largest" —
    **no hits** in the corpus. No corpus problem directly encodes the DM/RL tree-realizable
    subset-sum structure.
  - No other subtopic (`pigeonhole`, `processes-and-algorithms`, `extremal-principle`) surfaced a
    closer match after filtering ~40 candidates with "discrepancy/signed-sum/balance" keywords;
    none matched the *tree-realizable* (differences-only) restriction that is the crux difficulty
    here. **Verdict: no strong corpus match — this restricted-discrepancy structure appears
    genuinely bespoke to this problem.**

- **Prior progress:** Reduction R-UV (certified) makes Prop UV an exact iff for the upper bound in
  the valley. Lemma RL certified (achievable leftovers = tree-realizable signed subset sums,
  strictly fewer than all $\{0,\pm1\}$ patterns). Lemma VS certified (no single DM move admits an
  IH(n−1) certificate in the valley — rigorous adaptivity, ≥2 coordinated cuts forced). Theorem
  VERT certified profile-independently (not just for $C_n$: the proof in breakpoint-vertex.md §3
  is stated for *any* input multiset $A$, so it already applies to Xiang's optimal response too).

- **Dead ends (do not retry):**
  - Naive $2^{n+1}$-subset pigeonhole over ALL $\{0,\pm1\}$ sign patterns — invalid, RL shows only
    tree-realizable patterns (a strict subset) are achievable (round 7, certified).
  - No-DELETE / full-support differencing tree (using all $n+1$ pieces) as THE construction —
    machine-refuted, overshoots on 214/516 valley profiles up to $7.5\times$ (round 7).
  - Treating VERT-vertex-search as a bypass of GAP-ACH: it is **not independent** of route (i).
    VERT's tie-pattern vertices, once cancelling pairs are peeled (Lemma P), are exactly DM/RL's
    differencing-tree leftovers on a distinct-value core — i.e. routes (i) subset-sum-pigeonhole
    and (ii) VERT-vertex-enumeration are **the same underlying combinatorial object described in
    two languages**, not two independent attacks. Do not expect VERT alone to close Prop UV without
    also confronting the achievability restriction.

- **Small-case / intuition notes (conjecture, numerically checked this round):**
  - Ran a from-scratch brute force (independent of R7's machine check): for $n=3,4$, over random
    valley profiles ($a_1<L/2$, $a_2<\beta_nL$), computed $\min\mathcal R(A)$ by exhaustively
    searching **all** subsets $T$ and **all** binary bipartition trees on $T$ (a superset-check of
    tree-realizable differencing, not just the KK chain) — found worst-case ratio
    $\min\mathcal R(A)/u_nL \approx 0.66$ ($n=3$, 300 trials) and $\approx 0.43$ ($n=4$, 60 trials),
    i.e. Prop UV held with comfortable margin in every trial, consistent with R7's 387-profile
    check (worst ratio 0.56). This is strong numeric confirmation Prop UV is TRUE and not
    razor-thin (the margin does not seem to shrink to 0 as profiles approach the valley boundary,
    in the sampled trials) — but still only evidence, not a profile-independent proof.
  - **(iii) The single make-or-break sub-step (shared by routes i and ii):** construct/characterize,
    for every valley profile, an explicit choice of (a) which subset $T$ to DELETE down to, and
    (b) a nonnegative-differencing-tree order on $T$, such that the resulting leftover is
    $\le u_nL$ — profile-independently, in closed form (not case-by-case numerics). The extremal
    dyadic profile's descending-cascade telescoping ($2^n-2^{n-1}-\cdots-1=1$) is the model to
    generalize; the open question is exactly how many/which small pieces must be DELETEd as a
    function of how far $A$ is from dyadic (using $a_1<L/2$, $a_2<\beta_nL$ to control it), and
    proving the resulting chain's overshoot is bounded by $u_nL$ in general. No shortcut around
    this construction was found; both routes converge on it.
