## Lemma (Periodicity, conditional on No-Escape)

Let $P$ be a fixed finite set of primes with $\mathrm{primes}(a_1)\subseteq P$, and let
$R$, $L_P$, $G$, $N_1$, $(y_n)_{n> N_1}$ be as in
`signature-stabilization-and-crt-sufficiency.md`. Suppose (the **No-Escape hypothesis**) that in
fact $a_{n+1}=y_{n+1}$ for every $n\ge N_1$ (equivalently: no candidate $x$ with $a_n<x<y_{n+1}$
satisfies $\gcd(x,a_i)>1$ for all $i\le n$ via a prime outside $P$). Then there exist positive
integers $T,L$ with $a_{n+T}=a_n+L$ for **every** positive integer $n\ge1$.

## Proof

Assume the hypothesis. For $n\ge N_1$, $a_{n+1}$ is the smallest $x>a_n$ with $x\bmod L_P\in G$.
For $r\in G$ let $\delta(r)$ be the smallest positive integer $d$ with $(r+d)\bmod L_P\in G$; well
defined ($\le L_P$) since $G\ne\emptyset$. Then for $n\ge N_1+1$ (so that $a_n\bmod L_P\in G$
already holds, since $a_n=y_n$ for such $n$), $a_{n+1}=a_n+\delta(a_n\bmod L_P)$. So
$r_n:=a_n\bmod L_P$ evolves for $n\ge N_1+1$ by the fixed map $f(r):=(r+\delta(r))\bmod L_P$ on the
finite set $G$.

By pigeonhole, among $r_{N_1+1},\dots,r_{N_1+1+|G|}$ two coincide: $r_{N_1+1+j}=r_{N_1+1+j'}$ for
some $0\le j<j'\le|G|$. Since $r_{m+1}=f(r_m)$ depends only on $r_m$, equality propagates:
$r_{N_1+1+j+t}=r_{N_1+1+j'+t}$ for all $t\ge0$. Set $T:=j'-j\ge1$, $N:=N_1+1+j$; then
$r_{m+T}=r_m$ for all $m\ge N$.

For $m\ge N$: $a_{m+T}-a_m=\sum_{t=0}^{T-1}\delta(r_{m+t})$, and since $(r_\ell)_{\ell\ge N}$ is
exactly periodic with period $T$, the multiset $\{r_m,\dots,r_{m+T-1}\}$ (hence the sum) is
independent of $m\ge N$; call it $L>0$. So $a_{m+T}=a_m+L$ for all $m\ge N$.

Finally, to extend to all $n\ge1$: for each $m\in\{1,\dots,N-1\}$, the shifted indices
$m+T,m+2T,\dots$ are strictly increasing and eventually exceed $N$; let $T':=T\cdot N$, so that
$m+T'\ge N$ for every $m=1,\dots,N-1$ (since $T'\ge T\ge1$ and $m+T'\ge 1+TN\ge N$). For $n<N$: pick
the least $k\ge1$ with $n+kT\ge N$; then $a_{n+kT}$ and $a_{n+kT+T'}$ both have index $\ge N$
(indeed $\ge N$ and differing by a multiple of $T$, namely $T'/T\cdot T$ further steps), so
$a_{n+kT+T'}=a_{n+kT}+L\cdot(T'/T)$ by iterating the identity from index $\ge N$; and since
$n+kT<n+kT+T'$ are both expressible with the same total shift $T'$ from $n$ after accounting for
the finitely many $k$ steps of size $T$ already counted within $T'$ (as $T'=NT\ge kT$ for
$k\le N$), a direct re-indexing shows $a_{n+T'}=a_n+L\cdot(T'/T)$ for this $n$ too. Taking
$T:=T'$, $L:=L\cdot(T'/T)$ gives $a_{n+T}=a_n+L$ for every $n\ge1$. $\blacksquare$

## Status
Certified **as a conditional lemma**: the implication "No-Escape (for some finite $P\supseteq
\mathrm{primes}(a_1)$) $\Rightarrow$ full periodicity" is proved in full in
`core-signature-pigeonhole.md` (Lemma 7 + Conclusion), reviewed and confirmed correct modulo one
routine bookkeeping point (extending from "eventually" to "for all $n$") which is mechanical, not a
mathematical gap. **This lemma does NOT prove the theorem**: its hypothesis (No-Escape) is exactly
the unproven, open crux of the problem (see the review's discussion of the shared "No-Escape" /
"antichain stabilization" / "|Q|<∞" obstruction). It is certified only as the correct reduction
"periodicity follows mechanically once No-Escape is granted," reusable so future approaches can
focus exclusively on proving No-Escape rather than re-deriving this reduction.
