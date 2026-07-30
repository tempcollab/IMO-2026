# Scouting report: the residual cross-tie gap (b) — minority-part, deep-bracket sub-case

Lens: the ONE remaining lower-bound gap for `imo-2026-03` (IMO 2026 P3), after
gap (a) was fully closed (Lemma TREE-BOUND, round 8). Scouting only — no
proof attempted.

## 1. Precise statement of what's unresolved

Setup (integer normalization, from `alternating-sum-toolkit.md` /
`cross-tie-affine.md`): fix `n`, anchors `t_i = 2^{n-i}` (`i=1..n`,
`t_i = 2 t_{i+1}`), top piece `= 2t_1`. Xiang Yu splits some of Liu Bang's
`n+1` original pieces with his `≤n` marks. The target is `D(B) ≥ t_n = 1`
for every reachable `B` (equivalent to `oddsum(B) ≥ c(n)`, Lemma D-REFORM).

By Lemma V'-GEN's vertex reduction (well-separated case closed by
`recursive-embedding-induction`; single-free-coordinate case closed by Lemma
FC; anchor-only case closed by Lemma TREE-BOUND), the *only* case not yet
covered is: two or more split pieces `π_1,...,π_k` (`k≥2`, distinct pieces)
each contribute one free coordinate, and these free coordinates are
currently **tied at a common value `v`**, adjacent in sorted order with no
anchor between them (a genuine cross-piece tie, not resolvable by treating
each piece's free coordinate independently).

Lemma CROSS-TIE-AFFINE (`geometric-dominance-construction`, certified in
`lemmas/cross-tie-affine.md`) shows `D(v)` is affine on the cell containing
the tie, so the minimum over the cell sits at an endpoint (an anchor `t_j`),
not the interior tie — this closes two of three sub-cases with **zero
residue**:
- `π_l` has `≥3` parts (companions already pinned at anchors) — reduces
  directly to the already-closed well-separated case.
- the tied coordinate is the **majority** (larger) part of a 2-part-split
  piece — the "self-meeting-point-is-an-anchor" fact (`top_π/2` is always
  itself an anchor, from `t_i=2t_{i+1}`) means snapping to the self-meeting
  boundary lands on an anchor too, giving a zero-residue even-multiplicity
  block.

**What's NOT closed**: when the tied coordinate is the **minority**
(strictly smaller) part of a 2-part-split piece `π` (total `top_π = t_i` or
`2t_1`), in a bracket `(t_{j+1}, t_j)` with `t_j < top_π/2` (i.e. `v` must
cross an *external* anchor before ever reaching `π`'s own self-meeting
point `top_π/2`). Here the D-minimizing endpoint is the external anchor
`t_j`, but the companion `c = top_π − t_j` is then a **fixed, generically
non-power-of-2** number (e.g. `top_π=t_i`, winning endpoint `t_j` with
`j>i+1`: `c = t_i − t_j = 2^{n-j}(2^{j-i}-1)`, a power of 2 only when
`j−i=1`, the already-closed "aligned" case). So the resulting vertex
configuration has one genuinely non-anchor residue value floating in the
merge, and neither Lemma TREE-BOUND (anchor-only) nor Lemma FC
(single-free-coordinate) covers it directly. The exact open claim: **for
every such minority/deep-bracket residue configuration, is `D ≥ t_n` still
true?** (Believed true, numerically supported, not proved.)

## 2. Numerical experiments — why this case is structurally different

I reproduced and extended the file's own probes with exact `Fraction`
arithmetic (`/tmp/residue_explore.py`, `/tmp/residue2.py`,
`/tmp/global_search.py`).

- **Symmetric two-minority tie** (`n=4`, both `t_2=4` and `t_3=2` split with
  their minority parts tied at `v`, everything else untouched): `D` is
  **exactly flat at 11** for every `v∈(0,1)` tested (well above `t_4=1`).
  This confirms the file's reported slope `M=0` finding and shows the flat
  behavior is not a coincidence of one instance.
- **Genuine external-anchor-snap residue** (`n=6`, `π` = `t_2=16` split with
  minority `v` snapping to external anchor `t_5=2`, companion `c=14`
  — confirmed non-power-of-2 — cross-tied with a second split piece `t_k`
  also hitting `v=2`): `D` computed at `43` for every tested `k∈{1,3,4}`,
  vastly above `t_6=1`.
- **Unrestricted global search** (`scipy.differential_evolution`, many
  restarts, all mark-allocations up to 4 touched pieces, `n=3,4,5`): the
  true global minimum of `oddsum(B)` was found to match the conjectured
  bound `c(n)` **exactly** in every case, always achieved by the
  already-closed "all marks on `P_1`" (Proposition K / doubling-family)
  configuration — never by a residue configuration. No violation found
  anywhere.

**Why the residue case looks harder but is numerically harmless.** The
common thread: whenever Xiang Yu is forced into a "minority part tied deep
below its own halving level," he has necessarily spent a mark creating a
*small* minority piece `v` while leaving a *large* leftover residue `c`
un-anchored — this is mark-inefficient. The affine slope is small/zero
in these regimes precisely because the tied coordinate's rank in the
overall sort is "buried" (many larger anchors sit above it), so moving it
barely changes `D`, and the configuration's `D`-value is dominated by the
untouched large anchors, which are already `≥ t_n` on their own. In every
tested instance the residue configuration is *far* from the true minimum,
not merely weakly satisfying the bound — this is the same qualitative
signature the two approaches independently reported (flat slope,
non-competitive `D`).

## 3. Candidate techniques

- **PAIR-CANCEL + domination, not a from-scratch bound (most promising).**
  `recursive-embedding-induction`'s certified PAIR-CANCEL identity says a
  genuine tied pair `{y,y'}` (both `=v`, adjacent ranks) contributes exactly
  `0` net to `D`, so `D(\text{full}) = D(B'')` where `B''` deletes the tied
  pair. Instead of trying to bound `D(B'')` directly by re-running the whole
  induction on a "short by one leaf per piece" object (flagged in
  `recursive-embedding-induction` round 8 as unfinished, option (ii)), the
  numerics above suggest a **comparison/domination** argument may be easier:
  show the residue configuration's `D` is always `≥ D` of some *already-
  covered* configuration reachable with the same or fewer marks (e.g. the
  anchor-only config obtained by NOT creating the minority split at all, or
  by snapping to the piece's *own* self-meeting point instead of the
  external anchor). This would let gap (b)'s last case piggyback on Lemma
  TREE-BOUND / Lemma FC without a new base-level induction — closer in
  spirit to a "wasted move" argument (cf. `universal-adversary-strategy`'s
  DOM/HALVE lemmas and the `dual-objective-shift` lemma, all "spending a
  mark this way cannot help the adversary" style facts already in the
  knowledge base / lemma folder).
- **Extend the TREE-BOUND forest formalism to admit one "impure" leaf.**
  Lemma TREE-BOUND's induction crucially uses that all leaves are exact
  powers of 2 (forced halving, since no two distinct powers of 2 sum to a
  power of 2). The residue value `c = t_i − t_j = 2^{n-j}(2^{j-i}-1)` is
  *not* a power of 2, but `2^{j-i}-1` is a run of 1-bits — i.e. `c` is a sum
  of `j-i-1` *distinct* powers of 2 (specifically `2^{n-j}+2^{n-j+1}+\cdots
  +2^{n-i-1}`, all present as anchors `t_{i+1},...,t_j` after `j-i-1`
  hypothetical further binary splits). This hints that the residue could be
  handled by extending the forest-reachability induction to trees with
  exactly one "stunted" branch of controlled shape, rather than needing an
  entirely separate mechanism — but this was not attempted and is only a
  structural observation, not a worked argument.
- **Bounded-width exchange move — already ruled out, don't re-attempt.**
  `recursive-embedding-induction`'s round-5 negative result (Lemma X,
  move-traps, composition width growing with `n`) is a certified dead end
  for Lemma L's combinatorial core; the residue case looks structurally
  similar (a "local perturbation" argument fails for the same reason — the
  free coordinate is rigid once its piece has no slack) so a bounded-width
  local-move fix for gap (b) should be expected to hit the same wall.
  Flagging this explicitly so the next round doesn't re-spend effort here.
