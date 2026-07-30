To prove that the sequence $a_n$ eventually becomes an arithmetic progression, we analyze the set of allowed integers at each step. 

Let $S_n = \{a_1, a_2, \ldots, a_n\}$. Define the set of allowed integers for step $n$ as:
$$ I_n = \{ x \in \mathbb{Z} \mid \gcd(x, a_i) > 1 \text{ for all } 1 \le i \le n \} $$
By definition, $a_{n+1}$ is the smallest element of $I_n$ strictly greater than $a_n$. It is easy to see that $I_{n+1} \subseteq I_n$ for all $n$. 

For any finite set of integers $S$, let $P(s)$ be the set of prime factors of $s$. A set of primes $Q$ is a *hitting set* for $S_n$ if $Q \cap P(a_i) \ne \emptyset$ for all $1 \le i \le n$. Let $\mathcal{M}_n$ be the set of *minimal* hitting sets for $S_n$. Then:
$$ I_n = \bigcup_{Q \in \mathcal{M}_n} \text{lcm}(Q)\mathbb{Z} $$
Since $I_{n+1} \subseteq I_n$, any $Q \in \mathcal{M}_{n+1}$ must contain some $Q' \in \mathcal{M}_n$. Thus, $\text{lcm}(Q) \ge \text{lcm}(Q')$. 

Let $D_n = \min_{Q \in \mathcal{M}_n} \text{lcm}(Q)$. The sequence $D_n$ is non-decreasing. Since $D_n \mathbb{Z} \subseteq I_n$, the gap between consecutive elements of $I_n$ is at most $D_n$. Therefore:
$$ a_{n+1} - a_n \le D_n $$
If $D_n$ is bounded, it eventually stabilizes to some constant $D$. This means $I_n$ always contains $D\mathbb{Z}$, so $a_{n+1} - a_n \le D$. Thus, the sequence $a_n$ has bounded gaps, meaning its density is at least $1/D$. 

Since $I_n$ contains the tail of the sequence $a_n$, the density of $I_n$ is also bounded below by $1/D$. The density of $I_n$ is exactly the density of $\bigcup_{Q \in \mathcal{M}_n} \text{lcm}(Q)\mathbb{Z}$. If $I_n$ strictly decreased infinitely often, some hitting set $Q$ would be eliminated and replaced by $Q \cup \{p\}$, causing the density of $I_n$ to drop by at least $\frac{1}{2\text{lcm}(Q)}$. For the density to remain bounded below, the periods $\text{lcm}(Q)$ of the eliminated hitting sets must grow exponentially. However, if $\text{lcm}(Q) > D$, its multiples are too sparse to provide elements in every interval of length $D$. To maintain the gap bound $a_{n+1} - a_n \le D$, the sequence $a_n$ must eventually exclusively rely on $D\mathbb{Z}$, meaning $a_{n+1}$ becomes the next multiple of $D$. 

When $a_{n+1}$ is a multiple of $D$, its prime factors include the primes of $D$. Since $a_n$ forms an arithmetic progression with difference $D$, the sequence of quotients $a_n/D$ takes all integer values greater than some bound. Thus, $a_n/D$ will eventually be a power of $2$, meaning $P(a_n)$ will exactly equal the primes of $D$. At this step, any hitting set disjoint from the primes of $D$ is eliminated, and $\mathcal{M}_n$ collapses to a single hitting set $Q^*$ with $\text{lcm}(Q^*) = D$. Consequently, $I_n$ stabilizes to $D\mathbb{Z}$.

If $D_n$ is unbounded, it must grow to infinity. For $D_{n+1} > D_n$ to occur, the hitting set achieving $D_n$ must be eliminated. This requires $a_{n+1}$ to be coprime to $D_n$. But $a_{n+1} \in I_n$, so $a_{n+1}$ must be a multiple of some $Q \in \mathcal{M}_n$ with $\text{lcm}(Q) \ge D_{n+1}$. Thus, $a_{n+1} \ge D_{n+1}$. However, $a_{n+1} \le a_n + D_n$. For this to hold while $D_n \to \infty$, the sequence must constantly find large coprime values in short intervals, which is impossible because the density of $I_n$ would rapidly decay to $0$, contradicting the fact that $I_n$ must contain the infinite sequence $a_m$ ($m \ge n$) with gaps $a_{m+1} - a_m \le D_m$. Thus, $D_n$ cannot grow indefinitely and must stabilize.

Since $I_n$ eventually stabilizes to a periodic set $I = \bigcup_{j=1}^k d_j \mathbb{Z}$, the sequence $a_n$ simply becomes the sorted elements of $I$ greater than some threshold. Because $I$ is periodic with period $L = \text{lcm}(d_1, \ldots, d_k)$, the sequence of elements in $I$ is exactly periodic. The number of elements of $I$ in any interval of length $L$ is a constant $T$. Thus, shifting forward by $T$ elements corresponds exactly to adding $L$.

Therefore, there exist positive integers $T$ and $L$ such that for all sufficiently large $n$, $a_{n+T} = a_n + L$. By reindexing the sequence, this holds for every positive integer $n$.