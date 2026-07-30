## imo-2026-03

### majorization-upper: advance (WALL U — compressed case via O1 split-bottom + IVT, plus the cheap certifiable milestone)
Target: Prove D* ≤ 1/D_n for the compressed case a_{n+1} > 1/D_n (m = n+1, strictly decreasing, smallest piece exceeds the tower's smallest), completing the general-n upper bound c(n) ≤ 2^n/D_n.
Technique: IVT / intermediate value on a one-parameter tunable split + PL-breakpoint machinery (`pl-breakpoint-minimum`). The continuity is in the split piece x; the exact-pairing feasibility of the rest is a PL function of x with finitely many breakpoints.
Skeleton:
  1. CERTIFY the cheap milestone `halving-always-a-nplus1` (halving a_1,…,a_n gives D = a_{n+1} for ANY strictly-decreasing m=n+1 config, all n) — by the parity/grouping argument (each a_i/2 is pairwise distinct ⟹ size-2 block ⟹ contributes 0; the unique odd-block a_{n+1} sits at position 1 + 2·(#blocks above it) = odd ⟹ contributes +a_{n+1}). Verified 0/20000 exact-Fraction.
  2. This immediately closes the a_{n+1} ≤ 1/D_n region for ALL n (D* ≤ a_{n+1} ≤ 1/D_n, unconditional, no bottom-dominance hypothesis) — generalizes + drops the hypothesis of `bottom-dominant-halving`. Fold this closure into Part VIII of this slug.
  3. Compressed case (a_{n+1} > 1/D_n): split a_{n+1} → {x, a_{n+1} − x} with x ∈ (0, 1/D_n] (1 mark). The leftover x is the unique odd-block (sits at an odd position by the same parity structure as step 1) ⟹ contributes +x; all size-2 blocks contribute 0 — by the parity argument of `halving-always-a-nplus1` generalized to the split-bottom refinement.
  4. The remaining n pieces {a_1,…,a_n, a_{n+1}−x} must be exactly paired into n/2 equal pairs via n−1 marks (each pair → size-2 block → contributes 0). Then D = x ≤ 1/D_n — by `spine-pair-cancellation` / even-block contribution.
  5. The exact-pairing feasibility of {a_1,…,a_n, a_{n+1}−x} is a function of the continuous parameter x with finitely many PL breakpoints (where a fragment ties an existing piece) — by PL structure (sort order changes at finitely many x-values).
  6. IVT / parity-on-breakpoints: at x = a_{n+1} (no split) the rest is unpaired and D = a_{n+1} > 1/D_n; as x ↓ 0 the rest {a_1,…,a_n,a_{n+1}} approaches the original n+1 config, and (conjecturally, via the bounded-spread pigeonhole) becomes pairable. Prove ∃ x ≤ 1/D_n admitting a valid exact pairing — by IVT on the PL-pairing-feasibility correspondence, OR by the bounded-spread pigeonhole fallback below.
  7. Conclude D = x ≤ 1/D_n for the compressed case ⟹ general-n upper bound complete — by step 2 (a_{n+1}≤1/D_n) + step 6 (a_{n+1}>1/D_n).
Key lemmas (claim + one-line mechanism):
  - `halving-always-a-nplus1` (D = a_{n+1} for any strictly-decreasing m=n+1 config under n-mark halving) — because strictly-decreasing ⟹ a_i/2 pairwise distinct ⟹ each forms a size-2 block at an even start position ⟹ contributes 0; the a_{n+1}-block is the unique odd-multiplicity block and starts at an odd position.
  - Exact-pairing existence for some x ≤ 1/D_n (THE OPEN CORE) — because x is a continuous tunable lever and the pairing-feasibility structure is PL with finitely many breakpoints; the bounded-spread pigeonhole (a_{n+1} > 1/D_n ⟹ a_i ≥ a_{n+1} > 1/D_n for all i ⟹ a_1 ≤ 1 − n/D_n = (D_n − n)/D_n ⟹ spread a_1/a_{n+1} < D_n − n) gives near-equal pieces ⟹ a matchable multiset.
Open gaps: Step 6 — the exact-pairing existence for some x ≤ 1/D_n. The "pairable as x → 0" needs a real argument; the bounded-spread pigeonhole is the conjectured mechanism (near-equal pieces ⟹ matchable), but the subset-sum/multiset-equal-sums existence is the genuine open core. Parity obstruction is consistent: n marks ⟹ 2n+1 refined pieces (odd) ⟹ D ≠ 0; the split-bottom route leaves x as the unique odd leftover, so D = x (small), never D = 0 via n marks — matches the target D ≤ 1/D_n (not D = 0).
Cases to cover: none beyond the single compressed regime (all n, strictly-decreasing m=n+1, a_{n+1} > 1/D_n).
Watch out for: do NOT assert "pairable at x → 0" without the bounded-spread argument — the subset-sum existence is the load-bearing unproved step. The bottom-up pair-cascade (residual recurrence) is DEAD (residual = D(L) ≫ 1/D_n) — do not revive it; only the split-bottom tunable route is live. The V(n)←V(n−1) IH and 3-mark cascade are DEAD (phantom-crux) — do not revive.

### even-packing-upper: new (WALL U — compressed case via O4 even-position packing, a genuinely different optimization framing)
Target: Prove D* ≤ 1/D_n for the compressed case a_{n+1} > 1/D_n via the even-position packing reframe (maximize even-position sum).
Technique: Optimization / greedy packing on alternating slots (NOT IVT/continuity, NOT subset-sum existence — a different certificate form: the primal "max even-sum" view).
Skeleton:
  1. Algebraic reframe: D = 1 − 2·E where E = even-position sum of the refined multiset (since D = odd-sum − even-sum and odd+even = 1). Target D ≤ 1/D_n ⟺ E ≥ (2^n − 1)/D_n — by the D=total−2·even identity (verified 0/5000; tower tight at E = (2^n−1)/D_n).
  2. Tower reference: parallel halving of T_n packs EXACTLY (2^n − 1)/D_n into even slots (tight, certified `parallel-halving-saturates-tower`) — the tower is the unique minimizer of E.
  3. Compressed configs are near-equal: a_{n+1} > 1/D_n ⟹ every a_i ≥ a_{n+1} > 1/D_n ⟹ a_1 ≤ (D_n − n)/D_n ⟹ spread a_1/a_{n+1} < D_n − n (bounded factor) — by the size bound.
  4. GREEDY PACKING LEMMA (THE OPEN STEP): for a bounded-spread multiset (spread < D_n − n, n+1 pieces summing to 1), Xiang can place ≤ n marks so that the refined multiset's even positions absorb ≥ (2^n − 1)/D_n mass — by a greedy "fill even slots from the largest pieces" argument: near-equal pieces distribute evenly across alternating slots at high density, strictly exceeding the tower's packed amount (the tower is the LEAST packable because its geometric spread concentrates mass in odd slots).
  5. Conclude D = 1 − 2·E ≤ 1/D_n for the compressed case — by step 1 + step 4.
Key lemmas (claim + one-line mechanism):
  - D = 1 − 2·E (algebra) — because D = odd-sum − even-sum and odd+even = total = 1.
  - Greedy even-slot packing ≥ (2^n−1)/D_n for bounded-spread multisets — because near-equal pieces (spread < D_n−n) distribute mass evenly across alternating positions at density ≥ 1/2 − O(1/spread), and the tower's geometric concentration in odd slots is the WORST case for even-slot packing (its even-sum = (2^n−1)/D_n is the minimum achievable even-sum). Mechanism: the tower is the extremal MINIMIZER of even-sum (most mass trapped in odd slots by the 2:1 geometric cascade); compressing the spread strictly increases the even-sum.
Open gaps: Step 4 — the greedy packing bound. The mechanism "tower is the minimizer of even-sum; compression increases it" is the conjectured extremal/packing argument. Needs a rigorous exchange/smoothing proof (not just intuition): show that any deviation from the 2:1 geometric cascade shifts mass from odd to even slots.
Cases to cover: none beyond the compressed regime.
Watch out for: the greedy may not be optimal; Xiang's marks affect the sort order (hence which positions are even). The "compression increases even-sum" exchange step must be proven, not assumed — it is the dual of the (refuted) Max-bound exchange; do NOT assume Schur-convexity (D* is not Schur-convex). This framing is genuinely different from O1: it attacks the max even-sum (an optimization/packing quantity) rather than the subset-sum existence, so it does NOT bottom on the same subset-sum core as O1/O2/bounded-spread.

### tail-count: advance (WALL L — sub-gap (i) "balance ⟹ block" via route A: PL + mass-balance + dyadic dominance)
Target: Prove D ≥ 1 (tower units) at every breakpoint config of T_n, closing the lower bound c(n) ≥ 2^n/D_n for all n.
Technique: PL+breakpoint reduction (`pl-breakpoint-minimum`) + mass-balance (`mass-balance-lemma`) + dyadic-dominance / superincreasing forcing (route A).
Skeleton:
  1. PL+breakpoint reduction (certified): the global min of D over all ≤ n-mark refinements of T_n is attained at a breakpoint (tie) config — by `pl-breakpoint-minimum`.
  2. Mass-balance (certified): on any cell, D = 2·S₊ − D_n (S₊ = mass at + positions); so D = 1 ⟺ S₊ = 2^n — by `mass-balance-lemma` (pure algebra, tie-agnostic).
  3. At a breakpoint, S₊ (hence D) is tie-agnostic. The top-piece fragments sum to 2^n; the below-top tower pieces sum to 2^n − 1. So D = 1 ⟺ (mass of below-tower pieces at +) = (mass of fragments at −) — by mass-balance + the tie structure.
  4. HARD STEP "balance ⟹ block": the breakpoint structure (every fragment ties an adjacent piece) + dyadic dominance of tower pieces (each 2^k > Σ_{j<k} 2^j, the superincreasing property) forces (fragments at −) = 0 (the block condition) — by the superincreasing chain-forbiddance argument below. (THE OPEN STEP; verified 0/523 counterexamples across T_3/T_4/T_5 after the origin-based reclassification.)
  5. Block condition holds ⟹ `telescoping-block-lemma` gives D = 2^n − (2^n − 1) = 1 directly on the spine (all fragments at +, all below-tower at −) — by `telescoping-block-lemma` (certified, GAP-B(d)).
  6. Conclude D ≥ 1 at every breakpoint ⟹ D ≥ 1 everywhere ⟹ lower bound c(n) ≥ 2^n/D_n — by step 1 + step 5.
Key lemmas (claim + one-line mechanism):
  - "balance ⟹ block": if a fragment f sits at a − position, then by sorted order some tower piece t > f (or a fragment tied to a tower piece) sits at the preceding + position; the balance (towers at +) = (fragments at −) then requires a subset of (other tower pieces + other fragments) to exactly cover the deficit — but the superincreasing structure (each 2^k > sum of all smaller 2^j) makes such an exact cover by smaller tower pieces IMPOSSIBLE unless (fragments at −) = 0. Mechanism: the tower pieces are a superincreasing sequence, so no nontrivial subset-sum of smaller pieces equals a larger one — the only solution to the balance equation is the trivial (all fragments at +, all below-tower at −).
  - Mass-balance (D = 2S₊ − D_n, D=1 ⟺ S₊ = 2^n) — certified, the algebraic engine that converts the geometric balance to a numerical equality.
Open gaps: Step 4 — the "balance ⟹ block" implication. The superincreasing chain-forbiddance is the conjectured mechanism (verified 0/523 T_3/T_4/T_5), but the rigorous subset-sum exclusion across all tie-breakings is not yet a proof. The hard sub-case: fragments that tie tower pieces (a fragment value may equal a tower piece 2^k, creating sign-assignment ambiguity).
Cases to cover: (a) dyadic endpoints (all fragments pair-cancel, spine all-tower, D = 1 by `dyadic-refinement-lower-bound`) — settled; (b) split-tower balanced top (generalized GAP-B(d) at level k) — settled; (c) general non-dyadic breakpoint — THE OPEN CASE (step 4).
Watch out for: the spine sign-pattern / multi-swap subset-sum framing is CIRCULAR (F = T+1 ≡ D(spine)=1 under the assumed pattern; Fraction counterexample T_3 spine {5,2}) — do NOT chase it. Sub-gap (ii) is VACUOUS (certified `mass-balance-lemma`) — do not re-attack. The superincreasing argument must handle fragments tied to tower pieces (sign-assignment ambiguity) rigorously, not just the clean case.

### tower-induction: hold (WALL L — G2-odd spine sign-bookkeeping, the rival mechanism for the same lower wall; NOT built this round)
Target: same as tail-count (whole lower bound), via the spine arithmetic / sign-bookkeeping framework (S1/S2/S3).
Technique: Spine arithmetic — adjacent-equal pair-cancellation (`spine-pair-cancellation`), strong-breakpoint group structure (`strong-breakpoint-group-structure`), even-group spine lower bound (`even-group-spine-lower-bound`).
Skeleton: S1 spine-pair-cancellation reduces to a strictly-decreasing spine; S2 groups non-dyadic fragments at strong breakpoints; S3 closes even-group breakpoints. The OPEN step is G2-odd: odd-count non-dyadic leftovers — the leftover's sign is a GLOBAL position-parity quantity, and the frontier recursion does not extend to unbalanced splits.
Status: STUCK on G2-odd for 3 rounds. The explorer confirmed no 6th genuinely-different lower framing exists (5 framings — PL, spine, gaps-leftover, LP, XOR — all converge on the same G1-equivalent wall). This is the rival MECHANISM for the same wall as tail-count's route A; HOLD this round (do not build) so the lower-wall build budget goes to tail-count's route A (the primary, more-concretely-verifiable advance). If route A stalls, revisit this spine mechanism next round.
Open gaps: G2-odd (leftover sign-bookkeeping) — undeveloped.
Watch out for: the spine sign-pattern framing is CIRCULAR (round-5 negative) — do NOT retry. This slug is the S1/S2/S3 machinery (value-agnostic), NOT the circular spine sign-pattern/multi-swap framing.

---

## COPY recommendation
None. The two compressed-case routes (O1 split-bottom+IVT in `majorization-upper`, O4 even-packing in `even-packing-upper`) are genuinely different FRAMINGS (continuity/IVT vs optimization/packing), not two ways to fill the same gap within one approach — so they are separate slugs, not a copy-twin of one.

## Diversity note (single-gap trap avoidance)
On WALL U, `majorization-upper` (O1) bottoms on the exact-pairing/subset-sum existence for some x ≤ 1/D_n; `even-packing-upper` (O4) bottoms on the greedy even-slot packing bound (an exchange/extremal argument that the tower minimizes even-sum). These are DIFFERENT open cores (subset-sum existence vs packing-density exchange), so the two slugs do not die together on a single gap. The bounded-spread pigeonhole and O2 (split-large-to-match-medium) both bottom on the SAME subset-sum existence as O1 — so they are folded as a FALLBACK within `majorization-upper` (step 6), NOT opened as separate slugs (avoids the single-gap trap on the upper wall).

build set: majorization-upper, even-packing-upper, tail-count
