# Approach: dyadic-discrepancy (explicit strategies + discrepancy identity)

## Status
partial

## Approaches tried
- (round 7 build, GAP U — verified & hardened) **Confirmed the round-6 closure is complete and
  correct**, and hardened its single load-bearing bookkeeping step. Rather than the pin-top-2
  potential $\psi(k,\beta)$ the outliner assigned (which has an unresolved $k=4$ near-miss and needs
  a two-parameter recursion), the subset-sum/Realizability closure of §4.7 handles the strictly
  balanced sub-case (iii-b) $\ell_1<\Sigma/2$ — and *every* regime — uniformly, so I kept it. New
  this round: an explicit **Physical-Decomposition remark** in §4.7 proving $D(\text{actual final
  multiset})=D(\text{effective multiset})$ via the equal-pair residue $P=E\uplus\bigcup_s\{v_s,v_s\}$
  (one pair per op), closing the only remaining prose gap between "reachable effective total" and the
  true discrepancy the claiming phase faces. Verification (exact Fraction arithmetic): (a) subset-sum
  pigeonhole $\min_\epsilon|\sum\epsilon_i\ell_i|\le u_n$ — $0$ violations, $n\le4$; (b) ground-truth
  op-DP $\min$ reachable effective total $=\min_\epsilon|\sum\epsilon_i\ell_i|$ EXACTLY — $0$
  mismatches; (c) the constructive Realizability op-sequence reaches $|\sum\epsilon_i\ell_i|$ in
  **exactly $n$ ops** (never overrunning budget), $n\le5$; (d) the ACTUAL physical final multiset
  conserves mass $=\Sigma$ and has true $D\le u_n$ — $0$ violations, worst ratio $0.9936$. GAP U is
  fully closed for all $n$. (Overall status still partial: GAP L / lower-bound Case B, owned by the
  induction-recursion slugs, remains open.)
- (round 6 build, GAP U — CLOSED) **The entire upper bound is now proven for all $n$**,
  closing sub-case (iii-b) and in fact superseding the whole RT casework. Key discovery:
  the minimal reachable effective total equals $\min\{|\sum_i\epsilon_i\ell_i|:\epsilon\in\{-1,0,1\}^{m}\setminus\{0\}\}$
  (verified: exact match to the ground-truth DP over 4000 random instances, $0$ discrepancy).
  A **subset-sum pigeonhole** then bounds this minimum: among the $2^{m}$ subset sums of an
  $m$-piece partition ($m=n+1$) in $[0,\Sigma]$, two consecutive sorted sums differ by
  $\le\Sigma/(2^{n+1}-1)=u_n\Sigma$; their symmetric difference is a $\{-1,0,1\}$ pattern of
  value $\le u_n\Sigma$. A **Realizability Lemma** (induction: repeatedly pin an opposite-signed
  pair, bisect the zeros) shows every such pattern is reached by Xiang in $\le n$ cuts, giving
  effective total $\le u_n\Sigma$, hence $D\le u_n$. Verified: construction gives total $=|$signed
  sum$|$, uses $\le n$ ops, ratio $\le0.9994$ (tight at dyadic) over 3000 instances; pigeonhole
  gap $\le u_n$ with $0$ violations over 6000 instances ($n\le5$). This is a from-scratch proof,
  far cleaner than the pin-top-2 potential $\psi(k,\beta)$ the outline requested; the k=4 near-miss
  is resolved because the argument does **not** fix pin-top-2 as the first move — it selects the
  optimal $\{-1,0,1\}$ pattern globally. GAP U fully closed. (Overall status still partial: the
  lower bound Case B / GAP L, owned by induction-recursion, remains open.)
- (new, round 1) Direct/constructive framing built on the greedy-claim lemma and the
  discrepancy identity. No prior verdict yet.
- (round 1 build) Proved Lemma G in full (greedy-claim, both discrepancy identities,
  incl. the integral form D = measure{x : #pieces>x is odd}). Reduced the whole problem
  to a minimax discrepancy D* = u. Fully settled n=1 (both bounds, adaptive Xiang rule).
  Lower bound: Case A (top piece survives) closed; established that the ≤n cut budget is
  ESSENTIAL (unlimited cuts drive D→0), so Case B needs a genuine counting argument —
  left as an explicit gap. Upper bound (non-myopic Xiang, general n): framework only —
  the main open gap.
- (round 2 build, GAP U) NEW rigorous progress on the upper bound. (i) Proved the
  **flip-set reformulation** (Lemma F): the final odd-level set is the symmetric difference
  of Liu's odd-set with the n cut flip-sets — a clean exact tool. (ii) Proved
  **bisection-invisibility** (Cor. F2): bisecting a piece makes it parity-invisible even
  under further cuts, so bisecting ℓ₁ reduces D exactly to the discrepancy of the remaining
  pieces. (iii) Proved the **dominant-piece inductive step** (Prop. D): if ℓ₁ ≥ c(n) then
  bisect-and-recurse gives D ≤ u_n (conditional on the theorem at n−1) — this covers the
  extremal dyadic partition and reduces GAP U to the *non-dominant* case ℓ₁ < c(n).
  (iv) **Completely proved the n=2 upper bound** (D ≤ 1/7 for EVERY Liu partition), via an
  explicit ≤2-cut strategy with three exhaustive cases; verified 0 violations on 2·10⁵
  random partitions, max D = 0.14266 < 1/7 (tight). Remaining open: the general non-dominant
  inductive step (n ≥ 3).
- (round 4 build, GAP U Case (iii)) NEW rigorous progress: introduced the **Pivot Lemma**
  (§4.6) — for any multiset $\ell_1\ge\dots\ge\ell_m$ and any subset $S\subseteq\{\ell_2,\dots,\ell_m\}$
  with $\mathrm{sum}(S)\le\ell_1$, Xiang using **exactly** $m-1$ ops (bisect the others $\notin S$,
  subtract $S$ into $\ell_1$) reaches effective total $=\ell_1-\mathrm{sum}(S)$; validity and the
  op-count are proven cleanly. Using $S=$ all others, this **fully closes the sub-case
  $\ell_1\ge\Sigma/2$ of Case (iii)** (indeed the whole slab $\Sigma/2\le\ell_1<c(k)\Sigma$
  regardless of $\ell_2$): residual $=2\ell_1-\Sigma<(2c(k)-1)\Sigma=u_k\Sigma$. Verified: $0$
  violations, worst ratio $\to1$ at the boundary $\ell_1\to c(k)\Sigma$ (tight), $k\le7$. The
  remaining gap is **sharpened** to the balanced sub-case $\ell_1<\Sigma/2$ (equivalently
  $\beta:=\ell_1/\Sigma<\tfrac12$), where the pivot-into-$\ell_1$ subset-sum can leave a gap
  $>u_k\Sigma$ (numerically up to $\sim3.5\,u_k$ at $k=3$) and the true optimum uses a *different*
  pivot / pin-created intermediate coins (e.g. cancel a near-equal pair $\ell_2\approx\ell_3$ and
  delete $\ell_1$). Refuted this round: naive deterministic schedules ("merge top two",
  "pin smallest into largest") — ratios $\gg1$ for $\beta<\tfrac12$; and even reducing to a single
  piece (min $|\pm$signed sum$|$) — ratio up to $\sim19\,u_k$, since the optimum must *zero out*
  (bisect) some pieces, not $\pm$-combine all. Status remains partial; Case (iii)/$\beta<\tfrac12$ open.
- (round 3 build, GAP U) General-n cleanup and partial closure of the upper bound.
  (i) Proved the **Invisible-Pair Lemma** (any two *equal* pieces are parity-invisible ⇒
  D unchanged), which unifies and strengthens Cor. F2. (ii) Introduced the **generalized-pin**
  move (for any two pieces ℓ_i>ℓ_j: cut ℓ_i into {ℓ_j, ℓ_i−ℓ_j}, deleting the equal pair
  {ℓ_j,ℓ_j}); together with **bisect** these are exact "removal ops" that each cost ≤1 cut,
  preserve D as the discrepancy of a strictly smaller sub-multiset, and lower the running total
  by 2ℓ_j resp. ℓ_i. (iii) Reduced GAP U to the **Residual-Total Theorem (RT)**: it suffices to
  drive the residual sub-multiset's *total* ≤ u_n (since D ≤ total). (iv) Proved RT's inductive
  step for **two of the three cases for general n**: the *dominant* case ℓ₁≥c(n)Σ and the
  *balanced-top* case 2ℓ₂≥c(n)Σ both close by one removal op + IH — this subsumes Prop. D
  (dominant only) and now handles all n. (v) Isolated the sole open case — the **balanced case**
  max(ℓ₁,2ℓ₂)<c(n)Σ (all pieces small) — and proved a rigorous **obstruction**: any greedy
  "remove-max-total" / black-box single-move+IH strategy provably CANNOT close it (its
  guarantee telescopes to 2/((n+1)(n+2)) > u_n for n≥3; deterministic max-greedy numerically
  violates u_n from n=3 on). So the balanced case needs a strengthened potential/IH that
  exploits post-move sub-extremality. RT itself verified numerically (0 violations, dyadic
  tight) at n≤5. Remaining open: the balanced case (n≥3).

## Current best

**Answer:** $c(n)=\dfrac{2^n}{2^{n+1}-1}$ (so $c(1)=\tfrac23,\ c(2)=\tfrac47,\ c(3)=\tfrac8{15}$),
equivalently $c(n)=\tfrac{1+u}{2}$ with $u:=\dfrac1{2^{n+1}-1}$ the smallest dyadic piece.

Fully proven this round:

- **Lemma G** (shared, `lemmas/greedy-claim.md`): optimal alternating claiming = greedy
  take-the-largest; first player gets the odd-rank sum. Rigorous exchange/induction, ties
  handled. Certifiable.
- **Discrepancy identities.** With $D=$ Liu $-$ Xiang $=2S-1$ ($S=$ Liu's total, $\Sigma$
  pieces $=1$): (i) pairing form $D=\sum_i(b_{2i-1}-b_{2i})+[b_M\,|\,M\text{ odd}]\ge0$;
  (ii) **integral form** $D=\lambda\{x\ge0:\ N(x)\text{ odd}\}$, $N(x)=\#\{$pieces $>x\}$.
  Hence $c(n)=\tfrac{1+D^*}2$ with $D^*=\max_{\text{Liu}}\min_{\text{Xiang}}D$, and the
  target is exactly $D^*=u$.
- **n=1 completely settled** (both bounds): for Liu's single mark at $p\le\tfrac12$, Xiang's
  best response value is $D^*(p)=\min(p,\,1-2p)$, maximised at $p=\tfrac13$ giving
  $D^*=\tfrac13=u_1$, i.e. $c(1)=\tfrac23$. This exhibits Xiang's adaptive rule (bisect the
  big piece if $p\le\tfrac13$, else pin the median at $p$).
- **Lower bound, Case A:** if Xiang leaves Liu's top dyadic piece $g_n=2^nu$ uncut then
  $D\ge 2g_n-1=u$. (Because $D\ge 2b_1-1$ always, and $b_1\ge g_n$.)

**Proven this round (upper bound, GAP U — new):**
- **Flip-set reformulation (Lemma F).** For any Liu partition with odd-set $O_0$, after
  Xiang's cuts $1,\dots,n$ with flip-sets $F_1,\dots,F_n$ (each $F_j=[0,x_j)\cup[L_j-x_j,L_j)$
  for the cut piece length $L_j$), the final discrepancy is $D=\lambda(O_0\triangle F_1\triangle\cdots\triangle F_n)$.
