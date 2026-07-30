Here is a complete and rigorous solution to the problem.

### Part (a): Termination and Final State

Let the state of the blackboard be represented by a multiset of 2026 positive integers, denoted by $S = \{x_1, x_2, \ldots, x_{2026}\}$. 
Let $\Omega(x)$ denote the number of prime factors of $x$ counted with multiplicity, with the convention that $\Omega(1) = 0$. Note that $\Omega$ is completely additive: $\Omega(uv) = \Omega(u) + \Omega(v)$ for any positive integers $u, v$.

We define two quantities based on the state of the board:
1. $N = \sum_{i=1}^{2026} \mathbf{1}_{x_i > 1}$, the number of integers strictly greater than 1.
2. $\Sigma = \sum_{i=1}^{2026} \Omega(x_i)$, the total number of prime factors across all integers on the board.

We monitor the combined quantity $Q = \Sigma + N$. We will show that $Q$ strictly decreases with every valid move.

In one move, Confucius chooses two integers $m > 1$ and $n > 1$ from the board. Let $d = \gcd(m, n)$. We can write $m = d \cdot a$ and $n = d \cdot b$ where $a, b$ are positive integers and $\gcd(a, b) = 1$. 
The chosen numbers $m$ and $n$ are replaced by:
$$ \gcd(m, n) = d \qquad \text{and} \qquad \frac{\operatorname{lcm}(m, n)}{\gcd(m, n)} = \frac{m \cdot n / d}{d} = \frac{d a \cdot d b}{d^2} = ab $$
Let us evaluate the change in $\Sigma$. The sum of $\Omega$ for the two new numbers is:
$$ \Omega(d) + \Omega(ab) = \Omega(d) + \Omega(a) + \Omega(b) $$
The sum of $\Omega$ for the two old numbers was:
$$ \Omega(m) + \Omega(n) = \Omega(da) + \Omega(db) = 2\Omega(d) + \Omega(a) + \Omega(b) $$
Thus, the change in $\Sigma$ is exactly $\Delta \Sigma = -\Omega(d) \le 0$.

Now we evaluate the change in $N$. The two old numbers $m$ and $n$ both contribute $1$ to $N$. The new numbers $d$ and $ab$ contribute $\mathbf{1}_{d > 1} + \mathbf{1}_{ab > 1}$. 
Since $m, n > 1$, we cannot have $d = 1$ and $ab = 1$ simultaneously. (If $d = 1$, then $a = m > 1$ and $b = n > 1$, giving $ab > 1$). Thus, at least one of $d$ or $ab$ is strictly greater than 1, meaning $\mathbf{1}_{d > 1} + \mathbf{1}_{ab > 1} \ge 1$. 
The change in $N$ is:
$$ \Delta N = \mathbf{1}_{d > 1} + \mathbf{1}_{ab > 1} - 2 \le 1 - 2 = -1 $$

The total change in $Q$ is $\Delta Q = \Delta \Sigma + \Delta N = -\Omega(d) + \Delta N$.
- If $d = 1$, then $\Omega(d) = 0$, so $\Delta Q = 0 + (-1) = -1$.
- If $d > 1$, then $\Omega(d) \ge 1$, so $\Delta Q \le -1 - 1 = -2$.

In all cases, $Q$ strictly decreases by at least 1. Since $Q$ is a non-negative integer, the process must terminate after a finite number of moves.

When the process terminates, there are no valid moves left, which implies there is at most one integer $M > 1$ on the board. We must prove there is exactly one. 
Let $P = \prod_{i=1}^{2026} x_i$ be the product of all integers on the board. In a move, $m$ and $n$ are replaced by $d$ and $ab$, so the product of all numbers on the board changes by a factor of:
$$ \frac{d \cdot ab}{m \cdot n} = \frac{d \cdot ab}{da \cdot db} = \frac{1}{d} $$
Thus, $P_{\text{new}} = P_{\text{old}} / d$. Since $d$ divides $m$, and $m$ is a factor of $P_{\text{old}}$, $P_{\text{new}}$ remains a positive integer. 
Notice that $P$ decreases if and only if $d > 1$. If $P_{\text{new}} = 1$, we would need $P_{\text{old}} = d$. However, $m$ and $n$ are factors of $P_{\text{old}}$, so $P_{\text{old}} \ge m \cdot n \ge d \cdot d = d^2$. This implies $d \ge d^2$, forcing $d \le 1$. If $d = 1$, $P$ is unchanged ($P_{\text{new}} = P_{\text{old}}$). Therefore, $P$ can never decrease to 1. 
Since $P$ is initially $\ge 2^{2026} > 1$ and never becomes 1, the board can never be filled entirely with 1s. Therefore, when the process terminates, there is exactly one integer $M > 1$ on the board.

### Part (b): Independence of $M$

We will show that the prime factorization of $M$ is uniquely determined by the initial state, making $M$ independent of all choices.

Let $p$ be an arbitrary prime. For any integer $x$, let $v_p(x)$ denote the exponent of $p$ in the prime factorization of $x$ (with $v_p(1) = 0$).
Let $e_i = v_p(x_i)$ be the exponents of $p$ across the 2026 numbers on the board. We claim that the greatest common divisor of these exponents is invariant under any move.

In a move, we select $m$ and $n$, with exponents $x = v_p(m)$ and $y = v_p(n)$. The new numbers are $d = \gcd(m, n)$ and $ab = \operatorname{lcm}(m, n)/\gcd(m, n)$. 
The exponent of $p$ in $d$ is $\min(x, y)$. 
The exponent of $p$ in $ab$ is $v_p(\operatorname{lcm}(m, n)) - v_p(\gcd(m, n)) = \max(x, y) - \min(x, y) = |x - y|$.
Thus, the multiset of exponents of $p$ undergoes the replacement of $(x, y)$ by $(\min(x, y), |x - y|)$.

We use the well-known identity that for any non-negative integers $x$ and $y$:
$$ \gcd(x, y) = \gcd(\min(x, y), |x - y|) $$
Because the greatest common divisor of the replaced pair is identical to that of the original pair, the greatest common divisor of the entire multiset of exponents of $p$ across all 2026 positions remains unchanged. Let this invariant be $g_p$.

When the process terminates, exactly one integer $M > 1$ remains, and the other 2025 integers are $1$. The exponents of $p$ on the board are $E_p = v_p(M)$ and $2025$ zeros. The greatest common divisor of this final multiset is $\gcd(E_p, 0, \ldots, 0) = E_p$.
Because the GCD of the exponents is invariant, we must have $E_p = g_p$. 

This implies that the exponent of $p$ in $M$ is exactly $g_p$, the GCD of the exponents of $p$ in the initial 2026 integers. Since this holds for every prime $p$, the prime factorization of $M$ is completely and uniquely determined by the initial state. Thus, the value of $M$ is entirely independent of the choices made during the process.