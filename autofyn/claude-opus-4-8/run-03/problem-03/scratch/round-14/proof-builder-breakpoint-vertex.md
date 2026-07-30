# Build report — breakpoint-vertex (UPPER wall), Round 14

**Status: partial. Gate run first (mandatory); no proof shipped — the route's closing mechanism is refuted by the corrected numeric picture.**

## What I did
Ran the mandatory numeric/exact-fraction gate for the extremal-tie / smoothing-minimax route over the ACTUAL valley domain `{a_1<1/2, a_2<β_n}` (β_n=2^{n-1}/(2^{n+1}-1)) at n=3..8, using the certified `Φ(A)=min positive descending-include/skip reachable value = min_{∅≠T tree-realizable}descKK(T)` (Lemma FGR). Located maximizers, measured the tie structure, and searched for the true valley max.

## Gate outcome (decisive)
1. **Bound holds (target sound).** No valley profile with `Φ/u_n ≥ 1` exists (exact + multi-restart search, n=3,4,5). Prop UV is TRUE.
2. **No margin — the reviewer's premise is REFUTED.** Explicit exact valley family
   `A^{(n)} = {2^n, 2^{n-1}, …, 4, 3, 2}/(2^{n+1}+1)` (dyadic ladder with its two smallest parts {2,1}→{3,2}, which pushes `a_1=2^n/(2^{n+1}+1)<1/2` INTO the valley; `a_2<β_n` holds) has
   `Φ(A^{(n)}) = 1/(2^{n+1}+1)`, so `Φ/u_n = (2^{n+1}-1)/(2^{n+1}+1) → 1`.
   Exact ratios: 0.882, 0.939, 0.969, 0.985, 0.992, 0.996 at n=3..8. The claimed "worst 0.75, interior maximizer with margin" was an under-sampling artifact. **The valley residual is asymptotically as tight as the full upper bound.**
3. **Maximizer is a degenerate, n-dependent tied face.** At `{16,8,4,3,2}/33` (n=4) the min value `1/33` is achieved by 14 distinct signed patterns at once; the whole-tail difference `|2a_1−1|` and many short interior differences all tie. No clean single achiever, no closed-form pin.

## Why I stopped (no fake proof)
The extremal-tie step 4 (unique achiever ⇒ feasible ascent ⇒ contradiction) is sound in kind and gives the dichotomy "boundary active or ≥2 tied achievers." But step 5 — turning that into `Φ ≤ u_n` — needed a clean maximizer bounded away from tight (a margin). Findings 1–3 kill this: no asymptotic margin, and the maximizing face is high-dimensional, degenerate, and n-varying. Closing the valley now requires an EXACT tight argument reproducing `u_n` on that face — no easier than the full open crux. Per the directive ("if the gate FAILS, report the refutation and STOP"), I shipped no proof.

## Deliverable
Promotable **Lemma VALLEY-TIGHT**: explicit exact valley family `A^{(n)}={2^n,…,4,3,2}/(2^{n+1}+1)` with `Φ = 1/(2^{n+1}+1)`, ratio→1, certifying `M*_valley/u_n → 1` (the valley residual is asymptotically tight). Verified exactly n=3..8.

## Recommendation (Spec note)
- The reviewer's binding correction rested on a numerically wrong margin (0.75). Corrected: `M*_valley → u_n`.
- Both upper vehicles that rely on the valley having exploitable slack are dead for the same reason: breakpoint-vertex's margin-bound closing AND valley-differencing-construction's robustness/margin premise. Do NOT re-attempt any crude/non-tight bound in the valley — provably impossible.
- Honest residual unchanged (first-gap / Subset-KK pigeonhole `min_{∅≠T}descKK(T) ≤ u_n`), now known TIGHT throughout the valley. Next lever must be a genuinely different TIGHT framing (exact induction carrying the `{…,4,3,2}` near-extremal family, or the LOWER-wall LP-dual/smoothing machinery transported to the reachable-value discrepancy).

Files: results/imo-2026-03/approaches/breakpoint-vertex.md (Round 14 section at top).
