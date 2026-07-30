## Status
partial

## Approach: induction-peel (framing A — strong induction on n / recursive peeling)

Target (the whole claim): for every positive integer $n$, the largest $c$ Liu Bang can
guarantee is
$$c(n)=\frac{2^n}{2^{n+1}-1}.$$
We reduce the whole game to a one–dimensional *sizing* problem (shared Lemmas R, M, P,
imported from `lemmas/`), then attack the two bounds by strong induction on $n$ organised
around the **cancelling-pair peel**.

Throughout put
$$S=2^{n+1}-1,\qquad u=u_n=\frac1S=\frac1{2^{n+1}-1},\qquad c(n)=\frac{1+u_n}{2}=\frac{2^n}{2^{n+1}-1}.$$
The last identity is elementary: $\tfrac{1+u_n}{2}=\tfrac12\cdot\tfrac{2^{n+1}-1+1}{2^{n+1}-1}=\tfrac{2^{n+1}}{2(2^{n+1}-1)}=\tfrac{2^n}{2^{n+1}-1}$.

---

### 1. Imported infrastructure (Lemmas R, M, P) — CERTIFIED

We import verbatim the three certified shared lemmas (`lemmas/reduction-odd-rank.md`,
`lemmas/measure-identity.md`, `lemmas/cancelling-pair.md`); they are used below without
re-proof.

**Lemma R (reduction).** On any fixed multiset of piece lengths $b_1\ge\cdots\ge b_m$ the
alternating claiming game (Liu first, each maximising his own total) awards Liu the odd-rank
pieces; hence with $\sum b_i=1$, writing
$$D:=\sum_{i\ge1}(-1)^{i+1}b_i=b_1-b_2+b_3-\cdots\ (\ge 0),$$
Liu's total is $\tfrac{1+D}{2}$. Consequently the whole problem is the **scalar minimax**: Liu
chooses $\le n$ cuts to maximise $D$, then Xiang chooses $\le n$ further cuts to minimise $D$;
Liu can guarantee $c(n)=\tfrac{1+u_n}{2}$ **iff** the minimax value of $D$ equals $u_n$.

**Lemma M (parity–measure identity).** For $N(t):=\#\{i:b_i>t\}$,
$$D=\int_0^\infty\mathbf 1[N(t)\text{ odd}]\,dt=\big|\{t>0:N(t)\text{ odd}\}\big|.$$

