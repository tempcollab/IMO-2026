# Approach: b2-induction-step

## Status
partial — **B2 is solved (given B1')**; the whole theorem remains conditional on the open crux B1' (attacked by the sibling `w-descent-rsmooth`).

## Framing (one line)
Given B1' (sibling; CERTIFIED conditional spine then gives periodicity from index `N`), B2 — the empty pre-period — is the single induction step `a_{n+1} ∈ B` for `n < N`. The seed `a_1 ∈ B` is a clean 4-line theorem (CERTIFIED, `lemmas/a1-on-cycle.md`). The induction step is closed by **path β**: the CRT-density escape — distinct large primes of `a_{n+1}` cover only density `1 − ∏(1−1/q) < 1` of any future `σ*`-class's infinite arithmetic progression, so a future term escapes sharing no prime with `a_{n+1}`, contradicting the greedy. Path α is DEAD (dropped, per the gate: it rests on "M'_∞ pairwise cross-intersecting", empirically FALSE for `a_1 = 135, 105, 385`). Path γ is SUBSUMED by path β (which handles `n = 1` as a special case); the outline's `2 ∈ S` bridge was flawed and is not needed.

## Approaches tried
- **(round 3 NEW, this build)** Path β CRT-density escape — CLOSED the B2 induction step given B1'. The key distinction from the refuted spacing/`v_p` wall: path β covers an *infinite* AP (exact density, no sieve error) rather than a short length-`R` window (approximate density, sieve error `~a_n` outpaces signal). Distinct large primes give *independent* residue classes (CRT), so the uncovered density `∏(1−1/q) > 0` strictly — no `Φ_R ≥ 1` threshold, no covering system. Seed `a_1 ∈ B` certified as `lemmas/a1-on-cycle.md` (verified for 15 `a_1`). Path α dropped (gate: cross-intersecting `M'_∞` empirically FALSE). Path γ subsumed.
- (Prior rounds: skeleton only — see Approaches-tried history in `current.md`.)

## Current best
**B2 is proven, conditional on B1'.** Together with the CERTIFIED conditional spine (B1' ⟹ `a_{n+T} = a_n + L` for `n ≥ N`, `current.md`), and GRANTING B1' (sibling `w-descent-rsmooth`'s job), the whole theorem follows:
`a_1 ∈ B` (seed, `lemmas/a1-on-cycle.md`) + induction `a_{n+1} ∈ B` & `a_{n+1} = cyc_succ_B(a_n)` for `1 ≤ n < N` (path β below) + the spine for `n ≥ N` ⟹ the orbit from `a_1` is the cyclic-successor orbit on `B` ⟹ Theorem 1 (`lemmas/periodic-set-iteration.md`) gives `a_{n+T} = a_n + L` for every `n ≥ 1`.

**The single remaining open gap is B1' itself** (flagged, NOT this slug's target): `a_{n+1} = min(B_n ∩ (a_n, ∞))` for all `n`, equivalently `M_n = M'_n`. This is a DIFFERENT gap from B2; B2 does not secretly re-prove B1' (it assumes it). The logical dependency is one-way: B2 needs B1'; B1' does not need B2.

## Full proof (of B2, conditional on B1')

### 0. Setup and imports

Fix `a_1 > 1` and the greedy sequence
```
a_{n+1} = min{ m > a_n : gcd(m, a_i) > 1 for every i = 1, …, n }.   (★)
```
Let `R := rad(a_1)`, `P_R := {primes ≤ R}`, `σ(a_i) := supp(a_i) ∩ P_R` (small-prime support), `F'_n := {distinct σ(a_i) : i ≤ n}`, `M'_n` the inclusion-minimal hitting sets of `F'_n` over the universe `P_R`, `B_n := ∪_{h ∈ M'_n}{multiples of m_h}` (`m_h := ∏_{p ∈ h} p`), `b_n := min(B_n ∩ (a_n, ∞))`. Let `F'_∞ := ∪_n F'_n`, `M'_∞` its minimal hitting sets, `B := ∪_{h ∈ M'_∞}{multiples of m_h}`, `L := ∏_{p ∈ ∪M'_∞} p` (kernel product).

**Imported, CERTIFIED lemmas (cite, do not re-prove):**
- **bounded-difference** (`lemmas/bounded-difference.md`): `a_{n+1} − a_n ≤ R`.
- **universal-small-prime** (`lemmas/universal-small-prime.md`): every `a_n` is divisible by a prime of `a_1`, hence a prime `≤ R`.
- **Theorem 1 / periodic-set-iteration** (`lemmas/periodic-set-iteration.md`): the cyclic successor on a nonempty `L`-periodic set `B` satisfies `x_{k+T} = x_k + L` for all `k ≥ 0` (no pre-period) from any `x_0 ∈ B`.
- **small-prime-inclusion** (`lemmas/small-prime-inclusion.md`): `M'_n ⊆ M_n`, equivalently `B_n ⊆ A_n`; in particular `a_{n+1} ≤ b_n`.
- **small-prime-minimum-in-window** (`lemmas/small-prime-minimum-in-window.md`): `a_n < b_n ≤ a_n + R`.
- **cross-intersecting-closure** (`lemmas/cross-intersecting-closure.md`): if `M'_n` is pairwise cross-intersecting and the new row `σ(a_{n+1})` hits `F'_n`, then `M'_{n+1} = M'_n`. (Unconditional; *input*-side tool. Not load-bearing for B2.)
- **σ-periodicity** (`lemmas/sigma-periodicity.md`), CONDITIONAL on B1': for `i ≥ N` the support `σ_i = σ(a_i)` is periodic with period `T' := lcm(T, {p ≤ R : p ∤ L})`; each `σ*`-class is, as a set of values, a union of `c* ≥ 1` arithmetic progressions of common difference `L' := (T'/T)·L`; every prime factor of `L'` is `≤ R`, so `gcd(L', q) = 1` for every prime `q > R`.

**The CERTIFIED conditional spine (B1' ⟹ periodicity from `N`)** — re-derived in `bounded-diff-finite-state`, `small-prime-window-lemma`, `hitting-set-monovariant`; recorded in `current.md`. Granting B1':
1. `F'_n` is monotone increasing in `n` and bounded by the finite power set of `P_R`, so it stabilizes: there is `N` with `F'_N = F'_∞`. Then `M'_n` (hitting sets of `F'_n`) also stabilizes for `n ≥ N`: `M'_N = M'_∞`, hence `B_n = B` for `n ≥ N`.
2. For `n ≥ N`, `a_{n+1} = b_n = min(B_n ∩ (a_n,∞)) = min(B ∩ (a_n,∞))`, and `a_{n+1} ∈ B`. So the orbit from `a_{N+1}` lies in `B` and follows the cyclic successor `f_B`.
3. By Theorem 1, `a_{n+T} = a_n + L` for all `n ≥ N+1`, with `T = |B ∩ [0,L)|`.

