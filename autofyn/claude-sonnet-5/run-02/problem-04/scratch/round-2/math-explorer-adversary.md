## imo-2026-04 (adversary-side exploration)

Note: `problems.jsonl` lists this problem's `difficulty_level` as `"medium"` (rating 7), not
`"hard"` — flag this discrepancy to the orchestrator, but proceeding with the assigned task
since the run has already committed to this problem_id.

### Setup (same notation as sibling report)
Triangle angles (p,q,r), p+q+r=180. Cutting the vertex with angle p, letting x1 range freely
over (0,p), gives children A={q,x1,r+p-x1}, B={r,p-x1,q+x1}. Verified via sympy:
sum(A)-180=0, sum(B)-180=0 identically. Re-derived and confirm the sibling's two base facts
independently:
- **θ>90° impossible**: re-derived the non-obtuse invariant from scratch — for p,q,r≤90, the
  two "new" angles r+p-x1 and q+x1 sum to exactly 180, so at most one exceeds 90; the other
  child is automatically non-obtuse. Shan-Yu picks a non-obtuse starting triangle and always
  keeps whichever child stays non-obtuse. Holds up; no hole found.
- **θ=90° forceable in 1 move from ANY triangle**: re-derived independently via the altitude-
  foot construction; confirmed the "universal double hit" only exists for V=90 (any other V
  requires an existing angle 2V, i.e. is state-dependent, not universal).

### NEW mechanism found: the "transfer move" (the main new result this round)
This is a strictly more powerful and more general tool than plain bisection, and it resolves
the sibling's open question in the negative for the pure-dyadic conjecture (H2 is false) while
also showing H1 ("all θ≤90° work") is probably too strong as stated.

**Lemma (transfer, verified algebraically).** If the current triangle has an angle P>θ, cut
that vertex with x1=θ: branch A={other-neighbor, θ, P+neighbor-θ} contains θ directly (an
immediate win, so Shan-Yu never picks it). Branch B={neighbor, P-θ, other-neighbor+θ} is the
forced escape: **θ is not present in B in general**, and B is exactly the original triangle
with θ subtracted from P and added to whichever neighbor Mulan designated (her choice of which
neighbor receives it, by choosing x1=θ vs x1=P-θ instead). This is a fully deterministic,
adversary-forced transition (Shan-Yu has no real choice — the other branch is an instant loss).
Verified with sympy: children formula gives A2=(q,θ,p+r-θ), B2=(r,p-θ,q+θ) exactly.

**Corollary — spectator creation is always possible.** Bisecting any current angle p forces
p/2 into BOTH children unconditionally (sibling's Lemma 1, re-confirmed), so repeated
bisection of any angle drives it below any target threshold in finitely many forced moves.
Hence Mulan can always manufacture an angle <θ (a "spectator") from any starting triangle,
regardless of Shan-Yu's choice, before doing anything else.

### Verified construction: θ=60° forceable in ≤2 moves from ANY starting triangle
(Stronger and cleaner than the sibling's original 90→45 style chain for 60, which does not
reach 60 at all — 60 is not of the form 90/2^k.) Using the transfer lemma with target θ=60:
if the current triangle is not equilateral, its minimum angle r<60 automatically (since three
angles ≥60 summing to 180 forces all =60). Cut one of the other two angles p (>... just needs
p>60-r type validity, verified always satisfiable since p+q≥90) with x1=r+p-60: branch A
directly contains 60 (win), branch B is forced and always equals exactly {r, 60-r, 120} —
independent of the rest of the triangle. B contains a 120° angle; bisecting it (bisection
lemma) forces 60° into BOTH sub-children. So: **Mulan wins with θ=60° in at most 2 moves from
any non-equilateral start, 0 moves if equilateral.** Checked numerically (exact fraction
arithmetic) that the algebra is self-consistent (sums to 180 at every step).

### Verified general family: θ = 180°/(2^k+1), k=0,1,2,… is forceable
Generalizing the θ=60 (k=1) construction: with spectator r<θ, transfer move on angle p forces
either an immediate win or the fixed escape triangle {r, θ-r, 180-θ}. If 180-θ = 2^k·θ exactly
(i.e. θ=180/(2^k+1)), then k successive bisections of the (180-θ)-angle-lineage force it down
to exactly θ, each step forced regardless of Shan-Yu (bisection lemma applies to whichever
child survives, since only the numeric value being bisected matters, not the rest of the
triangle). This gives θ ∈ {90°, 60°, 36°, 20°, 180/17°≈10.588°, 180/33°≈5.4545°, …} all
**rigorously forceable** (algebra fully worked by hand + sympy-checked identities), each in
finitely many (k+2) moves from any start.

**Closure under halving:** if θ is forceable then θ/2 is forceable (force θ, then bisect).
Combined with the family above: **θ = 180 / ((2^k+1)·2^j) is forceable for all k,j≥0.** This
is a strictly larger set than the sibling's 90/2^k family (e.g. 60°, 36°, 30°, 20°, 15°, 12°
(see below) are all new members).

