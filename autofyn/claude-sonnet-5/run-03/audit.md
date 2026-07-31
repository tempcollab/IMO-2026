# GPT-5.6 audit of `autofyn/claude-sonnet-5/run-03`

## Scope and grading standard

I audited the selected `current.md` in each of
`results/imo-2026/autofyn/claude-sonnet-5/run-03/problem-01` through
`problem-06` against the corresponding statements in `problems.jsonl`. I
also followed the promoted lemmas and approach files on which the selected
proofs depend. In particular, I inspected the load-bearing computer-assisted
inequality in Problem 2 and the signature-purification proof in Problem 6.
After the initial audit, I separately re-audited the subsequently added
`problem-02/code/` bundle and its `README.md`; the Problem 2 discussion below
records that second pass.

The Autofyn labels `solved`, `approved`, `certified`, reviewer prose, and
random numerical tests were not treated as mathematical evidence. Code is
allowed, but a computer-assisted step must be reproducible: the actual code
or a complete independently checkable certificate must be retained, its
domain coverage must be verifiable, and exact/directed-rounding claims must
not rest only on a prose report that a computation once succeeded.

I use the requested harsh completion-based IMO standard: a complete proof,
or one needing only a genuinely tiny local repair, receives 7. A missing
load-bearing direction, theorem, or computational certificate receives 0;
substantial research progress does not by itself earn partial credit.

## Executive verdict

| Problem | Verdict | Score |
|---|---|---:|
| 1 | Complete | 7/7 |
| 2 | Final hard case rests on an unavailable interval-arithmetic computation | 0/7 |
| 3 | Explicitly incomplete for general `n` in both minimax directions | 0/7 |
| 4 | Complete characterization | 7/7 |
| 5 | Complete | 7/7 |
| 6 | Complete; signature determinacy and periodicity are valid | 7/7 |
| **Total** |  | **28/42** |

The zero on Problem 2 does **not** mean that I found a counterexample to
`OM=ON` or to the claimed residual inequality. It means the submitted
artifacts do not contain a checkable proof of the computation on which the
last hard case depends. Supplying and successfully auditing the missing
interval program/certificate could change that verdict.

## Problem 1 — 7/7

### What the proof does

For each prime `p`, a move sends the selected pair of valuations to

\[
(a,b)\longmapsto (\min(a,b),|a-b|).
\]

The proof uses

\[
\min(a,b)^2+|a-b|^2\le a^2+b^2,
\]

with strict inequality exactly when `min(a,b)>0`. Globally it tracks the
number `k` of nonunit entries and the sum `Sigma` of the squares of all
prime valuations. A move either reduces `k` by one, or keeps `k` fixed and
strictly reduces `Sigma`. The nested strong induction on `(k,Sigma)` is a
valid well-founded argument for termination under every possible sequence
of choices.

For uniqueness, the Euclidean identity

\[
\gcd(\min(a,b),|a-b|)=\gcd(a,b)
\]

preserves, for every prime `p`, the gcd of the full list of `p`-adic
valuations. At a terminal board with sole nonunit `M`, this invariant is
exactly `v_p(M)`, so all valuations of `M` are determined by the initial
board.

### Skeptical checks

- The output pair cannot be `(1,1)`: its product is
  `lcm(m,n)>1`. Thus one move reduces the number of nonunits by at most one.
- In the no-drop case, both outputs are nonunits, hence in particular
  `gcd(m,n)>1`; at least one prime makes the squared-valuation inequality
  strict.
- The inner induction really handles arbitrarily many stalling moves; it is
  not merely a strategy for choosing a favorable pair.
- The gcd-of-valuations invariant correctly handles zeros. In particular,
  `gcd(e,0)=e`, so a prime occurring in just one original number still gives
  a positive invariant.
- Terminality means at most one nonunit, while the no-double-collapse fact
  and the invariant exclude zero nonunits.
- Only finitely many primes occur initially, so the reconstructed product
  for `M` is finite.

The historical false identity mentioned at the top of the file is not used
in the selected proof; its replacement `gq=lcm(m,n)>1` is correct.

**Verdict: complete, 7/7.**

## Problem 2 — 0/7

### Structure of the claimed proof

The proof first polarizes the target. With `A` as origin,

\[
OM=ON\iff O\cdot(C-B)=\frac{|C|^2-|B|^2}{4}.
\]

