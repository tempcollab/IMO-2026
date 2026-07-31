# Fable 5 audit — AutoFyn / GPT-5.6 Sol

## Scope and grading standard

This report audits the selected `current.md` proof for each of Problems 1–6, together with every cited lemma file carrying a load-bearing step (Problem 6 imports four certified lemmas from `problem-06/lemmas/`; all four were read and re-derived). Internal status labels and numerical experiments are not treated as proof.

Every load-bearing computation was stress-tested with independent verification code written during this audit: random-play simulation of the Problem 1 process against the predicted terminal value, exact symbolic verification of the Problem 5 identities (sympy), exact-rational simulation of both Problem 3 constructions (the dyadic lower bound under random refinements and the folding response for random markings, with cut counts checked against the budget), direct greedy-sequence period checks for nineteen starting values in Problem 6, and a full numeric construction of the Problem 2 configuration from the given angle equalities (180 in-configuration instances; every claimed concyclicity, both circle equations, both radical axes, and the final equality verified to below 1e-8).

The completion-based standard gives 7 to a complete proof, 6 only when the sole omission has a uniquely local mechanical repair, and 0 when a load-bearing direction or theorem is missing.

## Executive verdict

| Problem | Verdict | Score |
|---|---|---:|
| 1 | Complete | 7/7 |
| 2 | Complete; explicit four-circle radical-axis certificate | 7/7 |
| 3 | Complete; matching lower and upper bounds | 7/7 |
| 4 | Complete characterization | 7/7 |
| 5 | Complete characterization | 7/7 |
| 6 | Complete; marked-prime descent gives finite control | 7/7 |
| **Total** |  | **42/42** |

## Problem 1 — 7/7

Termination uses the monovariant `Psi = 2^k P`, where `P` is the board product and `k` the number of entries exceeding one. The three cases (coprime pair, equal pair, unequal pair with common factor) are disjoint and exhaustive, and in each `Psi` drops by a factor of at least two or by the selected gcd; the case analysis correctly rules out a second unit output when `m != n` share a factor, since `lcm(m,n) = gcd(m,n)` would force `m = n`.

For uniqueness, the per-prime valuation update `(r,s) -> (min(r,s), |r-s|)` preserves the gcd of the full exponent column, including zero valuations. A terminal all-ones board would force the invariant column gcd to zero against its positive initial value, so exactly one entry `M > 1` survives, and `v_p(M)` equals the initial column gcd prime by prime. Random-play simulation over 300 boards confirmed both the terminal shape and the predicted value of `M` in every play.

**Verdict: complete, 7/7.**

## Problem 2 — 7/7

The proof constructs `D = BK ∩ AC` and `E = CL ∩ AB`, derives `AD = c sin x / sin(alpha+x)` and `AE = b sin x / sin(alpha+x)` from explicit coordinates, and reads off the key relation `AB·AE = AC·AD`. In the oblique basis `u = AB`, `v = AC`, the circle through `A` and the midpoints `P`, `Q` of `BE`, `CD` gets the explicit equation (8), and the circles `(CEMK)` and `(BDNL)` get equations (9) and (11), each derived from three point substitutions with the coincidence cases `E = M` and `D = N` replaced by the tangent condition as a double root — the given angle equalities supply exactly the tangency needed there, so no limiting argument is used.

Subtracting the equations shows the radical axis of `(CEMK)` and `(APQ)` is the line `BD` and that of `(BDNL)` and `(APQ)` is the line `CE`; since `K` lies on `BD` and on the first circle, and `L` on `CE` and on the second, both lie on `(APQ)`. The circumcircle of `AKL` is therefore `(APQ)`, and the directed powers of `M` and `N` come out to `-(1/4)AB·AE` and `-(1/4)AC·AD`, equal by the key relation, giving `OM = ON`.