**Lemma T (toggle calculus, part of M's file).** Cutting a piece $s$ into $s_1\ge s_2$ flips
the parity of $N$ exactly on $E=[0,s_2)\cup[s_1,s)$, of measure $2s_2$; after cuts with
toggle-sets $E_1,\dots,E_r$ the final odd-set is $O_0\,\triangle\,E_1\triangle\cdots\triangle E_r$,
so $D_{\text{final}}=\mu\!\big(O_0\,\triangle\,\bigoplus_i E_i\big)$.

**Lemma P (cancelling pair).** $D(\mathcal S\cup\{v,v\})=D(\mathcal S)$ for every multiset
$\mathcal S$ and $v>0$. Hence the two atomic **peel moves**, each using exactly one cut and
reducing the piece count by exactly one, preserve the *eventual* value $D$ of the game:
- **MATCH** two current pieces $P\ge Q$: cut $P$ into $(P-Q,\,Q)$; the new $Q$ pairs with the
  old $Q$; delete the pair. Effect on the multiset: $\{P,Q\}\mapsto\{P-Q\}$; total length drops
  by $2Q$.
- **DELETE** a piece $x$ (bisect): cut $x$ into $(x/2,x/2)$ and delete the pair. Effect
  $\{x\}\mapsto\{\}$; total length drops by $x$.

Every subsequent cut is applied to the reduced multiset, so the game on the current pieces with
budget $k$ is *value-equivalent* to the game on the reduced multiset with budget $k-1$.

Everything below is stated for $D$. All statements are **scale-invariant**: on a stick of
length $L$ the value is $u_nL$.

---

### 2. The value recursion and base cases — PROVED

$$\frac1{u_n}=2^{n+1}-1=2(2^{n}-1)+1=\frac2{u_{n-1}}+1\ \Longrightarrow\
u_n=\frac{u_{n-1}}{2+u_{n-1}} .$$

**Base $n=0$.** One piece of length $L$; no cuts; $D=L=u_0L$.

**Base $n=1$ (both directions).** *Lower:* Liu plays $(\tfrac23,\tfrac13)$. Xiang's one cut: cutting
$\tfrac23$ into $s_1\ge s_2$ keeps the odd-set of measure $\tfrac13$ by Lemma T (removed top
interval and added bottom interval both length $s_2$); cutting $\tfrac13$ only raises $D$ above
$\tfrac13$. So $D\ge\tfrac13=u_1$. *Upper:* for any Liu split $(a_1,a_2)$, $a_1\ge a_2$, Xiang
MATCHes ($\{a_1,a_2\}\mapsto\{a_1-a_2\}$, $D=a_1-a_2$) or DELETEs $a_1$ (leaving $\{a_2\}$,
$D=a_2$); he takes the smaller. If both $a_2>\tfrac13$ and $a_1-a_2>\tfrac13$ then $a_1>\tfrac23$
and $a_2>\tfrac13$ force $a_1+a_2>1$, impossible; so $\min(a_2,a_1-a_2)\le\tfrac13=u_1$. Hence
minimax $D=\tfrac13$, $c(1)=\tfrac23$. $\checkmark$

---

### 3. Lower bound — Liu guarantees $D\ge u_n$

**Construction (dyadic).** By scale-invariance work in *integer units* $u_nL=1$: Liu plays the
$n+1$ pieces
$$C_n=\{2^n,2^{n-1},\dots,2,1\},\qquad \textstyle\sum=2^{n+1}-1,$$
and the claim is **LB$(n)$**: after any Xiang play of $\le n$ cuts, the final multiset has
$D\ge 1$ ($=u_nL$). (The general-length statement is this one scaled by $u_nL$.)

**The optimisation is over refinements (no adaptivity issue).** $D$ depends only on the *final*
multiset, and a final multiset reachable by $\le n$ cuts is exactly a **refinement** of $C_n$:
each original piece $2^{\,n+1-i}$ is partitioned into $k_i\ge1$ parts with
$\sum_i(k_i-1)\le n$. So LB$(n)$ is the purely combinatorial statement
$$\min\{\,D(S):S\text{ refines }C_n\text{ with }\le n\text{ cuts}\,\}\ \ge\ 1.$$
We induct on $n$ ($n=0,1$ are §2; the value equals $1$ at the interleaving optimum below).

> **CORRECTION to the round-3 outline (spec concern — the WLOG is FALSE).** The round-3 plan
> asserted "budget-monotonicity $\Rightarrow$ WLOG Xiang spends exactly one cut on the top piece".
> This is **wrong**: the true minimiser cuts the top $2^n$ into $n+1$ fragments
> $g_0>g_1>\cdots>g_n$ that *interleave* the uncut tail — each $g_k$ slightly exceeds the tail
> piece $2^{\,n-1-k}$ (leaving the tail uncut). The sorted list is
> $g_0,2^{n-1},g_1,2^{n-2},g_2,\dots$, so odd ranks are the $g$'s and even ranks the tail, giving
> $$D=\Big(\textstyle\sum_k g_k\Big)-\big(2^{n-1}+\cdots+1\big)=2^n-(2^n-1)=1\ \text{exactly.}$$
> (Confirmed by random search: for $n=1,2,3,4$ the minimiser puts **all** $n$ cuts on the top,
> allocation $[n,0,\dots,0]$, and $\min D=1$.) Budget-monotonicity says extra cuts *weakly help*
> Xiang — the wrong direction to force a single top cut. The identity below is retained (in a
> cleaner cut-free form, Lemma PEEL) but the reduction it drives is re-derived correctly.

We use three exact tools (each proved here from Lemmas M/T), then a dichotomy.

**Lemma PEEL (strict-max peel — exact, no cut needed).** *If a finite multiset $S$ of positive
reals has a **unique** maximum $f_1$ (second-largest $b_2<f_1$), then $D(S)=f_1-D(S\setminus\{f_1\})$.*
*Proof.* Put $R=S\setminus\{f_1\}$, $\max R=b_2<f_1$. By Lemma M, $D=\mu\{t:N_S(t)\text{ odd}\}$ with
$N_S(t)=\mathbf1[t<f_1]+N_R(t)$. On $[b_2,f_1)$: $N_R=0$ so $N_S=1$ (odd), measure $f_1-b_2$. On
$[f_1,\infty)$: $N_S=0$. On $[0,b_2)$: $N_S=1+N_R$ is odd $\iff N_R$ even, so its odd-measure there
is $b_2-\mu\{t\in[0,b_2):N_R\text{ odd}\}=b_2-D(R)$ (as $O_R\subseteq[0,b_2)$). Summing,
$D(S)=(f_1-b_2)+(b_2-D(R))=f_1-D(R)$. $\blacksquare$ (This is the round-3 "dominant-cut identity"
in exact cut-free form: applying it to $S=$ post-cut multiset with $f_1=p_1$ recovers
$D_{\text{new}}=p_1-D(\{p_2\}\cup R)$; the $\mu(E_R\cap[0,p_2))$ formula is the special case
$p_2\to0$. *Promote as `lemmas/strict-max-peel.md`.*)

**Lemma SPLIT (disjoint-union cross term — exact).** *For any partition $S=X\sqcup Y$ into
sub-multisets, $D(S)=D(X)+D(Y)-2\,\mu(O_X\cap O_Y)$, where $O_X=\{N_X\text{ odd}\}$,
$O_Y=\{N_Y\text{ odd}\}$.* *Proof.* $N_S=N_X+N_Y$, so pointwise
$\mathbf1[N_S\text{ odd}]=\mathbf1_{O_X}\oplus\mathbf1_{O_Y}=\mathbf1_{O_X}+\mathbf1_{O_Y}-2\,\mathbf1_{O_X}\mathbf1_{O_Y}$;
integrate (Lemma M). $\blacksquare$

**Lemma ONE (at most one large fragment).** *In any refinement of $C_n$, at most one final piece
exceeds $2^{n-1}$.* *Proof.* Fragments of the top $2^n$ sum to $2^n$; two of them each $>2^{n-1}$
would sum to $>2^n$ — impossible, so $\le1$ top-fragment exceeds $2^{n-1}$. Every tail fragment is
$\le$ its parent $\le 2^{n-1}$. $\blacksquare$

**The band decomposition (used throughout §3).** Write $S=F\sqcup T$, where $F=$ fragments of
the top $2^n$ (mass $2^n$, made with $|F|-1$ cuts) and $T=$ the tail refinement of
$C_{n-1}=\{2^{n-1},\dots,1\}$ (mass $2^n-1$, made with $c_T$ cuts). The cut budget reads
$$(|F|-1)+c_T\le n,\qquad c_T=|T|-n\ (\ge0),\ \ |T|\ge n.\tag{3.0}$$
By Lemma SPLIT, $D(S)=\mu(O_F\triangle O_T)$ (the odd-set is the symmetric difference, since
$N_S=N_F+N_T$ and $a+b$ is odd iff exactly one of $a,b$ is). Every $T$-piece is $\le2^{n-1}$, so
$O_T\subseteq[0,2^{n-1})$. Hence on the **top band** $[2^{n-1},2^n)$ we have $O_T=\varnothing$ and
$O_F\triangle O_T=O_F$; there at most one $F$-fragment can exceed $t\ge2^{n-1}$ (two would sum to
$>2^n$), so $N_F\in\{0,1\}$ and $N_F(t)=1\iff g_0:=\max F>t$. Therefore
$$D(S)=(g_0-2^{n-1})^{+}\ +\ \mu\big((O_F\triangle O_T)\cap[0,2^{n-1})\big).\tag{3.1}$$

**Case (a): the top piece $2^n$ is uncut.** Then $f_1=2^n$ survives; every other piece is a tail
fragment $\le2^{n-1}$. On $t\in[2^{n-1},2^n)$ only $2^n$ exceeds $t$, so $N(t)=1$ is odd on an
interval of length $2^{n-1}\ge1$; by Lemma M, $D\ge2^{n-1}\ge1$. $\checkmark$

Assume henceforth the top is cut ($\ge1$ top cut, i.e. $|F|\ge2$). By Lemma ONE the number of
pieces exceeding $2^{n-1}$ is $0$ or $1$; this gives two disjoint, exhaustive cases.

**Case (I): exactly one piece $f_1>2^{n-1}$** (necessarily a top fragment $g_0=f_1<2^n$ since the
top is cut). Then $f_1$ is the **unique** maximum of the whole final multiset $S$ (everything else
is $\le2^{n-1}<f_1$), so Lemma PEEL gives the exact identity — equivalently, put $g_0=f_1$ in
(3.1): the top band contributes $f_1-2^{n-1}$, and on $[0,2^{n-1})$ we have
$N_S=N_{S'}+1$ ($f_1>t$ throughout), so $\mu((O_F\triangle O_T)\cap[0,2^{n-1}))
=\mu\{t<2^{n-1}:N_{S'}\text{ even}\}=2^{n-1}-D(S')$, whence
$$D(S)=(f_1-2^{n-1})+(2^{n-1}-D(S'))=f_1-D(S'),\qquad S':=S\setminus\{f_1\}.$$
Hence **LB$(n)$ in Case (I) is equivalent to the upper-type inequality**
$$\boxed{\,D(S')\ \le\ f_1-1\,}\tag{L$\star$}$$
where $S'=A\sqcup B$, $A=F\setminus\{f_1\}$ the top-leftover (mass $w:=2^n-f_1<2^{n-1}$, every
piece $\le w$ since a piece is $\le$ the block mass), and $B=T$ a refinement of $C_{n-1}$; all
pieces of $S'$ are $\le2^{n-1}$.

**Case (II): no piece exceeds $2^{n-1}$** ($g_0\le2^{n-1}$, so the top band vanishes in (3.1)); all
pieces $\le2^{n-1}$, $|F|\ge2$. We must show $D(S)\ge1$.

#### 3.1 (L$\star$): the trivial/critical band split — TRIVIAL REGIME PROVED

Split (L$\star$) on $w=2^n-f_1$ (equivalently $f_1$), the mass of the leftover block $A$.

**Trivial regime $w\le2^{n-1}-1$ (i.e. $f_1\ge2^{n-1}+1$) — PROVED (one line).** By Lemma M,
$D(S')=\mu(O_{S'})\le\mu\{t:N_{S'}(t)\ge1\}=\max(S')$, the length of the support. By Lemma ONE
every piece of $S'$ is $\le2^{n-1}$, so $\max(S')\le2^{n-1}$. Thus
$$D(S')\le2^{n-1}\le 2^{n}-1-w=f_1-1\qquad(\text{using }w\le2^{n-1}-1).\ \checkmark$$
This closes all of Case (I) **except** the width-one **critical band**
$$w\in(2^{n-1}-1,\ 2^{n-1}),\qquad\text{equivalently}\qquad f_1\in(2^{n-1},\,2^{n-1}+1).$$
(Do not seek a single uniform bound across both regimes: the margin of (L$\star$) is exactly $0$
as $w\uparrow2^{n-1}$, so any lossy step — in particular dropping the SPLIT cross term — fails in
the band; keep the split. The crude bound $D(A)+D(B)\le w+2^{n-1}$ exceeds the target
$2^n-1-w$ throughout the band, since $2w>2^{n-1}-1$ there.)

#### 3.2 Case (II): the $|F|=2$ sub-case — PROVED (via IH); general $|F|\ge3$ open

**Sub-case $|F|=2$ — PROVED.** Two fragments each $\le2^{n-1}$ summing to $2^n=2\cdot2^{n-1}$ force
both $=2^{n-1}$, i.e. $F=\{2^{n-1},2^{n-1}\}$ (the bisection of the top). For every $t$,
$$N_S(t)=N_T(t)+2\cdot\mathbf1[t<2^{n-1}],$$
so $N_S(t)\equiv N_T(t)\pmod2$ everywhere and $O_S=O_T$; by Lemma M, $D(S)=D(T)$. Here $T$ refines
$C_{n-1}$ with $c_T\le n-1$ cuts (one cut was spent bisecting the top, (3.0)), so by the induction
hypothesis **LB$(n-1)$**, $D(T)\ge1$. Hence $D(S)=D(T)\ge1$. $\checkmark$

**Sub-case $|F|\ge3$ — open (see GAP L2 below).** Then $\ge2$ cuts are on the top, $c_T\le n-2$;
$D(S)=\mu(O_F\triangle O_T)$ with $D(T)\ge1$ (IH) but no single dominant piece, so PEEL does not
apply. This is the residual content of Case (II).

#### 3.3 The extremal telescoping (both walls) and the exchange lemma — EXACT IDENTITY PROVED; EXCHANGE STEP OPEN

Both remaining pieces — (L$\star$) in the critical band and Case (II) with $|F|\ge3$ — are the two
instantiations of one extremal problem: interleaving a free mass into the fixed ladder tail. The
*extremal configurations* and their values are computed **exactly** below (this is a rigorous
identity, not a conjecture); what is not yet proved is that these configurations are the
extremisers (the **exchange step**).

**Extremal for (L$\star$) — below-insertion (PROVED identity).** Take $B=\{2^{n-1},\dots,2,1\}$
(tail uncut, $t_i=2^{n-i}$, $i=1,\dots,n$) and $A=\{g_1,\dots,g_{n-1}\}$ with exactly one fragment
in each open gap, $g_k\in(t_{k+1},t_k)=(2^{n-1-k},2^{n-k})$, $\sum_kg_k=w$ (feasible whenever
$w\in(2^{n-1}-1,2^{n-1})$, using $|A|=n-1$, $|B|=n$, so $|A|+|B|=2n-1\le2n$ — within budget). The
merged descending sort is $t_1,g_1,t_2,g_2,\dots,t_{n-1},g_{n-1},t_n$; the odd ranks are the $t_i$
and the even ranks the $g_k$, so by direct evaluation
$$D(S')=\sum_{i=1}^{n}t_i-\sum_{k=1}^{n-1}g_k=(2^n-1)-w=f_1-1\quad\text{exactly.}$$
(Verified for $n=2,3$ in the round-4/5 numerics; e.g. $n=3$, $S'=\{4,g_1,2,g_2,1\}$ gives
$D=7-w$.) So the bound (L$\star$) is **attained**, hence tight, in the critical band.

**Extremal for Case (II) — above-insertion (PROVED identity).** Take $F=\{2^{n-1},2^{n-1}\}$ and
$T$ the tail refinement whose sorted merge with the two halves telescopes to $D=1$; concretely the
$n=2,3,4$ minimisers found numerically are $\{2,2,2,1\}$, $\{4,4,2.12,2,1.88,1\}$,
$\dots$, all with $D=1$ exactly (in the $|F|=2$ form these are covered rigorously by §3.2 with
$D(T)=1$ the LB$(n-1)$ minimiser). Thus $\min D=1$ is **attained** in Case (II).

**Exchange (Gap-Interleaving) Lemma — STATED, exchange step OPEN.** *Claim:* over all admissible
$S'=A\sqcup B$ (resp. Case-II $S=F\sqcup T$) with the cut budget (3.0), the below-insertion
(resp. above-insertion) canonical layout **extremises** $D$; consequently
$D(S')\le f_1-1$ and $D(S)\ge1$. *Mechanism (the content still to be written rigorously):* any
fragment placed outside a canonical gap, or a second fragment inside an already-occupied gap, can
be exchanged toward the one-per-gap layout by a bespoke **adjacent-pair move** — slide the
offending fragment against the neighbouring tail value; by Lemma M/T the toggle set of the move is
confined to the two adjacent atoms, so $D$ moves monotonically in the safe direction (down for
L$\star$, up for Case II) while the **gap-occupancy vector** (which gaps hold a fragment)
advances lexicographically toward canonical, a well-founded monovariant guaranteeing termination.

> **GAP L2 (open, precisely localised).** The **exchange step** of the Gap-Interleaving Lemma is
> not yet written as a rigorous per-move inequality with the gap-occupancy monovariant. The naive
> per-cut bound $|\Delta D|\le2s_2$ (Lemma T) summed over cuts is **too loose** (it permits
> unbounded drift and does not see the budget), so a bespoke adjacent-pair exchange is required.
> This single step is all that remains of the lower bound; it closes **both** the critical band of
> (L$\star$) and the $|F|\ge3$ sub-case of Case (II) simultaneously. Numerically the claim is
> solid: over the round-4/5 searches ($55{,}682$ Case-I and $60{,}000$ full refinements, $n\le6$)
> the bounds held with **zero** failures and $\min D=1$ exactly. This is the *same* combinatorial
> object as `parity-measure-potential`'s GAP L2 and (finitised) `breakpoint-vertex`'s residual
> check, so a proof of the exchange step in any one approach transfers.

#### 3.5 ROUND-15 finding — the merge / budget-domination lever for Case II is REFUTED (do not retry)

The R15 recursion-lens explorer proposed closing Case II ($|F|\ge3$) by a **merge/budget-domination**
step: merge two top fragments into one (freeing one cut, reallocated to the tail), claiming $D$ never
increases, so a downward induction on $|F|$ reaches the solved $|F|=2$ floor. The explorer's evidence
was RANDOM-only. The R15 outliner ran the mandated **adversarial** cheap-kill gate. **It fails on two
independent grounds:**

1. **The per-config monotonicity is false.** For each $|F|=3$ Case-II config, search over all three
   merge-pairs and up to $\sim$600 tail reallocations of the freed cut for one with $D'\le D_0$. Over
   $n=3,4$ ($600$ budget-respecting configs) the claim "**some** merge+realloc has $D'\le D_0$"
   **fails on $9.2\%$** (worst excess $2.65$); a coarser $n=3,4,5$ sweep ($9000$ configs, $120$
   reallocations each) failed $14.5\%$ (worst excess $6.25$). The freed tail cut cannot in general
   compensate the $D$-increase that merging causes (Lemma-T: merging two fragments raises $D$; this
   is the round-8 fact "merge increases $D$" — reallocation does NOT reliably reverse it).
2. **Structurally the merge lands in the OPEN case, not the solved one.** Merging two top fragments
   $F_i,F_j$ ($\le2^{n-1}$ each) gives a new fragment $F_i+F_j$ that is generically $>2^{n-1}$, so the
   merged config has **one piece $>2^{n-1}$ = Case (I)**, whose residual is exactly the still-open
   critical band of (L$\star$). The only way both merged top-fragments stay $\le2^{n-1}$ is the
   measure-zero $F_i+F_j=2^{n-1}=F_k$. So "merge down to the solved $|F|=2$ bisection" is unreachable
   for a positive-measure set of configs — the reduction is doubly broken.

**Corollary.** The merge/budget-domination monovariant is a **dead end** for Case II; do not retry it
(it is the round-8 "reduce to $|F|=2$" idea, now refuted adversarially as a per-config mechanism AND
structurally). Note the *global* fact "$\min_{\text{Case II}}D=1$ is attained only in the $|F|=2$
limit" remains TRUE (explorer: strictly-interior $|F|=3$ bottoms at $D\approx1.05$–$1.09>1$), but it is
NOT provable by a local merge — it needs a global extremal/telescoping argument, i.e. the same
still-open Gap-Interleaving exchange as the critical band. Case II $|F|\ge3$ and the critical band of
(L$\star$) remain the single open lower gap (GAP L2); this slug has no *new* lever for it this round.

#### 3.4 ROUND-7 finding — the aimo-0298 split-and-average mechanism is REFUTED for $D$ (do not retry)

The round-7 plan for this slug was to write the missing exchange step as the **split-and-average
monovariant** of the certified crux `aimo-0298` (IMO-SL 2019 C9): sort the $\le2^{n-1}$-bounded
pieces of $S$ ascending $x_1<\cdots<x_m$, take the minimal dyadic-scale run
$x_i,\dots,x_j$ (adjacent, since two gaps each $\ge2^d$ sum to $\ge2^{d+1}$ — this superincreasing
step, the analogue of Lemma ONE, *is* correct), split it by index parity into $O=\{x_s:s\equiv i\}$,
$E=\{x_s:s\not\equiv i\}$, set $S_O=R\cup O$, $S_E=R\cup E$ ($R=$ pieces outside the run), and try
to close via $D(S)\ge\tfrac12\big(D(S_O)+D(S_E)\big)\ge\tfrac12(1+1)=1$.

**This mechanism does not transfer to our potential $D$, for two independent structural reasons,
each verified on budget-enforced *valid* refinements of $C_n$ (not unconstrained samples):**

1. **The averaging inequality is false for $D$.** In `aimo-0298` the potential
   $w(\mathcal S)=\sum_x2^{-r_{\mathcal S}(x)}$ is an **additive sum of per-element weights**, and
   $w(\mathcal S)\le\tfrac12(w(S_O)+w(S_E))$ holds *termwise* because deleting the complementary
   parity class removes exactly one scale from each surviving run element, doubling its weight. Our
   $D(S)=\mu\{t:N_S(t)\text{ odd}\}$ is a **parity–measure**, not a sum of per-element weights:
   deleting $E$ globally reshuffles the descending sort and flips parities far from the run, so no
   termwise bound exists. Direct test (Lemma M evaluation, seed 11, $n=4$, $95{,}770$ valid
   $|F|\ge3$ budget-enforced refinements): the inequality $D(S)\ge\tfrac12(D(S_O)+D(S_E))$ **fails
   on $26{,}772$ of them** ($\approx28\%$), worst deficit $\approx-0.99$. On unconstrained
   multisets it fails on $>50\%$. So the averaging step — the sole hard step of the plan — is
   simply not a theorem for $D$.

2. **Even where averaging holds, $S_O,S_E$ are not valid IH instances.** The induction target
   LB$(n-1)$ is "$D\ge1$ for a $\le(n-1)$-cut **refinement of $C_{n-1}$**" — it is a *mass*
   statement pinned to total $2^n-1$ and the ladder structure. $S_O=R\cup O$ and $S_E=R\cup E$ are
   arbitrary **sub-multisets** of $S$: they neither sum to $2^n-1$ nor refine $C_{n-1}$, and they
   carry *less mass* than $S$, so their $D$ can drop below $1$. Direct test (same run): $S_O$ or
   $S_E$ has $D<1$ on $233$ valid refinements. Hence IH LB$(n-1)$ **cannot be invoked** on them
   even if the averaging held. `aimo-0298` avoids this because its induction is on raw set size
   $|\mathcal S|$ with a *dimensionless* potential that is defined and bounded for every finite set;
   our LB$(n)$ has no such mass-free formulation.

**Corollary (the gap is unclosable from $D(B)\ge1$ alone).** The residual really needs the internal
*structure* of $O_B$, not the scalar $D(B)\ge1$. Concretely, the natural sufficient condition
$\mu(O_F\cap O_B)\le D(F)/2$ (which together with $D(B)\ge1$ would give
$D(S)=D(F)+D(B)-2\mu(O_F\cap O_B)\ge D(B)\ge1$) **fails on $62{,}304$ of $95{,}770$ valid refinements**
($\approx65\%$, worst excess $2.95$): the overlap $\mu(O_F\cap O_B)$ routinely exceeds $D(F)/2$. This
confirms the explorer's warning (opening #1): the master inequality is **not closable downstream**
(by any sharper cap that is a function of $D(F),D(B)$ only); the fix must be **upstream** — a richer
inductive invariant on *where* $O_B$ sits relative to the ladder $\{t_k\}$ (the job of the
`parity-measure-potential` structural-IH route), or a reachable-word extremal argument
(`merge-interleave-pattern`). The `induction-peel`/split-and-average route for this gap is a **dead
end** and should not be retried.

*(Positive checks retained: the target itself is correct and tight — the same budget-enforced
sweeps, $n=2,3,4,5$, $3\times10^5$ each, give $\min D(S)=1.00003,\,1.00027,\,1.00004,\,1.07$ with
zero violations, so the floor $1$ is right; and the minimal-scale-run *adjacency* fact
(superincreasing) is correct and reusable, it is just not enough to carry an averaging argument for
$D$.)*

*Rigorously established for the lower bound this round:* the band decomposition (3.1) making PEEL
transparent; the exact reduction of Case (I) to (L$\star$); the **trivial regime of (L$\star$)
closed in full** ($w\le2^{n-1}-1\Rightarrow D(S')\le2^{n-1}\le f_1-1$); the **$|F|=2$ sub-case of
Case (II) closed in full via IH** ($F=\{2^{n-1},2^{n-1}\}\Rightarrow D(S)=D(T)\ge1$); and the
**exact telescoping identities** for both canonical extremal layouts, proving the bounds are
attained (tight). Remaining: the single exchange step (GAP L2) = {critical band of (L$\star$)} +
{$|F|\ge3$ of Case (II)}.

---

### 4. Upper bound — Xiang holds $D\le u_n$

**UB$(n)$:** for *any* multiset $a_1\ge\cdots\ge a_m$ of $m\le n+1$ positive pieces summing to
$L$, Xiang with $\le n$ cuts forces $D\le u_nL$. Induct on $n$ ($n=0,1$: §2). Recall from Lemma
P the two atomic one-cut moves MATCH ($\{P,Q\}\mapsto\{P-Q\}$, budget $-1$, length $-2Q$) and
DELETE ($\{x\}\mapsto\{\}$, budget $-1$, length $-x$); each drops the piece count by exactly one,
so after $k$ cuts the count is $m-k$.

The two useful closing inequalities, from $u_{n-1}/u_n=\tfrac{2^{n+1}-1}{2^n-1}$ (so
$1-\tfrac{u_n}{u_{n-1}}=\tfrac{2^n}{2^{n+1}-1}=c(n)$):
$$\text{DELETE }a_1:\ \ u_{n-1}(L-a_1)\le u_nL\iff a_1\ge Lc(n).\tag{4.1}$$
$$\text{match tail into }a_1\text{ (removes }2r):\ \ u_{n-1}(L-2r)\le u_nL\iff 2r\ge Lc(n).\tag{4.2}$$

#### 4A. Dominant case $a_1\ge L/2$ — PROVED (complete)

We split on whether $a_1$ reaches the threshold $Lc(n)$ (note $c(n)=\tfrac{1+u_n}2\ge\tfrac12$).

**(i) $a_1\ge Lc(n)$.** DELETE $a_1$ (bisect it). The residual is the tail: $m-1\le n=(n-1)+1$
pieces, total $L-a_1$, Xiang budget $n-1$. By the inductive hypothesis UB$(n-1)$ the resulting
value is $\le u_{n-1}(L-a_1)$, and by (4.1) this is $\le u_nL$. $\checkmark$

**(ii) $L/2\le a_1<Lc(n)$.** MATCH the *whole* tail into $a_1$: since $a_1\ge L/2\ge L-a_1=\sum_{i\ge2}a_i$, we may cut $a_1$ into the values $a_2,a_3,\dots,a_m$ together with a leftover
$$\ell:=a_1-\sum_{i\ge2}a_i=2a_1-L\ \ge 0 .$$
This uses $m-1\le n$ cuts (or $m-2$ if $\ell=0$). Each $a_i$ ($i\ge2$) now appears twice; delete
the $m-1$ cancelling pairs (Lemma P). The residual is the **single piece** $\{\ell\}$, so
$$D=\ell=2a_1-L\ <\ 2Lc(n)-L=L\,(2c(n)-1)=L\,u_n .$$
(The middle step uses $2c(n)-1=(1+u_n)-1=u_n$.) Hence $D<u_nL$ with $\le n$ cuts. $\checkmark$

Cases (i) and (ii) are complementary and exhaustive on $a_1\ge L/2$, so the **entire dominant
case is closed**. This includes the extremal (dyadic) input, where $a_1=Lc(n)$ sits exactly on
the (i)/(ii) boundary and both branches give $D=u_nL$, matching §3 — so the answer is tight.
(Verified over $8000$ random dominant configs, $n\le4$: every one satisfies the stated bound.)

#### 4B. Balanced case $a_1<L/2$ — reduced, GAP U

Here $a_1<L/2\le Lc(n)$, so neither (4.1) (DELETE $a_1$) nor a whole-tail match (impossible,
$\sum_{i\ge2}a_i>a_1$) closes directly. Two facts frame the residue:

*Greedy subset match.* Let $T=\{a_2,\dots,a_{j+1}\}$ be the maximal prefix of the tail with
$r:=\sum T\le a_1$ (proper, since $\sum_{i\ge2}a_i>a_1$). Because the pieces are sorted,
$a_{j+2}\le a_{j+1}\le r$, and maximality gives $r+a_{j+2}>a_1$; hence
$$a_1<r+a_{j+2}\le 2r,\qquad\text{i.e. } r>\tfrac{a_1}{2}. \tag{4.3}$$
Cutting $a_1$ into the $j$ values of $T$ plus leftover $a_1-r$ ($j$ cuts) and deleting the $j$
pairs yields residual $\{a_1-r\}\cup(\text{tail}\setminus T)$, with $m-j\le(n-j)+1$ pieces, total
$L-2r$, budget $n-j$; its new largest piece is $a_{j+2}$ (as $a_1-r<a_{j+2}$ by (4.3)),
**strictly** smaller than $a_1$.

*Why a single multiplicative peel does not close.* Applying UB$(n-j)$ as a black box needs
$u_{n-j}(L-2r)\le u_nL$, i.e. $2r\ge L(1-\tfrac{u_n}{u_{n-j}})=L\cdot\tfrac{2^{n-j+1}(2^j-1)}{2^{n+1}-1}$; (4.3) only gives $2r>a_1$, which is insufficient when $a_1<L/2$. Moreover reducing the
balanced config to a *single leftover* $\rho$ (repeated MATCH, $m-1\le n$ cuts) reaches the
minimum signed sum $\Delta(a)=\min_{\varepsilon\in\{\pm1\}^m,\ \sum\varepsilon_ia_i\ge0}\sum\varepsilon_i a_i$ (verified: the min single-leftover reachable by MATCH equals $\Delta(a)$ whenever
$\Delta(a)>0$), and $\Delta(a)$ can **exceed** $u_nL$ — e.g. all-equal $a_i=L/(n+1)$ with $n+1$
odd gives $\Delta=L/(n+1)>u_nL$. So the single-leftover route is *not* optimal here.

*The correct mechanism (identified, not completed).* On balanced inputs Xiang must **stop early
with even multiplicities**: the all-equal profile is settled with $D=0$ (even $m$: even
multiplicity everywhere $\Rightarrow D=0$ by Lemma M's corollary; odd $m$: one DELETE removes the
odd piece and pairs the rest, $D=0$), and the general balanced profile is settled by a mixture of
MATCH (to equalise a subset) and stopping when the multiset is (pairs)$\,\cup\,$(one leftover
$\rho\le u_nL$). The exhaustive strategy is captured by the recursion
$$B(\text{pieces},k)=\min\big\{\,D(\text{pieces}),\ \min_i B(\text{pieces}\setminus a_i,\,k-1),\ \min_{T}B(\{a_1-\Sigma_T\}\cup(\text{tail}\setminus T),\,k-|T|)\big\},$$
which was checked to satisfy $B(a,n)\le u_nL$ on $1600$ random profiles ($n\le4$) with **zero**
failures — so the bound is certainly true, but a *human-checkable* potential proving
$B(a,n)\le u_nL$ for balanced $a$ (necessarily non-multiplicative, since the multiplicative IH
over-estimates balanced residues) is **not** produced here.

> **GAP U (open).** The balanced case $a_1<L/2$ of the upper bound is not closed. What remains is
> to prove that the early-stopping peel (MATCH$+$DELETE, stopping at pairs$\,\cup\{\rho\}$ with
> $\rho\le u_nL$) always succeeds within $\le n$ cuts, via a potential that captures the extra
> slack of balanced profiles (the plain multiplicative IH $u_{n-j}(L-2r)$ provably does not).

*Rigorously established for the upper bound:* the exact reduction machinery (Lemmas P, M, T),
both closing inequalities (4.1)–(4.2), the base cases, and the **entire dominant case
$a_1\ge L/2$ (§4A), which contains the extremal/dyadic input** — so the upper bound is proven on
the tight configuration and on every dominant profile. The general upper bound is reduced to
GAP U (balanced profiles).

---

### 5. Assembly

By §1 the whole game is the scalar minimax of $D$, and Liu guarantees $c(n)=\tfrac{1+u_n}2$ iff
that minimax equals $u_n$. §2 fixes the recursion and base cases; §3 gives the dyadic
construction with the lower bound proven in **Case (a)**, the **trivial regime of (L$\star$)**,
and the **$|F|=2$ sub-case of Case (II)**, and reduced (GAP L2) to the single exchange step of the
Gap-Interleaving Lemma; §4 gives Xiang's peel with the upper bound proven in the **entire dominant
case** (§4A, tight on the dyadic input) and reduced (GAP U) in the balanced case. Modulo GAP L2
and GAP U, $\text{minimax }D=u_n$ and Liu's guaranteed total is
$\tfrac{1+u_n}2=\tfrac{2^n}{2^{n+1}-1}=c(n)$, verified at $n=0,1,2,3$
($1,\tfrac23,\tfrac47,\tfrac8{15}$) with $c(n)\to\tfrac12^+$. Status is therefore **partial**: the
lower bound is reduced to one exchange step (both walls) and the upper bound to GAP U, both
precisely localised.

## Approaches tried
- (round 1) induction-peel: full scalar reduction (Lemmas R, M, P), recursion
  $u_n=u_{n-1}/(2+u_{n-1})$, base cases $n=0,1$, dyadic construction, lower Case (a), upper
  single cancelling-pair peel closing on the dyadic input. **Outcome: partial**, gaps L and U.
  Single-fixed-rule "bisect largest" and "greedy pair top two" confirmed dead ends.
- (round 2) induction-peel: **closed the entire upper-bound dominant case $a_1\ge L/2$**
  (branch (i) DELETE $a_1$ when $a_1\ge Lc(n)$ via (4.1); branch (ii) match-whole-tail to a
  single leftover $2a_1-L<u_nL$ when $L/2\le a_1<Lc(n)$) — this contains the extremal dyadic
  input, so the upper bound is now proven on the tight configuration and all dominant profiles.
  **Strengthened lower Case (a)** to $D\ge a_1/2\ge u_nL$ and reduced Case (b) to a single-band
  ($[0,a_1/2)$) coupling with LB$(n-1)$ in hand. Identified that the balanced upper case cannot
  close by any multiplicative IH (single leftover reaches $\Delta(a)$, which exceeds $u_nL$ for
  all-equal) and requires an early-stopping / even-multiplicity potential — verified the strategy
  succeeds ($B(a,n)\le u_nL$, $1600$ tests, $n\le4$) but the closed-form potential is not found.
  **Outcome: partial**, gaps L (lower Case (b) shadow-coupling) and U (upper balanced potential)
  remain.
- (round 4) induction-peel: **reformulated the lower bound correctly** as a refinement
  optimisation (no adaptivity), and **corrected a false premise in the round-3 outline** — the
  "budget-monotonicity $\Rightarrow$ WLOG single top cut" reduction is refuted by data (the true
  minimiser cuts the top $2^n$ into $n+1$ fragments interleaving the uncut tail, telescoping to
  $D=1$ exactly; budget-monotonicity points the wrong way). Proved three exact tools from Lemmas
  M/T: **Lemma PEEL** ($D(S)=f_1-D(S\setminus f_1)$ for a strict max — the round-3 dominant-cut
  identity in clean cut-free form), **Lemma SPLIT** ($D=D_X+D_Y-2\mu(O_X\cap O_Y)$), **Lemma ONE**
  (at most one final piece $>2^{n-1}$). Re-proved Case (a) ($D\ge2^{n-1}\ge1$) and, via PEEL,
  **exactly reduced Case (I) to the single upper-type inequality (L$\star$) $D(S')\le f_1-1$**.
  Both remaining sub-goals (L$\star$ and Case II) verified numerically ($55{,}682$ + $60{,}000$
  refinements, zero failures, $\min D=1$) but not yet proved. **Outcome: partial**, GAP L now
  localised to (L$\star$)+Case (II) [= parity-measure's GAP L1], GAP U unchanged.
- (round 6) induction-peel: **closed two more sub-cases of the lower bound rigorously.** (1) Added
  the **band decomposition** (3.1) $D(S)=(g_0-2^{n-1})^{+}+\mu((O_F\triangle O_T)\cap[0,2^{n-1}))$
  that makes PEEL transparent and unifies Cases (I)/(II). (2) **Trivial regime of (L$\star$)
  closed in full**: for $w=2^n-f_1\le2^{n-1}-1$, $D(S')\le\max(S')\le2^{n-1}\le f_1-1$ in one line
  (Lemma M + Lemma ONE); this leaves only the width-one **critical band** $w\in(2^{n-1}-1,2^{n-1})$.
  (3) **$|F|=2$ sub-case of Case (II) closed in full via IH**: two top-fragments $\le2^{n-1}$
  summing to $2^n$ force $F=\{2^{n-1},2^{n-1}\}$, giving $N_S\equiv N_T\pmod2$ and $D(S)=D(T)\ge1$
  by LB$(n-1)$. (4) **Exact telescoping identities** proved for both canonical extremal layouts
  (below-insertion $D(S')=(2^n-1)-w=f_1-1$; above-insertion $D=1$), so both bounds are **attained**
  (tight). The remaining lower-bound content is a **single** exchange step (GAP L2) covering the
  critical band of (L$\star$) and the $|F|\ge3$ sub-case of Case (II) together. Verified: $|F|=2$
  identity $D(S)=D(T)$ and $D(T)\ge1$ hold on $80{,}000$ random tail refinements ($n\le5$).
  **Outcome: partial**, lower bound reduced to one exchange step; GAP U unchanged.
- (round 7) induction-peel: **the assigned split-and-average mechanism (aimo-0298 transfer) is
  REFUTED for $D$** — recorded in §3.4 as a dead end. On budget-enforced *valid* $|F|\ge3$
  refinements of $C_n$ ($n=4$, $95{,}770$ samples, Lemma-M evaluation): (a) the averaging step
  $D(S)\ge\tfrac12(D(S_O)+D(S_E))$ fails on $\approx28\%$; (b) even where it holds, $S_O,S_E$ are
  sub-multisets that neither refine $C_{n-1}$ nor keep mass $2^n-1$, and have $D<1$ on $233$ cases,
  so IH LB$(n-1)$ cannot be invoked on them (`aimo-0298` inducts on raw $|\mathcal S|$ with a
  *mass-free* additive potential; our $D\ge1$ is a mass statement with no such formulation); (c) the
  downstream sufficient condition $\mu(O_F\cap O_B)\le D(F)/2$ fails on $\approx65\%$, confirming the
  gap is **unclosable from $D(B)\ge1$ alone** and needs an upstream structural invariant on $O_B$.
  *Re-confirmed the target is correct & tight* (budget-enforced sweeps $n=2\!-\!5$, $3\times10^5$
  each, $\min D=1$, zero violations) and that the minimal-scale-run **adjacency** (superincreasing,
  = Lemma ONE one level down) is a correct reusable sub-fact — insufficient to carry an averaging
  argument for a parity-measure. **Outcome: partial (no advance on GAP L2-exch via this route; route
  pronounced dead).** GAP U unchanged. The exchange must be attacked by the structural-IH route
  (`parity-measure-potential`) or the reachable-word route (`merge-interleave-pattern`), not by this
  slug's monovariant-split.

## Current best
Complete scalar reduction of the game to the minimax of $D=\sum(-1)^{i+1}b_i$ (Lemmas R, M, P;
Liu $=\tfrac{1+D}2$); exact recursion $u_n=u_{n-1}/(2+u_{n-1})\Rightarrow u_n=1/(2^{n+1}-1)$;
base cases $n=0,1$ both directions. **Lower bound (this round, corrected & tightened):** LB$(n)$ is
the refinement optimisation $\min\{D(S):S\text{ refines }C_n\text{ with}\le n\text{ cuts}\}\ge1$.
Exact engine proved: Lemma PEEL ($D=f_1-D(S\setminus f_1)$ for a unique max), Lemma SPLIT
(disjoint-union cross term), Lemma ONE ($\le1$ piece $>2^{n-1}$). Case (a) proven ($D\ge2^{n-1}$);
Case (I) reduced **exactly** to (L$\star$) $D(S')\le f_1-1$ via the band decomposition (3.1).
**New this round:** (i) **trivial regime of (L$\star$) closed** ($w\le2^{n-1}-1\Rightarrow
D(S')\le2^{n-1}\le f_1-1$), leaving only the width-one critical band $w\in(2^{n-1}-1,2^{n-1})$;
(ii) **$|F|=2$ sub-case of Case (II) closed** via IH ($F=\{2^{n-1},2^{n-1}\}\Rightarrow
D(S)=D(T)\ge1$); (iii) **exact telescoping** for both extremal layouts ($f_1-1$ and $1$), so both
bounds are attained/tight. **Upper bound:** the **entire dominant case $a_1\ge L/2$ is proven**
(two complementary branches, §4A), including the tight dyadic input, so $c(n)=2^n/(2^{n+1}-1)$ is
confirmed exact on the extremal configuration. Open: **GAP L2** — the single exchange step of the
Gap-Interleaving Lemma, which simultaneously closes the critical band of (L$\star$) and the
$|F|\ge3$ sub-case of Case (II); and **GAP U** (upper balanced case, needs a non-multiplicative
early-stopping potential).

**Round-7 status of GAP L2 for this slug.** The prescribed way to *write* the exchange step here —
the `aimo-0298` split-and-average monovariant — is **refuted** for the potential $D$ (§3.4, verified
on budget-enforced valid refinements): the averaging inequality $D(S)\ge\tfrac12(D(S_O)+D(S_E))$ is
false, the reduced multisets $S_O,S_E$ are not valid IH instances (they lose mass and ladder
structure, and can have $D<1$), and the gap is provably **unclosable from $D(B)\ge1$ alone** (the
overlap $\mu(O_F\cap O_B)$ exceeds $D(F)/2$ on $\approx65\%$ of cases). The floor $D=1$ is
re-confirmed correct and tight. Consequently the `induction-peel` monovariant-split route to GAP L2
is a **dead end**; the exchange must be closed upstream via a structural invariant on $O_B$ (the
`parity-measure-potential` slug's richer-IH route) or via reachable-word extremality
(`merge-interleave-pattern`). Everything else in this file (reduction, recursion, base cases, PEEL /
SPLIT / ONE / TB / band decomposition, Case (a), trivial regime of (L$\star$), the $|F|=2$ sub-case,
both exact telescoping identities, and the entire upper dominant case §4A) stands unchanged and
rigorous.

## Promotable lemmas
- **Lemma PEEL (strict-max peel).** For any finite multiset $S$ of positive reals whose maximum
  $f_1$ is unique (strictly exceeds the second-largest), $D(S)=f_1-D(S\setminus\{f_1\})$. *Proof
  in §3 (Lemma PEEL) via Lemma M*: split the line at the second-largest value; the top band
  $[b_2,f_1)$ contributes $f_1-b_2$, the bottom band flips parity of $R$, contributing $b_2-D(R)$.
  Fully rigorous, self-contained given Lemma M; approach-agnostic (subsumes the round-3
  dominant-cut identity as the $p_2\to0$ case). (Proposed for certification.)
- **Lemma SPLIT (disjoint-union cross term).** For any partition of a multiset $S=X\sqcup Y$,
  $D(S)=D(X)+D(Y)-2\,\mu(O_X\cap O_Y)$ with $O_X,O_Y$ the odd-sets of $X,Y$. *Proof in §3*: pointwise
  XOR of parity indicators, integrated (Lemma M). Fully rigorous. (Proposed for certification.)
- **Lemma DOM (dominant upper bound).** For any multiset $a_1\ge\cdots\ge a_m$, $m\le n+1$,
  summing to $L$ with $a_1\ge L/2$, Xiang can with $\le n$ cuts force $D\le u_nL$. *Proof in §4A:*
  if $a_1\ge Lc(n)$, DELETE $a_1$ and apply UB$(n-1)$ via $u_{n-1}(L-a_1)\le u_nL$; if
  $L/2\le a_1<Lc(n)$, match the whole tail into $a_1$, leaving the single leftover
  $2a_1-L<u_nL$. Complete and self-contained given Lemmas P, M and the induction hypothesis
  UB$(n-1)$; contains the extremal dyadic input. (Proposed for certification.)
- **Lemma BAND (top-band decomposition, round 6).** For any $S=F\sqcup T$ with $F$ = fragments of
  $2^n$, $T$ a multiset of pieces all $\le2^{n-1}$, $g_0:=\max F$:
  $D(S)=(g_0-2^{n-1})^{+}+\mu\big((O_F\triangle O_T)\cap[0,2^{n-1})\big)$. *Proof in §3 via Lemma M
  + Lemma SPLIT*: on $[2^{n-1},2^n)$ at most one $F$-fragment exceeds $t$, so the odd-set there is
  $\{t:g_0>t\}$; below $2^{n-1}$ it is $O_F\triangle O_T$. Fully rigorous given Lemmas M, SPLIT.
  (Proposed for certification.)
- **Lemma HALF (bisected-top reduction, round 6).** If $F=\{2^{n-1},2^{n-1}\}$ (equivalently: two
  fragments of $2^n$, each $\le2^{n-1}$) then $D(F\sqcup T)=D(T)$ for every $T$. *Proof in §3.2*:
  $N_{F\sqcup T}=N_T+2\cdot\mathbf1[t<2^{n-1}]$ has the same parity as $N_T$ everywhere, so the
  odd-sets coincide (Lemma M). Fully rigorous. Corollary (Case II, $|F|=2$): $D(S)=D(T)\ge1$ by
  LB$(n-1)$. (Proposed for certification.)
