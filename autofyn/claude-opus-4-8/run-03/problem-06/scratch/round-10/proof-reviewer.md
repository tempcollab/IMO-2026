# Proof-reviewer — Round 10 (imo-2026-06, IMO 2026 P6)

## 1. smallest-essential-prime-descent — VERDICT: APPROVE (Status: solved)

Builder claimed **solved**. I independently re-derived every load-bearing step from scratch and verified
numerically. **The claim is correct: this is a complete, rigorous proof of IMO 2026 P6.** First solve after
10 rounds on the shared wall.

Scores — Correctness 10/10, Completeness/rigor 10/10, Progress: decisive (unsolved→solved).

### Why it works (the framing that dissolves the 10-round wall)
The whole population had been stuck proving "no prime > P_max (largest prime factor of a_1) is ever
load-bearing." This approach **does not need that statement.** It uses the cruder notion **small prime :=
prime ≤ a_1** (a larger set than {p ≤ P_max}), and proves the stronger, cleaner fact **"similar numbers
(same primes ≤ a_1) have the same good/bad status"** directly, via the aimo-0030 game calculus. The
periodicity modulus is M = ∏_{p≤a_1} p — a valid (non-minimal) period; the theorem only needs *some*
period, so the sharper L_0 = ∏_{p≤P_max} p target was never necessary. This is a genuinely different
framing, exactly the diversity mandate the run kept calling for.

### Step-by-step verification (all re-derived independently)
- **ENUM / PER imports**: re-derived ENUM myself (m∈E_∞∩[a_1,∞) ⟹ m is a term: if a_n<m<a_{n+1}, m
  satisfies the constraint defining a_{n+1}, forcing a_{n+1}≤m, contradiction). Correct, certified.
- **F1 (recursive characterization)** — the load-bearing bridge. (⟸) is the crux: goods <m are {a_1..a_j},
  hypothesis gives gcd(m,a_l)>1 ∀l≤j, the greedy rule forces a_{j+1}≤m, maximality forces a_{j+1}=m. Airtight,
  non-circular (uses only the greedy definition + ENUM). Verified numerically (0 violations, a_1∈{15,35,99,231}).
- **F2, F3** trivial and correct.
- **Claim 1 / Claim 2 / Claim 3**: each re-derived. Claim 3's minimal-counterexample descent is the delicate
  one — I checked: p∣x forced; y=1 eliminated via move x→a_1; y≥2 gives α with y^{α-1}<a_1; the descent
  inequality **p^{r-1}y^α < p^r y = x < n** genuinely holds (uses a_1≤p and x<n); the induction j=0..r stays
  ≥a_1 and <n so minimality applies; final contradiction via Claim 1 on x∣p^r y^α. Valid infinite descent,
  no circularity. Verified numerically (0 violations, all seeds, N up to 6000).
- **Main claim / (★)**: minimal-pair descent d_0→d_0/p, split p≤a_1 (Claim 2 contrapositive, needs p²∣d_0 —
  correctly established from similarity) and p>a_1 (Claim 3). Both branches force d_0/p good, contradicting
  minimality. Correct. Verified numerically: **0 mixed-status similarity groups** for a_1∈{15,16,17,30,35,45,
  99,100,210,231}.
- **Conclusion**: n,n+M similar ⟹ same status ⟹ E_∞ tail-periodic mod M ⟹ ENUM+PER give the theorem with
  explicit T,L=M>0. Matches the exact problem statement (a_{n+T}=a_n+L for every n≥1).

No hidden gaps, no skipped cases, no crux-move reference (F1/F2/F3 are proved here from the greedy
definition; the aimo-0030 game is only motivation). The recorded Status `solved` is correct.

**Action taken**: wrote `current.md` Status=solved + Full proof; certified terminal lemma
`lemmas/recursive-good-bad-and-similarity-closure.md` (F1 + Claims 1–3 + Main claim). Recorded
`verified-milestone`.

## 2. covering-small-part-descent — VERDICT: CHANGES REQUESTED (Status: partial)

Builder claimed **partial** — honest and correct. Lemma 15 (Hub abundance under ¬(FIN-Q)) is genuinely
**gap-free**: (a) transversal D=Q(m_1) from (★) at one hub; (b) H infinite by CRT (gcd(L_0,∏D)=1) + (★);
(c) residue-locality of S gives every hub a bad term. I verified each part against the certified (★)
dichotomy — correct. The self-diagnosis that the iterated hub-value walk cannot descend (Obstruction 1: a
single finite transversal already yields all hubs, so ¬(FIN-Q) exerts no overflow pressure; Obstruction 2:
every value-shed changes m mod L_0, orthogonal to the ≤L_0-node pigeonhole; min H_r is a class-function) is
correct — this is a legitimate structural pinning, not hand-waving.

Scores — Correctness 10/10, Completeness/rigor: partial by construction (crux EC/CSP open), Progress:
modest (one new gap-free lemma + correct stall diagnosis). Its recorded Status `partial` is accurate.

**However it is now moot**: the sibling approach solved the whole problem this round, so this lane's
residual gap no longer needs closing. Certified Lemma 15 into
`lemmas/hub-abundance-under-not-finq.md`. Recorded `advanced` (superseded).

## Lemmas certified this round
- `lemmas/recursive-good-bad-and-similarity-closure.md` (F1 + F2/F3 + Claims 1–3 + Main claim = terminal,
  solves P6) — from smallest-essential-prime-descent.
- `lemmas/hub-abundance-under-not-finq.md` (Lemma 15) — from covering-small-part-descent.
(Lemmas 10/12/13/14 of covering-small-part-descent were already certified in prior rounds; not re-certified.)

## Bottom line
IMO 2026 P6 is **SOLVED**. `current.md` updated to Status=solved with the full proof.
