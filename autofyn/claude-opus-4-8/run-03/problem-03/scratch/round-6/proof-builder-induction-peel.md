# Build report — induction-peel (imo-2026-03), round 6

Focus: LOWER wall. Assigned: close (L⋆) `D(S')≤f₁−1` (all pieces ≤2^{n-1}) and GAP L2 (Case II,
top shredded into all-≤2^{n-1} fragments, `D≥1`) via the PEEL/SPLIT machinery + exchange/interleaving.

## Status: PARTIAL. Lower bound reduced to a SINGLE exchange step; two new sub-cases closed rigorously.

## What I closed this round (rigorous, no gaps)

1. **Band decomposition (3.1)** — new Lemma BAND:
   `D(S) = (g₀−2^{n-1})⁺ + μ((O_F △ O_T) ∩ [0,2^{n-1}))`, where `S=F⊔T` (top fragments ⊔ tail
   refinement of C_{n-1}). Proved from Lemma M + Lemma SPLIT: on the top band [2^{n-1},2^n) at
   most one fragment exceeds t (two would sum >2^n), so the odd-set there is exactly {t: g₀>t}.
   This makes PEEL transparent and unifies Cases (I)/(II). Recovers `D(S)=f₁−D(S')` in Case I.

2. **Trivial regime of (L⋆) — CLOSED in one line.** For `w = 2^n−f₁ ≤ 2^{n-1}−1`:
   `D(S') ≤ max(S') ≤ 2^{n-1} ≤ 2^n−1−w = f₁−1` (Lemma M gives D ≤ support length; Lemma ONE gives
   every S'-piece ≤ 2^{n-1}). This leaves ONLY the width-one **critical band**
   `w ∈ (2^{n-1}−1, 2^{n-1})`, i.e. `f₁ ∈ (2^{n-1}, 2^{n-1}+1)`. (Kept the two-subcase split as the
   reviewer required — a uniform bound is impossible, margin →0 at w↑2^{n-1}.)

3. **Case (II) sub-case |F|=2 — CLOSED via IH** — new Lemma HALF. Two top-fragments ≤2^{n-1}
   summing to 2^n force `F={2^{n-1},2^{n-1}}`; then `N_S = N_T + 2·1[t<2^{n-1}]` has the same
   parity as N_T everywhere, so `D(S)=D(T)`, and `D(T)≥1` by the induction hypothesis LB(n−1)
   (T refines C_{n-1} with ≤n−1 cuts). Verified `D(S)=D(T)` and `D(T)≥1` on 80k random tails, n≤5.

4. **Exact extremal telescoping — PROVED IDENTITY (both walls).** Below-insertion (one fragment
   per gap, uncut tail) gives `D(S')=Σt_i−Σg_k=(2^n−1)−w=f₁−1` exactly; above-insertion gives
   `D=1` exactly. So BOTH bounds are attained/tight — this confirms the answer is exact on the
   extremal configuration and pins the extremiser.

## What remains open — GAP L2 (one step, both walls)

The **exchange step** of the Gap-Interleaving Lemma: prove the canonical one-per-gap layout is the
extremiser (so any config has D(S')≤f₁−1 / D(S)≥1). Mechanism identified (adjacent-pair exchange
against the neighbouring tail value, confined toggle set by Lemma M/T, gap-occupancy vector as a
lex monovariant for termination) but NOT written as a rigorous per-move inequality. The naive
per-cut `|ΔD|≤2s₂` bound is too loose (doesn't see the cut budget). This single step closes BOTH
the critical band of (L⋆) AND the |F|≥3 sub-case of Case (II). Same object as
parity-measure-potential's GAP L2 and breakpoint-vertex's finitised residual.

Key finding (spec-relevant): the unlimited-cut versions of both bounds are FALSE (numerically
refuted, n=2..4) — the cut budget ≤n is essential and the exchange must respect it. So no
cut-free/mass-only argument can work here (consistent with the certified whole-tail-peel's negative
companion). The extremiser uses ALL n cuts (one fragment per gap), confirming the round-4
correction that "WLOG single top cut" is false.

## Promotable lemmas (proposed for certification)
- **Lemma BAND** (top-band decomposition) — §3, from M+SPLIT.
- **Lemma HALF** (bisected top: `D({2^{n-1},2^{n-1}}⊔T)=D(T)`) — §3.2, from M.

## Spec concerns
None new. The answer c(n)=2^n/(2^{n+1}−1), minimax D=u_n stands; the extremal telescoping this
round re-confirms tightness. Upper bound GAP U (balanced a₁<L/2) unchanged and out of my lane.
