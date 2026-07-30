time 22m 37s

# IMO 2026 Problem 2: Equal Midpoint Distances from a Circumcentre

## Problem

Let $ABC$ be a triangle, and let $M$ and $N$ be the midpoints of
$AB$ and $AC$, respectively. Let $K$ and $L$ be chosen inside
triangles $BMC$ and $BNC$, respectively, such that $K$ lies inside
$\angle LBA$, $L$ lies inside $\angle ACK$, and
$$
\angle KBA=\angle ACL,\qquad
  \angle LBK=\angle LNC,\qquad
  \angle LCK=\angle BMK.
$$
If $O$ is the circumcentre of triangle $AKL$, then
$$
OM=ON.
$$

## Solution

*Proof.*
Let $\omega$ be the circumcircle of $AKL$. We shall prove that $M$
and $N$ have equal powers with respect to $\omega$. Since
$$
\operatorname{Pow}_{\omega}(X)=OX^{2}-R_{\omega}^{2}
$$
for every point $X$, equality of those powers will immediately imply
$OM=ON$.

Set
$$
x=\angle KBA=\angle ACL,\qquad
  y=\angle LBK=\angle LNC,\qquad
  z=\angle LCK=\angle BMK.
$$
Because $BK$ lies inside $\angle LBA$ and $CL$ lies inside
$\angle ACK$,
<a id="eq:angles-at-BC"></a>
$$
\angle LBA=x+y,
  \qquad
  \angle ACK=x+z.
$$

### 1. The order of the rays through $A$
We first show that the rays from $A$ occur in the order
<a id="eq:ray-order"></a>
$$
AB,\ AK,\ AL,\ AC.
$$
Indeed, write the positive barycentric coordinates of $K$ and $L$
with respect to $ABC$ as
$$
K=(a_K:b_K:c_K),
  \qquad
  L=(a_L:b_L:c_L).
$$
For an interior point $P=(a:b:c)$, the position of the ray $BP$
inside $\angle ABC$, measured from $BA$ toward $BC$, is determined
monotonically by $c/a$. Since $BK$ lies between $BA$ and $BL$,
<a id="eq:B-order"></a>
$$
\frac{c_K}{a_K}<\frac{c_L}{a_L}.
$$
Similarly, the position of $CP$ inside $\angle ACB$, measured from
$CA$ toward $CB$, is determined monotonically by $b/a$. Since
$CL$ lies between $CA$ and $CK$,
<a id="eq:C-order"></a>
$$
\frac{b_L}{a_L}<\frac{b_K}{a_K}.
$$
Consequently,
$$
\frac{c_K}{b_K}
  =\frac{c_K/a_K}{b_K/a_K}
  <\frac{c_L/a_L}{b_L/a_L}
  =\frac{c_L}{b_L}.