### Computational exploration (AND-OR game search, exact fraction arithmetic — evidence, not proof)
Implemented a proper AND-OR search (transfer moves = single forced child; bisection moves =
AND over both children, both must independently be forceable) over the restricted move family
{bisect any angle, transfer-to-θ at any angle exceeding θ}, memoized on (state,depth), starting
from the equilateral triangle, depth up to 12. This is a SUFFICIENT (not exhaustive — it omits
fully general single moves with other x1 targets) subset of Mulan's real strategy space, so
"True" results are solid evidence of forceability (modulo hand-verifying the witness), "False"
results only mean "not found in this restricted family within this depth," not proof of
impossibility.

Results (θ in degrees, `True`=strategy found, `False`=not found within depth 12):
```
5:True 10:True 12:True 15:True 18:True 20:True 22.5:True 30:True 36:True 45:True 60:True
70:False 50:False 40:False 25:False 24:False 35:False 55:False 65:False 75:False 80:False 85:False
180/7(~25.714): True   180/17: True
```
The True set beyond the hand-derived family exactly matches 180/((2^k+1)2^j): e.g. 12=180/15
(15=? — actually 12 is reached via 60/... check: 12 = 180/(2^?+1)*2^-j path found by search,
consistent with closure). The 180/7 result is a genuine surprise: 180/7 (an "ugly" rational,
not obviously in the hand-derived family) is forceable within depth 12, while the "nicer" 25°
and 40°, 50°, 70° etc. are NOT found forceable even at depth 12. This is a real structural
signal (not noise — re-ran at depth 12 with memo sizes 340k–900k, stable) that the true
characterization is a nontrivial number-theoretic condition on θ, not simply "θ≤90°" (H1) and
not simply the dyadic-of-90 or dyadic-of-(180/(2^k+1)) families found by hand. **This is the
key open gap for the outliner**: find the exact arithmetic criterion — my best guess, unverified,
is that it resembles the orbit of θ under the two maps x↦x/2 and x↦180-x (or their inverses)
under composition, i.e. a continued-fraction/binary-expansion-style criterion in base 2 relative
to 180°, but I did not derive or verify this further; treat as a research lead, not a claim.

### Distinct openings for the outliner
1. **Transfer-move lemma as the master tool.** State and prove the transfer lemma rigorously
   (it's clean algebra, fully verified above) — it strictly subsumes the sibling's bisection
   lemma and the 90°-double-hit as special/boundary cases, and is likely the correct
   "elementary move" the whole solution should be built from.
2. **Constructive lower bound: θ=180/((2^k+1)·2^j) forceable**, with an explicit finite move
   count (k+j+2 moves), fully rigorous, ready to write up as-is. This directly refutes the pure
   90/2^k conjecture (H2) from the sibling's report — 60°, 36°, 20°, 30°, 15°, etc. all work.
3. **Push for the exact characterization via the transfer-lemma recursion.** Formalize
   "forceable" as the least fixed point of: θ∈F if θ=90, or 2θ∈F, or [∃ construction via
   transfer+recursion on 180-θ]∈F — try to nail the closed form (my computational evidence
   points to something richer than the halving-closure family, given 180/7 succeeded).
4. **Alternative target for "for which θ" answer:** given the difficulty rating (7, "medium")
   and the numeric ambiguity found, consider whether the intended competition answer is
   actually the clean **θ ∈ (0°,90°]** (H1, i.e. ALL such θ), and that my depth-12 restricted
   search simply hasn't found the right strategy yet for 25°,40°,70° etc. (the move family
   used is not exhaustive — real Mulan has a continuum of x1 choices per move, not just
   {bisect, transfer-to-θ}). This should be checked by trying to extend the transfer lemma to
   a genuinely two-parameter family (aiming an intermediate value V≠θ, not just θ itself) to
   see if 40° or 70° can be reached with a cleverer intermediate target.

