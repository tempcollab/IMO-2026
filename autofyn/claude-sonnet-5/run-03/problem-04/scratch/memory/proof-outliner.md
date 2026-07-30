ALWAYS: when three math-explorers disagree, treat the one that ran an exhaustive/exact minimax
(not just a greedy simulation or a single-chain conjecture) as authoritative for the ANSWER, but
still re-derive its key lemmas by hand/numerically before building an outline on top of them
(round 2, imo-2026-04: explorer-verify's minimax refuted two plausible-looking but wrong
conjectures from greedy/chain-restricted explorers).
ALWAYS: for game-theoretic "for which θ can player X force a win" problems, look for a clean
"supplementary P-angle" or similar identity that turns a single move into a forced dichotomy
(both children constrained), then induct on a natural integer parameter (here n=180/θ) via two
lemmas: one that forces progress when a case condition holds (some angle small) and one
deterministic chip/transfer move that creates that condition when it doesn't hold (round 2,
imo-2026-04).
NEVER: assume the "only if"/converse direction of a forcing-game characterization is symmetric
in difficulty to the forward direction — in continuous/geometric forcing games the forward
(constructive) direction is often fully tractable by explicit induction, while the converse
(adversary survives forever) typically needs a genericity/linear-independence or dimension-
counting argument that is much harder to nail down in one pass; budget outliner/builder time
asymmetrically toward the converse gap once the forward direction looks solid (round 2,
imo-2026-04).
NEVER: spend outline time re-deriving a forward-direction construction independently in more
than one approach when time is short — import it explicitly from the approach that has it, and
spend the other approaches' distinct effort entirely on the harder open direction (round 2,
imo-2026-04: budget-partition-dimension and three-distance-avoidance both explicitly import the
forward direction from chip-double-force.md rather than re-deriving it).
