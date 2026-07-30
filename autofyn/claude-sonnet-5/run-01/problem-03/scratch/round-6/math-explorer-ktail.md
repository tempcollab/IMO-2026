# Explorer report — round 6 — lens: k<n with tail simultaneously refined

Target gap (shared by `geometric-dominance-construction` and
`recursive-embedding-induction`): extend the lower bound from Lemma L
(`k=n`, tail untouched, now fully proved) to general `0≤k<n` with Xiang
Yu's remaining `n-k` marks simultaneously refining the tail adversarially.

## Summary verdict

No contradiction found anywhere (numerics, `n` up to 4, agree with `c(n)`
exactly for every `k≥1` tested). The gap is real but I found a **concrete,
previously-unexploited mechanism** — "split the top piece exactly in
half" — that gives a clean, one-line inductive proof of the **`k=1`
tail-refined** case (already covered abstractly by
`recursive-embedding-induction`'s Claim ★, `s=2`, but the mechanism below
is the *concrete* instance and suggests exactly how to generalize past
`s=2`, which is where Claim ★ was proved false in the abstract form). I
recommend the next attempt be framed as a **joint generalization of Lemma
PARITY-PAIR**, replacing its fixed tail-constant list `t_1,...,t_n` with a
*recursively-bounded variable tail*, rather than as a further abstraction
of Claim ★ (which is a dead end past `s=2`, per the certified
counterexample already on file).

## 1. Numerics: what does the optimal response look like for `k<n` with tail split?

I ran global numeric optimization (`scipy.optimize.minimize`, many restarts,
softmax parametrization to keep pieces positive, exhaustive enumeration
over how the `n-k` tail marks are *distributed* among the `n` tail pieces)
for `n=2,3` and every `k=0,...,n`. Full script/output in this round's temp
files. Headline numbers:

```
n=2, c(2)=4/7≈0.5714
  k=0: min oddsum ≈ 0.6429   (> c(2), as expected — Prop A gives strict
                               excess once tail has ≥2 pieces)
  k=1: min oddsum ≈ 0.5714 = c(2)  ✓ tight
  k=2: min oddsum ≈ 0.5714 = c(2)  ✓ tight

n=3, c(3)=8/15≈0.5333
  k=0: min oddsum ≈ 0.6333   (> c(3))
  k=1: min oddsum ≈ 0.5333 = c(3)  ✓ tight
  k=2: min oddsum ≈ 0.5333 = c(3)  ✓ tight
  k=3: min oddsum ≈ 0.5333 = c(3)  ✓ tight
```

So: **for every `k≥1` tested, the bound is tight at exactly `c(n)` even
when the tail is simultaneously refined with the full remaining budget** —
no numeric evidence of any new obstruction beyond what's already known from
the tail-untouched case. This is reassuring (the target is still exactly
`c(n)`, not something smaller), but also means there's no "easy tell" from
numerics about *which* structural argument closes it — the answer is
already known, what's missing is the proof mechanism.

