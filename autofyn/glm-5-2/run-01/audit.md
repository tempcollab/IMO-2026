# GPT-5.6 audit — AutoFyn / GLM-5.2 / run-01

## Scope and grading standard

I audited the six claimed solutions in `results/imo-2026/autofyn/glm-5-2/run-01` against the statements in `problems.jsonl`. Supporting artifacts were used only when they supplied an exact, reproducible proof step. Numerical experiments were treated as sanity checks, not proofs.

The scores use a strict IMO-style scale. A score of 7 requires a complete proof. A score of 6 is reserved for a proof whose only omission is a genuinely local exceptional case or similarly mechanical repair. A load-bearing missing argument receives 0 rather than generous progress credit.

## Score summary

| Problem | Score | Verdict |
|---|---:|---|
| 1 | 7/7 | Complete |
| 2 | 6/7 | Essentially complete; one degenerate case is not proved |
| 3 | 0/7 | Explicitly partial; both general bounds remain open |
| 4 | 7/7 | Complete |
| 5 | 7/7 | Complete |
| 6 | 7/7 | Complete |
| **Total** | **34/42** | |

## Problem 1 — 7/7

Submission audited: `problem-01/current.md`.

The proof is complete.

For each prime (p), a move changes the two relevant valuations from ((\alpha,\beta)) to

\[
(\min(\alpha,\beta),|\alpha-\beta|).
\]

The identity

\[
\gcd(\min(\alpha,\beta),|\alpha-\beta|)=\gcd(\alpha,\beta)
\]

therefore makes the gcd (D_p) of the full list of (p)-adic valuations invariant. This is exactly the right invariant for uniqueness of the final survivor.

Termination is also handled rigorously. The lexicographic potential

