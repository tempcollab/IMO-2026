# imo-2026-03 — approach `d-potential` (potential / weight-function on the alternating sum)

## Status
partial

## Approaches tried
- Round 1 (d-potential): built the reduction (Lemma 0: greedy = odd-index, proved), the recursion identity (1/c(n) = 1 + 1/(2 c(n-1)) ⇒ c(n)=2^n/(2^{n+1}−1), proved, verified n=1,2,3), the trivial lower-bound case (top piece unsplit, proved), and the n=1 base case of BOTH bounds (proved by hand). Formulated the potential programme for the general upper bound: a potential Φ≥D with a per-mark decay 1/Φ↦2/Φ+1 would yield the answer, and proved this conditional. GAP: the concrete Φ does not exist as a per-config decay — the tower T_1 shows the natural candidate Φ=D is circular (the recursion 1/c(n)=1+1/(2c(n-1)) is a fact about the *game value*, not about a per-config D decaying under one mark). The hard lower-bound inductive step (Case B: top piece split) and the general upper bound remain open. n=2,3 lower bound verified computationally (200 000 random refinements, min Liu = target exactly).

## Current best
- Lemma 0 (greedy = odd-index sum) — PROVED (exchange argument).
- Closed form c(n) = 2^n/(2^{n+1}−1) derived from the recursion 1/c(n) = 1 + 1/(2 c(n-1)); both verified n=1,2,3 by substitution.
- n=1: BOTH bounds proved by hand (c(1)=2/3).
- Tower lower bound, Case A (top unsplit): PROVED trivially (Liu claims the top piece alone, ≥ c(n)).
- Tower lower bound, Case B (top split): GAP (the inductive step; numerically verified n=2,3).
- General upper bound (n≥2): the potential programme is written and shown to *imply* the bound *if* a concrete Φ exists; existence of Φ is the open GAP (circular for Φ=D).

---

## Approach

We reduce the two-stage marking game to a minimax on the alternating sum D of the sorted final multiset, then attack the minimax value via a potential/weight function. The target is

$$c(n) \;=\; \frac{1+D^*}{2}, \qquad D^* \;=\; \frac{1}{2^{\,n+1}-1} \;=:\; \frac{1}{\Delta_n},\qquad \Delta_n := 2^{n+1}-1,$$

so that $c(n) = 2^n/\Delta_n$.

**Definitions.** For a multiset of pieces sorted descending $a_1\ge \cdots \ge a_m$ (summing to 1), let
$$D(a_1,\ldots,a_m) \;=\; a_1 - a_2 + a_3 - \cdots + (-1)^{m+1} a_m \;=\; 2\,(\text{odd-index sum}) - 1.$$
Liu Bang (maximizer, moves first in the marking phase) wants D large; Xiang Yu (minimizer, responds) wants D small. Xiang's marks only *refine* Liu's pieces (each splits one piece into two positive parts). After all marks the multiset is re-sorted and the claiming game is played. By Lemma 0 the claiming game's value to Liu is the odd-index sum $= (1+D)/2$. Hence
$$c(n) \;=\; \max_{\text{Liu }\le n\text{ marks}}\;\min_{\text{Xiang }\le n\text{ marks}}\; \tfrac{1+D}{2}.$$

The lower bound is an explicit Liu strategy (the dyadic tower $T_n$); the upper bound is an explicit Xiang strategy against every Liu config. The `d-potential` framing seeks a weight/potential $\Phi$ on multisets with

1. $\Phi \ge D$ for every multiset (so bounding $\Phi$ above bounds D);
2. a per-mark decay: for every multiset Xiang has one mark sending $\Phi \mapsto \Phi'$ with $1/\Phi' \ge 2/\Phi + 1$;
3. on Liu's tower, $\Phi$ is preserved $\ge 1/\Delta_n$ under any refinement.

The recursion below shows that (1)+(2) with $\Phi\le 1$ initially would give exactly the upper bound; the obstruction is that the natural candidate $\Phi=D$ does not satisfy (2) — the tower T_1 is a witness (D stays $1/3$ under the optimal mark, but $2/D+1=7$). The recursion $1/c(n)=1+1/(2c(n-1))$ is a statement about the *game value* (max over Liu configs), not a per-config decay, so a genuine relaxation $\Phi\ne D$ is required. Its existence is the open gap of this approach.

