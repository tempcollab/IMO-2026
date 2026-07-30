## imo-2026-04 (game-theoretic / adversarial-invariant route)

## Operation (derived and verified)

State = unordered angle triple (A,B,C), A+B+C=180°, all in (0,180). Mulan picks a vertex to **destroy** (cut to) — say A — and a parameter α∈(0,A) (the part of angle A assigned to child 1). Let B,C be the other two angles. The two children are:

- **Child 1** (keeps B): (α, B, 180−α−B)
- **Child 2** (keeps C): (A−α, C, B+α)

Verified: sums = 180, all positive. **Supplementary pairing confirmed**: the two *new* angles at P are (180−α−B) and (B+α); their sum is exactly 180°. Reparametrize by β = B+α ∈ (B, 180−C): then child 1 = (β−B, B, 180−β), child 2 = (180−C−β, C, β), and the two P-angles are β and 180−β.

**Structural consequences (load-bearing):**
1. Each child **preserves exactly one** of the two non-destroyed angles. The destroyed angle is gone in both children. So Shan-Yu's discard chooses *which of two angles survives* — the angle Mulan "destroys" never survives.
2. The two P-angles are supplementary: β and 180−β. So if Mulan makes the P-angle of one child equal to θ, the P-angle of the *other* child equals 180−θ. **Shan-Yu takes the other.** Hence the supplementary trick only forces a win in one move when θ = 180−θ, i.e. **θ = 90°** (k=2). This is the unique one-move universal win.
3. For θ ≠ 90, forcing requires the *sibling* of the θ-bearing child to itself be a winning position — a 2-step (or k-step) reflection. Verified for θ=60: a (120,B,C) triangle with B+C=60 is a one-move win (cut to 120, set β=60+B: child1 = (60, B, 120) [has 60 via β−B=60], child2 = (60, C, 60) [has 60]; both children carry 60). So 120° triangles are forced in one move, and a general triangle can be pushed toward a 120°-triangle (lattice + minimax confirm θ=60 winning from every tested start).

## Conjectured characterization (strong evidence)

**Mulan wins ⟺ 180°/θ is an integer ≥ 2, i.e. θ = 180°/k for some k ∈ {2,3,4,…}.**

Equivalently θ ∈ {90, 60, 45, 36, 30, 180/7, 22.5, 20, 18, …} (infinite, accumulating at 0°; 0 excluded). **Unit-invariance forces this over the narrower "integer divisor of 180":** the problem is geometric and the operation is scale/ratio-invariant under the 180° total, so the answer cannot depend on θ being an integer number of degrees. The condition "180/θ ∈ ℕ" is a ratio (unit-free); "θ ∈ ℤ degrees" is not. The integer-lattice probe matched the *integer* members of {180/k}, but only because it only tested integer θ — it cannot distinguish the two, and the finer 7.5°-lattice resolves θ=22.5=180/8 as **winning** (equilateral ∈ W there).

Evidence:
- **Integer lattice (unit 1°, N=180, β integer), all 178 integer θ scanned:** winning set = exactly the divisors of 180 below 180 = {1,2,3,4,5,6,9,10,12,15,18,20,30,36,45,60,90}. This is precisely the integer members of {180/k : k≥2}. (Caveat: lattice restricts Shan-Yu's initial to integer-triangles and Mulan's β to integers — a subset game.)
- **Generalized lattice rule (verified):** on a lattice with unit u (N·u=180, integer N), target θ=t·u (integer t), the discrete attractor says Mulan wins on that lattice **iff t | N**. Since N/t = 180/θ = k, the condition t|N is automatic once k=180/θ is an integer (take u=θ, N=k, t=1, 1|k). So **whenever 180/θ∈ℕ, the θ-granular lattice is a win**, and finer lattices (u=θ/d) work the same way as long as d|k.
- θ=22.5 (=180/8) **winning** on the 7.5-lattice (t=3, N=24, 3|24); equilateral (8,8,8)·7.5 ∈ W. (An earlier depth-5 coarse-β minimax gave False for 22.5 — that was a **β-grid artifact**: it sampled α=A·{1..17}/18 and never hit the magic α=22.5 that creates the 22.5 angle. Do not trust coarse-β negatives.)
- θ=37.5 (=180/4.8, not Char-B): **losing** on every lattice tested (7.5-lattice t=5, N=24, 5∤24; no lattice with t|N exists since 180/37.5=4.8∉ℕ). Consistent.
- θ=72,100,120,144,54 (all non-Char-B): equilateral is in Shan-Yu's safe set on the lattice; real minimax (depth 3, fine β) cannot force from equilateral or near-equilateral non-integer starts.
- θ=45,36,30,60,90: real minimax (fine continuous β) forces within ≤3 moves from non-integer starts (61,60,59), (70,70,40), (100,50,30). Not lattice artifacts.

