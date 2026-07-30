## imo-2026-03 — lens: GAP U's balanced Case (iii), strengthened-potential / balanced-recursion route

### Setup recap (verified by re-reading, not re-derived)
RT(k): from ≤k+1 pieces of total Σ, Xiang has ≤k "removal ops" (bisect: −ℓ_i; generalized-pin ℓ_j
into ℓ_i: −2ℓ_j; free delete of an exact-equal pair: 0 cost) reaching effective total ≤ u_kΣ.
Cases (i) dominant ℓ_1≥c(k)Σ and (ii) balanced-top 2ℓ_2≥c(k)Σ are PROVEN for all k (one op + IH).
Only Case (iii), max(ℓ_1,2ℓ_2)<c(k)Σ, is open. Builder proved black-box greedy/single-move+IH
is provably insufficient (telescopes to 2/((k+1)(k+2)) > u_k for k≥3).

I wrote a brute-force solver (`/tmp/round-4/rt_search.py`) computing the TRUE optimal residual
total f(k,ℓ) = min over all legal op-sequences (recursive exhaustive search, memoized), for a
given numeric partition ℓ. This is a genuine ground-truth oracle (not a heuristic), usable for
k≤4 (branching is manageable). All findings below are numerical/empirical unless stated as a
re-derivation of an already-certified fact.

### Finding 1 — the optimal strategy in Case (iii) is NOT bisect-then-recurse; it's a chained-pin (Euclidean-like) sequence
Tracing the solver's actual chosen op sequence at a point just inside Case (iii) near the dyadic
boundary (k=3, pieces ≈ (0.5323, 0.2663, 0.1330, 0.0683), which sits at max(ℓ_1,2ℓ_2)=1.0647<c(3)):
the optimal sequence is **pin(ℓ_1,ℓ_3) → pin(result,ℓ_4) → pin(result,ℓ_2)** — three chained pins,
never a bisect. This resembles a Euclidean-algorithm-style repeated subtraction on the piece
values, i.e. Case (iii)'s real mechanism looks like an **exchange/subtraction algorithm** (pin
the top piece down against successively smaller pieces) rather than "peel off one dominant piece
and recurse." This is a genuinely different sub-opening than the ψ(k,β) potential the builder
proposed: instead of finding a closed-form potential, try to prove directly that a **specific
canonical chained-pin schedule** (e.g., repeatedly pin the current largest against the current
smallest, a "greedy Euclidean" variant — NOT the refuted max-total greedy) achieves total ≤u_kΣ
in Case (iii). Note: builder's refuted "remove-max-total greedy" always removes the largest
single deletable chunk; the chain here is different — it pins ℓ_1 against a SMALL piece (ℓ_3,
not ℓ_2), which only removes 2ℓ_3 (small) but transforms ℓ_1 into a much smaller residual
(ℓ_1−ℓ_3), effectively doing "long division" on ℓ_1. This has not been tried; worth scouting.

### Finding 2 — Case (iii) has real slack; the bound is not tight in the interior
Random sampling (several thousand trials/​k) of the max of f over the *interior* of Case (iii)
(strict inequality, sampled away from the boundary):
```
k=2: max f/u_k ≈ 0.88   (interior sup, sampled)
k=3: max f/u_k ≈ 0.76
k=4: max f/u_k ≈ 0.72
```
So the true supremum of f restricted to Case (iii) is bounded well away from u_k in these
samples — consistent with the claim (already in the approach file) that Case (iii) is "strictly
sub-extremal," and suggesting there is room for a **non-tight, cruder bound** (e.g. any bound of
the form f ≤ (1−δ_k)u_k for a fixed δ_k>0, or even a bound depending polynomially rather than
matching u_k exactly) to close the case — you do NOT need a sharp closed-form ψ(k,β) that meets
u_k at the boundary; a strategy that's merely "good enough" (with slack ≥ 12–28%) suffices. This
lowers the bar for the outliner: don't over-invest in finding the exact extremal ψ; a looser
sufficient bound is fine.

