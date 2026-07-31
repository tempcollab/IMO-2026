# GPT-5.6 audit of `autofyn/claude-sonnet-5`

## Scope and grading standard

I audited the six selected proofs against the corresponding statements in
`problems.jsonl`. The selected submissions are:

- Problem 1: `problem-01/imo-2026-01-solution.md`
- Problem 2: `problem-02/current.md` and its cited lemma files
- Problem 3: `problem-03/current.md` and the lemma/approach files on which its
  imported lower bound depends
- Problem 4: the full proof in `problem-04/imo-2026-04.md`
- Problem 5: the full proof in `problem-05/imo-2026-05.md`
- Problem 6: `problem-06/current.md`

The internal Autofyn labels “solved,” “approved,” and “certified” were not
treated as mathematical evidence. I checked the cited arguments themselves.
Code is allowed where it supplies a correct, exact, reproducible certificate;
numerical experiments alone are only corroboration.

I use the completion-heavy grading standard requested for these audits: a
complete proof with at most a tiny local repair receives 7, while a missing
load-bearing direction or lemma receives 0 rather than speculative partial
credit. For context, I separately mention where an ordinary problem-specific
marking scheme might plausibly recognize substantial progress.

## Executive verdict

| Problem | Verdict | Score |
|---|---|---:|
| 1 | Complete | 7/7 |
| 2 | Complete; directed-angle branches and exact cofactor identity are valid | 7/7 |
| 3 | Lower bound proved, but the general upper bound remains open | 0/7 |
| 4 | Complete; two harmless local errors | 7/7 |
| 5 | Complete | 7/7 |
| 6 | Complete | 7/7 |
| **Total** |  | **35/42** |

The only rejected proof is Problem 3. Its claimed answer appears to be right,
and its upper-bound half is good mathematics, but its lower-bound half is
promoted from an abstract D/M game to the actual cutting game through a chain
of lemmas that does not establish that promotion.

## Problem 1 — 7/7

### Outline of the argument

For each prime `p`, the proof replaces every board entry by its `p`-adic
valuation. A move on two entries becomes

\[
(a,b)\longmapsto (\min(a,b),|a-b|).
\]

The gcd of the complete valuation list is preserved by this Euclidean step.
Consequently

\[
\Gamma=\prod_p p^{\gcd_i v_p(x_i)}
\]

is invariant. Termination is proved independently using

