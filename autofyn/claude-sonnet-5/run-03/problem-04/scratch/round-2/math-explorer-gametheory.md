## imo-2026-04

### Core structural fact (verified algebraically and numerically) — the child-triangle formula
Let T have angles (α at A, β at B, γ at C), α+β+γ=180°. If Mulan cuts from P on side BC
(opposite A) splitting α into x1 (=∠BAP) and x2=α−x1 (=∠CAP), then, by the exterior-angle
theorem at P:
- **Child1 = ABP**: angles {β, x1, γ+x2}   (keeps β fully, loses γ)
- **Child2 = ACP**: angles {γ, x2, β+x1}   (keeps γ fully, loses β)
(∠APB = γ+x2 and ∠APC = β+x1 are supplementary, sum 180°, matching ∠APB+∠APC=180.)
This is the master formula: every move is "pick a vertex to split (destroying that vertex's
angle, redistributing it as x1,x2), keep the other two vertices' angles each in one child,
and each child gets a new angle = (kept-angle of the OTHER child) + (split-part going to the
OTHER child)." This identity is exact and should be cited directly (no need to re-derive from
scratch each approach — but it must still be proven in the final writeup via exterior angle
theorem, it's elementary).

### Distinct openings
1. **θ = 90° is a universal 1-move win, proved in closed form.** Pick the vertex A with the
   *largest* angle α (so the other two, β,γ, are both <90°, since a triangle has at most one
   angle ≥90°). Choose x1 = α−90+γ (equivalently solve γ+x2=90). Then Child1 has angle
   90° at P (∠APB=90°) AND Child2 has angle β+x1 = 90° at P too (since the two P-angles are
   supplementary and 90 is the unique self-supplementary value: 90+90=180). **Both children
   contain 90° — Shan-Yu cannot avoid it, for ANY starting triangle.** Verified both
   algebraically and numerically (Bash/Python, 5 random triangles, both children always hit
   90.0000° exactly). This is a clean, fully rigorous result — worth building an approach
   around directly, and it also strongly hints that the general winning region for Mulan is
   built from repeatedly reducing to a "some angle = 2θ" situation (see opening 3 below), of
   which θ=90°→2θ=180 is a degenerate/trivial instance (any split of any angle a into
   (a/2,a/2) using θ=a/2... not quite the same trick, but structurally related: whenever the
   *split vertex's angle itself equals 2θ*, an even split forces x1=x2=θ, giving both children
   angle θ — a second, more general 1-move win condition worth exploring.)

2. **θ > 90°: Shan-Yu has an explicit, fully rigorous invariant survival strategy — I proved
   this completely, not just conjectured it.** Claim: for θ>90°, Shan-Yu wins (survives
   forever) by (a) picking any initial triangle with all angles ≤90° (e.g. equilateral 60-60-60,
   or any acute/right triangle — always possible and never has an angle >90 so never equals
   θ>90 either), and (b) at every subsequent step, always keeping a child whose three angles
   are all ≤90°. Proof this is always possible: suppose current T has all angles ≤90 and Mulan
   splits vertex-angle a≤90 into x1,x2 (x1+x2=a≤90, so 0<x1,x2<90 strictly). The two new
   P-angles are (c+x2) and (b+x1) with (c+x2)+(b+x1) = b+c+a = 180, so **at least one of them
   is ≤90**. Whichever child has its P-angle ≤90 also has its other two angles (the kept angle
   ≤90 by the invariant, and x1 or x2 <90) — so that WHOLE child has all angles ≤90. Shan-Yu
   keeps that child. Induction closes: the invariant "all angles ≤90°" is maintained forever,
   so no angle ever equals θ>90°, Mulan never wins. **This settles the θ>90 direction
   completely** (modulo writing it up formally) — no further exploration needed there, it's a
   proof, not a conjecture. Note the invariant breaks exactly at 90° (which is why θ=90 itself
   is a Mulan win, not covered by this strategy — consistent with opening 1).

