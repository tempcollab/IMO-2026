To determine for which values of $\theta$ Mulan can guarantee a win, let's analyze the game mathematically. 

Let the angles of the current triangle $\mathcal{T}$ be $A, B, C$, with $A+B+C = 180^\circ$. 
When Mulan chooses a point $P$ on the perimeter and cuts to the opposite vertex, say $A$, the point $P$ lies on the side $BC$. This cut splits the angle $A$ into two smaller angles, $x$ and $A-x$, where $0 < x < A$. 
The two resulting triangles have the following angle sets:
1. Triangle 1: $B, x, 180^\circ - B - x = A+C-x$
2. Triangle 2: $C, A-x, 180^\circ - C - (A-x) = B+x$

We can see that Shan-Yu's choice is equivalent to choosing between the two states:
- **Child 1:** $\{B, x, C+A-x\}$ (where $A$ is replaced by $x$, transferring $A-x$ to $C$)
- **Child 2:** $\{C, A-x, B+x\}$ (where $A$ is replaced by $A-x$, transferring $x$ to $B$)

### Part 1: Mulan wins if $\theta$ divides $180^\circ$
Assume $\theta \mid 180^\circ$, so $180^\circ = n\theta$ for some integer $n \ge 2$.
First, observe that if any angle of the triangle is exactly $k\theta$ for some integer $k \ge 1$, Mulan can force a win. If $k=1$, she has already won. If $k \ge 2$, she cuts that angle with $x = \theta$. Child 1 will contain the angle $\theta$, so if Shan-Yu chooses Child 1, Mulan wins. To avoid this, Shan-Yu must choose Child 2, which replaces $k\theta$ with $(k-1)\theta$. By repeating this process, Mulan forces the multiple down to $2\theta$. When the angle is $2\theta$, a cut with $x=\theta$ makes BOTH children have an angle of $\theta$, so Mulan wins regardless of Shan-Yu's choice.

Now, suppose the current triangle has no angle that is a multiple of $\theta$. We can write $A = a + k_A\theta$, $B = b + k_B\theta$, and $C = c + k_C\theta$, where $a, b, c \in (0, \theta)$ are the remainders modulo $\theta$, and $k_A, k_B, k_C \ge 0$ are integers. 
Because $A+B+C = 180^\circ = n\theta$, we have $a+b+c = K\theta$ for $K \in \{1, 2\}$.

Mulan wants to force a multiple of $\theta$ into both children. She will do this by cutting an angle $X \in \{A, B, C\}$ with a carefully chosen $x = \theta - y$, where $y$ is the remainder of the "next" angle. Specifically, she needs $0 < x < X$, which is equivalent to $X > \theta - y \implies X + y > \theta$.
Suppose for the sake of contradiction that no angle satisfies this condition. Then:
- $A \le \theta - b \implies A = a \implies k_A = 0$ and $a+b \le \theta$
- $B \le \theta - c \implies B = b \implies k_B = 0$ and $b+c \le \theta$
- $C \le \theta - a \implies C = c \implies k_C = 0$ and $c+a \le \theta$

Summing the three inequalities gives $2(a+b+c) \le 3\theta$. However, $a+b+c = K\theta \ge \theta$. This implies $2K\theta \le 3\theta \implies 2K \le 3$. Since $K \in \{1, 2\}$ and $n \ge 2$ (which implies $K$ cannot be $0$), if $K=2$ we get $4 \le 3$ (contradiction), and if $K=1$ then $k_A=k_B=k_C=0 \implies a+b+c = n\theta \implies \theta = n\theta \implies n=1$ (contradiction, since $n \ge 2$). 
Thus, there is ALWAYS at least one angle $X$ that satisfies $X > \theta - y$. 

Mulan cuts this angle $X$ with $x = \theta - y$.
- **Child 1** will have the "next" angle become $y + x = y + \theta - y = \theta$. This is a positive multiple of $\theta$.
- **Child 2** will have the "previous" angle become $Z + X - x = Z + X - (\theta - y) = (X+y+Z) - \theta = 180^\circ - \theta = (n-1)\theta$. Since $n \ge 2$, this is also a positive multiple of $\theta$.

Since both children contain an angle that is a positive multiple of $\theta$, Mulan guarantees a win in finitely many steps.

### Part 2: Shan-Yu wins if $\theta$ does not divide $180^\circ$
Assume $\theta \nmid 180^\circ$. Let $r = 180^\circ \pmod \theta$, so $r \in (0, \theta)$. 
Shan-Yu initially chooses a triangle with angles $A = r/3$, $B = r/3$, and $C = 180^\circ - 2r/3$. Notice that all angles are positive and sum to $180^\circ$, forming a valid triangle. The remainders of these angles modulo $\theta$ are $a = r/3$, $b = r/3$, and $c = r/3$, all of which are strictly non-zero.

Shan-Yu's strategy is to maintain the invariant that **no angle in the triangle is a multiple of $\theta$**. Let the current state have remainders $a, b, c \in (0, \theta)$. 
When Mulan cuts angle $A$ with parameter $x$, let $m = x \pmod \theta$.
- Child 1 has remainders $a-m$, $b+m$, and $c$. This child contains a $0$ (a multiple of $\theta$) if and only if $m \in \{a, -b\}$.
- Child 2 has remainders $m$, $b$, and $a+c-m$. This child contains a $0$ if and only if $m \in \{0, a+c\}$.

For Mulan to force Shan-Yu into a multiple of $\theta$, she needs BOTH children to contain a $0$. This requires $m$ to be in the intersection of $\{a, -b\}$ and $\{0, a+c\}$.
However, because $\theta \nmid 180^\circ$, we know $a+b+c \equiv 180^\circ \not\equiv 0 \pmod \theta$. 
Checking the intersections:
- $a = 0$ (impossible, $a \in (0, \theta)$)
- $a = a+c \implies c = 0$ (impossible)
- $-b = 0 \implies b = 0$ (impossible)
- $-b = a+c \implies a+b+c = 0 \pmod \theta$ (impossible)

The intersection is always empty! This means for any $x$ Mulan chooses, at least one child will have NO multiples of $\theta$ in its angles. Shan-Yu simply chooses that child. By induction, Shan-Yu can avoid creating any multiple of $\theta$ forever. Since $\theta$ itself is a multiple of $\theta$, Mulan can never win.

### Conclusion
Mulan can guarantee her victory if and only if $\theta$ is a divisor of $180^\circ$.

**Final Answer:**
Mulan can guarantee her victory in finitely many steps if and only if **$\theta$ divides $180^\circ$** (i.e., $\theta = \frac{180^\circ}{n}$ for some integer $n \ge 2$).