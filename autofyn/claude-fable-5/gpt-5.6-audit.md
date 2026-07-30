# GPT-5.6 audit — AutoFyn / Claude Fable 5

## Scope and grading standard

This report audits the selected `current.md` proof for each of Problems 1–6,
together with every cited lemma or approach file carrying a load-bearing
step. Internal status labels and numerical experiments are not treated as
proof.

The completion-based standard gives 7 to a complete proof, 6 only when the
sole omission has a uniquely local mechanical repair, and 0 when a
load-bearing direction or theorem is missing.

## Executive verdict

| Problem | Verdict | Score |
|---|---|---:|
| 1 | Complete | 7/7 |
| 2 | Complete; branch-pinned trigonometric certificate is valid | 7/7 |
| 3 | Complete; matching lower and upper bounds | 7/7 |
| 4 | Complete characterization | 7/7 |
| 5 | Complete characterization | 7/7 |
| 6 | Complete; small-prime descent gives periodic enumeration | 7/7 |
| **Total** |  | **42/42** |

## Problem 1 — 7/7

The proof handles termination and uniqueness separately but with compatible
prime-valuation machinery. For each prime `p`, a move changes the two selected
valuations by

\[
(a,b)\longmapsto(\min(a,b),|a-b|).
\]

For termination, let `S` be the sum of all prime-factor multiplicities on the
board and `C` the number of entries greater than one. A move with nontrivial
gcd strictly decreases `S`; a coprime move preserves `S` and strictly
decreases `C`. Thus `(S,C)` decreases lexicographically in
`N x N`, so every play terminates. A terminal board has at most one nonunit.

For every prime `p`, the gcd of the complete list of `p`-adic valuations is
invariant because

\[
\gcd(a,b)=\gcd(\min(a,b),|a-b|),
\]

including all zero-valuation cases. Some prime has a positive initial
valuation-gcd, so the terminal board cannot consist entirely of ones. Hence
exactly one entry `M>1` remains, and prime by prime

\[
v_p(M)=\gcd(v_p(a_1),\ldots,v_p(a_{2026})).
\]

This determines `M` solely from the initial board and proves both requested
parts.

**Verdict: complete, 7/7.**

## Problem 2 — 7/7

The proof first consumes the interiority hypotheses to fix every relevant
ordinary-angle branch. In particular, all sines divided by in the law-of-sines
relations are strictly positive, and the two angle-inside-angle assumptions
give the exact additive relations at `B` and `C`.

Six law-of-sines equations eliminate the auxiliary angles and yield the two
side relations

\[
\ell_K=bQ_u-cP_u=0,\qquad
\ell_L=cQ_v-bP_v=0.
\]

The separate monotonicity argument proves that `A,K,L` are noncollinear, so
the circumcenter and the determinant used later are legitimate. Median
identities and coordinates reduce `OM=ON` to one trigonometric polynomial
condition `G=0`.

The closing certificate is the explicit identity

\[
2\sin A\,G=\alpha\ell_K+\beta\ell_L.
\]

The report prints the coefficients of `b^2`, `bc`, and `c^2` and verifies
each by complete product-to-sum cancellation. Thus this is a checkable
algebraic identity rather than an unsupported invocation of a computer
algebra system. Since `sin A>0`, the two side relations force `G=0` and hence
`OM=ON`. I found no lost supplementary-angle branch or unhandled degeneracy.

**Verdict: complete, 7/7.**

## Problem 3 — 7/7

The claimed value is

\[
c(n)=\frac{2^n}{2^{n+1}-1}.
\]

The reduction from the alternating claiming game to the sum of the
odd-ranked final lengths is correct. Equivalently, since the total length is
one, the first player's value is one half plus one half of the descending
alternating discrepancy.

For the lower bound, Liu Bang uses the dyadic ladder. After Xiang Yu's at
most `n` additional cuts, pair the final fragments consecutively in
nonincreasing order and form the multigraph whose vertices are original
ladder rungs and whose edges are paired fragments. The edge count guarantees
a nontrivial tree component. At its highest rung, the total mass exceeds the
combined mass of all lower rungs by one unit, so the sum of the corresponding
pair gaps is at least one unit. After rescaling, the discrepancy is at least
`1/(2^{n+1}-1)`.

