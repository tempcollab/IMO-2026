# Build report — induction-peel (imo-2026-03), round 1

**Status: partial.** Answer confirmed $c(n)=2^n/(2^{n+1}-1)$ (verified exact for $n\le3$ by
minimax numerics; recursion, measure identity, cancelling-pair identity all checked in code).

## What is now fully rigorous (promotable)
- **Lemma R** (greedy claiming, Liu gets odd ranks, Liu $=\tfrac{1+D}{2}$) — full token-swap
  exchange proof. Shared, ready to certify.
- **Lemma M** (parity–measure identity $D=|\{t:N(t)\text{ odd}\}|$) — full proof; the clean handle
  used by all approaches. Ready to certify.
- **Lemma P** (cancelling pair: $D(\mathcal S\cup\{v,v\})=D(\mathcal S)$) — full proof; this is the
  induction-peel engine (one cut deletes a cancelling pair, drops piece count by 1 and length by
  $2v$, leaves eventual $D$ unchanged). Ready to certify.
- Recursion $u_n=u_{n-1}/(2+u_{n-1})$, $c(n)=(1+u_n)/2$; base cases $n=0,1$ both directions.
- **Lower bound Case (a):** if Xiang never cuts the current largest dyadic piece, $D\ge u_nL$
  (top interval $[L',P)$ has $N\equiv1$). Uses the constant-gap superincreasing identity
  $a_j-R_j=u_n$ for all $j$.
- **Upper bound peel arithmetic (6.1):** the single-cancelling-pair peel closes iff
  $\max(a_1,2a_2)\ge Lc(n)$; proven, and **tight/complete on the dyadic extremal input** (so the
  answer is confirmed exact there).

## Two open gaps (honest)
- **GAP L** (lower bound, Case (b)): when Xiang *does* cut the top piece, the global descending
  sort couples top-fragments and tail; symmetric-difference bound is too lossy
  ($D\ge u_nL-|\{N_P\text{ odd}\}|$, and $|\{N_P\}|$ can be $\gg u_nL$). Needs a migration/protected-
  interval argument that survives the top cut. Not closed.
- **GAP U** (upper bound, the load-bearing A2): the single-pair peel does NOT close when
  $\max(a_1,2a_2)<Lc(n)$ — real counterexample $(0.5,0.28,0.22)$, $n=2$ ($\max=0.56<0.571$), where
  Xiang still wins ($D\approx0.003$) but via a two-cut manoeuvre that does not factor as "delete one
  big pair then recurse." The induction as set up (peel by top two ranks) is genuinely incomplete;
  a correct version must track the whole descending profile, not just $a_1,a_2$.

## Spec concerns
- None on the problem statement. The reduction to the $D$-minimax is clean and the answer is
  robustly confirmed. The difficulty is entirely in the two coupling gaps, which are the *same wall*
  the outline-reviewer predicted the whole field shares (adaptive Xiang bound + top-cut lower bound).

## Recommendation to orchestrator / next outliner
- Certify Lemmas R, M, P into `results/imo-2026-03/lemmas/` — they are approach-agnostic and both
  rival approaches need them.
- The induction-peel framing bottoms out on GAP U because peeling "top two ranks" loses the profile.
  If parity-measure-potential also stalls on its B3, next round genuinely needs a *profile-global*
  Xiang strategy (e.g. process thresholds top-down making $N(t)$ even except a length-$u_n$ tail),
  not another top-rank peel — consistent with the reviewer's "seed a different framing" note.

Proof written to /home/agentuser/repo/results/imo-2026-03/approaches/induction-peel.md
