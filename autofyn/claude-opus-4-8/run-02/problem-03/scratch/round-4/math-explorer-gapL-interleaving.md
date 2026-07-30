## imo-2026-03 — lens: GAP L residual GAP-LB′ (joint rank-interleaving invariant)

### Setup recap (verified against current.md / induction-recursion.md, no discrepancies found)
In the integer-unit normalization, Case B splits `F = Y ⊎ Z`, `Y` = top-descendants (sum `2^n=2θ`,
`θ=2^{n-1}`), `Z` = bottom-descendants (sum `2^n-1=2θ-1`, all parts `≤θ`, `Dbot=altsum(Z)≥1` by IH).
The residual "doubly-balanced" region has `y₁ = max(Y) < θ+1`, i.e. **all of Y also lies in `(0,θ]`**
(the two conditions together literally collapse to: Y and Z are BOTH multisets confined to `(0,θ]`,
sums `2θ` and `2θ-1` resp., `|altsum(Y)-Dbot|<1`). Needed: `D̃ = altsum(Y⊎Z) ≥ 1`.

### Key reformulation found this round (new, not in prior approach files)
Because `sum(Y) − sum(Z) = 2θ − (2θ−1) = 1` **identically**, the target `D̃ ≥ 1` is *exactly*
```
D̃ ≥ sum(Y) − sum(Z)                                   (★J, "joint merge-domination")
```
This is a cleaner, more symmetric restatement than the `2λ(O_Y^<∩O_Z)≤…` form in current.md — same
content, but it foregrounds the right general-purpose lemma to hunt for: a "merged-sort alternating
sum ≥ sum-difference" fact.

**This general inequality is FALSE for arbitrary Y, Z** (even under the natural side constraints):
- Fully arbitrary Y,Z (no sum/bound constraints): `D̃ ≥ sum(Y)-sum(Z)` fails badly (~25% violation
  rate over 2·10^5 random trials, min residual `≈ -17.6`). [`/tmp/round-4/scratch/probe5.py`]
- Y confined to `(0,θ]` summing to `2θ`, Z *arbitrary* in `(0,θ]` with `altsum(Z)≥1` but sum(Z)
  unconstrained: still fails (found `D̃≈0.046` in the region `Dbot≥1`). [`probe6.py`]
- Even forcing **both** sum constraints (`sum(Y)=2θ`, `sum(Z)=2θ−1`, both bounded by `θ`, `Dbot≥1`):
  still **fails** — found `D̃≈0.135 < 1` with a *totally generic* `Z` (not built by the recursive
  dyadic cutting process). [`probe7.py`, explicit counterexample: `Y=[3.31,1.75,1.72,1.22]`,
  `Z=[3.31,1.20,1.06,1.00,0.23,0.20]`, `Dbot=2.20≥1`, `D̃=0.135`.]

**Conclusion: the theorem is false for a "scalar-summary" Z (any multiset with the right sum and
`Dbot≥1`) — it genuinely needs Z's specific origin as a `≤(n−1)`-cut response of the literal
`(n−1)`-dyadic `{1,…,2^{n−1}}`, not merely its aggregate statistics.** This is a sharper, numerically
pinned-down version of the "one-sided confinement is refuted" finding already in current.md/induction
-recursion.md — it shows *no* scalar strengthening of the IH (sum, alt-sum, even a location-confinement
of `O_Z`) can suffice; the actual multiset structure of `Z` (or at least its full recursive cut-tree)
must be used.

### Numerical study of the true extremal family (global optimization, not just random sampling)
Ran a Nelder–Mead global search (softmax/sigmoid parametrization, many restarts) over all `(a,b)`
splits and all choices of which bottom pieces get cut, for `n=2,3` [`probe4.py`]. Result: **the true
global minimum of `D̃` over genuine Case-B configurations is exactly 1** in every `(a,b)` cell tested,
confirming current.md's numerics, and — importantly — **the minimizers found by the global optimizer
lie inside the doubly-balanced residual region** (e.g. n=2, a=2,b=0: `y₁≈2.64<θ+1=3`, so this is
not covered by (◇◇)/(★★) at all — the hardest case really is the bottleneck).

