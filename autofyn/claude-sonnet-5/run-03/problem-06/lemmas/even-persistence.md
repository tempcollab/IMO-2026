## Lemma (Even Persistence)

**Statement.** Let $(a_n)_{n\ge1}$ be the greedy sequence of the problem ($a_1>1$ fixed, and for
$n\ge1$, $a_{n+1}$ is the smallest integer $>a_n$ with $\gcd(a_{n+1},a_i)>1$ for every
$i=1,\dots,n$). If $a_1$ is even, then $a_n$ is even for every $n\ge1$, and $a_{n+1}=a_n+2$ for
every $n\ge1$. Consequently $a_n=a_1+2(n-1)$ for all $n\ge1$, and the theorem holds for this case
with $(T,L)=(1,2)$.

**Proof.**

*Lemma A (consecutive integers are coprime).* For every positive integer $m$, $\gcd(m,m+1)=1$: any
common divisor $d$ of $m$ and $m+1$ divides $(m+1)-m=1$.

*Main induction.* Prove by strong induction on $n\ge1$ the statement $P(n)$: "$a_1,\dots,a_n$ are
all even, and $a_{n+1}=a_n+2$."

Base case $n=1$: $a_1$ is even by hypothesis. $a_2$ is the smallest integer $>a_1$ with
$\gcd(a_2,a_1)>1$. The candidate $a_1+1$ fails by Lemma A ($\gcd(a_1+1,a_1)=1$). The candidate
$a_1+2$ succeeds: it is even (since $a_1$ is even), so $2\mid\gcd(a_1+2,a_1)$. Since $a_1+1$ is the
only integer strictly between $a_1$ and $a_1+2$ and it is excluded, $a_2=a_1+2$, which is even.
$P(1)$ holds.

Inductive step: assume $P(n)$, i.e. $a_1,\dots,a_n$ even and $a_{n+1}=a_n+2$ (hence $a_{n+1}$ is
even too, since $a_n$ is even). Then $a_{n+2}$ is the smallest integer $>a_{n+1}$ with
$\gcd(a_{n+2},a_i)>1$ for all $i=1,\dots,n+1$. The candidate $a_{n+1}+1$ fails by Lemma A (taking
$i=n+1$: $\gcd(a_{n+1}+1,a_{n+1})=1$). The candidate $a_{n+1}+2$ succeeds against every
$i=1,\dots,n+1$: it is even, and every $a_i$ for $i\le n+1$ is even (by the inductive hypothesis for
$i\le n$, and shown above for $i=n+1$), so $2\mid\gcd(a_{n+1}+2,a_i)$ for all such $i$. Since
$a_{n+1}+1$ is the only integer strictly between $a_{n+1}$ and $a_{n+1}+2$ and it is excluded,
$a_{n+2}=a_{n+1}+2$. This gives $P(n+1)$.

By induction, $P(n)$ holds for every $n\ge1$: every term is even and $a_{n+1}=a_n+2$ always.
Telescoping gives $a_n=a_1+2(n-1)$ for every $n$. Taking $T=1$, $L=2$ gives $a_{n+T}=a_n+L$ for
every $n$, proving the theorem in this case (indeed a much stronger conclusion: the sequence is
exactly the arithmetic progression $a_1,a_1+2,a_1+4,\dots$ from the very first term). $\blacksquare$

**Source.** `approaches/absorption-recurrence-even-case.md` (round 4). Verified independently by
the proof-reviewer via a from-scratch simulation of the exact greedy recursion for even
$a_1\in\{2,4,6,10,12,30,100,210,210,2310\}$ over 60 terms each: in every case the gap sequence is
identically $2$, matching the closed form exactly (including the previously reported
$a_{894}=4096=2^{12}$ for $a_1=2310$, since $2310+2\cdot893=4096$).

**Scope.** This lemma fully and unconditionally settles the problem's theorem for every even
$a_1$. It supersedes, for this case, all antichain/absorption/P-Confinement machinery elsewhere in
this population (that machinery remains the operative route for odd $a_1$, which this lemma does
not address).
