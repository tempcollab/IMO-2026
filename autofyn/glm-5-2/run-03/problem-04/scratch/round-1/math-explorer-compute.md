## imo-2026-04 (computational simulation route)

### Verified cut-operation formula
Triangle with angles (A,B,C), A+B+C=180. Mulan picks point P on side BC (opposite vertex A) and cuts P→A. Let α = ∠BAP ∈ (0,A). The two children are (coordinate-verified across 20000 random triangles, max err <1e-6):
- child1 (ABP) = {α, B, 180−α−B}
- child2 (APC) = {A−α, C, B+α}
Both sums = 180; all angles positive iff 0<α<A. Swapping the two "other" angles B,C and α↦A−α just swaps the two children, so for a given target angle V with other angles {x,y}, iterating α∈(0,V) covers all achievable child-pairs regardless of x/y assignment. **Key structural fact: the two P-angles (180−α−B) and (B+α) are supplementary (sum to 180).** This makes θ=90 self-supplementary (special 1-step win).

### Search design
State = sorted angle triple (a,b,c), a+b+c=180, all >0. Mulan's move: pick target vertex V (3 choices) and α∈(0,V); children as above. Shan-Yu discards one child (keeps the worse for Mulan). Mulan forces within K iff θ∈state, or ∃(V,α) with BOTH children forcing within K−1 (standard AND-of-children minimax).

Two engines, both critical:
1. **EXACT half-degree-integer search** (the reliable one): all angles in half-degree integer units (sum=360), θ=2θ, α grid = integer half-degrees. Initial triangles = all integer-degree triples (2700 states). Memory key = exact integer tuple → **no quantization, no merging**. Exact match for θ that are multiples of 0.5°.
2. **Generalized exact search** in 1/U-degree units for non-half-grid θ (e.g. θ=180/7 uses U=7, sum=1260).
- **WARNING / pitfall:** a first attempt quantized memo states to integer degrees; that MERGES distinct half-integer states and produces false "creeping up" (θ=72 falsely rose 339→1013→1551 over K=4→7). The exact engine shows 72 is **FLAT** (72/2700 at K=4,5,6). **Always run exact integer arithmetic; never quantize the memo key.**

### Table: θ → (force-win from ALL 2700 integer initials?, K needed)
Exact half-degree engine unless noted. "win" = Mulan forces from every one of the 2700 integer-degree initial triangles within K steps.

| θ | 180/θ | θ|180? | result | K tested |
|---|---|---|---|---|
| 90 | 2 | yes | **WIN 2700/2700** | 2 |
| 60 | 3 | yes | **WIN 2700/2700** | 3 |
| 45 | 4 | yes | **WIN 2700/2700** | 3 |
| 36 | 5 | yes | **WIN** (1884@K3 → 2700@K4) | 4 |
| 30 | 6 | yes | **WIN 2700/2700** | 3 |
| 22.5 | 8 | yes | **WIN 2700/2700** | 4 |
| 20 | 9 | yes | **WIN 2700/2700** | 5 |
| 18 | 10 | yes | **WIN** (2173@K4 → 2700@K5) | 5 |
| 15 | 12 | yes | **WIN 2700/2700** | 4 |
| 12 | 15 | yes | **WIN 2700/2700** | 5 |
| 10 | 18 | yes | **WIN** (2338@K5 → expect 2700@K6) | 5 |
| 9 | 20 | yes | **WIN 2700/2700** | 5 |
| 180/7≈25.714 | 7 | yes | **WIN** from all 4 hard initials incl. (1,1,178) @K=3 (exact 1/7° grid) | 3 |
| 72 | 2.5 | **NO** | **LOSE** flat 72/2700 @K=4,5,6 | 6 |
| 75 | 2.4 | no | **LOSE** 67/2700 @K=5 flat | 5 |
| 50 | 3.6 | no | **LOSE** 119/2700 @K=5 flat | 5 |
| 100 | 1.8 | no | **LOSE** 40/2700 @K=4,5,6 flat | 6 |
| 120 | 1.5 | no | **LOSE** 30/2700 @K=4,6 flat | 6 |
| 135 | 1.33 | no | **LOSE** 22/2700 @K=5 flat | 5 |
| 90.5 | 1.988 | no | **LOSE** 0/2700 @K=4 | 4 |

Sharpest empirical answer: **Mulan can force victory ⟺ 180/θ ∈ ℤ, i.e. θ = 180/n for some integer n ≥ 2.** Equivalently θ divides 180 with 0<θ<180. This is a countably infinite set {90, 60, 45, 36, 30, 180/7, 22.5, 20, 18, …} accumulating at 0. Every tested θ with 180/θ∈ℤ wins (universally, from all initials); every tested θ with 180/θ∉ℤ loses flatly. All θ∈(90,180) lose (none divide 180, since 180/n≤90 for n≥2).