- **Bisection-invisibility (Cor. F2).** Bisecting a piece $\ell$ ($F=[0,\ell)$) makes it
  contribute $0$ to the level-parity at every threshold, even under further cuts of the other
  pieces; hence bisecting $\ell_1$ yields $D=D(\text{remaining pieces, further cut})$.
- **Dominant-piece step (Prop. D).** If $\ell_1\ge c(n)=(1+u_n)/2$, then bisecting $\ell_1$ and
  applying the theorem at level $n-1$ to the remaining $\le n$ pieces gives $D\le u_{n-1}(1-\ell_1)\le u_n$.
- **n=2 upper bound, COMPLETE:** for every Liu partition into $\le3$ pieces, an explicit
  $\le2$-cut Xiang strategy gives $D\le u_2=\tfrac17$ (three exhaustive cases). Hence $D^*(2)=\tfrac17$
  and $c(2)=\tfrac47$ is fully proven (upper bound; lower bound is Case A + GAP L).

**Open gaps** (honest):
- **GAP L (lower bound, Case B):** when Xiang cuts the top piece $g_n$, show the resulting
  interleaved multiset still has $D\ge u$ using only the ≤n cut budget. The budget is
  provably essential (numerics: with unlimited cuts $D\to0$), so this is a real counting
  argument, not a soft estimate. (Owned by the induction-recursion approach; not attacked here.)
- **GAP U (upper bound, all $n$): CLOSED (round 6, §4.7).** For every Liu partition into $\le n+1$
  pieces, Xiang has a $\le n$-cut response with $D\le u_n$, hence $c(n)\le 2^n/(2^{n+1}-1)$. Proof:
  the minimal reachable effective total equals $\min\{|\sum\epsilon_i\ell_i|:\epsilon\in\{-1,0,1\}^m\setminus\{0\}\}$;
  a subset-sum pigeonhole on the $2^{n+1}$ subset sums gives a pattern of value $\le u_n$, and the
  Realizability Lemma reaches it in $\le n$ ops. This supersedes and completes the RT casework of
  §4.5–4.6 (which remain valid and are subsumed). No gap remains in the upper bound.

---

# Full argument (with the two gaps marked)

## 0. Reduction to a static discrepancy game

The claiming phase depends only on the multiset of final piece **lengths**, not on their
positions on the stick: relabelling positions leaves the multiset — hence every player's
achievable totals — unchanged. So the game is:

1. **Liu** chooses a partition of $1$ into $m\le n+1$ positive parts (his $\le n$ marks).
2. **Xiang**, seeing them, applies $\le n$ further cuts, each replacing one current piece by
   two positive parts summing to it (marks are distinct, but a cut may fall anywhere in the
   interior of a current piece; distinctness only forbids re-marking an existing point, a
   measure-zero restriction that never helps Xiang, who can perturb infinitesimally).
3. The pieces are claimed alternately, Liu first, both maximising own total.