**Structure of the extremal (D̃=1) configurations — the "shadow/zigzag" pattern.** In every minimizer
found, sorting `Y∪Z` descending gives a near-perfect **T/B alternation**, and each `Y`-part sits just
*above* (by an infinitesimal margin) some `Z`-value:
- n=2, a=2,b=0: `Y=(2.64,1.32,0.04)`, `Z=(2,1)` → merged labels `T,B,T,B,T`. `altsum = (2.64-2)+(1.32-1)+0.04 = sum(Y)-sum(Z) = 1` exactly.
- n=3, a=3,b=0: `Y=(4.30,2.25,1.40,0.05)`, `Z=(4,2,1)` → labels `T,B,T,B,T,B,T`, same telescoping.
- n=3, a=2,b=1 (cut piece "1"): `Y=(4.03,2.47,1.50)`, `Z=(4,2,1,0)` → labels `T,B,T,B,T,B,B`: a
  strictly-alternating **prefix** followed by leftover `Z`-elements (all below the smallest `Y`) —
  and the trailing `B,B` block contributes `0` net (it starts on a `−` sign and its own sub-alt-sum
  is the *nonneg* level-measure discrepancy of the tail, which the optimizer drives to exactly 0 by
  packing the extra `Z`-mass at `0`).
- n=3, a=1,b=2 (cut pieces "1" and "4" i.e. bidx=(0,2)... one case gave two equal `Y=(4,4)` — labels
  `T,T,B,B,B,B,B`, `altsum = 4-4+2.44-2+1.56-1+0 = 1` — here the *leading* pair is `T,T` (no
  cancellation from `Y` against `Z` at the top at all), and the whole discrepancy is carried by the
  `Z`-tail's own internal alt-sum (`=1`, matching `Dbot` exactly, since `D_top^< = altsum(4,4)=0`).

**Upshot — the telescoping identity behind (★J).** When the merge order strictly alternates
`T,B,T,B,…,T` for the *first* `min(|Y|,|Z|)+1` entries (or more precisely, whenever every `Y`-part
that appears has no two `Z`-parts strictly between consecutive `Y`-parts other than one), the
alternating sum telescopes to exactly `sum(Y_{used}) − sum(Z_{used})` plus a residual tail-alt-sum
that is *always ≥ 0* (level-measure identity applied to the tail alone, which is a plain sorted
descending list — the alt-sum of any sorted descending list is `≥ 0`, indeed `≥ 0` term-by-term via
consecutive-pair grouping, exactly the argument already proved for Lemma G). **This gives a clean,
completely general two-part decomposition:**
```
D̃ = [telescoped head, = sum(Y_head) − sum(Z_head)] + [alt-sum of tail, ≥ 0].
```
The open question is *only*: can it be shown that **the head telescoping always uses up all of Y
and covers a Z-mass ≤ sum(Y) − 1** (so the head total is `≥ 1`), i.e. that `Y`'s parts never end up
"trapped" below too much `Z`-mass? This is the honest content of GAP-LB′, now isolated as a purely
combinatorial merge-order claim, independent of the level-measure machinery.

### Can this be turned into a genuine monovariant? (partial answer — not fully closed)
Sketch of a candidate but **incomplete** monovariant: define for the merged sorted sequence, scanning
top-down, a running counter `c` = (# Y-elements seen so far) − (# Z-elements seen so far). The
alt-sum telescopes cleanly exactly on stretches where `c` stays in `{0,1}` (perfect alternation); a
"run" of `k` consecutive same-label elements shifts `c` by `k` and changes the telescoping algebra —
concretely, `k` consecutive `Z`'s in a row (a "B-run") make those `k` elements contribute an
**internal nonneg alt-sum** (good — helps), but a run of `k` consecutive `Y`'s ("T-run") makes them
contribute their **internal alt-sum**, which for `k≥2` could in principle be small (if the run's
values are close together it approaches `0`, not `sum` of those elements) — this is exactly where a
counterexample-style loss could occur, and matches the failed-generic-Z counterexample structure. I
could **not** complete this into a proof — the missing ingredient is a bound on how much of `Y`'s
total mass can appear in "T-runs" (as opposed to strictly alternating with Z), and this is precisely
where the actual recursive structure of Z (that it comes from cutting a dyadic set, so its OWN
sorted sequence has bounded local density / cannot have long stretches without a fresh dyadic
"anchor" value nearby) must be invoked. **Recommend:** next round attack this specific sub-claim —
"Y's T-runs (against the specific dyadic-derived Z) carry total mass ≤ 1 less than |T-run| would
suggest" — via strong induction on Z's own recursive decomposition (Z = Y'⊎Z' at threshold θ/2),
i.e. a genuinely **two- (or multi-) level joint induction**, not induction that first collapses Z to
the scalar `Dbot≥1`.

### Exchange / canonical-form route — partially promising, not verified as a full argument
Because the extremal configs have `Y`'s cut-fragments landing at generic irrational-looking positions
"just above" `Z`'s dyadic breakpoints (not canonical numbers), a **continuity/compactness + smoothing
argument** is plausible: the space of Case-B configurations in the closed doubly-balanced region is
compact (cut positions in closed bounded simplices), `D̃` is continuous, so a global min is attained;
one could then try to show any minimizer must be a *boundary* point of the parameter simplex (e.g. one
of the `Y`-parts degenerates to `0`, per the `y₁≈0.04, 0.05` pattern seen in every minimizer above!),
which would let an inductive "remove the vanishing part" argument reduce `a→a−1` — **this exactly
mirrors the observed numerics: in every extremal config found, the smallest `Y`-part is driven to (or
very near) `0`.** This is a genuinely different, not-yet-tried angle: **prove directly that WLOG at
the Case-B minimum, one top-fragment has length `0`** (i.e. the optimal Xiang response effectively
uses `< a` cuts on top), which would reduce Case B with `a` cuts to Case B with `a−1` cuts by an
exchange argument, bottoming out at `a=1` (a single top cut), a case that might be tractable by hand.
This has NOT been attempted by any approach file — flag as a fresh sub-opening for the outliner.

### Crux corpus (games-and-strategy, invariants-and-monovariants, combinatorics) — checked, no strong match
Queried `combinatorics` × `games-and-strategy` (39 hits) and searched all cruxes for
alternat/merge/interleav/sorted/rank/discrepancy keywords (201 hits, scanned). **No genuinely
analogous crux found** for "alternating sum of a merged sorted sequence from two structured sources."
The closest tangential ones:
- `aimo-0117` (games-and-strategy): dyadic/geometric powers-of-two sequence where "the single largest
  value strictly exceeds the sum of all others" — same *flavor* of dyadic-domination idea used
  already in the Domination corollary (C3) / half-total single-crosser identity, but not about merges.
- `aimo-0146` (double-counting / extremal-principle): an exchange-smoothing argument pushing weight
  toward higher elements of a sorted sequence to extremize a weighted sum — structurally similar in
  *spirit* to the "push the vanishing top-fragment" exchange idea above, but the problem (min-cost
  matching over degree sequences) is not analogous enough to adapt directly.
Neither is a real match; **report: none directly analogous**, this residual gap appears to be a
genuinely fresh combinatorial fact specific to this problem's recursive dyadic structure.

### Recommendation summary for the outliner
1. The residual is best restated as **`D̃ ≥ sum(Y) − sum(Z)` (≡ 1)**, a merge-domination claim — this
   reformulation is cleaner than the `2λ(∩)` form and should replace it in the write-up.
2. This general merge-domination fact is **false** without Z's genuine recursive structure (three
   numerically-verified counterexamples now on record, see probes 5–7) — do NOT attempt to prove
   (★J) as a free-standing lemma about arbitrary bounded multisets; it must use Z's actual cut-tree.
3. Two live sub-openings, neither closed:
   (a) **Head/tail telescoping + bounded-T-run mass**, via a two-level joint induction on Z's own
       recursive split (Z = Y'⊎Z' at θ/2) rather than collapsing Z to `Dbot≥1` first;
   (b) **Exchange/degenerate-boundary argument**: show WLOG at the Case-B minimum one top-fragment
       has length 0 (strongly suggested by every numerical minimizer having its smallest Y-part → 0),
       reducing `a` cuts to `a−1` cuts inductively.
4. Both are genuinely new angles not in `induction-recursion.md`'s prior notes — worth a slug each if
   the outliner wants to diversify beyond "just try harder on the same merged-order idea."

### Dead ends (confirmed / reconfirmed, do not retry)
- One-sided confinement of `O_Z` or `O` to a "high" region — REFUTED (carried over from round 3,
  reconfirmed here with the sharper reformulation: even the *aggregate* strengthenings sum(Z),
  `altsum(Z)≥1` are insufficient; only Z's full multiset/tree structure works).
- Proving `D̃ ≥ sum(Y)-sum(Z)` as a general two-multiset lemma (no side info about Z's origin) —
  numerically refuted (three independent counterexample searches, probes 5,6,7).
- `W(n−1,b) > u_{n−1}` strict bound — already retired per current.md, reconfirmed consistent.

### Small-case / intuition notes (all labeled conjecture / numerical evidence only)
- Global-optimum `D̃ = 1` (not just `≥1`) is exactly attained in the doubly-balanced region for every
  `(a,b)` split tested at `n=2,3` — the theorem is tight there, not slack, so any successful bound
  must be essentially sharp, not a loose estimate.
- Every observed minimizer drives the smallest top-fragment to (near) `0` — strong structural hint
  supporting the exchange/degenerate-boundary route above.
- The label-string alternation pattern in every minimizer is "maximal-alternation-until-Y-exhausted,
  then leftover-Z-tail" — supports the head/tail telescoping decomposition as the right lens, even
  though closing it needs Z's tree structure.