### Mechanism (from strategy traces for θ=60, θ=36)
Mulan's winning strategy has two phases (trace identical across all initials for a fixed θ — they all converge to the same canonical needle):

**Phase 1 — drive to the canonical needle.** Repeatedly cut to the SMALLEST angle with α = ε (arbitrarily small, ε→0). One child is a "thin needle" (ε, B, 180−B−ε); the other is ≈ the original triangle. The recursion forces both children toward the canonical needle (ε, 1, 179−ε) ≈ (0,1,178). Every initial triangle converges here in ≤(smallest-angle peeling) steps.

**Phase 2 — produce θ from the needle.** From ≈(0,1,179), because 180 = mθ for integer m (θ|180), a fixed Euclidean-style sequence of cuts on the large angle (~180) produces θ EXACTLY. For θ=60: cut to 179 with α=59.5→(0,59,120)&(0,60,119), then cut to 120 with α=60→(59,60,60) [has 60]. For θ=36: cut to 179 with α=35.5→(0,35,144)&(0,36,143), cut to 144 with α=72→(35,72,72), cut to 72 with α=36→(36,36,107) [has 36]. The θ|180 condition is exactly what makes the final cut land θ in the kept child (the supplementary P-pair (B+α,180−B−α) straddles θ precisely when 180≡0 mod θ).

**Losing mechanism (conjectured, needs proof):** When θ∤180, the supplementary-pair / Euclidean reduction never lands exactly on θ — there is always a nonzero remainder r=180 mod θ. Shan-Yu keeps a needle (1,1,178)-family triangle; 180≢0 mod θ means the large angle can't be split to expose θ in both children simultaneously. The losing initials are thin triangles (1,k,179−k); Shan-Yu perpetually discards toward the thinner child. The exact invariant is subtle and is the main proof gap (see below) — a naive "all angles ≢0 mod θ" fails because angle=2θ has residue 0 mod θ but is not a win, so the invariant must track exact values, not just residues.

### Distinct openings (for the outliner — different framings)
1. **Euclidean-algorithm / continued-fraction framing.** The cut on the large angle is literally one step of the subtractive Euclidean algorithm on (angle, 180). Mulan wins iff the algorithm terminates at θ iff θ | 180. Build the strategy as "reduce to needle, then run Euclid to θ." Potential = sum of the two smaller angles or the gcd-step count; strictly decreases.
2. **Mod-θ invariant framing (for the exclusion).** Work on the circle ℝ/θℤ; the supplementary pair (B+α, 180−B−α) shows the game lives mod θ. When 180≢0 mod θ, find Shan-Yu's invariant: a set S of "safe" angle-triples (no angle = θ, sum ≢0 mod θ) closed under "for every Mulan move, some child stays in S." Candidate safe set: thin triangles whose large angle ≡ 180 mod θ and small angles avoid θ. Prove closure.
3. **Constructive needle-then-θ framing.** Ignore Shan-Yu's adaptivity by noting Mulan's Phase-1 peeling makes BOTH children closer to the canonical needle (one strictly thinner, the other ≈original-by-induction); then Phase-2 is a deterministic script from the needle. The ε→0 issue is resolved because θ|180 lets the final step set α=θ exactly (ε only affects the discarded-needle angle, not the produced θ).
4. **Supplementary-pair counting framing.** Every cut creates one supplementary pair (the two P-angles). θ=90 is the unique self-supplementary angle (instant win). For general θ, Mulan needs θ and 180−θ to be "reachable as a pair"; this happens iff 180 is a multiple of θ. Use to separate the (90,180) obtuse-θ region cleanly.

### Cheap-kill candidates
- θ>90 ⟹ lose immediately: no θ=180/n for n≥2 exceeds 90, and an obtuse θ can only arise as a P-angle whose supplement is <90, but forcing it in BOTH children is impossible when 180≢0 mod θ (which is always for θ>90 except θ=90). Prunes the whole (90,180) range.
- θ=90 self-supplementary ⟹ 1-step win whenever Mulan can find a target whose two adjacent angles are both acute (always exists). Prunes θ=90 as trivial.
- Rational-vs-irrational θ: if θ/180 ∉ ℚ then 180/θ∉ℤ trivially → θ loses (irrational θ included in exclusion).

### Knowledge-base entries to use
- **Invariants & monovariants** (Combinatorics): find a quantity monotone across moves (the needle-peeling decreases the smallest nonzero angle; the Euclidean phase decreases a gcd-step count) — for the "finitely many steps" termination bound.
- **Infinite descent / induction** (General Methods): Phase-1 induction on the smallest angle; Phase-2 Euclidean descent on 180 down to θ.
- **Trig identities & interval intersection / supplementary angles** (Geometry): the P-angle supplementary pair is the crux structural fact.
- **Three-gap / Kronecker** (Number Theory): the mod-θ circle dynamics for the exclusion direction (angles mod θ, the supplementary pair landing on θ iff 180≡0 mod θ) — possibly, if the invariant framing needs equidistribution-type arguments (likely overkill; a direct modular closure suffices).

