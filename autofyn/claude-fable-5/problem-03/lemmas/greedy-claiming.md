# Lemma: greedy-claiming (and the multiset/Stackelberg reduction)

*Proposed by the tie-structure-variational builder, round 1. **CERTIFIED by the proof-reviewer, round 2**: Sub-lemmas 1–2 re-derived by hand (termwise rank comparison is exact), Claims A–B induction checked, and the value odd(S) verified against a full game-tree brute force on 200 random rational multisets (with ties and zeros) in exact arithmetic. Corollary R's endpoint/zero-piece handling checked. Shared infrastructure for all approaches to imo-2026-03 — import freely.*

## Statement

**Lemma G (value of the alternating claiming game).** Let $S = \{v_1 \ge v_2 \ge \dots \ge v_m\}$ be a finite multiset of nonnegative reals. Two players alternately claim one unclaimed element each, Player 1 moving first; each player's payoff is the sum of the elements they claim, and each plays to maximise their own payoff. Then with optimal play Player 1's payoff is exactly the **odd-rank sum**
$$\mathrm{odd}(S) := v_1 + v_3 + v_5 + \cdots,$$
and Player 2's payoff is exactly the even-rank sum $\mathrm{even}(S) := v_2 + v_4 + \cdots$. (When $S$ has repeated values, "rank" refers to any fixed sorted ordering; the sums are independent of how ties are ordered.)