By **Lemma G**, if the final pieces sorted descending are $b_1\ge\cdots\ge b_M$, Liu's total
is $S=\operatorname{odd}(A)=b_1+b_3+\cdots$. Since $\sum b_i=1$, writing $D:=S-(1-S)=2S-1$,
$$S=\frac{1+D}{2},\qquad D=\sum_{i\ge1}(b_{2i-1}-b_{2i})+[\,b_M\text{ if }M\text{ odd}\,]\ge0.$$
Liu maximises $D$, Xiang minimises it, so
$$c(n)=\frac{1+D^*}{2},\qquad D^*:=\max_{\text{Liu partition}}\ \min_{\text{Xiang }\le n\text{ cuts}}\ D.$$
Both statements of Lemma G and of the integral identity
$D=\lambda\{x\ge0:N(x)\text{ odd}\}$ (with $N(x)=\#\{i:b_i>x\}$) are proved in
`lemmas/greedy-claim.md`.

## 1. The answer and its two-sided reformulation

Set $u:=\dfrac1{2^{n+1}-1}$. Then $2\cdot 2^nu=2^{n+1}u=(2^{n+1}-1)u+u=1+u$, so
$$c(n)=\frac{2^n}{2^{n+1}-1}=2^nu=\frac{1+u}{2}.$$
Thus the target $c(n)=2^n/(2^{n+1}-1)$ is **equivalent to $D^*=u$**, i.e.

- **(Lower)** Liu has a partition forcing $D\ge u$ against every Xiang response;
- **(Upper)** for every Liu partition, Xiang has $\le n$ cuts forcing $D\le u$.

*Verification of the value at small $n$.* $n=1$: $c=2/3$, done in §3 both ways. $n=2$:
$c=4/7$; a full brute-force of the game on rational grids divisible by $7$ returns $4/7$
(independently reproduced by the outline reviewer), and §2/§4 below meet at $D^*=u_2=1/7$
on the dyadic partition $(4/7,2/7,1/7)$. Numerically, the minimax discrepancy on the dyadic
partition equals $u_n$ exactly for $n=1,2,3,4$ (ratio $D_{\min}/u=1.0000$).

## 2. Liu's construction (the dyadic partition) and the lower bound

**Construction.** Liu marks the cumulative partial sums of $u,2u,\dots,2^{n-1}u$, producing
$n+1$ pieces
$$g_k=2^k u\quad(k=0,1,\dots,n),\qquad \sum_{k=0}^n 2^k u=(2^{n+1}-1)u=1.$$
This uses exactly $n$ marks. (Marking fewer points only removes a Liu option, so it cannot
raise his guarantee; hence $n$ marks / $n{+}1$ pieces is WLOG for the lower bound.)

We must show: for the multiset obtained from $\{g_0,\dots,g_n\}$ by any $\le n$ Xiang cuts,
$D\ge u$.

**A universal inequality.** For any multiset with total $1$ and largest piece $b_1$,
$$D=b_1-\underbrace{(b_2-b_3+b_4-\cdots)}_{=\,D(A\setminus\{b_1\})\ \in[0,\,1-b_1]}\ \ge\ b_1-(1-b_1)=2b_1-1,\tag{2.1}$$
because the discrepancy of any multiset is at most its total (odd-rank sum $\le$ total).

**Case A — Xiang leaves the top piece $g_n$ uncut.** Then $g_n=2^nu$ is present, and no other
piece (original $\le 2^{n-1}u$, or a sub-piece, hence smaller) exceeds it, so $b_1=g_n$. By
(2.1), $D\ge 2\cdot 2^n u-1=u$. $\checkmark$

**Case B — Xiang cuts the top piece $g_n$ (GAP L).** Then $b_1<2^nu$, so (2.1) gives only
$D>2b_1-1$, which can be $<u$; Case A's estimate no longer suffices.

*What is established toward Case B.*
- The $\le n$ cut budget is **essential**: allowing unlimited cuts, Xiang can drive $D$
  arbitrarily close to $0$ on the dyadic partition (verified numerically, $n=1{,}\dots,4$).
  So Case B must be a genuine counting argument exploiting "$n$ cuts for $n+1$ pieces."
- Via the integral identity with threshold $t:=(2^n-1)u=1-g_n$ (the sum of all pieces below
  the top): for $x> t$ only sub-pieces of $g_n$ can exceed $x$ (every sub-piece of a lower
  original piece has length $\le 2^{n-1}u\le t$), and for $n\ge2$ at most one sub-piece of
  $g_n$ can exceed $t$ (two would sum to $>2t=(2^{n+1}-2)u>2^nu$). Hence
  $\int_t^\infty f=(p_1-t)^+$ where $p_1$ is the largest sub-piece of $g_n$, and
  $D=(p_1-t)^+ +\int_0^t f$. Case A is $p_1=g_n\Rightarrow(p_1-t)^+=u$.
- **What remains:** a lower bound on the low part $\int_0^t f$ (equivalently, controlling the
  interleaving of $g_n$'s sub-pieces with the lower group) that recovers $D\ge u$ when
  $p_1<g_n$, using that at most $n-1$ cuts are left for the lower group. The natural attempt
  (delete the top piece and apply a scaled induction hypothesis $H_{n-1}$ to the lower group,
  which is $t\cdot L_{n-1}$ with $u_n=t\,u_{n-1}$) fails because adding the top sub-pieces can
  *decrease* $D$ (adding pieces is not monotone in $D$). Closing this cleanly is GAP L. The
  "one cut short $\Rightarrow$ an odd tier survives" pigeonhole (explorer notes) is the
  intended mechanism but is not yet a proof.

## 3. The case n = 1 (both bounds, complete)

Liu marks one point; by reflecting the stick we may assume his mark is at $p\in(0,\tfrac12]$,
giving pieces $\{1-p,\ p\}$ with $1-p\ge\tfrac12\ge p$. (Liu marking $0$ points leaves one
piece which Xiang can bisect, giving Liu only $\tfrac12<\tfrac23$, so it is dominated.)

For three pieces summing to $1$, $D=1-2\cdot(\text{median})$: indeed with three sorted pieces
$b_1\ge b_2\ge b_3$, $D=b_1-b_2+b_3=(b_1+b_2+b_3)-2b_2=1-2b_2$. For two pieces $D=b_1-b_2$.
Xiang minimises $D$, i.e. **maximises the median** (or, with no cut, the two-piece gap is
already fixed). We enumerate Xiang's options.

- **No cut:** $D=(1-p)-p=1-2p$.
- **Cut the small piece $p$** into $a'\ge b'>0$: pieces $\{1-p,a',b'\}$ with $1-p$ largest;
  median $=a'<p$, so $D=1-2a'>1-2p$. Dominated by "no cut."
- **Cut the big piece $1-p$** into $a\ge b>0$ ($a+b=1-p$): pieces $\{a,b,p\}$, and Xiang wants
  the median as large as possible. Two pieces exceeding $p$ would need $2p<a+b=1-p$, i.e.
  $p<\tfrac13$; then balancing $a=b=\tfrac{1-p}{2}\ (\ge p)$ makes the median $\tfrac{1-p}2$,
  and this is the largest possible median (the second-largest of three positive reals with
  one fixed at $p$ and the other two summing to $1-p$ is maximised by balancing), giving
  $D=1-(1-p)=p$. If $p\ge\tfrac13$, no two pieces can exceed $p$, so the median is $\le p$ and
  $=p$ is attained (take $a\ge p\ge b$), giving $D=1-2p$.

Hence Xiang's best-response value is
$$D^*(p)=\min\big(p,\ 1-2p\big)=\begin{cases}p,&p\le\tfrac13,\\ 1-2p,&\tfrac13\le p\le\tfrac12.\end{cases}$$
This is increasing then decreasing, maximised at $p=\tfrac13$ with $D^*(\tfrac13)=\tfrac13=u_1$.
Therefore $D^*=\tfrac13$ and $c(1)=\tfrac{1+1/3}2=\tfrac23$, attained by Liu's mark at
$\tfrac13$ (the dyadic partition $\{\tfrac13,\tfrac23\}$), and no Liu mark does better. $\blacksquare$
(This is the $n=1$ instance of the whole claim, both bounds, and it displays the adaptive
Xiang rule: **bisect** the big piece when $p\le\tfrac13$, else **pin the median at $p$**.)

## 4. Xiang's strategy and the upper bound (GAP U)

Throughout, $u_n:=1/(2^{n+1}-1)$ and $c(n):=(1+u_n)/2=2^nu_n$. We record two dead rules
first (do NOT retry): "bisect the $n$ largest pieces" (refuted, Liu reaches $3/4$); myopic
"reduce $D$ most per single cut" (refuted, Liu $0.65>4/7$ at $n=2$); and "cut only the top
piece with the whole budget" as a UNIVERSAL rule (refuted on near-balanced Liu). Xiang's
optimum is non-myopic and regime-dependent. We now build the correct tool and close $n\le2$
completely, and reduce the general case to a single named sub-problem.

### 4.1 The flip-set reformulation (Lemma F)

**Notation.** For a multiset of positive lengths, let $N(t)=\#\{\text{pieces}>t\}$ and
$O:=\{t\ge0:N(t)\text{ odd}\}$; by the integral identity (Lemma G) $D=\lambda(O)$. For a
single cut of a piece of length $L$ into parts $x,\,L-x$ ($0<x\le L-x$), the **flip-set** is
$$F(L,x):=[0,x)\cup[L-x,\,L),\qquad\lambda\big(F(L,x)\big)=2x=2\min(x,L-x).$$

**Lemma F (symmetric-difference form).** Let Liu's partition have odd-set $O_0$. Suppose Xiang
performs cuts $1,2,\dots,k$, where cut $j$ splits a *currently present* piece of length $L_j$
into $x_j,\,L_j-x_j$, with flip-set $F_j:=F(L_j,x_j)$. Then the final discrepancy is
$$D=\lambda\big(O_0\,\triangle\,F_1\,\triangle\,\cdots\,\triangle\,F_k\big),$$
where $\triangle$ is symmetric difference.

*Proof.* Fix a threshold $t\ge0$ and track the parity of $N(t)$ as the cuts are applied. By
the certified **Cut-Flip Lemma** (`lemmas/cut-flip.md`), replacing one part of length $L$ by
$x,L-x$ changes $N(t)$ by the increment $\delta(t)=\mathbf1[t<x]+\mathbf1[t<L-x]-\mathbf1[t<L]$,
which is odd exactly for $t\in F(L,x)$ and even (in fact $0$) otherwise. Increments from
distinct cuts add: after all $k$ cuts,
$$N_{\text{final}}(t)=N_0(t)+\sum_{j=1}^k\delta_j(t).$$
This identity holds regardless of the order of the cuts and regardless of whether cut $j$ acts
on an original piece or on a sub-piece created by an earlier cut — each cut simply removes one
current part and adds two, and $N(t)$ counts parts exceeding $t$ additively. Reducing mod $2$,
$$N_{\text{final}}(t)\equiv N_0(t)+\sum_{j=1}^k\mathbf1\big[t\in F_j\big]\pmod2 .$$
Hence $t$ lies in the final odd-set iff it lies in an odd number of the sets
$O_0,F_1,\dots,F_k$, i.e. iff $t\in O_0\triangle F_1\triangle\cdots\triangle F_k$. Taking
Lebesgue measure and using $D=\lambda(O_{\text{final}})$ gives the claim. $\qquad\blacksquare$

Lemma F turns Xiang's problem into a **parity-covering** problem: choose flip-sets
$F_1,\dots,F_k$ (each of the special two-interval shape $[0,x)\cup[L-x,L)$, with $L$ a length
available when the cut is made) to make $\lambda(O_0\triangle F_1\triangle\cdots\triangle F_k)$
as small as possible. Sequential availability is the only coupling between the cuts.

### 4.2 Bisection makes a piece parity-invisible (Cor. F2)

**Corollary F2.** If cut $j$ *bisects* a piece, i.e. $x_j=L_j/2$, then $F_j=[0,L_j/2)\cup[L_j/2,L_j)=[0,L_j)$.
In particular, bisecting a piece of length $\ell_1$ and then applying any further cuts only to
the *other* pieces yields
$$D=\lambda\Big(\big[0,\ell_1)\ \triangle\ O_{\mathrm{rest}}\Big)\quad\text{when }O_{\mathrm{rest}}\subseteq[0,\ell_1)\ \ (\star),\qquad\text{but unconditionally}\quad D=D\big(\{\ell_2,\dots\}\text{ after those cuts}\big).$$
Precisely: let the two halves $\ell_1/2,\ell_1/2$ be present in the final multiset together with
the (possibly further-cut) other pieces $R$. The two equal halves contribute
$N_{\text{halves}}(t)=2\cdot\mathbf1[t<\ell_1/2]$, which is **even for every $t$**; hence by
Lemma F the level-parity of the whole multiset equals that of $R$ alone, so $D=\lambda(O_R)=D(R)$.

Thus *bisecting $\ell_1$ deletes it from the discrepancy*: whatever Xiang later does to the
remaining pieces, the final $D$ equals the discrepancy of those remaining pieces alone. This is
the exact, unconditional statement behind the certified "Bisection = keep a sub-multiset"
corollary, extended to allow further cuts on the retained pieces.

### 4.3 The bisect-and-recurse reduction and the dominant-piece step

We use the natural scale-invariant induction hypothesis.

> **Theorem U($n$).** For every partition of a length-$L$ segment into $\le n+1$ positive
> pieces, Xiang using $\le n$ cuts can force $D\le u_n\,L$.

By homogeneity of $D$ under scaling all lengths by a constant (both $O$ and $\lambda$ scale
linearly), it suffices to prove Theorem U($n$) for $L=1$; the general $L$ then follows by
rescaling. **U(1) is proven in §3** (there, min $D\le\tfrac13=u_1$ over any $\le2$-piece Liu
partition of total $1$; scaling gives $\le u_1 L$).

**Proposition D (dominant-piece step).** *Assume Theorem U($n-1$). Let a partition of $1$ into
$\le n+1$ pieces have largest piece $\ell_1\ge c(n)$. Then Xiang, with $\le n$ cuts, forces
$D\le u_n$.*

*Proof.* Xiang **bisects $\ell_1$** (one cut). By Corollary F2, the final $D$ equals the
discrepancy of the remaining pieces $\{\ell_2,\dots,\ell_m\}$ after whatever further cuts Xiang
makes on them. These remaining pieces form a partition of $L':=1-\ell_1$ into $m-1\le n$ pieces,
and Xiang still has $n-1$ cuts. By Theorem U($n-1$) applied to this length-$L'$ partition
(which has $\le n$ pieces $=(n-1)+1$, matching the hypothesis of U($n-1$)),
$$D\le u_{n-1}\,L'=u_{n-1}(1-\ell_1).$$
Now we use the identity $\tfrac1{u_n}=\tfrac2{u_{n-1}}+1$ (verified:
$\tfrac1{u_n}=2^{n+1}-1=2(2^n-1)+1=\tfrac2{u_{n-1}}+1$). Dividing by $\tfrac1{u_{n-1}}=2^n-1$
gives $\dfrac{u_{n-1}}{u_n}=2+u_{n-1}$, i.e. $\dfrac{u_n}{u_{n-1}}=\dfrac1{2+u_{n-1}}$, hence
$$c(n)=\frac{1+u_{n-1}}{2+u_{n-1}}=1-\frac1{2+u_{n-1}}=1-\frac{u_n}{u_{n-1}}$$
(the first equality is the value $c(n)=2^nu_n=\tfrac{1+u_{n-1}}{2+u_{n-1}}$ checked in §1).
Therefore $1-\ell_1\le 1-c(n)=\dfrac{u_n}{u_{n-1}}$, and
$D\le u_{n-1}(1-\ell_1)\le u_{n-1}\cdot\dfrac{u_n}{u_{n-1}}=u_n$. $\qquad\blacksquare$

**Consequence.** Proposition D reduces the general upper bound to the **non-dominant case**
$\ell_1<c(n)$: if Theorem U($n-1$) holds and the non-dominant case of U($n$) is settled, then
U($n$) holds. In particular Proposition D handles Liu's extremal *dyadic* partition, whose top
piece is exactly $g_n=2^nu_n=c(n)\ge c(n)$: bisecting it and recursing reproduces the dyadic
structure one level down and meets the bound with equality.

### 4.4 The upper bound for n = 2 is complete: $D\le u_2=\tfrac17$

We prove Theorem U(2) with $L=1$ unconditionally (U(1) is proven, and everything below uses
only U(1) plus explicit cuts). Liu's partition is $\ell_1\ge\ell_2\ge\ell_3\ge0$, $\sum=1$.

We repeatedly use the following instance of U(1), which is immediate from §3 (or a direct check):

> **($\ast$) Two-piece one-cut bound.** For two pieces $P\ge p>0$ of total $\sigma=P+p$, one
> Xiang cut forces $D\le\min(p,\,P-p)$. *(If $p\le P/2$, bisect $P$: the multiset $\{P/2,P/2,p\}$
> has $D=p$. If $p>P/2$, pin $p$ by cutting $P$ into $\{p,P-p\}$: the multiset $\{p,p,P-p\}$ has
> $D=P-p$. Either way $D=\min(p,P-p)$, and all created parts are $\le P$.)*

We split into three exhaustive, disjoint cases on $(\ell_1,\ell_2,\ell_3)$.

Also, the degenerate cases $m\le2$ (i.e. $\ell_3=0$) are trivial: **bisect each of the $\le2$
pieces** (using $\le2$ cuts). All pieces then occur in equal pairs, so $N(t)$ is even for every
$t$ and $D=0\le\tfrac17$. So assume $\ell_1\ge\ell_2\ge\ell_3>0$ (three pieces).

**Case D (dominant): $\ell_1\ge\tfrac47$.** This is Proposition D at $n=2$ (using the proven
U(1)). Concretely, bisect $\ell_1$; by Cor. F2, $D$ equals the discrepancy of $\{\ell_2,\ell_3\}$
after one further cut, which by ($\ast$) is $\le\min(\ell_3,\ell_2-\ell_3)$. If both
$\ell_3>\tfrac17$ and $\ell_2-\ell_3>\tfrac17$ then $\ell_2>\tfrac27$ and
$\ell_2+\ell_3>\tfrac37$; but $\ell_2+\ell_3=1-\ell_1\le\tfrac37$, a contradiction. Hence
$\min(\ell_3,\ell_2-\ell_3)\le\tfrac17$, so $D\le\tfrac17$. $\checkmark$

**Case a (balanced top): $\ell_1<\tfrac47$ and $\ell_1\le2\ell_2$.**
If $\ell_1=\ell_2$: the two equal top pieces already cancel ($D_0=\ell_3$), and **bisecting
$\ell_3$** flips $[0,\ell_3)=O_0$, giving $D=0\le\tfrac17$.
If $\ell_1>\ell_2$: Xiang **pins a copy of $\ell_2$** — cut $\ell_1$ into $\{\ell_2,\ \ell_1-\ell_2\}$
(both parts positive). Set $q:=\ell_1-\ell_2$; the multiset is $\{\ell_2,\ell_2,q,\ell_3\}$. Since
$\ell_1\le2\ell_2$ we have $q=\ell_1-\ell_2\le\ell_2$, and $\ell_3\le\ell_2$; so the two $\ell_2$'s
are the two **largest** parts. Now Xiang applies ($\ast$) to the pair $\{q,\ell_3\}$ (one more
cut), which produces only parts $\le\max(q,\ell_3)\le\ell_2$. In the final multiset the two
$\ell_2$'s occupy ranks $1,2$ and cancel ($b_1-b_2=0$), so $D$ equals the discrepancy of the
sub-multiset produced from $\{q,\ell_3\}$; by ($\ast$),
$$D\le\min(p,\,P-p),\qquad p:=\min(q,\ell_3),\ \ P:=\max(q,\ell_3).$$
We claim $\min(p,P-p)\le\tfrac17$. Suppose not: $p>\tfrac17$ and $P-p>\tfrac17$, so
$P=p+(P-p)>\tfrac27$ and $p+P>\tfrac37$. But $p+P=q+\ell_3=(\ell_1-\ell_2)+\ell_3
=\ell_1+\ell_3-\ell_2=(1-\ell_2)-2\ell_2+... $; compute directly: $q+\ell_3=\ell_1-\ell_2+\ell_3$
and $\ell_2+\ell_3=1-\ell_1$ give $\ell_3=1-\ell_1-\ell_2$, so
$q+\ell_3=(\ell_1-\ell_2)+(1-\ell_1-\ell_2)=1-2\ell_2$. Also $P\le\ell_2$ (both $q,\ell_3\le\ell_2$),
so $P>\tfrac27$ forces $\ell_2>\tfrac27$, whence $q+\ell_3=1-2\ell_2<1-\tfrac47=\tfrac37$ —
contradicting $q+\ell_3=p+P>\tfrac37$. Hence $D\le\min(p,P-p)\le\tfrac17$. $\checkmark$

**Case b (dominant-ish top, sub-threshold): $\ell_1<\tfrac47$ and $\ell_1>2\ell_2$.**
Then $\ell_2<\ell_1/2<\tfrac27$. Xiang **bisects $\ell_1$**; by Cor. F2, $D$ equals the
discrepancy of $\{\ell_2,\ell_3\}$ after one further cut, which by ($\ast$) is
$\le\min(\ell_3,\ell_2-\ell_3)$. Since $\ell_3+(\ell_2-\ell_3)=\ell_2$, the smaller of the two
is $\le\ell_2/2<\tfrac17$. Hence $D<\tfrac17$. $\checkmark$

The three cases are exhaustive and disjoint: either $\ell_1\ge\tfrac47$ (D), or $\ell_1<\tfrac47$
with $\ell_1\le2\ell_2$ (a), or $\ell_1<\tfrac47$ with $\ell_1>2\ell_2$ (b). In every case
$D\le u_2=\tfrac17$. Combined with the lower bound (Case A of §2 gives $D\ge\tfrac17$ on the
dyadic partition $(\tfrac47,\tfrac27,\tfrac17)$ when the top piece is left uncut; and the
brute-force check reproduces $D^*(2)=\tfrac17$), we obtain $c(2)=\tfrac{1+1/7}2=\tfrac47$.
*(Numerical validation of the explicit strategy above: $0$ violations over $2\times10^5$ random
$3$-piece partitions, with maximal achieved $D=0.14266<\tfrac17=0.142857$, i.e. the bound is
tight.)* $\qquad\blacksquare$

### 4.5 General $n$: the Invisible-Pair Lemma, removal ops, and the Residual-Total Theorem

We now give the clean general-$n$ machinery that turns GAP U into a single named combinatorial
theorem, prove two of its three cases for all $n$, and isolate the one open case with a rigorous
proof that greedy methods cannot close it.

**Invisible-Pair Lemma (IP).** *For any finite multiset $R$ of positive lengths and any value
$v>0$, adjoining two equal copies leaves the discrepancy unchanged: $D(R\cup\{v,v\})=D(R)$.*

*Proof.* For every threshold $t\ge0$, $N_{R\cup\{v,v\}}(t)=N_R(t)+2\cdot\mathbf1[t<v]$. The added
term is even for **every** $t$, so $N_{R\cup\{v,v\}}(t)\equiv N_R(t)\pmod2$ for all $t$; the two
multisets have identical odd-sets $O$, hence $D=\lambda(O)$ is identical (integral identity,
`lemmas/greedy-claim.md`). $\qquad\blacksquare$

IP subsumes and strengthens Cor. F2: bisecting a piece $\ell$ replaces it by the equal pair
$\{\ell/2,\ell/2\}$, which by IP is invisible, so bisecting $\ell$ is exactly *deleting* $\ell$
from the discrepancy — and this holds no matter what further cuts are applied elsewhere, because
IP is a statement about the *final* multiset.

**Two removal ops.** Let the current multiset (Liu's pieces, possibly already partly cut) be
$\ell_1\ge\ell_2\ge\cdots\ge\ell_m>0$. Xiang may apply, at the cost of **one cut** each:

- **(B) Bisect $\ell_i$:** cut $\ell_i$ into $\{\ell_i/2,\ell_i/2\}$. By IP this deletes $\ell_i$;
  the effective multiset becomes $\{\ell_1,\dots,\ell_m\}\setminus\{\ell_i\}$, running total drops
  by $\ell_i$.
- **(P) Generalized pin $\ell_j$ into $\ell_i$** (any $i,j$ with $\ell_i>\ell_j$): cut $\ell_i$
  into $\{\ell_j,\ \ell_i-\ell_j\}$ (both parts positive). Now two copies of $\ell_j$ are present
  (the original and the new one); by IP they are invisible, so the effective multiset becomes
  $\{\ell_1,\dots,\ell_m\}\setminus\{\ell_i,\ell_j\}\ \cup\ \{\ell_i-\ell_j\}$, running total drops
  by $2\ell_j$.

In addition, whenever the current effective multiset already contains two equal pieces, IP lets
Xiang **delete that pair for free** (0 cuts). Each of B, P reduces the piece count by exactly $1$;
a free deletion reduces it by $2$. Crucially, **every removal op preserves the identity
"final $D$ = discrepancy of the current effective multiset"** — this is exactly IP applied to the
deleted equal pair, and it is unaffected by later cuts to the surviving pieces. (Marks are
distinct, but all created cut points are interior to existing pieces and can be perturbed
infinitesimally without changing lengths, so distinctness never obstructs a removal op.)

Since $D(\text{any multiset})\le b_1\le(\text{its total})$ (pairing form: $D=\sum_i(b_{2i-1}
-b_{2i})+[\text{leftover}]\le b_1$), we obtain the key reduction:

> **Residual-Total Theorem (RT).** *If, from a partition of total $\Sigma$ into $\le n+1$ pieces,
> Xiang can (using $\le n$ removal ops) reach an effective multiset of total $\le u_n\Sigma$, then
> the final discrepancy satisfies $D\le u_n\Sigma$.* Taking $\Sigma=1$, RT $\Rightarrow$ the upper
> bound $D\le u_n$.

So it suffices to prove the purely combinatorial claim:

> **Claim RT($k$).** For every multiset of $\le k+1$ positive reals of total $\Sigma$, Xiang using
> $\le k$ removal ops (B, P, free-pair) can reach effective total $\le u_k\Sigma$.

We prove RT($k$) by strong induction on $k$ **except for one case**, which we leave as the honest
open gap. Set $c(k):=1-u_k/u_{k-1}=2^k/(2^{k+1}-1)$ (identity verified in §4.3 and checked
symbolically; $u_0=1$).

**Base RT($0$).** One piece, $0$ ops: effective total $=\Sigma=u_0\Sigma$ since $u_0=1$. $\checkmark$

**Trivial reduction ($m\le k$).** If the multiset has $m\le k$ pieces, bisect all $m$ of them
($m\le k$ ops): every piece is deleted, effective total $=0\le u_k\Sigma$. $\checkmark$ Hence the
only nontrivial case of RT($k$) is $m=k+1$ pieces, which we assume henceforth.

**Inductive step, Case (i) — dominant: $\ell_1\ge c(k)\Sigma$.** Bisect $\ell_1$ (op B, one cut).
The effective multiset has $\le k$ pieces and total $\Sigma-\ell_1\le(1-c(k))\Sigma
=(u_k/u_{k-1})\Sigma$; apply RT($k-1$) with the remaining $k-1$ ops to reach total
$\le u_{k-1}\cdot(u_k/u_{k-1})\Sigma=u_k\Sigma$. $\checkmark$

**Inductive step, Case (ii) — balanced top: $\ell_1<c(k)\Sigma$ and $2\ell_2\ge c(k)\Sigma$.**
If $\ell_1>\ell_2$, pin $\ell_2$ into $\ell_1$ (op P, one cut): effective multiset
$\{\ell_1-\ell_2,\ell_3,\dots,\ell_{k+1}\}$ has $\le k$ pieces and total $\Sigma-2\ell_2\le
(1-c(k))\Sigma=(u_k/u_{k-1})\Sigma$; apply RT($k-1$): total $\le u_k\Sigma$. $\checkmark$
If instead $\ell_1=\ell_2$, delete this equal pair for free ($0$ cuts): effective multiset has
$\le k-1$ pieces and total $\Sigma-2\ell_1=\Sigma-2\ell_2\le(u_k/u_{k-1})\Sigma$; with all $k$ ops
still available, apply RT($k-1$): total $\le u_{k-1}(u_k/u_{k-1})\Sigma=u_k\Sigma$. $\checkmark$

Cases (i) and (ii) are exactly the union $\max(\ell_1,2\ell_2)\ge c(k)\Sigma$, and both close for
**every** $n$ by a single removal op plus the induction hypothesis. (Case (i) is precisely
Prop. D of §4.3, now seen as one half of a two-case reduction; Case (ii) is new this round and
handles the "balanced-top" regime that Prop. D missed.)

**Case (iii), balanced: $\max(\ell_1,2\ell_2)<c(k)\Sigma$.** Here every piece is $<c(k)\Sigma$ and
$\ell_2,\dots,\ell_{k+1}<c(k)\Sigma/2$; no single removal op deletes a $c(k)$-fraction of the total.
Round 4 splits this case cleanly with the **Pivot Lemma** and closes the sub-case $\ell_1\ge\Sigma/2$
outright; the sole remaining gap becomes the strictly-balanced sub-case $\ell_1<\Sigma/2$.

### 4.6 The Pivot Lemma and the closure of Case (iii) for $\ell_1\ge\Sigma/2$

**Pivot Lemma.** *Let a current multiset be $\ell_1\ge\ell_2\ge\dots\ge\ell_m>0$ (the pivot is the
largest, $\ell_1$). Let $S\subseteq\{\ell_2,\dots,\ell_m\}$ be any subset with $\mathrm{sum}(S)\le\ell_1$.
Then Xiang, using **exactly $m-1$ removal ops**, can reach an effective multiset whose total is
$$\ell_1-\mathrm{sum}(S)\ \ (\ge0).$$*

*Proof.* Xiang performs two blocks of ops.
(1) **Bisect** every piece of $\{\ell_2,\dots,\ell_m\}\setminus S$ (that is $m-1-|S|$ pieces). By the
Invisible-Pair Lemma each bisected piece is deleted from the effective multiset; this uses $m-1-|S|$
ops and leaves the effective multiset $\{\ell_1\}\cup S$.
(2) **Subtract** the pieces of $S$ into the pivot, one at a time, in *decreasing* order
$s_1\ge s_2\ge\dots\ge s_r$ ($r=|S|$): at step $i$ the current pivot value is
$R_i:=\ell_1-(s_1+\dots+s_{i-1})$, and Xiang applies the generalized pin of $s_i$ into the pivot
(cut the pivot $R_i$ into $\{s_i,\,R_i-s_i\}$, whose equal pair $\{s_i,s_i\}$ is deleted by IP,
leaving $R_i-s_i=R_{i+1}$). This is a legal pin provided $R_i\ge s_i$; and indeed
$$R_i-s_i=\ell_1-(s_1+\dots+s_i)\ \ge\ \ell_1-\mathrm{sum}(S)\ \ge\ 0,$$
since $s_1+\dots+s_i\le\mathrm{sum}(S)\le\ell_1$. If $R_i=s_i$ (so $R_{i+1}=0$) the two equal parts are
deleted for free instead. Block (2) uses $r=|S|$ ops. The final effective total is
$R_{r+1}=\ell_1-\mathrm{sum}(S)$. Total ops $=(m-1-|S|)+|S|=m-1$. $\qquad\blacksquare$

Applied to the RT setting ($m=k+1$, budget $k=m-1$), the Pivot Lemma exactly exhausts the budget and
gives Xiang the residual $\ell_1-\mathrm{sum}(S)$ for **any** admissible subset $S$. Optimising over
$S$: the best pivot-into-$\ell_1$ residual is
$$\rho^{\mathrm{piv}}:=\ell_1-\max\Big\{\mathrm{sum}(S):\ S\subseteq\{\ell_2,\dots,\ell_{k+1}\},\ \mathrm{sum}(S)\le\ell_1\Big\}\ \ge0 .$$

**Closure of Case (iii) when $\ell_1\ge\Sigma/2$ (sub-case (iii-a)).** Here $\mathrm{sum}(\{\ell_2,\dots,\ell_{k+1}\})=\Sigma-\ell_1\le\ell_1$,
so $S=\{\ell_2,\dots,\ell_{k+1}\}$ (all of them) is admissible in the Pivot Lemma. The residual is
$$\rho^{\mathrm{piv}}=\ell_1-(\Sigma-\ell_1)=2\ell_1-\Sigma .$$
Since (Case (iii)) $\ell_1<c(k)\Sigma$, and $2c(k)-1=\dfrac{2\cdot2^k-(2^{k+1}-1)}{2^{k+1}-1}=\dfrac1{2^{k+1}-1}=u_k$,
$$\rho^{\mathrm{piv}}=2\ell_1-\Sigma<(2c(k)-1)\Sigma=u_k\Sigma .$$
Hence by RT, $D\le\rho^{\mathrm{piv}}<u_k\Sigma$. $\checkmark$ (This closes the whole slab
$\Sigma/2\le\ell_1<c(k)\Sigma$ regardless of $\ell_2$; the residual is tight, $\to u_k\Sigma$ as
$\ell_1\to c(k)\Sigma$, matching the dyadic boundary. Verified: $0$ violations over $\ge2\times10^4$
random instances per $k$, $k\le7$, worst ratio $\to1^-$.)

Thus Cases (i), (ii) and (iii-a) together settle **every** configuration with $\ell_1\ge\Sigma/2$ or
$\max(\ell_1,2\ell_2)\ge c(k)\Sigma$. Combining with the certified Cases (i),(ii): the ONLY remaining
region is the *strictly balanced* sub-case.

> **[SUPERSEDED — closed in §4.7.]** The sub-case below was the sole open gap after round 4; it is
> now *fully resolved* by the Realizability Lemma + Subset-Sum Pigeonhole of §4.7, which closes the
> entire upper bound for all $n$ without the pin-top-2 potential. The obstruction discussion here is
> retained only to document why the earlier fixed-schedule routes failed (and why §4.7 avoids them).
>
> **GAP U (sharpened to sub-case (iii-b)).** Assume RT($k-1$). Prove RT($k$) for $m=k+1$ pieces with
> $$\ell_1<\tfrac12\Sigma\quad\text{and}\quad \ell_2<\tfrac12 c(k)\Sigma:$$
> Xiang with $\le k$ ops reaches effective total $\le u_k\Sigma$.

*Why (iii-b) is genuinely harder (proved obstructions).* When $\ell_1<\Sigma/2$ the "others"
$\ell_2,\dots,\ell_{k+1}$ have total $\Sigma-\ell_1>\ell_1$, so the pivot-into-$\ell_1$ subset-sum
$\rho^{\mathrm{piv}}$ need not be small: on coarse instances it exceeds $u_k\Sigma$ (e.g. $k=3$,
$(\ell_i)=(0.492,0.253,0.252,0.003)$ gives $\rho^{\mathrm{piv}}=0.492-0.256=0.236\approx3.5\,u_3$).
On such instances the *true* optimum uses a different structure — it deletes the pivot $\ell_1$ and
cancels a near-equal pair (bisect $\ell_1$, bisect $\ell_4$, pin $\ell_2$ into $\ell_3$: residual
$\ell_2-\ell_3=0.001$). So closing (iii-b) requires either (α) an *adaptive pivot* rule (choose the
pivot after possibly deleting $\ell_1$, and allow pin-created intermediate "coins" $\ell_i-\ell_j$
as additional subset-sum denominations), or (β) the strengthened balanced-recursion potential. Both
are the open research step; I do **not** claim either. Numerically (solver `/tmp/round-4/rt_search.py`,
exhaustive over all op-sequences) RT($k$) holds in (iii-b) with substantial slack — worst residual
$\approx0.83\,u_3$, $0.72\,u_4$ (Finding 2) — so the sub-case is strictly sub-extremal, but the slack
shrinks to $0$ only as $\ell_1\uparrow\Sigma/2$ (the (iii-a)/(iii-b) interface), so any sufficient
bound must still be sharp there.

*Status of GAP U — proved facts.*
- **Numerically true and tight.** A full search over all B/P/free-pair sequences confirms the
  minimal reachable effective total is $\le u_k$ for all tested partitions ($n\le5$, $\ge2\times
  10^5$ random partitions, $0$ violations), with the maximum attained exactly at Liu's dyadic
  partition (which sits on the boundary $\ell_1=c(n)\Sigma$ of Case (i)). So Case (iii) is
  strictly *sub-extremal* — its true residual is $<u_k\Sigma$ — but proving this requires more
  than the black-box induction.
- **Greedy provably fails (obstruction).** The natural "remove the largest total each step"
  strategy — always apply the op deleting $\max(\ell_1,2\ell_2)$ — does **not** suffice for
  $k\ge3$. Indeed, after any such op the new maximum piece is $\le\tfrac12\max(\ell_1,2\ell_2)$
  (bisect is used only when $\ell_1\ge2\ell_2$, giving new max $\le\ell_2\le\ell_1/2$; pin gives
  new max $\le\ell_2=\tfrac12(2\ell_2)$), and with $\le k{+}1{-}j$ pieces after $j$ ops the total
  obeys $r_j\le(k{+}1{-}j)\cdot\tfrac12(r_{j-1}-r_j)$, i.e. $r_j\le\frac{k+1-j}{k+3-j}r_{j-1}$.
  Telescoping, $r_k\le r_0\prod_{j=1}^k\frac{k+1-j}{k+3-j}=\frac{2}{(k+1)(k+2)}$, which **exceeds**
  $u_k=1/(2^{k+1}-1)$ for $k\ge3$ (e.g. $k=3$: $\tfrac1{10}>\tfrac1{15}$). Moreover the *actual*
  deterministic max-greedy strategy numerically violates $u_k$ from $k=3$ on (worst residual
  $0.074>1/15$ at $k=3$). Hence any proof of Case (iii) must be **non-greedy**: it must exploit
  that the effective multiset *after* a balanced move is itself balanced (all pieces small
  relative to its own total), so that RT($k-1$) applied there gives strictly less than the
  black-box bound $u_{k-1}\cdot(\text{new total})$. Concretely, the required strengthening is a
  potential/IH of the form "residual $\le\psi(k,\beta)\Sigma$ where $\beta=\ell_1/\Sigma$ is the
  top-piece fraction, with $\psi(k,c(k))=u_k$ and $\psi$ solving the balanced recursion"; deriving
  and verifying such $\psi$ is the open work. I do **not** claim it.

The $n=2$ instance of Case (iii) *is* fully proven — it is Cases a,b of §4.4, closed by the
three-piece bookkeeping ("$q+\ell_3=1-2\ell_2$ vs $P\le\ell_2$"). The obstruction above explains
why that bookkeeping does not lift verbatim to $n\ge3$: it implicitly used the strengthened bound
available in the balanced regime, which the general $\psi$ must capture.

### 4.7 The complete upper bound via subset-sum pigeonhole (closes GAP U for ALL $n$)

*(Round 6.)* The RT machinery of §4.5–4.6 reduces the upper bound to reaching a small **effective
total** by removal ops, and closes every regime except the strictly-balanced (iii-b). We now give
a **from-scratch closure of the entire upper bound**, valid for all $n$, that supersedes the
regime split: it needs neither the pin-top-2 potential nor the Pivot-Lemma subset restricted to a
single pivot. The engine is a characterization of the reachable effective totals as **all
$\{-1,0,+1\}$-signed sums**, closed by a subset-sum pigeonhole. Throughout, "removal op" = bisect
/ generalized pin / free-pair delete of §4.5, each a legal Xiang move costing $\le1$ cut, and by
the Invisible-Pair Lemma each preserves the identity *(final $D$) $=$ (discrepancy of the current
effective multiset)*; also $D(\text{multiset})\le(\text{its total})$ (pairing form, §4.5). So it
suffices to reach, from Liu's $m\le n+1$ pieces of total $\Sigma$ using $\le n$ removal ops, an
effective multiset of **total $\le u_n\Sigma$** ($u_n=1/(2^{n+1}-1)$). By homogeneity take
$\Sigma=1$; the general $\Sigma$ follows by rescaling all lengths.

If $m\le n$: bisect all $m$ pieces (op B, $m\le n$ ops); every piece is deleted, effective total
$=0\le u_n$. So assume $m=n+1$ pieces $\ell_1,\dots,\ell_{n+1}>0$, $\sum_i\ell_i=1$, budget $n$.

**Realizability Lemma (signed sums are reachable).** *Let $\epsilon\in\{-1,0,+1\}^{m}$ be not
identically $0$. Then Xiang, using $\le m-1$ removal ops, can reach an effective multiset whose
total equals $\bigl|\sum_{i=1}^{m}\epsilon_i\ell_i\bigr|$.*

*Proof.* First **bisect** every piece $\ell_i$ with $\epsilon_i=0$ (op B); by the Invisible-Pair
Lemma these are deleted from the effective multiset. This costs $|Z|$ ops, where $Z=\{i:\epsilon_i=0\}$,
and leaves the sub-multiset $T:=\{\ell_i:\epsilon_i\ne0\}$ carrying signs $\epsilon_i\in\{\pm1\}$.
Replacing $\epsilon$ by $-\epsilon$ if necessary (this does not change $|\sum\epsilon_i\ell_i|$), we
may assume the **signed total** $V:=\sum_{i:\epsilon_i\ne0}\epsilon_i\ell_i\ge0$. We prove, by
induction on $r:=|T|\ge1$, that $T$ (with its $\pm1$ labels) can be reduced by $\le r-1$ removal ops
to an effective multiset of total exactly $V$, *preserving the labelled signed sum $=V$ at every
step.*

- $r=1$: the single piece has label $+1$ (else $V<0$), so its value is $V$; $0$ ops. $\checkmark$
- $r\ge2$: If all labels are $+1$, then $V=\sum_{i\in T}\ell_i$ equals the total of the current
  (untouched) effective multiset; stop, using $0$ further ops. Otherwise both a $+1$ and a $-1$
  label occur (they cannot all be $-1$, as that forces $V<0$). Pick **any** piece $a$ with label
  $\sigma$ and any piece $b$ with label $-\sigma$, chosen so that $a\ge b$ (relabel the pair so the
  larger is $a$). Apply the op:
  - if $a>b$: **generalized pin** $b$ into $a$ (cut $a$ into $\{b,a-b\}$, delete the equal pair
    $\{b,b\}$), replacing $a,b$ by a single piece of value $a-b>0$ carrying label $\sigma$;
  - if $a=b$: **free-delete** the pair $\{a,b\}$ ($0$ ops), removing both.

  In either case the labelled signed sum is unchanged: the removed contribution $\sigma a+(-\sigma)b
  =\sigma(a-b)$ equals the contribution $\sigma\cdot(a-b)$ of the replacement piece (and $0$ in the
  free-delete case, matching $a=b$). One removal op (or none) has reduced $|T|$ by $1$ (or $2$),
  the signed sum still equals $V\ge0$, and all piece values stay positive. By induction the rest
  costs $\le(r-1)-1$ ops, so the total for $T$ is $\le r-1$ ops. $\checkmark$

Total ops $=|Z|+(\le r-1)=|Z|+r-1=m-1$ (since $|Z|+r=m$). The final effective total is $V=|\sum\epsilon_i\ell_i|$. $\blacksquare$

*(Every pin is legal: we always cut the strictly larger of the chosen opposite-signed pair, so the
part $a-b$ is positive; ties $a=b$ are handled by the free-delete branch, so the strict-cut
requirement is never violated. The "marks distinct" caveat is immaterial: all cut points are
interior and perturbable by §0/§4.5.)*

**Physical-decomposition remark (why $D$ of the *actual* final multiset equals the effective total's
discrepancy).** The Realizability construction is a sequence of legal Xiang cuts; the *actual*
(physical) final multiset $P$ is what the pieces-claiming phase then acts on, and we must certify
$D(P)$, not merely the total of a bookkeeping "effective multiset." We claim
$$P \;=\; E \;\uplus\; \big(Q_1\uplus\dots\uplus Q_t\big),\qquad\text{each }Q_s=\{v_s,v_s\}\text{ an equal pair},$$
where $E$ is the effective multiset produced by the induction (final total $=V=|\sum\epsilon_i\ell_i|$)
and each op contributes exactly one equal pair $Q_s$ to the physical residue: a **bisect** of $\ell$
leaves the two physical halves $\{\ell/2,\ell/2\}$; a **generalized pin** of $b$ into $a$ (cut $a$
into $\{b,\,a-b\}$) leaves the original piece $b$ and the freshly-cut copy $b$ as the pair
$\{b,b\}$, retaining only $a-b$ in $E$; a **free-delete** of $\{a,a\}$ leaves that pair. (Mass is
conserved: $\sum P=\sum_i\ell_i=\Sigma$, and $\sum E=V$, so $\sum_s\lambda(Q_s)=\Sigma-V$.) Applying
the Invisible-Pair Lemma once per pair $Q_s$ — each is a pair of *equal* values, hence invisible to
the level-parity at every threshold *irrespective of the other pieces* — strips all $t$ pairs
without changing the odd-set, giving $D(P)=D(E)$. Since $D(E)\le(\text{total of }E)=V$ (pairing
form), we conclude $D(P)\le V$. This is the exact, unconditional link from the reachable effective
total to the discrepancy of the position the claiming phase actually faces. *(End-to-end verified:
over $200$ random partitions per $n\le4$, the actual physical final multiset conserves mass $=\Sigma$
and has true discrepancy $D(P)\le u_n$ with $0$ violations, worst ratio $0.9936$, using exactly $n$
ops — no budget overrun.)*

**Subset-Sum Pigeonhole.** *For $m=n+1$ positive reals $\ell_1,\dots,\ell_m$ with $\sum\ell_i=1$
there is a pattern $\epsilon\in\{-1,0,+1\}^{m}$, not identically $0$, with
$\bigl|\sum_i\epsilon_i\ell_i\bigr|\le u_n=\dfrac1{2^{n+1}-1}.$*

*Proof.* For each of the $2^{m}=2^{n+1}$ subsets $A\subseteq\{1,\dots,m\}$ form the subset sum
$s_A:=\sum_{i\in A}\ell_i\in[0,1]$. Sort these $2^{n+1}$ real numbers as
$0=s_{(0)}\le s_{(1)}\le\dots\le s_{(2^{n+1}-1)}=1$ (the extremes are the empty and full subsets).
Their $2^{n+1}-1$ consecutive gaps are nonnegative and sum to $s_{(2^{n+1}-1)}-s_{(0)}=1$, so the
**smallest gap is $\le\dfrac1{2^{n+1}-1}=u_n$** (a minimum of $N$ nonnegative reals summing to $1$
is $\le1/N$). Let $s_A\le s_B$ realize a smallest gap, so $0\le s_B-s_A\le u_n$; the subsets are
distinct ($A\ne B$, since equal indices give the same term, and consecutive sorted values come from
distinct subsets — if two subsets share the value they are still distinct sets, giving gap $0$).
Set $\epsilon_i:=\mathbf1[i\in B]-\mathbf1[i\in A]\in\{-1,0,+1\}$. Indices in $A\cap B$ cancel, so
$\sum_i\epsilon_i\ell_i=s_B-s_A\in[0,u_n]$, and $\epsilon\not\equiv0$ because $A\ne B$. $\blacksquare$

**Upper bound, Theorem U($n$), complete.** Given Liu's partition ($m=n+1$ pieces, total $1$),
choose $\epsilon$ by the Subset-Sum Pigeonhole and realize it by the Realizability Lemma in
$\le m-1=n$ removal ops. The effective total is $|\sum\epsilon_i\ell_i|\le u_n$, hence
$$D=D(\text{effective multiset})\le(\text{effective total})\le u_n .$$
The $\le n$ removal ops correspond to $\le n$ real cuts (bisect $=1$ cut, generalized pin $=1$ cut,
free-delete $=0$ cuts; §4.5), so this is a legal $\le n$-cut Xiang response. Scaling by $\Sigma$
gives the length-$\Sigma$ statement. Therefore for **every** Liu partition into $\le n+1$ pieces
Xiang forces $D\le u_n$, i.e. $D^*\le u_n$ and $c(n)\le 2^n/(2^{n+1}-1)$. $\qquad\blacksquare$

*Sharpness / consistency.* On Liu's dyadic partition $\ell_i=2^iu_n$ ($i=0,\dots,n$) every
$\{-1,0,+1\}$ combination is $u_n\sum_i\epsilon_i2^i$, an integer multiple of $u_n$; the only way
$\sum_i\epsilon_i2^i=0$ with $\epsilon\in\{-1,0,1\}$ is $\epsilon\equiv0$ (uniqueness of the
base-$2$ representation with digits in $\{-1,0,1\}$ up to the leading term — indeed
$|\sum_{i}\epsilon_i2^i|\ge 2^{j}-\sum_{i<j}2^i=1$ where $j$ is the top nonzero index), so the
minimal nonzero value is exactly $u_n$. Thus the pigeonhole bound is **attained with equality**
on the extremal partition, matching the lower-bound construction of §2 and confirming the constant
$u_n$ is sharp. *(Numerics: over $6000$ random partitions with $n\le5$, the minimal consecutive
subset-sum gap never exceeds $u_n$, worst ratio $0.99975$, attained near dyadic; the realizability
construction reaches total $=|$signed sum$|$ in $\le n$ ops with worst ratio $0.9994$; and the
minimal reachable total from the ground-truth op-DP equals $\min_\epsilon|\sum\epsilon_i\ell_i|$
exactly on all $4000$ tested instances — validating both the characterization and the bound.)*

**Why this resolves the k=4 near-miss and the (iii-b) obstruction.** The obstruction recorded in
§4.6 and by the round-6 gates is that *fixing* the first move to "pin-top-2" (merge $\ell_1,\ell_2$)
overshoots on part of (iii-b) — e.g. the instance $[0.483,0.168,0.151,0.117,0.081]$ at $k=4$ gives
ratio $1.039$ after pin-top-2, even with optimal recursion. The pigeonhole argument does **not**
commit to any fixed first move: it selects the globally optimal $\{-1,0,+1\}$ pattern. On that same
instance the pigeonhole/realizability pattern reaches effective total $\approx0.017=0.53\,u_4$
(the true optimum), because the optimal pattern there is *not* $\ell_1-\ell_2-\cdots$ but a
different sign assignment (e.g. deleting $\ell_1$ or pinning a small piece into it). So the
strictly-balanced regime — and every regime — is handled uniformly, and no secondary threshold,
pin-top-3 escape branch, or two-parameter potential $\psi(k,\beta)$ is needed. GAP U is closed.

## Summary

Rigorously complete: the reduction (§0), Lemma G and both discrepancy identities
(`lemmas/greedy-claim.md`), the answer and its reformulation $D^*=u$ (§1), the full $n=1$
solution both bounds (§3), the lower-bound Case A (§2), the flip-set reformulation (Lemma F,
§4.1), bisection-invisibility (Cor. F2, §4.2), and the **complete upper bound for $n=2$** (§4.4).
**New this round (§4.5):** the **Invisible-Pair Lemma** (IP) and the two exact **removal ops**
(bisect / generalized pin), the **Residual-Total Theorem** (RT) reducing GAP U to a clean
combinatorial claim, and the **general-$n$ inductive step for Cases (i) dominant and (ii)
balanced-top** (both close for all $n$ via one op + IH, subsuming Prop. D). **New this round (§4.6):** the **Pivot Lemma** (residual $\ell_1-\mathrm{sum}(S)$ in exactly $m-1$
ops) and, via it, the complete closure of Case (iii-a) $\Sigma/2\le\ell_1<c(n)\Sigma$ (residual
$2\ell_1-\Sigma<u_n\Sigma$) for every $n$. GAP U is thereby reduced to the *single* strictly-balanced
sub-case (iii-b) $\ell_1<\tfrac12\Sigma$. We prove two rigorous **obstructions** ruling out the easy
routes: (1) greedy / black-box single-move induction telescopes to $2/((n+1)(n+2))>u_n$ for $n\ge3$
(§4.5); (2) the pivot-into-$\ell_1$ subset-sum strategy alone is insufficient in (iii-b) (§4.6), so
an adaptive pivot / pin-created intermediate coins (or the strengthened balanced potential) is
required. **New this round (§4.7): the entire upper bound is now proven for all $n$** by the
Realizability Lemma + Subset-Sum Pigeonhole, closing GAP U (including (iii-b)) and superseding the
§4.5–4.6 regime split. The remaining open piece of the *whole problem* is **GAP L only** (the lower
bound when Xiang cuts the top piece, owned by induction-recursion). Status therefore **partial**
(GAP U done, GAP L open), with the answer $c(n)=2^n/(2^{n+1}-1)$ established as the correct target,
the upper bound $c(n)\le 2^n/(2^{n+1}-1)$ **fully proven for every $n$**, and everything verified
computationally ($n\le5$: characterization exact, pigeonhole gap $\le u_n$, construction $\le n$ ops).

## Promotable lemmas

- **Lemma G (greedy-claim value)** — statement and full proof in
  `results/imo-2026-03/lemmas/greedy-claim.md`. Already certified. Reusable by every approach.
- **Discrepancy identities corollary** (pairing form and integral form
  $D=\lambda\{x:N(x)\text{ odd}\}$) — proved in the same lemma file; already certified.
- **Lemma F (flip-set / symmetric-difference reformulation), NEW, fully proven (§4.1).**
  *After Xiang's cuts with flip-sets $F_1,\dots,F_k$, $D=\lambda(O_0\triangle F_1\triangle\cdots\triangle F_k)$.*
  Rests only on the certified Cut-Flip Lemma plus additivity of the level increments. Clean,
  reusable by all approaches (turns Xiang's problem into exact parity-covering). **Recommend
  certifying.**
- **Corollary F2 (bisection-invisibility), NEW, fully proven (§4.2).** *Bisecting a piece
  contributes $0$ to level-parity at every threshold, even under further cuts of the other
  pieces; hence bisecting $\ell_1$ gives $D=D(\text{remaining pieces, further cut})$.* Drives
  the bisect-and-recurse reduction. **Recommend certifying.**
- **Proposition D (dominant-piece step), fully proven conditional on U($n-1$) (§4.3).**
  *If $\ell_1\ge c(n)$ then Xiang forces $D\le u_n$.* Reduces the general upper bound to the
  non-dominant case. Certifiable as a conditional lemma.
- **Theorem U(2) (n=2 upper bound), NEW, fully proven (§4.4).** *Every $\le3$-piece Liu
  partition admits a $\le2$-cut Xiang response with $D\le\tfrac17$.* Together with Case A this
  proves $c(2)=\tfrac47$. **Recommend certifying.**
- **Invisible-Pair Lemma (IP), NEW, fully proven (§4.5).** *For any multiset $R$ and $v>0$,
  $D(R\cup\{v,v\})=D(R)$.* One-line proof (even offset to $N(t)$ at every $t$). Unifies and
  strengthens Cor. F2; the backbone of all removal-op arguments. **Recommend certifying.**
- **Removal-op reduction + Residual-Total Theorem (RT), NEW, fully proven (§4.5).** The bisect
  and generalized-pin ops each cost $\le1$ cut, preserve "final $D$ = discrepancy of the current
  effective multiset," and lower the total by $\ell_i$ resp. $2\ell_j$; consequently
  $D\le(\text{reachable effective total})$, so forcing effective total $\le u_n$ forces $D\le u_n$.
  Reusable framing for the whole upper bound. **Recommend certifying.**
- **RT induction, Cases (i)+(ii), NEW, fully proven for all $n$ conditional on RT($n-1$) (§4.5).**
  *If $\max(\ell_1,2\ell_2)\ge c(n)\Sigma$ then one removal op + RT($n-1$) forces effective total
  $\le u_n\Sigma$.* Subsumes Prop. D (dominant) and adds the balanced-top case. Certifiable as a
  conditional lemma; leaves only the balanced case $\max(\ell_1,2\ell_2)<c(n)\Sigma$ open.
- **Pivot Lemma, NEW, fully proven (§4.6).** *For any multiset $\ell_1\ge\dots\ge\ell_m$ and any
  $S\subseteq\{\ell_2,\dots,\ell_m\}$ with $\mathrm{sum}(S)\le\ell_1$, Xiang using exactly $m-1$
  removal ops (bisect the pieces $\notin S$, subtract $S$ into $\ell_1$ in decreasing order) reaches
  effective total $=\ell_1-\mathrm{sum}(S)$.* Op-count and pin-validity ($R_i-s_i=\ell_1-\sum_{\le i}s\ge0$)
  are proven cleanly; rests only on the certified IP + generalized-pin ops. Unconditional, reusable.
  **Recommend certifying.**
- **Case (iii-a) closure, NEW, fully proven for all $n$ conditional on RT (§4.6).** *If
  $\Sigma/2\le\ell_1<c(n)\Sigma$ then the Pivot Lemma with $S=$ all others gives residual
  $=2\ell_1-\Sigma<u_n\Sigma$, hence $D<u_n\Sigma$.* Closes the entire slab and reduces GAP U to the
  strictly-balanced sub-case (iii-b) $\ell_1<\Sigma/2$. Certifiable.
- **Realizability Lemma, NEW, fully proven (§4.7).** *For any multiset $\ell_1,\dots,\ell_m$ and any
  $\epsilon\in\{-1,0,+1\}^m\setminus\{0\}$, Xiang using $\le m-1$ removal ops reaches an effective
  multiset of total exactly $|\sum_i\epsilon_i\ell_i|$.* Constructive induction (bisect the zeros;
  repeatedly pin an opposite-signed pair / free-delete equal pairs), preserving the signed sum;
  rests only on the certified Invisible-Pair + generalized-pin/bisect ops. Unconditional, reusable —
  it characterizes Xiang's reachable effective totals as exactly the $\{-1,0,1\}$-signed sums.
  **Recommend certifying.**
- **Subset-Sum Pigeonhole + complete upper bound, NEW, fully proven for all $n$ (§4.7).** *Among the
  $2^{n+1}$ subset sums of an $(n+1)$-piece partition of $\Sigma$, two consecutive sorted sums differ
  by $\le u_n\Sigma$; the resulting $\{-1,0,1\}$ pattern, realized by the Realizability Lemma in
  $\le n$ ops, gives effective total $\le u_n\Sigma$, hence $D\le u_n\Sigma$.* This proves
  $c(n)\le 2^n/(2^{n+1}-1)$ for every $n$ from scratch, sharp at the dyadic partition, and closes
  GAP U in full (superseding §4.5–4.6). **Recommend certifying as the upper-bound half of P3.**