- **Crux corpus.** Searched `games-and-strategy` /
  `invariants-and-monovariants` subtopics (220 combinatorics cruxes). The
  most relevant transferable idea is "reduce an ordering-invariance claim to
  invariance under a single adjacent transposition" (`aimo-0003`) — this is
  essentially the exchange-move idea already tried and found insufficient in
  bounded width; no crux found that gives a genuinely new mechanism for
  "residual non-anchor value after a forced discrete snap." The corpus
  didn't surface a ready-made technique closer to this problem's specific
  structure (self-similar binary/geometric configuration) than what's
  already in the population's own certified lemmas.

## 4. Assessment: promising vs. dead end

- **Promising**: the domination/comparison route (piggyback residue
  configs onto already-closed anchor-only cases via an inequality
  `D(\text{residue config}) ≥ D(\text{some TREE-BOUND-covered config})`,
  rather than a fresh induction) — numerics strongly support that residue
  configurations are never close to minimal, which is exactly the kind of
  evidence a domination argument would need and predicts.
- **Dead end (confirmed, don't re-attempt)**: bounded-width single/multi-
  exchange perturbation directly on the residue value — same rigidity
  obstruction as Lemma L's already-documented negative result.
- **Open, unexplored**: extending the TREE-BOUND forest induction to
  "impure"/residue leaves via the binary-decomposition observation on
  `2^{j-i}-1`. Structurally suggestive but not attempted; would need someone
  to actually carry out an induction, not just numerics.
- All numerical evidence (three independent hand-built residue instances
  plus an unrestricted global search over small `n`) is consistent with the
  gap being a **true but currently unproved statement**, not a hidden
  counterexample — no evidence found that Liu Bang's bound actually fails
  in this sub-case.

## Files/scripts produced (scouting only, not part of the proof record)
- `/tmp/residue_explore.py`, `/tmp/residue2.py`, `/tmp/global_search.py` —
  exact-`Fraction` and `scipy.differential_evolution` probes described
  above.
