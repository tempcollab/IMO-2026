# Lemma ONE (dyadic top-scale dichotomy) — CERTIFIED (round 4)

**Statement.** In any refinement of `C_n = {2^n, 2^{n-1}, …, 2, 1}` (each original piece
partitioned, total added parts ≤ n), at most one final piece exceeds `2^{n-1}`.

**Proof.** The fragments of the top piece `2^n` sum to `2^n`; two of them each `> 2^{n-1}`
would sum to `> 2^n`, impossible — so at most one top-fragment exceeds `2^{n-1}`. Every
fragment of a non-top piece is `≤` its parent `≤ 2^{n-1}`. Hence at most one final piece
`> 2^{n-1}`. ∎

**Certification.** Elementary (superincreasing). Reviewer-approved round 4. This gives the
disjoint exhaustive lower-bound dichotomy: `a ∈ {0,1}` final pieces `> 2^{n-1}`.
(Identical to parity-measure-potential's "dyadic top-scale dichotomy".)
