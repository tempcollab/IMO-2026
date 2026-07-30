## imo-2026-04 (lattice / discrete-structure route)

### Distinct openings surfaced
1. **Lattice-multiple invariant (the clean one).** The natural discrete set is "integer multiples of θ": an angle is "tainted" iff it equals kθ for some k≥1. Mulan wins iff she can force a taint; Shan-Yu avoids iff he can keep the triangle taint-free. This reframes the continuous game as a discrete taint game on the finite set {θ, 2θ, …, ⌊180/θ⌋·θ}.
2. **Alignment move (P-slot double-creation).** A single cut can place a multiple-of-θ in *both* children's P-slots simultaneously — this is the move that re-aligns an arbitrary triangle onto the "lattice of multiples." Its solvability is exactly the gate θ = 180°/n.
3. **Reduce move (tracked-vertex descent).** Once one angle is mθ, Mulan cuts that vertex with α=θ: one child gets θ (immediate threat), the other keeps (m−1)θ. Shan-Yu is forced into the (m−1)θ child; the tracked angle's level m strictly decreases to 1. Pure natural-valued potential.
4. **Four-case exclusion enumeration.** "Both children tainted" decomposes into α-slot / P-slot × α-slot / P-slot (4 pairings); three contradict the parent's taint-freedom, the fourth forces nθ=180. This is the hard exclusion half, and it is a finite casework, not a deep invariant.

### Candidate technique(s)
Invariant/monovariant on a discrete level set (the "multiples of θ" lattice) + a two-phase strategy (align once, then descend). Closest KB entry: *Invariants & monovariants* (Combinatorics) and *Induction / infinite descent* (General Methods). The potential is the integer level m of the tracked angle = mθ.

### Cheap-kill candidates
- The alignment move IS the cheap structural kill for the inclusion: it reduces "force θ from an arbitrary triangle" to "create a multiple of θ in both children of one cut," a one-move step whose feasibility is a single divisibility test (nθ = 180).
- The exclusion is a 2×2 casework (α-slot vs P-slot, in each child) — no heavy computation.

### Knowledge-base entries to use
- **Invariants & monovariants** (Combinatorics): the taint-free invariant and the decreasing level m.
- **Induction / infinite descent** (General Methods): inclusion strategy is induction on n (or on the level m).
- **Pigeonhole / extremal** (General Methods): "an interval of length > θ contains a multiple of θ" is the pigeonhole fact underpinning the alignment move's existence.

### Analogous past problems (cruxes)
- **aimo-0236** (combinatorics, invariants-and-monovariants) — token game: Alice adds a fixed constant a, Bob halves; termination hinges on a p-adic-valuation threshold "every token's valuation < v vs ≥ v." Crux: *find a regime preserved by both players' moves in which one player's move fixes every relevant level while the other's forced move strictly decreases a nonnegative-integer potential.* This is the exact structure here: the "level" of an angle = its index k in kθ; Mulan's alignment fixes levels (creates exact multiples), Shan-Yu's forced avoid reduces the tracked level by 1. Strong analogue — adapt the "preserved regime + decreasing natural potential" framing.
- **aimo-0077** (combinatorics, invariants-and-monovariants) — crux: *build a witness set as an arithmetic progression with common difference = the move's block length, so each move's window contains exactly one witness.* The multiples {θ, 2θ, …} are exactly such an arithmetic progression with difference θ; the alignment move creates two complementary witnesses (kθ and (n−k)θ) summing to 180. Resonant but not a direct citation.
- No crux in the corpus is a triangle/angle-cutting game (this is a 2026 problem); the analogues are structural (monovariant + arithmetic-progression witness), not geometric.

### Prior progress
None (round 1, empty workspace).

### The splitting operation — exact form (derived, verified)
Triangle T = (A, B, C), A+B+C = 180°. Mulan cuts to vertex A with parameter α ∈ (0, A) (α = the angle ∠BAP at the cut vertex, on the side of B). The two children are:
- **C1 = (α, B, A+C−α)**  — keeps angle B; angle at P = A+C−α = 180°−B−α.
- **C2 = (A−α, C, B+α)** — keeps angle C; angle at P = B+α.
(Verify sums: α+B+(A+C−α)=180 ✓; (A−α)+C+(B+α)=180 ✓.) Cutting to B or C is the cyclic permutation. So: **one angle is "split" (A → α and A−α), one angle is preserved per child (B in C1, C in C2), and the third angle in each child is the fresh "P-angle," a linear function of α.** Mulan controls α freely (any real in (0, A)); Shan-Yu chooses which child. (Verified by direct angle-chasing; also cross-checked against the retrograde solver: feeding exactly these child formulas reproduces the all-win lattice result.)

### Lattice closure condition
Let θ = 180°/n. The set L_n = {(aθ, bθ, cθ) : a+b+c=n, a,b,c ≥ 1} is the lattice of triangles whose angles are multiples of θ. It is **closed** under the operation when Mulan picks α = kθ (integer k): both children C1=(kθ, bθ, (a+c−k)θ) and C2=((a−k)θ, cθ, (b+k)θ) lie in L_n. A non-degenerate triangle lattice of this form exists iff nθ = 180° with n integer ≥ 2 (so that three positive multiples can sum to 180). This is the first hint that the answer is θ = 180°/n.

