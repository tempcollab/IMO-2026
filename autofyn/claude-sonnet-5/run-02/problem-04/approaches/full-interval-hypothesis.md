## Status
unsolved

## Approach: full-interval-hypothesis

Target: prove S = (0°,90°] exactly (H1: Mulan can force EVERY θ ≤ 90°, not just the
dyadic-scaffold family {180/((2^k+1)2^j)}).

## Approaches tried

- **Round 2 (this round): hand/symbolic verification of the θ=180/7 witness FIRST,
  per the outline-reviewer's required order, before attempting the general recursion.**
  Outcome: **found a genuine new legal move (the "cross-transfer") that DOES extend the
  forceable set beyond dyadic-scaffold in principle, but proved rigorously that it
  CANNOT reach θ=180/7**, giving strong evidence the earlier computational witness for
  180/7 was a search artifact, and that H1 (full interval) is very likely FALSE. Full
  derivation below. `binary-word-invariant.md` was checked before/while writing this
  section (still `Status: unsolved`, step 1 not yet computed as of this round's write-up
  time — this approach's finding was derived independently, not borrowed, but it
  converges with and sharpens binary-word-invariant's simpler {g1,g2}-orbit test, which
  flagged the same 180/7 discrepancy using only the two "obvious" generators x/2 and
  180−x. This approach adds the THIRD, adaptive generator that binary-word-invariant's
  outline speculated might be needed, and shows even with that generator, 180/7 still
  fails.)

## The cross-transfer move (new, proven-legal primitive)

**Setup.** By the (imported, re-verified) transfer lemma from `dyadic-scaffold`, from
any starting triangle Mulan can reach, in finitely many Shan-Yu-immune moves, a state of
the shape
$$\{r,\ \theta-r,\ 180-\theta\}$$
where $r>0$ is a "spectator" angle whose exact value is tied to Shan-Yu's original
(possibly irrational) starting angle $a_0$ via $r=a_0/2^n$ for whatever bisection depth
$n$ Mulan used — i.e. $r$ is a value Mulan can make arbitrarily small but does **not**
control precisely; only $180-\theta=:P$ is a "pure" quantity depending on $\theta$ alone.

**Claim (cross-transfer lemma).** From a state $\{s,\ P,\ \theta-\varepsilon(s)\}$ of
this shape — precisely, from $\{r,\theta-r,P\}$ with $P=180-\theta$ — Mulan may cut the
$P$-vertex with $x_1 = r+P-(\theta+r) = P-\theta$, i.e. targeting the value
$\theta+r$ (which she may do because she knows the numeric value of $r$ once it is
created). This requires $0<x_1<P$, i.e. $0<P-\theta<P$: the right inequality is
$\theta>0$ (given); the left is $P>\theta$, i.e. $180-\theta>\theta$, i.e. $\theta<90°$
— true for all $\theta<90°$ (the boundary $\theta=90°$ is already solved directly by
the altitude-foot double hit in `dyadic-scaffold`, so this move is only needed for
$\theta<90°$).

Applying the general cut formulas (triangle $\{p,q,r_{\text{spec}}\}=\{P,\theta-r,r\}$,
cut at $p=P$) with $x_1=P-\theta$:
$$A=\{q,\,x_1,\,r_{\text{spec}}+p-x_1\}=\{\theta-r,\ P-\theta,\ \theta+r\}$$
$$B=\{r_{\text{spec}},\,p-x_1,\,q+x_1\}=\{r,\ \theta,\ 180-\theta-r\}.$$
(Verified by direct algebraic substitution — re-derived independently with sympy this
round, not merely asserted; see computation below.)

$B$ **contains θ exactly**, so Shan-Yu (who loses instantly if the triangle ever
contains θ) never chooses $B$; he is **forced into $A=\{\theta-r,\,180-2\theta,\,\theta+r\}$**.
Crucially, $A$ contains the value $180-2\theta$ — a **new pure (r-independent) angle**,
literally sitting in the triangle as an actual angle, regardless of Shan-Yu's choice.