\[
\left(\sum_i\Omega(x_i),\#\{i:x_i>1\}\right)
\]

strictly decreases in every possible type of move: a nontrivial gcd decreases the first coordinate, while a coprime pair preserves the first coordinate and decreases the second. Thus infinite play is impossible. At a terminal board there can be at most one entry greater than (1), while the valuation invariant prevents all entries from becoming (1). Hence there is exactly one survivor.

Finally, at a terminal board (D_p=v_p(M)) for every prime (p), so

\[
M=\prod_p p^{D_p},
\]

which depends only on the initial board. Both requested parts are proved with no missing case.

## Problem 2 — 6/7

Submission audited: `problem-02/imo-2026-02.md`, together with the exact symbolic artifacts in `problem-02/scratch/round-1/`.

### What is established

The initial reduction is sound. If (A'=2O-A) is the antipode of (A) on the circumcircle of (AKL), then the homothety of ratio (1/2) centered at (A) gives

\[
OM=ON\iff A'B=A'C.
\]

The coordinate parametrization of (K) and (L), the two incidence equations, and the elimination of the side ratio (b=AC/AB) are coherent. The load-bearing Direction Lemma is reduced to a polynomial identity. I independently ran `scratch/round-1/independent_cert.py`; it reconstructed the incidences and (A'), obtained zero remainder when the cleared numerator of (g) was divided by the cleared numerator of (C), and confirmed the stated rational identity exactly. Thus this is not merely a numerical certificate.

There is a presentational danger in writing (g=C(T_n/T_d)), because (T_d\ne0) is not established on every configuration. The retained denominator-safe pseudodivision is sufficient: after clearing only the genuine half-angle and incidence denominators, the numerator of (C) divides the numerator of (g), with zero remainder. Those genuine denominators are nonzero under the strict interior hypotheses. I therefore do not penalize the certificate itself.

The (B\leftrightarrow C), (K\leftrightarrow L) relabelling and orientation reversal correctly yield, for

\[
\theta=90^\circ-A-\alpha,
\]

the two directed-line relations

\[
\measuredangle(BC,BA')=\theta,
\qquad
\measuredangle(BC,CA')=-\theta.
\]

### Missing exceptional case

The final inference in lines 102–105 is not valid when (\theta=0). In that case the two displayed directed-line relations say only that (A',B,C) are collinear. The object called (\triangle A'BC) is degenerate, its two “base angles” are both (0), and the usual converse “equal base angles imply equal opposite sides” cannot be invoked. Collinearity alone plainly does not imply that (A') is the midpoint of (BC).

Nothing in the submission proves that (A+\alpha=90^\circ) is impossible. Indeed the run's own numerical artifact includes a configuration with (A=80^\circ), (\alpha=10^\circ), for which the desired midpoint conclusion happens to be true; the numerical check does not supply the missing exact proof. The case needs a separate specialization of the coordinate identities (or another exact argument) proving (A'=(B+C)/2).

There is a related unspoken nondegeneracy assumption when a zero cross-product is interpreted as a directed angle: the proof should also exclude (A'=B) and (A'=C), or absorb those possibilities into the exceptional-case calculation. The exact algebraic spine is otherwise intact, so these are local endpoint/degeneracy repairs rather than a failure of the main method. Under the stated rubric this earns **6/7**, not 7.

## Problem 3 — 0/7

Submission audited: `problem-03/current.md` and its cited approach and lemma
files.

The submission accurately labels itself partial. It conjectures

\[
c(n)=\frac{2^n}{2^{n+1}-1}
\]

and contains useful reductions, special cases, and numerical evidence, but not
a solution for general `n`.

Two load-bearing parts are explicitly open:

- The lower bound is still open for general non-dyadic, multi-split
  refinements. The verified block and spine cases do not establish the
  required all-partitions statement.
- The upper bound still lacks a general Xiang Yu strategy in the compressed
  case. The remaining condition is explicitly recorded as open.

These are the two load-bearing directions of the all-`n` theorem rather than
local omissions. Under the requested completion policy, this is **0/7**.

## Problem 4 — 7/7

Submission audited: `problem-04/current.md`.

The characterization

\[
\theta=\frac{180^\circ}{n}\qquad(n\ge2)
\]

is proved in both directions.

For necessity, the set of triangles with no angle equal to a positive integral multiple of (\theta) is shown to be closed under at least one of Shan-Yu's two choices whenever (180^\circ/\theta\notin\mathbb Z). The four possible ways in which both children could acquire a multiple telescope respectively to (C,A,B,) or (180^\circ), giving a contradiction. The equilateral triangle is a valid safe opening, so Shan-Yu can preserve the invariant forever.

For sufficiency, an angle (m\theta) can be split so that one child immediately has (\theta) and the other has ((m-1)\theta), giving induction on (m). If no angle is already a multiple, an open interval of length (C/\theta>1) supplies an integer (k) and a cut for which the two new angles are (k\theta) and ((n-k)\theta). The (n=2) case is treated separately and correctly.

Line 172 says a triangle is “(B_\theta)-free but contains (m\theta),” which is literally contradictory. This is an obvious stray adjective: the intended exhaustive trichotomy is “contains (\theta), contains another multiple (m\theta), or contains no multiple,” and Lemma R applies in the second case without any (B_\theta)-free assumption. No new idea or missing argument is needed, so this wording slip does not reduce the score.

## Problem 5 — 7/7

Submission audited: `problem-05/current.md`.

The answer (f(x)=x+c), (c\ge0), is completely established.

Writing (g(x)=f(x)-x), substitution (x=f(y)) forces

\[
g(f(y))=g(y),
\]

so the forward orbit is (y+n g(y)). Positivity of the codomain rules out (g(y)<0). The two squared inequalities are then combined into the exact squeeze

\[
|(g(x)-g(y))(g(x)+g(y)+2x+2y)|\le (x-f(y))^2.
\]

If (g(y_0)=\alpha>0), the arithmetic orbit with spacing (\alpha) gives lattice points uniformly close to every sufficiently large (x), and the squeeze forces (g(x)\to\alpha). Hence all positive values of (g) coincide. The proof then shows (g) is constant on a tail and uses the supremum of the zero set to rule out coexistence of the values (0) and (\beta>0). Thus (g) is a single nonnegative constant. The candidate family is checked by QM–AM–GM. I found no hidden regularity assumption or uncovered branch.

## Problem 6 — 7/7

Submission audited: `problem-06/current.md` and
`problem-06/approaches/w-descent-rsmooth.md`.

The proof is logically complete. First, the greedy definition gives the
characterization that an integer `m>=a_1` occurs exactly when it shares a
prime factor with every smaller occurring integer. Hence every excluded
integer has a smaller occurring coprime witness.

Let `k=a_1`. The smooth-substitution lemma is valid in both cases. If `b` is
already `k`-smooth, take `x=b`; otherwise, replacing its large-prime part by
a minimal power of one of its small primes produces `k<=x<=b` with exactly
the same prime divisors at most `k`.

A minimal-counterexample descent now proves the similarity theorem: two
integers at least `k` with the same set of prime divisors at most `k` are
either both in or both outside the greedy set. The strict decrease comes from
the smaller coprime witness, so it does not depend on the substituted integer
being strictly smaller than that witness.

Finally, residue modulo

\[
P=\prod_{p\le k,\ p\text{ prime}}p
\]

determines this small-prime signature. Membership is therefore `P`-periodic,
and the sequence is the cyclic increasing enumeration of the allowed residue
classes. One complete cycle adds `P`, yielding

\[
a_{n+T}=a_n+P
\]

for every `n>=1`.

**Verdict: complete, 7/7.**

## Final verdict

This run contains four fully correct solutions (P1, P4, P5, P6), one essentially complete solution with a local degeneracy omission (P2), and one openly incomplete attempt (P3). The strict IMO total is

\[
\boxed{34/42}.
\]
