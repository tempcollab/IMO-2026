# Round 5 proof-reviewer report — imo-2026-02

## Verdict summary
- `synthetic-angle-chase-aklastar` — **APPROVE**. Status: **solved**. This is the FOURTH "solved"
  claim across this run's history for this problem, and the first that survives adversarial review.
- `coordinate-groebner-elimination` — **CHANGES REQUESTED**. Status: **partial** (self-report was
  accurate; not an overclaim this round).
- `inversion-at-a-collinearity` — **CHANGES REQUESTED**. Status: **partial** (self-report accurate;
  genuine new mechanism found, loop not closed).

`results/imo-2026-02/current.md` has been updated: `Status: solved`, with the complete `## Full proof`
and a `## Reviewer's independent verification` section documenting every check performed. Two new
lemmas certified: `lemmas/ray-betweenness-sign-lemma.md`, `lemmas/unsigned-angle-equals-abs-directed-angle.md`.

---

## 1. `synthetic-angle-chase-aklastar.md` — full adversarial re-derivation

Given this problem's history (three prior false "solved" claims, all caught by independent
re-derivation), I re-derived every load-bearing step from scratch rather than trusting the write-up.

### 1a. Lemma A (ray-betweenness sign lemma) — the new central claim
Re-derived the two-case ($\sigma=\pm1$) trigonometric argument by hand; it is correct and complete —
each case reduces to a clean chain of `sin`-sign-range implications with no gap. Independently
stress-tested with an *adversarial* numeric construction (not derived from the formula under test):
generated $(V,R,Q)$ at random, built $P$ via `atan2`-interpolation between the directions of $R,Q$ from
$V$, filtered to keep only $P$ that pass the lemma's hypotheses (a),(b) via direct same-side-of-line
tests, then checked the conclusion. **200,000 trials, 0 failures.**

### 1b. Applications at $B,C$ (Lemma A) and at $N,M$ (reused `interior-point-side-test.md`)
- Verified "K inside $\angle LBA$" and "L inside $\angle ACK$" are exactly the hypotheses the problem
  states (checked against the literal problem statement in `run_state.md`), and that the $(V,R,Q,P)$
  instantiations in Applications 1–2 correctly encode them.
- Recomputed the four base cross products with sympy from scratch:
  `cross(A-B,C-B) = -qa`, `cross(A-C,B-C) = qa`, `cross(C-N,B-N) = -qa/2`, `cross(B-M,C-M) = qa/2` —
  all match the file's claims exactly.
- Verified the "new edge" reuse of `interior-point-side-test.md` (edge $NC$ of $\triangle BNC$ off
  vertex $B$; edge $MB$ of $\triangle BMC$ off vertex $C$) is a *bona fide* application of the already-
  certified lemma (triangle $NCB=BNC$, $N,C$ on line $NC$, $B\notin$ line $NC$ since $B,N,C$ collinear
  would force $A,B,C$ collinear — correctly noted in the file), not a new unproven claim smuggled in.

### 1c. The dichotomy-mismatch flagged by `coordinate-groebner-elimination` this round
The sibling file raised a real, subtle point: $e_1=0$ splits as $\theta_1=\theta_2$ **or**
$\theta_1=\theta_2+\pi\pmod{2\pi}$, whereas the *unsigned*-angle hypothesis $|\theta_1|=|\theta_2|$
splits as $\theta_1=\theta_2$ **or** $\theta_1=-\theta_2$ — two genuinely different dichotomies, sharing
only the branch $\theta_1=\theta_2$. I checked whether `synthetic-angle-chase-aklastar.md`'s argument
is vulnerable to this. It is not: the file's own "Basic fact" section states the correct dichotomy
($\theta_1=\theta_2$ or $\theta_1=-\theta_2$, matching the unsigned-equality reading), and Step 7 does
not resolve it by picking a branch of $e_1=0$ — instead it proves $\theta_1,\theta_2$ are BOTH strictly
positive (in $(0,\pi)$) independently of hypothesis (ii), so $|\theta_1|=|\theta_2|$ collapses (trivially,
since a positive number equals its own absolute value) to the single real equality $\theta_1=\theta_2$.
Plugging this exact equality into the $\sin(\theta_1-\theta_2)$ formula for $e_1$ gives $e_1=0$
directly — no need to worry about which branch of $\{e_1=0\}$ is realized, since $\theta_1-\theta_2=0$
exactly (not just $\equiv0\pmod\pi$). This is the correct resolution of the ambiguity the sibling
flagged, and it is watertight.