### Candidate answer (CONJECTURE, but very strongly supported)
**Mulan guarantees victory iff θ = 180°/n for some integer n ≥ 2** (equivalently 180°/θ is an integer ≥ 2; i.e. θ is a "unit fraction" of 180°). The winning set is {90°, 60°, 45°, 36°, 30°, 180°/7, 20°, …} = {180°/n : n = 2, 3, 4, …}.

Evidence (all conjectural, computational — NOT a proof):
- **Retrograde solve on L_n** (target = θ = 1 unit): for every n = 3…15, ALL of L_n is winning; rounds ≤ 2. Moreover, on L_N with target k, "all-win" holds **iff k | N** (tested N = 12, 24, 30, 36) — i.e. θ = (k/N)·180 wins on its lattice iff N/k is an integer, i.e. θ = 180/n.
- **1°-grid retrograde** (all integer-degree triangles, target = θ°): all-win **iff θ divides 180** (tested θ = 1…179; the all-win set is exactly the divisors of 180: {1,2,3,4,5,6,9,10,12,15,18,20,30,36,45,60,90}; non-divisors like 7,8,11,…,50,…,55 all FAIL). This tests off-lattice (e.g. θ=45 vs triangle (50,60,70), not on L_4) and confirms the divisibility condition, not just "lattice-aligned" triangles.
- **Implemented strategy (alignment + tracked reduction)** wins 400/400 random rational triangles for every n = 2, 3, 4, 5, 6, 7, 9, 12, 15, 20, 30, 60, 90, 120, 150, with max steps ≈ n−1 (matches the bound). Uses exact rational arithmetic (sympy-free Fraction).
- **Exclusion sim**: for non-divisor θ (50,7,80,100,25,42) Shan-Yu's taint-free invariant holds (Mulan cannot taint both children); for divisor θ (10=180/18, 180/7) the invariant breaks (alignment move exists). Consistent with the conjecture.

### The two key moves (the mechanics the outliner will assemble)

