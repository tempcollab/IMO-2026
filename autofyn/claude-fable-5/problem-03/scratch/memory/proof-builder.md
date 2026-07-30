# proof-builder — per-role rules

ALWAYS: check `results/<id>/lemmas/` immediately before writing a shared lemma file (parallel sibling builders can race you; first-to-write claims it, others import) (round 1)
ALWAYS: prefer a static LP/vertex ("minimizer at a vertex of the piecewise-linearity arrangement") argument over iterative slide-with-monovariant arguments for piecewise-linear minimax structure — it sidesteps re-sorting/cycling objections entirely (worked for imo-2026-03 GAP T, round 1)
NEVER: use integrality/parity-in-units shortcuts for stick-cutting replies — cut positions are real-valued; pinned tie systems can force non-integral sub-pieces (e.g. a 4-unit rung cut into three 4/3 pieces is a legal vertex reply) (round 1)
ALWAYS: when a gap overlaps a sibling approach's casework, stop and record the overlap honestly instead of duplicating (kill-criterion instruction from outline-reviewer; imo-2026-03 round 1)
ALWAYS: before grinding regional casework on a budget claim like U(m), try a global pigeonhole obstruction first (all 2^m subset sums pairwise > β apart would exceed the total range T = (2^m−1)β) — it closed imo-2026-03's entire middle case in one paragraph after two rounds of case analysis (round 3)
ALWAYS: for realizing signed-sum targets by Match/FreeRetire chains, use an adaptive two-pile walk with stuck-state mass accounting (the only reachable stuck state has residual < target) rather than fixing an ordering or a sign vector a priori — sidesteps the "not all signed sums reachable" trap entirely (round 3)