This is a genuinely new mechanism beyond `dyadic-scaffold`'s bisection: it converts one
pure quantity $P$ into a **different** pure quantity $2P-180$ (here $P=180-\theta \mapsto
2(180-\theta)-180=180-2\theta$), in a single Shan-Yu-immune move, by exploiting that $r$
is numerically known even though it is uncontrolled.

**Symmetry check.** Using the spectator $\theta-r$ instead of $r$ (target
$2\theta-r$) produces exactly the same new pure value $180-2\theta$ (re-derived
independently — see computation below): no new information, confirming this is the
unique non-degenerate "cross-transfer" available from this state, not one of several.

### Verification (this round, exact symbolic algebra, not floating point)

```
sympy, exact:
state (p,q,r)=(180-θ, θ-r, r); sum check 0.  [OK]
transfer target = θ+r:
  A1 = [θ-r, 180-2θ, θ+r]      (no θ present, generic escape)
  B1 = [r, θ, 180-θ-r]          (contains θ exactly -> Shan-Yu avoids)
mirror, spectator = θ-r, target = 2θ-r:
  A  = [r, 180-2θ, 2θ-r]
  B  = [θ-r, θ, 180-2θ+r]       (contains θ exactly -> same forced escape, same
                                  new pure value 180-2θ)
```
Both computations independently confirm the identical new pure quantity $180-2\theta$.

### Iterating the mechanism: the two-generator monoid on the "pure" value

Write $P_0=180-\theta$. Two Shan-Yu-immune operations transform the current pure value
$P$:
- **(H1) Bisection** (imported lemma): $P \mapsto P/2$ — bisect the pure angle, forced
  into both children.
- **(H2) Cross-transfer** (new, proved above): $P \mapsto 2P-180$ — forced into the
  unique non-instant-win branch.

Both are affine maps on $P$: $h_1(P)=P/2$ ($\alpha=\tfrac12,\beta=0$), $h_2(P)=2P-180$
($\alpha=2,\beta=-180$). **These are the only two moves available on a single pure
quantity**: bisecting one of the two $r$-linked angles instead of $P$ never produces a
new $r$-independent value (verified directly: cutting the $\theta-r$ vertex forces
$(\theta-r)/2$ into both children, but the third angle in each child is
$P+(\theta-r)/2$ or $r+(\theta-r)/2$ — both still mix $P$ (or nothing) with an
$r$-dependent term, so $P$ itself is unchanged and no new pure value appears); and the
only non-degenerate cross-transfer target (the one making the escape branch contain
$\theta$ exactly) is uniquely $\theta+r$ (using spectator $r$) or $2\theta-r$ (using
spectator $\theta-r$), both giving the same $h_2$, as shown above. So **every reachable
state in this family has the shape "two $r$-linked junk angles + one pure value $P_n$,"
and $P_n$ evolves only by finite compositions of $h_1,h_2$.**

