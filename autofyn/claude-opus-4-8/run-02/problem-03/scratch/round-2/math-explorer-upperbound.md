## imo-2026-03 — lens: GAP U, the general upper bound (Xiang's non-myopic ≤n-cut strategy)

### Setup recap (verified against certified spine, no re-derivation needed)
Game reduced (Lemma G + level-measure identity, both CERTIFIED in `lemmas/greedy-claim.md`)
to: for Liu's partition into m ≤ n+1 pieces, Xiang has ≤ n further cuts (each splits one
current piece into two positive parts) to minimize D = λ{t : N(t) odd}, N(t)=#{pieces>t}.
Target: for EVERY Liu partition, min_Xiang D ≤ u = 1/(2^{n+1}-1). Known refuted rules:
"bisect the n largest, leave smallest" and myopic greedy (both in current.md already).

### New numerical work this round (brute-forced optimal Xiang response, general Liu inputs)
I built a genuine (not myopic) optimizer: for a Liu partition of m parts, enumerate all cut-
budget allocations (k_1,...,k_m) with Σk_i ≤ n (k_i = extra cuts spent subdividing piece i
into k_i+1 sub-parts), then for each allocation run many-restart Nelder–Mead over the actual
split positions to find the true min D for that allocation, then minimize over allocations.
This is a genuinely general (non-restricted) search over all Xiang strategies, not merely
bisection or myopic. Verified against known certified facts first (dyadic n=2 gives exactly
1/7, dyadic n=3 gives exactly 1/15) — matches current.md's numbers exactly, so the tool is
trustworthy.

**Critical methodological finding (a cheap-kill warning for future rounds):** an outer
adversarial search over Liu configs, using an UNDER-converged inner optimizer (only 4
restarts), found an apparent counterexample Liu=[0.6026,0.3013,0.0961] with min D ≈ 0.205 >
u₂=1/7 — this looked like it would REFUTE the conjectured answer. Re-running the inner
optimization on that same Liu config with 60 restarts instead gives the true value 0.0961 <
1/7 (Xiang's real best reply: bisect pieces 1 and 2, i.e. split 0.6026→{0.3013,0.3013} and
0.3013→{0.1506,0.1506}, leave 0.0961 alone). **Any numerical "counterexample" to D*=u must be
re-verified with a much better-converged inner minimization before being trusted** — spurious
violations from non-convergence are easy to manufacture and would wrongly suggest the answer
c(n)=2^n/(2^{n+1}-1) is false. I record this so no future round wastes effort chasing a fake
refutation.

With well-converged inner search, a random scan of 25-40 Liu configs (n=2) all gave min D <
1/7 (max found ≈ 0.118 < 0.1429), consistent with the dyadic partition being the true
maximizer — this is *conjecture, strong numerical support*, not new proof.

### Distinct openings for GAP U

**Opening 1 — "cut only the dominant piece" (self-similar recursive rule).**
On the DYADIC Liu partition specifically, the optimizer's found optimum for n=2 and n=3 both
concentrate Xiang's cuts entirely on the TOP piece (allocation (n,0,...,0) achieves exactly
D=u, tied with the already-known bisect-two-largest strategy). This is consistent with the
self-similar recursive picture already in induction-recursion.md (top piece g=2^n u, bottom
block = scaled (n-1)-dyadic): cutting the top piece with the full remaining budget in a
scaled-recursive way and leaving the (already near-optimal) bottom block alone reproduces the
same structure one level down. **However this rule is REFUTED as a GENERAL rule**: on a
near-balanced Liu partition [0.4192,0.3880,0.1928] (b1≈b2), restricting Xiang to cut ONLY the
top piece gives worst-case 0.1615 > 1/7, i.e. strictly worse than u — cutting only the top
piece is provably suboptimal there. The TRUE optimal response on that config instead spends
both cuts subdividing the SMALLEST piece (splitting 0.1928 into ~{0.0964,0.0964,~0}),
achieving D≈0.031 ≪ 1/7. **Do not present "always cut the top piece" as the general rule —
numerically refuted.** This is new evidence (this round), sharper than round-1's refutation of
"bisect n largest."

**Opening 2 — adaptive two-regime rule generalizing the proven n=1 rule.**
The n=1 rule (certified in dyadic-discrepancy.md §3) is: bisect the big piece if the small
piece p ≤ 1/3, else pin the median at p (leave uncut / cut minimally). The n=2/n=3 data above
shows the SAME dichotomy one level up: when the top piece dominates (dyadic-like, top piece >
half the total and much larger than the rest), Xiang should subdivide the TOP piece (matches
Opening 1's finding on dyadic); when the top pieces are already close to balanced (small
"pairing gap" b1−b2), Xiang should instead subdivide the SMALLEST piece(s) to fix the
parity/count without disturbing the near-cancelling top pairs. This suggests the correct
general Xiang rule is: **look at the pairing-form gaps (b1−b2), (b3−b4), ... and spend cuts to
close whichever gap is largest / whichever piece is "extra" (the odd-count leftover), doing
so recursively** — i.e. a genuine greedy-on-gaps (not greedy-on-D-reduction, which was already
refuted as myopic) rule. This is the most promising opening: it unifies the n=1 proof, the
dyadic-optimal top-cut, and the near-balanced bottom-cut behavior into one adaptive
prescription, but the exact general statement and proof are NOT worked out here — this is
scouting, not a proof.