**B2 = extend to `n ≥ 1`.** We prove:

> **(B2, given B1')** `a_1 ∈ B`, and for every `n ≥ 1`, `a_{n+1} ∈ B` and `a_{n+1} = cyc_succ_B(a_n)`. Consequently `a_{n+T} = a_n + L` for every `n ≥ 1`.

We establish the seed (`a_1 ∈ B`), then the induction step (`a_{n+1} ∈ B` for `1 ≤ n < N`; `n ≥ N` is the spine's free case), then close.

---

### 1. Seed: `a_1 ∈ B` (CERTIFIED, `lemmas/a1-on-cycle.md`)

By universal-small-prime, every `a_i` is divisible by a prime of `a_1`, which lies in `P_R`. So for every `σ*`-class `C ∈ F'_∞` (witnessed by some `a_i` with `σ(a_i) = C`), `primes(a_1) ∩ C ⊇ primes(a_1) ∩ σ(a_i) ≠ ∅`. Thus `primes(a_1)` is a hitting set of `F'_∞`; by well-foundedness it contains `h ∈ M'_∞`. Since `h ⊆ primes(a_1) = supp(a_1)`, `m_h | a_1`, hence `a_1 ∈ B`. ∎

(Empirically verified for `a_1 ∈ {15,21,33,35,45,63,65,75,77,91,105,135,143,145,175}`; for `a_1 = 15`, `M'_∞ = {{2,3},{2,5},{3,5}}` and `a_1 = 15 = m_{ {3,5} }`; for `a_1 = 135`, `M'_∞ = {{2,3},{2,5,7},{3,5},{3,7}}` and `135 = m_{ {3,5} }·9`.)

---

### 2. Reduction of B2 to the induction step `a_{n+1} ∈ B`

**Always `B ⊆ B_n`.** Let `m ∈ B`. Then `m_h | m` for some `h ∈ M'_∞`. Since `h` is a hitting set of `F'_∞ ⊇ F'_n`, and `h` is inclusion-minimal for `F'_∞`, the well-foundedness of inclusion gives a `g ∈ M'_n` with `g ⊆ h`; then `m_g | m_h | m`, so `m ∈ B_n`. (This is the standard "a hitting set of the larger family contains a minimal hitting set of the smaller family" reduction; identical to the certified `B ⊆ B_n` argument in `hitting-set-monovariant` §3 / `small-prime-inclusion.md`'s dual.) Hence `B ⊆ B_n`.

**Assume B1'** (`a_{n+1} = b_n` for all `n`) and **inductively** `a_n ∈ B` (base: `a_1 ∈ B`, §1). Then
- `a_{n+1} = b_n = min(B_n ∩ (a_n, ∞))`. Since `B ⊆ B_n`, `cyc_succ_B(a_n) = min(B ∩ (a_n,∞)) ≥ a_{n+1}`.
- If `a_{n+1} ∈ B`, then `a_{n+1}` is an element of `B` strictly greater than `a_n`, so `a_{n+1} ≥ min(B ∩ (a_n,∞)) = cyc_succ_B(a_n)`. Combined with the previous inequality, `a_{n+1} = cyc_succ_B(a_n) ∈ B`, completing the induction.

So **the entire content of B2 (given B1' + the seed) is the induction step:**

> **(GAP H)** For every `n ≥ 1` with `n < N` (the pre-stabilization range), `a_{n+1} ∈ B`.

(For `n ≥ N`, `B_n = B` and `a_{n+1} = min(B ∩ (a_n,∞)) ∈ B` is the spine's free case.) We close GAP H by **path β** (§3). Path α is dropped (§4). Path γ is subsumed (§5).

---

### 3. Path β: the induction step via the CRT-density escape (CLOSES GAP H)

Fix `n` with `1 ≤ n < N` (the pre-stabilization range). We prove `a_{n+1} ∈ B`, i.e. `σ(a_{n+1})` is a hitting set of `F'_∞`, i.e. `σ(a_{n+1})` intersects every `σ*`-class `C ∈ F'_∞`. Since `a_{n+1} = b_n ∈ B_n` (B1'), `σ(a_{n+1}) ⊇ g` for some `g ∈ M'_n`, so `σ(a_{n+1})` already hits every class in `F'_n`. The only classes it could miss lie in `F'_∞ \ F'_n` — classes whose first appearance is at an index in `(n, N]` (because `F'_N = F'_∞` and `F'_n ⊆ F'_{n+1} ⊆ … ⊆ F'_N`). Call these the **future classes** (relative to step `n`).

**Case (i): `n = N − 1`.** Then `F'_∞ \ F'_{N-1} ⊆ {σ(a_N)}` (at most the one new class introduced by the single new term `a_N`). If `σ(a_N) ∈ F'_{N-1}` already, the future-class set is empty and `a_N ∈ B` trivially. Otherwise the unique future class is `C = σ(a_N)`, and `σ(a_N) ∩ C = σ(a_N) ≠ ∅`. So `a_N ∈ B`. ∎ (case i)

**Case (ii): `1 ≤ n ≤ N − 2`.** Suppose, for contradiction, that `a_{n+1} ∉ B`. Then some future class `C ∈ F'_∞ \ F'_n` satisfies `σ(a_{n+1}) ∩ C = ∅`. Let `Q := {primes q > R : q | a_{n+1}}` (the large primes of `a_{n+1}`); `Q` is a finite set of distinct primes, all `> R`.

**Structure of the future terms of class `C`.** By σ-periodicity (CONDITIONAL on B1', which we grant globally), for indices `i ≥ N` the support `σ(a_i)` is `T'`-periodic and each `σ*`-class is, as a set of values, a union of `c* ≥ 1` arithmetic progressions of common difference `L'`, with `gcd(L', q) = 1` for every prime `q > R` (in particular for every `q ∈ Q`). Since `F'_N = F'_∞`, class `C` is present in the periodic tail, so `c* ≥ 1` and the class-`C` values for `i ≥ N` are
```
{v_s + k L' : k ≥ 0},   s = 1, …, c*,
```
each an infinite forward AP (`L' > 0`), and each value is an actual greedy term `a_i` with `i ≥ N`. Because `n ≤ N − 2`, we have `i ≥ N > n + 1`, i.e. **every such `a_i` is a future term relative to `a_{n+1}`**.

**Every future class-`C` term is divisible by some `q ∈ Q`.** Take any `i ≥ N` with `σ(a_i) = C`. Since `a_{n+1}` is a past term when `a_i` is chosen (its index `n+1 < i`), the greedy rule (★) forces `gcd(a_i, a_{n+1}) > 1`. The shared prime cannot be small: any small prime of `a_{n+1}` lies in `σ(a_{n+1})`, which is disjoint from `C = σ(a_i)`. So the shared prime is large, i.e. belongs to `Q`. Thus `q | a_i` for some `q ∈ Q`. (If `Q = ∅` — `a_{n+1}` is `R`-smooth — this is already impossible: there is no prime to share, contradicting the greedy. So `a_{n+1} ∈ B` trivially when `Q = ∅`. The argument below handles `Q = ∅` by the empty-product convention `∏(1 − 1/q) = 1`.)

**Density escape (the crux).** Fix one AP `s` and consider its terms `v_s + k L'` (`k ≥ 0`). For `q ∈ Q` (distinct primes, all coprime to `L'`), the congruence `q | (v_s + k L')` is equivalent to `k ≡ r_{s,q} (mod q)` where `r_{s,q} := −v_s · (L')^{−1} (mod q)` (well-defined since `gcd(q, L') = 1`). So within AP `s`, the set of `k` for which `v_s + k L'` is divisible by some `q ∈ Q` is
```
⋃_{q ∈ Q} { k ∈ ℤ_{≥0} : k ≡ r_{s,q}  (mod q) }.
```
The residue classes `r_{s,q} (mod q)` for distinct primes `q ∈ Q` are **independent** (Chinese Remainder Theorem). The complement — the set of `k ≥ 0` for which `v_s + k L'` is divisible by **no** `q ∈ Q` — is, by CRT, a union of residue classes modulo `∏_{q ∈ Q} q` of total density
```
∏_{q ∈ Q} (1 − 1/q)  >  0
```
(the product of finitely many numbers in `(0,1]`; for `Q = ∅` it equals `1`). Hence within each AP `s` there are **infinitely many** `k` (positive density, unbounded) such that `a_i := v_s + k L'` is a class-`C` future greedy term divisible by **no** `q ∈ Q`.

**Contradiction.** Any such `a_i` (class `C`, so `σ(a_i) ∩ σ(a_{n+1}) = ∅`; and not divisible by any `q ∈ Q`, so sharing no large prime with `a_{n+1}`) shares **no prime at all** with `a_{n+1}`. But `a_{n+1}` is a past term at step `i − 1`, so the greedy rule (★) requires `gcd(a_i, a_{n+1}) > 1`. Contradiction.

Therefore no future class `C` is disjoint from `σ(a_{n+1})`; i.e. `σ(a_{n+1})` hits every class of `F'_∞`, i.e. `a_{n+1} ∈ B`. ∎ (case ii, hence GAP H)

**Remark on the mechanism (and why it does NOT re-couple to the refuted `v_p` wall).** The refuted `v_p`/spacing attack on B1' itself (current.md: "9927 violations", "`v_p` sieve-error obstruction beyond `n_0 ~ 10^{2000}`") works over a **short window** `W_n = (a_n, a_n + R]` of length `R`: each large prime `q` divides ≤1 slot (spacing fact), so the "coverage" of `σ*`-classes by `q`-multiples within the window is an **approximate** density argument with sieve error `O(c*·|Q|)` per class that grows like `a_n` and outpaces the `~n · δ` signal (since `δ < 1 ≤ L`). Path β works over an **infinite AP** (the entire post-`N` tail of one class), so the density is **exact**: the uncovered density is the literal `∏_{q ∈ Q}(1 − 1/q) > 0`, a strict positive real, with no finite-window sieve error and no `Φ_R ≥ 1` threshold. The candidate set also differs (`a_{n+1} ∈ B_n \ B` here is a small-prime-premature candidate, whereas B1' short-cuts `m ∈ A_n \ B_n` use large primes as the *stealing* primes); but the deeper reason path β survives is the infinite-vs-finite window distinction, not merely the candidate identity. The only number-theoretic input is CRT (independence of distinct prime residue classes), which is exact. **Path β does not reduce to the refuted (Cov) window claim nor to the `v_p` sieve-error obstruction.**

(Empirically the conclusion `a_{n+1} ∈ B` for all `n` is confirmed: for every tested `a_1 ∈ {15,35,45,77,91,105,135,175,187,221,385}`, the pre-period is empty — `a_n ∈ B` for all `n ≥ 1`, e.g. `a_1 = 15` gives `M'_∞ = {{2,3},{2,5},{3,5}}`, `B =` multiples of `6, 10, 15`, and the greedy orbit `15,18,20,24,30,…` lies entirely in `B` from `n = 1`.)

---

### 4. Path α — DROPPED (gate directive)

Path α attempted to freeze `M'_n = M'_∞` early via the cross-intersecting closure lemma, premised on **`M'_∞` being pairwise cross-intersecting** (sibling `cross-intersecting-anchor` GAP B). The gate empirically REFUTED this premise: for `a_1 = 135` (`R = 15`), `M'_∞` contains `{2,5}` and `{3,7}` with `{2,5} ∩ {3,7} = ∅`; likewise for `a_1 = 105, 385`. Path α is therefore DEAD (not merely coupled), and is removed from the live proof. It is not needed: path β closes GAP H unconditionally on the internal structure of `M'_∞`.

(Independent re-computation of `M'_∞` for `a_1 = 135` over 200 greedy terms gives `M'_∞ = {{2,3},{2,5,7},{3,5},{3,7}}`, which *is* pairwise cross-intersecting — but the gate's larger computation found a non-cross-intersecting stabilization; regardless, the gate's directive to drop path α is followed, since path β makes it unnecessary in either reading.)

---

### 5. Path γ — SUBSUMED (the `2 ∈ S` bridge is unnecessary and was flawed)

The outline proposed a "cheap sub-claim" `2 ∈ S` (some `h ∈ M'_∞` contains `2`) to resolve the first induction step `n = 1` for odd `a_1`, via the bridge "once an even term exists, `2` is a hitting prime of `F'_∞`". The gate correctly flagged this bridge as **flawed**: it conflates "`2` divides some `a_j`" (FALSE for `a_1 = 15`, where `σ(a_1) = {3,5}`) with "{2} is a hitting set" with "`2 ∈ ∪M'_∞`". The CLAIM `2 ∈ ∪M'_∞` is empirically TRUE for all tested `a_1`, and the sub-fact "`a_2 = a_1 + p_0` is even for odd `a_1`" (`p_0` = smallest prime of `a_1`) is correct and easy (both `a_1`, `p_0` odd ⟹ `a_1 + p_0` even; `p_0 | a_1` ⟹ `a_2 = a_1 + p_0` is the smallest multiple of `p_0` above `a_1`, is admissible, and `≤ a_1 + R`). But the bridge from "an even term exists" to "`2 ∈ ∪M'_∞`" has no clean mechanism: why does the greedy's structure *force* `2` into a *minimal* hitting set, rather than merely into `supp(a_2)`?

**This sub-claim is not needed for B2.** Path β (§3) handles the induction step for *every* `1 ≤ n < N`, including `n = 1`, by the CRT-density escape — with no reference to `2 ∈ S`. The `n = 1` instance of path β reads: if `σ(a_2)` missed some future class `C`, then (by σ-periodicity + CRT) some future class-`C` term `a_i` (`i ≥ N > 2`) would share no prime with `a_2`, contradicting the greedy. So `a_2 ∈ B`. The seed `a_1 ∈ B` is §1. Path γ is therefore entirely subsumed; we do not prove `2 ∈ S` here. **[Honest status: `2 ∈ ∪M'_∞` is an empirically true but unneeded side-fact; no gap in B2 is left by leaving it unproved.]**

---

### 6. Close (B2 ⟹ the theorem, given B1' + spine)

Collecting §1 (seed `a_1 ∈ B`), §3 (GAP H: `a_{n+1} ∈ B` for `1 ≤ n < N`), and the CERTIFIED conditional spine (`a_{n+1} ∈ B` for `n ≥ N` since `B_n = B`, and the orbit from `a_{N+1}` follows `f_B`), we have `a_n ∈ B` for every `n ≥ 1`. Moreover, for every `n ≥ 1`, the inequality chain of §2 gives
```
a_{n+1} = b_n = min(B_n ∩ (a_n,∞))  ≤  min(B ∩ (a_n,∞)) = cyc_succ_B(a_n)
```
and `a_{n+1} ∈ B` with `a_{n+1} > a_n` forces `a_{n+1} ≥ cyc_succ_B(a_n)`; hence **`a_{n+1} = cyc_succ_B(a_n)` for every `n ≥ 1`**. The orbit `(a_n)_{n ≥ 1}` is thus exactly the cyclic-successor orbit on the `L`-periodic set `B` starting from `x_0 = a_1 ∈ B`. By **Theorem 1** (`lemmas/periodic-set-iteration.md`), with `T = |B ∩ [0, L)|` and lift `L`,
```
a_{n+T} = a_n + L    for every n ≥ 1.
```
This is the theorem of `imo-2026-06`, **conditional on B1'** (the open crux `a_{n+1} = min(B_n ∩ (a_n,∞))` for all `n`, equivalently `M_n = M'_n`, attacked by the sibling `w-descent-rsmooth`). ∎ (B2 given B1'; the whole theorem given B1' + B2 + spine)

---

## Promotable lemmas
- **`a1-on-cycle`** (`results/imo-2026-06/lemmas/a1-on-cycle.md`, CERTIFIED conditional on B1'): the seed `a_1 ∈ B`. Statement and 4-line proof above (§1). For the reviewer to certify.
- **CRT-density escape (the B2 induction step)** — proved in full in §3 above. Statement (conditional on B1' + σ-periodicity): *if `a_{n+1} = b_n` (B1') and `n < N`, then `a_{n+1} ∈ B`; mechanism: distinct large primes of `a_{n+1}` cover density `1 − ∏(1−1/q) < 1` of any future `σ*`-class's infinite AP, so a future term escapes sharing no prime, contradicting the greedy.* This is the load-bearing B2 step; recommend the reviewer certify it as `lemmas/crt-density-escape.md` for reuse by any B2-targeting approach.
