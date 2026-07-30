## Status
partial

## Approach: smoothing-majorization (framing E) — REBUILT round 6: the upper bound as a finite DELETE/MATCH reduction game (D-tracking), NOT subset-cover, NOT global-concavity smoothing

Target (the whole claim): for every positive integer $n$, the largest $c$ Liu can guarantee is
$$c(n)=\frac{2^n}{2^{n+1}-1},\qquad\text{equivalently minimax }D=u_n=\frac1{2^{n+1}-1}.$$

Throughout $u_k:=1/(2^{k+1}-1)$, $c(k)=2^k/(2^{k+1}-1)=(1+u_k)/2$, and $\beta_k:=2^{k-1}/(2^{k+1}-1)$.
By Lemma R (`lemmas/reduction-odd-rank.md`) the game reduces to the scalar minimax of the
alternating sum $D=\sum_i(-1)^{i+1}b_i$ on the descending-sorted **final** multiset, and Liu's
guaranteed share is $(1+D)/2$; so it suffices to prove the minimax value of $D$ equals $u_n$.

This round's rebuild **discards** the refuted round-3 (SMOOTH) monotonicity ("$V$ nondecreasing
along a dyadic-ward exchange" — false, $V$ has interior valleys) and the round-5 (D-DICHOTOMY)
subset-pairing plan. In its place it recasts the entire **upper bound** (Xiang's side) as a
*finite combinatorial reduction game* on the multiset, using two elementary legal Xiang moves that
are exact D-tracking operations (both are instances of the certified cancelling-pair Lemma P). This
is a genuine reframing away from mass-threshold subset-cover (refuted, `whole-tail-peel.md`) and
from any convexity claim on $V$.

---

### 1. Imported infrastructure (certified) — no re-proof

- **Lemma R** (`lemmas/reduction-odd-rank.md`): minimax of $D=\sum(-1)^{i+1}b_i$; Liu $=(1+D)/2$.
- **Lemma M** (`lemmas/measure-identity.md`): $D=\mu\{t:N(t)\text{ odd}\}$, $N(t)=\#\{b_i>t\}$;
  even multiplicity of every value $\Rightarrow D=0$.
- **Lemma P** (`lemmas/cancelling-pair.md`): $D(S\cup\{v,v\})=D(S)$ for any $v>0$ and any multiset $S$.
- **Lemma WHOLE-TAIL-PEEL** (`lemmas/whole-tail-peel.md`): if $m\le k+1$, sum $L$, and
  $L/2\le a_1\le c(k)L$, then $\le k$ cuts force $D=2a_1-L\le u_kL$ (unconditional).

**Convention.** A *profile* is a multiset of positive lengths, sorted $a_1\ge a_2\ge\cdots\ge a_m$,
with sum $L$. Xiang's job (the upper bound) is: given a profile of $m\le n+1$ pieces and $n$ marks
(cuts) available, produce a final multiset with $D\le u_nL$.

---

### 2. Xiang's two elementary reductions (the D-tracking move set)

**Lemma DM (elementary reductions).** Let $S$ be the current multiset of pieces. Each of the
following is achievable by Xiang with **one** additional mark, and the stated $D$ identity holds
(a copy of a piece may be cancelled at any intermediate stage by Lemma P):

- **DELETE $x$** (bisection). Xiang marks the midpoint of a piece $x$, splitting it into
  $\{x/2,x/2\}$. By Lemma P the pair cancels: $D(S)\mapsto D\big(S\setminus\{x\}\big)$. Net effect:
  remove one piece; cost one mark.
- **MATCH $(x,y)$**, $x>y>0$ two *distinct* pieces of $S$. Xiang marks the point at distance $y$
  from one end of the piece $x$, splitting it into $\{y,\,x-y\}$. The new fragment $y$ equals the
  already-present piece $y$; by Lemma P the pair $\{y,y\}$ cancels:
  $D(S)\mapsto D\big((S\setminus\{x,y\})\cup\{x-y\}\big)$. Net effect: replace two pieces by their
  difference; cost one mark. (If $x=y$ the two equal pieces already cancel by Lemma P at **zero**
  cost.)

**Proof.** Both moves place a single interior mark on one current piece, hence use one Xiang mark
and are legal; in each case the resulting multiset contains a repeated value, and Lemma P (applied
to the full multiset) states that deleting that repeated pair leaves $D$ unchanged. The stated
image multiset is exactly the full multiset with that pair deleted. $\square$

**Bookkeeping.** Xiang applies a finite sequence of DELETE/MATCH moves. Each non-degenerate move
uses exactly one mark, so a sequence of $\le n$ non-degenerate moves is a legal Xiang response
(marks land at interior points of disjoint intervals, so any measure-zero coincidence with an
existing mark is avoided by choosing which end of the piece to measure the offset from). The value
of $D$ after the sequence is the alternating sum of the reduced multiset, computed exactly along
the way by Lemma P. **This replaces the continuum of Xiang responses by a finite reachability
game — with no subset enumeration and no mass threshold.** (For the *upper* bound we need only that
these moves are *legal and sufficient*; we do **not** claim they are *optimal* — that is the
separate VERT statement of the breakpoint-vertex approach, and is not used here.)

**Faithfulness check (numerics only, not a proof step).** Over $2000$ random balanced profiles for
$1\le n\le 5$, the optimal $\le n$-move DELETE/MATCH sequence attains $D\le u_nL$ with worst ratio
$D/u_nL=0.75$ — so the answer $u_n$ is achievable *within this finite move set*. This confirms the
reformulation loses nothing; the remaining task is a *profile-independent* uniform bound.

---

### 3. The upper bound by strong induction on $n$

**Theorem UB($n$).** Any profile of $m\le n+1$ pieces, sum $L$, admits a legal $\le n$-cut Xiang
response with $D\le u_nL$.

We prove UB($n$) by strong induction, with the balanced valley isolated as an explicit **GAP**.

**Base cases.**
- **UB($0$):** $m\le1$, no cuts, $D=a_1=L=u_0L$ (as $u_0=1/(2^1-1)=1$). Tight.
- **UB($1$):** $m\le2$. If $m\le1$, use the $m\le n$ reduction below ($D=0$). If $m=2$ then
  $a_1\ge L/2$ automatically, and there is *no balanced case*; Step 3.1–3.2 below close it
  ($a_1\le \tfrac23L$: whole-tail-peel $D=2a_1-L\le u_1L=L/3$; $a_1>\tfrac23L$: DELETE $a_1$,
  residual $a_2=L-a_1<L/3=u_1L$). Fully closed.

**Reduction $m\le n$ (short pieces).** If $m\le n$, DELETE every piece (bisect each; each pair
cancels by Lemma P), using $m\le n$ cuts; the reduced multiset is empty, so $D=0\le u_nL$. Hence
*the upper bound is nontrivial only for $m=n+1$ (full budget)*, which we assume from here.

Fix $n\ge2$, $m=n+1$, and assume UB($k$) for all $k<n$. Sort $a_1\ge\cdots\ge a_{n+1}$, sum $L$.
Split on $a_1$ into four **disjoint, exhaustive** cases.

**Step 3.1 — Dominant, dyadic-heavy: $a_1\ge c(n)L$.** DELETE $a_1$ (one cut). The residual is
$\{a_2,\dots,a_{n+1}\}$: $\le n$ pieces, sum $L-a_1$, with $n-1$ cuts left — a full-budget level
$(n-1)$ instance. By UB($n-1$), Xiang forces
$$D\le u_{n-1}\,(L-a_1)\le u_{n-1}\,\big(1-c(n)\big)L=u_nL,$$
where the last equality is the exact identity
$$u_{n-1}\big(1-c(n)\big)=\frac1{2^n-1}\cdot\frac{2^{n+1}-1-2^n}{2^{n+1}-1}
=\frac1{2^n-1}\cdot\frac{2^n-1}{2^{n+1}-1}=\frac1{2^{n+1}-1}=u_n. \tag{3.1}$$

**Step 3.2 — Dominant, sub-dyadic: $L/2\le a_1<c(n)L$.** Lemma WHOLE-TAIL-PEEL (certified,
$k=n$, $m=n+1\le n+1$) applies verbatim: $\le n$ cuts force $D=2a_1-L$, and $2a_1-L\le u_nL$
exactly because $a_1\le c(n)L=(1+u_n)L/2$. $\square$

**Step 3.3 — Balanced, second piece heavy: $a_1<L/2$ and $a_2\ge\beta_nL$.** Apply MATCH$(a_1,a_2)$
(one cut; degenerate free cancel if $a_1=a_2$). The residual is
$R=\{a_1-a_2,\ a_3,\dots,a_{n+1}\}$: exactly $n$ pieces (full budget for level $n-1$), sum
$L-2a_2$, with $n-1$ cuts left. By UB($n-1$),
$$D=D(R)\le u_{n-1}\,(L-2a_2)\le u_{n-1}\,(L-2\beta_nL)=u_nL,$$
using $a_2\ge\beta_nL$ (monotone: $u_{n-1}(L-2a_2)$ decreases in $a_2$) and the exact identity
$$u_{n-1}\,(1-2\beta_n)=\frac1{2^n-1}\cdot\frac{2^{n+1}-1-2^n}{2^{n+1}-1}
=\frac1{2^n-1}\cdot\frac{2^n-1}{2^{n+1}-1}=u_n, \tag{3.3}$$
since $1-2\beta_n=1-\tfrac{2^n}{2^{n+1}-1}=\tfrac{2^n-1}{2^{n+1}-1}$. (Verified exactly for
$2\le n\le7$: $u_{n-1}(1-2\beta_n)=u_n$.) $\square$

**Step 3.4 — Balanced valley: $a_1<L/2$ and $a_2<\beta_nL$ — GAP U-VALLEY.** This is the sole
uncovered case and the genuine open crux (see §5).

Cases 3.1–3.4 are disjoint (split by $a_1\ge c(n)L$ / $L/2\le a_1<c(n)L$ / $a_1<L/2$, the last
subdivided by $a_2$ vs $\beta_nL$) and exhaust every $m=n+1$ profile. Hence, **modulo GAP
U-VALLEY**, UB($n$) holds for all $n$.

---

### 4. Lower bound — reuse shared machinery (imported, unchanged)

Liu plays the dyadic profile $\mathcal D_n=\{2^n,\dots,2,1\}/(2^{n+1}-1)$. Case A (top piece
uncut $\Rightarrow D\ge u_n$) is certified. Case B (top piece cut) is **GAP L**, attacked by
`induction-peel` / `parity-measure-potential` via the gap-interleaving telescoping; this approach
imports whichever GAP L closure certifies first and contributes nothing new to the lower bound.

---

### 5. Assembly and honest gap statement

By Lemma R the game is the scalar minimax of $D$. Upper bound: §3 forces $D\le u_nL$ on every
profile **except** the balanced valley $\{a_1<L/2,\ a_2<\beta_nL\}$ (GAP U-VALLEY). Lower bound:
dyadic construction (Case A certified + imported GAP L). Together they give minimax $D=u_n$ and
$c(n)=(1+u_n)/2=2^n/(2^{n+1}-1)$ — **conditional on GAP U-VALLEY and GAP L**.

**GAP U-VALLEY (the crux of this approach, stated honestly).** Balanced full-budget profiles with
$a_2<\beta_nL$ ($\beta_n\downarrow1/4$). Numerically the DELETE/MATCH optimum still gives
$D\le u_nL$ here (worst observed ratio $0.75$), so the target is true and *reachable within the
move set*; what is missing is a **profile-independent** choice of $\le n$ moves. The obstruction is
sharp and refutes every simple deterministic rule (all tested this round, worst $D/u_nL$ over
$1\le n\le8$ balanced profiles):
- "always MATCH the top two": $4.23$;
- "always DELETE $a_1$": $25.5$;
- "MATCH top two if $a_2\ge\beta_nL$ else DELETE $a_1$": $10.7$.

So no single-rule / monotone descent works: the optimal move sequence is genuinely adaptive and
$V$ has interior valleys (as flagged). Closing GAP U-VALLEY requires either (a) an adaptive
potential that certifies a good move exists at *every* balanced valley profile, or (b) importing
the breakpoint-vertex finiteness theorem VERT to finitize the search and then a uniform vertex
bound. This approach's rigorous new content is the reduction of §2–§3 (the DELETE/MATCH game and
the four-case split, closing everything but the valley), not the valley itself.

