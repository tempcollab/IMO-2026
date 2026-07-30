# Non-concavity of V(p) (negative result) + exact n=2, one-mark-on-top value

Certified from `majorization-smoothing.md` (round 4, Step 0 reconciliation).
Independently re-verified by the proof-reviewer: closed form (†) checked
against a 20001-point grid search at all three reference points (exact
match), and the true global minimum over all 10 valid Xiang-Yu compositions
(`k_1+k_2+k_3≤2`) checked by grid search at `p=mid`: confirmed minimum is
exactly 0.52, matching (†), no composition beats it.

## Closed form (†): n=2, exactly one mark spent splitting p_1, tail untouched

For sorted `p=(p_1,p_2,p_3)`, `p_1+p_2+p_3=1`, the value Xiang Yu achieves
using a single mark that splits only `p_1` (tail `p_2,p_3` untouched) is
exactly
```
V_{(1,0,0)}(p) = min( max(p_1, 1-p_1),  p_1/2 + p_2 ).
```

*Proof.* Full six-region case analysis over the split point `x∈[p_1/2,p_1]`
(WLOG by symmetry), each region shown affine or constant in `x`; monotone
regions push to their boundary with a constant region, giving
`max(p_1,1-p_1)` (from the "tie with p_2 or p_3" boundary) and `p_1/2+p_2`
(from the equal-split boundary `x=p_1/2`) as the two candidate values, and
their min is the achieved optimum. See source file for full case table.

## Negative result: V(p) := min_B oddrank(B) is NOT concave in sorted p

At `n=2`: `p1=(0.7,0.2,0.1)` gives `V=0.55`; `p2=(0.34,0.33,0.33)` gives
`V=0.50`; `mid=(0.52,0.265,0.215)` gives `V=0.52 < (0.55+0.50)/2=0.525`.
Reproduced exactly (not an optimizer artifact) via the closed form (†) above,
and confirmed to be the TRUE global value at all three points (checked
against every one of the 10 valid Xiang-Yu compositions with budget ≤2, not
just composition `(1,0,0)`).

*Structural mechanism (why no refinement of the "concave via affine pieces"
strategy can rescue this).* `V(p)` is a min of: an affine function
(`p_1/2+p_2`) and `max(p_1,1-p_1)`, which is itself a genuinely convex
function of `p_1` (a min of two affine pieces would be concave, but this is a
MAX of two affine pieces, hence convex). A min of a concave and a convex
function is in general neither concave nor convex, and dips below the affine
chord exactly where the convex branch is active and lower — exactly what
happens at `mid`. This rules out ANY "refine the discrete split-type until
each piece is affine, then argue V is a min of affine functions hence
concave" strategy: refining does produce affine pieces, but they combine via
an inner `max` before the outer `min`, and that inner `max` is intrinsic to
the game (which of two near-tied ranks Xiang Yu's split ties to), not an
artifact of insufficient refinement.

## Status
Certified as a negative result + a genuine exact data point (n=2, k=1,
tail-untouched value formula). Rules out the entire "global concavity of V"
proof strategy for this problem — no future approach should re-attempt
proving V concave in the sorted-p domain.