## Most promising Mulan winning strategy (and its wall)

**Lattice-attractor strategy on the θ-lattice (θ=180/k).** Mulan restricts to β that are integer multiples of θ (β=mθ, m∈{1,…,k−1}); then both new P-angles are multiples of θ (mθ and (k−m)θ). If the current triangle's angles are all multiples of θ, the children stay on the θ-lattice, and the discrete attractor (rule t|N, here 1|k) wins in finitely many moves.

**Wall:** this only works if the *current* triangle is already on the θ-lattice (all angles multiples of θ). The equilateral (60,60,60) is on the θ-lattice only when 3|k (θ=60,20,…). For other k, equilateral is NOT on the θ-lattice — so Mulan needs a **bridge** from an arbitrary real triangle to the θ-lattice. The depth-3 minimax wins for θ=45 from non-45-lattice starts, so a bridge exists, but it is not the trivial "first move snaps to lattice."

**Candidate bridge (the monovariant the outliner should formalize): a Euclidean-algorithm on θ-residues.** Define r(x)=x mod θ ∈ [0,θ). Since A+B+C=180=kθ, we have r(A)+r(B)+r(C)≡0 (mod θ), and each in [0,θ), so the residue-sum ∈ {0, θ, 2θ}. If the sum is 0, all residues 0 → on θ-lattice → win. Otherwise Mulan chooses α so that the new angles' residues strictly reduce the residue-sum (or reduce max residue) — the same Euclidean/gcd reduction seen in cruxes aimo-0225 (2-adic halving) and aimo-0236 (valuation descent). This is conjectural in detail but matches the lattice behavior and the KB's Kronecker/invariants entries. **The outliner must prove the residue-sum strictly decreases and reaches 0 in bounded steps.**

## Most promising Shan-Yu invariant (and where it leaks)