\[
\Psi=\left(\prod_i x_i\right)
      2^{\#\{i:x_i>1\}}.
\]

Every legal move decreases `Psi` by at least a factor of two. At a terminal
position there is at most one entry greater than 1, and the invariant then
identifies that entry uniquely.

### Skeptical checks

- When the selected entries are coprime, their product does not fall, but the
  number of nonunits drops by one; hence `Psi` still halves. When their gcd is
  nontrivial, the product falls sufficiently to cover the possible change in
  the nonunit count. All equality cases, including equal selected numbers,
  are handled.
- Zero valuations cause no issue: the transform is precisely an ordinary
  Euclidean gcd step on nonnegative integers.
- “Terminal” initially yields only *at most* one nonunit. The proof correctly
  excludes the all-ones board. Some initial entry has a prime divisor, so the
  corresponding valuation list is not identically zero and has positive gcd;
  the all-ones board would give gcd zero for every prime.
- On a terminal board `(M,1,...,1)`, the exponent of each prime in `Gamma` is
  exactly `v_p(M)`, so the displayed formula determines `M` and proves choice
  independence.

I found no load-bearing omission. The solution is far longer than necessary,
but that is not a correctness defect.

**Verdict: complete, 7/7.**

## Problem 2 — 7/7

Submission audited: `problem-02/current.md` and the lemma files it cites.

After placing `B=(0,0)`, `C=(a,0)`, and `A=(p,q)`, the proof correctly
reduces `OM=ON` to the scalar condition `myexpr=0` for the circumcenter of
`AKL`. The determinant divided by in this reduction is nonzero because the
problem gives a genuine triangle `AKL`.

The main possible failure in a coordinate treatment is an invalid conversion
of the three ordinary-angle hypotheses into directed-angle equations. This
proof closes that branch issue. Interiority fixes the rotations defining `K`
and `L`; the ray-betweenness and side-of-line arguments then establish the
signs of all four relevant cross products at `B`, `C`, `M`, and `N`.
Consequently all four directed angles lie in `(0,pi)`, so the ordinary-angle
equalities imply the exact directed equalities used to obtain `e_1=e_2=0`.

The two residuals factor as `e_1=T_K A_1` and `e_2=T_L B_1`, with both ray
parameters positive. Direct expansion of the displayed formulas verifies the
exact identity

\[
\operatorname{myexpr} Z
=2(q-T_KX)A_1+2(T_LX'-q)B_1.
\]

Finally, `Z=aX+s(p^2+q^2)>0`: interiority gives `X>0`, and all remaining
factors are positive. Thus `A_1=B_1=0` forces `myexpr=0`, which is equivalent
to `OM=ON`. No numerical experiment is load-bearing.

**Verdict: complete, 7/7.**

## Problem 3 — 0/7

### Correct result and completed lower bound

The replacement gives the correct target

\[
c(n)=\frac{2^n}{2^{n+1}-1}.
\]

Its lower-bound direction is complete. For the geometric opening, the
submission develops a valid alternating-sum formulation and a subdivision
tree argument. The anchor-only, residual, and multiple-tie-cluster cases are
all covered, so this opening forces the claimed payoff for every `n`.

The upper-bound induction is also complete for small configurations through
`m=4`: the threshold reduction closes Cases A and B, and the finite
three-strategy/affine-cell analysis closes Case C for four initial pieces.
The rational cell inequalities used there are exact.

### Missing general upper bound

The proof does not extend the Case-C strategy to arbitrary `m`. The selected
file explicitly leaves every general `m>=5` instance open. Its proposed
SLACK-COVER/Hall-type subset-matching statement is not proved, and the
finite menu of tie strategies used for `m=4` has no demonstrated
generalization. Several numerical searches and exact checks of the `m=4`
cells do not establish the required quantified statement for all `m`.

This is the entire upper-bound direction asserting that no non-geometric
opening beats the proposed value. It is load-bearing and cannot be supplied
by a local edit. Under the completion-heavy rubric, the solution remains
incomplete despite proving one full direction and several nontrivial small
cases.


**Verdict: incomplete, 0/7.**

## Problem 4 — 7/7

### Outline of the argument

Represent a triangle by its angle triple `(alpha,beta,gamma)`. Cutting the
vertex of angle `alpha` with parameter `0<t<alpha` gives children

\[
L(t)=(t,\beta,\alpha+\gamma-t),\qquad
R(t)=(\alpha-t,\gamma,\beta+t).
\]

For `theta=180 degrees/n`, attacking an angle larger than `theta` with
`t=theta` makes one child contain `theta`, forcing Shan-Yu to retain the
other child and thereby subtracting `theta` from the attacked angle. When a
small helper angle `h<theta` is present, the helper-reset move forces the
universal triangle

\[
(\theta-h,h,180^\circ-\theta).
\]

Its last angle is `(n-1)theta`, so repeated forced subtraction reaches
`theta`.

For the converse, when `180 degrees/theta` is not an integer, Shan-Yu starts
from

\[
(\theta/2,\theta/2,180^\circ-\theta)
\]

and maintains the invariant that no angle is an integral multiple of
`theta`. The four congruence cases show that, after any cut at any vertex,
both children cannot simultaneously violate the invariant. Shan-Yu can
therefore preserve it forever.

### Skeptical checks

- Both child-triple formulas are correct and preserve total angle 180
  degrees.
- The transfer move is genuinely forced because the discarded choice would
  contain `theta` immediately.
- Substituting `t=theta-h` in the helper-reset move gives exactly
  `(theta-h,h,180 degrees-theta)` on the retained side and puts `theta` in
  the rejected side.
- The room-condition sum argument ensures an eligible partner exists. Its
  use of `theta<=90 degrees` is valid for every integer `n>=2`.
- The proof uses a fixed finite pipeline, not a naive redispatch loop; the
  manufactured `(n-1)theta` coordinate then decreases deterministically.
- The survival triangle is positive and satisfies the invariant whenever
  `180 degrees/theta` is nonintegral.
- The congruence argument is symmetric in the attacked vertex and covers an
  arbitrary real split, not merely the special winning moves.

### Two local errors found

1. The proof writes `ceil(A_0/theta)<=n-1`, which can be false when
   `A_0/theta` lies strictly between `n-1` and `n`. The number of required
   subtractions is instead the least `j` for which
   `A_0-j theta<=theta`; it is still at most `n-1` because `A_0<n theta`.
   The termination bound survives unchanged.
2. Lemma 4 contains the reversed display `a+b+c>3theta=180`. The intended
   relation is `180=a+b+c>3theta`, yielding `theta<60 degrees`. The
   surrounding argument uses the correct conclusion, so this is plainly a
   typographical reversal.

Both are isolated one-line repairs and neither changes the strategy or the
characterization.

**Verdict: complete, 7/7.**

## Problem 5 — 7/7

### Outline of the argument

Substituting `x=f(y)` collapses both outer terms of the given inequality and
forces

\[
f(f(y))=2f(y)-y.
\]

Iteration then gives `f^n(y)=y+n(f(y)-y)`. Positivity of every iterate
implies `f(y)>=y`. Writing `d(x)=f(x)-x`, the squared lower inequality,
applied with `x` replaced by `f(x)`, gives the exact identity and inequality

\[
(2f(x)-x+y)^2-4f(x)f(y)
=(x-y)^2+4f(x)(d(x)-d(y))\ge0.
\]

Partitioning any interval `[a,b]` into `N` equal pieces and applying this in
both directions yields

\[
|d(b)-d(a)|\le \frac{(b-a)^2}{4aN}.
\]

Letting `N` grow proves that `d` is constant, hence `f(x)=x+c` with `c>=0`.
The converse follows from ordinary QM-AM-GM applied to `x` and `y+c`.

### Skeptical checks

- The substitution `x=f(y)` is legal because the codomain is positive.
- The iterate argument uses no unstated continuity, measurability, or
  surjectivity assumption.
- Squaring is reversible in the required direction because all expressions
  are positive.
- The algebraic defect identity has the correct coefficient `4f(x)`.
- The partition estimate is applied in both orientations, so it controls the
  absolute difference rather than only proving one-sided monotonicity.
- The denominator is uniformly bounded using `f(x_i)>=x_i>=a>0`; hence the
  limit argument is rigorous.
- For `f(x)=x+c`, the middle expression is `(x+(y+c))/2`, so both required
  inequalities are exactly QM-AM and AM-GM.

No gap or illegitimate regularity assumption was found.

**Verdict: complete, 7/7.**

## Problem 6 — 7/7

### Outline of the argument

Let `k=a_1`. The proof first establishes the exact recursive
characterization: an integer `n>k` is a nonterm if and only if it is coprime
to some earlier term. It then proves:

1. every multiple of a term is a term;
2. if `rs` is a nonterm, then `r^2s` is a nonterm; and
3. if `p>k` is prime and `n` is a nonterm, then `np` is a nonterm.

The third statement is proved by a valid minimal-counterexample descent. From
these claims, the proof shows that two integers at least `k` having the same
set of prime divisors at most `k` have the same term/nonterm status.

Set

\[
P=\prod_{p\le k,\ p\text{ prime}}p.
\]

Congruent integers modulo `P` have the same small-prime set, so each residue
class is uniformly a term class or a nonterm class once restricted to
integers at least `k`. If there are `T` good residue classes, their increasing
enumeration immediately gives

\[
a_{n+T}=a_n+P
\]

for every `n>=1`.

### Skeptical checks

- The recursive IN/OUT lemma follows exactly from the minimality in the
  sequence definition; it does not assume the desired periodicity.
- The “multiple of a term” claim correctly uses the fact that every two
  distinct terms have gcd greater than one.
- In the big-prime companion lemma, the auxiliary number `y^alpha` is in the
  required domain and is strictly smaller than the alleged minimal
  counterexample. The descent through `p^i y^alpha` therefore closes.
- In the main minimal-counterexample theorem, `e_0=d_0/p` satisfies
  `e_0>=c_0>=k`. This domain check is crucial and is present.
- Removing a factor `p<=k` preserves the small-prime signature because
  similarity already forces `p` to divide the smaller member; when `p>k`,
  removal plainly affects no small prime.
- Sorting the finitely many good residue representatives in `[k,k+P)` gives
  consecutive nonoverlapping blocks. Thus the final relation holds from the
  first term, with no unproved “eventually periodic” to “periodic” jump.

There is one microscopic wording issue in Claim 1: its cited pairwise-term
corollary is stated for distinct terms, while the witness `m` could in
principle equal the term `n`. In that case `gcd(n,n)=n>1` directly, so the
same contradiction is immediate. This is not a mathematical gap.

The numerical checks in Section 8 are unnecessary; the proof before them is
self-contained.

**Verdict: complete, 7/7.**

## Final coordinator-style assessment

Problems 1, 2, 4, 5, and 6 are full solutions. Problem 2's computational
component is acceptable because it is an exact symbolic certificate whose
mathematical role and domain are explicit. Problem 4's two mistakes are
localized notation/arithmetic slips with immediate repairs and no effect on
the strategy.

Problem 3 is qualitatively different. Its geometric lower-bound opening and
the complete `m=4` upper-bound case are substantial, but the upper-bound
Case C for every `m>=5` remains unproved. It should not be promoted as a
solved proof in its current form.

**Final score: 35/42.**
