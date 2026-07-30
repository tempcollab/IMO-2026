# Build report — parity-measure-potential (imo-2026-03), round 6

Status: **partial** (advanced). Answer confirmed `c(n)=2^n/(2^{n+1}−1)`, minimax `D=u_n`.

## Deliverable 1 — Lemma U0 CERTIFIED (DONE)
Wrote `results/imo-2026-03/lemmas/even-multiplicity-corrector.md`, self-contained on certified
Lemma M:
- U0(a): every value even multiplicity ⇒ `D=0` (measure-zero odd-set).
- U0(b): budget `≥ m` ⇒ Xiang bisects all `m` pieces, every final value even multiplicity ⇒
  `D=0 ≤ u_n L`.
- U0(c): upper bound `UB(n)` is nontrivial only for `m=n+1`.
Ready for reviewer certification. Imported by `smoothing-majorization` (regime-i base) and
`breakpoint-vertex` (§4B) — unblocks both. Numerically re-verified (5/5 even-mult multisets → D=0).

## Deliverable 2 — GAP L2 via measure calculus (ADVANCED, still PARTIAL)
Route deliberately distinct from induction-peel's rearrangement (uses Lemma SPLIT's cross term,
not exchange).

**Closed rigorously this round:**
- **Master inequality** `D(S) ≥ |D(F) − D(B)|` for every a=0 refinement `S = F ⊔ B` (F = top
  fragments, B = tail refinement of `C_{n−1}`). Proof: Lemma SPLIT `D(S)=D(F)+D(B)−2μ(O_F∩O_B)`
  plus the trivial cap `μ(O_F∩O_B) ≤ min(D(F),D(B))` (Lemma M identifies `μ(O_F)=D(F)`,
  `μ(O_B)=D(B)`) and `x+y−2min(x,y)=|x−y|`.
- **IH input** `D(B) ≥ 1` (B is a refinement of `C_{n−1}` by `c_B ≤ n−1` cuts since `|F|≥2`;
  apply LB(n−1)).
- **Consequence:** the ENTIRE subregime `|D(F)−D(B)| ≥ 1` is closed — in particular every
  even-multiplicity fragmentation `D(F)=0` (via U0(a)), which subsumes the equal-bisection subcase
  AND the whole doubling-response family.
- **Extremal value = 1** computed exactly two ways (the attained top-down doubling cascade; the
  (L2-telescope) merged alternating formula `Σg_k − Σt_k = 2^n − (2^n−1) = 1`). So `1` is the
  correct floor, not a sample.

**Fixed a flaw in the prior file:** the round-5 "self-pairing ⇒ WLOG distinct fragments" reduction
was D-preserving (Lemma P) but silently dropped the refinement-of-`C_n` structure (top mass falls
below `2^n`), so it did not actually induct. Replaced by the F/B SPLIT decomposition, which keeps
`B` a genuine refinement of `C_{n−1}` for the IH.

**Residual explicit gap — GAP L2-exch (measure form):**
`μ(O_F ∩ O_B) ≤ (D(F)+D(B)−1)/2`, equivalently `D(S) ≥ 1`, needed only in the *balanced*
subregime `|D(F)−D(B)| < 1` with `D(F) > 0` (there the trivial cap is lossy). This is the genuine
interleaving-extremality crux — same combinatorial content as induction-peel's exchange step, here
isolated to a single clean scalar cross-term bound via the measure/SPLIT calculus (a second,
independent derivation route = diversity insurance). NOT closed. The per-cut toggle bound
`|ΔD|≤2s₂` is too loose (does not certify a floor).

## Numerics run (checks only, not proof)
- U0(a): even-mult multisets → D=0 exactly.
- (L2-telescope): n=4 canonical interleaving → D=1.000000.
- n=3, 3·10⁵ random a=0 refinements: master inequality `D(S) ≥ |D(F)−D(B)|` and `D(S) ≥ 1` never
  violated; residual regime is real (found `D(F)=D(B)=1` with master bound `0` but true `D(S)=2`,
  i.e. cross term happened to be 0 there).

## Spec / scope concerns
- GAP L2-exch (this file, measure route) and induction-peel's Gap-Interleaving exchange share the
  same combinatorial target object — the outline-reviewer's flagged closeness risk stands. The
  genuinely-different insurance line for the lower wall remains `breakpoint-vertex` (VERT finitizes
  L1/L2). Recommend keeping it in the build set.
- The measure route now pins the L2 residual to ONE scalar inequality; if either the exchange
  route or the finiteness route closes the interleaving-extremality, L2 falls. Suggest next round
  the outliner point one builder at proving `μ(O_F∩O_B) ≤ (D(F)+D(B)−1)/2` directly (adjacent-atom
  toggle across a single tail value `t_k`), which is the cleanest scalar form of the crux.

Files touched:
- results/imo-2026-03/lemmas/even-multiplicity-corrector.md (new, for certification)
- results/imo-2026-03/approaches/parity-measure-potential.md (updated: imports, GAP L2 section,
  Status/Approaches/Current best/Open gaps/Promotable)
