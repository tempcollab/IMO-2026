# Lemma: halving-underpacks-compressed

**Status:** CERTIFIED (round 6, reviewer-certified).

**Statement.** For a strictly-decreasing m = n+1 Liu config L = (a_1 > ⋯ > a_{n+1}), the halving strategy (halve a_1, ..., a_n, leave a_{n+1}) packs

$$E_{\text{halve}} = \frac{1 - a_{n+1}}{2}.$$

In the compressed case (a_{n+1} > 1/D_n, where D_n = 2^{n+1} − 1), this is STRICTLY less than the tower target (2^n − 1)/D_n. Hence halving alone cannot close the compressed case; a genuinely different packing strategy (piece-matching / tie-creation) is needed.

**Proof.** By `halving-always-a-nplus1` (certified round 6), halving a_1, ..., a_n gives D = a_{n+1}. By `even-position-reframe` (certified round 6), E = (1 − D)/2. Hence E_halve = (1 − a_{n+1})/2.

In the compressed case a_{n+1} > 1/D_n:

$$E_{\text{halve}} = \frac{1 - a_{n+1}}{2} < \frac{1 - 1/D_n}{2} = \frac{2^n - 1}{D_n}.$$

The deficit is (a_{n+1} − 1/D_n)/2 > 0 on the E-side. ∎

**Interpretation.** The default halving strategy leaves a_{n+1} as the unique odd-multiplicity leftover. When a_{n+1} ≤ 1/D_n (the spreading case), this leftover is small enough — E_halve ≥ (2^n−1)/D_n. When a_{n+1} > 1/D_n (the compressed case), the leftover is too large — halving UNDERPACKS the even slots. Xiang must instead SPLIT the large pieces to create ties, driving the unique odd-multiplicity leftover DOWN to ≤ 1/D_n (the O2 mechanism). The existence of such a tie-creation strategy for every compressed config is the open core (GAP-U2-packing / GAP-U2-compressed).

**Verified.** n=2..5: E_halve < (2^n−1)/D_n whenever a_{n+1} > 1/D_n. ✓