**Corollary R (multiset/Stackelberg reduction for imo-2026-03).** In the stick game with parameter $n$:
$$c(n) \;=\; \sup_{a} \; \inf_{x} \; \mathrm{odd}\big(S(a,x)\big),$$
where $a = (a_1 \ge \dots \ge a_k > 0)$ ranges over partitions of $1$ into $k \le n+1$ parts (Liu Bang's pieces — only the multiset of sizes matters, not their positions on the stick), $x$ ranges over Xiang Yu's legal replies — a choice of $m_j \ge 0$ cuts inside piece $j$ with $\sum_j m_j \le n$ and, for each $j$, cut positions $0 < x_{j,1} < \dots < x_{j,m_j} < a_j$ — and $S(a,x)$ is the resulting multiset of all sub-piece sizes.

## Proof of Lemma G

For a multiset $T$ write $\mathrm{odd}(T)$ for its odd-rank sum. All claims are by induction on $|T|$, using two termwise inequalities proved first.

**Sub-lemma 1.** For sorted $v_1 \ge \dots \ge v_m$ and any index $j$ with $1 \le j \le m$:
$$\mathrm{odd}(S \setminus \{v_j\}) \;\ge\; \mathrm{even}(S).$$
*Proof.* The rank-$r$ element of $S' := S\setminus\{v_j\}$ is $v_r$ if $r < j$ and $v_{r+1}$ if $r \ge j$. The number of odd ranks of $S'$ is $\lceil (m-1)/2 \rceil = \lfloor m/2 \rfloor$, which equals the number of terms of $\mathrm{even}(S)$. Compare them termwise over odd $r = 1, 3, 5, \dots$: the $r$-th odd-rank element of $S'$ is $v_r \ge v_{r+1}$ if $r < j$, and exactly $v_{r+1}$ if $r \ge j$; the corresponding term of $\mathrm{even}(S)$ is $v_{r+1}$. Summing the termwise inequalities gives the claim. $\square$

**Sub-lemma 2.** For sorted $v_1 \ge \dots \ge v_m$ ($m \ge 2$) and any $j \ge 2$:
$$\mathrm{odd}\big(\{v_2,\dots,v_m\} \setminus \{v_j\}\big) \;\ge\; \mathrm{odd}(S) - v_1 = v_3 + v_5 + \cdots.$$
*Proof.* Let $T := \{v_2,\dots,v_m\}\setminus\{v_j\}$, $|T| = m-2$. The rank-$r$ element of $T$ is $v_{r+1}$ if $r \le j-2$ and $v_{r+2}$ if $r \ge j-1$. The number of odd ranks of $T$ is $\lceil (m-2)/2 \rceil$, which equals the number of terms of $v_3 + v_5 + \cdots$ (indices $i$ odd, $3 \le i \le m$). Termwise over odd $r$: the $r$-th odd-rank element of $T$ is $v_{r+1} \ge v_{r+2}$ if $r \le j-2$, and exactly $v_{r+2}$ if $r \ge j-1$; the corresponding term of $v_3+v_5+\cdots$ is $v_{r+2}$. Summing gives the claim. $\square$

**Claim A (first-mover guarantee).** In the claiming game on any multiset $T$, the player about to move can guarantee a payoff of at least $\mathrm{odd}(T)$, by always claiming a currently-largest element.

*Proof.* Induction on $|T|$. If $|T| \le 1$ the mover takes everything: payoff $= \mathrm{odd}(T)$. Let $|T| = m \ge 2$, $T$ sorted as $v_1 \ge \dots \ge v_m$. The mover claims $v_1$ (a largest element). The opponent then claims some $v_j$, $j \ge 2$ (from $\{v_2,\dots,v_m\}$). The mover now moves first on $T' := \{v_2,\dots,v_m\}\setminus\{v_j\}$, $|T'| = m-2$, and by the induction hypothesis guarantees at least $\mathrm{odd}(T')$. By Sub-lemma 2, the mover's total is at least
$$v_1 + \mathrm{odd}(T') \;\ge\; v_1 + \big(\mathrm{odd}(T) - v_1\big) = \mathrm{odd}(T). \qquad\square$$

**Claim B (second-mover guarantee).** In the claiming game on $S$, the player moving second can guarantee at least $\mathrm{even}(S)$.

*Proof.* The first player claims some $v_j$. The second player is now first to move on $S \setminus \{v_j\}$ and, by Claim A, guarantees at least $\mathrm{odd}(S\setminus\{v_j\})$, which is $\ge \mathrm{even}(S)$ by Sub-lemma 1. $\square$

Since every element is eventually claimed, the two payoffs always sum to $\mathrm{odd}(S) + \mathrm{even}(S)$. Player 1 can guarantee $\ge \mathrm{odd}(S)$ (Claim A) and Player 2 can guarantee $\ge \mathrm{even}(S)$ (Claim B); each guarantee caps the other player at exactly the complementary amount. Hence with optimal play Player 1 gets exactly $\mathrm{odd}(S)$ and Player 2 exactly $\mathrm{even}(S)$.

Well-definedness under ties: if $v_r = v_{r'}$, exchanging their positions in the sorted order permutes equal summands, so $\mathrm{odd}(S)$ and $\mathrm{even}(S)$ do not depend on the tie-breaking. $\blacksquare$

## Proof of Corollary R

The game is sequential: Liu Bang marks $\le n$ points, Xiang Yu sees them and marks $\le n$ further points (all marked points distinct), the stick is cut at all marks, and then the claiming game of Lemma G is played on the resulting multiset of piece lengths, Liu Bang first. By Lemma G the claiming phase has exact value $\mathrm{odd}$ of the final multiset for Liu Bang, so
$$c(n) = \sup_{\text{Liu marks}} \; \inf_{\text{Xiang marks}} \; \mathrm{odd}(\text{final multiset}).$$

It remains to see that only size multisets matter.

*Liu's side.* Marking $p \le n$ interior points produces $p+1$ pieces; conversely any multiset $\{a_1,\dots,a_k\}$ of $k \le n+1$ positive reals summing to $1$ is realised by marking the $k-1 \le n$ partial sums $a_1, a_1+a_2, \dots$ (distinct interior points). So Liu's strategy space is exactly the set of partitions $a$ as stated.

*Xiang's side.* A mark of Xiang lies in the interior of exactly one Liu piece (it must differ from Liu's marks; the stick endpoints are not interior to the stick and marking an endpoint would create a length-$0$ piece — equivalently, an endpoint mark changes nothing, so we may disregard it: formally, a mark at an endpoint of the stick adds a piece of length $0$, which changes no rank of any positive piece and adds $0$ to whoever claims it, hence leaves $\mathrm{odd}$ unchanged). Placing $m_j$ distinct marks in the interior of piece $j$ at relative positions $0 < x_{j,1} < \dots < x_{j,m_j} < a_j$ splits it into sub-pieces $x_{j,1},\, x_{j,2}-x_{j,1},\, \dots,\, a_j - x_{j,m_j}$, and every such tuple is legal (the marks are automatically distinct from each other and from Liu's marks). The final multiset is $S(a,x)$ as defined, depending only on $(a, x)$ and not on the physical layout. Hence the inner infimum is exactly over the replies $x$ described. $\blacksquare$

## Remarks for importers

- **Zero-padding is harmless:** adding entries of size $0$ to a multiset changes neither $\mathrm{odd}$ nor $\mathrm{even}$ (the positive entries keep their ranks; zeros contribute $0$). Used when compactifying Xiang's reply space (a "cut with a zero sub-piece" is value-equivalent to a reply with one fewer cut).
- **Trivial bound:** $\mathrm{odd}(S) - \mathrm{even}(S) = \sum_i (v_{2i-1} - v_{2i}) + v_{\text{last if odd}} \ge 0$ termwise, so Liu Bang's value is always $\ge \tfrac12$ of the total.