### 1d. Cofactor identity (myexpr·Z = 2(q-T_K X)A_1 + 2(T_L X'-q)B_1) — full independent re-derivation
Re-built the entire coordinate chain from scratch in sympy (own script, not copied from any approach
file): parametrized $K,L$ exactly per $(\ast)$, computed $e_1,e_2$ from their raw cross/dot
definitions, confirmed $T_K \mid e_1$ and $T_L\mid e_2$ exactly (zero remainder polynomial division),
confirmed $A_1:=e_1/T_K$ and $B_1:=e_2/T_L$ match the file's displayed quadratic-in-$T_L$/$T_K$ forms
modulo $c^2+s^2-1$ (checked at an exact Pythagorean-pair point, zero residual), and confirmed the full
identity $\mathrm{myexpr}\cdot Z=2(q-T_KX)A_1+2(T_LX'-q)B_1$ both (i) at 3 independent exact rational
Pythagorean-pair points (zero residual) and (ii) as a full polynomial identity by symbolic reduction of
$s^2\to1-c^2$ down to literally `0` (not just `simplify`-zero, exact cancellation). **Note:** my first
attempt at this check produced a large nonzero "diff" — traced to my own transcription bug (dividing by
an extra spurious factor of `(a-p)^2+q^2` a second time); once corrected the identity is exact. This is
recorded here as a caution for future rounds: always re-verify a "failed" independent check for one's
own bug before concluding the source proof is wrong.

### 1e. $Z>0$
Re-verified $K_y=T_K\cdot X$ algebraically (expansion of $R(-\alpha)(p,q)$'s $y$-component), and
$K_y=\mu q/2>0$ from the barycentric-interior argument (re-derived independently, matches). Combined
with $\sin\alpha>0$ (re-derived independently via the "$K\notin$ line $AB$" argument), $Z=aX+s(p^2+q^2)$
is manifestly a sum of two strictly positive terms.

### 1f. End-to-end numeric stress test (adversarial, not the builder's own checks)
Constructed genuinely valid configurations by *solving* the actual quadratic systems
$g_1(\alpha,p,q,a;T_L)=0$, $g_2(\alpha,p,q,a;T_K)=0$ for random $(p,q,a,\alpha)$, taking all root
combinations, and filtering by directly testing **all** five position/interiority hypotheses via raw
coordinate geometry (barycentric-positivity + same-side-of-line tests) — not assuming any of the
proof's machinery. Found **340 valid configurations** spanning $\alpha\in(0.007,1.32)$ rad — a much
broader spread than the previously-flagged 5-sample check (all sharing $\alpha=0.05$). In every single
case: all four Step-7 sign predictions (S1)–(S4) held exactly as claimed, and $OM=ON$ held to
floating-point precision (one example verified to 12 significant digits). Zero failures across all 340
cases plus the 200,000-trial Lemma-A-only sweep.

### 1g. Verdict
Every load-bearing step re-derived independently and found correct: the circumcenter reduction, the
rotation-sign convention, $\sin\alpha>0$, the cofactor identity, $Z>0$, and — the genuinely new part
this round — the branch-selection closure via Lemma A + the two new applications of
`interior-point-side-test.md`. No hand-waving, no skipped cases, no unjustified division (the one
division, by $Z$, is justified by $Z>0$ proven unconditionally). **Status: solved. APPROVE.**

---

## 2. `coordinate-groebner-elimination.md`

Self-reported `partial`, and this is accurate — not a fourth overclaim. This round it:
- Correctly re-derived the same cofactor identity and $Z>0$ argument as the sibling (own notation).
- Found and proved (from scratch, independently) essentially the same Ray-Betweenness Lemma as the
  sibling's Lemma A, and used it to establish $\sin\theta_1>0,\sin\theta_1'>0$ (the vertex-$B$/$C$
  halves).
- Explicitly and honestly flagged that the vertex-$N$/vertex-$M$ halves (needed to pin
  $\theta_2,\theta_2'$ into $(0,\pi)$ too) are **not** closed in this file — this is exactly the piece
  the sibling closed via reusing `interior-point-side-test.md` on new edges, a step this file does not
  contain.

This is real, correctly-scoped progress; the file's own honesty about the residual gap is a point in
its favor given this problem's history of overclaiming. Verdict: **CHANGES REQUESTED** — the gap is
now closed (fully) by the sibling; this file should adopt the same closing mechanism (or a citation +
adaptation of the certified `ray-betweenness-sign-lemma.md` plus its own equivalent of the two new
`interior-point-side-test.md` applications) if the population wants a second independent solved proof.
Since the problem is already solved via the sibling, this is now optional/lower priority.

---

## 3. `inversion-at-a-collinearity.md`

Self-reported `partial`, accurate. Genuine new contribution this round: Lemma 4 (a cross-ratio-based
"vertex-swap angle-to-concyclicity" fact, needing no inversion center) that resolves the round-4
diagnosis that hypotheses (ii),(iii) were "invisible" to the single-inversion-center mechanism (Lemma
2). Lemma 4's proof (via the same cross-ratio-realness fact as Lemma 3) is short and I checked it is
correct — it reduces to `(X,W;P,Q)` being a real cross ratio, standard. However, the resulting system
(three concyclic-quadruple facts sharing points $K$ or $L$ pairwise, plus the branch-selection question
inherited from the rest of the population) is not chased to a closed loop; the file honestly says so.
This remains a genuinely different framing (no dependence on the coordinate route's algebra), valuable
as population diversity/insurance even though the problem is now solved via the sibling. Verdict:
**CHANGES REQUESTED** (real, incomplete progress; not structurally dead — Lemma 4 is a legitimately
new, reusable tool).

---

## Certified lemmas this round
- `lemmas/ray-betweenness-sign-lemma.md` (new) — certified, full proof + independent 200k-trial
  numeric stress test.
- `lemmas/unsigned-angle-equals-abs-directed-angle.md` (new) — certified, trivial but load-bearing,
  fully proved.

## `current.md`
Updated: `## Status` = `solved`, `## Full proof` written in full (self-contained restatement of the
chain, cross-referencing certified lemmas), plus a `## Reviewer's independent verification` section
documenting every check performed above so future rounds/agents can audit without repeating the full
derivation.

## Note for future rounds
This is a genuine solve, not a provisional one — but given this problem's specific track record (3
prior false positives), if any future agent revisits this file, the load-bearing steps to re-check
first are (in order of subtlety): (1) the branch-selection closure (Step 7 / Lemma A), (2) the cofactor
identity, (3) the rotation-sign convention. All three were independently re-derived this round from the
raw definitions, not merely re-read.