## Approaches tried
- (round 3, new) SMOOTH monotonicity of $V$ along dyadic-ward exchange — REFUTED ($V$ has interior
  valleys; global concavity false). Discarded.
- (round 5 plan) D-DICHOTOMY simultaneous even-pairing / whole-tail regime split — not built; its
  regime (i) "single small leftover $\rho\le u_nL$" is refuted as a *reduce-to-one-piece* strategy
  (min nested-difference ratio up to $28\times u_n$ on balanced), so a single forced leftover does
  NOT bound $D$; superseded by the DELETE/MATCH game below (which does *not* reduce to one piece).
- (round 6, REBUILT) Recast the upper bound as the finite DELETE/MATCH reduction game (Lemma DM,
  rigorous via Lemma P). Proved UB($0$), UB($1$) fully; proved the strong-induction step on all
  four cases EXCEPT the balanced valley $a_2<\beta_nL$: dominant $a_1\ge c(n)L$ via DELETE-then-
  UB($n-1$) with the exact identity (3.1); sub-dyadic $L/2\le a_1<c(n)L$ via certified whole-tail-
  peel; balanced-heavy $a_1<L/2,\,a_2\ge\beta_nL$ via MATCH-top-two-then-UB($n-1$) with the exact
  identity (3.3). Verified thresholds exactly ($u_{n-1}(1-c(n))=u_{n-1}(1-2\beta_n)=u_n$). The
  balanced valley remains the labeled open GAP U-VALLEY; confirmed every simple deterministic rule
  fails there (ratios 4.2–25.5), so it needs an adaptive argument or VERT finitization.

