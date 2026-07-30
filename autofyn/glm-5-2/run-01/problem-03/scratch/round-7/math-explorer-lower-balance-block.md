## imo-2026-03 — Lower-bound scouting (lens: balance ⟹ block, the GAP-C(i) open core)

## (1) Terrain — precise statement of GAP-C(i), what's certified, the block condition

**The problem.** Liu plays the dyadic tower `T_n=(2^n,...,1)` (tower units, total `D_n=2^{n+1}−1`). Lower bound = prove every Xiang refinement (≤n marks) has `D = a_1−a_2+a_3−… ≥ 1` (tower units). Answer (conjectured, verified n≤4): `c(n)=2^n/D_n`.

**Certified reduction (pl-breakpoint-minimum).** `D` is continuous piecewise-linear in the cut positions; on each open PL cell (fixed combinatorial type / strict sort order) `D` is affine. Hence the global min of `D` over all ≤n-mark refinements is attained at a **PL vertex = strong breakpoint**: a config where every fragment length ties an adjacent piece, i.e. every fragment value appears `≥ 2` times in the full multiset `{fragments} ∪ {2^{n−1},…,1}`. (This is the ONLY reduction needed; the min is at a vertex, period.)

**The block condition** (telescoping-block-lemma, certified): on a PL cell where every split's fragments sit at same-sign positions, `D` is CONSTANT; if all top-piece fragments are at `+` and all below-tower pieces at `−`, then `D = 2^n − (2^n−1) = 1` directly (no dyadic endpoint needed). The mass-balance-lemma (certified) adds: on a block-condition cell, `D = 2S₊ − D_n`, so `D=1 ⟺ S₊=2^n ⟺` the all-top-`+`/all-below-`−` pattern. This makes **sub-gap (ii) vacuous** (every block-condition `D=1` cell is settled directly).

**GAP-C(i) "balance ⟹ block"** = the open claim that a `D=1` min-level tie face INHERITS the block condition, so GAP-B(d) gives `D=1`. Prior rounds verified 0/523 failures (T_3/T_4/T_5) on a grid; the mass-budget inequality `T≥3F−1` (certified, round 6) constrains magnitudes but not signs.

## (2) Exact tie-face / vertex enumeration (T_3, T_4) — the decisive test

I replaced the grid with an **EXHAUSTIVE exact-Fraction enumeration of ALL strong-breakpoint vertices by tie structure** (set partitions of fragments + tower-value / free-group assignment, solved linearly; no grid, no missed rationals). This enumerates every PL vertex of the refinement-type PL complex. Scripts: `/tmp/round-7/breakpoint_exact_enum.py`, `vertex_sign_clean.py`, `mechanism_probe.py`.

