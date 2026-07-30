# Two-leftover transport lemma (GAP-A)

**Source:** `tail-count` §12, round 4. Corollary of `telescoping-block-lemma` (GAP-B(d)).

## Statement

In a cascade refinement of the dyadic tower `T_n` (tower units, total `D_n = 2^{n+1}−1`) where the top piece `2^n` is split into `≥ 3` fragments via cascading splits, consider a breakpoint (tie) config where exactly two fragments `a, d` are non-dyadic and all other fragments are dyadic (each equal to a tower piece `2^k, k < n`), pairing off with the corresponding tower pieces. Let `t` be the unique unpaired tower piece (the only tower piece whose count is odd). Then the spine is `{a, t, d}` (`a > t > d`), and

$$a + d = t + 1, \qquad D = a - t + d = 1.$$

## Proof

By the cascade structure, all fragments derive from the top piece `2^n`, so their total mass is `2^n` (telescoping, `telescoping-block-lemma` (b)). The dyadic fragments each equal a tower piece and pair with it (by `strong-breakpoint-group-structure`: at a strong breakpoint, non-dyadic fragments form adjacent-equal groups; here each non-dyadic value appears exactly once, so the lone non-dyadic survivors are `a, d`, and the dyadic fragments pair with tower pieces of the same value by `spine-pair-cancellation`). The paired fragment mass equals the paired tower mass (each pair: fragment = tower piece, same value). The unpaired tower mass is `t` (the single survivor). The total tower mass below `2^n` is `2^n − 1`. So:

- (paired tower mass) `= (2^n − 1) − t`,
- (paired fragment mass) `= (paired tower mass) = (2^n − 1) − t` [each pair: same value],
- (unpaired fragment mass) `= a + d = 2^n − (paired fragment mass) = 2^n − (2^n − 1 − t) = t + 1`.

The sorted config places all fragments at `+` positions and all tower pieces at `−` positions (the interleaved order `{a, t_1, f_1, t_2, f_2, ..., d}` where tower pieces `t_j` sit at even positions and fragments at odd positions). By `telescoping-block-lemma` (d):

$$D = 2^n - (2^n - 1) = 1.$$

Equivalently, the spine `{a, t, d}` has `D(spine) = a − t + d = (t + 1) − t = 1` (by `spine-pair-cancellation`, `D(config) = D(spine)`). ∎

## Scope

This proves `D = 1` for the spine-3 cascade case (and, by the same `telescoping-block-lemma` (d) mechanism, for spine-5 and spine-7 cascade cells where all fragments sit at `+` and all tower pieces at `−`). Corollary of `telescoping-block-lemma` (d); the mass identity `a + d = t + 1` is the spine-length-3 instance of `gaps-leftover-identity`.

## Verification (not a proof step)

T_3 spine-3: `{a, 4, 2, 2, 1, 1, d}` with `a + d = 5 = t + 1` (`t = 4`). `D = (a+d) − 4 = 5 − 4 = 1`. Verified `Fraction`-exact for `a = 9/2, d = 1/2`.
