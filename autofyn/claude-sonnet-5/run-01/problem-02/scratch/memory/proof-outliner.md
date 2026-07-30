ALWAYS: for geometry problems with a metric target (OM=ON style), check first whether the explorer
found an algebraic/coordinate reformulation that eliminates the need for an auxiliary point (e.g.
the coordinate-native "myexpr=0" identity here) — it often sidesteps a degenerate/special case
(isosceles AB=AC) that a synthetic auxiliary-point route (A*-concyclicity) must handle separately.
Give the outliner-selected build set at least one approach of each flavor: pure synthetic chase,
inversion/transformation, and coordinate bash — since for hard geometry (IMO P2/P3/P6 level) no
single flavor is guaranteed to close and they genuinely differ in mechanism even when sharing an
intermediate reformulation, so they are NOT single-gap-trap violations (per CLAUDE.md, sharing a
reformulation is fine if the closing mechanism differs). (round 2)
ALWAYS: when explorers report a killed hypothesis (e.g. "K/L is not a spiral similarity center",
"AK,AL not isogonal") explicitly carry that into every new approach file's "Approaches tried"
dead-ends list so builders don't waste a cycle rediscovering it. (round 2)
ALWAYS: when a shared-gap plateau (e.g. an algebraic quantity Z whose sign is needed) gets closed by
explorers via a geometric positivity argument (interior-point-of-triangle convex-combination sign,
or a triangle-angle trig identity), write the closing argument directly INTO each affected approach
file as an "Outline update" section (not just the round report) — builders read the approach file,
not the outliner's own report file, so the fix must land there to actually get used. (round 4)
NEVER: assume a shared gap closing for two sibling approaches means they should be merged — if both
are genuinely different top-level framings (e.g. rotation-operator coordinates vs raw ca/sa
coordinates), keep them as independent rival slugs even after they converge on the same gap-closing
lemma; independent survival is insurance against a subtle review-time error in one. (round 4)
ALWAYS: when an approach file's Status header disagrees with current.md's reviewer verdict (e.g. a
builder self-reported "solved" but current.md records a reviewer override to "partial"), explicitly
call out the stale header in the revision instructions so the next builder fixes it — otherwise the
overclaim silently persists in the file even though current.md is correct (round 5, imo-2026-02:
coordinate-groebner-elimination.md still said "solved" at its own header despite current.md's
documented downgrade).
ALWAYS: when two sibling coordinate approaches share a gap and one has fully closed a sub-lemma
(e.g. rotation-sign convention) rigorously while the other only checked it numerically, tell the
lagging sibling to CITE the certified lemma from lemmas/ rather than re-deriving its own weaker numeric
version — keeps both files internally consistent without merging them into one slug (round 5).
