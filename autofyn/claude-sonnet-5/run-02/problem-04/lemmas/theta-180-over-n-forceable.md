# Lemma: θ = 180°/n is forceable for every integer n ≥ 2

**Statement.** For every integer $n\ge2$, $\theta=180°/n \in S$: Mulan can force
$\theta$ to appear in finitely many Shan-Yu-immune moves, from any starting triangle.

**Proof.**
*Case $n=2$ ($\theta=90°$).* By the altitude-foot double hit (`double-hit-primitives.md`,
case D2), from any triangle without a $90°$ angle, one cut forces $90°$ into both
children, so Shan-Yu cannot avoid it: win in one move (or already won).

*Case $n\ge3$ ($\theta=180°/n\le60°$).*
1. **Manufacture a "big" angle and a small spectator simultaneously.** Any triangle's
   largest angle is $\ge60°\ge\theta$ (else all three angles $<60°$ and sum $<180°$).
   Call it $p_0$; if $p_0=\theta$ Mulan has already won (only possible if $\theta=60°$,
   $n=3$, equilateral start). Otherwise $p_0>\theta$. Fix any other angle $s_0\ne p_0$
   of the starting triangle. Repeatedly bisect the current descendant of $s_0$ (using
   the bisection double-hit, `double-hit-primitives.md` case D1 with $p$ = current
   value, i.e. cutting at $x_1=p/2$): $s_0\to s_0/2\to\cdots\to s_0/2^k<\theta$, for
   $k=\lceil\log_2(s_0/\theta)\rceil+1$. Each bisection targets the $s_0$-lineage, a
   vertex distinct from whichever vertex currently carries the surviving big angle, so
   by the **Persistence Lemma** below, some angle $\ge p_0>\theta$ survives every step
   regardless of Shan-Yu's choices. After $k$ bisections: a spectator $r:=s_0/2^k<\theta$
   and a big angle $P\ge p_0>\theta$ are simultaneously, immune-ly present.

   **Persistence Lemma.** If Mulan bisects an angle $s$ of a triangle whose other two
   angles are $X,Y$, then in *either* child, some present angle is $\ge\max(X,Y)$.
   *Proof.* Children are $\{Y,s/2,X+s/2\}$ and $\{X,s/2,Y+s/2\}$. If $X\ge Y$ (so
   $\max=X$): child 2 contains $X$ directly; child 1 contains $X+s/2>X$. If $Y\ge X$
   (so $\max=Y$): child 1 contains $Y$ directly; child 2 contains $Y+s/2>Y$. Either way,
   both children have an angle $\ge\max(X,Y)$. $\blacksquare$

2. **One transfer move.** Apply the transfer move (`transfer-and-shift-moves.md`) with
   $p=P>\theta$, spectator $r<\theta$: Shan-Yu is forced (else instant loss) into
   $B=\{r,\theta-r,180°-\theta\}$ exactly.

3. **$n-2$ shift moves.** Starting from $c_0:=180°-\theta$ (other two angles $r,
   \theta-r$ fixed), repeatedly apply the shift move (`transfer-and-shift-moves.md`),
   always designating $r$ as receiver: after the $i$-th shift the state is
   $\{r+i\theta,\ \theta-r,\ 180°-(i+1)\theta\}$. Each shift needs the pre-shift
   "$c$"-value $>\theta$: $180°-i\theta>\theta \iff i<n-1$, valid for $i=1,\dots,n-2$
   (using $\theta=180°/n$). After $m=n-2$ shifts, the third entry is
   $180°-(n-1)\theta=180°-180°(n-1)/n=180°/n=\theta$ exactly. (For $n=3$: $m=1$ shift.)

Every step (bisections, transfer, shifts) is Shan-Yu-immune (the discarded child is
always the one Shan-Yu is forced away from because it would otherwise contain $\theta$,
or, for pure bisections, both children contain the bisected value regardless). Hence
$\theta=180°/n$ is forced in finitely many moves from any starting triangle. $\blacksquare$

**Explicit exact-fraction witness for $n=7$ ($\theta=180°/7°$).** From equilateral
$(60°,60°,60°)$: bisect once $\to(30°,60°,90°)$ (both branches identical by symmetry);
bisect the $30°$ $\to$ either $(15°,60°,105°)$ or $(15°,75°,90°)$; transfer with
spectator $15°$ (both branches) $\to (15°,\,75/7°,\,1080/7°)$ identically; then $5$
shift moves on the $1080/7$-lineage, receiver $=15°$-lineage:
$1080/7\to900/7\to720/7\to540/7\to360/7\to180/7=\theta$ (the last step, $p=360/7=2\theta$,
is simultaneously a bisection double-hit). Final triangle
$\{1005/7°,\,75/7°,\,180/7°\}$, sum $=180°$ exactly, contains $\theta=180/7°$. Every
move and every intermediate value was hand re-verified with exact `sympy.Rational`
arithmetic by the proof-reviewer (round 2), reproducing `binary-word-invariant`'s claimed
sequence number-for-number, and independently re-confirming every cut's legality
($x_1\in(0,p)$ at each step) and that Shan-Yu was genuinely forced (never had a
$\theta$-free branch available) at every non-bisection step.

**Consequence.** This family $\{180°/n : n\ge2\}$ strictly contains
`dyadic-scaffold`'s constructive family $\{180°/((2^k+1)2^j) : k,j\ge0\}$ (every
$(2^k+1)2^j$ is an integer $\ge2$; conversely e.g. $n=7$ is not of that form, since
$2^k+1=7\Rightarrow2^k=6$ is not a power of $2$).

**Source.** `binary-word-invariant` (round 2), Sections 3–4. Certified by proof-reviewer
round 2 after full independent hand/computer re-verification of both the general
construction and the $n=7$ numeric witness.
