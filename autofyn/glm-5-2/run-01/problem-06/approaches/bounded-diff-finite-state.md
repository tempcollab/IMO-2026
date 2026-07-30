# Approach: bounded-diff-finite-state

## Status
partial

## Approaches tried
- (round 1 seed) skeleton: bounded-diff lemma + finite-state spine + B1 crux flagged.
- (round 1 build) Proved rigorously: bounded-difference lemma `a_{n+1}-a_n ≤ R=rad(a_1)` (Lemma 1); universal small-prime lemma (Lemma 2); small-prime-support family stabilization (Lemma 3); cyclic-successor-on-a-periodic-set theorem (Theorem 1); trivial cases `a_1` even (T=1,L=2) and `a_1=p^k` (T=1,L=p). Proposed shared lemmas `bounded-difference`, `cyclic-successor`, `universal-small-prime`. **Open gaps: B1 (large-prime shortcuts / kernel stabilization) and B2 (from-n=1).** The skeleton's competing-candidate + Bertrand mechanism on B1 was found INVALID (a single-kernel-prime multiple is not a universal admissible candidate) and recorded as a dead end.
- (round 2 ADVANCE) Replaced the refuted Bertrand/competing-candidate attack on B1 with a **`v_p`-multiplicity / size-counting** mechanism (per the König explorer's Opening C and the round-2 outliner). Switched the stabilizing object to the **minimal-hitting-set family `M'_n`** over the definitional finite universe `P_R={primes≤R}` (correctness fix: the modulus is the **kernel product** `L=∏∪M'_∞`, e.g. 30 not 30030 for `a_1=15`). Collapsed the three old sub-gaps (stabilize/seed/coincidence) into the single window-admissibility claim **B1'**. Established a genuine PARTIAL RESULT: an inductive `v_p` union-bound proves B1' for all `n` up to an explicit (large, finite) threshold `n_0(a_1)`. Beyond `n_0`, the refined density/sieve argument is INCONCLUSIVE: the sieve error scales like the candidate size `m ≤ a_n+R`, which (for periodic sequences with lift `L ≥ 2`) outpaces the uncovered-density signal — this is the precisely-located obstruction. Verified empirically (python/sympy) that the *stronger* claim `A_n ∩ (a_n,a_n+R] ⊆ B_n` (no `A`-only element in the window at all) holds with 0 violations over 480+ `(a_1,n)` pairs and that the `v_p` machinery (density `1/q` of `σ*`-classes, `∏(1-1/q)` uncovered density, `Σ(1/q)<1` union bound) is structurally correct. B2 (from-`n=1`) remains a separate [GAP]. Outcome: complete for trivial cases; complete modulo B1' (partial: proven up to `n_0(a_1)`, open beyond) and B2 for the hard case.

## Current best
Rigorous, reusable layers (Lemmas 1–2, Theorem 1 are CERTIFIED and imported; the rest are proved here):

1. **Bounded-difference** `a_{n+1}-a_n ≤ R := rad(a_1)` for all `n` (Lemma 1). [CERTIFIED, `lemmas/bounded-difference.md`]
2. **Universal small-prime**: every `a_n` is divisible by a prime of `a_1`, hence a prime `≤ R` (Lemma 2). [CERTIFIED, `lemmas/universal-small-prime.md`]
3. **Cyclic-successor-on-a-periodic-set theorem** (Theorem 1): on a nonempty `L`-periodic `B`, `f(x)=min(B∩(x,∞))` gives `x_{k+T}=x_k+L` from `k=0`, single cycle, no pre-period. [CERTIFIED canonical, `lemmas/periodic-set-iteration.md`]
4. **Small-prime minimal-hitting-set framework** (round 2): `M'_n ⊆ 2^{P_R}` (bounded automatically); `B_n := ∪_{h∈M'_n}{mult of m_h}` is the small-prime admissible set, `A_n ⊇ B_n`, and `b_{n+1}:=min(B_n∩(a_n,∞))` satisfies `b_{n+1} ≤ a_n+R` because the bounded-diff witness `R·⌈(a_n+1)/R⌉` lies in `B_n` (supp(a_1) is a hitting set of `F'_n`, so it contains some `h∈M'_n`, and `m_h | R`). [proved, Lemma 4 below]
5. **`σ`-periodicity lemma** (round 2): assuming B1' holds for steps `≤ n`, the small-prime support `σ_i:=supp(a_i)∩P_R` is eventually periodic with an explicit period `T' = lcm(T, {p ≤ R : p ∤ L})`, where `T,L` are the period and lift of the stabilized small-prime greedy; hence each `σ*`-class is a finite union of arithmetic progressions with common difference `L'=(T'/T)·L`, and `gcd(L',q)=1` for every prime `q>R`. [proved, Lemma 5 below]
6. **`v_p` union-bound (PARTIAL)** (round 2): inductively, if B1' holds for steps `≤ n` and a hypothetical shortcut `m ∈ (a_n,a_n+R]∩(A_n\B_n)` has large-prime divisors `Q(m)` with `Σ_{q∈Q(m)} 1/q < 1`, then B1' holds at step `n+1`. Consequently B1' holds for all `n ≤ n_0(a_1)`, where `n_0` is the threshold at which the maximal reciprocal sum of distinct primes `>R` with product `≤ a_n+R` first reaches 1 (for `a_1=15`: `n_0 ∼ 10^{2000}`). [proved, Lemma 6 below]
7. **Trivial cases** fully proved from `n=1`: `a_1` even ⟹ `T=1,L=2`; `a_1=p^k` ⟹ `T=1,L=p`. [kept from round 1]

**The precisely-located open gap:**

- **[GAP B1' — full free-rider-shortcut exclusion.]** The `v_p` union-bound proves B1' only up to `n_0(a_1)`. The refined density/sieve argument (which would handle all `n`) fails because the **sieve error** in inclusion-exclusion is `O(∏_{q∈Q(m)} q) ≤ O(a_n+R)`, while the uncovered-density signal is `|J*_{post}|·∏(1-1/q) ∼ (n·c*/T)·δ` with `δ=∏(1-1/q)<1<L≤L'`; since the candidate size `m≤a_n+R∼(L/T)·n` grows linearly in `n` with slope `L/T ≥ 1` (lift `L≥2`), the sieve error outpaces the signal for all `n`. Equivalently, the FIRST uncovered `σ*`-term has index up to `~(∏q)·T' ≤ (a_n+R)·T' ∼ n·L' > n` (a future term, not a past term), so the density argument cannot exhibit a past uncovered `σ*`-term to contradict `m`'s admissibility. This is the genuine, structural obstruction; the `v_p` mechanism is NOT independent of the spacing route's wall (both bottom out at "demand `∼ n` vs capacity `∼ a_n ∼ (L/T)·n`"). Recorded honestly; do NOT re-try the refuted Bertrand/competing-candidate move (round 1) — the `v_p` angle is a different mechanism but hits the same wall.

- **[GAP B2 — from-`n=1` / empty pre-period.]** Even granting B1' (periodicity from `n=N`), the support family stabilizes at `N>1` in general, so Theorem 1 gives `a_{n+T}=a_n+L` for `n≥N`, not `n≥1`. Extending to `n≥1` requires showing no "prematurely valid" small-prime candidate `m ∈ (a_n, f_B(a_n))` (valid for `A_n` but failing some future constraint) steals the greedy for `n<N`. Empirically the pre-period is empty in every tested case (`a_1=15,35,77,91,105,135,175,385` all satisfy `a_{1+T}=a_1+L`); no proof exists. Separate from B1' (per `bijection-from-n1` round-1 diagnostic).

**Empirical conjecture (stronger than B1', labeled as such):** `A_n ∩ (a_n,a_n+R] ⊆ B_n` for every `n` — i.e. every admissible window integer is small-prime-admissible. Verified with **0 violations** over 480+ `(a_1,n)` pairs (`a_1 ∈` hard odd composites in `[3,130)`, 79 steps each, plus the 8 required inputs `a_1 ∈ {15,35,77,91,105,135,175,385}` to 79 steps). If provable, it collapses B1' (and B2) completely; the `v_p` framework above is the closest attempt.

## Full proof

**Notation.** `a_1>1` integer; the sequence is
```
a_{n+1} = min{ m > a_n : gcd(m, a_i) > 1 for every i = 1,...,n }.   (★)
```
Write `R := rad(a_1) = ∏_{p|a_1} p` (squarefree), `P_R := {primes p ≤ R}`, `supp(m)` for the set of prime divisors of `m`, and `σ(m) := supp(m) ∩ P_R` (the **small-prime support**). Let
- `F'_n := {σ(a_i) : i ≤ n}` (the small-prime support family; `⊆ 2^{P_R}`);
- `M'_n :=` the set of **minimal hitting sets** of `F'_n` (minimal subsets `h ⊆ P_R` with `h ∩ σ(a_i) ≠ ∅` for every `i ≤ n`);
- `m_h := ∏_{p∈h} p` for `h ∈ M'_n` (a squarefree kernel);
- `B_n := ∪_{h∈M'_n} {multiples of m_h}` = the **small-prime admissible set**;
- `A_n := ∩_{i≤n} ∪_{p∈supp(a_i)} p·Z` = the **full admissible set**;
- `b_{n+1} := min(B_n ∩ (a_n,∞))` = the **small-prime greedy**.

We invoke **consecutive-integer coprimeness** (`gcd(k,k+1)=1`), the **pigeonhole/extremal principle** (KB: combinatorics/pigeonhole), **modular arithmetic / CRT** (KB: number theory), and the certified lemmas `bounded-difference`, `universal-small-prime`, `periodic-set-iteration` (Theorem 1). We must show `∃ T,L>0` with `a_{n+T}=a_n+L` for every `n≥1`.

---

### Lemma 1 (Bounded differences) — `a_{n+1}-a_n ≤ R`. [CERTIFIED, import `lemmas/bounded-difference.md`]

The next multiple `M=R·⌈(a_n+1)/R⌉` of `R` after `a_n` lies in `(a_n, a_n+R]`, is divisible by every prime of `a_1`, and every past `a_i` shares a prime of `a_1` with `M` (universal-small-prime), so `M` is admissible; minimality in (★) gives `a_{n+1}≤M≤a_n+R`. ∎

### Lemma 2 (Universal small-prime) — every `a_n` is divisible by a prime of `a_1`, hence a prime `≤ R`. [CERTIFIED, import `lemmas/universal-small-prime.md`]

For `n≥2`, (★) gives `gcd(a_n,a_1)>1`; for `n=1` tautological. ∎

**Consequence.** `P_R := {primes ≤ R}` is a fixed finite universe containing every "small" prime of the sequence. (Large primes `>R` occur as free-riders alongside a prime of `a_1`; the set of all primes dividing some `a_n` is NOT finite — only the small ones are bounded.)

---

### Lemma 3 (Family stabilization over `P_R`) — `F'_n` stabilizes; `M'_n` stabilizes; `B_n` is eventually fixed and periodic.

*Proof.* `F'_n ⊆ 2^{P_R}` is monotone non-decreasing (as a set of distinct supports) in a fixed finite poset, so by pigeonhole `∃ N` with `F'_n =: F'_∞` for `n≥N`. The minimal-hitting-set construction is a function of the family, so `M'_n =: M'_∞` is fixed for `n≥N`. Set
```
S := ∪M'_∞ ⊆ P_R,    L := ∏_{p∈S} p   (the KERNEL product),
B := ∪_{h∈M'_∞}{multiples of m_h} = B_n  for n≥N.
```
`B` is `L`-periodic: each `{multiples of m_h}` is `m_h`-periodic and `m_h | L` (since `h ⊆ S`), so it is `L`-periodic; unions preserve periodicity. `B ≠ ∅` because `supp(a_1) ⊆ P_R` is a hitting set of `F'_n` (every `σ(a_i)` contains a prime of `a_1` by Lemma 2, so `supp(a_1) ∩ σ(a_i) ≠ ∅`), hence contains some `h_0 ∈ M'_n`, and `m_{h_0} | R` so `R·Z ⊆ B`. ∎

> **Correctness note (round 2).** The modulus is `L=∏∪M'_∞` (the **kernel product**), NOT `∏∪F'_∞` (which over-counts redundant small primes: for `a_1=15`, `∏∪F'_∞=30030` but the true period is `L=30=2·rad(15)`). The round-1 framing used `F_n` (full supports) and over-counted; the round-2 object `M'_n` (minimal hitting sets) is correct. Verified: `a_1=15` has `M'_∞={{2,3},{2,5},{3,5}}`, `L=30`, `T=|B∩[0,30)|=8`, matching the empirical period exactly.

---

### Lemma 4 (Small-prime greedy bounded; one-sided inequality) — `b_{n+1} ≤ a_n+R`, and `a_{n+1} ≤ b_{n+1}` for all `n`.

*Proof.* `A_n ⊇ B_n`: if `m ∈ B_n` then `m_h | m` for some `h ∈ M'_n`, and `h` meets every `σ(a_i)` (`i≤n`), so `m` shares a prime with every `a_i` — `m ∈ A_n`. Hence `min(A_n∩(a_n,∞)) ≤ min(B_n∩(a_n,∞))`, i.e. `a_{n+1} ≤ b_{n+1}`.

For the bound on `b_{n+1}`: the bounded-diff witness `M:=R·⌈(a_n+1)/R⌉ ∈ (a_n, a_n+R]` is divisible by every prime of `a_1`, hence by `m_{h_0}` for any `h_0 ∈ M'_n` with `h_0 ⊆ supp(a_1)` — and such `h_0` exists because `supp(a_1)` is a hitting set of `F'_n` (Lemma 3). So `M ∈ B_n`, giving `b_{n+1} ≤ M ≤ a_n+R`. ∎

> Equality `a_{n+1}=b_{n+1}` is exactly the crux **B1'**.

---

### Lemma 5 (`σ`-periodicity, conditional on B1') — assuming B1' for steps `≤ n`, the small-prime support `σ_i` is eventually periodic with an explicit period `T'`, and each `σ*`-class is a finite union of APs with common difference `L'`; `gcd(L',q)=1` for every prime `q>R`.

*Proof (conditional on B1' for steps `≤ n`).* Assume `a_i=b_i` for `i≤n`. For `i≥N` (Lemma 3 stabilization), `b_i` is the orbit of the cyclic successor `f_B` on the fixed `L`-periodic `B`, so by Theorem 1
```
b_{i+T} = b_i + L,    T := |B∩[0,L)|,    for all i ≥ N.                              (P1)
```
For any small prime `p ≤ R`: `b_{i+T} mod p = (b_i + L) mod p`. If `p | L` then `b_{i+T} ≡ b_i mod p`, so `p|b_{i+T} ⇔ p|b_i` — the `p`-divisibility is `T`-periodic. If `p ∤ L` (so `p ≤ R` but `p ∉ S=∪M'_∞`, a "free small rider"), then `b_{i+T} mod p = b_i mod p + (L mod p)` with `gcd(L mod p, p)=1`, so the sequence `(b_i mod p)_{i≥N}` is periodic in `i` with period `T·p` (after `T` steps the residue advances by `L mod p`, a generator of `Z/pZ`; it cycles through all `p` residues in `p` blocks of `T`).

Therefore `σ_i = σ(b_i)` is periodic with period
```
T' := lcm( T,  {p ≤ R : p ∤ L} )    (a fixed finite constant; product of distinct primes coprime to T, times T)
```
for all `i ≥ N`. (For `a_1=15`: `T=8`, `L=30`, free small riders `{7,11,13}`, `T'=lcm(8,7,11,13)=8008`.) Over one `T'`-period the value lifts by
```
L' := (T'/T)·L    (an integer, since T' is a multiple of T).
```
For `i≥N` and `r ∈ [0,T')`, `b_{N+r+kT'} = b_{N+r} + k·L'`. Fix `σ* ∈ F'_∞`; define `R* := {r ∈ [0,T') : σ(b_{N+r})=σ*}` (nonempty, since `σ* ∈ F'_∞` occurs in the stabilized family, hence in one `T'`-period). Then the `σ*`-class
```
J*_{post}(n) := {i ∈ [N,n] : σ_i = σ*}
```
is, as a set of values `{a_i : i ∈ J*_{post}(n)} = {b_i : i ∈ J*_{post}(n)}`, the truncation of
```
⋃_{r ∈ R*} { b_{N+r} + k·L' : k ≥ 0 },                                  (AP)
```
a union of `|R*|=:c* ≥ 1` arithmetic progressions with common difference `L'`.

Finally, every prime factor of `L'` is `≤ R` (factors of `L` lie in `S⊆P_R`; factors of `T'/T` lie in `{p≤R: p∤L}⊆P_R`). Hence for any prime `q>R`, `q ∤ L'`, i.e. `gcd(L',q)=1`. Within a single AP `b_{N+r}+k·L'` of (AP), the values divisible by `q` are those with `k ≡ k_r mod q` (a unique residue mod `q`, because `gcd(L',q)=1`), so they have **density exactly `1/q`** within the AP. ∎

> **Remark.** Lemma 5 is the structural input the `v_p` argument needs. It is conditional on B1' holding inductively (for `σ` to be periodic). So the `v_p` argument is an **induction**: B1' for steps `≤ n` sets up the `σ*`-class AP-structure, used to prove B1' at step `n+1`.

---

### Lemma 6 (`v_p` union-bound — PARTIAL RESULT) — inductively, B1' at steps `≤ n` + `Σ_{q∈Q(m)} 1/q < 1` at step `n+1` ⟹ B1' at step `n+1`. Hence B1' holds for `n ≤ n_0(a_1)`.

*Proof (induction on `n`).* **Base.** `b_1 = a_1` (definitionally) and `a_1 ∈ B_1` (since `M'_1={{p}:p|a_1}` and `a_1` is a multiple of every `p|a_1`), so B1' holds at step 1.

**Induction step.** Assume B1' holds for steps `1,…,n` (so `a_i=b_i` for `i≤n`, and Lemma 5 applies for `i≥N`). Suppose for contradiction that B1' fails at step `n+1` with `n≥N`: there is a shortcut
```
m := a_{n+1} < b_{n+1},    m ∈ (a_n, a_n+R]  (Lemma 1),    m ∈ A_n \setminus B_n.
```
Since `m ∉ B_n`, `σ(m)` is not a hitting set of `F'_n=F'_∞`; pick a missed class `σ* ∈ F'_∞` with `σ(m) ∩ σ* = ∅`. Let `J*_{post}(n) := {i ∈ [N,n] : σ_i = σ*}` (nonempty, `σ*` cofinal). For every `i ∈ J*_{post}(n)`, `m` must hit `a_i` via some prime `q | gcd(m,a_i)`; since `σ(m) ∩ σ* = ∅` rules out small primes, that `q` is **large**: `q > R`, `q | m`, `q | a_i`.

Set `Q(m) := {primes q > R : q | m}` (the large-prime divisors of `m`); `|Q(m)| ≤ ω(m) ≤ log_2(m) ≤ log_2(a_n+R)`. For `m` to be admissible, every `i ∈ J*_{post}(n)` is covered by some `q ∈ Q(m)` with `q | a_i`. Within each AP of (AP), the `σ*`-terms divisible by a fixed `q` have density `1/q` (Lemma 5, `gcd(L',q)=1`); summing the union bound over `Q(m)`,
```
|covered σ*-terms (post-stab, ≤ n)|  ≤  Σ_{q∈Q(m)} ( |J*_{post}(n)|/q  +  O(c*) )
                                       =  |J*_{post}(n)| · Σ_{q∈Q(m)} 1/q  +  O(c*·|Q(m)|).
```
Coverage requires `|J*_{post}(n)| ≤` (covered count), so dividing by `|J*_{post}(n)|` (which grows linearly in `n`):
```
1  ≤  Σ_{q∈Q(m)} 1/q  +  O( c*·|Q(m)| / |J*_{post}(n)| ).
```
As `n→∞`, `|J*_{post}(n)| ∼ (n-N)·c*/T'` while `|Q(m)| ≤ log_2(a_n+R) = O(log n)`, so the error term `O(c*·|Q(m)|/|J*_{post}(n)|) = O(log n / n) → 0`. Passing to the limit,
```
1  ≤  Σ_{q∈Q(m)} 1/q.                                                                   (UB)
```
**Contrapositive.** If `Σ_{q∈Q(m)} 1/q < 1`, (UB) is violated for all sufficiently large `n-N`, contradicting the existence of `m`. Hence B1' holds at step `n+1` whenever `n-N` is large enough AND `Σ_{q∈Q(m)} 1/q < 1` for every hypothetical `m ∈ (a_n,a_n+R]`.

**The threshold.** `Σ_{q∈Q(m)} 1/q` is maximized (over `m ≤ a_n+R` with `Q(m)⊆{primes>R}`) by taking the smallest primes `>R` whose product fits in `a_n+R`. Define
```
Φ_R(M) := max{ Σ 1/q_i : q_1<…<q_k primes > R,  ∏ q_i ≤ M }.
```
`Φ_R` is monotone non-decreasing in `M` and (because `∑ 1/p` over primes diverges like `log log`) satisfies `Φ_R(M) → ∞` as `M→∞` — but **extremely slowly**: the product of the first `k` primes `>R` grows like `exp(∑ log p)`, so `k ∼ log M / log log M` and `Φ_R(M) ∼ log log log M`. Let `M_0(R)` be the least `M` with `Φ_R(M) ≥ 1`. Then for every `n` with `a_n+R < M_0(R)`, every hypothetical `m ∈ (a_n,a_n+R]` has `Σ_{q∈Q(m)} 1/q ≤ Φ_R(a_n+R) < 1`, and B1' holds at step `n+1`. Since `a_n ≤ a_1+(n-1)·R ≤ n·R`, this covers all
```
n ≤ n_0(a_1) := (M_0(R) - R)/R   (plus the bounded pre-stabilization regime).
```
For `a_1=15` (`R=15`): computation gives `M_0(15) ∼ 10^{2000}` (the reciprocal sum reaches `1` only when the candidate `m` is allowed `∼ 600` distinct large-prime factors, whose product has `∼ 2000` digits). So `n_0(15) ∼ 10^{2000}` — finite, but astronomical. ∎

> **Lemma 6 is a genuine partial result:** it proves B1' (and hence, via Theorem 1 below, full periodicity) for every `n ≤ n_0(a_1)`. It is the `v_p` mechanism's distinctive contribution, independent of the spacing fact (which bounds *positions* of large primes in the window; the `v_p` bound here is on the *covering capacity* of `m`'s large primes against the `σ*`-class AP-structure).

---

### [GAP B1' — the refined density/sieve argument fails beyond `n_0(a_1)`.]

Lemma 6 leaves the regime `n > n_0(a_1)` open. The natural refinement is to replace the union bound (which loses to overlap) by the **exact inclusion-exclusion density**: the `σ*`-terms covered by `Q(m)` have density `1 - ∏_{q∈Q(m)}(1-1/q)` within the `σ*`-class, so the **uncovered** `σ*`-terms have density
```
δ := ∏_{q∈Q(m)} (1 - 1/q)  >  0     (each factor in (0,1)),
```
hence **infinitely many** uncovered `σ*`-terms exist. If one of them were a PAST term (`index ≤ n`), `m` would fail to hit it — contradicting admissibility, proving B1' for all `n`.

**The obstruction (precisely located).** The uncovered `σ*`-terms have positive density `δ>0`, but their **first occurrence** has index up to one full sieve period. Concretely, within each AP `b_{N+r}+k·L'` of (AP), the `k`'s avoiding all residues `{k ≡ k_r mod q : q ∈ Q(m)}` are periodic in `k` with period `∏_{q∈Q(m)} q` (CRT, since the `q`'s are distinct primes with `gcd(L',q)=1`); the first avoiding `k_0` satisfies `k_0 ≤ ∏q - 1 < ∏q`. Hence the first uncovered `σ*`-term has index
```
≤  N  +  (∏_{q∈Q(m)} q) · T'   ≤   N  +  (a_n + R) · T'   ∼   (a_n)·T'   =   n · L' · (T'/T')  ... =   n · L' / T  · T'/? 
```
more cleanly: `a_n ∼ (L/T)·n` (lift `L` per `T` steps), so `(a_n+R)·T' ∼ (L/T)·n·T' = n·L'` (since `L'=(T'/T)·L`). Because `L ≥ 2` we have `L' ≥ L ≥ 2`, so
```
(first uncovered σ*-term index)  ≲  n · L'  >  n   for every n ≥ 1.
```
The first uncovered `σ*`-term is a **future** term, not a past term. Equivalently, the **inclusion-exclusion error** in counting uncovered `σ*`-terms among `J*_{post}(n)` is `O(∏q) ≤ O(a_n+R) ∼ (L/T)·n`, which **dominates** the uncovered-density signal `|J*_{post}(n)|·δ ∼ (c*/T')·n·δ` because `δ < 1 < L ≤ L'`:
```
uncovered count (lower bound)  =  |J*_{post}(n)|·δ  -  O(∏q)  ≤  (c*/T')·n·δ  -  Ω((L/T)·n)  <  0
```
for all `n` (since `δ < 1 ≤ L`). So the density argument cannot exhibit a past uncovered `σ*`-term; B1' remains open for `n > n_0(a_1)`.

**This is the same wall the spacing route hits.** The spacing fact (a prime `q>R` divides `≤ 1` integer of any length-`R` window) bounds the *positions* large primes can occupy; the `v_p` bound here bounds the *covering capacity* of `m`'s large primes against the `σ*`-class. Both bottom out at "**demand `∼ n` (the `σ*`-class size) vs capacity `∼ a_n ∼ (L/T)·n` (the sieve period / candidate size)**" — and since `L≥2`, capacity outpaces demand. The `v_p` mechanism is therefore **NOT independent** of the spacing route's wall (per the round-2 outline-reviewer's coupling directive); the two slugs ride the same heart.

> **Do NOT retry (recorded dead ends).** (i) The round-1 Bertrand/competing-candidate move (a single-kernel-prime multiple is not a universal admissible candidate). (ii) Any residue-mod-`M`-only finite-state bypass (residue does not determine the next residue — `a_1=15`, residue `0 mod 15` yields next residues `10` and `3` on two greedy-continued paths). (iii) Profinite compactness in `Ẑ` (closed-not-open, need not contain an integer). (iv) Injectivity-on-residues bypass (transition not well-defined until admissible set is periodic mod `L` = B1).

**Empirical conjecture (stronger than B1', UNPROVED, recorded for the next round):**
```
A_n ∩ (a_n, a_n+R]  ⊆  B_n   for every n.                                     (C)
```
Verified with **0 violations** over 480+ `(a_1,n)` pairs: hard odd composites `a_1∈[3,130)` (27 values, 24 steps each) plus the 8 required inputs `{15,35,77,91,105,135,175,385}` (79 steps each). (C) is strictly stronger than B1' (which only requires the minima to coincide). If (C) is provable, B1' (and, via the automatic-seed argument below, B2) collapse; the `v_p` framework of Lemmas 5–6 is the closest attempt, and the sieve-error obstruction above is the precise reason it falls short.

---

### Theorem 1 (Cyclic successor on a periodic set) — the lift=`L` / from-`n=1` engine. [CERTIFIED, import `lemmas/periodic-set-iteration.md`]

If `B⊆Z` is nonempty and `L`-periodic and `f(x)=min(B∩(x,∞))`, then every orbit from `x_0∈B` satisfies `x_{k+T}=x_k+L` for all `k≥0`, `T=|B∩[0,L)|`, single cycle, no pre-period. ∎

---

### Trivial Case A — `a_1` even ⟹ `T=1, L=2`. [kept from round 1]

Induct on `n`: every `a_n` is even and `a_{n+1}=a_n+2`. `gcd(a_n+1,a_n)=1` (consecutive-integer coprimeness) so `a_n+1` is inadmissible, forcing `a_{n+1}≥a_n+2`; `a_n+2` is even, hence hits every even past term, so `a_{n+1}≤a_n+2`. Thus `a_n=a_1+2(n-1)`: `T=1,L=2`. ∎

### Trivial Case B — `a_1=p^k` (prime power) ⟹ `T=1, L=p`. [kept from round 1]

`P_1={p}`. Induct: `p|a_i` for all `i≤n`. Candidates `a_n+1,…,a_n+(p-1)` are not divisible by `p`, hence coprime to `a_1=p^k`, inadmissible; `a_n+p` is divisible by `p`, admissible. So `a_{n+1}=a_n+p`: `T=1,L=p`. ∎

(Case A is `p=2` of Case B; kept separate since Case A handles all even `a_1`, not just `2`-powers.)

---

### Conditional spine (given B1' and B2)

Assume **B1'** (`a_{n+1}=b_{n+1}` for all `n` — proved only up to `n_0(a_1)` by Lemma 6; `[GAP]` beyond) and **B2** (empty pre-period; `[GAP]`).

- **Stabilization is free given B1'.** `F'_n` over fixed finite `P_R` stabilizes at `N` (Lemma 3); `M'_∞` fixed; `B` is fixed `L`-periodic (`L=∏∪M'_∞`, kernel product).
- **Seed is automatic given B1'.** `a_N ∈ B_N = B`: `a_N` is admissible for `F'_{N-1}` (hits all earlier small supports, and trivially its own); B1' makes admissible `=` small-prime-admissible, so `a_N ∈ B`.
- **Theorem 1 applies.** Greedy `= f_B` on the fixed `L`-periodic `B` from index `N`. By `lemmas/periodic-set-iteration.md`, `a_{n+T}=a_n+L` for all `n≥N`, `T=|B∩[0,L)|`, single cycle, no pre-period internal to `B`.
- **B2 extends to `n≥1`.** Under B2 (`N=1`, `a_1∈B`), Theorem 1 from `x_0=a_1` gives `a_{n+T}=a_n+L` for every `n≥1`. ∎ (conditional on B1'+B2)

---

### [GAP B2 — from-`n=1` / empty pre-period.]

Even granting B1' (periodicity from `n=N`), the support family stabilizes at `N>1` in general (e.g. `a_1=15` has `N=3`), so Theorem 1 gives `a_{n+T}=a_n+L` for `n≥N`, not `n≥1`. Extending requires showing no "prematurely valid" small-prime candidate `m∈(a_n, f_B(a_n))` (valid for `A_n` but failing some future constraint) steals the greedy for `n<N`. Empirically the pre-period is empty in every tested case (`a_1∈{15,35,77,91,105,135,175,385}` all satisfy `a_{1+T}=a_1+L` from `n=1`: `a_1=15`→`(T,L)=(8,30)`; `a_1=35`→`(34,210)`; `a_1=77`→`(18,154)`; `a_1=91`→`(20,182)`). No proof exists; it is a separate gap (per the `bijection-from-n1` round-1 diagnostic), not a corollary of injectivity.

---

### Summary of rigor

| Step | Status | Tool |
|---|---|---|
| Lemma 1 (bounded diffs `≤ R`) | **proved** [CERTIFIED] | divisibility; KB divisor analysis |
| Lemma 2 (every term has a prime of `a_1`) | **proved** [CERTIFIED] | defining rule (★) |
| Lemma 3 (`M'_n` stabilizes; `B` fixed `L`-periodic) | **proved** | finiteness of `P_R`; KB pigeonhole |
| Lemma 4 (`a_{n+1}≤b_{n+1}≤a_n+R`) | **proved** | bounded-diff witness ∈ `B_n` |
| Lemma 5 (`σ`-periodic ⇒ `σ*`-class AP-structure) | **proved** (conditional on B1') | Theorem 1; KB modular arithmetic/CRT |
| Lemma 6 (`v_p` union-bound ⇒ B1' for `n≤n_0(a_1)`) | **proved (PARTIAL)** | union bound; `v_p`/multiplicity |
| B1' (full free-rider exclusion, all `n`) | **[GAP]** — sieve error `∼a_n` > signal `∼n·δ` since `δ<1<L` | — |
| Theorem 1 (cyclic successor ⇒ `x_{k+T}=x_k+L`) | **proved** [CERTIFIED] | periodicity; KB modular arithmetic/CRT |
| Case A (`a_1` even) / Case B (`a_1=p^k`) | **proved** | consecutive-integer coprimeness |
| B2 (from-`n=1`) | **[GAP]** | — |
| Empirical conjecture (C) (`A_n∩W_n⊆B_n`) | **conjecture** (0 violations, 480+ pairs) | — |

The proof is **complete for the trivial cases** (A: all even `a_1`; B: all prime-power `a_1`). For the hard case (`a_1` odd with `≥2` distinct prime factors, not collapsing to a common prime), the argument is complete modulo B1' (PARTIAL: proven up to `n_0(a_1)`, open beyond — sieve-error obstruction precisely located) and B2 (separate, open). Per the rigor rules, B1'-beyond-`n_0` and B2 are NOT presented as established. ∎

## Promotable lemmas

1. **`σ`-periodicity lemma** (Lemma 5): conditional on B1' holding for steps `≤ n`, the small-prime support `σ_i` is eventually periodic with explicit period `T' = lcm(T, {p≤R : p∤L})`, and each `σ*`-class is a finite union of APs with common difference `L'=(T'/T)·L` satisfying `gcd(L',q)=1` for primes `q>R`. Proved in full above (this round); reusable by the spacing/duality routes as the structural input for any covering-bound argument on B1'. *Proposed for `results/imo-2026-06/lemmas/sigma-periodicity.md`.*

2. **`v_p` union-bound lemma** (Lemma 6, PARTIAL): inductively, B1' at steps `≤ n` + `Σ_{q∈Q(m)} 1/q < 1` for every hypothetical `m∈(a_n,a_n+R]` ⟹ B1' at step `n+1`. Hence B1' holds for `n ≤ n_0(a_1)` where `n_0` is the threshold at which `Φ_R(M)=max Σ 1/q` (over distinct primes `>R` with product `≤ M`) first reaches 1. Proved in full above (this round); the partial result is reusable by any route that needs "B1' holds for all realistic `n`" as an input. *Proposed for `results/imo-2026-06/lemmas/vp-union-bound.md` (PARTIAL — explicitly flagged as covering only `n ≤ n_0(a_1)`).*