It then invokes a long coordinate/rotation/elimination chain reducing the
geometric branch-selection problem to two trigonometric implications `(I)`
and `(II)` for `beta` in `(0,gamma)`. The final split compares the zero
`beta_1` of

\[
Y(\beta)=2\cos^2\beta-2X_0
\]

with `beta_0=(pi-A)/3` and `gamma=B` after taking `B<=C`.

- If `beta_1<=beta_0`, `(II)` is vacuous because `Y<0` on the range where
  its other hypothesis can hold.
- If `beta_1>=gamma`, monotonicity of `G` and a correct endpoint identity
  give `G(beta)>0` throughout the interval.
- In the middle case `beta_0<beta_1<gamma`, the proof reduces the last
  residual subcase to `T>=0` on a two-dimensional domain `D_b`.

The first and third branches of this trichotomy are elementary once the
earlier reduction is accepted. The middle branch is the decisive issue.

### The unavailable load-bearing certificate

The lemma `lemmas/t-nonnegative-on-case-b-residual-domain.md` claims the
following computer-assisted proof of `T>=0`:

1. Near a boundary corner, an `mpmath.iv` computation supposedly bounds
   the admissible slope by `(0.2024,3.121)` and a directional Hessian by
   `35.67`; Taylor's theorem then yields a positive lower bound.
2. Away from the corner, an `mpmath.iv` adaptive quadtree supposedly
   resolves 708 boxes, proving each box either outside `D_b` or positive
   for `T`, with zero unresolved boxes.

Those are not optional corroborations. They are the only justification of
`T>=0` over the continuum in the remaining `P>0, E<0` part of Case (b), and
that inequality is required to finish `(II)` and hence the original
geometry problem.

Even after the later `problem-02/code/` bundle was added, the run does
**not** retain the interval-arithmetic program that allegedly produced these
bounds and boxes. It contains exploratory and symbolic Python files from
other rounds, but no round-20 script implementing this
domain-safety/Hessian/quadtree verification, no machine-readable list of
the resolved boxes, and no independently checkable output certificate.
The approach and lemma files merely repeat the claimed decimal enclosures
and box counts.

This is especially material because the run's own proof-reviewer states
that the quadtree was **not independently re-run box-by-box**; it checked
the corner formulas and then used a 200,000-sample floating-point sweep as
corroboration. Sampling cannot certify a universal inequality. The log
contains reports of the computation and later spot checks, but not a
reproducible retained certificate from which the claimed exhaustive domain
coverage can be audited.

### Re-audit of the subsequently added `code/` bundle

I read `code/README.md` before inspecting the scripts. The bundle contains
38 Python files copied from rounds 2, 3, 4, 7, 14, and 16. Static inspection
gives the following concrete findings:

- No added Python file imports `mpmath.iv`, uses interval objects, or
  implements interval box subdivision.
- None contains the final certificate's distinctive quantities or outputs:
  the 708 resolved boxes, the `35.67` Hessian bound, the slope enclosure
  `(0.2024,3.121)`, the domain `D_b`, or an unresolved-box audit.
- The round-2 through round-7 files are early geometric exploration and
  Ptolemy/equivalence checks. They do not prove the final Case-(b) inequality.
- The round-14 files test a proposed polynomial/SOS ansatz and some local
  symbolic identities. Again, they do not provide a global interval cover.
- The highlighted round-16 scripts concern an SDP/SOS experiment at one
  rational witness point. `build_exact_point.py` explicitly fixes a single
  point and reads `/tmp/round-15/sos_work/polys.pkl`; the subsequent scripts
  read generated `/tmp/round-16/*.pkl` files, solve numerical CVXPY problems,
  round Gram matrices, and inspect eigenvalues numerically. These are a
  different attempted certificate, not the Taylor-plus-quadtree proof used
  by `current.md`.
- The required pickle inputs are not retained in `code/` and are absent from
  `/tmp`; the only similarly named `scratch/round-16/exact_polys.pkl` is a
  zero-byte file. Thus most of the highlighted round-16 chain is not
  reproducible from the added bundle as packaged.
- Even within that unrelated SOS chain, an exact coefficient-identity check
  is not by itself an exact positive-semidefiniteness certificate: several
  scripts assess PSD through floating-point eigenvalues. More importantly,
  a certificate at one fixed witness point would not establish `T>=0` on
  the full two-dimensional domain needed by the proof.