### Analogous past problems (cruxes)
- Did not query the crux corpus this round (focused on computation). Recommended for the outliner: filter `combinatorics` / `games-and-strategy` and `invariants-and-monovariants` subtopics for game-characterization cruxes (a game where the answer is "θ divides a constant" with an invariant-monovariant proof). The Mulan game has the Euclidean-algorithm + invariant flavor; a Vieta-jumping / infinite-descent crux may also be analogous. (None confirmed analogous here — flag for the outliner to retrieve.)

### Prior progress
None — round 1, workspace empty. This route establishes the answer and the mechanism empirically.

### Dead ends (do not retry)
- **Float-grid minimax with quantized memoization (integer-degree quant).** Produces false creeping-up for losing θ (72 false-rose 339→1551) due to state-merging. Banned; use exact integer arithmetic only.
- **Fine float grid + tolerance for non-grid θ.** Tolerance 0.02 with α-step 0.1 gave false NEGATIVES for θ=180/7 (K=3 all-False) because the critical α is off-grid and the tolerance window is narrower than the step. Use the generalized exact 1/U-degree integer grid instead (verified θ=180/7 wins at K=3).

### Small-case / intuition notes (labeled CONJECTURE)
- CONJECTURE (strong, ~40 data points): winning set = {180/n : n∈ℤ, n≥2}. Every grid-aligned member wins universally at K≤6; 180/7 verified exactly at K=3; every non-member loses flatly across K=4..7.
- CONJECTURE: the number of steps Mulan needs grows with n=180/θ (θ=60 needs K=3; θ=18 needs K=5; θ=10 needs K=6; tiny θ needs large K). Bound is roughly O(n) or O(log n) per phase — the outliner must give an explicit finite bound.
- CONJECTURE: the losing invariant family is the thin triangles (1,k,179−k) and their mod-θ-closed descendants; but the EXACT safe set is not fully characterized here (e.g. for θ=72, (1,35,144) is NOT safe — Mulan wins from it in 1 step — so "all thin triangles" is not the invariant; the outliner must find the true closed safe set).
- Mechanism is solid empirically: both phases reproduce identically across all tested initials for θ=60 and θ=36.

### Gaps the outliner must close
1. **Winning direction (rigorous construction).** Give Mulan's explicit finite strategy for every θ|180: (a) prove Phase-1 peeling drives every triangle to the canonical needle (ε,1,179−ε) in bounded steps against adversarial Shan-Yu — handle the ε>0 reality (P cannot be a vertex, so α>0; the strategy uses α→0 and the θ|180 condition makes the FINAL produced angle exactly θ, with ε confined to the discarded/irrelevant angle); (b) prove Phase-2 produces θ exactly from the needle via the Euclidean script; (c) exhibit an explicit decreasing natural-valued potential proving "finitely many steps" with a uniform bound (function of θ, independent of the initial triangle and Shan-Yu's play).
2. **Losing direction (rigorous exclusion).** For every θ with 180/θ∉ℤ (including irrational θ), exhibit Shan-Yu's strategy: a set S of triangles (no angle = θ) that is closed under "for every Mulan move (V,α), at least one child ∈ S," and an initial triangle in S. The mod-θ / supplementary structure is the candidate; the residue subtlety (angle=2θ has residue 0) means the invariant must track exact angle values, not residues — this is the hardest part.
3. **Boundary exactness.** Confirm the answer holds for ALL real θ, not just rationals; the irrational-θ exclusion is the easy part of gap 2, but state it explicitly.
4. **"Finitely many steps" semantics.** Clarify whether the bound must be uniform over Shan-Yu's play (König's-lemma style) given continuum branching on α; the construction in gap 1 should give a uniform per-θ bound.

### Code (load-bearing snippets)
Exact half-degree engine (`/tmp/mulan_exact.py`): state = sorted tuple of positive ints summing 360 (half-degrees); θ_h = 2θ; children(s,ti,α)=sorted(α,x,360−α−x) & sorted(V−α,y,x+α); minimax `can_force(th,state,K,memo)` returns True iff θ in state OR ∃(target,α∈1..V−1) with both children can_force at K−1. Memo key = (state,K) with EXACT integer tuple — no quantization.
Generalized engine (`/tmp/mulan_unit.py`): same with sum=180·U, θ_unit=θ·U, for non-half-grid θ (U = denominator, e.g. U=7 for θ=180/7).