**Opening 3 — LP/potential certificate, order-aware version.**
potential-certificate.md already proved NO separable per-piece potential can certify the
bound (clean witness + LP infeasibility) — this is a genuine, certified dead end for any
*separable* weighting scheme; do not retry a per-piece potential. An ORDER-AWARE certificate
(a function of the sorted sequence and cut structure jointly, not a sum of independent
per-piece terms) has not been tried and is not obviously ruled out by the separability-gate
argument (that argument specifically used a splitting witness that behaves oppositely on two
different multisets — it does not address certificates depending on rank/position). This
remains open territory but is a genuinely different (non-constructive, duality-flavored)
route from Openings 1-2 if a direct adaptive construction stalls.

**Opening 4 — direct budget-vs-piece-count pigeonhole (from round-1 explorer), reframed.**
Round-1's mechanism ("Xiang is exactly one cut short of bisecting all n+1 pieces, forcing an
odd leftover tier") is exactly right for the SYMMETRIC dyadic case (produces the tie structure
seen in Opening 1's alternative optimum) but does not obviously generalize since a non-dyadic
Liu partition need not produce clean "tiers" after bisection at all (that's exactly why
bisection-only is refuted). The pigeonhole idea should be re-targeted at the GAP structure
(pairing-form (b_{2i-1}-b_{2i})) rather than at literal tiers of equal pieces — connects
directly to Opening 2.

### Cheap-kill candidates
- **Convergence-gate on any numerical claim about D*:** before trusting ANY new numeric
  "min D" value for a candidate Liu config, re-run with ≥15-20 restarts of a derivative-free
  optimizer (or a proper allocation-enumeration + refined local search as above); single-shot
  or low-restart numerics gave a false > u result this round (see above) and would have misled
  the outliner into doubting the (correct) answer.
- The b1 vs (1-b1) domination bound D ≥ 2b1-1 (already certified, `cut-flip.md` C3) gives an
  immediate necessary condition: Xiang MUST reduce the top piece below (1+u)/2 = 2^{n-1}u+1/2ish
  whenever it's large, i.e. whenever Liu's top piece exceeds (1+u)/2, Xiang has no choice but to
  cut it — this is consistent with Opening 1 kicking in only in the "top-dominant" regime.

### Knowledge-base entries to use
- General Proof Methods: exchange/induction arguments (used already for Lemma G; likely needed
  again for Opening 2's adaptive rule proof).
- Invariants and monovariants — a rank/gap-based monovariant is the natural formalization of
  Opening 2's "close the largest gap" rule.
- Extremal principle / smoothing — relevant to proving Opening 2's adaptive rule is optimal
  (an exchange argument showing no other cut allocation beats "close the largest gap first").
- Nothing new found beyond what's cited in current.md; the crux corpus search (below) did not
  surface additional KB-adjacent tools specific to GAP U.

### Analogous past problems (cruxes)
Re-checked `crux_moves_documentation.md` fields; queried combinatorics/games-and-strategy and
combinatorics/extremal-principle subtopics for "adaptive/threshold" or "gap-closing" strategy
patterns analogous to Opening 2. Found nothing meaningfully closer than round-1's two
citations (`aimo-0225` dyadic-valuation P/N parity flavor, `aimo-0663` slot-vs-budget
pigeonhole) — both already flagged as "flavor only, not template" in round 1; that verdict
still stands after this round's more concrete numerics. **No new genuinely analogous crux
found for the adaptive two-regime rule (Opening 2).**

### Prior progress
Unchanged from current.md: full spine certified (Lemma G, level-measure identity, cut-flip),
n=1 fully solved both directions, lower-bound Case A closed. GAP U is untouched by any
approach beyond the "framework" stated in dyadic-discrepancy.md §4. This round's numerics
sharpen the picture (two concrete refutations: top-cut-only and, from round 1, bisect-n-
largest / myopic-greedy) and surface Opening 2 as the most concrete new candidate mechanism.

### Dead ends (do not retry)
- **Bisect the n largest, leave smallest** (round 1) — refuted, Liu can reach ~0.75.
- **Myopic greedy (reduce D most per single cut)** (round 1) — refuted, Liu 0.65 > 4/7 at n=2.
- **"Cut only the single largest piece with the whole budget" as a UNIVERSAL rule** (this
  round, new) — refuted: fails on near-balanced Liu (e.g. [0.4192,0.3880,0.1928], n=2), where
  it gives 0.1615 > u2=0.1429, while the true optimum (cut the smallest piece instead) gives
  0.031. Works only in the "top-dominant" regime (dyadic-like); do not present as a general
  rule.
- **Separable per-piece potential certificate** (round 1, potential-certificate.md) — proven
  dead end (LP infeasibility + explicit witness); do not retry a separable weighting.

### Small-case / intuition notes (labeled conjecture except where noted)
- n=2 dyadic: min D = 1/7 exactly, confirmed by well-converged brute force (allocation "both
  cuts on top piece" ties with "bisect two largest"). CONJECTURE (strong numerical support,
  not proof): 1/7 is the true max over all Liu partitions for n=2 (25+ random configs all
  strictly below 1/7 with well-converged inner search).
- n=3 dyadic: min D = 1/15 exactly, same tie structure (all-cuts-on-top achieves it).
- The optimal Xiang allocation is regime-dependent: concentrate on the top piece when it
  dominates (dyadic-like inputs); concentrate on the smallest piece(s) when the top few pieces
  are already near-balanced. This adaptive two-regime behavior, first proven rigorously at
  n=1 (bisect big piece vs pin median), now has numerical confirmation one level up (n=2,3) —
  this is the shape GAP U's eventual proof will likely need to formalize (Opening 2).