## Current best
The answer $c(n)=2^n/(2^{n+1}-1)$, minimax $D=u_n$ (shared). New this round: the upper bound is a
**finite DELETE/MATCH reduction game** (Lemma DM), and a clean four-case strong-induction closing
everything except the balanced valley $\{a_1<L/2,\ a_2<\beta_nL\}$, with all three non-valley
cases proved by exact identities (3.1)/(3.3)/whole-tail-peel. This replaces the refuted subset-cover
and the refuted global-concavity smoothing with a genuine profile-independent D-tracking move set.
Only obstruction left in this approach: GAP U-VALLEY (adaptive; every simple rule refuted) and the
imported GAP L (lower bound).

## Open gaps
- **GAP U-VALLEY:** balanced full-budget profiles with $a_2<\beta_nL$ ($\beta_n=2^{n-1}/(2^{n+1}-1)$).
  Uniform $\le n$-move DELETE/MATCH bound $D\le u_nL$ is true numerically but not proved
  profile-independently; the optimal sequence is adaptive (all deterministic single-rules refuted).
- **GAP L (imported):** lower-bound Case B; closed elsewhere, imported when certified.

## Promotable lemmas
- **Lemma DM (elementary Xiang reductions).** In the cutting game, from any current multiset $S$
  Xiang can, with one mark, either DELETE a piece $x$ ($D(S)\mapsto D(S\setminus\{x\})$, via
  bisecting $x$ and cancelling by Lemma P) or MATCH two pieces $x>y>0$
  ($D(S)\mapsto D((S\setminus\{x,y\})\cup\{x-y\})$, via marking $x$ at offset $y$ and cancelling
  by Lemma P); equal pieces cancel at zero cost. Proved in §2 (self-contained given certified
  Lemma P). Reusable by any approach as the exact D-tracking upper-bound move set.