For the upper bound, the subset-sum pigeonhole lemma correctly finds two
disjoint nonempty subcollections whose total lengths differ by at most
`T/(2^m-1)`. The Match/Bisect walk realizes this balancing physically: each
match uses one legal interior cut and retires an exactly tied pair, while a
single carrier records the running difference. The empty-pile cases and sign
changes are covered, and the cut count is at most `m-1`. Retired tied pairs do
not affect discrepancy, leaving a final discrepancy at most the same bound.

With `m=n+1` and `T=1`, the upper and lower bounds coincide and give the
displayed value of `c(n)`.

**Verdict: complete, 7/7.**

## Problem 4 — 7/7

The cut formula exactly parametrizes every legal move: splitting an angle
`R` by `t in (0,R)` gives the two child triples stated in the proof, and every
such `t` is geometrically realizable.

Modulo the subgroup `theta Z`, call a triangle clean when none of its angles
has residue zero. If `180 degrees/theta` is nonintegral, exhaustive
four-case bookkeeping shows that both children of a clean triangle cannot be
unclean: three cases would make a parent angle resonant, and the fourth would
make `180 degrees` resonant. A clean initial triangle exists after excluding
only finitely many choices, so Shan-Yu can keep a clean child forever.

If `theta=180 degrees/n`, a legal fork makes both children contain a positive
integral multiple of `theta`. From an angle `k theta`, cutting off `theta`
either wins immediately or leaves `(k-1)theta`, giving finite descent. The
proof checks the lift into the legal open cut interval and separately handles
`n=2`, where a single cut forces a right angle in both children. The strategy
covers every starting triangle and wins within at most `n-1` cuts.

Therefore the exact winning set is

\[
\theta=\frac{180^\circ}{n},\qquad n\ge2.
\]

**Verdict: complete, 7/7.**

## Problem 5 — 7/7

The candidate functions `f(x)=x+c`, `c>=0`, satisfy both inequalities; after
squaring, each reduces to the same nonnegative perfect square.

For necessity, substituting `x=f(y)` forces

\[
f(f(y))=2f(y)-y.
\]

Writing `d(y)=f(y)-y`, forward iteration gives
`f^n(y)=y+n d(y)`. Positivity of every iterate rules out `d(y)<0`, so
`f(y)>=y` throughout the domain.

A second substitution into the right inequality yields the two-point bound

\[
|d(a)-d(b)|\le
\frac{(a-b)^2}{4\min(a,b)}.
\]

Subdividing any compact interval into `k` equal pieces and telescoping makes
the right side shrink like `1/k`; hence `d(a)=d(b)` for every positive
`a,b`. This argument derives constancy directly and assumes no continuity or
measurability. Thus `d` is a constant `c>=0`, producing exactly the stated
family.

**Verdict: complete, 7/7.**

## Problem 6 — 7/7

Pairwise gcd intersection of sequence terms follows immediately from the
greedy rule. The proof then identifies the sequence with the increasing
enumeration of all integers at least `a_1` that intersect every term in prime
support; the “valid below are terms” induction justifies using smaller valid
integers as earlier sequence elements.

Let `Q` be the finite set of primes at most `a_1` and `sigma(m)` the primes
of `m` lying in `Q`. The companion lemma is correct: if a term contains a
prime larger than `a_1`, its small-prime support can be realized by a strictly
smaller integer still at least `a_1`. Strong induction on the later index,
combined with a minimal earlier counterexample, then proves the Small Common
Prime Lemma

\[
\sigma(a_i)\cap\sigma(a_j)\ne\varnothing
\qquad(i<j).
\]

The strict decreases and threshold cases in this descent are all accounted
for. Consequently membership in the complete term set depends only on which
primes in `Q` divide an integer. Residue modulo

\[
M=\prod_{p\in Q}p
\]

determines exactly that signature, so the allowed integers form a nonempty
union of residue classes modulo `M`. Each interval `(a_n,a_n+M]` contains
exactly one representative of every residue class and hence exactly `T`
allowed integers, with `a_n+M` last. Therefore

\[
a_{n+T}=a_n+M
\]

for every `n>=1`. This proves the required identity without an unproved
eventual-to-global step.

**Verdict: complete, 7/7.**
