# Lemma: even-group-spine-lower-bound (S3)

**Statement.** Let `T_n=(2^n,2^{n-1},\dots,2,1)` (tower units, total `D_n=2^{n+1}-1`). Let
`M` be a **strong-breakpoint** refinement of `T_n` (every fragment ties an adjacent piece
in the sorted order — the vertex condition of `pl-breakpoint-minimum`) in which every
non-dyadic group (maximal run of adjacent-equal non-power-of-2 fragments) has EVEN count.
Then

$$D(M) \;\ge\; 1 \qquad(\text{tower units } = \; 1/D_n \text{ real}).$$

**Proof.** By `spine-pair-cancellation` (S1), `D(M)=D(\operatorname{sp}(M))` where the spine
is the config after removing all adjacent-equal pairs. At a strong breakpoint
(`strong-breakpoint-group-structure`, S2): (i) every dyadic fragment pairs off (each value
`2^k` either pairs with an extracted copy or is part of a balanced-split pair), so the only
dyadic survivors in the spine are values `2^k` appearing an ODD number of times; (ii) every
non-dyadic group of EVEN count `2r` is `r` adjacent-equal pairs, hence fully cancels
(Corollary S2), leaving NO non-dyadic leftover. So the spine is a strictly-decreasing sequence
of DISTINCT powers of 2: `2^{k_1}>2^{k_2}>\cdots>2^{k_s}` with `k_1>k_2>\cdots>k_s\ge 0`.

**Geometric bound.** `D=2^{k_1}-2^{k_2}+2^{k_3}-\cdots+(-1)^{s+1}2^{k_s}`. The negative terms
are a subset of `\{2^{k_2},\dots,2^{k_s}\}`, whose sum is at most the sum of ALL distinct
powers of 2 strictly below `2^{k_1}`, i.e. `\le 1+2+\cdots+2^{k_1-1}=2^{k_1}-1` (geometric
series). The positive terms beyond the first are also a subset of the smaller powers, so they
only increase `D`. Hence `D\ge 2^{k_1}-(2^{k_1}-1)=1`.

**Nonempty.** The total mass of `M` is `D_n=2^{n+1}-1` (ODD). Each removed adjacent-equal pair
contributes mass `2v` (EVEN). So the spine's total mass is `D_n-(\text{even sum})`, which is
ODD, hence `\ge 1` — the spine is nonempty. (Equivalently, a nonempty strictly-decreasing
sequence of distinct powers of 2 has odd sum iff `2^0=1` is among them.) ∎

**Verified.** All `2^7-1=127` nonempty strictly-decreasing subsequences of
`\{1,2,4,\dots,64\}` have `D\ge 1`, min `=1` (at `\{1\}` or `\{2,1\}`). Direct alternating-sum
recomputation on constructed even-group strong breakpoints of `T_n` for `n=2,3,4` matches.

**Closes:** the even-group strong-breakpoint sub-case of the non-dyadic multi-split lower-bound
gap (G1) for ALL `n`. Does NOT close the odd-count sub-case (G2-odd): odd-count non-dyadic
groups leave a leftover in the spine whose sign depends on global position parity (witnesses:
`\{4.75,4,0.25\}` `D=1`; `\{4,7/3,2\}` `D=11/3`), and odd-group MINIMIZERS (`D=1`) exist, so
the bound must be tight to 1 — the geometric argument fails there. The odd-count spine bound
is the open hard step.

**Importable by:** `tower-induction` (Route D even-group sub-result), `tail-count` (the
pair-cancellation even-group sub-step, derived here from the block/spine viewpoint — same
result, different machinery), `gaps-leftover` (the spine-charging even-group base case).

**Depends on:** `spine-pair-cancellation` (S1), `strong-breakpoint-group-structure` (S2),
`pl-breakpoint-minimum`.