### Finding 3 — approaching the boundary along a RADIAL path, f is continuous and matches u_k in the limit, but is NOT globally monotone
Perturbing the dyadic partition inward along the ray "steal ε from top piece ℓ_1, feed it to the
bottom piece ℓ_{k+1}" (keeping ℓ_2,…,ℓ_{k-1} fixed at their dyadic values minus a small correction
to stay strictly in Case (iii)) gives f/u_k → 1 continuously as ε→0 (k=3: ratios 0.97, 0.85,
0.70, 0.40, 0.25 for ε=0.001…0.05) — consistent with f being continuous across the Case(i)/(iii)
boundary. However, testing OTHER directions/starting points (8 random Case-(iii) instances,
pushing ℓ_1 toward c(k) along various rays) shows **f is NOT monotone in general** — it goes up
and down non-trivially along generic rays (e.g. trial 5: 0.0217→0.0033→0.0217→0.0171→0.0110→
0.0036 as t increases from 0 to 0.95). So a naive "compactness + monotonicity ⇒ sup is a boundary
limit" argument does **not** trivially work as a global mechanism — the landscape of f is jagged
(reflecting the discrete choice of which op is optimal at each cell of a piecewise-linear
partition of parameter space). This DEAD-ENDS the simplest version of the "extremal point via
calculus of variations" idea; a working compactness argument (if it exists) would need to argue
about the specific finitely-many "active" linear pieces of f near a hypothetical interior
maximizer, not a naive directional-monotonicity claim. Flag this concretely so the outliner
doesn't waste a round rediscovering non-monotonicity.