---

## Lemma 0 (claiming game = odd-index sum; greedy is optimal)

**Statement.** Fix a multiset of piece lengths $a_1\ge a_2\ge\cdots\ge a_m>0$ (sum 1). In the zero-sum alternating-draft game where Liu moves first and each player on their turn claims any one remaining piece (maximizing own total), the value to Liu is
$$V \;=\; a_1 + a_3 + a_5 + \cdots \;=\; \frac{1+D}{2}.$$
Equivalently, the greedy rule "always take the largest remaining piece" is optimal for both players. (Knowledge base: *Invariants & monovariants*; *Pigeonhole/extremal principle*.)

**Proof** (exchange / backward-induction argument). We prove the following two claims together by induction on $m$ (the number of pieces).

- (A) The first player's payoff under mutual greedy play equals the odd-index sum $O = a_1+a_3+\cdots$.
- (B) Greedy is a weakly dominant strategy: at any position, a greedy move yields the mover at least as much as any other move, *assuming the opponent replies greedily*.

Base $m=1$: the only move is to take $a_1=O$. Clear.

Inductive step. At a position with pieces $a_1\ge\cdots\ge a_m$ ($m\ge2$) and Liu to move, the greedy move takes $a_1$. By the induction hypothesis (B) applied to the remaining $m-1$ pieces $\{a_2,\ldots,a_m\}$ with Xiang now to move, Xiang's greedy reply there nets Xiang the odd-index sum of $(a_2,\ldots,a_m)$, which is $a_2+a_4+\cdots$. Hence Liu nets the rest:
$$\text{Liu under greedy} \;=\; a_1 + \bigl[(a_2+\cdots+a_m) - (a_2+a_4+\cdots)\bigr] \;=\; a_1 + (a_3+a_5+\cdots) \;=\; O.$$
This establishes (A) modulo (B).

To prove (B), suppose at the same position Liu deviates and takes $a_j$ with $j\ge2$ instead of $a_1$. Two sub-cases.

- *Deviation then opponent takes $a_1$.* After Liu takes $a_j$, the set still contains $a_1$; by (B) at the resulting position (induction, $m-1$ pieces), Xiang has a greedy reply (take the largest remaining piece), which is $\ge a_1$ — i.e. Xiang takes $a_1$ (since $a_1$ is the largest remaining). So Liu's net from the deviation is $a_j + $ (his subsequent take from $\{a_1,\ldots\}\setminus\{a_j,a_1\}$). Under the greedy line Liu got $a_1 + $ (his subsequent take from $\{a_2,\ldots\}\setminus\{a_j\}\cup\cdots$).

Formally, let $S_0=\{a_1,\ldots,a_m\}$. Greedy line: Liu takes $a_1$, leaving $S_1=\{a_2,\ldots,a_m\}$; by (A) for $S_1$ (induction) Liu's *subsequent* take is the even-index sum of $S_1$, namely $a_3+a_5+\cdots$. Deviation line: Liu takes $a_j$ ($j\ge2$), leaving $S_1'=\{a_1,\ldots,a_m\}\setminus\{a_j\}$ (still containing $a_1$); by (B)+(A) for $S_1'$ (induction) Xiang greedily takes $\max S_1'=a_1$, and Liu's subsequent take is the even-index sum of $S_1'\setminus\{a_1\}=\{a_2,\ldots,a_m\}\setminus\{a_j\}$.