**Universal start = equilateral (60,60,60).** On the lattice, equilateral ∈ S (Shan-Yu's safe set) for *every* tested non-Char-B θ (72,100,120,54,144). For θ=120 the mechanism is explicit and clean: from equilateral, cut to a vertex, β∈(60,120). Child1=(β−60,60,180−β) and child2=(120−β,60,β). A 120° angle would require β−60=120 (β=180, excluded), 180−β=120 (β=60, excluded), 120−β=120 (β=0, excluded), or β=120 (excluded). **No single cut from equilateral can produce 120 in either child.** Moreover the supplementary trick reflects Mulan's 120-creating cuts (which need β=120 in some other configuration) back toward equilateral: setting a P-angle to 120 forces the sibling's P-angle to 60, and combined with the preserved 60's yields an equilateral-ish sibling that Shan-Yu keeps. Verified on lattice: for θ=120 the Mulan-winning region W = {(a,b,120):a+b=60} *exactly* the triangles already containing 120 — the attractor never grows beyond the target set. So from equilateral Mulan can never reach 120.

**Residue obstruction (general θ∤180):** write 180 = qθ+δ with δ = {180/θ}·θ ∈ (0,θ) (nonzero precisely when 180/θ∉ℕ). Then for *every* triangle, r(A)+r(B)+r(C) ≡ δ (mod θ) — never ≡0. So **no triangle can ever have all three angles multiples of θ** when θ∤180. This is a structural obstruction to the lattice-bridge. (Caveat: "all angles multiples of θ" is stronger than "Mulan wins", so this obstruction is necessary-but-not-sufficient for losing; the full losing proof needs the closed safe set S, not just the residue sum.)

**Where the invariant leaks / what the outliner must close:** the residue-sum obstruction alone does not forbid a *single* angle from equaling θ (an angle = θ has residue 0, which is compatible with sum ≡ δ as long as the other two residues sum to δ). So Shan-Yu needs a stronger invariant — a closed set S (greatest fixed point of "no θ-angle and every cut has a child in S") containing equilateral. The lattice computes S explicitly for each θ∤180 and it is large and stable; the real-game task is to exhibit a real closed set (likely defined by residue conditions + interval constraints on the angles) that contains equilateral and prove closure under arbitrary β. The θ=120 case above is the template.

## Distinct openings for the outliner (rival framings)

1. **Lattice-attractor + Euclidean residue bridge (Char B winning direction).** Prove: (a) on the θ-lattice Mulan wins (finite attractor, rule 1|k); (b) a residue monovariant drives any real triangle onto the θ-lattice in bounded moves. Top-level target: the whole characterization's "if" half.
2. **Supplementary-reflection / equilateral safe set (Char B losing direction).** Prove equilateral ∈ S(θ) for every θ with 180/θ∉ℕ, by exhibiting the real closed safe set (residue + interval) and proving closure under all β. Template = the θ=120 explicit reflection. Top-level target: the "only if" half.
3. **Potential/monovariant direct forcing (bypass the lattice).** Find a real-valued potential Φ(A,B,C) (e.g. min over orderings of |angle − θ|, or the residue-sum) that Mulan strictly decreases to 0 regardless of Shan-Yu's discard, giving a direct bounded forcing strategy without lattice detour. Top-level target: a self-contained winning proof for Char B.
4. **One-move-both-children characterization.** Classify exactly the (triangle, θ) pairs where Mulan has a cut making *both* children θ-bearing in one move (the θ=90 universal case; the 120-triangle for θ=60; etc.), then iterate. This is the "discard-aware" local move lemma that any global strategy composes from.

## Cheap-kill candidates (try before heavy computation)

- **Supplementary = 90° trick:** θ=90 is a one-move universal win (destroy the largest angle A; if A≥90 it's already 90 or A>90, then B,C<90 so β=90∈(B,180−C) and both children get a 90 at P). Free.
- **θ=120 from equilateral is unreachable in one move** (boundary exclusion β∉{60,120}) — free lower bound showing θ=120 losing via equilateral.
- **Residue-sum parity:** r(A)+r(B)+r(C)≡0 mod θ iff θ|180; instant necessary condition for the lattice-bridge to even be possible. Free obstruction for the losing direction.
- **t|N lattice rule:** instant check of which θ are winnable on a given lattice; rules out θ=37.5, 72, etc. on every lattice in one line.

## Knowledge-base entries to use

- **Invariants & monovariants** (Combinatorics): the residue-sum monovariant and the lattice safe set S are the two engines.
- **Kronecker / Weyl equidistribution** (Number Theory): motivating the residue-reduction / density of {mθ} on the lattice.
- **Three-gap / Steinhaus theorem** (Number Theory): the {kα} gap structure may govern the θ-lattice attractor's geometry — candidate for the bounded-depth bound.
- **Pigeonhole / extremal principle** (Combinatorics): the "every triangle has an angle ≤60 and ≥60" fact underlies θ=60.
- **Induction / infinite descent** (General): the residue-reduction is a descent on a natural-valued potential.
- **Hall's marriage / SDR** (Combinatorics): possibly for matching Mulan's move choices to forcing configurations (weaker candidate).

## Analogous past problems (cruxes)

- **aimo-0236** (combinatorics, games-and-strategy + invariants): "two-phase 2-adic valuation invariant, first-mover keeps the witness one step ahead; descent via halving." Crux = *maintain a valuation witness strictly above the opponent's reducing threshold, with a two-part induction holding before AND after each opponent move.* Analogous because: Mulan is the first-mover each round (she cuts, then Shan-Yu discards) and must nurse a residue/witness toward θ while Shan-Yu tries to discard it — the "witness one step ahead" framing fits the discard game. Adapt: the "valuation" is the θ-residue, the "threshold" is residue 0.
- **aimo-0225** (combinatorics, games-and-strategy): "P/N status determined by 2-adic valuation of a difference that exactly halves each step; flip depends on valuation parity." Crux = *game value by parity of a halving-valuation.* Analogous because the θ-lattice attractor reduces residue by a divisibility/halving dynamic; the P/N (Mulan/Shan-Yu) status on lattice states is governed by t|N. Adapt: replace 2-adic by θ-residue.
- **aimo-0262** (combinatorics, games-and-strategy): "self-reproducing invariant family of configurations restored after each opponent move, by induction." Crux = *hand the defender a self-reproducing invariant and show each legal move restores it.* This is the **template for Shan-Yu's losing strategy**: exhibit a family of triangles (the safe set S) closed under "after any Mulan cut, Shan-Yu can pick a child still in S." Directly the dual of this problem.

(No exact match in the corpus — this is a continuous reachability game, and the closest cruxes are valuation/invariant-flavored games. The three above give the right *proof shapes*; every borrowed step still needs proving from scratch.)

## Prior progress

None (round 1, empty workspace).

## Dead ends (do not retry)

- **Coarse-β depth-limited minimax for small/non-integer θ (e.g. θ=22.5, 180/7):** returns False but is an **artifact of the β-grid** (nalpha=18–25 misses the magic α values that create the θ-angle). Do not conclude "losing" from a neg search that doesn't sample β near θ-creating positions. Either (a) include all β such that some child angle = θ (β ∈ {θ, 180−θ, B+θ, 180−C−θ, …} intersect the interval), or (b) use the lattice attractor with a unit u that makes θ a lattice point.
- **"Contains a 60° angle" as a Shan-Yu invariant for θ=60:** the equilateral has 60 but Mulan destroys the 60-angle vertex and the survivor need not retain 60. Not closed. (For θ≠60 even worse.)
- **Subgroup/number-field invariant based on the initial triangle's angle group alone:** fails because Mulan chooses β from a continuum and can introduce any angle in one move. The invariant must be a *closed set of triples*, not a module generated by the initial angles.

## Small-case / intuition notes (labeled CONJECTURE)

- CONJECTURE (strong): winning θ = {180/k : k≥2 integer}. Verified on integer lattice (all 178 integer θ), on generalized lattices (rule t|N), and by fine-β real minimax for θ∈{30,36,45,60,90} from non-integer starts.
- CONJECTURE: equilateral (60,60,60) is the universal Shan-Yu defense for every non-winning θ. Verified on lattice for θ∈{54,72,100,108,120,135,144,150}; explicit one-move-unreachability shown for θ=120.
- CONJECTURE: the winning move count from the worst-case start is O(k) (θ-lattice attractor depth) — bounded and finite for each fixed k, but growing as θ→0. Needs the outliner's bound.
- The discard is the whole difficulty: supplementary pairing lets Mulan create θ in *one* child almost for free; the game is entirely about forcing the *sibling*. θ=90 is the only θ where sibling-creation is automatic (θ=180−θ).

## Sharp open questions for the outliner

1. **Bridge lemma (winning half):** Prove that for θ=180/k, from *any* real triangle (not necessarily on the θ-lattice, possibly with irrational angles), Mulan reaches a θ-lattice triangle (or directly forces θ) in finitely many bounded moves. The residue-sum Euclidean reduction is the candidate — prove it strictly decreases and terminates. *This is the crux of the whole problem.*
2. **Safe-set lemma (losing half):** For θ with 180/θ∉ℕ, exhibit a real closed set S (greatest fixed point of "no θ-angle and ∀cut ∃child∈S") with equilateral ∈ S, and prove closure under arbitrary continuous β. The residue-sum ≡δ≢0 obstruction is necessary; is it sufficient (together with interval constraints) to define S? Or is a finer invariant (e.g. "all angles lie in a specific union of residue classes modulo θ, plus open intervals avoiding θ") needed?
3. **Boundedness of the move count:** "Finitely many steps" needs an explicit natural-valued bound. On the θ-lattice the attractor depth gives one; does the residue-bridge add a bounded overhead, or can the number of residue-reduction steps blow up for irrational starts? (The Three-gap/Kronecker structure of {mθ} likely governs this — tie it down.)