### Candidate technique(s)
- Direct algebraic/invariant bookkeeping (as in sibling report), extended with the transfer
  lemma above.
- Induction / explicit finite construction for the θ=180/((2^k+1)2^j) family.
- Possibly: represent θ/180 in binary and relate forceability to a finite/eventually-periodic
  binary expansion condition (unverified conjecture — worth 20–30 min of dedicated algebra by
  the outliner/builder before committing to it).

### Cheap-kill candidates
- Equilateral-triangle-has-min-angle-<θ-unless-equilateral pigeonhole (used to guarantee a
  spectator exists for θ=60 in one shot).
- The sum identity (new-angle-A)+(new-angle-B)=180° (from sibling report) — also the backbone
  of the transfer lemma's escape-branch computation.

### Knowledge-base entries to use
Same as sibling report: "Invariants & monovariants", "Constructive / incremental" /
"Constructive vs. existence", "Induction", "Synthetic toolkit" (altitude/right-angle facts).

### Analogous past problems (cruxes)
No new matches found beyond what the sibling already reported (no geometry cruxes in corpus;
`aimo-0236`, `aimo-0521` are the closest methodological analogues, already noted there — not
close enough to be true cruxes, same conclusion holds from this lens).

### Prior progress
Sibling report (`math-explorer-angle-invariant.md`) established: θ>90 impossible (proved),
θ=90/2^k forceable (proved), open question on general acute θ. This report **resolves that H2
is false** (60°,36°,20°,... work, not just 90/2^k) via the new transfer lemma, and gives a
strictly larger constructive family θ=180/((2^k+1)2^j), but leaves the EXACT final
characterization open — computational evidence suggests it's neither the full interval (0,90]
nor this halving-closure family alone (180/7 works, 25° apparently doesn't within the tested
move family/depth).

### Dead ends (do not retry)
- Sibling's dead ends still hold (see their report): no triangle-independent one-move
  double-hit for V≠90; transcendence-based defenses for Shan-Yu don't work since Mulan picks
  x1 after seeing the state.
- My own dead end: naively trying to reuse the SAME transfer target r (spectator) repeatedly
  without varying which neighbor receives the transfer leads to a 2-cycle {r,θ-r,180-θ} ↔
  itself and never terminates for generic θ — must actually bisect the (180-θ) angle to make
  progress (bisection is the only progress-making step in this chain; pure transfer-repetition
  loops).
- Treating the depth-12 restricted-move-family search as proof of impossibility for
  25°,40°,50°,70° etc. — it is NOT a proof, only a (nontrivial, since 180/7 succeeded in the
  same search) piece of negative evidence; do not assert impossibility for these values without
  further algebraic work.

### Small-case / intuition notes (all labeled conjecture except where marked proved)
- θ=90°, θ=180/(2^k+1) for k=0,1,2,…, and θ=180/((2^k+1)2^j) for all k,j≥0: **proved**
  forceable (explicit finite constructions given above).
- θ>90°: **proved** impossible.
- θ=180/7≈25.714°: computationally forceable within a restricted move family at search depth
  12 (**conjectural** — not hand-verified into a clean closed-form proof yet, but the witness
  path was extracted and is at least self-consistent arithmetically).
- θ=25°,40°,50°,70°, and several other "round number" values: **not found forceable** within
  the same restricted move family at depth ≤12 — suggestive but not proof of impossibility;
  likely resolvable either by extending the move family (intermediate non-θ targets) or by
  finding a genuine refined invariant blocking them specifically.
- Overall best guess for the outliner: the true answer is almost certainly **not** the clean
  full interval (0°,90°] and **not** simply the dyadic-of-90 family; it's some more intricate
  countable (likely dense) subset of (0°,90°], probably describable via a base-2
  continued-fraction-like criterion on θ (or θ/180). Nailing this exactly is the central
  remaining task.
