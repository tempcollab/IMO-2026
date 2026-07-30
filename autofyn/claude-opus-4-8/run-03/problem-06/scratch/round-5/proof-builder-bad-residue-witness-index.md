# Build report — bad-residue-witness-index (round 5)

Status: **partial** (real new progress; crux gap remains).

## What was proved (gap-free)
- Steps 1–4 of the residue framing, each a short corollary of certified facts (S(m) depends only on
  m mod L_0; F1; GPC; bad-partner): residue-level badness, W(r)-large-link, W(r) points to bad terms,
  and the class-membership characterization (★): within a bad class r, m ∈ E_∞ ⟺ for every i ∈ W(r)
  some large prime q ∈ Q_i divides m.
- **NEW Reduction Lemma (promotable): (FIN-W) ⟹ theorem.** If for every term m only finitely many terms
  are small-disjoint from m, then the relevant large-prime set Q_rel is finite, E_∞ is tail-periodic
  from a_1 with period M = L_0·∏Q_rel, and PER+ENUM give a_{n+T}=a_n+M for all n. This is a DIRECT
  periodicity proof that does NOT route through (CSP); (CSP) is the special case M = L_0. It strictly
  weakens the standing crux: (CSP) ⟹ (FIN-W) ⟹ theorem, and (FIN-W) suffices.

## The remaining gap (honest)
(FIN-W) itself = the infinite-witness branch of Step 5. Pigeonhole (gap-free) reduces its failure to a
clean **star configuration**: a hub term m plus an infinite family T_p of bad off-lattice terms, all
divisible by one fixed large prime p, all in one residue class mod L_0 (so mutually small-connected via a
fixed nonempty s_1), each small-disjoint from m, all ≡ c mod pL_0. The final contradiction from this
configuration is NOT closed — this is the field's standing wall relocated. The reviewer's warning ("one
prime dividing infinitely many terms is not alone a contradiction") is exactly the unmet obligation; the
unused structure is off-lattice (GPC) + fixed residue class + hub small-disjointness. No dead route was
used (not covering/Helly, not global Σ1/p² capacity, not window-CRT — a_1 < L_0 verified).

## Recommendation to reviewer
- Certify the **Finite-witness periodicity** lemma (FIN-W ⟹ theorem). It genuinely sharpens the crux:
  the whole problem now reduces to "each term is small-disjoint from only finitely many terms," a
  strictly weaker and cleaner statement than (CSP), with a per-large-prime, off-lattice, single-class
  target for the next round.
- Route: CHANGES REQUESTED (partial, advanced) — the reduction is new and gap-free; only (FIN-W) is open.

## Suggestion for orchestrator / next round
The star configuration is now the common crux object across the field (it is the covering-small-part
"unbounded family" and the minimal-linking-prime "window descent" object in disguise). If both new
framings again bottom out on it, seed a framing that attacks the greedy DYNAMICS of the actual successor
a_{n+1} (window-minimality) — none of the live approaches exploits how a_{n+1} is *chosen*, only the
static set E_∞.
