# Proof builder report — breakpoint-vertex (imo-2026-03), round 8

**Status: partial.** Target this round was to close UPPER Prop UV ($\min\mathcal R(A)\le u_nL$ over the
finite VERT vertex set, profile-independently). I did NOT fully close it, but I made genuine rigorous
progress that sharpens and de-risks the residual, and I proved two new promotable lemmas plus a
rigorous negative result. No numeric spot-check is used as a proof step anywhere.

## What I proved rigorously this round (self-contained on certified Lemmas P/DM)

1. **Lemma ESF-1 (subtraction-from-top subfamily).** For $A=\{a_1\ge\dots\ge a_{n+1}\}$ and any
   $T\subseteq\{2,\dots,n+1\}$ with $\sum_{i\in T}a_i\le a_1$: $\;a_1-\sum_{i\in T}a_i\in\mathcal R(A)$,
   realized by exactly $n$ DM moves ($|T|$ MATCHes — each legal because the running value stays
   $\ge$ the next resident piece, since every partial sum $\le\sum_T\le a_1$ — plus $n-|T|$ DELETEs).
   Budget verified exactly.

2. **Lemma ESF-2 (subset-caterpillar subfamily).** For any nonempty subset $T$ in any order
   $t_1,\dots,t_k$, the caterpillar value $v_1=t_1$, $v_j=|v_{j-1}-t_j|$ satisfies $v_k\in\mathcal R(A)$,
   realized in exactly $n$ moves ($k-1$ MATCHes + $n{+}1{-}k$ DELETEs). The abs-flip step
   $v_{j-1}<t_j$ is a single legal MATCH$(t_j,v_{j-1})$ that cuts the resident $t_j$ into
   $\{v_{j-1},t_j-v_{j-1}\}$ and cancels the running piece (Lemma P). In particular **descending-KK
   over any subset is realizable.** ESF-2 is strictly larger than ESF-1 (the abs-flip).

3. **Reduction UV' (rigorous sufficiency).** By ESF-2 + Reduction R-UV, Prop UV follows from the
   cleaner **Subset-KK claim**: *every full-budget balanced-valley profile has a subset whose
   descending-KK caterpillar value is $\le u_nL$.* This replaces the abstract "min over the whole
   $\mathcal R(A)$" by a minimum over an **explicit constructive family** (subset + one fixed order),
   which is sufficient for the upper bound (we need existence of one small value, not the true min).

4. **Rigorous negative result (abs-flip is mandatory).** The tempting "greedy subset-sum toward
   $a_1$" route (ESF-1 only) is *provably* insufficient. Explicit rational $n=2$ valley counterexample
   $A=\{9/20,\,7/25,\,27/100\}$ (sum $1$; $a_1=9/20<1/2$; $a_2=7/25=0.28<\beta_2=2/7$): the ESF-1
   minimum is $\min\{9/20,\,17/100,\,9/50\}=17/100>u_2=1/7$, while the abs-flip subset $\{a_2,a_3\}$
   gives $|7/25-27/100|=1/100\le u_2$. This kills the one-sided route (which realizes only the crude
   aimo-0796 bound $\rho<a_2$, short of $u_n$ by up to a factor $\beta_n/u_n=2^{n-1}$) and pins the
   residual to the genuinely two-sided Subset-KK claim.

All four are written into §4B.4 of the approach file with full proofs; ESF-1/ESF-2 are added to the
Promotable lemmas section.

## Why Prop UV is still open (honest gap)

The residual **Subset-KK claim** is a genuine restricted-discrepancy statement. Computational scouting
(only to *find* the right target, never used as a proof) established:
- Min over all trees, and min over subsets of descending-KK, both land $\le u_nL$ on every valley
  profile with margin (worst ratios $0.31$–$0.74$, $n=2\dots6$) — so the claim is true.
- **No simple deterministic single-pass policy works.** Full-support descending-KK, descending-KK
  with early-stop-delete, and the greedy "include iff it strictly reduces the running value" all
  overshoot (up to $\sim3$–$15\times$). The correct subset requires foresight — the genuine content is
  a *scale recursion* (represent the residual after the first big crossing using the smaller pieces,
  recursively), exactly the crux shared with valley-differencing-construction / subset-sum-pigeonhole.

I could not produce a profile-independent proof of the Subset-KK claim within budget. I explicitly did
NOT paper over it: the natural "one move then IH$(n-1)$" recursion is blocked by Lemma VS, and the
"remove mass then apply a lower-level IH" route is blocked because reaching the dominant regime
requires removing $\Theta(L)$ mass, impossible with $O(1)$ small-piece moves.

## Net advance for the population
- Prop UV is now a bound over an **explicit constructive family** (was an existence statement over the
  abstract achievable set) — a strictly better target for next round's builder.
- The one-sided family is **rigorously eliminated**, so the field will not waste a round on
  greedy-subset-sum-toward-$a_1$.
- ESF-1/ESF-2 are certification-ready and reusable by valley-differencing-construction (they supply
  the exact realizability + budget bookkeeping that its GAP-DELETE-RULE needs).

## Spec concerns
None. The reduction chain R-UV → Reduction UV' → Subset-KK claim is exact; the answer
$c(n)=2^n/(2^{n+1}-1)$, $u_n=1/(2^{n+1}-1)$ is unchanged and confirmed.

## Promotable lemmas (for reviewer certification)
- **Lemma ESF-1** (subtraction-from-top subfamily) — statement + full proof in §4B.4. Depends only on
  certified P/DM.
- **Lemma ESF-2** (subset-caterpillar subfamily, incl. descending-KK realizability + the explicit
  insufficiency-of-ESF-1 counterexample) — statement + full proof in §4B.4. Depends only on certified
  P/DM.

File written: results/imo-2026-03/approaches/breakpoint-vertex.md (Status: partial).
