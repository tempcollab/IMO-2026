# proof-reviewer rules

ALWAYS: verify the cut-operation angle formula and the supplementary P-pair (180-α-B)+(B+α)=180 by independent angle chase before trusting any Mulan-game proof — it is the single load-bearing identity (round 1, imo-2026-04).

ALWAYS: for "tainted angle mθ ⇒ Mulan wins" descent lemmas, check the tracked vertex is a GEOMETRIC vertex of the kept child — the cut goes to V, so V survives in both children; this makes the "same-vertex invariant" a one-liner, not a gap. Don't accept a builder over-formalizing it, but don't flag it as a gap either (round 1, imo-2026-04).

NEVER: accept a "max-residue strictly decreases for BOTH children" claim without checking the empty-interval obstruction: the two fresh P-residues r(β), θ−r(β) can't both be < Φ when Φ≤θ/2 unless r(β)=0 (which IS the alignment move). It was refuted computationally in imo-2026-04 round 1.

ALWAYS: for exclusion "taint-free invariant" proofs, run a numerical sweep over non-divisor θ (rational p/q with p>1, irrational like √5000, and θ>90°) testing that no α makes BOTH children tainted — the 2×2 casework is the shared wall and a single flaw sinks all approaches resting on it (round 1, imo-2026-04).
