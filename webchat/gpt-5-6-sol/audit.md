# Fable 5 audit — Web (chatgpt.com) / GPT-5.6 Sol

## Scope and grading standard

This report audits `problem-01.md` through `problem-06.md`, the one-shot web-interface solutions, against the problem statements quoted in the files themselves. The leading `time` lines are interface metadata and were ignored; the mathematics was judged directly.

Load-bearing computations were stress-tested with independent verification code written during this audit: random-play simulation of the Problem 1 process, exact-rational simulation of both Problem 3 constructions, symbolic verification of the Problem 5 identities, greedy-sequence period checks for Problem 6, and a full numeric construction of the Problem 2 configuration from the given angle equalities, testing the two signed power formulas of its Section 3 in 263 in-configuration instances.

The completion-based standard gives 7 to a complete proof, 6 only when the sole omission has a uniquely local mechanical repair, and 0 when a load-bearing direction or theorem is missing.

## Executive verdict

| Problem | Verdict | Score |
|---|---|---:|
| 1 | Complete | 7/7 |
| 2 | Complete in substance; signed power formulas asserted without orientation bookkeeping | 6/7 |
| 3 | Complete; matching lower and upper bounds | 7/7 |
| 4 | Complete characterization | 7/7 |
| 5 | Complete characterization | 7/7 |
| 6 | Complete; minimal-support descent gives finite period | 7/7 |
| **Total** |  | **41/42** |

## Problem 1 — 7/7

Termination uses `Phi = T + R`, the total prime multiplicity plus the count of nonunit entries. The per-prime computation `T_old - T_new = Omega(gcd)` is exact, and the two cases (`d > 1` drops `T`; `d = 1` drops `R` by exactly one since the coprime outputs are `1` and `mn`) each strictly decrease `Phi`. A move never removes the last nonunit, so the terminal board has exactly one entry `M > 1`. The column-gcd invariant `I_p` under `(a,b) -> (min(a,b), |a-b|)` is proved including the zero cases, and reading it at the terminal board determines `v_p(M)` from the initial board alone. Random-play simulation confirmed shape and value in every trial.

**Verdict: complete, 7/7.**

## Problem 2 — 6/7

The solution is a self-contained trigonometric argument. The ray order `AB, AK, AL, AC` is proved by barycentric monotonicity from the two interiority hypotheses. The two midpoint conditions become the sine relations `sin(x+p) sin z = 2 sin p sin(x+z)` and `sin(x+r) sin y = 2 sin r sin(x+y)`, and double computation of `AK`, `AL` gives the compatibility relation `X^2 sin(phi) sin(psi) = YPQZ`.

Section 4 is fully rigorous and was re-derived line by line during this audit: the reduction of the power-equality goal to `D = 0`, the passage to `E(S)`, the proof that `F(S)` is constant in `S` (the product-to-sum cancellation `Q cos(T+x+p) - P cos(T+x+r) = -sin(p-r) cos T` is exact), the evaluation at `S_0 = x+y+z` using the cotangent forms of the midpoint relations, and the two closing product-to-sum identities are all correct. Given the Section 3 formulas, the conclusion follows.

The deduction of those Section 3 formulas is the sole gap. The expressions
`Pow(M) = c^2 X sin(z-lambda) / (4 Z sin lambda)` and `Pow(N) = d^2 X sin(y-kappa) / (4 Y sin kappa)`
are obtained from a "directed sine rule" in triangles `AMT` and `ANU` whose sign conventions are asserted rather than derived: with directed angles modulo pi the sines are defined only up to sign, the side of `M` on which the second intersection `T` falls is not determined, and the degenerate positions (line `MK` tangent to the circle, or passing through `A`) are not addressed. The formulas are in fact correct as stated — the independent numeric test matched both, signs included, to 1e-10 over 263 in-configuration instances — so the omission is a routine directed-lengths verification, local and mechanical, but it is load-bearing: an undetected sign flip in either formula would break the final equality.

