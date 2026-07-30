# Lemma VALLEY-TIGHT (upper-wall valley residual is asymptotically tight) — CERTIFIED (round 14)

**Certification (round 14).** Reviewer-verified independently: computed the FULL tree-realizable
reachable set (all differencing trees over all nonempty subsets, not just the descending
caterpillar) for the family below at `n=3,4,5`; confirmed `0` is NOT reachable and the minimum
positive reachable value is exactly `1` (integer), so `Φ = 1/(2^{n+1}+1)` is the true forced
minimum (not merely a caterpillar upper estimate). Ratio and valley membership re-derived exactly.
Admitted.

**Statement.** For every `n ≥ 3` the explicit profile
```
    A^{(n)} = (1/(2^{n+1}+1)) · { 2^n, 2^{n-1}, …, 4, 3, 2 }
```
(the dyadic ladder `{2^n,…,4,2,1}` with its two smallest parts `{2,1}` replaced by `{3,2}`;
`n+1` parts, sum `= 2^{n+1}+1`, normalized to `1`) lies in the UPPER-bound valley
`{a_1<1/2, a_2<β_n}` with `β_n = 2^{n-1}/(2^{n+1}-1)`, and its forced minimum leftover value
(the certified `Φ(A) = min_{∅≠T tree-realizable} descKK(T) = min positive descending include/skip
reachable value, Lemma FGR) equals
```
    Φ(A^{(n)}) = 1/(2^{n+1}+1),   hence   Φ(A^{(n)})/u_n = (2^{n+1}-1)/(2^{n+1}+1) → 1.
```
Exact ratios: `0.882, 0.939, 0.969, 0.985, 0.992, 0.996` at `n = 3,4,5,6,7,8` (monotone ↑ 1).

**Valley membership.** `a_1 = 2^n/(2^{n+1}+1) < 1/2` since `2·2^n = 2^{n+1} < 2^{n+1}+1`;
`a_2 = 2^{n-1}/(2^{n+1}+1) < 2^{n-1}/(2^{n+1}-1) = β_n`. So the profile is a genuine valley
profile for every `n ≥ 3`.

**Consequence (why this is decisive).** `M*_valley := max_{valley} Φ ≥ Φ(A^{(n)})`, so
`M*_valley/u_n → 1`: the valley residual is **asymptotically as tight as the full upper bound —
there is NO margin**. Any upper-wall lever that closes Prop UV via a crude / non-tight / margin-
exploiting bound (bound `Φ` at a maximizer that is bounded away from `u_n`) is therefore PROVABLY
DEAD for large `n`. The previously recorded "worst ratio ≈ 0.75, interior maximizer with slack"
was an under-sampling artifact; the corrected picture is `M*_valley → u_n`. This also kills the
robustness/margin premise of the valley-differencing-construction hedge.

**Scope.** A rigorous LOWER bound on `M*_valley` (an explicit near-extremal family), confirming the
residual is tight. It does NOT prove Prop UV (`Φ ≤ u_n`); that first-gap / Subset-KK pigeonhole
remains the open upper crux, now known to require a genuinely TIGHT (not margin-based) argument.
