# Build report — two-box-balancing (imo-2026-03, round 2)

**Status: partial.** Answer confirmed `c(n)=2^n/(2^{n+1}-1)`, `V=u_n=1/(2^{n+1}-1)`,
`2c(n)-1=u_n` (verified). File: `results/imo-2026-03/approaches/two-box-balancing.md`.

## What I CLOSED (fully rigorous)
- **Reformulation** `D=|O|-|E|` (odd/even-rank boxes) and reduction `c(n)=(1+V)/2`; invariants
  stated on lengths/scales (heeded the reviewer's rank-vs-scale warning).
- **Lemma U0 (NEW, promotable):** if Liu commits `m ≤ n` pieces, Xiang forces `D=0` with `≤ m`
  cuts, via a top-copy chain making every final length even-multiplicity (Corollary of Lemma M).
  This is a genuinely new, clean result: it discharges the ENTIRE upper bound except the single
  boundary case `m=n+1`. Computationally verified (20000 multisets: D=0, ≤m cuts).
- **Upper, `m=n+1` dominant with `a_1 ≤ c(n)`:** replicate-all + Lemma P ⇒ `D=2a_1-1 ≤ u_n`.
- **Lower Case A** (top scale uncut): `D ≥ 2^{n-1}u_n ≥ u_n` (box statement of "top scale alone
  in O, unpairable without a cut").
- **Lower Case B reduced to a single Sub-lemma SL** (top scale cut ⇒ residual dominates
  order-(n-1) dyadic); SL Case A, SL perfect-bisection recursion (uses IH `L(n-1)≥1` + Lemma P),
  and SL base n=1 all proven.
- **Base cases n=0,1 both directions** complete through this framing.
- **Dyadic tightness:** bisect-the-top cancelling chain ⇒ `D=u_n` on `𝒟_n`.

## What REMAINS open (honest gaps — the two shared walls, unbroken)
- **GAP U** — adaptive subset-match strategy for `m=n+1` when non-dominant OR dominant with
  `a_1>c(n)`. I found a genuine cut-count obstruction (GAP U1): in the dominant `a_1>c(n)` branch
  the replicate-all already spends all n cuts and leaves `D=2a_1-1>u_n`; there is no spare cut to
  bisect the leftover, so this branch is NOT closed by the naive move and folds into GAP U.
- **GAP L** — Sub-lemma SL for imperfect top cuts `p_1≠p_2` (the shadow-coupling / net-toggle
  domination inequality). SL Case A degenerates as `p_1↓2^{n-1}` (near-perfect bisection).

## Spec / correctness concerns for the reviewer
- Lemma U0's cut count: reaches `|R|≤1` in `≤ m-1` reduction steps, `+1` bisection `= ≤ m` cuts;
  correct only for `m ≤ n`. The `m=n+1` boundary genuinely fails by one cut — this is exactly
  why `m=n+1` is the hard case, and it is stated as such (not papered over).
- I corrected an initial wrong claim (bisect-then-U0 in the `a_1>c(n)` dominant branch) inline as
  GAP U1 rather than deleting it, to flag the trap for future builders.
- SL and the lower bound depend on `L(n-1)≥1` (IH); the induction is valid only once GAP L closes
  the imperfect-cut branch — do NOT read §2 as a completed induction.

## Diversity note
As the reviewer flagged, this approach's lower-bound Case B ("cutting a scale costs that scale")
shares intuition with induction-peel's shadow map — they will likely stall on the same SL/GAP L
wall. The distinctive, non-shared contribution here is **Lemma U0** on the UPPER side, which the
other approaches don't have. Recommend certifying Lemma U0 into `lemmas/` so all approaches can
import it (collapses the upper bound to `m=n+1` uniformly).
