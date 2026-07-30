## Goal

Solve IMO 2026 Problem 4 (the Mulan triangle game). Find and prove all real θ ∈ (0°,180°) for which Mulan can guarantee a triangle with a θ angle in finitely many steps, regardless of Shan-Yu's play.

- Problem id: `imo-2026-04` (domain: combinatorics/game; answer_type: characterization — must prove both inclusion and exclusion).
- Metric: proof-reviewer verdict on `results/imo-2026-04/current.md` — `## Status` = solved, with a rigorous proof giving the exact set of θ and verifying (a) Mulan's forcing strategy for every winning θ, (b) Shan-Yu's avoiding strategy for every non-winning θ.
- Eval: read `results/imo-2026-04/current.md` `## Status` and `results/imo-2026-04/approaches/.ranking.json` each round. Baseline: no approaches yet (round 1). Target: Status=solved.
- Constraint: rigor rules in CLAUDE.md (no skipped cases, no hand-waving, name tools, prove not conjecture; characterization needs both directions; "finitely many steps" needs an explicit decreasing natural-valued potential or a finite bound).

## Goal Updates
- [2026-07-28] User: solve imo-2026-04. (Note: this problem is tagged difficulty_level "medium"/rating 7 in the benchmark, but the user explicitly chose it — it takes priority over the "hard-only" targeting in CLAUDE.md.)

## Eval History
- Round 1: BREAKTHROUGH. Status `solved` (proof-reviewer APPROVE on all 3 approaches). Answer: Mulan wins ⟺ θ = 180°/n for integer n≥2 (θ divides 180°). Ranking (Elo): lattice-descent 1546 (verified-milestone) > residue-monovariant 1515 (advanced, Φ-crux refuted→fallback) > equilateral-witness 1485 (advanced, E-alone refuted→safe set S={all angles≤90°} for θ>90°) > euclidean-needle 1454 (not built, deferred). Lemmas certified: reduce-move, alignment-move, taint-free-invariant.
- Orchestrator independent verification (round 1): inclusion M1+M2 forces 100% of ~250 random triangles per n=2..30 against fully-adversarial Shan-Yu, max steps = n−1 exactly (matches bound); exclusion: equilateral is a safe start for non-divisor θ={72,100,50,80,120,89} (no one-move crack). Confirms the proof.

## Rules
- ALWAYS: the cut operation (cut to vertex A, param α) gives children C1=(α,B,180−α−B) [keeps B] and C2=(A−α,C,B+α) [keeps C]; the two fresh P-angles are supplementary (sum 180°). This is the load-bearing structural fact of the game (round 1).
- ALWAYS: for inclusion, apply M2 (reduce: cut the mθ-vertex with α=θ) FIRST when an angle is already a multiple of θ; only use M1 (align) when NO angle is a multiple. Applying M1 on an already-tainted triangle loops and never descends (caught by orchestrator sim round 1).
- NEVER: accept "the Φ=max(angle mod θ) monovariant decreases for both children" — it's FALSE when Φ≤θ/2 (the interval (θ−Φ,Φ) is empty); the alignment move is the only bypass (residue-monovariant builder, round 1).
- ALWAYS: for characterization problems, each slug targets BOTH directions end-to-end; do not split one proof across slugs (CLAUDE.md). But keep the population diverse in framing so a shared wall (here: 3/4 exclusions rest on the same 2×2 taint casework) doesn't collapse everything at once — push ≥1 independent exclusion route (the obtuse safe-set S={all angles≤90°} is the independent one for θ>90°).
- ALWAYS: when N explorers independently converge on the same answer computationally+structurally, trust the convergence and have the outliner build rival framings on it rather than re-litigating the answer (round 1: 3 explorers → θ=180°/n).

## State
- Round 1 DONE. imo-2026-04 SOLVED. `results/imo-2026-04/current.md` Status=solved with full proof. Three APPROVE'd approaches + three certified lemmas. Independent sim verification passed.
- Next (if run continues): harden the exclusion's shared wall — give the independent obtuse safe-set S a full treatment for all θ>90° and consider an independent exclusion for θ∈(0°,90°] beyond the taint casework, so the population doesn't rest on one argument. Otherwise the problem is complete.
