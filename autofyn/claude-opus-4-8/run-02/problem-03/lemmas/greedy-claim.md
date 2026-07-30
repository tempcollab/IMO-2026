# Lemma G — Greedy-claim value of the alternating selection game

**Status:** CERTIFIED (proof-reviewer, round 1). Verified rigorous; numerically
confirmed (0 mismatches on 4000 random multisets for the value; greedy-first optimal
on 3000 tie-heavy multisets; level-measure identity 0 mismatches on 3000 multisets).
**Proved in:** `approaches/dyadic-discrepancy.md`, round 1.

## Statement

Let $A=\{b_1\ge b_2\ge\cdots\ge b_M\}$ be a finite multiset of nonnegative reals
(sorted descending). Two players alternately claim elements of $A$: the first
player (Mover) claims one element, then the second player claims one of the
remaining, and so on until $A$ is exhausted. Each element is claimed exactly
once; each player wants to maximise the sum of the elements they claim. This is a
finite, constant-sum, perfect-information game, so it has a well-defined optimal
value by backward induction.

**Claim.** Under optimal play by both players,

1. Claiming the currently-largest remaining element is an optimal move for the
   player to move, at every position; and
2. the first player's total equals the **odd-rank sum**
   $$\operatorname{odd}(A):=b_1+b_3+b_5+\cdots,$$
   and the second player's total equals the **even-rank sum**
   $\operatorname{even}(A)=b_2+b_4+\cdots$.

## Proof

Because the game is constant-sum (the two totals always add up to
$T:=\sum_i b_i$), "each player maximises their own total" is equivalent to a
strictly competitive (zero-sum) game, and backward induction on the finite game
tree yields a well-defined value regardless of how ties are broken. Let $V(A)$
denote the total secured by the player to move, under optimal play, from the
multiset $A$.

**A one-step recursion.** Suppose the Mover claims some element $b_j$. The
remaining multiset is $A\setminus\{b_j\}$, and it is now the opponent's turn to
move on it; by definition the opponent secures $V(A\setminus\{b_j\})$ and the
Mover secures the rest of $A\setminus\{b_j\}$, namely
$(T-b_j)-V(A\setminus\{b_j\})$. Hence the Mover's total when starting with $b_j$
is
$$b_j+\big[(T-b_j)-V(A\setminus\{b_j\})\big]=T-V(A\setminus\{b_j\}).$$
The Mover picks $j$ to maximise this, i.e. to minimise $V(A\setminus\{b_j\})$:
$$V(A)=T-\min_{1\le j\le M} V(A\setminus\{b_j\}).\tag{$\ast$}$$

**Induction on $M$.** We prove $V(A)=\operatorname{odd}(A)$, with $j=1$ attaining
the minimum in $(\ast)$. Base cases $M=0$ ($V=0$) and $M=1$ ($V=b_1$) are clear.

Assume the claim for all multisets of size $<M$. For each $j$,
$V(A\setminus\{b_j\})=\operatorname{odd}(A\setminus\{b_j\})$ by the inductive
hypothesis. We compute $\operatorname{odd}(A\setminus\{b_j\})$. Removing the
element at sorted position $j$ leaves positions $1,\dots,j-1$ unchanged and
shifts positions $j+1,\dots,M$ down by one rank. Therefore
$$\operatorname{odd}(A\setminus\{b_j\})=\sum_{\substack{i<j\\ i\ \mathrm{odd}}}b_i
      +\sum_{\substack{i>j\\ i\ \mathrm{even}}}b_i.$$
In particular, for $j=1$ (removing the largest), all surviving elements shift
down one rank, so the new odd ranks are the old even ranks:
$$\operatorname{odd}(A\setminus\{b_1\})=b_2+b_4+\cdots=\operatorname{even}(A)
      =T-\operatorname{odd}(A).\tag{1}$$

**Removing $b_1$ is optimal.** We show
$\Delta_j:=\operatorname{odd}(A\setminus\{b_j\})-\operatorname{odd}(A\setminus\{b_1\})\ge 0$
for every $j$. Using (1),
$$\Delta_j=\Big[\sum_{\substack{i<j\\ i\,\mathrm{odd}}}b_i
      +\sum_{\substack{i>j\\ i\,\mathrm{even}}}b_i\Big]-\sum_{i\,\mathrm{even}}b_i
      =\sum_{\substack{i<j\\ i\,\mathrm{odd}}}b_i-\sum_{\substack{i\le j\\ i\,\mathrm{even}}}b_i,$$
because $\sum_{i>j,\ \mathrm{even}}b_i-\sum_{i\,\mathrm{even}}b_i
=-\sum_{i\le j,\ \mathrm{even}}b_i$.

- If $j$ is **odd**, then
  $\Delta_j=\sum_{i<j}(-1)^{i+1}b_i=(b_1-b_2)+(b_3-b_4)+\cdots+(b_{j-2}-b_{j-1})\ge0$,
  a sum of nonnegative pairs (the list is descending).
- If $j$ is **even**, then
  $\Delta_j=\Big[\sum_{i<j}(-1)^{i+1}b_i\Big]-b_j
   =\big[(b_1-b_2)+\cdots+(b_{j-3}-b_{j-2})+b_{j-1}\big]-b_j\ge b_{j-1}-b_j\ge0$,
  since the pairs are nonnegative and $b_{j-1}\ge b_j$.

Thus $\min_j\operatorname{odd}(A\setminus\{b_j\})$ is attained at $j=1$, and by
$(\ast)$ and (1),
$$V(A)=T-\operatorname{odd}(A\setminus\{b_1\})=T-(T-\operatorname{odd}(A))
      =\operatorname{odd}(A).$$
Moreover, claiming $b_1$ realises this optimum, and every other choice $j$ gives
the Mover $T-\operatorname{odd}(A\setminus\{b_j\})\le\operatorname{odd}(A)$, so
greedy is optimal. This closes the induction. $\qquad\blacksquare$

## Corollary (discrepancy identities)

Let $S=\operatorname{odd}(A)$ be the first player's total and
$D:=S-(T-S)=2S-T$ the first player's **advantage**. Then:

- **(Pairing form)** $D=\sum_{i\ge1}(b_{2i-1}-b_{2i})+[b_M\text{ if }M\text{ odd}]\ge0$;
  in particular $S\ge T/2$.
- **(Integral form)** For threshold $x\ge0$ let $N_A(x)=\#\{i:b_i>x\}$ be the
  number of pieces longer than $x$. Then
  $$D=\lambda\big(\{x\ge0:\ N_A(x)\ \text{is odd}\}\big),$$
  where $\lambda$ is Lebesgue measure.

*Proof of the integral form.* Write each $b_i=\int_0^\infty\mathbf1[b_i>x]\,dx$.
Then $D=\sum_i(-1)^{i+1}b_i=\int_0^\infty\sum_i(-1)^{i+1}\mathbf1[b_i>x]\,dx$. For
fixed $x$, the pieces exceeding $x$ are exactly the top $N_A(x)$ in sorted order,
so $\sum_i(-1)^{i+1}\mathbf1[b_i>x]=\sum_{i=1}^{N_A(x)}(-1)^{i+1}$, which equals
$1$ if $N_A(x)$ is odd and $0$ if it is even. Integrating gives the claim. (Ties
only affect a measure-zero set of thresholds.) $\qquad\blacksquare$