$$
Since the position of $AP$ inside $\angle BAC$, measured from $AB$
toward $AC$, is determined monotonically by $c/b$, this proves
[the displayed equation](#eq:ray-order).

Define
$$
p=\angle BAK,
  \qquad
  r=\angle CAL,
  \qquad
  \theta=\angle KAL.
$$
Thus
<a id="eq:A-decomposition"></a>
$$
\angle BAC=p+\theta+r.
$$
Also set
$$
\kappa=\angle AKL,
  \qquad
  \lambda=\angle ALK,
  \qquad
  S=\kappa+\lambda=\pi-\theta.
$$
Finally, write
$$
c=AB,
  \qquad
  d=AC,
  \qquad
  \rho=\frac{d}{c}.
$$

### 2. Relations forced by the two midpoint conditions
In triangle $BMK$, we have
$$
BM=\frac{c}{2},
  \qquad
  \angle MBK=x,
  \qquad
  \angle BMK=z.
$$
The sine rule therefore gives
$$
BK=\frac{c}{2}\frac{\sin z}{\sin(x+z)}.
$$
On the other hand, the sine rule in triangle $ABK$ gives
$$
BK=c\frac{\sin p}{\sin(x+p)}.
$$
Hence
<a id="eq:midpoint-M"></a>
$$
\sin(x+p)\sin z
  =2\sin p\sin(x+z).
$$
The same argument in triangles $CNL$ and $ACL$ yields
<a id="eq:midpoint-N"></a>
$$
\sin(x+r)\sin y
  =2\sin r\sin(x+y).
$$

For brevity, put
<a id="eq:abbreviations"></a>
$$
X=\sin x,
  \quad
  Y=\sin(x+y),
  \quad
  Z=\sin(x+z),
  \quad
  P=\sin(x+p),
  \quad
  Q=\sin(x+r).
$$
The remaining angles in triangles $ABL$ and $ACK$ are
<a id="eq:phi-psi"></a>
$$
\phi:=\angle ALB=S-p-x-y,
  \qquad
  \psi:=\angle AKC=S-r-x-z.
$$
The sine rule in triangles $ACL$ and $ABL$ gives
$$
AL=\frac{dX}{Q}=\frac{cY}{\sin\phi},
$$
whereas the sine rule in triangles $ABK$ and $ACK$ gives
$$
AK=\frac{cX}{P}=\frac{dZ}{\sin\psi}.
$$
Consequently,
<a id="eq:rho-two-ways"></a>
$$
\rho
  =\frac{YQ}{X\sin\phi}
  =\frac{X\sin\psi}{PZ}.
$$
Equating the two expressions in [the displayed equation](#eq:rho-two-ways), we obtain
<a id="eq:compatibility"></a>
$$
X^{2}\sin\phi\sin\psi=YPQZ.
$$

Moreover, the sine rule in triangle $AKL$ gives
$$
\frac{AK}{AL}=\frac{\sin\lambda}{\sin\kappa}.
$$
Using the expressions above for $AK$ and $AL$, we find
<a id="eq:kappa-lambda-ratio"></a>
$$
\frac{\sin\kappa}{\sin\lambda}
  =\frac{\rho P}{Q}.
$$

### 3. The powers of $M$ and $N$
We use directed lengths on secants and directed angles modulo $\pi$.
Let $T\ne K$ be the second intersection of the line $MK$ with
$\omega$, and orient that line from $M$ toward $K$. Since
$A,K,L,T$ are concyclic,
$$
\measuredangle ATM
  \equiv \measuredangle ATK
  \equiv \measuredangle ALK
  =\lambda
  \pmod{\pi}.
$$
Also, because $MA$ and $MB$ are opposite rays and
$\angle BMK=z$,
$$
\measuredangle AMT\equiv \pi-z\pmod{\pi}.
$$
Thus the directed sine rule in triangle $AMT$ gives
$$
\frac{\overline{MT}}{MA}
  =\frac{\sin(z-\lambda)}{\sin\lambda}.
$$
Furthermore, the sine rule in triangle $BMK$ gives
$$
MK=\frac{cX}{2Z}.
$$
Therefore, by the secant form of the power theorem,
<a id="eq:power-M"></a>
$$
\operatorname{Pow}_{\omega}(M)
  =\overline{MK}\,\overline{MT}
  =\frac{c^{2}X}{4Z}
   \frac{\sin(z-\lambda)}{\sin\lambda}.
$$

Likewise, if $U\ne L$ is the second intersection of the line $NL$
with $\omega$, then
<a id="eq:power-N"></a>
$$
\operatorname{Pow}_{\omega}(N)
  =\frac{d^{2}X}{4Y}
   \frac{\sin(y-\kappa)}{\sin\kappa}.
$$
Thus $\operatorname{Pow}_{\omega}(M)=\operatorname{Pow}_{\omega}(N)$ is equivalent to
<a id="eq:power-goal"></a>
$$
\frac{\sin(\lambda-z)}{Z\sin\lambda}
  =\rho^{2}
   \frac{\sin(\kappa-y)}{Y\sin\kappa}.
$$

### 4. Trigonometric reduction
Put
<a id="eq:t-definition"></a>
$$
t=\frac{\sin\kappa}{\sin\lambda}
  =\frac{\rho P}{Q},
$$
where the second equality is [the displayed equation](#eq:kappa-lambda-ratio). Since
$S=\kappa+\lambda$, the identities
$$
\sin S\,\sin(\lambda-z)
  =\sin\lambda\,\sin(S-z)-\sin\kappa\,\sin z
$$
and
$$
\sin S\,\sin(\kappa-y)
  =\sin\kappa\,\sin(S-y)-\sin\lambda\,\sin y
$$
give
<a id="eq:lambda-z-reduction"></a>
<a id="eq:kappa-y-reduction"></a>
$$
\begin{aligned}
\frac{\sin(\lambda-z)}{\sin\lambda}
  &=\frac{\sin(S-z)-t\sin z}{\sin S},\\
  \frac{\sin(\kappa-y)}{\sin\kappa}
  &=\frac{\sin(S-y)-t^{-1}\sin y}{\sin S}.
\end{aligned}
$$
Substituting [the displayed equation](#eq:t-definition)--[the displayed equation](#eq:kappa-y-reduction) into
[the displayed equation](#eq:power-goal), and then using
[the displayed equation](#eq:midpoint-M)--[the displayed equation](#eq:midpoint-N), shows that
[the displayed equation](#eq:power-goal) is equivalent to $D=0$, where
<a id="eq:D"></a>
$$
D=
  \frac{\sin(S-z)}{Z}
  -\rho^{2}\frac{\sin(S-y)}{Y}
  -2\rho\left(\frac{\sin p}{Q}-\frac{\sin r}{P}\right).
$$
Multiplying by $PZ\sin\phi$ and using
[the displayed equation](#eq:rho-two-ways), we obtain
<a id="eq:E-from-D"></a>
$$
PZ\sin\phi\,D=E(S),
$$
where
<a id="eq:E-definition"></a>
$$
E(S)=
  P\sin\phi\sin(S-z)
  -Q\sin\psi\sin(S-y)
  +\frac{2YZ}{X}\bigl(Q\sin r-P\sin p\bigr).
$$
We claim that
<a id="eq:key-identity"></a>
$$
E(S)
  =\frac{\sin(p-r)}{X^{2}}
   \left(X^{2}\sin\phi\sin\psi-YPQZ\right).
$$

To prove the claim, define
$$
F(S)=E(S)
  -\frac{\sin(p-r)}{X^{2}}
   \left(X^{2}\sin\phi\sin\psi-YPQZ\right)
$$
and put
$$
T=2S-p-r-2x-y-z.
$$
By the product-to-sum formulas, the entire $S$-dependent part of
$2F(S)$ is
<a id="eq:S-dependent-part"></a>
$$
-P\cos(T+x+r)
  +Q\cos(T+x+p)
  +\sin(p-r)\cos T.
$$
Now $P=\sin(x+p)$ and $Q=\sin(x+r)$, so
$$
\begin{aligned}
&Q\cos(T+x+p)-P\cos(T+x+r)\\
  &\quad=
  \cos T\bigl(Q\cos(x+p)-P\cos(x+r)\bigr)\\
  &\qquad
  -\sin T\bigl(Q\sin(x+p)-P\sin(x+r)\bigr)\\
  &\quad=-\sin(p-r)\cos T.
\end{aligned}
$$
This cancels the last term in [the displayed equation](#eq:S-dependent-part). Hence
$F(S)$ is independent of $S$.

We may therefore evaluate it at the convenient value
$$
S_{0}=x+y+z.
$$
Dividing [the displayed equation](#eq:midpoint-M) by $\sin p\sin z$, and
[the displayed equation](#eq:midpoint-N) by $\sin r\sin y$, respectively, gives
$$
\cot p=\cot x+2\cot z,
  \qquad
  \cot r=\cot x+2\cot y.
$$
It follows that
<a id="eq:shifted-sines"></a>
$$
\sin(z-p)=\frac{\sin p\,Z}{X},
  \qquad
  \sin(y-r)=\frac{\sin r\,Y}{X}.
$$
At $S=S_{0}$, we have $\phi=z-p$ and $\psi=y-r$. Using
[the displayed equation](#eq:shifted-sines) in [the displayed equation](#eq:E-definition), we get
<a id="eq:E-at-S0"></a>
$$
E(S_{0})
  =\frac{YZ}{X}\bigl(Q\sin r-P\sin p\bigr),
$$
while
<a id="eq:bracket-at-S0"></a>
$$
X^{2}\sin\phi\sin\psi-YPQZ
  =YZ\bigl(\sin p\sin r-PQ\bigr).
$$
Finally, the elementary identities
$$
\begin{aligned}
Q\sin r-P\sin p
  &=-\sin(x+p+r)\sin(p-r),\\
  \sin p\sin r-PQ
  &=-X\sin(x+p+r)
\end{aligned}
$$
show that
$$
X\bigl(Q\sin r-P\sin p\bigr)
  =\sin(p-r)\bigl(\sin p\sin r-PQ\bigr).
$$
Together with [the displayed equation](#eq:E-at-S0) and [the displayed equation](#eq:bracket-at-S0), this gives
$F(S_{0})=0$. Since $F$ is constant, $F(S)=0$ for all $S$, and
therefore [the displayed equation](#eq:key-identity) is proved.

Now [the displayed equation](#eq:compatibility) makes the right-hand side of
[the displayed equation](#eq:key-identity) equal to zero. Hence $E(S)=0$. By
[the displayed equation](#eq:E-from-D), and because $PZ\sin\phi\ne0$, we obtain $D=0$.
Therefore [the displayed equation](#eq:power-goal) holds, and
[the displayed equation](#eq:power-M)--[the displayed equation](#eq:power-N) give
$$
\operatorname{Pow}_{\omega}(M)=\operatorname{Pow}_{\omega}(N).
$$
Consequently,
$$
OM^{2}-R_{\omega}^{2}
  =ON^{2}-R_{\omega}^{2},
$$
so $OM=ON$, as required.
∎