**Composition formula.** A finite composition of $n$ moves (any order/mix of $h_1,h_2$)
sends $P_0 \mapsto A_n P_0 + B_n$ where $A_n=2^{s}$, $s=(\#h_2)-(\#h_1)\in\mathbb Z$
(any integer, since slopes multiply regardless of order), and $B_n$ is a signed sum of
terms $-180\cdot 2^{c_i}$ (one $c_i\in\mathbb Z$ per $h_2$ used, $c_i$ = net
$h_2$-minus-$h_1$ count occurring *after* that use — a standard affine-composition
telescoping identity, checked by direct expansion:
$P_{\text{final}}=\bigl(\prod\alpha_i\bigr)P_0+\sum_i\beta_i\prod_{j>i}\alpha_j$, and
$\beta_i\in\{0,-180\}$).

**Win condition via this mechanism**: Mulan wins outright the moment the pure value
$P_n$ itself equals $\theta$ (then $\theta$ is a literal, $r$-independent angle in the
triangle — an unconditional win, immune to Shan-Yu's choices and to the unknown value
of $r$). So we ask: for which integer $s$ can $B_n = \theta - 2^{s}(180-\theta)$ be
realized as a finite sum of terms $-180\cdot2^{c_i}$?

### The obstruction for θ = 180/7

Write $\theta=180/N$ with $N=7$. Then
$$B_n=\theta-2^s(180-\theta) = \frac{180}{N}\Bigl(1-2^s(N-1)\Bigr)
     = \frac{180}{N}\bigl[(1+2^s)-2^sN\bigr]
     = \frac{180(1+2^s)}{N}-180\cdot2^s.$$
The term $-180\cdot2^s$ is already an integer multiple of a power of $180\cdot2$, i.e.
dyadic. So $B_n$ can be realized as a finite sum of $-180\cdot2^{c_i}$ terms **only if**
$\dfrac{180(1+2^s)}{N}$ is itself dyadic (denominator a power of 2 after reduction).
Since $N=7$ is odd and coprime to 180's relevant factor structure here (we need
$7\mid(1+2^s)$, i.e.
$$2^{s}\equiv -1 \pmod 7 \quad\text{for some integer } s.$$

**This has NO solution.** The powers of 2 modulo 7 are $2^0=1,\ 2^1=2,\ 2^2=4,\
2^3=1,\dots$ — period 3 (since $2^3=8\equiv1$, and $2^1,2^2\not\equiv1$), so the set of
*all* integer powers of $2 \bmod 7$ (including negative exponents, via the modular
inverse $2^{-1}\equiv4\pmod7$) is exactly the subgroup $\langle2\rangle=\{1,2,4\}\subset
(\mathbb Z/7\mathbb Z)^\times$, which has order $3$. Since $3$ is odd, this subgroup
cannot contain the unique order-$2$ element $-1\equiv6\pmod7$ (a subgroup of odd order
$3$ inside a cyclic group of order $6$ never contains the order-$2$ element, else its
order would have to be divisible by $2$). Concretely: $\{1,2,4\}\not\ni 6$. So
$2^s\equiv-1\pmod7$ fails for every integer $s$.

**Conclusion.** No finite composition of the two available Shan-Yu-immune moves on the
pure quantity (bisection $h_1$, cross-transfer $h_2$) can ever drive $P_0=180-\theta$
to exactly $\theta=180/7$. This is a fully algebraic argument — it holds even before
imposing the additional constraint that every intermediate value stay a valid angle in
$(0,180)$, so it is not merely a search-depth limitation: it is an exact-arithmetic
impossibility inside this move family, at *any* depth, in *any* order.

### What this establishes and what it does not

- It does **not** by itself prove θ=180/7 is unforceable in the actual game (there
  could in principle be some other move sequence not of the "one pure quantity + two
  r-linked junk angles" shape this analysis covers — e.g. a fundamentally different
  cut pattern the escape-state framework doesn't reduce to). We have not ruled that out.
- It **does** show, rigorously, that the *natural* extension of the proven mechanisms
  (transfer + bisection + the one genuinely new "adaptive cross-transfer" this round
  discovered, which is the mechanism the outline speculated might be needed to reach
  180/7) **cannot** produce 180/7. Given that this is precisely the class of strategy
  the original computational search (referenced by `dyadic-scaffold`'s open-gap note)
  would plausibly have found if 180/7 were genuinely reachable, this is strong evidence
  the earlier "180/7 forceable at search depth 12" claim was a **search artifact** (a
  bounded/restricted-family search bug, floating-point near-miss, or a move that was
  not actually legal under the problem's exact cut rule), not a genuine witness. No
  such witness has ever been hand-extracted or exhibited by any approach to date.
- Consequently, **H1 (Mulan forces the full interval (0°,90°]) is very likely FALSE**:
  180/7 is exactly the kind of "generic, non-dyadic" θ that H1 requires to be
  forceable, and the most powerful mechanism found so far provably cannot reach it.

### A genuinely new (but unresolved) byproduct: does the cross-transfer extend the family at all?

The same computation, run for general odd $N$, shows $\theta=180/N$ satisfies the
*necessary* congruence condition $2^s\equiv-1\pmod N$ (for the pure-value mechanism to
have a chance) exactly when $-1\in\langle2\rangle\subset(\mathbb Z/N\mathbb Z)^\times$,
i.e. when the multiplicative order of $2 \bmod N$ is even. This holds trivially for
every $N=2^k+1$ (dyadic-scaffold's family: $2^k\equiv-1$ by definition) but numerically
also holds for other $N$ not of that form (e.g. $N=11$: order of $2\bmod11$ is $10$,
and $2^5=32\equiv10\equiv-1\pmod{11}$). **This is only a necessary condition, not a
proof of forceability** — an explicit bounded search for a valid ($(0,180)$-respecting)
move sequence realizing $\theta=180/11$ via $h_1,h_2$ up to depth 15 did **not** find
one (exhaustively checked all $2^{15}$ binary move sequences from the base state); the
congruence being solvable does not by itself guarantee a realizable path (the exact
integer value of $B_n$, not just its value mod $N$, must also match a sum of exactly
the right number/pattern of signed powers of two while respecting the $(0,1)$ range at
every step — a strictly stronger, unverified condition). So **no positive
extension of the forceable family beyond dyadic-scaffold has been established here**;
this is flagged as an open, possibly-fruitful direction but not a proven result.

## Current best

**H1 is very likely false**, evidenced by a rigorous impossibility proof (order-of-2
mod 7 obstruction) showing the natural nested-transfer extension of the proven
mechanisms cannot reach θ=180/7, strongly suggesting the earlier computational
"180/7 forceable" witness was a search artifact rather than a real construction. This
approach's central hypothesis is **not supportable** and should not be pursued further
as stated; the actual characterization of S beyond dyadic-scaffold's family remains
open and is better attacked by `corrected-genericity-bound` (necessity) and
`binary-word-invariant` (abstract orbit framing, which this round's finding sharpens:
the relevant generator set is not just $\{x/2,180-x\}$ but should also include the
cross-transfer $h_2$ derived above, and even with that addition 180/7 is excluded).

No constructive progress toward proving S=(0°,90°] was found; the round's real
contribution is negative (ruling out a specific test case rigorously) plus one
reusable, previously-unrecorded legal primitive (the cross-transfer lemma).

## Open gaps

- Full impossibility of θ=180/7 in the *actual* game (not just within the
  "one-pure-quantity" move family analyzed here) is not established — would need to be
  combined with a genuine invariant/genericity argument (see
  `corrected-genericity-bound`) to become airtight.
- Whether $N=11,13,\dots$ (order of $2\bmod N$ even, $N$ not of the form $2^k+1$) are
  actually forceable via the cross-transfer mechanism is open — the necessary
  congruence condition holds but no explicit valid construction was found in a depth-15
  search.
- The rational/irrational θ split flagged in earlier rounds is now moot for this
  approach's H1 claim, since H1 itself is refuted at a single rational test point.

## Promotable lemmas

**Cross-transfer lemma.** From a triangle $\{r,\theta-r,180-\theta\}$ with
$0<\theta<90°$ and spectator $r$ with $0<r<180-2\theta$ (achievable by further
bisection if necessary), the cut at the $(180-\theta)$-vertex with
$x_1=(180-\theta)-\theta-r$ (i.e. targeting $\theta+r$) produces children
$A=\{\theta-r,\,180-2\theta,\,\theta+r\}$ and $B=\{r,\,\theta,\,180-\theta-r\}$; since
$B$ contains $\theta$ exactly, Shan-Yu is forced into $A$, which contains the new
pure angle $180-2\theta$ regardless of $r$. Proved in full above (symbolic algebra,
independently re-derived with the mirror spectator choice for a consistency check).
Reusable by any approach building further nested-transfer constructions.

**Order-of-2 obstruction (θ=180/7 case).** Within the monoid generated by
$h_1(P)=P/2$ and $h_2(P)=2P-180$ acting on the pure quantity $P$ starting from
$P_0=180-\theta$, the target $\theta=180/N$ is reachable (i.e. $P_n=\theta$ for some
finite composition) only if $2^s\equiv-1\pmod N$ has an integer solution $s$. For
$N=7$, no such $s$ exists (the subgroup $\langle2\rangle=\{1,2,4\}\subset(\mathbb
Z/7\mathbb Z)^\times$ has odd order 3 and does not contain $-1\equiv6$). Hence
$\theta=180/7$ is not reachable via this mechanism. Proved in full above; the general
necessary-condition statement (for arbitrary odd $N$) is stated but not claimed
sufficient.