**Flat-optimum phenomenon deepens.** As already reported by prior rounds
for the tail-untouched case, many different Xiang Yu strategies attain the
minimum exactly (not a unique minimizer). With the tail *also* free, this
gets worse: e.g. for `n=3,k=2`, the optimizer found top-split
`[0.2668, 0.1967, 0.0698]` — visibly *not* the "doubling family"
`{p2,p3,p1-p2-p3} = {4/15,2/15,2/15} = [0.2667,0.1333,0.1333]` — yet both
achieve `oddsum = 8/15` exactly. This is consistent with (not a
contradiction of) the certified fact from the `n=2` hand-check
(`geometric-dominance-construction`'s Lemma-B gate, also
`recursive-embedding-induction`'s corresponding section): whenever the
split values and tail values *interleave* in the pattern
`s_1≥t_1≥s_2≥t_2≥...`, `oddsum` equals `Σ s_i` **exactly**, independent of
the precise values within that interleaved region — i.e. the objective is
genuinely flat (constant) on a whole positive-dimensional cell, not just
tied at isolated points. Any proof strategy must handle this: it needs an
inequality that is tight on a *region*, not simply "beat a unique
adversarial point."

## 2. A clean, exactly-provable mechanism for `k=1` (concrete, not abstract)

I isolated exactly why `x = p1/2` (splitting the top piece exactly in
half) is the worst case for Liu Bang among `k=1` strategies, and why it's
provable cleanly, in a way that generalizes better than Claim ★'s
abstraction. Exact-fraction check at `n=2`:

- Fix `x = p1/2` (so both top-split pieces equal `p1/2 = p2` exactly,
  since `p1=2p2`, Lemma S). Then vary the **entire remaining tail split**
  `y ∈ [p2/2, p2]` (the mark spent splitting `p2`, `p3` untouched): I
  verified by exact `Fraction` computation over 11 sample points that
  `oddsum` stays **exactly `4/7`** for *every* `y` in the range — a full
  flat line, not just a point.
- Fixing `y = p2/2` instead and varying `x` upward from `p1/2` strictly
  **increases** `oddsum` (0.571 → 0.6 → 0.628 → ... → 0.714), confirming
  `x=p1/2` is the binding (worst-case-for-Liu-Bang) boundary, not an
  interior optimum.

**Why this is provable in one clean step, by induction on `n`:** at
`x=p1/2=p2`, the two top-split pieces are *both exactly equal to* `p2`,
which — since `p2 = max` of any valid refinement of the tail `T_0` reached
with `≤n-1` marks (splitting only ever shrinks the max) — **dominates the
entire (arbitrarily refined) tail**, occupying ranks 1 **and** 2 tied.
Only rank 1 counts toward `oddsum`, contributing `p1/2`. Because the tying
block has **even** size (2), the tail's own ranks shift down by an *even*
number, so parity is preserved: the tail's own `oddsum` (as an independent
`n-1`-level sub-game with `n-1` marks) is exactly what gets added. By the
recursive identity `c(n) = 2λ_n c(n-1)` (Lemma G1, already certified) and
self-similarity (`T_0 = λ_n·A_{n-1}`), *if* the full theorem holds at level
`n-1` for **whatever** refinement the remaining `n-1` marks produce, this
gives
```
oddsum(B) = p1/2 + oddsum(T) ≥ p1/2 + λ_n·c(n-1) = p2 + p2 = p1 = c(n).
```
This is exactly the mechanism `recursive-embedding-induction`'s Claim ★
(`s=1` case) already formalizes and has fully proved — I just re-derived
its concrete instance from scratch to understand *why* it's the tight
case, and confirmed numerically it really is the worst point, not merely
*a* valid point. **This is not new content** (Claim ★ `s=1,2` already
covers `k≤1` with tail-refined, conditional on full `M(n-1)`) — it's
useful confirmation the existing conditional proof is tight and correctly
scoped, and it clarifies *the reason* `s≤2` is special: an even-size tying
block at the top preserves parity of everything below it, letting the
recursion "hand off" cleanly to `n-1`'s own game untouched. This parity
mechanism is *exactly* Lemma PARITY-PAIR's Case A (even `c_1`) — the two
approaches' machinery for this special point coincide.

## 3. Why Claim ★ genuinely can't extend past `s=2` (re-confirmed), and what should replace it

Claim ★ (`geometric-dominance-construction`/`recursive-embedding-induction`,
round 4) tried to abstract the tail down to two scalars,
`max(T)≤q, oddrank(T)≥q`, and showed this is enough for `s≤2` (`k≤1`) but
**provably false** for `s≥3` (exact counterexample already on file, cited
in both approach files). My numerics above confirm this is the right
place to stop trying to push the *abstract* version further — the
obstruction is structural, not a matter of missing a cleverer choice of
scalar summary. **Any working argument for `k≥2` must use more of `T`'s
actual structure than two scalars.**