**Verdict: complete in substance, one uniquely local mechanical repair outstanding, 6/7.**

## Problem 3 — 7/7

The claiming-phase lemma is proved by the clean two-sided greedy argument: the first claimant can secure the odd ranks, the second the even ranks, and the two guarantees exhaust the total. The cancellation lemma (equal pairs delete from a sorted list without changing the alternating sum, leaving at most the residual total `d`) and the matching lemma (common refinement of two concatenations within `p+q-1` cuts) are both correct.

The upper bound covers the under-marking case by bisection and the full case by the subset-sum pigeonhole, with the `Q` empty and `d = 0` subcases handled; the cut budget `|P|+|Q|-1+|R| = n` is exact. The lower bound uses the dyadic marking; the pairing multigraph on `n+1` parents with at most `n` edges has a tree component, its bipartite signing is bounded above by the alternating sum via the triangle inequality, and below by `u` since the largest dyadic value present exceeds the sum of all smaller ones. Both constructions were simulated in exact arithmetic without a violation.

**Verdict: complete, 7/7.**

## Problem 4 — 7/7

The preliminary claim (an angle `m theta` forces a win within `m-1` cuts, by splitting off `theta`) is a correct induction. Sufficiency combines it with the integer-crossing lemma, whose two cases (some coordinate above one; all below one forcing sum exactly two) are both right, and the crossing cut hands whichever child Shan-Yu keeps a positive integral label below `n`. Necessity works in the subgroup `H = theta Z`: from the equilateral start all three angles stay outside `H`, since the four ways both children could carry an `H`-angle each force `a`, `b`, `c`, or `180°` into `H`. As `theta` itself lies in `H`, Mulan never wins. The two directions give exactly `theta = 180°/n`, `n >= 2`.

**Verdict: complete, 7/7.**

## Problem 5 — 7/7

Substituting `x = f(y)` pins the middle of the chain between two copies of `f(y)`, giving `f(f(y)) = 2 f(y) - y` with no squaring needed, hence arithmetic orbits and `d >= 0`. The bound `d(x) - d(y) <= Phi(x, f(y))` with the rationalized form of `Phi` and the floor-aligned orbit points forces any two positive values of `d` to coincide, the denominator growing linearly along the aligned pairs. Openness of the zero set follows from continuity of `Phi(x, z)` at `x = z`; openness of the positive set from the strict failure of the AM–GM half at `x = p`, `y = p`. Connectedness excludes coexistence, and the verification step is exactly QM–AM and AM–GM applied to `x` and `f(y)`. All identities verified symbolically.

**Verdict: complete, 7/7.**

## Problem 6 — 7/7

The enumeration claim (the sequence lists `S ∩ [a_1, ∞)` in increasing order) is proved by minimality at the first skipped index. The two lemmas are correct: any two elements of `S` share a factor (via the multiple `kx` with `k ≡ 1 mod y`, which must be a term), and any non-member above `a_1` has an earlier coprime term. The set `M` of divisibility-minimal squarefree members of `S` covers `S` by multiples.

The descent lemma is the crux and it is sound: for `m ∈ M` with `q | m` and `m/q > a_1`, the cofactor is a non-member, the coprime witness term supplies a strictly smaller member of `M`, and coprimality to the cofactor plus squarefreeness force the shared prime to be `q` itself, so `q` survives the descent to a member with cofactor at most `a_1`. If infinitely many primes occurred in `M`, pigeonhole on the bounded cofactors would force a fixed term to be divisible by infinitely many primes. Hence finitely many primes, `M` finite, membership in `S` periodic with period `L`, and counting `T` elements per window gives `a_{n+T} = a_n + L` for every `n >= 1` directly, with no eventual-to-global step. Simulation over nineteen starting values confirmed the global period.

**Verdict: complete, 7/7.**