I re-derived all four circle equations and both radical-axis subtractions by hand; the algebra is exact. The end-to-end numeric check (constructing `K`, `L` from the three given angle equalities under the statement's interiority constraints) confirmed every intermediate concyclicity and the conclusion in all 180 solved instances, and correctly fails only for spurious roots violating the configuration constraints, which the hypotheses exclude.

**Verdict: complete, 7/7.**

## Problem 3 — 7/7

The claiming phase is settled by backward induction: taking a longest remaining piece is optimal, so the first claimant's value is the odd-rank sum `(1+D)/2`, with `D` the sorted alternating discrepancy.

The lower bound rests on the tree-component discrepancy lemma: if the parent lengths have all subset sums separated by at least `d`, any refinement by at most `m-1` splits has `D >= d`. The pairing multigraph has at most `m-1` edges, hence a tree component; its bipartition gives two distinct subset sums, and the triangle inequality bounds their gap by a sub-sum of the rank-pair differences, which total exactly `D`. With the dyadic parents `1/T, 2/T, ..., 2^n/T` and `d = 1/T` this yields the guarantee `2^n/T`.

The upper bound takes two consecutive subset sums with gap `r <= 1/(2^(n+1)-1)`, and the consecutiveness argument correctly forces every positive-support parent to have length at least `r`, which is what lets the entire residual sit inside one parent after the concatenation-refinement. The cut accounting `(|P|-1)+(|N|-1)+1 = s-1` plus one halving cut per unsupported parent stays within the budget, including the `N` empty and `r = 0` cases and the `m <= n` case where the residual is halved with the spare cut. The parity argument for the sorted list (even multiplicities plus one residual copy) gives `D = r`, hence the share `(1+r)/2 <= 2^n/T`.

Both constructions were simulated in exact rational arithmetic: the dyadic lower bound held under random refinements for `n = 1..4`, and the implemented folding response never exceeded the cut budget or the value bound for random markings at `n = 1..3`.

**Verdict: complete, 7/7.**

## Problem 4 — 7/7

The cut transition `(x, b, a+c-x)`, `(a-x, c, b+x)` is derived by angle chasing and every `0 < x < a` is realizable. For nonintegral `s = 180°/theta`, the all-nonintegral invariant survives every cut: the four ways both children could acquire an integral coordinate force one of `a`, `b`, `c`, `s` to be integral, each a contradiction, so Shan-Yu can hold the invariant forever from the equiangular start and no angle ever equals `theta`.

For `s = n >= 2`, the integer-crossing lemma (with the correct two-case proof, the all-below-one case forcing sum exactly 2) supplies a legal cut making both children carry a positive integral label, and the halving descent `k -> {floor(k/2), k - floor(k/2)}` strictly decreases the label whichever child Shan-Yu keeps, terminating at label 1. The strategy covers triangles with and without an integral label, so every `n >= 2` is winning.

**Verdict: complete, 7/7.**

## Problem 5 — 7/7

The squared forms `L, U >= 0` satisfy `L + U = 2(x - f(y))^2` and `L - U = 2(g(x)-g(y))(x+y+f(x)+f(y))`; both identities verified symbolically. Substituting `x = f(y)` forces both to vanish, giving `g(f(y)) = g(y)`, arithmetic forward orbits, and `g >= 0`. The cone estimate `|g(x)-g(y)|(x+y+f(x)+f(y)) <= (x-f(y))^2` with nearest-integer orbit alignment makes any two positive values of `g` equal, since the aligned pairs keep the right side bounded by `a^2/4` while the left grows linearly. Coexistence of zero and positive displacement is excluded by showing both level sets are relatively open, contradicting connectedness of the positive reals. The converse verification reduces both inequalities to the same perfect square, also verified symbolically.

**Verdict: complete, 7/7.**

## Problem 6 — 7/7

The four imported lemmas were each checked: the static gcd-polar enumeration (terms are exactly the admissible integers at least `a_1`, by minimality at the first skipped index), exact-support self-duality (powers of the radical realize every support in the upfamily), the ordered disjoint-witness lemma (the skipped threshold `mu(H)` yields an earlier term with disjoint support and smaller radical), and global periodic enumeration (a finite controller makes membership translation-invariant by `L`, and the order-preserving bijection advances every term exactly `T` places, giving `a_{n+T} = a_n + L` for all `n >= 1` with no eventual-to-global gap).

The new finite-control argument is the marked-prime descent, and it is correct: for a minimal support `C` containing the marked prime `p` with `rad(C \ {p}) >= a_1`, the exact threshold identity `mu(C \ {p}) = rad(C \ {p})` feeds the witness lemma; the returned support meets `C` only in `p`, so minimizing inside it keeps `p` while strictly decreasing the radical. Termination lands at `rad(S) < a_1`, where `p` is bounded by `a_1` (empty complement, via `p | a_1`) or by one of the finitely many thresholds `mu(S)` over squarefree `S` below `a_1`. Every minimal support then lies below `B`, giving the controller and the periodicity. Direct simulation over nineteen starting values confirmed a global period from `n = 1` in every case.

**Verdict: complete, 7/7.**
