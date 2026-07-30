# Proof review — imo-2026-04 (Mulan's Triangle Game), round 2

Reviewed two built approaches adversarially: independently re-derived every claimed
identity by hand, and independently re-implemented and simulated both the forward
algorithm and Lemma A in fresh Python scripts (not the builders' scripts) to cross-check.

## 1. `results/imo-2026-04/approaches/chip-double-force.md`

**Claimed Status:** solved. **Verdict: APPROVE. True Status: solved.**

### Master cut formula
Re-derived from scratch (triangle angle sum + straight-line supplementary angle at P):
for a triangle (a,b,c) at (A,B,C), cutting vertex A at x=∠BAP∈(0,a) gives
Child₁=(b,x,a+c-x), Child₂=(c,a-x,b+x). Matches the proof exactly. Correct.

### Forward direction (M1/M2 state machine)
Checked every algebraic substitution:
- **M1**: with a=T,b=G,c=S, x=θ, Discard=(G,θ,T+S-θ) (always contains θ, since the "x" slot
  is literally θ by construction — trivially true for every T,S,G), Keep=(S,T-θ,G+θ).
  Verified the two sub-cases (T≠2θ safe; T=2θ terminal) algebraically — correct.
- **M2**: the inequality argument "not both u,w ≥ (n-1)θ" checked (2(n-1)θ≤u+w<nθ ⟹ n<2,
  contradiction) — correct, and the "≥" boundary case is also correctly excluded by the
  same strict contradiction. Child_A=(t,θ-t,(n-1)θ), Child_B=(keep-small,s-θ+t,θ) — verified
  by direct substitution into the master formula (a=s,b=t,c=keep-small,x=θ-t); matches.
  n=2 vs n≥3 branching correct.
- **Termination.** I checked the subtle point myself: can "Target" (which decreases by
  exactly θ each M1 step) ever land exactly on θ without being caught by the T=2θ terminal
  check? No — Target_{k+1}=θ implies Target_k=2θ, which is caught as terminal *before* the
  subtraction step is taken, so a continuing (non-terminal) Target trajectory never equals
  θ. This closes exactly the loophole the round-1 outline-reviewer flagged ("naive iteration
  can loop"); the proof's own justification for this is correct, if slightly terse.
  Shield/Growing safety (Shield fixed and ≠θ from the moment of designation; Growing
  strictly increasing from a value that starts either >θ or in (0,θ), hence never lands
  exactly on θ) — checked and correct in every branch (case-3 direct designation,
  M2-hand-off designation).
- **Reachability of all cases for small n.** Verified by hand: n=2 forces case-3 (all
  angles >θ) to be vacuous (a triangle can have at most one angle ≥90°=θ when n=2, so at
  least two angles are always <θ, guaranteeing step 2 always fires) — consistent, no gap.
  Worked a concrete example by hand (θ=60°, n=3, triangle (100,50,30)): M2 → (30,30,120),
  Shan-Yu forced (Child_B=(50,70,60) contains θ); then M1 with Target=120=2θ is immediately
  terminal (both branches contain θ) — matches the algorithm's own n=3 prediction (n-3=0
  extra M1 steps, then terminal), exactly 2 total moves.
- **Independent re-simulation.** I reimplemented the algorithm literally (not the builder's
  script) in `/tmp/verify.py` and ran it over n=2..19, 200 random triangles per n (3600
  trials): **0 failures**, every trial ends in a Mulan win, every internal assertion
  (Discard-branch always θ; Keep/Child_A branch never θ except at designed terminal steps;
  Target never silently hits θ) held throughout.
- **Minor style note (not a rigor violation).** The phrase "any rational player avoids an
  immediate loss when a safe alternative exists" is informal. The actual logical content
  needed — and which the proof, on inspection, *does* fully supply — is: for *every* choice
  Shan-Yu makes (not just a "rational" one), Mulan eventually wins: picking the θ-branch
  ends the game immediately in her favor, picking the safe branch continues the (terminating)
  induction. Both cases are in fact covered; I recommend the next write-up state this
  explicitly ("regardless of which child Shan-Yu keeps...") rather than invoking rationality,
  but this is a clarity improvement, not a mathematical gap — I verified the underlying claim
  is true by inspecting both branches at every step type (M1 non-terminal, M1 terminal, M2
  non-terminal, M2 terminal).

### Converse direction (residue-mod-θ clean invariant)
- **Lemma A.** Re-derived the 4-case exhaustive check from scratch using the homomorphism
  g(α)=(α/θ) mod 1. All four cases (0=g(p), g(q)=0, g(r)=0, g(p)+g(q)+g(r)=0⟺ρ∈ℤ) are
  correctly shown impossible under the stated hypotheses. This is genuinely exhaustive: the
  "unclean" condition for each child is disjunctively `x∈{...}` over exactly two elements
  each (from the two new angles per child), so "both unclean" is exactly the 2×2=4-case
  intersection enumerated — no case is missing.
  **Independent numerical re-check** (`/tmp/verify2.py`, 300,000 random trials, distinct
  seed/script from the builder's): 0 counterexamples.
- **Lemma B (clean starting triangle).** Verified a₀:=θ/√2 is valid for the *entire* range
  0°<θ<180° (since 1/√2<1, a₀<θ<180 always) — correct, including boundary behavior as θ→0°
  (a₀→0, still positive) and θ→180° (a₀→127.28°, still <180°). The interval I and countable
  exclusion set F are correctly constructed (I uncountable, F=ℚ∪{countably many points}
  countable, so I∖F≠∅); the algebra deriving c₀'s non-resonance condition
  (t=ρ-1/√2-k ⟺ c₀=kθ) is correct on direct substitution.
- **"θ itself is 1×θ" / n=1 exclusion.** Explicitly checked: the proof defines θ-resonant as
  g(α)=0 i.e. α is *any* integer multiple of θ, and explicitly notes "θ itself is
  θ-resonant (=1·θ)" — so a clean triangle by definition never has an angle equal to θ. This
  is correctly and explicitly handled, not an accidental omission.
- **Boundary self-consistency at θ=90° (n=2).** Forward gives a genuine 1-move win (verified
  above); converse's Lemma A case-4 exclusion (g(p)+g(q)+g(r)=ρ mod 1=0 ⟺ ρ∈ℤ) is exactly
  the condition that fails at ρ=2 — so Lemma A correctly does *not* apply there, and there is
  no contradiction between the two directions. Confirmed by direct computation.

### Answer verification (compute_and_prove/characterization requirement)
The answer θ=180°/n (integer n≥2) is stated explicitly, and both directions are proved as
complete, from-scratch arguments — the strongest possible verification. The boundary case
θ=90° is additionally spot-checked on both sides. This satisfies CLAUDE.md's requirement.

### Verdict
No fatal gaps found after adversarial, independent re-derivation of every load-bearing
identity (master formula, M1, M2, the 4-step algorithm's termination argument, Lemma A's
4-case check, Lemma B's construction) and independent computational re-verification (3600
forward-algorithm trials, 300,000 Lemma-A trials, both 0 failures). **This is a complete,
rigorous proof of both directions. Status: solved. Verdict: APPROVE.**
`current.md` has been rewritten with the certified Status and Full proof.

## 2. `results/imo-2026-04/approaches/budget-partition-dimension.md`

**Claimed Status:** partial. **Verdict: CHANGES REQUESTED. True Status: partial (confirmed,
with an additional bug found in its own claimed-complete converse).**

- Its Lemma A (residue one-move safety) is essentially identical to chip-double-force's, and
  checked correct by the same independent re-derivation/re-simulation above.
- **Bug found: Lemma B is broken as stated.** The proof sets a₀:=√2·θ and asserts "Since
  0<θ<180, a₀<180" — this does **not** follow (√2·θ>θ, not <θ), and is false in general: for
  θ ≥ 180/√2 ≈ 127.28°, a₀=√2θ ≥ 180°, which is not a valid triangle angle (I verified this
  numerically: θ=128°→a₀≈181.0°; θ=150°→a₀≈212.1°; θ=170°→a₀≈240.4°; θ=179°→a₀≈253.1°). This
  means the explicit clean-triangle construction fails to produce a valid triangle for
  roughly the top quarter of the θ-range (≈127.28° to 180°), so **this file's own converse
  proof is not actually complete for all θ as claimed**, even though its Lemma A is correct
  and its overall *mechanism* is sound (the sibling file's corrected constant a₀:=θ/√2 fixes
  this and is what should be cited/promoted instead).
- Forward direction is intentionally not present (cites sibling by design, per the
  outline-reviewer's round-2 directive) — this is fine and consistent with the file's own
  stated `partial` status, but note the "complete, self-contained, rigorous proof" framing of
  its converse section is overclaimed given the Lemma B bug above.
- **Verdict: CHANGES REQUESTED** — real, independently-verified progress (Lemma A is a
  correct and reusable central lemma — already certified into `lemmas/residue-clean-invariant.md`
  in the *corrected* form), but the gap to close (for this file specifically) is: replace
  a₀:=√2·θ with a₀:=θ/√2 in its own Lemma B (or simply cite the corrected lemma from the
  sibling / the certified lemma file instead of re-deriving it with the wrong constant).
  Its Status remains `partial` (matches the file's own self-assessment, for a different but
  related reason than what it stated).

## Promotable lemmas — certification results

Certified into `results/imo-2026-04/lemmas/` (all held to full rigor bar, re-derived/
re-verified independently by the reviewer, no `sorry`/gaps):
- `master-cut-formula.md` — certified.
- `general-chip-move.md` (M1) — certified.
- `compensation-move.md` (M2) — certified.
- `forward-direction-theorem.md` — certified.
- `residue-clean-invariant.md` (Lemma A + Lemma B) — certified **with the corrected
  constant a₀:=θ/√2** (chip-double-force's version); explicitly flags and rejects
  budget-partition-dimension's a₀:=√2·θ version as buggy.
- `theta-gt-90-invariant.md` — certified as an independent special-case cross-check.

No lemma was rejected outright; one lemma (Lemma B) required using the corrected constant
from chip-double-force.md rather than budget-partition-dimension.md's version, which is
noted explicitly in the certified file so no future approach re-imports the broken constant.

## `results/imo-2026-04/current.md`

Rewritten by the reviewer (owner of this file) with:
- `## Status`: solved
- `## Full proof`: the complete, self-contained assembled proof (master formula, forward
  algorithm M1/M2, converse Lemma A/B with the corrected a₀, boundary check at θ=90°, answer
  verification), consolidated from chip-double-force.md and cross-checked against my own
  independent derivations/simulations above.

## Summary

- `chip-double-force.md`: **APPROVE**, Status **solved**. This closes the run's goal
  (problem imo-2026-04 is now solved and certified).
- `budget-partition-dimension.md`: **CHANGES REQUESTED**, Status **partial** (Lemma A
  correct and now certified/promoted in corrected form; its own Lemma B has a genuine
  algebra bug for θ≳127.28° that should be fixed by swapping in θ/√2).
