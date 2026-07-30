# Math-explorer report: menu-coverage gap for the general-n upper bound (round 7)

**Lens.** Scouted numerically what is happening in `minimax-mixed-duality`'s
reported ~26%-uncovered region of the `m=3` menu-coverage sweep, and how the
menu `{DOM, HALVE, TAIL-SNIP, SANDWICH, PARTIAL-DOM}` behaves at `m=4,5`.
Question: is there a missing named move that completes the menu, or does the
menu approach structurally break down? Tooling: Python,
`scipy.optimize.differential_evolution` as an exploratory global-optimum
oracle over Xiang Yu's full response space (all mark-allocation vectors,
continuous cut positions), cross-checked against direct construction/`Fraction`-style
exact evaluation of named-lemma formulas. Not a proof; all claims below are
numerical evidence with concrete witnesses, reproducible from the scripts left
at `/tmp/round-7/explore.py` and `/tmp/round-7/explore2.py`.

**Headline finding.** The menu gap is *not* a single missing move. Two things
are true simultaneously:

1. **A large chunk of the reported ~26% gap at `m=3` is an artifact of
   applying each certified lemma only once/shallowly, not of a missing
   construction.** Recursively composing the *already-certified* lemmas
   (HALVE recursing into the tail with the remaining budget; PARTIAL-DOM's
   residual `r` further refined with leftover budget) raises `m=3` coverage
   from ~75% (shallow, matches the reported ~74%) to **92%** with *zero* new
   lemmas — just correct recursive use of what's already certified.
2. **The true remaining gap needs at least two genuinely new constructions**
   (below), which close `m=3` and `m=4` to 100% on a 40-sample sweep each,
   **but a residual gap reappears at `m=5`** that these do not close — and
   its witnesses require *three-piece* simultaneous coordination, up from
   two. This is evidence the required coordination degree grows with `m`,
   which is a structural warning sign for a finite named-move menu.

## Reproducing the reported ~74%/92% split (m=3, budget=2)

Direct check, 100 random `m=3` configs, budget `n=2`, target `c(2)=4/7`:

- Applying each of DOM / HALVE / TAIL-SNIP / SANDWICH exactly once (no
  recursion) — the "shallow menu" — covers **75/100**, matching
  `minimax-mixed-duality`'s reported ~74% on its own independent sweep.
- The *same four lemmas*, but with HALVE allowed to recurse into the tail
  (apply the whole menu again to `T` with the remaining `budget-1`) and
  PARTIAL-DOM allowed to try every `j` (not just maximal `j`) — covers
  **92/100**, with no new lemma added.

**Takeaway for next round:** before hunting for new moves, make sure the
`universal-adversary-strategy` casework write-up is using each certified
lemma *recursively/compositionally*, not as a one-shot check — a third of the
apparent gap disappears just from that.

## Two new constructions found by inspecting the optimizer's solutions

For the remaining ~8% at `m=3`, I ran a global optimizer (all allocation
vectors, DE over cut positions) to find the true optimum and read off its
structure on concrete failing witnesses.

**Witness 1** `A=(0.5798,0.3515,0.0687)`, `m=3`, budget 2. DOM applies
(`p1≥S`) but gives `oddrank=p1=0.5798>c(2)=0.5714` — DOM alone cannot beat
the target when `p1` itself already exceeds it. True optimum
`≈0.53435 < c(2)`, found allocation: **1 mark tying `p1` down to `p2` (a
PARTIAL-DOM `j=1` move, residual `r=p1-p2`), then the *second* mark spent
**halving the residual `r`** instead of leaving it as one piece.** Exact
structure of the optimum: `p1 → (p2, r/2, r/2)` with `r=p1-p2`; resulting
sorted list `p2, p2', r/2, r/2, p3` where `p2'≈p2` (an exact tie at the
boundary) gives `oddrank = p2 + r/2 + p3`.