The README says that the final proof is self-contained and the scripts are
only supporting exploration. That description conflicts with the proof's
own load-bearing Steps (iii)-(iv), which expressly appeal to a “certified
`mpmath.iv`” Hessian/domain-safety computation and adaptive quadtree sweep.
The exact corner identities written in Markdown establish the corner value
and first derivative; they do not establish the global interval enclosures
or exhaustive away-from-corner coverage.

Accordingly, the added scripts provide useful historical context and some
checks of upstream algebra, but they do not supply the missing certificate
identified in the initial audit.

### Why the prose description is insufficient

To validate this as a computer-assisted proof, an auditor would at minimum
need to check:

- the exact interval extensions used for `X_0,P,E,T` and every derivative;
- the outward-rounding behavior for all transcendental evaluations;
- the precise initial box cover and the subdivision rule;
- that every discarded box is excluded by an inequality valid on the whole
  box, with the correct strict/non-strict boundary conventions;
- that the claimed subranges really cover all of `D_b`, including the
  pinch regions and overlaps;
- the complete list or deterministic regeneration of all terminal boxes;
  and
- that no unresolved or silently depth-capped box was dropped.

Numbers such as “708 boxes,” “zero unresolved,” and `|Q|<=35.67` assert the
result of these checks but do not permit the checks to be reproduced. A
floating-point random sweep showing no violation does not repair that
absence.

There is also a presentation problem in the selected `current.md`: its
Step 2 compresses a very large geometric branch-selection derivation into a
list of cited “certified” files. I followed the relevant chain far enough to
locate the final obligation, but even granting the upstream exact identities
does not remove the missing interval certificate at the end.

Under the requested binary completion standard, this is not a tiny local
omission. It is the proof of the last hard universal inequality.

**Verdict: not established by the submitted artifacts, 0/7.**

## Problem 3 — 0/7

### What has been established

The file conjectures

\[
c(n)=\frac{2^n}{2^{n+1}-1}
\]

and contains a large amount of substantial partial work. Among other
things, it reduces the claiming stage to an odd-rank/alternating-sum
minimax problem, develops the geometric lower-bound opening, proves many
peeling and endpoint lemmas, closes several excess and sliver subcases, and
proves the full small case `n=2`. It also obtains several exact candidate
responses for the upper-bound side and closes one region for `n=3`.

The selected file is commendably explicit that it remains `partial` and
that no full proof is warranted.

### Missing lower-bound direction

For the proposed Liu Bang opening, one must prove that **every** legal
Xiang Yu refinement using at most `n` additional cuts leaves the required
odd-rank sum. The general induction program `GT(m)` still has its own
`e=0` residual. Closing the other excess cases and the separate
`Case-B(m,k)` sliver does not close that residual: the file expressly notes
that they land on opposite sides of the relevant threshold and are
different objects.

Therefore the proposed geometric opening is not proved to guarantee the
claimed value for arbitrary `n`.

### Missing upper-bound direction

For an arbitrary Liu Bang opening, one must construct or prove the existence
of an Xiang Yu response whose odd-rank sum is at most the proposed value.
The file has a complete treatment only for `n=2`. For `n=3`, Region II
remains without a case-complete symbolic coverage proof: a seven-construction
panel has strong numerical support, but the file itself found an exact hole
in the previous six-construction panel, illustrating why random/global
optimization evidence is not exhaustive. General `n>=4` is not attempted.

Thus both directions required by the general problem remain incomplete.
The work is serious and potentially useful, but the missing statements are
the main theorem, not small repairs. Under the requested completion-heavy
grading standard, no partial points are awarded.

**Verdict: incomplete for general `n`, 0/7.**

## Problem 4 — 7/7

Submission audited: `problem-04/current.md` and its promoted move lemmas.

The answer is

\[
\theta=\frac{180^\circ}{n}\qquad(n\ge2\text{ an integer}).
\]

The master cut formula correctly models every legal cut. For the forward
direction, the general chip move cuts `theta` from a target angle: one child
wins immediately and the only delaying child decreases the target by
`theta`. If no suitable target multiple is initially present, the
compensation move uses an angle below `theta` to make both children contain
positive integral multiples of `theta`; the unique delaying branch starts
the same integer-valued descent. The legality inequalities are checked, the
tracked target stays positive, and the separate `n=2` boundary terminates in
one move. Thus the strategy wins after finitely many cuts for every starting
triangle.

