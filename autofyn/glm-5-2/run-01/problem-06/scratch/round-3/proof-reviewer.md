# Proof review — IMO 2026 P6 (`imo-2026-06`), round 3

Reviewed two built approaches: `w-descent-rsmooth` (claims SOLVED) and `b2-induction-step` (claims B2-given-B1'). Read CLAUDE.md (rigor rules), current.md (certified conditional spine, refuted (Cov) window, B2≠corollary), outline-reviewer gate, both approach files, the new lemma `a1-on-cycle.md`, all imported certified lemmas, and the exact problem statement. Verified all load-bearing claims computationally (python3/sympy). Findings below.

## Headline

**Neither slug is SOLVED.** Both have real gaps. The `w-descent-rsmooth` builder marked its approach `solved`; I downgrade it to `partial` — Lemma 2 (s-substitution) contains a false claim (`n ≥ 1 ⟹ b has a big prime`) that breaks the bound `x ≤ b` in a load-bearing sub-case, leaving the similarity theorem's descent unjustified when `r` is `k`-smooth with `a = rad(small part) < k`. The `b2-induction-step` path-β CRT-density escape is logically sound, but it imports the CERTIFIED `sigma-periodicity` lemma whose `T'` formula is BUGGY (verified `a_1=35, p=17`: period 578, lemma's `lcm(34,17)=34` is not a period); with the corrected formula path β survives.

A **third** bug was found in a previously-certified lemma (`sigma-periodicity`): the `T'` formula drops a factor of `p` whenever a prime `p ≤ R` divides `T` but not `L`. Corrected formula: `T' = T · ∏{p ≤ R, p ∤ L, p prime}` (equivalently `lcm(T, {p·T : p ∤ L})`), NOT `lcm(T, {p ∤ L})`.

---

## SLUG 1: `w-descent-rsmooth` — CHANGES REQUESTED (Status: partial)

The builder marked Status `solved`. **This is wrong — downgrade to `partial`.** The strategy (characterization + s-substitution + minimal-counterexample similarity + CRT periodicity + Theorem 1) is sound and the key theorems are computationally verified, but Lemma 2's proof has a real gap.

### What is CORRECT (verified)

1. **Lemma 1 (characterization `G = H`).** `n ≥ k ∈ G ⟺ n` is coprime to none of the smaller `G`-elements. I re-derived the proof independently and verified computationally (9 values of `a_1` ∈ {6,15,35,77,91,105,135,175,385}, full greedy coverage of [a_1, 350]): **0 mismatches**. The `H ⊆ G` direction (the load-bearing one) is clean: `g_r = a_r` (the r-th greedy element, since `G` is strictly increasing) IS the largest `G`-element below `n`, so the `r` past terms `a_1,…,a_r` are exactly the `G`-elements below `n`; `n ∈ H` ⟹ `n` admissible at step `r` ⟹ `a_{r+1} ≤ n` ⟹ contradiction with maximality of `g_r` unless `n ∈ G`. Valid.
2. **Cor 1.1, Cor 1.2.** Follow cleanly from Lemma 1. Valid.
3. **Similarity theorem (statement).** Computationally verified: 9 values of `a_1`, range [a_1, 350/600] with full greedy coverage: **0 violations** (no two similar integers ≥ a_1 have different G-status). The THEOREM is true.
4. **Part IV (periodicity).** The CRT step is correct: `P = ∏(ALL primes ≤ k)`, so `n` and `n+P` have the same small-prime set (every prime ≤ k divides P); by the similarity theorem, same G-membership; so G is P-periodic for n ≥ k. Theorem 1 application is correct (G* P-periodic, a_1 ∈ G*, orbit = cyclic successor, no pre-period). Verified: the proof's non-minimal period `P` is consistent with the observed minimal period (e.g. a_1=15: P=30030, minimal (T,L)=(8,30), 30 | 30030 ✓).
5. **B2 (from n=1).** IF the similarity theorem holds, B2 is genuinely free via Theorem 1 (no pre-period inside the periodic set, orbit starts at a_1 ∈ G*). The round-1-2 worry (B2 ≠ corollary of injectivity) is correctly dissolved here — not via injectivity, but via the stronger similarity theorem + Theorem 1's single-cycle structure. Valid (conditional on the similarity theorem).

### The GAP — Lemma 2 (s-substitution), the load-bearing lemma for the similarity theorem

**Lemma 2 proof, the `n ≥ 1` branch:** *"Choose one big prime `q` of `b` (which exists: if `b` had no big prime, `b` would already be `k`-smooth and we would be in the `n = 0` situation with `x = a ≤ b`, done; so in the `n ≥ 1` branch `b` has a big prime `q`)."*

**This claim is FALSE.** Counterexample: `a_1 = k = 15`, `b = 18 = 2·3²`. Small primes of `b`: {2,3}. `a = 2·3 = 6`. `p = 2`. The least `n` with `2^n · 6 ≥ 15` is `n = 2` (since `2^1·6 = 12 < 15`, `2^2·6 = 24 ≥ 15`). So `n = 2 ≥ 1`, putting us in the `n ≥ 1` branch. But `b = 18` is **15-smooth** (no prime > 15 divides it) — it has NO big prime `q`. The proof's claim "n ≥ 1 ⟹ b has a big prime" is a non-sequitur: `n ≥ 1` means `a < k` (the inflation is needed to clear `k`), which is about the SIZE of `a = rad(small part)`, NOT about whether `b` carries a prime > `k`. The two conditions are independent.

**Consequence:** the bound `x ≤ b` (via the chain `x < p·k ≤ a·k < a·q ≤ b`) is UNJUSTIFIED when `b` is `k`-smooth and `a < k`, because there is no big prime `q` to anchor the final inequality `a·q ≤ b`. And in fact the construction FAILS in this case: `x = 2^2·6 = 24 > 18 = b`. I verified this is not an isolated artifact:
- `a_1=15`: 1 construction failure (b=18, x=24).
- `a_1=77`: 1 failure (b=98, x=112).
- `a_1=91`: 2 failures (b=98, b=126).
- `a_1=105`: 4 failures.
- `a_1=135`: 6 failures.
- `a_1=175`: 3 failures.
For `a_1 ∈ {35,77,91,105,135,175}` NO greedy term carries a prime > `a_1`, so the big-prime branch is NEVER exercised — every application of Lemma 2 in the similarity descent hits the broken `k`-smooth sub-case.

**Downstream effect on the similarity theorem (Part III).** The descent chooses `r ∈ G` (a move from `a ∉ G`, `gcd(a,r)=1`), then invokes Lemma 2 to produce `r'` with `k ≤ r' ≤ r`, `k`-smooth, similar to `r`, and uses `max(r, r') = r < a` to drive the minimal-counterexample contradiction. When `r` is `k`-smooth with `a < k` (e.g. `r = 18` for `a_1 = 15`), the proof's construction gives `r' = 24 > 18 = r`, so `max(r, r') = 24`, NOT `r`; the strict decrease `max(r, r') < max(a, b)` is no longer guaranteed, and the descent stalls. The "GAP F" remark merely re-asserts `r' ≤ r` — it does not patch the gap.

**The statement of Lemma 2 is TRUE** (a patched proof exists: if `b` is `k`-smooth, take `x = b` directly — trivially `k`-smooth, similar to itself, `k ≤ b ≤ b`; otherwise `b` has a big prime `q` and the `n ≥ 1` bound goes through). With this one-case-split patch, the similarity theorem's descent is fully rigorous (when `r` is `k`-smooth take `r' = r ∈ G` trivially; when `r` has a big prime, the patched Lemma 2 delivers `r' ≤ r`). I verified the patched descent is computationally consistent (0 similarity violations). **But as written, the proof is not rigorous — the gap is in a load-bearing lemma.**

### aimo-0030 citation check
The proof is self-contained — every step is re-proved in the P6 language; `aimo-0030` is invoked only as a structural analog ("the crux shape"), not as authority. No step rests on `aimo-0030`'s authority without re-proof. (The gap above is a genuine proof error, not a citation shortcut.) PASS on the no-citation requirement.

### Verdict
**CHANGES REQUESTED.** Status: `partial` (downgraded from the builder's `solved`). The strategy is sound and would yield a complete proof once Lemma 2 is patched. The single required change: **patch Lemma 2's proof** — add the case split "if `b` is `k`-smooth, take `x = b`" before the `n ≥ 1` argument, and in the similarity theorem handle the `r`-is-`k`-smooth sub-case by taking `r' = r`. With that patch the proof is complete (characterization ✓, similarity ✓, CRT periodicity ✓, Theorem 1 ✓, B2 free ✓). Without it, the similarity theorem's descent has an unjustified step.

### Scores
- Correctness: the Lemma-2 sub-case is wrong as written; the rest is correct.
- Completeness/rigor: gap in a load-bearing lemma (Lemma 2), affecting the crux (similarity descent).
- Progress: MAJOR — the characterization (Lemma 1) and the similarity theorem (statement) are the right crux and are verified; the proof is one patch away from a complete solve.

---

## SLUG 2: `b2-induction-step` — CHANGES REQUESTED (Status: partial)

The builder's Status is `partial — B2 solved given B1'`. This is honest about the B1' dependency. The path-β CRT-density escape is a genuine, sound mechanism. But it imports a CERTIFIED lemma (`sigma-periodicity`) that has a bug in its `T'` formula; with the corrected formula, path β survives.

### What is CORRECT (verified)

1. **Seed `a_1 ∈ B` (`lemmas/a1-on-cycle.md`).** The 4-line proof is rigorous GIVEN B1': universal-small-prime ⟹ every `a_i` shares a prime of `a_1` (≤ R) ⟹ `primes(a_1)` hits every `σ*`-class in `F'_∞` ⟹ contains a minimal `h ∈ M'_∞` ⟹ `m_h | a_1` ⟹ `a_1 ∈ B`. Verified for 15 `a_1`. **CERTIFY** the lemma (conditional on B1', honestly flagged).
2. **`B ⊆ B_n`.** A hitting set of the larger family `F'_∞` contains a minimal hitting set of the smaller family `F'_n` (well-foundedness of inclusion). Valid.
3. **Reduction of B2 to the induction step `a_{n+1} ∈ B`.** The inequality chain (`a_{n+1} = b_n ≤ cyc_succ_B(a_n)` since `B ⊆ B_n`; and `a_{n+1} ∈ B, a_{n+1} > a_n` ⟹ `a_{n+1} ≥ cyc_succ_B(a_n)`) is correct. Valid.
4. **Path β — CRT-density escape (logic).** Assuming `a_{n+1} ∉ B`, some future class `C ∈ F'_∞ \ F'_n` is disjoint from `σ(a_{n+1})`. Every future class-`C` term `a_i` (`i ≥ N > n+1`) must share a prime with `a_{n+1}` (greedy); the shared prime can't be small (`σ(a_{n+1}) ∩ C = ∅`), so it's a large prime `q ∈ Q` (the finite set of primes > R dividing `a_{n+1}`). Within each class-`C` AP (difference `L'`, `gcd(L', q) = 1`), `q`-divisible terms form one residue class mod `q`; CRT over distinct `q ∈ Q` gives uncovered density `∏(1−1/q) > 0`; infinitely many class-`C` terms share NO prime with `a_{n+1}` — contradicting the greedy. The contradiction is valid. `Q` is finite (fixed integer `a_{n+1}`). All cases covered (n = N−1 case (i); 1 ≤ n ≤ N−2 case (ii); n ≥ N is the spine's free case; N=1 trivial). Valid.
5. **The infinite-vs-finite window distinction is REAL.** Path β works over the INFINITE post-N AP (exact CRT density, no sieve error); the refuted (Cov) window was finite (length R, approximate density, sieve error `~a_n` outpaces signal `~n·δ`). The candidate sets also differ (`a_{n+1} ∈ B_n \ B` small-prime-premature vs B1's large-prime `A_n \ B_n` shortcuts). Path β does NOT reduce to the refuted (Cov) claim or the `v_p` sieve-error obstruction. PASS.
6. **B1' dependency flagged honestly.** B2 needs B1' (one-way); path β uses σ-periodicity (conditional on B1'); the proof states this explicitly. PASS.
7. **Path α dropped, path γ subsumed.** Correct (path α's cross-intersecting premise is empirically FALSE; path γ's `2 ∈ S` bridge is unnecessary given path β covers n=1). Honest.

### The GAP — the imported `sigma-periodicity` lemma has a buggy `T'` formula

Path β cites: *"for indices `i ≥ N` the support `σ(a_i)` is `T'`-periodic … each `σ*`-class is, as a set of values, a union of `c* ≥ 1` APs of common difference `L'` … `gcd(L', q) = 1` for every prime `q > R`."* This is the load-bearing structural input.

**The `sigma-periodicity` lemma's `T'` formula is WRONG.** It states `T' := lcm(T, {p ≤ R : p ∤ L})`. The correct period is `T' := lcm(T, {p·T : p ≤ R, p ∤ L}) = T · ∏{p ≤ R, p ∤ L, p prime}`. The discrepancy arises when a prime `p ≤ R` satisfies `p ∤ L` AND `p | T`: the `p`-divisibility of `b_i` has period `p·T` (`p` "blocks of `T`"), but the lemma's `lcm(T, p) = T` (since `p | T`) DROPS the factor of `p`.

**Verified computationally (`a_1 = 35`):** `R = rad(35) = 35`, orbit `(T, L) = (34, 210)`. Prime `p = 17`: `17 ≤ 35`, `17 ∤ 210`, `17 | 34`. The minimal period of `(17 | a_i)` over the greedy tail (8092 terms) is **578 = 17·34**. The lemma's `T'` contribution for `p=17` is `lcm(34, 17) = 34`, which is **NOT** a period (the 17-component fails). The lemma's full `T' = 1910099906` is missing a factor of 17 (ratio 17 vs the correct `32471698402`). So for `a_1 = 35`, the claim "`σ` is `T'`-periodic" (with the lemma's `T'`) is FALSE.

**Impact on path β.** Path β's AP-structure claim ("class-`C` values form APs of difference `L' = (T'/T)·L`") uses the lemma's (buggy) `T'`. For `a_1 = 35`, this `L'` is too small — the class-`C` values form APs with the CORRECT (larger) difference `L'_correct = ∏{p ∤ L}·L`, not the lemma's `L'_buggy = ∏{p ∤ L, p ∤ T}·L`.

**BUT path β's CONCLUSION survives with the corrected period.** Crucially, path β only needs: (a) class-`C` terms form an infinite AP (or union of APs) with SOME common difference `L'`; (b) `gcd(L', q) = 1` for `q ∈ Q` (the large primes of `a_{n+1}`, all > R). With the CORRECTED `T' = T · ∏{p ∤ L}`, we get `L' = ∏{p ∤ L}·L`, whose prime factors are all ≤ R (factors of `L` are kernel primes ⊆ P_R; factors of `∏{p ∤ L}` are primes ≤ R). So `gcd(L', q) = 1` for `q > R` ✓, the AP is infinite ✓, and the CRT-density argument goes through. So path β's density escape is VALID with the corrected `sigma-periodicity` lemma.

(The gcd claim is robust: even the lemma's buggy `L'_buggy` has all prime factors ≤ R, so `gcd(L'_buggy, q) = 1` also holds — the bug doesn't break the gcd step, only the AP-period claim. The corrected period restores the AP structure.)

### Verdict
**CHANGES REQUESTED.** Status: `partial` (the builder's Status is already `partial`; I confirm it). The b2 proof's path β is logically sound and its conclusion (B2-given-B1') is correct. The required changes:
1. **Patch the `sigma-periodicity` lemma's `T'` formula** (see the third bug below) to `T' = T · ∏{p ≤ R, p ∤ L, p prime}`. With the corrected period, path β's AP-structure citation is rigorous.
2. After the patch, B2-given-B1' is fully rigorous. B1' (the open crux, sibling `w-descent-rsmooth`'s target — which itself has a gap this round) remains open.

### Scores
- Correctness: path β logic sound; the only issue is the imported (buggy) lemma, which is patchable and doesn't change the conclusion.
- Completeness/rigor: citation to a buggy lemma; with the correction, complete (conditional on B1').
- Progress: REAL — the CRT-density escape is a genuine new mechanism for B2 that does not re-couple to the refuted spacing/v_p wall. B2-given-B1' is essentially closed.

---

## Third bug: the `sigma-periodicity` lemma (CERTIFIED round 2) needs correction

The lemma `results/imo-2026-06/lemmas/sigma-periodicity.md` states `T' := lcm(T, {p ≤ R : p ∤ L})`. This is too small by a factor of `∏{p ≤ R : p ∤ L, p | T}` whenever some prime `p ≤ R` divides `T` but not `L`. The proof sketch itself says "the residue cycles through all `p` residues in `p` blocks of `T`" — i.e., period `p·T` — but the formula `lcm(T, p)` drops the extra `p` when `p | T`.

**Correct formula:** `T' := lcm(T, {p·T : p ≤ R, p ∤ L, p prime}) = T · ∏{p ≤ R, p ∤ L, p prime}`.

Verified: for `a_1 = 35` (`T=34, L=210`), the 17-component (17 ≤ 35, 17 ∤ 210, 17 | 34) has minimal period 578 = 17·34; the lemma's `lcm(34, 17) = 34` is not a period; the corrected `T' = 34 · (11·13·17·19·23·29·31)` is.

I have appended a correction note to the lemma file and updated the formula. The corrected lemma's other claims (`L' = (T'/T)·L` is an integer; every prime factor of `L'` is ≤ R; `gcd(L', q) = 1` for `q > R`; class-`σ*`-values form APs of difference `L'`) all remain valid with the corrected `T'`.

---

## Lemma certification

- **`a1-on-cycle.md`** (seed `a_1 ∈ B`): **CERTIFIED** (conditional on B1'). The 4-line proof is rigorous; verified for 15 `a_1`. Promotable — admits to `results/imo-2026-06/lemmas/` (already there).
- **`sigma-periodicity.md`**: previously CERTIFIED; **bug found in `T'` formula** — corrected in-place (correction note appended). The corrected version is valid. Downgrade the round-2 certification to "CERTIFIED with correction (round 3)".
- **s-substitution lemma** (w-descent Lemma 2): builder flagged promotable. **REJECT** as-stated (the proof has a false claim). Once patched (k-smooth case → x=b), it will be promotable. Do NOT admit the current version.
- **similarity theorem** (w-descent Part III): builder flagged promotable. **REJECT** as-stated (its descent depends on the unpatched Lemma 2). Once Lemma 2 is patched, promotable.

---

## Summary table

| slug | builder Status | true Status | verdict | outcome | gap |
|------|---------------|-------------|---------|---------|-----|
| `w-descent-rsmooth` | solved | **partial** | CHANGES REQUESTED | partial | Lemma 2 "n≥1⟹b has big prime" FALSE; bound x≤b broken for k-smooth b with a<k; similarity descent unjustified in that sub-case. Patch: k-smooth⟹x=b. |
| `b2-induction-step` | partial | **partial** | CHANGES REQUESTED | advanced | imports sigma-periodicity lemma with buggy T' formula (verified a_1=35, p=17); corrected formula T'=T·∏{p∤L} restores path β. B1' still open. |

The single biggest finding: **the w-descent approach is one patch away from a complete solve** (characterization ✓, similarity ✓ computationally, periodicity ✓, B2 free ✓). The patch is a one-case-split in Lemma 2. If the next round closes it, this problem is SOLVED.
