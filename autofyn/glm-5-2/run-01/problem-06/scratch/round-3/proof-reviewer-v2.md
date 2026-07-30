# Proof review v2 — IMO 2026 P6 (`imo-2026-06`), round 3 (post-patch)

Re-reviewed the patched `w-descent-rsmooth` (builder re-claims SOLVED after applying the one-case-split patch to Lemma 2). Read the updated approach file and the v2 builder report. Verified every load-bearing claim computationally (python3/sympy, 10 values of `a_1` including the purely-smooth regime). 

## Headline

**APPROVE. Status: SOLVED.** The patch closes the gap I flagged in v1. The proof is now complete, rigorous, and non-circular. IMO 2026 P6 is SOLVED.

The key concern the coordinator raised — whether the a⟶r move (Cor 1.2) is circular — is RESOLVED: Cor 1.2 is proved from Lemma 1 (the characterization G=H), which is proved from the greedy definition ALONE, with NO use of the similarity theorem or periodicity. The descent's strict decrease (`r < a`) comes from Cor 1.2, NOT from the s-substitution, so it is independent of Lemma 2. The purely-smooth regime is handled by a DIRECT contradiction (no descent/minimality needed when `r' = r`).

## Per-concern verification (coordinator's 6 points)

### 1. Is "a⟶r (Cor 1.2)" non-circular? — YES, verified

**Cor 1.2:** `n ≥ k, n ∉ G ⟹ ∃ r ∈ G with r < n and gcd(n, r) = 1.`

**Proof trace (from the file):** `n ∉ G ⟹ n ∉ H` (contrapositive of `H ⊆ G`, Lemma 1) ⟹ `n` fails the `H` condition ⟹ some `g ∈ G` with `g < n` has `gcd(n, g) = 1`. Take `r = g`.

**Dependency:** Lemma 1 (`G = H`) is proved from the greedy definition (★) alone:
- `G ⊆ H`: `n = a_j ∈ G` was selected to be coprime to none of `a_1,…,a_{j-1} = G ∩ [k,n)`. (Greedy definition.)
- `H ⊆ G`: `n ∈ H`, `g_r` = largest `G`-element below `n` = `a_r`; `n` coprime to none of `g_1,…,g_r = a_1,…,a_r`; `n` admissible at step `r`; `a_{r+1} ≤ n`; if `< n`, contradicts `g_r` maximality. (Greedy definition.)

**No use of the similarity theorem, Lemma 2, or periodicity.** Lemma 1 is the foundation, proved from scratch. Cor 1.1 (two G-elements share a prime) and Cor 1.2 (bad number has a move) are its corollaries. **NON-CIRCULAR.** ✓

**Computational verification:** Cor 1.2 (move `r < a` with `gcd(a,r)=1` exists for every bad `a`) checked for `a_1 ∈ {15,35,175,221,385}`: **0 failures** (389 bad `a` for `a_1=35` alone, all have a move). ✓

### 2. The minimal-counterexample descent structure — rigorous, strict decrease REAL

**Restatement:** Suppose the similarity theorem is false. Choose a counterexample pair `(a, b)` with `a ∉ G`, `b ∈ G`, `a, b` similar, `max(a, b)` minimal (well-defined: positive integers ≥ `k`, nonempty set has a least element, attained).

**Descent step:**
1. Cor 1.2: `r ∈ G`, `r < a`, `gcd(a, r) = 1`. [From Lemma 1, non-circular.]
2. `p | k` and `p | r` (Cor 1.1 or trivial if `r = k`). `p` small. `r` has a small prime ⟹ Lemma 2 applies: `r'` with `k ≤ r' ≤ r`, `k`-smooth, similar to `r`.
3. `max(r, r') = r < a ≤ max(a, b)`. **Strict decrease** — from `r < a` (Cor 1.2), NOT from `r' < r`. The pair `(r, r')` is similar; if `r' ∉ G` then `(r', r)` is a counterexample with smaller max, contradicting minimality. So `r' ∈ G`.
4. `r', b ∈ G`. Cor 1.1 (or trivial if `r' = b`): shared prime `p'` with `p' | r'`, `p' | b`. `p'` small (`r'` is `k`-smooth).
5. `p' | r` (`r' ~ r`, `p'` small), `p' | a` (`b ~ a`, `p'` small). `gcd(a, r) ≥ p' ≥ 2`. Contradiction with `gcd(a, r) = 1`. ∎

**The strict decrease is REAL and verified:** `r < a` comes from Cor 1.2 (Lemma 1), verified 0 failures. `max(r, r') = r` since `r' ≤ r` (Lemma 2, verified 0 failures). So `max(r, r') = r < a ≤ max(a, b)`. The minimality step is on the counterexample set (pairs with opposite G-status) — it does NOT assume the similarity theorem (which would say no such pairs exist). **Non-circular.** ✓

### 3. The purely-smooth regime (a_1 ∈ {175, 221, 385}) — handled by DIRECT contradiction

In this regime, NO greedy term has a prime `> a_1`, so every `r ∈ G` is `k`-smooth. Lemma 2 always takes Case 1 (`r' = r`). 

**The descent reduces to a direct contradiction (no minimality needed):**
- `r' = r ∈ G` trivially (no minimality invoked).
- `r ≠ b`: if `r = b`, then `gcd(a, r) = gcd(a, b)`, but `a, b` are similar (same small primes); `b ∈ G` has a small prime (universal-small-prime), so `a` shares it, `gcd(a, b) > 1`, contradicting `gcd(a, r) = 1`. So `r ≠ b`.
- Cor 1.1: `r, b` (distinct, both in G) share a prime `p'`. `p' | r`, `r` `k`-smooth ⟹ `p'` small.
- `p' | a` (`b ~ a`, `p'` small). `p' | r`. `gcd(a, r) ≥ p' > 1`. Contradiction with `gcd(a, r) = 1`.

**No descent, no minimality, no stripping — just the common-small-prime contradiction.** The argument is uniform across both regimes (the minimality is only load-bearing in Case 2 where `r' < r`). ✓

**Computational verification:** `a_1 = 35` (purely-smooth): all 389 bad `a` in `[35, 500]` have a move `r < a` with `gcd(a, r) = 1`, and all such `r` are `k`-smooth. The `r ≠ b` logic verified: no bad `a` has its move `r` equal to a good element similar to `a` (confirming `r ≠ b` is forced). ✓

### 4. Characterization Lemma 1 (G = H) — re-confirmed, the true foundation

**Re-verified for `a_1 = 15` and `a_1 = 35`, full greedy coverage of `[a_1, 300]`: 0 mismatches.** The threshold `k = a_1` (value, not `R = rad(a_1)`) is the natural one: "small" = primes ≤ `a_1`. This is strictly more inclusive than the spine's `R = rad(a_1)` (e.g. `a_1 = 135`: `R = 15` but `k = 135`, so `23` is "small" under `k` but "big" under `R` — dissolving the delay-2 artifact). The characterization holds under the `k = a_1` threshold. ✓

### 5. Periodicity conclusion — rigorous, consistent with observed period

**CRT step:** `P = ∏(ALL primes ≤ k)`. For any prime `p ≤ k`, `p | P`, so `n ≡ n + P (mod p)`, hence `p | n ⟺ p | (n + P)`. So `n` and `n + P` have the same small-prime set (same similarity class). By the similarity theorem, same G-membership. So G-membership depends only on `n mod P`. ✓ (Elementary; the key is that P includes ALL primes ≤ k, so every small prime divides P.)

**Theorem 1 application:** `G^* = {m : m mod P ∈ R}` (P-periodic extension), `G^* ∩ [k, ∞) = G`, `a_1 = k ∈ G^*`. The orbit `a_{n+1} = min{m ∈ G^* : m > a_n}` (since `a_n ≥ k`, `min` over `G^*` = `min` over `G` for `m > a_n ≥ k`). Theorem 1 (certified): `a_{n+T} = a_n + P` for all `n ≥ 1`, `T = |R|`, no pre-period. ✓

**Consistency with observed period:** `a_1 = 15`: `P = 30030`, observed minimal `(T, L) = (8, 30)`. `30 | 30030` ✓ (30030 = 30 · 1001). The proof's `T = |R| = 8008 = 8 · 1001`, `L = P = 30030 = 30 · 1001`. `a_{n+8008} = a_n + 30030` is consistent with `a_{n+8} = a_n + 30`. A non-minimal period is valid. ✓

**Verified directly:** `a_1 = 6` (`P = 30`, `T = 15`): `a_{n+15} = a_n + 30` for all `n` (14984 pairs checked, including from-`n=1`: `a_{16} = 36 = 6 + 30`). `a_1 = 15`: `a_{n+8} = a_n + 30` from `n = 1` (`a_9 = 45 = 15 + 30`). G is P-periodic: 0 failures for `a_1 = 6` (`P = 30`) and `a_1 = 15` (`P = 30030`). ✓

### 6. B2 close — genuinely free, prematurely-valid-candidate obstruction killed

Theorem 1 gives periodicity **from `n = 1` (no pre-period)** because the cyclic successor is a single cycle on the residue set `R` (a bijection, not merely eventually-periodic). The orbit starts at `a_1 = k ∈ G^*`, so `a_{n+T} = a_n + P` holds from `n = 1`.

**The prematurely-valid-candidate obstruction (rounds 1-2) is genuinely killed,** not glossed: that obstruction was specific to the B1'-spine framework (where `a_{n+1} = b_n` only for `n ≥ N`, and for `n < N` one must show `a_{n+1} ∈ B` against prematurely-valid candidates). The w-descent proof BYPASSES the spine entirely: it shows `a_{n+1} = f_{G^*}(a_n)` for ALL `n ≥ 1` (not just `n ≥ N`), because `G^*` is defined from the similarity theorem, which holds for ALL `n ≥ k` simultaneously. There is no pre-stabilization range `n < N` to worry about. The orbit IS the cyclic successor from `n = 1`. ✓

## Lemma 2 (patched) — verified

**Case 1** (`b` `k`-smooth ⟹ `x = b`): trivially `k ≤ x ≤ b` (equality), `k`-smooth, similar to `b`. ✓
**Case 2** (`b` has big prime `q > k`): strip + inflate by minimal power of one small prime; bound `x < p·k ≤ a·k < a·q ≤ b` (anchored by the big prime `q` with `a·q | b`). ✓

**Verified:** 0 failures across `a_1 ∈ {15,35,77,91,105,135,175,221,385}`, all greedy terms (first 300). Includes the purely-smooth regime (Case 1) and the big-prime regime (Case 2). ✓

The builder's remark is correct: the descent needs `r' ≤ r` (NOT `r' < r`); the strict decrease is `r < a` from Cor 1.2. In Case 1 (`r' = r`), the descent still has `max(r, r') = r < a`. ✓

## Sigma-periodicity — NOT a dependency of this proof

The proof does NOT use `sigma-periodicity` (it proves periodicity directly via similarity + CRT, Part IV). The round-2 `sigma-periodicity` bug and its correction do not affect this proof. (Noted in the file.) ✓

## aimo-0030 citation — self-contained

Every step is re-proved in the P6 language. `aimo-0030` is a structural analog, not a citation. No step rests on `aimo-0030`'s authority. ✓

## Verdict

**APPROVE. Status: SOLVED.** The proof is complete and rigorous for every `a_1 > 1`:
1. Lemma 1 (characterization G=H) — proved from scratch, verified 0 mismatches.
2. Cor 1.1, 1.2 — corollaries of Lemma 1, non-circular.
3. Lemma 2 (s-substitution, patched) — Case 1 / Case 2 split, verified 0 failures.
4. Similarity theorem — minimal-counterexample descent, strict decrease from Cor 1.2 (non-circular), verified 0 violations. Purely-smooth regime handled by direct contradiction.
5. Periodicity — similarity + CRT ⟹ G P-periodic ⟹ Theorem 1 ⟹ `a_{n+T} = a_n + P` from `n = 1`. Verified.
6. B2 — free (Theorem 1 no-pre-period, orbit from `a_1 ∈ G^*`). Prematurely-valid-candidate obstruction bypassed.

**Final answer:** `T = |G^* ∩ [0, P)|`, `L = P = ∏_{p ≤ a_1, p prime} p`, and `a_{n+T} = a_n + L` for every positive integer `n`. ✓ (Matches the problem statement exactly.)

IMO 2026 P6 is SOLVED.