3. **θ ≤ 90°, pure "exact-chip forcing" sub-strategy (deterministic subgame) — strong evidence
   Mulan wins, but a real gap remains for special resonant θ.** Whenever Mulan sets x1=θ exactly
   (valid iff 0<θ< the split vertex's angle S), that child contains θ; Shan-Yu is FORCED into
   the complementary child, giving a **deterministic** transition. There are actually 4 distinct
   "exact-threat" moves per chosen split-vertex S (with other two angles P,Q): threaten via
   x1=θ, via x2=θ, via the P-angle (Q+x2)=θ, or via the P-angle (P+x1)=θ — each valid under its
   own positivity constraint, forcing a specific deterministic successor. I coded this
   "forcing-only" subgame (BFS/game-graph over the deterministic transitions) and tested it
   numerically (Python, see below): for a fixed generic triangle (70°,65°,45°), sweeping
   θ=5°,10°,...,175°, **every θ>90° dies immediately (0–4 ply)** — consistent with and a nice
   independent check of the rigorous invariant in opening 2. For θ≤90°, MOST values force a win
   quickly via pure chipping (θ=90:0 ply, 60:1, 45:0, 30:5, 20:9, 15:1, 35:0, 65:0, 70:0, 10:5,
   5:7 ply) — **but not all**: θ=25° and θ=40° and θ=50° and θ=55° died (cycled in a finite
   closed orbit of ~10–56 states) despite being <90°. A closer probe of θ=180/7≈25.714°
   (chosen because 180/n for n=2,3,4,5,6 — i.e. 90,60,45,36,30 — all won via pure forcing
   quickly, but n=7 didn't) confirmed: pure forcing **provably cycles forever without ever
   hitting θ** for θ=180/7 (BFS closes into a finite set of ~121–128 states with no further new
   states reachable and none equal to θ). **This does NOT mean Shan-Yu survives for θ=180/7** —
   it only means the *restricted* "always chip exactly θ" strategy fails; Mulan is not
   restricted to that. She can also make non-forcing "setup" moves (split value ≠ any of the 4
   threat values) that give Shan-Yu genuine choice between two non-threatening children, and
   still win overall if BOTH children are (recursively) Mulan-winning positions. This full
   two-player minimax ("T is Mulan-win iff θ∈T already, or ∃ move s.t. BOTH children are
   Mulan-win") is the real object of study and is NOT reducible to the pure-forcing subgraph.
   **This is the key open gap**: does the richer move set (non-forcing setup moves + forcing)
   let Mulan escape resonant values like 180/7 and win for ALL θ≤90°? I could not resolve this
   in the exploration budget — flagging it explicitly as the crux gap for the outliner.

### Candidate technique(s)
- Invariant / monovariant argument (knowledge_base.md: "Invariants & monovariants", "Invariant/
  monovariant" under General Proof Methods) — directly gives the complete θ>90° direction (see
  opening 2), and is the natural template to try to extend/refine for the θ≤90° direction (e.g.
  find an invariant Mulan can force PROGRESS on, like a potential function that strictly
  decreases toward an integer count of remaining "chip moves needed").
- Induction / strong induction on a well-founded potential function (e.g. on the value
  ⌈max-angle/θ⌉ or on number of "chippable" vertices) for the θ≤90° forcing-win direction.
- Exterior-angle / angle-chasing (knowledge_base.md "Synthetic toolkit") underlies the master
  child-formula derivation — needs to be stated cleanly in any approach.
- IVT / continuity-of-choice argument (Mulan's x1 ranges over a continuum, giving her exact
  control of the resulting P-angle over an open interval) — likely needed to close the θ≤90
  resonance gap (opening 3), possibly via a 2-move combo that first perturbs a "bad" state off
  its resonance before resuming forcing.

### Cheap-kill candidates
- **At most one angle of a triangle can be ≥90°** — trivial parity-like structural fact,
  directly gives the θ>90° survival invariant (opening 2) with no heavy machinery. This alone
  likely settles (rigorously) one whole direction of the "iff" — a genuine cheap kill, already
  essentially complete, not just a pruning heuristic.
- **Supplementary-pair symmetry** (the two new P-angles always sum to 180°) is the reason θ=90°
  is uniquely a forced 1-move win — worth checking early for any θ whether α=2θ for the current
  triangle's largest angle (instant double-win), a cheap check before deeper strategy.

### Knowledge-base entries to use
- "Invariants & monovariants" / "Invariant / monovariant" (General Proof Methods) — for the
  θ>90 survival proof and likely for the θ≤90 forcing argument.
- "Synthetic toolkit: angle chasing" — underlies the child-angle formula (exterior angle
  theorem).
- "Induction" (ordinary/strong) — natural framework for both directions (Shan-Yu's invariant
  induction; Mulan's forced-win induction on number of remaining chips).

### Analogous past problems (cruxes)
Searched crux corpus (`domain=combinatorics`, `subtopic=games-and-strategy`, 39 entries) and
scanned for triangle/angle/cut-based games plus geometry. **No genuinely analogous problem
found.** The closest surface matches were:
- `aimo-0225` (game on a regular n-gon, strategy-stealing via symmetry + 2-adic valuation
  recursion) — technique of "recursing on valuation that halves each step, P/N status flips with
  parity" is a loose structural echo of the "chip exactly θ, deterministic forced successor"
  mechanic found here, but the underlying combinatorics (polygon counters vs. continuous
  triangle angles) is different enough that I would not call it truly analogous — flag as
  weak inspiration only, not a real match.
- `aimo-0766` (IMO 2024 hunter vs. invisible rabbit) — superficially a pursuit game with
  continuous real-valued moves and an adversary, but the "hide behind sensor tolerance" crux
  move doesn't transfer; not analogous.
No geometry cruxes exist in the corpus (per crux_moves_documentation.md), so nothing closer
was available. **Verdict: no strong crux match — this problem's core mechanic (cevian-split
game with discard) appears to be a fresh construction not mirrored in the corpus.**

### Prior progress
None — this is the first exploration round for imo-2026-04 (empty `results/imo-2026-04/`
population per the dispatch).

### Dead ends (do not retry)
- **Treating "pure exact-θ chip forcing" as a complete strategy for all θ≤90°.** It provably
  cycles without hitting θ for resonant values like θ=180/7≈25.714° (verified via exhaustive
  BFS over the deterministic forcing-move graph, ~121-128 state closed orbit, no escape). Any
  approach that tries to prove θ≤90°⟹Mulan-wins using ONLY the four "exact-threat" forcing
  moves (x1=θ, x2=θ, P-angle=θ two variants) will hit this exact wall. A correct approach must
  also use non-forcing "setup" moves with a genuine two-branch (AND) argument, or a smarter
  global argument (e.g. continuity/IVT over a bounded number of moves) — not yet found.
- Do not assume symmetry θ↔180−θ in this game — the mechanics are NOT symmetric under this
  substitution (verified numerically: θ=30 wins fast via forcing, θ=150 dies immediately;
  θ=45 wins, θ=135 dies) — the boundary is at 90°, not some symmetric pair.

### Small-case / intuition notes (labeled conjecture where not proven)
- **Proven**: θ>90° ⟹ Shan-Yu wins (survives forever), via the "keep all angles ≤90°" invariant
  (opening 2, full proof given above — ready for the outliner/builder to write up rigorously,
  this looks essentially complete already).
- **Proven**: θ=90° ⟹ Mulan wins in exactly 1 move for every starting triangle (opening 1).
- **Conjecture (strong numeric support, not proven)**: θ<90° ⟹ Mulan wins, via a combination of
  forcing moves (quick, for "nice" θ) and non-forcing setup moves to escape resonant/bad θ like
  180/7 (needs new argument). Tested θ=5,10,...,85 in 5° steps against a fixed generic triangle
  under pure forcing: most win within ≤9 ply; θ=25,40,50,55 cycle under pure forcing alone
  (open gap, not evidence against the conjecture, since Mulan has more tools available).
- Overall best-guess characterization for the outliner to target: **Mulan can force a win iff
  0° < θ ≤ 90°** (closed at 90, open at 180 side). This is a conjecture for the θ≤90 direction
  and a theorem (as proven above) for the θ>90 direction. The main remaining work is closing the
  resonance gap in opening 3 to make θ≤90° fully rigorous, likely via a cleverer inductive
  strategy for Mulan that doesn't rely solely on hitting θ by exact repeated subtraction.

### Verification code used (for reproducibility, not part of any proof)
Python/Bash simulations (exact algebraic child-formula, BFS over the deterministic
forcing-move graph) were run in this session to produce all numeric claims above; e.g. the
θ=90° double-win formula was checked on 5 random triangles (all exact hits to floating precision),
and the forcing-graph sweep θ=5°..175° step 5° was run against triangle (70°,65°,45°).
