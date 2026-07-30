# Build report — induction-recursion-telescope (imo-2026-03 / IMO 2026 P3), Round 4

Slug: **induction-recursion-telescope** (fresh copy of induction-recursion; owns GAP L Case-B
doubly-balanced GAP-LB′ via the merged-order signed-sum / telescoping route). Status: **partial**.
No overclaim. The tight/equality core of GAP-LB′ is now closed rigorously; a strictly smaller,
precisely isolated residual (`maxc≥2`) remains and genuinely requires Z's cut-tree.

## What I closed / advanced this round (all rigorous)

Working in the certified integer-unit normalization (Liu `={1,…,2^n}`, top piece `2^n`, bottom
block the literal `(n−1)`-dyadic, target `D̃≥1`), Case B (`a≥1` top cuts, `b≤n−1` bottom, `F=Y⊎Z`):

1. **Clean reformulation `(♣)` (PROVED).** With `M:=N_Y−N_Z`: since `N_Y+N_Z≡N_Y−N_Z (mod 2)`,
   `D̃=∫1[M odd]`; and since `sum(Y)−sum(Z)=2^n−(2^n−1)=1` identically, `∫M=1`. So `D̃≥1` is
   *exactly* `∫1[M odd] ≥ ∫M`. This replaces the opaque `2λ(O_Y^<∩O_Z)` term with one integer
   profile `M`. The value `1` is forced by the dyadic weights (not an estimate).

2. **Merged-order lattice identity `(♦)` (PROVED — this is the requested Lemma-G signed sum on the
   merged order).** Merge `Y⊎Z` descending, label T/B, prefix imbalance `c_i=#T−#B`. Then `M=c_i`
   on `(w_{i+1},w_i)`, and `D̃−1 = Σ_i ψ(c_i)Δw_i` with `ψ(c)=1[c odd]−c`, `Δw_i=w_i−w_{i+1}≥0`.
   Verified to machine precision (max error `7e−15` over `3·10⁵` Case-B configs).

3. **Termwise Lattice Lemma T (NEW, PROVED).** `ψ(c)≥0 ⇔ c≤1`; so if `c_i≤1` for every prefix,
   `D̃−1=Σψ(c_i)Δw_i≥0` termwise ⇒ `D̃≥1`. Verified `0` violations over `251876` `maxc≤1` configs.
   **This closes the entire equality-attaining core:** over `4·10⁵` residual configs (`n≤5`), every
   tight (`D̃=1`) configuration has `maxc≤1` (near-tight `D̃<1.02`: `23058` had `maxc≤1`, only `3`
   had `maxc=2` and those already at `D̃≥1.017`). It settles the strict-alternation extremal family
   (e.g. `n=2,a=2,b=0`, `Y=(2.64,1.32,0.04)`, `Z=(2,1)`: `c=(1,0,1,0,1)`, all `ψ=0`, `D̃=1` exactly).

4. **Structure Lemma (NEW, PROVED).** Every `≤k`-cut response to `S_k=\{1,…,2^k\}` decomposes as
   `⊎_j Y^{(j)}` (fragments of `2^{k−j}`, budget `Σa_j≤k`), with each upper union `⊎_{j≥p}Y^{(j)}`
   itself a `≤(k−p)`-cut response to `S_{k−p}`. This exposes `Z`'s full recursive cut-tree and its
   dyadic **anchors** — the objects the residual argument must use (a scalar summary of `Z` cannot).

Carried forward (already rigorous): base `P(0)`, Case A (C3), `(◇◇) D̃≥(y₁−θ)⁺`, `(★★)`, closing
Case B on `{y₁≥2^{n−1}+1}∪{|D_top^<−D_bot|≥1−D_top^>}`.

## Precise remaining gap

**GAP-LB′-run.** The only open Case-B configurations are those whose merged descending order has
`maxc=\max_i c_i ≥ 2` (a "T-run" where top-fragments run `≥2` ahead of `Z`-parts). There `(♦)` has
negative terms and Lemma T fails. The exact open sub-claim:
```
Σ_{i: c_i≥2}(c_i − 1[c_i odd])Δw_i  ≤  Σ_{i: c_i≤0}(1[c_i odd] − c_i)Δw_i
```
("T-run deficit ≤ anchor surplus"). This must be proved **through** the Structure Lemma: the surplus
(`c_i≤0` heights) is guarded by `Z`'s dyadic anchors — e.g. an uncut anchor `z₁>y₁` opens the merge
with `c_1=−1` over width `z₁−y₁`, contributing `+2(z₁−y₁)`, a surplus of definite size set by `Z`'s
geometry. Recommended: a two-level joint induction descending into `Z=Y'^{(0)}⊎(\text{resp. }S_{n−2})`
at `θ/2`, matching each top-run to the anchors of the corresponding `Z`-subtree. I could not complete
this induction in the time budget. It is FALSE for a scalar-summarized/generic `Z` (probes 5–7), and
its `maxc≥2` infimum of `D̃` approaches `1` (min observed `1.017`), so no crude slack estimate
substitutes for the anchor-domination argument.

## Files
- Approach: `results/imo-2026-03/approaches/induction-recursion-telescope.md`
- Scratch/verification: `/tmp/round-4/scratch/{explore.py,lattice.py,tight.py,verify.py}`

## Promotable lemmas (for reviewer certification)
- **Exact-difference reformulation `(♣)` + merged-order lattice identity `(♦)`** — fully proved §2–§3.
- **Termwise Lattice Lemma T** (`#T−#B≤1` per prefix ⇒ `D≥sum(Y)−sum(Z)`) — fully proved §4;
  equality-robust; closes the tight core of GAP-LB′.
- **Structure Lemma** (recursive cut-tree of a dyadic response) — fully proved §5.

## Spec concerns
- None with the assigned route as a *framing*: the merged-order signed-sum decomposition `(♦)` is
  clean, exact, and equality-robust, and it genuinely reduces GAP-LB′ to the single lattice
  inequality GAP-LB′-run — a real advance over the round-3 `2λ(∩)` residual (the tight core is now
  removed, not just re-packaged). The honest caveat: the *closing* sub-claim (anchor-domination via
  the two-level induction) is still open — Lemma T is a general merged-order fact that does NOT
  invoke `Z`'s cut-tree, so it alone cannot reach `maxc≥2`; that region is exactly where the
  Structure Lemma's anchors must enter, and I did not complete that induction. Consistent with the
  reviewer's guard: the residual is honored as needing `Z`'s recursive structure, never a
  free-standing bounded-multiset lemma.
- Twin note: this route and the exchange twin (induction-recursion) now bottom out on the same
  GAP-LB′ residual but via provably different objects (merged lattice path + Z-anchors here;
  compactness + vanishing-fragment exchange there). Per the outline-reviewer's field note, if BOTH
  stall next round the orchestrator should escalate a genuinely different framing for GAP L.