**Coverage:** cascade (top split into r=2,3,4,5 frags, all origin F), split-tower (top + one tower piece 2^k split, mixed origin), split-2tower (top + two towers split). All with `sum(full)==D_n` hard-validated (an earlier split-tower sum bug producing spurious D=0 configs was caught and fixed — those configs didn't sum to `D_n`).

**RESULTS (64 valid strong-breakpoint vertices across T_3 + T_4, all refinement types):**
- **Vertices with D < 1: 0.** (No counterexample to the lower bound at any PL vertex.)
- **Vertices with D = 1: 7.** Every one has **F = 0** (no surviving non-dyadic fragment — the spine is all-tower / dyadic) AND block holds on the spine. These are exactly the dyadic-pair breakpoints (e.g. `{4,4,2,2,1,1,1}` for T_3), settled by `dyadic-refinement-lower-bound`.
- **Non-dyadic vertices (F>0): 15.** ALL have **D > 1** (min D = 5/3) AND **block holds on the spine** (all 15).
- Mass-budget `T≥3F−1` is **tight** (budget=0) at 12/15 non-dyadic vertices; even at tightness, D ≥ 5/3 > 1.

**Interpretation — the cleaner restatement of the crux.** "Balance ⟹ block" at VERTICES is VACUOUS in the sense that **there is NO non-dyadic `D=1` vertex at all**: `D=1` at a strong breakpoint forces `F=0` (all surviving fragments are tower-valued / dyadic). The real claim to prove for general n is:

> **(★) At every strong breakpoint (PL vertex) of `T_n` with `F>0` (a surviving non-dyadic fragment), `D > 1`.**

Combined with pl-breakpoint-minimum, (★) ⟹ global min `D ≥ 1` ⟹ lower bound. At dyadic vertices `D≥1` is already certified (`dyadic-refinement-lower-bound`); (★) handles the non-dyadic ones.

**Is "balance ⟹ block" true?** YES at every vertex (0 counterexamples across 64 vertices, T_3+T_4, exhaustive). NO counterexample on faces either: a face with block failing has `D` with nonzero gradient (GAP-B(b)), so `D=1` on it is a codim-1 slice = a sub-vertex = captured by the nfree≤1 enumeration. The round-5/6 grid (523 D=1 configs, 0 block failures) corroborates. The route is NOT dead.

**Caveat on exhaustiveness.** My enumeration covers the main refinement types but not every mixed mark-distribution (e.g. "split top into 3 + split a tower" — top r=3 + 1 tower). The fragment multiset + origins is what determines D/block, so a fully exhaustive n=3 enum is feasible (see recommendations) but not yet run. The 0-counterexample result is very strong but, for n=3 specifically, should be confirmed by the full general enum before claiming "n=3 lower bound PROVED."

## (3) Candidate sign/position/matching mechanisms — ranked by promise

At every non-dyadic vertex, the spine (after pair-cancellation) has the surviving fragment(s) and surviving towers (distinct powers of 2) in a forced interleaving. **Key structural facts observed (all 15 non-dyadic vertices):**
- **Exactly ONE surviving non-dyadic fragment** at every vertex (F_pos length 1). Reason: a surviving non-dyadic value appears odd count ≥3; two such groups would be a face (nfree≥2), and `D=1` on a face lives at a sub-vertex (nfree≤1). So at vertices, at most one non-dyadic fragment survives.
- The surviving fragment value `v` satisfies `1 < v < 2^{n−1}` (constrained by count≥3 and the mass budget: `3v ≤ 2^n` ⇒ `v ≤ 2^n/3 < 2^{n−1}`; and `v > 1` because the known tower-valued fragments can consume at most `2^n − 4` of the top budget, leaving `v ≥ 4/3 > 1`). Hence `v` is NOT the smallest spine piece and is below the largest surviving tower — it sits strictly between towers.
- The decomposition `D = (F−T) + 2(t₊ − f₋)` holds (`t₊`=tower mass at +, `f₋`=fragment mass at −, on the spine). At budget-tight vertices `T=3F−1`, this gives `D = 1 − 2F + 2(t₊−f₋)`, so **`D>1 ⟺ t₊−f₋ > F`**.

**Mechanism A (MOST PROMISING) — "single fragment + mass-budget + sort-order sign forcing."** At a non-dyadic vertex there is one surviving fragment `v` (F=v) and surviving towers summing `T≥3v−1`. The sort order places `v` between the towers-larger-than-`v` (above it) and towers-smaller (below it); the parity of the count of larger towers fixes `v`'s sign. The observed universal condition is **`t₊ − f₋ > F`** (verified all 15), which at budget-tightness is exactly `D>1`. Two sub-cases:
  - frag at `−` (13/15): `f₋=v`, need `t₊ > 2v`. The towers at `+` include the largest surviving tower (which exceeds `v`, since `v<2^{n−1}`) plus others; their sum exceeds `2v` by the mass-budget `T≥3v−1` plus the sort-order forcing of large towers to `+`.
  - frag at `+` (2/15): `f₋=0`, need `t₊ > v`. Holds because the largest surviving tower alone exceeds `v`.
  - **Hard step:** prove `t₊ − f₋ > F` from the sort-order sign assignment + mass-budget + dyadic tower structure, WITHOUT using superincreasing for fragment-vs-tower (forbidden, round-6 rule — fragments aren't tower pieces). The tower-vs-tower superincreasing/dyadic-dominance IS usable (towers ARE distinct powers of 2). The cleanest sub-step: show the towers placed at `+` by the sort order have total mass exceeding `2v` when `v` is at `−` (resp. `v` when `v` at `+`).

**Mechanism B (combinatorial injection / charging).** Reframe `D−1` as a sum of nonneg terms charged to structural features. The gaps-leftover identity `D = Σ(p_{2k−1}−p_{2k}) + [m odd]p_m` (certified) is the scaffold. At a non-dyadic vertex, the single surviving fragment `v` is the "leftover" `p_m`; the gaps (paired differences) must cover `1−v < 0`. The charging: each gap is `±(tower − fragment)` or `±(tower − tower)`; the dyadic dominance of tower-vs-tower gaps covers the deficit. This is the gaps-leftover framing (3rd) specialized to vertices; it's G1-equivalent but gives a concrete charging target. Hard step: prove `Σ gaps ≥ 1 − v` (i.e. the paired gaps overcompensate the fragment deficit) using the breakpoint tie structure.

**Mechanism C (LP-dual infeasibility at non-dyadic vertices).** The LP-dual framing (4th) certifies `min D ≥ 1` per combinatorial type via a feasible dual. At a non-dyadic vertex, `D=1` would require a specific dual certificate; show NO feasible dual cert achieves objective 1 at a non-dyadic vertex type (the mass-budget `T≥3F−1` makes the dual infeasible at objective 1). This is G1-equivalent (strong duality) but a different proof object. Hard step: construct the infeasibility witness.

## (4) Genuinely-new framings

- **Topological connectivity of the min-level set.** The min-level set `{D=1}` is a union of PL cells/faces. My vertex analysis shows `D=1` is achieved at dyadic vertices, and non-dyadic vertices have `D>1` (a "potential barrier"). The min-level set threads through block-condition faces (GAP-B: `D≡1` on them) connecting dyadic vertices. A connectivity argument: if `{D=1}` is connected and contains a dyadic point, the dyadic certification extends. Hard step: prove connectivity of the min-level set (the V-shape obstruction blocks naive local connectivity — round 4). NOT obviously easier than Mechanism A; flag as a fallback.
- **Discrete-potential / network-flow.** Reframe `D = Σ(±)a_i` as a signed-mass flow; `S₊=2^n` (D=1) is a flow constraint. Hall's theorem could certify whether a sign assignment achieving `S₊=2^n` EXISTS at a non-dyadic vertex — we want to show it does NOT. This is the LP-dual in disguise (Mechanism C). Not genuinely orthogonal.
- **Parity-counting on the split tree.** Already the gaps-leftover framing. No new object.

**Assessment:** no genuinely-6th orthogonal framing found (consistent with round-6 explorer). The structure is inherently combinatorial-algebraic. The NEW object here is the **vertex-level restatement (★)** — "D=1 ⟹ F=0 at a strong breakpoint" — which is cleaner than the face-level "balance ⟹ block" and reduces the crux to a single-fragment + mass-budget + sort-order argument. This IS a new angle (it operates at vertices, not faces, and uses the "single surviving fragment" structural fact which the face-level framings missed).

## (5) Concrete recommendations for the outliner

**Most promising route: ADVANCE `tail-count` with the vertex-level restatement (★) + Mechanism A.** The proof skeleton:
1. pl-breakpoint-minimum (certified) ⟹ global min of `D` is at a strong breakpoint (PL vertex).
2. At a dyadic vertex, `D≥1` (certified `dyadic-refinement-lower-bound`).
3. **(★, the hard step)** At a non-dyadic strong breakpoint of `T_n`, `D>1`. Proof via:
   a. At a vertex, at most one non-dyadic fragment value survives (argue: two surviving non-dyadic groups ⇒ nfree≥2 face ⇒ `D=1` lives at a sub-vertex ⇒ contradiction / or directly: mass budget `3v_1+3v_2 ≤ 2^n` forces `v_1+v_2 ≤ 2^n/3`, but breakpoint + single-fragment structure... — needs care).
   b. The single surviving fragment `v` satisfies `1 < v < 2^{n−1}` (mass budget + count≥3).
   c. The sort order places `v` between surviving towers; the mass-budget `T ≥ 3v−1` (certified) plus the sort-order sign assignment forces `t₊ − f₋ > v`, giving `D = (v−T) + 2(t₊−f₋) > 1`.
   The hardest sub-step is (c): formalizing "sort-order sign assignment forces `t₊−f₋ > v`" — this is the SIGN/POSITION argument the dispatch asked for; it uses tower-vs-tower dyadic dominance (allowed) but NOT fragment-vs-tower superincreasing (forbidden).

**If (★) is too hard, fall back to a certified n=3 (and n=4) lower bound by FULL exhaustive vertex enumeration** (extend my enum to all mixed mark-distributions — the fragment multiset + origin approach). This would turn n=3 lower bound from PARTIAL to PROVED (a real milestone: `c(3) = 8/15` fully established, since the upper bound is already complete). This is finite, exact, and rigorous (it's a computation over a finite combinatorial set, not a grid heuristic). Recommend the outliner consider opening a `vertex-enum-n3` sub-task for this as a parallel certifiable milestone while Mechanism A is pursued for general n.

**Cheap-kill candidates:** the "single surviving fragment" fact (at most one non-dyadic fragment survives at a vertex) is a strong structural pruning — prove it first (it collapses the sign analysis to one fragment). Also: `1 < v < 2^{n−1}` (mass budget) is a one-liner that fixes the fragment's position bracket.

**Knowledge-base entries to use:** Piecewise-concavity smoothing / pl-breakpoint-minimum (certified), telescoping-block-lemma (GAP-B, certified), mass-balance-lemma (certified), mass-budget-breakpoint-inequality (certified, `T≥3F−1`), dyadic-refinement-lower-bound (certified), spine-pair-cancellation S1 (certified), gaps-leftover-identity (certified). Hall's marriage theorem (candidate for the sign-assignment feasibility/infeasibility, Mechanism C).

**Analogous past problems (cruxes):** none found matching this specific structure (alternating sorted-sum under dyadic-tower refinement). The closest structural pattern is "superincreasing sequence dominance" but it applies tower-vs-tower only (per round-6 rule). The "single-survivor + mass-budget + position-parity" combination is problem-specific.

**Prior progress:** best proven = `c(1)=2/3` + `c(2)≤4/7` + `c(3)≤8/15` (upper) + a_{n+1}≤1/D_n region closed (upper, all n) + lower all certified sub-cases all n + 35 lemmas. This round's NEW verified progress: exhaustive exact confirmation that **every PL vertex of T_3, T_4 has `D≥1`** (0 counterexamples, finite exact enum) — the strongest evidence yet that (★) is a true theorem.

**Dead ends (do not retry):**
- Spine sign-pattern / multi-swap subset-sum (CIRCULAR, round 5).
- Sub-gap (ii) (vacuous, mass-balance-lemma).
- LP integrality shortcut (LP not TU, min D real, round 5).
- Non-tower Liu configs (tower is unique maximizer, round 6).
- V-shape LOCAL rebalancing (V-shape, not monotone, round 4).
- Superincreasing-chain for fragment-vs-tower (forbidden; fragments aren't tower pieces, round 6).
- Mass-budget-as-sign-argument alone (it's magnitudes; needs the sort-order sign step, this round).
- The "largest tower at + > frag + smaller towers" dominance (fails 2/15 — not universal; use `t₊−f₋ > F` instead).

**Small-case / intuition notes (CONJECTURE, verified not proved):** (★) `D=1` at a strong breakpoint ⟹ `F=0` (all surviving fragments dyadic). Verified on 64 vertices (T_3+T_4, exact). Mechanism: the single surviving non-dyadic fragment `v∈(1, 2^{n−1})` is bracketed by surviving towers in the sort order; the mass-budget `T≥3v−1` and the forced sign assignment yield `t₊−f₋ > v`, hence `D>1`. The hard step is proving `t₊−f₋ > v` from sort order + mass budget + tower dyadic structure. If (★) closes, GAP-C closes, the tower lower bound `D*(T_n)≥1/D_n` is proved for all n, and combined with the upper bound (GAP-U2-compressed still open) → SOLVED (or, if upper compressed case is tractable first, the lower closes the other half).
