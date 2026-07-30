## Lemma (Unconditional cofactor identity for myexpr)

**Setup.** $B=(0,0)$, $C=(a,0)$, $A=(p,q)$. $M=(A+B)/2$, $N=(A+C)/2$.
$$K = B + T_K\big(pc+qs,\ qc-ps\big), \qquad L = C + T_L\big((p-a)c-qs,\ qc+(p-a)s\big)$$
(free symbols $p,q,a,c,s,T_K,T_L$; $c,s$ need not satisfy $c^2+s^2=1$ for this lemma).
$$\mathrm{myexpr} := \Big(p-\tfrac a2\Big)\mathrm{cross}(K{-}A,L{-}A) + |K-A|^2(L-A)_y - |L-A|^2(K-A)_y,$$
$$e_1 := \mathrm{cross}(L{-}B,K{-}B)\mathrm{dot}(L{-}N,C{-}N) - \mathrm{cross}(L{-}N,C{-}N)\mathrm{dot}(L{-}B,K{-}B),$$
$$e_2 := \mathrm{cross}(L{-}C,K{-}C)\mathrm{dot}(B{-}M,K{-}M) - \mathrm{cross}(B{-}M,K{-}M)\mathrm{dot}(L{-}C,K{-}C).$$
Then $e_1=T_K\cdot A_1(T_L,c,s,p,q,a)$, $e_2=T_L\cdot B_1(T_K,c,s,p,q,a)$ ($A_1$ free of $T_K$, $B_1$
free of $T_L$ — elementary, since $K-B,L-C$ are linear in $T_K,T_L$ resp.). Writing
$X:=cq-ps$, $X':=cq+s(p-a)$, $Z:=aX+s(p^2+q^2)$:

**Statement.** The following is an identity of polynomials in $p,q,a,c,s,T_K,T_L$ — holding
*unconditionally*, with no use of $c^2+s^2=1$:
$$\mathrm{myexpr}\cdot Z = 2(q-T_K X)\,A_1 + 2(T_L X'-q)\,B_1.$$

**Verification.** Reproduced independently by full symbolic expansion (sympy): computed $e_1,e_2$
directly from the definitions above, divided by $T_K,T_L$ respectively to get $A_1,B_1$ (confirmed
free of $T_K,T_L$ resp.), formed $\mathrm{myexpr}$ from the Cramer's-rule circumcenter formula, and
verified $\mathrm{expand}(\mathrm{myexpr}\cdot Z - 2(q-T_KX)A_1 - 2(T_LX'-q)B_1)$ reduces to the zero
polynomial with no reduction modulo $c^2+s^2=1$ needed. (Independently re-derived by the proof-reviewer
from scratch in round 4, matching both `synthetic-angle-chase-aklastar.md`'s and
`coordinate-groebner-elimination.md`'s displayed forms up to the constant relating $Z$ and their
$D_1$/$g_1,g_2$ normalization.)

**Consequence.** If $A_1=0$ and $B_1=0$ (i.e. hypotheses (ii),(iii) hold under the given $K,L$
parametrization), then $\mathrm{myexpr}\cdot Z=0$; if additionally $Z\ne0$, then $\mathrm{myexpr}=0$.

**Scope / what this lemma does NOT establish.** This is a pure algebraic identity about the specific
symbolic expressions above — it does *not* by itself establish (a) that this $K,L$ parametrization
(with this specific rotation-sign convention, $R(-\alpha)$ for $K$ and $R(+\alpha)$ for $L$) covers
every geometric configuration satisfying the problem's position hypotheses (see
`interior-point-side-test.md` for that, proved rigorously only in `synthetic-angle-chase-aklastar.md`
as of round 4), nor (b) that $e_1=0,e_2=0$ (as opposed to a sign-flipped version) is the correct
encoding of the *unsigned* angle hypotheses (ii),(iii) — this remains open (see `current.md`).

**Status.** Proved in full as a self-contained algebraic fact, no gaps. Certified (round 4,
independently reverified by the proof-reviewer).
