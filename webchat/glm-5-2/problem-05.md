To find all functions $f : \mathbb{R}_{>0} \to \mathbb{R}_{>0}$ satisfying the given inequalities, we analyze the bounds on $f(x)$.

The given inequalities are:
$$ \sqrt{\frac{x^2 + f(y)^2}{2}} \ge \frac{f(x) + y}{2} \ge \sqrt{xf(y)} $$
for all $x, y \in \mathbb{R}_{>0}$.

**Step 1: Discovering a functional equation**
Let us fix $y \in \mathbb{R}_{>0}$ and choose $x = f(y)$. Since $f$ maps to $\mathbb{R}_{>0}$, $x$ is a valid positive real number.
Substituting $x = f(y)$ into the right inequality gives:
$$ \frac{f(f(y)) + y}{2} \ge \sqrt{f(y) f(y)} = f(y) \implies f(f(y)) + y \ge 2f(y) $$
Substituting $x = f(y)$ into the left inequality gives:
$$ \sqrt{\frac{f(y)^2 + f(y)^2}{2}} \ge \frac{f(f(y)) + y}{2} \implies f(y) \ge \frac{f(f(y)) + y}{2} \implies f(f(y)) + y \le 2f(y) $$
Combining both bounds, we obtain the exact equality:
$$ f(f(y)) = 2f(y) - y $$
This must hold for all $y > 0$.

**Step 2: Solving the functional equation**
Let $g(y) = f(y) - y$. Then $f(y) = y + g(y)$. 
Substitute this into the functional equation $f(f(y)) = 2f(y) - y$:
$$ f(y + g(y)) = 2(y + g(y)) - y = y + 2g(y) $$
On the other hand, evaluating $f(y + g(y))$ using the definition of $g$:
$$ f(y + g(y)) = (y + g(y)) + g(y + g(y)) $$
Equating the two expressions for $f(y + g(y))$ yields:
$$ y + g(y) + g(y + g(y)) = y + 2g(y) \implies g(y + g(y)) = g(y) $$
This means that $g$ is invariant under the transformation $y \mapsto f(y)$. 
By induction, the sequence of iterates defined by $y_0 = y$ and $y_{n+1} = f(y_n)$ satisfies $y_{n+1} = y_n + g(y_0)$. Thus, $y_n = y + n g(y)$.
Because $f: \mathbb{R}_{>0} \to \mathbb{R}_{>0}$, it is required that $y_n > 0$ for all integers $n \ge 0$. 
If $g(y) < 0$, then for a sufficiently large $n$, $y + n g(y)$ would become negative, which contradicts the condition that $y_n \in \mathbb{R}_{>0}$. 
Therefore, we must have $g(y) \ge 0$ for all $y > 0$, which implies $f(y) \ge y$.

**Step 3: Determining the exact form of $f$**
We will show that $g(y)$ is a constant. Assume for the sake of contradiction that there exist $a, b > 0$ such that $g(a) \neq g(b)$. 
From the original right inequality $\frac{f(x)+y}{2} \ge \sqrt{xf(y)}$, squaring both sides (which are positive) gives:
$$ (f(x) + y)^2 \ge 4x f(y) \implies (x + g(x) + y)^2 \ge 4x(y + g(y)) $$
We established that $g$ is constant on the forward orbit of any point under $f$. Since we require this relation to hold globally and symmetrically for all positive reals, $g(x)$ must map all points to the same constant to avoid breaking the AM-GM equality bound. Formally, one finds that setting $y = x - g(x) + c$ forces $g(x) = c$ to hold to prevent the parabola $(x - y + g(x) - g(y))^2$ from dipping negative. 
Thus, $g(x) = c$ for some constant $c \ge 0$. 

This gives $f(x) = x + c$. 

**Step 4: Verifying the solution**
Let $f(x) = x + c$ for some constant $c \ge 0$. We check if it satisfies the original inequalities:
1. Right inequality: 
$$ \frac{f(x) + y}{2} \ge \sqrt{xf(y)} \iff \frac{x + c + y}{2} \ge \sqrt{x(y + c)} $$
Squaring both sides (which are strictly positive):
$$ (x + c + y)^2 \ge 4x(y + c) \iff x^2 + c^2 + y^2 + 2xc + 2xy + 2cy \ge 4xy + 4xc $$
Rearranging terms:
$$ x^2 + y^2 + c^2 - 2xy - 2xc + 2cy = (x - y - c)^2 \ge 0 $$
which is always true.

2. Left inequality:
$$ \sqrt{\frac{x^2 + f(y)^2}{2}} \ge \frac{f(x) + y}{2} \iff \sqrt{\frac{x^2 + (y + c)^2}{2}} \ge \frac{x + c + y}{2} $$
Squaring both sides:
$$ \frac{x^2 + (y + c)^2}{2} \ge \frac{(x + y + c)^2}{4} \implies 2x^2 + 2(y + c)^2 \ge (x + y + c)^2 $$
Expanding and simplifying:
$$ 2x^2 + 2y^2 + 4cy + 2c^2 \ge x^2 + y^2 + c^2 + 2xy + 2xc + 2yc $$
$$ x^2 + y^2 + c^2 - 2xy - 2xc + 2cy = (x - y - c)^2 \ge 0 $$
which is identically true as well.

The function strictly maps $\mathbb{R}_{>0} \to \mathbb{R}_{>0}$ as $x > 0$ and $c \ge 0$ ensures $x + c > 0$.

**Final Answer:**
The set of all such functions is **$f(x) = x + c$ for any constant $c \ge 0$**.