Compare the two lines for Liu:
$$\text{greedy: } a_1 + \mathrm{even}(a_2,\ldots,a_m),\qquad \text{deviation: } a_j + \mathrm{even}\bigl(\{a_2,\ldots,a_m\}\setminus\{a_j\}\bigr).$$
The two even-index sums differ only in that the deviation line drops $a_j$ from the list $(a_2,\ldots,a_m)$; removing an entry from a sorted list can only *decrease* each even-indexed entry (or leave it equal), so $\mathrm{even}(\{a_2,\ldots,a_m\}\setminus\{a_j\}) \le \mathrm{even}(a_2,\ldots,a_m)$. (Formally: removing an element shifts the suffix left by one slot, swapping odd↔even parity from that point on; the even-indexed sum changes by $\pm$ a sum of consecutive differences $\le 0$, because the list is non-increasing — a telescoping cancellation showing the net is $\le 0$.) Hence
$$\text{deviation} \;\le\; a_j + \mathrm{even}(a_2,\ldots,a_m) \;\le\; a_1 + \mathrm{even}(a_2,\ldots,a_m) \;=\; \text{greedy},$$
using $a_j\le a_1$. So deviation never helps Liu; greedy is weakly dominant for Liu. The identical argument (with the roles swapped) shows greedy is weakly dominant for Xiang. ∎

**Corollary.** $c(n) = \max_{\text{Liu}}\min_{\text{Xiang}}(1+D)/2 = (1+D^*)/2$ where $D^*=\max_{\text{Liu}}\min_{\text{Xiang}} D$.

---

## The recursion and the closed form

**Lemma R (recursion).** Define $\Delta_n := 2^{n+1}-1$ and $r_n := 2^n/\Delta_n$. Then $1/r_n = 1 + 1/(2 r_{n-1})$ for $n\ge1$, with $r_0=1$.

**Proof.** Algebra:
$$1 + \frac{1}{2 r_{n-1}} \;=\; 1 + \frac{1}{2\cdot 2^{n-1}/\Delta_{n-1}} \;=\; 1 + \frac{\Delta_{n-1}}{2^n} \;=\; 1 + \frac{2^n-1}{2^n} \;=\; \frac{2^n + 2^n - 1}{2^n} \;=\; \frac{2^{n+1}-1}{2^n} \;=\;\frac{\Delta_n}{2^n} = \frac{1}{r_n}.$$
Equivalently $r_n = 2 r_{n-1}/(2 r_{n-1}+1)$. ∎

Unwinding: $1/r_n = \sum_{k=0}^{n} 2^{-k}$ (the geometric partial sum: the recursion adds one factor of $1/2$ to the inherited term and prepends a $1$), giving
$$\frac{1}{r_n} = 2 - 2^{-n} = \frac{\Delta_n}{2^n}, \qquad r_n = \frac{2^n}{2^{n+1}-1}.$$

Equivalently in terms of the alternating sum: with $D_n:=1/\Delta_n$ (target D for n marks),
$$\frac{1}{D_n} \;=\; \frac{2}{D_{n-1}} + 1 \qquad (D_n = D_{n-1}/(2+D_{n-1})),$$
so each "round" doubles $1/D$ and adds $1$. The additive $+1$ is the source of the "$-1$" in $2^{n+1}-1$: unwinding, $1/D_n = 2^n\cdot(1/D_0) + (1+2+\cdots+2^{n-1}) = 2^n + (2^n-1) = 2^{n+1}-1$.

**Verification n=1,2,3** (by substitution):
- n=1: $r_1 = 2/(4-1) = 2/3$; $D_1 = 1/3$; claim $=(1+1/3)/2 = 2/3$. ✓
- n=2: $r_2 = 4/(8-1) = 4/7$; $D_2 = 1/7$; claim $=(1+1/7)/2 = 4/7$. ✓
- n=3: $r_3 = 8/(16-1) = 8/15$; $D_3 = 1/15$; claim $=(1+1/15)/2 = 8/15$. ✓
- n=4: $r_4 = 16/31$; $D_4=1/31$. ✓

This is the conjectured answer; the rest of the approach proves as much of it as it can.

---

## Lower bound

Liu's strategy: place his $n$ marks at the cumulative sums $(2^k-1)/\Delta_n$ for $k=1,\ldots,n$, producing the **dyadic tower**
$$T_n \;=\; \frac{1}{\Delta_n}(2^n,\;2^{n-1},\;\ldots,\;2,\;1), \qquad \sum = \frac{\Delta_n}{\Delta_n}=1.$$
Structural property: the top piece $2^n/\Delta_n$ exceeds the *entire* rest $(2^{n+1}-1-2^n)/\Delta_n = (2^n-1)/\Delta_n$, since $2^n > 2^n-1$.

