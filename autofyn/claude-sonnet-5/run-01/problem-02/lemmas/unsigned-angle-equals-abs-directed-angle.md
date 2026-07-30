# Lemma: unsigned angle equals |directed angle|

**Source approach:** `synthetic-angle-chase-aklastar` (round 5, fact (U)). Certified by proof-reviewer,
round 5 — elementary, independently re-checked, no gaps.

**Statement.** For nonzero planar vectors $X,Y$, write $\mathrm{cross}(X,Y)=|X||Y|\sin\theta$,
$\mathrm{dot}(X,Y)=|X||Y|\cos\theta$ where $\theta\in(-\pi,\pi]$ is the directed angle from $X$ to $Y$
(the value given by `atan2`). Then the standard *unsigned* angle between $X,Y$,
$$\angle(X,Y):=\arccos\!\Big(\frac{\mathrm{dot}(X,Y)}{|X||Y|}\Big)\in[0,\pi],$$
equals $|\theta|$.

**Proof.** By definition $\cos\theta=\mathrm{dot}(X,Y)/(|X||Y|)$, so $\angle(X,Y)=\arccos(\cos\theta)$.
Since $\cos$ is even, $\arccos(\cos\theta)=\arccos(\cos|\theta|)$; and since $\theta\in(-\pi,\pi]$
gives $|\theta|\in[0,\pi]$, and $\arccos$ is the inverse of $\cos$ restricted to $[0,\pi]$,
$\arccos(\cos|\theta|)=|\theta|$. Hence $\angle(X,Y)=|\theta|$. $\blacksquare$

**Application (imo-2026-02).** Used to translate the problem's literal unsigned-angle hypotheses (ii)
$\angle LBK=\angle LNC$ and (iii) $\angle LCK=\angle BMK$ into $|\theta_1|=|\theta_2|$,
$|\theta_1'|=|\theta_2'|$ for the corresponding directed angles; combined with the
`ray-betweenness-sign-lemma.md` result that all four directed angles lie strictly in $(0,\pi)$ (hence
each equals its own absolute value), this yields the exact equalities $\theta_1=\theta_2$,
$\theta_1'=\theta_2'$ with no residual sign/branch ambiguity — the key closing step of the round-5
branch-selection argument.

**Status.** Trivial but load-bearing; proved in full, general, no gaps.