Conversely, when `180 degrees/theta` is nonintegral, call a triangle clean
when none of its angles is an integral multiple of `theta`. For an arbitrary
cut, the two ways each child could become unclean give four pairings. Three
would make a parent angle resonant; the fourth would make `180 degrees`
resonant. All four contradict the hypotheses. The supplied construction of a
clean initial triangle is valid throughout `0<theta<180 degrees`, so Shan-Yu
can retain a clean child forever.

Both game quantifiers and the full real-valued domain are covered.

**Verdict: complete, 7/7.**

## Problem 5 — 7/7

### Necessity

Setting `x=f(y)` makes the outer quadratic and geometric means both equal
to `f(y)`, so

\[
f(f(y))=2f(y)-y.
\]

This gives injectivity. With `g(x)=f(x)-x`, it also gives

\[
g(f(x))=g(x),\qquad f^{,n}(x)=x+n g(x).
\]

Since every iterate remains positive, `g(x)` cannot be negative.

The proof then substitutes into the squared right-hand inequality and
correctly obtains the two cross bounds

\[
(x-y)^2\ge4f(y)(g(x)-g(y)),
\]

and its version with `x,y` interchanged. Hence

\[
|g(x)-g(y)|\le
\frac{(x-y)^2}{4\min(f(x),f(y))}.
\]

On an equal partition of `[a,b]` into `N` subintervals, `f(z)>=z>=a`, so
telescoping gives

\[
|g(b)-g(a)|\le\frac{(b-a)^2}{4aN}.
\]

Letting `N` tend to infinity proves that `g` is constant, without any
unstated continuity assumption. Thus `f(x)=x+c` with `c>=0`.

### Sufficiency

For `f(x)=x+c`, put `A=x` and `B=y+c`. Both squared inequalities reduce to

\[
(A-B)^2\ge0.
\]

All original quantities are positive, so squaring introduced no spurious
solutions. The domain and the condition `c>=0` are handled correctly.

**Verdict: complete, 7/7.**

## Problem 6 — 7/7

### Good integers and the greedy sequence

With `k=a_1`, define `x>=k` to be good when every earlier integer coprime to
`x` is bad. Distinct good integers are pairwise non-coprime by definition.
The induction identifying the good integers with the greedy sequence is
valid: the next greedy term is good, and every skipped integer has an earlier
good coprime witness.

### Purification and signature determinacy

For `b>=k` having a prime factor at most `k`, let `a` be the squarefree
product of all such small prime factors and choose `p|a`. If `b` is not
`k`-smooth, choose a big prime `q|b` and the least `n` with
`x=p^n a>=k`. Then `x` has exactly the same small-prime signature as `b`
and `x<=b`:

- if `n=0`, then `x=a<aq<=b`;
- if `n>=1`, then `x<pk<=ak<aq<=b`.

The signature-determinacy descent is sound. In a minimal pair of same-signature
integers with opposite statuses, let `a` be bad and `b` good, and choose an
earlier good `r` coprime to `a`. Purify `r` to a `k`-smooth integer `r'`
with the same signature. Minimality forces `r'` good. Pairwise
non-coprimality of `r'` and `b` then supplies a common small prime; the two
signature equalities make that prime divide both `r` and `a`, contradicting
their coprimality. Thus good/bad status depends only on the set of prime
divisors at most `k`.

### Exact periodicity

Let

\[
L=\prod_{p\le k,\ p\ {\rm prime}}p.
\]

Integers `x` and `x+L` have identical small-prime signatures, so the good
set, hence the full sequence term set, is periodic from `k`. If `T` is the
number of good integers in `[k,k+L)`, translation by `L` is an
order-preserving bijection of the corresponding tails. Therefore

\[
a_{n+T}=a_n+L
\]

for every `n>=1`. All inequalities in purification are strict where needed,
and the period begins at the initial cutoff rather than only eventually.


**Verdict: complete, 7/7.**

## Final assessment

The run contains four fully correct solutions: Problems 1, 4, 5, and 6.
Problem 3 honestly remains a broad partial attempt and receives no credit
under the requested strict standard. Problem 2 may contain the ingredients
of a valid computer-assisted proof, but the retained submission does not
contain the executable/certificate for its decisive interval verification;
the newly added script bundle contains different exploratory/SOS code, and
the review prose and random sampling cannot substitute for the missing
interval certificate.

**Final score: 28/42.**