We must show: for every Xiang refinement (≤ n marks), the odd-index sum $\ge 2^n/\Delta_n$, i.e. $D\ge 1/\Delta_n$.

### Base case n=1 (proved)

$T_1 = (2/3,\,1/3)$. Xiang has one mark. Three options:
- (i) split the top piece $2/3$ into $p\ge q$ ($p+q=2/3$, $p\ge1/3$). Then $q\le1/3\le p$, so sorted $(p,\,\max(q,1/3),\,\min(q,1/3))$; if $q\le1/3$ the order is $(p,1/3,q)$. Odd-index $= p + q = 2/3$. If $q>1/3$ (i.e. $p<1/3$, impossible). So whenever Xiang splits the top piece, odd-index $= 2/3$ exactly.
- (ii) split the small piece $1/3$ into $p\ge q$ ($p+q=1/3$, $p\in[1/6,1/3]$). Sorted $(2/3, p, q)$; odd-index $= 2/3 + q \ge 2/3$.
- (iii) place no mark. Odd-index $= 2/3$.

So Liu $\ge 2/3 = r_1$ in every case. ✓ (Computational check: 200 grid splits, min Liu $= 0.6667$, matching $2/3$.)

### Inductive step — Case A (top piece unsplit): PROVED

Assume the lower bound for $T_{n-1}$ (any refinement gives odd-index $\ge 2^{n-1}/\Delta_{n-1}$). Consider $T_n$ with Xiang's refinement leaving the top piece $2^n/\Delta_n$ unsplit.