### Finding 4 — the amortized-halving monovariant W=2^{-#cuts remaining}
This doesn't have an obvious direct role: the actual recursion factor per level is u_k/u_{k-1} =
1/(2+u_{k-1}) ≈ 1/2 but not exactly 1/2 (only asymptotically as k→∞, u_{k-1}→0). So a pure
"total halves every cut" monovariant is only an approximation; using it directly would give a
bound like Σ/2^k which is close to but not exactly u_k = Σ/(2^{k+1}-1) (ratio →1/2 not 1 as
k→∞, i.e. Σ/2^k is roughly 2u_k — too weak by a constant factor). So W=2^{-#cuts} alone is
**not fine-grained enough**; it under- or over-shoots by a factor of ~2. It could still serve as
a coarse a priori bound to combine with case-(iii)'s slack (Finding 2) — e.g. show Case (iii)'s
extra slack (~72-88% of u_k) absorbs the ~2x looseness of the naive halving bound — but this is
speculative and unverified; flag as a possible combination, not a working mechanism.

### Finding 5 — RT (residual-total) vs targeting D directly
Confirmed (matches builder's claim): searching directly over op-sequences to minimize the final
discrepancy D (not just total) still bottoms out at essentially the same numbers as minimizing
total (I re-ran a restricted check using the `eval_f` total-minimizer's achieved multisets and
computed D on them — since after full removal chains typically only 0-1 pieces survive in the
effective multiset, D on that residual multiset ≈ its total in these tested instances). RT does
not look lossy in the tested range; no evidence that a direct-D potential would be meaningfully
easier than RT's total-based one. This corroborates the builder's own note — do not re-litigate
"RT is the obstruction," it isn't.

### Candidate technique(s)
- A **strengthened two-clause / disjunctive invariant with a reserve buffer** (see crux
  `aimo-0340` below) — exactly the shape of argument this case needs: instead of one fragile
  bound "residual ≤ u_kΣ," maintain a disjunction of two invariants across the induction so that
  whichever clause is about to fail is covered by the other, with a "reserve" (extra ops or extra
  slack pieces) that survives the exact transition where the plain bound would break.
- A **chained-pin / Euclidean-subtraction schedule** (Finding 1) as the actual winning strategy
  in Case (iii), rather than a single dominant-piece move.
- Direct proof of a **weaker sufficient bound** (Finding 2's slack) rather than chasing a tight
  ψ(k,β) matching u_k exactly at the Case-(iii)/boundary interface.

### Cheap-kill candidates
- None obvious that dispatch a whole case cheaply; but Finding 2 (interior slack ~25-30% at
  small k) suggests trying a crude union bound first (e.g., "two chained pins always beat u_k by
  a constant factor when ℓ_1<c(k)") before building a full closed-form potential — cheaper to
  disprove/confirm than deriving ψ(k,β).

### Knowledge-base entries to use
Need to check `knowledge_base.md` directly for named entries on invariants/monovariants and
games — I did not find a dedicated "amortized potential" or "exchange argument" named entry
beyond what's already cited in the certified lemma files (Cut-Flip, Lemma G); the relevant
general technique class is "monovariant / potential function with a reserve" and "extremal
principle" as generically named in `crux_moves_documentation.md`'s subtopic list (combinatorics:
`invariants-and-monovariants`, `extremal-principle`, `games-and-strategy`) — treat these as the
technique *categories* to search, not literal KB entries (I did not find a closer named KB
theorem specific to this).

### Analogous past problems (cruxes)
- **aimo-0340** (combinatorics, `invariants-and-monovariants`) — pearls-string cutting game with
  a per-step cut budget of k. Crux: *"Replace a single fragile survival inequality by a
  DISJUNCTIVE invariant whose second clause carries a reserve buffer, chosen so the exact
  transition where the plain inequality fails is caught by the other clause."* This is the
  closest structural analogy found: a cut-budget-capped adversarial process where a naive
  single-inequality induction breaks at one exact transition, fixed by a two-clause invariant
  with a "reserve" of untouched elements. Directly suggests the mechanism for Case (iii):
  maintain e.g. "(residual ≤ u_kΣ) OR (residual ≤ u_{k-1}Σ' AND m−1 further pieces all
  < Σ'/2 in reserve)" across the induction, with the reserve absorbing exactly the balanced
  transition. Worth a careful read of the full solution (`past_problems_database.json`,
  problem_id `aimo-0340`) by the outliner/builder.
- **aimo-0236** (combinatorics, `games-and-strategy`) — token-halving/valuation game with a
  "two-phase invariant that holds BOTH before AND after each opponent's move, self-restoring."
  Structurally relevant as a template for building an IH that survives one adversarial move
  (not just "apply IH once and done") — i.e., strengthen RT(k) to something that's stable under
  one op of Case (iii), not just checked at the top level.
- aimo-0117 flagged as a candidate (dyadic/geometric sequence structure) but its corpus solution
  text is a MISMATCH (Dutch dominoes proof unrelated to the stated stones-in-boxes problem) —
  do not use; likely a corpus data error.

### Prior progress
Unchanged from `current.md` / `dyadic-discrepancy.md` §4.5: RT reduces GAP U to Case (iii); Cases
(i),(ii) proven for all k; Case (iii) numerically true and tight only at the boundary (dyadic),
strictly sub-extremal in the interior (now quantified: ~72-88% of u_k at sampled points, k=2..4).

### Dead ends (do not retry)
- Greedy "remove-max-total" / black-box single-move+IH: rigorously refuted by the builder
  (telescopes above u_k for k≥3); reconfirmed consistent with my numerics (max-greedy path is
  not what the true optimal solver picks — Finding 1).
- Naive "sup over Case (iii) is attained as a monotone limit toward the boundary along any ray":
  REFUTED by Finding 3 — f is not globally monotone in ℓ_1 within Case (iii); only true along the
  specific extremal-adjacent ray tested, not generically. Do not assume monotonicity as a
  shortcut; any compactness argument must handle the jagged, piecewise-linear structure of f.
- Amortized W=2^{-cuts} as a standalone monovariant: too weak by a constant factor of ~2 (Finding
  4); not a working closed argument on its own.

### Small-case / intuition notes (all labeled conjecture / numerical)
- Conjecture (numerical, k≤4, thousands of samples): sup_{Case iii} f(k,·) < u_k strictly, with
  the gap shrinking toward 0 only as the partition approaches the Case-(i)/(ii) boundary; interior
  points have substantial slack (≥12% at k=2, growing to ≥24-28% at k=3,4).
- Conjecture (from Finding 1, single traced example, k=3): the optimal Case-(iii) strategy near
  the boundary is a chain of "pin largest against a smaller piece" moves resembling continued-
  fraction subtraction, not a single dominant-piece removal. Untested whether this generalizes as
  a clean deterministic rule across many Case-(iii) instances — only one trace examined; the
  outliner/builder should verify this pattern on more instances before committing to it as the
  strategy.