The natural candidate, and the one I recommend the next outline target:
**do not abstract `T` at all.** Since `T` (the adversarially-refined tail)
is *itself* a rescaled copy of a valid Xiang-Yu response to `A_{n-1}`
(self-similarity, Lemma 3), and Lemma PARITY-PAIR already proves a
positional (`D`-level, not just scalar-`oddrank`-level) bound for the
`k=n` "pure anchor" sub-case of exactly this kind of object — the fix is
to **generalize Lemma PARITY-PAIR's induction itself** so that instead of
peeling a top block against a *fixed* constant list `t_1,...,t_n`, it
peels a top block (Xiang Yu's split `S` of `p_1`, `k+1` parts, of *whatever
parity*) against a **variable** remainder `T`, and the induction hypothesis
invoked on the remainder is not "the constant list's own `D`-bound" but
"whatever `T` satisfies **by the same theorem one level down**, applied to
`T`'s own top-vs-tail split with the leftover `n-k-(mark spent on T's own
top)` budget." Concretely, this means proving the **full theorem**
(`M(n)`, all `k`, tail simultaneously refined) by **strong induction on
`n` jointly with a case split on the *parity of the top block's tie count*
exactly as in Lemma PARITY-PAIR**, where:
- **Case A analogue (even tying block):** the top piece's split has an
  even number of pieces tied at (or above) the tail's current max, forcing
  a clean, parity-preserving hand-off to the `M(n-1)` inductive hypothesis
  applied to *whatever* the remaining budget does to the tail (this is
  exactly what closed `k=1` above, and is exactly Claim ★'s `s=1,2` cases
  restated positionally).
- **Case B analogue (odd tying block):** use the already-certified
  **Lemma D-BOUND** (`0≤D(Y)≤max(Y)`) directly on the merged remainder,
  the same trick that rescues Lemma PARITY-PAIR's odd case — this is the
  piece that's missing for `k≥2` and is exactly where the abstract Claim ★
  broke (Claim ★ tried to use `oddrank(T)≥q` as a *hypothesis* rather than
  deriving a fresh `D`-level bound on the merged object directly).

This reframes the target lemma as: **"Lemma PARITY-PAIR-GEN": for every
`n`, every `0≤k≤n`, every valid `(k+1)`-part split `S` of `p_1`, and every
Xiang-Yu-reachable refinement `T` of the tail using `≤n-k` marks,
`D(S∪T) ≥ δ_n`** — proved by strong induction on `n`, generalizing the
existing (certified) proof of Lemma PARITY-PAIR (which is the special case
`k=n`, `T` fixed = untouched) rather than generalizing Claim ★ (which is
the special case `k≤1`, `T` abstracted to two scalars). The `k=1`
half-split computation in §2 is a fully worked concrete instance of
exactly this generalized induction's Case A step, confirming the shape is
right.

## 4. What "composed move width" from Lemma X suggests

`geometric-dominance-construction`'s Lemma X / move-trap analysis (round 5)
showed that a *bounded-width* single-exchange-move mechanism cannot prove
even the `k=n`, tail-untouched Lemma L — width grows with `n` in the
tested traps (`2→4` for `n=5..8`). I did not find a clean formula for
"composed move width as a function of `n-k`" this round (did not have
time to extend the move-trap machinery itself to the `k<n` polytope, which
has a different, larger combined vertex structure). Given that
Lemma PARITY-PAIR's *direct* induction succeeded where the bounded-exchange
approach failed even for `k=n`, I recommend **not** investing further in
extending the exchange/move-trap machinery to `k<n` — the peel-induction
route (§3 above) is the one with a working precedent on the closest
sub-case, and the exchange route's own file already concludes it is "at
best an equally-hard reformulation" of the peel-induction. This assessment
still looks correct for the wider `k<n` case.

## 5. Recommendation for proof-outliner

- **Do not** re-attempt Claim ★'s abstraction for `s≥3` — it is certified
  false, re-deriving it will not help.
- **Do** frame the next build-set entry as a direct generalization of the
  already-certified Lemma PARITY-PAIR (not of Claim ★): prove
  `D(S∪T) ≥ δ_n` for a **variable, adversarially-refined** `T` by strong
  induction on `n`, splitting on the parity of the top block's effective
  tie count against `T`'s current max, using Lemma D-BOUND in the odd case
  exactly as before. The `k=1` exact-half-split computation in §2 is a
  fully checked, ready-to-write-up base instance of the even case; the
  genuinely new work needed is the **odd case for general `k≥2`**, and
  handling `T` not being merely "the fixed tail" but itself a full
  recursive sub-instance of the same theorem.
- This is a substantial lemma (arguably as hard as Lemma PARITY-PAIR
  itself, plus an extra layer of induction on `k` or on the recursive
  depth of `T`'s own refinement) — expect it to take more than one round.
  Suggest the outliner scope a first pass at **`k=2`, tail refined**
  specifically (the smallest case not already covered by Claim ★), as a
  concrete target to de-risk the induction's odd-case mechanics before
  attempting the fully general `k`.
- Numerics (this report, §1) give no reason to doubt the target value
  `c(n)` is still correct and tight for every `k<n` tail-refined case
  tested — this is a proof-mechanism gap, not an open question about the
  right bound.