**(M1) Alignment move** (creates a multiple of θ in BOTH children's P-slots; re-aligns an arbitrary triangle to the lattice of multiples). Cut to vertex A (choose A = the largest angle), pick an integer k with
  B < kθ < A+B   (open interval of length A; exists since A > θ — see existence note),
set α = kθ − B. Then:
  - C2's P-angle = B + α = kθ.
  - C1's P-angle = A + C − α = 180° − B − (kθ − B) = 180° − kθ = (n−k)θ.
Both children now carry an exact multiple of θ (kθ and (n−k)θ), with 1 ≤ k ≤ n−1. This move is feasible **iff nθ = 180°** (the equation (n−k)θ + kθ = 180° is what makes the two P-angles complementary multiples); for θ ≠ 180°/n the alignment move has no solution (see exclusion).

Existence note: for n ≥ 3, the largest angle A ≥ 60° ≥ θ = 180°/n, with equality only in the equilateral θ = 60° case (already won); hence A > θ, so the open interval (B, A+B) of length A > θ contains a multiple of θ strictly (pigeonhole: multiples of θ are spaced θ apart). Also kθ < A+B = 180°−C < 180° forces k ≤ n−1, and kθ > B > 0 forces k ≥ 1. n = 2 (θ = 90°) is the special one-move case: cut to the vertex whose other two angles are acute (always exists unless already right), α = 90°−B puts 90° in both P-angles.

**(M2) Reduce move** (descends a tracked multiple to θ). If the triangle has an angle = mθ (m ≥ 2) at a tracked vertex V, cut to V with α = θ. Then C1 = (θ, …, …) already contains θ (immediate threat), and C2 = ((m−1)θ, …, …) carries the reduced multiple (m−1)θ at the cut-vertex remainder. Shan-Yu, to avoid θ, must keep C2; the tracked level decreases m → m−1. Repeat; at m = 1 the angle equals θ and Mulan wins. Validity throughout: (m−1)θ > 0 for m ≥ 2, and the drifting other angles stay positive and sum to 180° (B' + θ < 180° since B' < 180° − mθ). The **potential is the integer level m** of the tracked angle; it strictly decreases to 1, giving a finite bound of ≤ (m−1) ≤ (n−2) reduce moves.

**Inclusion strategy sketch (for the outliner to formalize, NOT a proof yet):** If θ already present, done. Else if some angle is a multiple mθ (m ≥ 2), run (M2) and descend. Else (no multiple present) run (M1) once to create a multiple in both children, then run (M2) on whichever Shan-Yu keeps. Total ≤ 1 + (n−2) = n−1 moves. (For n = 2, (M1) alone finishes in 1 move since it creates θ = 90° directly.)

### The exclusion half (the gate θ = 180°/n, derived)
For θ ≠ 180°/n, Shan-Yu maintains the invariant **"no angle of T is an integer multiple of θ."** Initial triangle: pick one avoiding the finite forbidden set {θ, 2θ, …, ⌊180/θ⌋·θ} (possible — it is a finite set of values). To preserve the invariant, Shan-Yu needs: from a taint-free parent, Mulan cannot make BOTH children tainted. Casework on how Mulan taints both children (cut to A; B, C untainted by invariant):
- C1 tainted via α-slot: α = k₁θ.  C2 tainted via α-slot: A−α = k₂θ. ⇒ A = (k₁+k₂)θ, contradicting A untainted. ✗
- C1 α-slot (α=k₁θ) & C2 P-slot (B+α=k₂θ). ⇒ B = (k₂−k₁)θ, contradicting B untainted. ✗
- C1 P-slot (A+C−α=k₁θ, i.e. α=180−B−k₁θ) & C2 α-slot (A−α=k₂θ). ⇒ C = (k₁−k₂)θ, contradicting C untainted. ✗
- C1 P-slot (α=180−B−k₁θ) & C2 P-slot (α=k₂θ−B). ⇒ (k₁+k₂)θ = 180°, i.e. **θ = 180°/n**. ✗ for θ ≠ 180°/n.
So for θ ≠ 180°/n, every Mulan move leaves at least one child taint-free; Shan-Yu keeps it; invariant preserved; θ (= 1·θ) never appears. This is a finite, rigorous casework (the crux of the hard direction). The key reason "a tainted angle = a Mulan win": if an angle = mθ (m ≥ 2), (M2) descends it to θ in m−1 forced moves; so Shan-Yu cannot tolerate ANY multiple, which is why the invariant must rule out all of them, not just θ.

### Where the gap could bite (open questions for the outliner)
1. **Reduce-phase vertex tracking under Shan-Yu's worst case.** The clean potential "level m of the tracked angle" requires that after each (M2) cut, Shan-Yu's forced child C2 actually carries the reduced (m−1)θ at a *locatable* vertex, so Mulan can keep cutting the same geometric angle. I verified this by exact-rational simulation (400/400 for n up to 150, max steps = n−1), but the prose proof must define the tracked vertex invariantly (e.g. "the angle that is a positive multiple of θ and was most recently created/reduced") and show it stays a multiple decreasing by θ while the other two angles never become a *smaller* multiple that Shan-Yu could exploit to fork — actually any multiple only helps Mulan, so the tracked-angle descent is the worst case. **Confirm: when several angles are simultaneously multiples, committing to descend any one of them still terminates** (my early greedy cycled when it switched which multiple to reduce; the fix is to commit to one tracked vertex). Outliner must state this cleanly.
2. **The alignment move's "smallest valid k" choice.** The interval (B, A+B) may contain several multiples kθ; the proof should pick any (e.g. the smallest) and confirm both kθ and (n−k)θ are in (0,180) and the resulting child angles are all positive. Straightforward but must be written.
3. **n = 2 (θ = 90°) boundary.** The general alignment move needs A > θ = 90°, which fails for acute triangles. Handle separately: θ = 90° is a 1-move win via the P-slot fork α = 90°−B (creates 90° in both P-angles), feasible iff the two non-cut angles are acute (always achievable by cutting to the largest angle's vertex). Verify this is the unique n = 2 instance and does not leak into n ≥ 3.
4. **Are there winning θ NOT of the form 180°/n?** The 1°-grid retrograde says no for integer-degree θ (exactly the divisors of 180 win), and the exclusion casework proves it for all real θ ≠ 180°/n. But the grid cannot test irrational θ directly; the exclusion casework is what carries that, so the outliner should make the casework airtight (it is the load-bearing wall). Double-check the casework covers θ irrational (where {kθ} never hits 180°, so combo 4 has no solution — consistent with "no winning θ outside 180°/n") and θ = 180°·(p/q) with p > 1 (e.g. θ = 2·(180/7) ≈ 51.4°; the grid test θ = 50° losing and the L_N-target-k tests confirm p > 1 loses).

### Small-case / intuition notes (CONJECTURE, from computation)
- θ = 90°: 1 move (P-slot fork). θ = 45°: 2 moves (align to 90° = 2θ, then fork). θ = 60°: 2 moves (align to 120° = 2θ, then fork — e.g. from (50,55,75), α=5 gives C1=(5,55,120), C2=(45,75,60); Shan-Yu keeps C1 with 120°=2θ, then cut to 120°-vertex, α=60 forkes both children to 60°). θ = 180°/n: ≤ n−1 moves (1 alignment + ≤ n−2 reductions).
- The dyadic chain (90, 45, 22.5, …) is a SUBSET (n = 2^k) — my first (wrong) guess. It is far too small: n = 3 (θ = 60°), n = 5 (36°), n = 7 (≈25.7°), … all win. The true boundary is "n = 180°/θ is a positive integer ≥ 2," not "n is a power of 2."
- The reason the dyadic-only guess failed: it used only the "fork" (both children get θ) and missed the "trap/align" move that creates a HIGHER multiple (kθ) in both children, which then descends. The alignment move is the actual crux.
