# Proof-reviewer report — imo-2026-03, round 1

Problem: IMO 2026 P3 (Chu–Han war). Determine largest c Liu can guarantee. Answer type:
expression in n. Claimed answer **c(n) = 2^n/(2^{n+1}−1)**.

## Independent verification (reviewer, done from scratch)

- **Answer is correct.** Brute-forced the full two-stage minimax of D on a discretized grid:
  minimax D = u_n = 1/(2^{n+1}−1) for n = 0,1,2 (0.333, 0.1429 exact). With Lemma R this gives
  c(n) = (1+u_n)/2 = 2^n/(2^{n+1}−1). Confirmed.
- **Lemma R (reduction, greedy claiming = odd-rank sum):** re-derived the recursion
  V(S) = Σ(S) − min_j V(S∖{b_j}) and the componentwise-domination argument; verified
  numerically (2000 random multisets: game value = odd-rank sum). CORRECT.
- **Lemma M/I (D = measure{N(t) odd}):** verified numerically (2000 tests). CORRECT.
- **Lemma P (cancelling pair, D(S∪{v,v})=D(S)) / toggle calculus:** verified numerically
  (2000 tests). CORRECT.
- **Peel arithmetic (6.1):** confirmed 1 − u_n/u_{n-1} = c(n) = 2^n/(2^{n+1}−1) symbolically
  for n=1..5. CORRECT.

All load-bearing lemmas shared by both approaches are sound. Neither approach overclaims —
both are honestly marked `partial` with precisely-stated gaps, and the recorded Status matches
reality.

---

## Approach 1: parity-measure-potential — CHANGES REQUESTED (Status: partial)

Scores: Correctness 10/10 (everything written is valid) · Rigor 6/10 (two real gaps, honestly
flagged) · Progress: substantial (foundational reduction + lower Case A + upper reduction with
a documented negative result).

What is genuinely proven and rigorous:
- Lemmas R, I, T — full, correct (verified independently).
- Lower bound Case A (Xiang leaves top piece uncut ⇒ D ≥ u): correct. Minor wording slip at
  n=1 ("≥2 other pieces … each strictly < 2^n−1") — for n=1 there is one other piece equal to
  2^n−1, but the conclusion N(t)=1 on [2^n−1,2^n) still holds since t ≥ 2^n−1 means that piece
  is not exceeded. Not fatal.
- Upper bound: the greedy-match analysis is fully carried out AND honestly reports greedy is
  insufficient for n ≥ 3 (worst-case D > u, computationally). This is a valuable documented
  dead-end, correctly isolating the difficulty to the all-strict, full-budget case m=n+1.

Precise remaining gaps (both KEY, honestly stated, not overclaimed):
- **GAP B2 (lower, top-piece cut):** for dyadic pieces 1,2,…,2^n, show D ≥ 1 when Xiang cuts
  the top piece P=2^n. Fragments of P (mass 2^n) dominate and perturb the sub-config 1,…,2^{n−1}
  in the global sort; residual is not a clean order-(n−1) instance.
- **GAP B3 (upper):** an adaptive Xiang strategy forcing D ≤ u for every Liu multiset; greedy
  proven insufficient, so the strategy must adapt to piece ratios.

Verdict: **CHANGES REQUESTED.** Real, verified progress; two coupling gaps remain.

---

## Approach 2: induction-peel — CHANGES REQUESTED (Status: partial)

Scores: Correctness 10/10 · Rigor 6/10 (two real gaps, honestly flagged) · Progress:
substantial (foundational reduction via cleaner Lemma-P engine + full base cases + peel
arithmetic proven tight on dyadic input).

What is genuinely proven and rigorous:
- Lemmas R, M, P — full, correct (verified). Lemma P (cancelling pair) is a clean, powerful
  engine.
- Recursion u_n = u_{n-1}/(2+u_{n-1}) and closed form; base cases n=0,1 fully solved both
  directions (checked).
- Lower Case (a) (top piece uncut ⇒ D ≥ u_n L): correct.
- Upper peel arithmetic (6.1) and its tight closure on the dyadic extremal input: correct
  (verified symbolically). This proves the answer is tight for the extremal configuration.

Precise remaining gaps (honestly stated):
- **GAP L (lower, top-piece cut):** same coupling as B2 above — top-piece fragments vs. tail
  in the global sort; symmetric-difference bound alone gives only D ≥ u_nL − |{N_P odd}| which
  is vacuous.
- **GAP U (upper):** the single-cancelling-pair peel closes only when max(a_1, 2a_2) ≥ L·c(n);
  it stalls otherwise (explicit example (0.5,0.28,0.22) at n=2). Needs a stronger peel or a
  profile-tracking induction, not just top-two ranks.

Verdict: **CHANGES REQUESTED.** Real, verified progress; two coupling gaps remain.

---

## Cross-cutting note for next round

Both approaches, despite different framings (global measure vs. strong induction), have
collapsed onto the SAME two obstructions: (i) lower bound when the top piece is cut, (ii)
upper bound for non-extremal Liu partitions where a single pair-peel is too weak. These are
genuinely the crux of the problem. The two upper-bound framings differ (greedy-match vs.
cancelling-pair peel) but hit walls one step apart. Next round should consider a third framing
for at least the upper bound (e.g. a potential/weighting argument on the measure, or an
LP/duality view of the minimax), and for the lower bound an argument that tracks the migration
of the tail's protected all-odd intervals under a top-piece cut.

## Certified shared lemmas (admitted to lemmas/)
- `lemmas/reduction-odd-rank.md` (Lemma R)
- `lemmas/measure-identity.md` (Lemma M/I + toggle calculus)
- `lemmas/cancelling-pair.md` (Lemma P)
All three: sorry-free, statements correct and no stronger than proved, verified numerically.

## Overall
Status (current.md): **partial**. Answer c(n)=2^n/(2^{n+1}−1) confirmed correct; full
foundational reduction certified; both bounds reduced to two precisely-stated coupling gaps.
Neither approach is solved.