This is not a new *primitive* — it is **Lemma PARTIAL-DOM composed with
Lemma SPLIT applied to its own residual `r`** (SPLIT already handles
"split any sorted position given the local ordering hypothesis," and
PARTIAL-DOM already tells you `r`'s exact rank). Neither
`universal-adversary-strategy`'s file nor `partial-dom.md` currently states
or uses this composition — PARTIAL-DOM's write-up spends its full `j` marks
and stops; it never revisits `r` with leftover budget. **Recommend a small
new corollary, "PARTIAL-DOM + residual-refine": after computing PARTIAL-DOM's
`(j,r)`, if budget `>j` remains, apply Lemma SPLIT to `r` in place (using its
already-known sorted rank inside the merged multiset) recursively.** This is
mechanically easy (both ingredient lemmas are already certified) and, on its
own, close a meaningful chunk of the residual gap.

**Witness 2** `A=(0.583,0.3461,0.0709)`, `m=3`, budget 2. Neither DOM
(`p1<S`... check: here `p1≥S` may or may not hold, but regardless) nor HALVE
(`p1<2p2`: `0.583<0.6922`, fails) fires with the standard hypotheses. True
optimum `≈0.53545`, found allocation: **both `p1` and `p2` halved
simultaneously** (`p1→(p1/2,p1/2)`, `p2→(p2/2,p2/2)`), giving sorted order
`p1/2,p1/2,p2/2,p2/2,p3` and `oddrank = p1/2+p2/2+p3`. This needs only
`p2≥2p3` (**not** `p1≥2p2`) — a strictly weaker, different hypothesis than
Lemma HALVE's.

This is a genuinely new base construction, **"cascade/multi-HALVE": halve the
top `K` pieces simultaneously whenever `p_K≥2p_{K+1}`** (Lemma HALVE is the
`K=1` case). Proof sketch (rank-shift, same technique as HALVE/DOM/SPLIT):
the `K` halved pairs occupy the top `2K` ranks in the order
`p_1/2,p_1/2,\dots,p_K/2,p_K/2` (valid since `p_1\ge\cdots\ge p_K` implies
the halves are already sorted, and `p_K/2\ge p_{K+1}` keeps the tail below
all of them); each pair contributes its half-value once to `oddrank` (odd
rank `2i-1`), and the tail shifts by the even number `2K`, preserving parity,
so `oddrank(B) = \sum_{i=1}^K p_i/2 + oddrank(\text{tail from } p_{K+1})`.
This looks like a clean, easily-certifiable lemma — essentially free, given
the existing DOM/HALVE/SPLIT proof machinery.

## Effect of adding these two constructions plus independent multi-piece ties

Built an "extended menu" = certified menu (used recursively) + multi-HALVE +
PARTIAL-DOM-with-residual-refine + a discrete search over **independent
single-cut ties** (any subset of up to `budget` pieces, each split once with
one fragment set to exactly equal some *other, untouched* piece's value — the
generalization suggested by the round-6 `m=4` witness "`p1` ties `p3`, `p2`
independently ties `p4`"). Coverage on fresh 40-sample sweeps, budget `=m-1`,
target `=c(m-1)`:

| m | budget | target | old shallow menu | extended menu |
|---|---|---|---|---|
| 3 | 2 | 0.5714 | ~74–75% (matches `minimax-mixed-duality`) | **40/40 = 100%** |
| 4 | 3 | 0.5333 | ~53% (32/60 in a 60-sample check) | **40/40 = 100%** |
| 5 | 4 | 0.5161 | ~35% (21/60) | **38/40 = 95%** |

So the extended menu is a real, substantial improvement — full coverage at
`m=3,4` in these sweeps — but **not complete at `m=5`**.

## The `m=5` residual: coordination degree appears to grow with `m`

Two `m=5` witnesses survive the extended menu; running the global optimizer
on them (finer settings, `maxper=3`) confirms the true optimum genuinely
beats `c(4)` but needs **three-piece simultaneous coordination**, not two:

- `A=(0.4265,0.2536,0.1747,0.1014,0.0438)`: true optimum `≈0.5009<0.5161`,
  optimal allocation `(1,0,1,2,0)` — **one mark on `p1`, one mark on `p3`,
  two marks on `p4`** (a 3-way split of `p4`), all with jointly-tuned,
  non-half, non-tie-to-a-fixed-value ratios (one of the `p3` fragments sits
  almost exactly at 0, i.e. close to a degenerate/wasted-mark boundary per
  Lemma TIE-NECESSARY, but not exactly).
- `A=(0.3415,0.3023,0.1664,0.1404,0.0494)`: true optimum `≈0.50225<0.5161`,
  optimal allocation `(2,1,0,1,0)` — **two marks on `p1`, one on `p2`, one on
  `p4`** — again three distinct pieces touched with jointly-tuned ratios.

Both are qualitatively like the `m=4` "`p1` ties `p3`, `p2` ties `p4`"
witness from round 6, but with **one more piece drawn into the coordinated
move** (3 pieces touched at `m=5` vs. 2 at `m=4`). The extended
pairwise-tie search (which only allows one cut per piece, tied to an
*untouched* value) cannot express this because here `p4` itself receives two
cuts (a 3-way split of a non-`p1` piece) — a shape not covered by any
construction tried so far, including the round-6 file's own SANDWICH/PARTIAL-
DOM/DOM family.

## Assessment: is there one more move that finishes the menu, or does the approach break down?

The evidence points toward the latter, at least for a menu of a **fixed,
small number of named move-shapes**:

- Going from `m=3` to `m=4` to `m=5`, the minimal witnesses that defeat the
  current (extended) menu require coordinating **2, then apparently 3**
  distinct pieces with mutually-dependent split ratios. Nothing in the data
  suggests this stops growing — it is consistent with (though does not
  prove) the coordination degree scaling with `m`, i.e. with `n`.
- This matches what Lemma TIE-NECESSARY already tells us structurally: the
  optimum lives at a cell-boundary of the *full* `k`-dimensional response
  polytope (`k` up to `n` marks, all potentially interacting), not at the
  boundary of any single piece's local sub-problem. A finite catalog of
  named single/pairwise moves is trying to enumerate special low-dimensional
  faces of an object whose relevant faces, in the worst case, may need all
  `k` coordinates simultaneously.
- Every time a witness has been chased down this round (as in rounds 5–6),
  the "fix" was not a *new independent primitive* but a **deeper
  composition** of the same few mechanisms (duplicate-and-cancel from DOM,
  rank-shift-preserving split from SPLIT, parity-preserving cascade from
  HALVE) applied to more pieces at once. This suggests the right target for
  next round is not "find move #7, #8, ..." but a **general theorem**: given
  Lemma TIE-NECESSARY's finite discrete search (a matching/assignment
  between "pieces receiving cuts" and "tie targets," at each of up to `n`
  marks), prove *some* member of that discrete search always achieves
  `≤c(n)` — i.e., attack the matching/assignment optimality question
  directly (as `universal-adversary-strategy`'s current open gap already
  states), rather than continuing to special-case its low-order instances.

## Concrete recommendations for next round

1. **Cheap, high-value fix first:** certify "PARTIAL-DOM + residual-refine"
   (composing already-certified PARTIAL-DOM and SPLIT — no new proof
   machinery needed) and "cascade/multi-HALVE" (`K`-fold simultaneous
   halving, `p_K≥2p_{K+1}`, same rank-shift technique as HALVE/DOM). Both are
   short, mechanical proofs given what's already certified, and numerically
   close a large fraction of the previously-reported gap (75%→92%+ at `m=3`
   from recursion alone, plus these two closing `m=3,4` fully in sampled
   sweeps).
2. **Do not expect a `m=5`-closing single move.** The `m=5` witnesses above
   are recorded exactly (`A=(0.4265,0.2536,0.1747,0.1014,0.0438)` and
   `A=(0.3415,0.3023,0.1664,0.1404,0.0494)`, budget 4, target
   `c(4)=16/31≈0.5161`) so a future round doesn't need to re-discover them;
   both need genuine 3-piece coordination with irrational-looking (non-tie,
   non-half) ratios.
3. **Reframe the open problem.** Given the growth pattern, recommend the
   outliner consider retargeting `universal-adversary-strategy`'s remaining
   gap from "complete the menu" to "prove the TIE-NECESSARY-implied
   matching/assignment problem always has a solution `≤c(n)`" — e.g. by
   induction on `n`/`m` using the multi-HALVE and PARTIAL-DOM-residual
   corollaries as base mechanisms inside the inductive step, rather than as
   terminal named moves. This is consistent with what the round-6 file
   already flagged as the sharpest open sub-problem; this round's numerics
   make the case more concrete (the coordination degree visibly grows from 1
   move at `m≤2`, to 2 pieces at `m=3,4`, to 3 pieces at `m=5`).

## Scripts left for reuse

- `/tmp/round-7/explore.py` — `oddrank`, generic response builder/global DE
  optimizer (`true_optimum`), the certified menu with recursion
  (`menu_best`), and the independent-tie discrete search
  (`extended_tie_search`).
- `/tmp/round-7/explore2.py` — adds `multi_halve_value` and
  `partial_dom_residual_menu` (the two new constructions above) and the
  combined `full_menu_best`, plus the `m=3,4,5` sweep that produced the
  coverage table.
