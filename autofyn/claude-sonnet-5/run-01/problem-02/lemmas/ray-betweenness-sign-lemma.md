# Lemma: ray-betweenness sign lemma (Lemma A)

**Source approach:** `synthetic-angle-chase-aklastar` (round 5, "Step 7"). Certified by proof-reviewer,
round 5 — re-derived independently by hand and stress-tested numerically (200,000 random trials,
0 failures, constructed via an independent `atan2`-based random-direction interpolation, not via the
formula being tested) before certification. No gaps.

**Statement.** Let $V,R,P,Q$ be four points with $P,Q\notin$ line $VR$. Suppose $P$ lies in the
interior of the (non-reflex) angle $\angle RVQ$, meaning $P$ lies simultaneously (a) on the same side
of line $VR$ as $Q$, and (b) on the same side of line $VQ$ as $R$ (the standard definition of the
interior of a convex angular sector as the intersection of its two bounding half-planes). Then
$$\mathrm{sign}\big(\mathrm{cross}(P-V,Q-V)\big)=\mathrm{sign}\big(\mathrm{cross}(R-V,P-V)\big).$$

**Proof.** For $X\ne V$ write $\theta(X)\in(-\pi,\pi]$ for the directed CCW angle from ray $VR$ to ray
$VX$, so $\mathrm{sign}(\sin\theta(X))=\mathrm{sign}(\mathrm{cross}(R-V,X-V))$. Condition (a) says
$\mathrm{sign}(\sin\theta(P))=\mathrm{sign}(\sin\theta(Q))=:\sigma\in\{+1,-1\}$ (both nonzero since
$P,Q\notin$ line $VR$). Condition (b) is the side test for line $VQ$:
$\mathrm{sign}(\mathrm{cross}(Q-V,P-V))=\mathrm{sign}(\mathrm{cross}(Q-V,R-V))$. Using
$\mathrm{cross}(Q-V,P-V)=|Q{-}V||P{-}V|\sin(\theta(P)-\theta(Q))$ and
$\mathrm{cross}(Q-V,R-V)=|Q{-}V||R{-}V|\sin(0-\theta(Q))=-|Q{-}V||R{-}V|\sin\theta(Q)$, condition (b)
becomes $\mathrm{sign}(\sin(\theta(P)-\theta(Q)))=-\sigma$.

*Case $\sigma=+1$:* $\theta(P),\theta(Q)\in(0,\pi)$, so $\theta(P)-\theta(Q)\in(-\pi,\pi)$, and
$\sin(\theta(P)-\theta(Q))<0 \iff \theta(P)<\theta(Q)$. So $0<\theta(P)<\theta(Q)<\pi$, giving
$\theta(Q)-\theta(P)\in(0,\pi)$, hence $\mathrm{cross}(P-V,Q-V)=|P{-}V||Q{-}V|\sin(\theta(Q)-\theta(P))>0$
— matching $\mathrm{sign}(\mathrm{cross}(R-V,P-V))=\mathrm{sign}(\sin\theta(P))=+1$.

*Case $\sigma=-1$:* symmetric; $\theta(P),\theta(Q)\in(-\pi,0)$, forcing $\theta(Q)<\theta(P)<0$, giving
$\theta(Q)-\theta(P)\in(-\pi,0)$, so $\mathrm{cross}(P-V,Q-V)<0$, matching
$\mathrm{sign}(\mathrm{cross}(R-V,P-V))=-1$. $\blacksquare$

**Reviewer's independent verification.** Re-derived the case-split proof from scratch (matches).
Separately verified numerically: 200,000 random $(V,R,Q)$ triples with $P$ constructed via
`atan2`-interpolation between the directions of $R,Q$ from $V$ at a random interior parameter
$t\in(0.05,0.95)$ and random distance, filtered to keep only those $P$ genuinely satisfying conditions
(a),(b) by direct side-of-line tests (not by the sign-relation being verified), then checked the
conclusion — 0 failures.

**Application (imo-2026-02).** Used in `synthetic-angle-chase-aklastar.md` (round 5) at vertex $B$
(with $V=B,R=A,Q=L,P=K$, translating "K lies inside angle LBA") and at vertex $C$ (with
$V=C,R=A,Q=K,P=L$, translating "L lies inside angle ACK"), pinning the signs of
$\mathrm{cross}(L-B,K-B)$ and $\mathrm{cross}(L-C,K-C)$, which — combined with two new applications of
`interior-point-side-test.md` at vertices $N,M$ — closes the directed-angle branch-selection gap for
hypotheses (ii),(iii) that had stalled the population since round 4.

**Status.** Proved in full, general (not specific to this problem beyond the two applications), no
gaps. Reusable for any problem needing to translate an unsigned "$X$ inside $\angle YVZ$" position
hypothesis into a directed-angle-range / cross-product-sign fact.
