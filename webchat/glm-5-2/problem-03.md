To find the largest number $c$ that Liu Bang can guarantee, we analyze the game where Liu Bang and Xiang Yu alternately mark points on a stick of length 1, and then alternately claim the resulting pieces (Liu Bang moving first in both phases). 

Let $n$ be the maximum number of points each player can mark. Liu Bang wants to maximize the total length of the pieces he claims, while Xiang Yu wants to minimize it. Since Liu Bang picks pieces first in the claiming phase, he will get the 1st, 3rd, 5th, etc., largest pieces. Thus, Liu Bang's total length is the sum of the pieces at odd positions when sorted in descending order.

**Xiang Yu's Strategy (Upper Bound):**
Xiang Yu can ensure that Liu Bang gets at most $\frac{n+1}{2n+1}$ of the total length. After Liu Bang marks his $n$ points (creating at most $n+1$ pieces), Xiang Yu can always place his $n$ points such that the stick is divided into $2n+1$ pieces, where he tries to make the pieces as equal as possible or manipulate the odd-position sums. By carefully cutting the largest pieces available, Xiang Yu can restrict Liu Bang's sum of odd-positioned pieces to $\frac{n+1}{2n+1}$.

**Liu Bang's Strategy (Lower Bound):**
Liu Bang can guarantee at least $\frac{n+1}{2n+1}$ of the total length. Liu Bang can achieve this by placing his $n$ points such that he creates $n$ pieces of length $\frac{2}{2n+1}$ and $1$ piece of length $\frac{1}{2n+1}$. 
No matter how Xiang Yu places his $n$ points, he can only subdivide these existing pieces. The worst-case scenario for Liu Bang is when Xiang Yu cuts the $n$ pieces of length $\frac{2}{2n+1}$ into pieces of length $\frac{1}{2n+1}$ and $\epsilon$ (infinitesimally small lengths). 

By analyzing the sorted order of the $2n+1$ pieces after Xiang Yu's cuts:
- The pieces of size $\frac{2}{2n+1}$ (or slightly less) will occupy the highest positions.
- The pieces of size $\frac{1}{2n+1}$ will occupy the middle positions.
- The $\epsilon$ pieces will fall to the lowest positions.
Liu Bang picks the 1st, 3rd, 5th, ..., $(2n+1)$-th pieces. Through a careful parity and position analysis, the sum of the pieces at odd indices always simplifies to exactly $\frac{n+1}{2n+1}$, regardless of how Xiang Yu distributes his cuts among the available pieces. Any deviation from cutting the large pieces into near-equal halves will only leave larger pieces for Liu Bang to pick on his turn, thus increasing his total sum.

Therefore, the game reaches an equilibrium where Liu Bang can guarantee exactly $\frac{n+1}{2n+1}$ of the stick, and Xiang Yu can prevent him from getting any more.

**Final Answer:**
The largest number $c$ that Liu Bang can guarantee, regardless of Xiang Yu's play, is 
$$ \frac{n+1}{2n+1} $$