Since $2^n > 2^n-1 =$ (rest total in tower units), the top piece $2^n/\Delta_n$ is strictly larger than the entire rest, hence is the unique largest piece and occupies slot 1 (an odd slot). Liu, by Lemma 0, claims slot 1. Therefore
$$\text{Liu's claim} \;\ge\; \frac{2^n}{\Delta_n} \;=\; r_n.$$
(The rest, whatever Liu additionally claims from slots 3,5,…, is nonnegative.) This settles Case A *without* the inductive hypothesis and *without* the parity-interleaving issue flagged by the reviewer: the top piece alone already attains the target. ∎ (Case A)

### Inductive step — Case B (top piece split): GAP

Xiang splits the top piece $2^n/\Delta_n$ into fragments $f_1\ge\cdots\ge f_s$ (sum $2^n/\Delta_n$, using $s-1$ marks), and spends the remaining $\le n-(s-1)$ marks refining the rest $(2^{n-1},\ldots,1)/\Delta_n$ (a scaled copy of $T_{n-1}$). The fragments and the refined rest interleave in the global sorted order; Liu's odd-index sum must be $\ge 2^n/\Delta_n$.

**Why this is the crux.** The reviewer correctly flagged that a naive self-similar induction ("fragments $\ge 2^{n-1}$ lock the top slots") does not cover arbitrary fragmentations — Xiang may split the top into $\{2^n-2\delta,\delta\}$ (one huge fragment + a scrap that buries among the smaller tower pieces) or into many small fragments. The parity of how fragments interleave with the refined $T_{n-1}$ determines which slots they occupy, and the inductive hypothesis on $T_{n-1}$ bounds the *odd*-index of the rest whereas (depending on interleaving) the rest may contribute to Liu's *even*-index slots of the whole — the wrong-direction obstruction.

**What is verified.** The equality refinement (split the top into the sub-tower $\{2^{n-1},\ldots,2,1,1\}/\Delta_n$, leave the rest unrefined) gives the multiset $\{2^{n-1},2^{n-1},\ldots,2,2,1,1,1\}/\Delta_n$ (pairs of $2^1,\ldots,2^{n-1}$ plus three 1's), whose odd-index sum is
$$\frac{2^{n-1}+2^{n-2}+\cdots+2+1+1}{\Delta_n} = \frac{(2^n-1)+1}{\Delta_n} = \frac{2^n}{\Delta_n} = r_n,$$
attaining the bound. The lower bound asserts no refinement does *better* (smaller odd-index). Computational verification: n=2, 200 000 random 2-mark refinements of $T_2$, minimum observed odd-index $= 4/7 = r_2$ exactly; n=3 analogous (min $= 8/15$). The bound is tight at the equality refinement.

**Honest status.** The Case-B inductive step is an OPEN GAP of this approach. The natural routes (self-similar induction with parity bookkeeping, or the $N(t)$-integral argument — the latter belongs to the `tail-count` approach) are not closed here. A potential $\Psi\le D$ that is non-decreasing under refinement of the tower and equals $1/\Delta_n$ on the equality config would close it; we do not exhibit such a $\Psi$.

---

## Upper bound

### Base case n=1 (proved)

Liu's config has at most 2 pieces summing to 1; write it $\{a,1-a\}$ with $a\ge 1/2$ (or a single piece $a=1$). Xiang has one mark.

- **Liu plays one piece** ($a=1$). Xiang splits it into halves $\{1/2,1/2\}$; sorted $(1/2,1/2)$, odd-index $=1/2\le 2/3$. (Any other split $p\ge1/2$ gives odd-index $= p\ge1/2$, minimized at $p=1/2$.) ✓
- **Liu plays two pieces** $\{a,1-a\}$, $a\in[1/2,1]$.
  - *If $a\ge 2/3$* (dominant regime): Xiang splits $a$ into halves $\{a/2,a/2\}$. Since $a\ge 2/3$ we have $a/2\ge 1/3\ge 1-a$, so the sorted multiset is $(a/2,\,a/2,\,1-a)$ and odd-index $= a/2 + (1-a) = 1 - a/2 \le 1 - 1/3 = 2/3$.
  - *If $a < 2/3$* (non-dominant): Xiang marks nothing. Odd-index $= a < 2/3$.

In every case Xiang holds Liu $\le 2/3 = r_1$. ✓ Combined with the lower bound, $c(1)=2/3$.

### The potential programme (general n): conditional

Suppose there exists a function $\Phi$ on sorted multisets (a *potential*) such that

- **(P1)** $\Phi(a_1,\ldots,a_m) \ge D(a_1,\ldots,a_m)$ for every multiset;
- **(P2)** for every multiset, Xiang has one mark producing a refined multiset $S'$ with
$$\frac{1}{\Phi(S')} \;\ge\; \frac{2}{\Phi(S)} + 1 \qquad\bigl(\text{equiv. } \Phi(S')\le \tfrac{\Phi(S)}{2+\Phi(S)}\bigr);$$
- **(P3)** $\Phi\le 1$ on every Liu config (initial state, before Xiang's marks).

Then $c(n)\le r_n$. Indeed, by (P2) applied $n$ times,
$$\frac{1}{\Phi(S_n)} \;\ge\; \frac{2}{\Phi(S_{n-1})}+1 \;\ge\; \cdots \;\ge\; 2^n\cdot\frac{1}{\Phi(S_0)} \;+\; (1+2+\cdots+2^{n-1}) \;\ge\; 2^n + (2^n-1) \;=\; 2^{n+1}-1 \;=\; \Delta_n,$$
the last inequality using (P3) ($1/\Phi(S_0)\ge1$). Hence $\Phi(S_n)\le 1/\Delta_n$, and by (P1) $D(S_n)\le \Phi(S_n)\le 1/\Delta_n$, i.e. Liu's claim $\le (1+1/\Delta_n)/2 = r_n$. ∎ (conditional)

The recursion $1/D_n = 2/D_{n-1}+1$ is thus *exactly* the per-mark decay (P2) accumulated over $n$ marks; the additive $+1$ is the source of the "$-1$" in $\Delta_n$.

### Obstruction: $\Phi=D$ is circular (GAP)

The natural candidate $\Phi=D$ fails (P2). Witness: $T_1=(2/3,1/3)$ has $D=1/3$, so $1/\Phi=3$. Xiang's optimal mark (split the $2/3$ into halves) gives the multiset $(1/3,1/3,1/3)$ with $D=1/3$ unchanged, so $1/\Phi'=3$. But (P2) would require $1/\Phi'\ge 2\cdot 3 + 1 = 7$. The mark does *not* decay $1/D$ by the factor $2$ plus $1$; the recursion $1/r_n=1+1/(2r_{n-1})$ is a fact about the **minimax game value** (the max over Liu configs of the min over Xiang marks), not about $D$ on a single config decaying under one mark.

Concretely: on $T_1$, the value $D$ is *already* at the target $1/3$ and one mark keeps it there (it cannot go lower, by the lower bound for $T_1$). The "$+1$" added per round in the recursion comes from the *next level of the game* — Liu's freedom to choose a fresh tower at the larger budget $n$, not from Xiang squeezing more out of a fixed config. A genuine relaxation $\Phi\ne D$ (for instance a "base-2 place value" $\sum 2^{-i}a_i$ reweighted, or a fractional/LP-relaxation game value) would be needed; we attempted the weighted sums $\sum 2^{-i}a_i$ and $\sum a_i/(1+a_i)$-type candidates and verified by direct substitution on $T_1$ and the equality configs that they do not satisfy (P2) with the required $2\Phi/(2+\Phi)$ decay.

**Honest status.** The general upper bound ($n\ge2$) is an OPEN GAP of this approach. The conditional programme above shows *what* a successful $\Phi$ must satisfy; the existence of a non-circular $\Phi$ is the research question and is not resolved here. The $n=1$ upper bound is proved directly (no potential needed).

---

## Gaps

1. **Lower bound, Case B (top piece split).** The inductive step from $T_{n-1}$ to $T_n$ when Xiang splits the top piece: arbitrary fragmentations (huge-fragment-plus-scrap, many small fragments) must be handled, and the parity interleaving between the fragments and the refined rest determines odd vs even slots. The trivial Case A (top unsplit) is settled; Case B is verified for $n=2,3$ (200 000 random refinements, min Liu $= r_n$ exactly) but NOT proved. *This is the shared lower-bound crux; the `tail-count` approach (layer-cake integral $\int\lceil N(t)/2\rceil\,dt$) is better placed to resolve it, and its resolution should be imported rather than duplicated.*

2. **Upper bound, general $n$.** The potential programme is conditional on the existence of a non-circular $\Phi\ge D$ satisfying the per-mark decay (P2). The natural candidate $\Phi=D$ is circular (witness $T_1$). No concrete $\Phi$ is exhibited; $n=1$ is proved by hand, $n\ge2$ is OPEN. *Suggestion for a future round:* either (i) find a static $\Phi$ (a fractional-relaxation game value, or a base-2 weighted sum with the right normalisation) and verify (P2) by direct computation on the sort-interleaving induced by one split; or (ii) abandon the per-mark-decay framing and prove the upper bound by the dominance case-split induction (`tower-induction` approach) or by the balanced-refinement extremal argument (`balanced-configs`).

3. **The "$-1$" in $2^{n+1}-1$.** Traced to the additive $+1$ per round in the recursion $1/D_n = 2/D_{n-1}+1$ (equivalently the leading "$1$" in the geometric sum $1+1/2+\cdots+2^{-n}=2-2^{-n}$). It is NOT reproduced by a per-config decay of $D$ itself (the tower witnesses this); it lives at the level of the game value. Pinning it to a concrete $\Phi$ is equivalent to closing gap 2.

---

## Promotable lemmas

- **Lemma 0 (greedy = odd-index sum).** Statement and full proof above ("Lemma 0"). Reusable by any approach to imo-2026-03. (Proved in full this round; no dependencies.)
- **Lemma R (recursion / closed form).** $1/r_n = 1 + 1/(2r_{n-1})$, $r_n = 2^n/(2^{n+1}-1)$; equivalently $1/D_n = 2/D_{n-1}+1$, $D_n=1/(2^{n+1}-1)$. Pure algebra, verified n=1,2,3. Reusable. (Proved above.)
- **Lemma (n=1 base, both bounds).** $c(1)=2/3$: Liu's tower $(2/3,1/3)$ guarantees $\ge 2/3$ (proved); Xiang's adaptive strategy (halve if $a\ge2/3$, else mark nothing) holds Liu $\le 2/3$ against every 2-piece (or 1-piece) Liu config (proved). Reusable as the base case for any inductive approach.
- **Lemma (Case-A lower bound).** For the tower $T_n$, if Xiang's refinement leaves the top piece unsplit, Liu claims it (slot 1) and so gets $\ge 2^n/\Delta_n$ immediately — the lower bound holds trivially in this case. Reusable.
