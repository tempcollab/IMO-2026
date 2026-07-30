# Lemma: decoupling of angle conditions under fixed-ray parametrization

**Source approaches:** `synthetic-angle-chase-aklastar` ("Key structural fact"),
`coordinate-groebner-elimination` (§3, "New structural fact"). Certified by proof-reviewer, round 2
— reproduced independently with sympy from the raw coordinate definitions (see review notes); no
gaps.

**Setup for this problem.** $B=(0,0)$, $C=(a,0)$, $A=(p,q)$, $M,N$ midpoints of $AB,AC$. Parametrize
$K=B+T_K\cdot R(-\alpha)(A-B)$, $L=C+T_L\cdot R(\alpha)(A-C)$ for $T_K,T_L>0$, where $R(\theta)$ is
rotation by $\theta$ (this makes $\angle KBA=\angle ACL=\alpha$ automatic for any $T_K,T_L$). Define,
via the cross/dot tangent identity, the polynomials
$$e_1 := \mathrm{cross}(L{-}B,K{-}B)\,\mathrm{dot}(L{-}N,C{-}N) - \mathrm{cross}(L{-}N,C{-}N)\,\mathrm{dot}(L{-}B,K{-}B),$$
$$e_2 := \mathrm{cross}(L{-}C,K{-}C)\,\mathrm{dot}(B{-}M,K{-}M) - \mathrm{cross}(B{-}M,K{-}M)\,\mathrm{dot}(L{-}C,K{-}C).$$

**Statement.** $e_1$ is exactly linear-homogeneous in $T_K$ (i.e. $e_1=T_K\cdot A_1$ with $A_1$ a
polynomial in $T_L,\cos\alpha,\sin\alpha,p,q,a$ not involving $T_K$ at all), and $e_2$ is exactly
linear-homogeneous in $T_L$ (i.e. $e_2=T_L\cdot B_1$ with $B_1$ not involving $T_L$). Consequently,
for $T_K,T_L>0$, the two angle conditions $e_1=0,e_2=0$ are equivalent to $A_1(T_L,\ldots)=0$ (a
condition on $T_L$ alone, given $\alpha$) and $B_1(T_K,\ldots)=0$ (a condition on $T_K$ alone) —
each in fact a **quadratic** in its single free variable. The two conditions do not couple $T_K,T_L$
to each other.

**Proof.** $K-B=T_K\cdot\hat K$ where $\hat K:=R(-\alpha)(A-B)$ is independent of $T_K$; every
occurrence of $K$ in $e_1$ is through the vector $K-B$ (in $\mathrm{cross}(L-B,K-B)$ and
$\mathrm{dot}(L-B,K-B)$), each of which is linear in $K-B=T_K\hat K$, hence linear in $T_K$; the rest
of $e_1$ (the $N,C$-dependent factors) is independent of $T_K$. So $e_1$ is linear-homogeneous in
$T_K$, i.e. divisible by $T_K$ with quotient $A_1$ free of $T_K$. Symmetrically for $e_2,T_L$ using
$L-C=T_L\cdot R(\alpha)(A-C)$. Since $T_K,T_L>0$ are nonzero, $e_1=0\iff A_1=0$ and $e_2=0\iff B_1=0$.
(That $A_1$ is degree exactly 2 in $T_L$, not merely $\le 2$, and likewise for $B_1$ in $T_K$, is
confirmed by direct expansion; the leading coefficients are displayed in the parent approach files.)
$\blacksquare$

**Caveat (not part of the certified statement):** whether the resulting leading coefficients (called
$Z$ / $D_1$ in the parent approaches) are provably nonzero on the geometrically valid locus is a
**separate, still-open question** — this lemma only certifies the decoupling/factorization structure,
not any nonvanishing claim about $Z$/$D_1$.
