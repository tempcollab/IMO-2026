# small-prime-window-lemma — IMO 2026 P6

**Approach:** reframe the crux B1 (kernel stabilize + coincidence + seed) as the SINGLE
window-admissibility claim B1' = "no large-prime shortcut in the window `(a_n, a_n+R]`, where
`R = rad(a_1)`," and attack it via the **spacing fact** (a prime `q > R` divides at most one integer
of any length-`R` window) plus a covering bound. Once B1' holds the rest is free (pigeonhole
stabilization of the small-prime minimal-hitting-set family over the definitional finite universe
`P_R = {primes ≤ R}`, then the certified cyclic-successor theorem).

## Status
partial

## Approaches tried
- **Round 2 (this approach).** Spacing+covering attack on B1'. Rigorously proved: (i) the clean
  reduction of the whole problem to the single claim B1' (with the correct stabilizing object
  `M'_n` = minimal hitting sets of small supports, and the correct modulus `L = ∏∪M'_∞`, the
  KERNEL product — NOT `∏∪F'_∞` which over-counts, verified `L=30` for `a_1=15` not `30030`);
  (ii) the **spacing fact** (a prime `q > R` divides at most one integer of `W_n = (a_n, a_n+R]`);
  (iii) a **necessary-condition lemma** refining the spacing attack: a shortcut candidate
  `m ∈ (a_n, b_n) ∩ (A_n \ B_n)` missing a small-support class `σ*` can hit a `σ*`-term `a_j` via
  a large prime `q` ONLY IF `a_j ≤ a_n + R - q`; hence every `σ*`-term in the value window
  `(a_n + R - q_min(m), a_n]` (where `q_min(m)` is `m`'s smallest large prime) is UNHITTABLE by
  `m`'s large primes — so a shortcut REQUIRES that no `σ*`-term lies in that window AND that every
  earlier `σ*`-term is divisible by an appropriate large prime of `m`. (iv) the conditional spine:
  given B1', `F'_n` stabilizes over finite `P_R`, `B_n = B` is a fixed `L`-periodic set, the seed
  `a_{N_0} ∈ B` is AUTOMATIC (closes the old B1(b) sub-gap for free), and Theorem 1 (imported)
  gives `a_{n+T} = a_n + L` for `n ≥ N_0`. **[GAP B1' — the covering SUFFICIENCY]**: I could not
  prove that the necessary spacing condition is also sufficient — i.e. that some `σ*`-term escapes
  `m`'s large-prime reach. The clean value-window version was tested empirically and FAILS (the
  `σ*`-terms are too sparse in a length-`(q_min - R)` window; 9927 violations at `a_1=15`), and
  the value-gap to the most recent missed term can be large (`747` at `a_1=175`), so the real
  obstruction is number-theoretic (which large primes divide which past terms), not pure
  value-spacing. **[GAP B2 — from-n=1]** remains open (secondary). Honest partial: the reduction,
  spacing fact, necessary-condition lemma, and conditional spine are rigorous; B1' sufficiency and
  B2 are the precisely-located open gaps.
- Prior rounds (shared, imported): bounded-difference, universal-small-prime, Theorem 1, trivial
  cases — all CERTIFIED (see lemmas/).

## Current best
The furthest rigorous progress:

1. **Clean reduction to B1'.** Using `M'_n` (minimal hitting sets of small supports `σ_i =
   supp(a_i) ∩ P_R`) as the object — automatically finite-valued over `P_R` — the problem's whole
   crux collapses to the single claim B1' = "`a_{n+1} = min(B_n ∩ (a_n,∞))` for all `n`," where
   `B_n = ∪_{h∈M'_n}{multiples of ∏_{p∈h}p}`. The old sub-gaps "stabilize kernel `S`,"
   "coincidence," and "seed `a_N ∈ A`" all dissolve: stabilization is free (pigeonhole over
   `P_R`), coincidence IS B1', and the seed is automatic (Lemma 6). The modulus is the KERNEL
   product `L = ∏_{p ∈ ∪M'_∞} p`, verified correct (e.g. `30` for `a_1=15`, not `30030`).

2. **Spacing fact (Lemma 7).** Every prime `q > R` divides at most one integer of `W_n`.

3. **Necessary-condition lemma (Lemma 8).** A shortcut `m ∈ (a_n,b_n) ∩ (A_n \ B_n)` missing `σ*`
   can hit a `σ*`-term `a_j` via large prime `q` only if `a_j ≤ a_n + R - q`. Hence all `σ*`-terms
   in the value window `(a_n + R - q_min(m), a_n]` are unkillable by `m`'s large primes. This is
   the genuine contribution of the spacing mechanism — it LOCALIZES the obstruction to recent
   `σ*`-terms — but it is only necessary, not sufficient.

**Open gaps (precisely located):**
- **[GAP B1' — covering sufficiency]** Prove that for every hypothetical shortcut `m ∈ (a_n, b_n) ∩
  (A_n \ B_n)` and every small-support class `σ*` that `σ(m)` misses, at least one `σ*`-term `a_j`
  is NOT divisible by any large prime of `m` (so `m` fails admissibility). The spacing fact gives
  the value bound `a_j ≤ a_n + R - q`; the unproved step is showing this value bound (or any other
  uniform bound) EXCLUDES every `σ*`-term. Empirically B1' holds universally (300–1500 terms, all
  13 tested `a_1`), but the clean value-window formulation FAILS as a sufficient mechanism. A
  genuinely new idea (beyond spacing/density) is needed; the obstruction is number-theoretic.
- **[GAP B2 — from-n=1]** Even granting B1' (periodicity from `n = N_0`), extend to `n ≥ 1`. The
  single-cycle property of Theorem 1 removes any pre-period INSIDE `B`, but `n < N_0` uses a
  different (still-stabilizing) `B_n`, so a "prematurely valid" small-prime candidate could in
  principle steal the greedy. Empirically the pre-period is always empty; no proof exists.

## Full proof
(Not yet — Status is `partial`. The rigorous partial structure follows; the two marked [GAP]s
are the only missing steps.)

---

### 0. Setup and imported machinery

Let `a_1, a_2, …` be defined by
```
a_{n+1} = min{ m > a_n : gcd(m, a_i) > 1  for every i = 1,…,n }.        (★)
```
We prove there exist positive integers `T, L` with `a_{n+T} = a_n + L` for all `n ≥ 1`.

**Notation.**
- `R := rad(a_1) := ∏_{p | a_1} p` (squarefree product of distinct primes of `a_1`).
- `P_R := { primes p : p ≤ R }` — a **fixed finite set** (the small-prime universe).
- `supp(x) := { primes p : p | x }`; `σ_i := supp(a_i) ∩ P_R` (the *small-prime support* of `a_i`).
- `F'_n := { σ_i : 1 ≤ i ≤ n }` (family of distinct small-prime supports seen so far; monotone in `n`).
- `M'_n :=` the set of **minimal hitting sets** of `F'_n` (subsets `h ⊆ P_R` meeting every member
  of `F'_n`, minimal under inclusion). `M'_n ⊆ 2^{P_R}` automatically.
- For `h ⊆ P_R`, `m_h := ∏_{p ∈ h} p`. The **small-prime admissible set**
  `B_n := ∪_{h ∈ M'_n} { x ∈ ℤ_{>1} : m_h | x } = ∪_{h ∈ M'_n} m_h · ℤ_{>0}`.
- The **true admissible set** `A_n := { m > 1 : gcd(m, a_i) > 1 ∀ i ≤ n }`.
- `W_n := (a_n, a_n + R]` (the *window*, of length `R`); `b_n := min(B_n ∩ (a_n, ∞))` (the
  small-prime minimum).

**Imported (certified, see `lemmas/`):**
- **Bounded-difference lemma** (`lemmas/bounded-difference.md`): `a_{n+1} - a_n ≤ R` for all `n`.
  *Mechanism:* `M := R · ⌈(a_n+1)/R⌉` (next multiple of `R` after `a_n`) is divisible by every
  prime of `a_1`; every past `a_i` shares a prime of `a_1` with `M` (universal-small-prime below),
  so `M` is admissible and `a_{n+1} ≤ M ≤ a_n + R`.
- **Universal-small-prime lemma** (`lemmas/universal-small-prime.md`): every `a_n` (`n ≥ 2`) shares
  a prime of `a_1` with `a_1`, hence is divisible by some prime `p ≤ R`. (For `n = 1` tautological.)
- **Theorem 1 — cyclic successor on a periodic set** (`lemmas/periodic-set-iteration.md`): if
  `A ⊆ ℤ` is nonempty and `L`-periodic (`A + L = A`), `f_A(x) = min{y ∈ A : y > x}`, and
  `x_0 ∈ A`, then the orbit `x_{k+1} = f_A(x_k)` satisfies `x_{k+T} = x_k + L` for all `k ≥ 0`,
  `T = |A ∩ [0,L)|`, single cycle, no pre-period.
- **Trivial cases** (proved round 1, verified): `a_1` even `⟹ T = 1, L = 2`; `a_1 = p^k` (prime
  power) `⟹ T = 1, L = p`. These are settled unconditionally and are henceforth excluded.

Henceforth assume **`a_1` is odd with at least two distinct prime factors** (the hard case).

---

### 1. The small-prime admissible set lies inside the true one

**Lemma 1 (B_n ⊆ A_n).** For every `n ≥ 1`, `B_n ⊆ A_n`, hence `min(A_n ∩ (a_n,∞)) ≤ min(B_n ∩
(a_n,∞))`, i.e. `a_{n+1} ≤ b_n`.

*Proof.* Take `m ∈ B_n`. Then `σ(m) ⊇ h` for some `h ∈ M'_n` (because `m` is divisible by `m_h =
∏_{p ∈ h} p`, so every `p ∈ h` divides `m`; `h ⊆ σ(m)`). Since `h` is a hitting set of `F'_n`, for
every `i ≤ n` we have `h ∩ σ_i ≠ ∅`. Pick `p ∈ h ∩ σ_i ⊆ P_R`; then `p | m` and `p ∈ σ_i ⊆
supp(a_i)`, so `p | a_i`. Thus `gcd(m, a_i) ≥ p > 1` for every `i ≤ n`, i.e. `m ∈ A_n`. ∎

(Equivalently: a hit by a small prime is a genuine hit, because `σ_i ⊆ supp(a_i)`.)

---

### 2. The small-prime minimum lies in the window

**Lemma 2 (`b_n ∈ W_n`, i.e. `a_n < b_n ≤ a_n + R`).** For every `n ≥ 1`, the next multiple of `R`
after `a_n` belongs to `B_n`, so `b_n ≤ a_n + R`.

*Proof.* Let `M := R · ⌈(a_n + 1)/R⌉` (the least multiple of `R` strictly greater than `a_n`). Then
`a_n < M ≤ a_n + R`. Since `R` is divisible by every prime of `a_1`, so is `M`; hence
`primes(a_1) ⊆ supp(M) ∩ P_R = σ(M)`. By the universal-small-prime lemma, every `a_i` (`i ≤ n`)
shares a prime of `a_1` with `a_1`, i.e. `σ_i ∩ primes(a_1) ≠ ∅`. But `primes(a_1) ⊆ σ(M)`, so
`σ(M) ∩ σ_i ⊇ σ(M) ∩ primes(a_1) ∩ σ_i ≠ ∅` for every `i ≤ n`. Therefore `σ(M)` is a hitting set
of `F'_n`; it contains some `h ∈ M'_n` (every hitting set contains a minimal one), so `M` is a
multiple of `m_h`, i.e. `M ∈ B_n`. Hence `b_n ≤ M ≤ a_n + R`. ∎

Consequently the greedy always lands in `W_n`: by the bounded-difference lemma `a_{n+1} ≤ a_n + R`,
and by definition `a_{n+1} > a_n`.

---

### 3. The crux B1' (single window-admissibility claim)

**Claim B1'.** *For every `n ≥ 1`,*
```
a_{n+1} = b_n = min(B_n ∩ (a_n, ∞)).
``

By Lemma 1 we always have `a_{n+1} ≤ b_n`; B1' is the **reverse inequality** `a_{n+1} ≥ b_n`.
Equivalently:

> **(B1', window form)** *No integer `m` with `a_n < m < b_n` (i.e. `m ∈ (a_n, b_n) ⊆ W_n`) lies
> in `A_n \ B_n`.*

(Indeed `a_{n+1}` is the minimum of `A_n ∩ (a_n, ∞)`; if some `m ∈ (a_n, b_n)` lay in `A_n \ B_n`,
it would be an admissible candidate smaller than `b_n`, contradicting `a_{n+1} = b_n` — so B1' is
exactly the absence of such "large-prime shortcuts.")

**Reformulation in hitting-set language (equivalence, recorded for clarity).** B1' is equivalent to:
*every minimal hitting set `g ∈ M_n` of the FULL support family `{supp(a_i) : i ≤ n}` uses only
small primes, i.e. `M_n = M'_n` for all `n`.* (Proof of equivalence: `A_n = ∪_{g ∈ M_n} {mult of
m_g}` and `B_n = ∪_{h ∈ M'_n} {mult of m_h}`. If `M_n = M'_n` then `A_n = B_n` and the minima
agree. Conversely, if some `g ∈ M_n` contains a large prime `q > R`, then by minimality of `g`
there is a past `a_j` with `supp(a_j) ∩ (g \ {q}) = ∅` and `q | a_j` — a row hit ONLY through `q`;
in the window form this is exactly a `σ*`-class (`σ_j`) that the candidate's small part misses,
requiring a large-prime hit. The two formulations coincide.) This is the equivalence found in
round-2 reconnaissance; it shows B1' is the SAME wall the other routes hit, now stated as one clean
claim.

---

### 4. The spacing fact

**Lemma 3 (spacing).** *Let `q > R` be a prime. Then `q` divides at most one integer of the window
`W_n = (a_n, a_n + R]`.*

*Proof.* Two distinct multiples of `q` differ by at least `q`. The window `W_n` has length `R < q`,
so it cannot contain two distinct multiples of `q`. ∎

This is the **only** structural input the spacing mechanism provides on window positions; it is
genuinely weak (at `a_1 = 35, n = 221`, large past primes collectively touch `15` of the `35`
window slots — so spacing alone does not bound the number of large-prime-touched slots).

---

### 5. The necessary-condition lemma (refined spacing)

Fix `n`, suppose (toward understanding a hypothetical shortcut) that `m ∈ (a_n, b_n) ∩ (A_n \ B_n)`
were a shortcut. Since `m ∉ B_n`, the small support `σ(m)` fails to hit some class `σ* ∈ F'_n`;
fix such a `σ*` and let `J* := { j ≤ n : σ_j = σ* }` (the past terms of this class). Because `m ∈
A_n`, `m` hits every `a_j` (`j ∈ J*`); but `σ(m) ∩ σ* = ∅`, so no small prime of `m` hits any
`a_j`. Hence for each `j ∈ J*` there is a **large prime** `q_j > R` with `q_j | m` and `q_j | a_j`.

**Lemma 4 (value bound on hittable `σ*`-terms).** *In the situation above, for each `j ∈ J*` and
the associated large prime `q_j | m, q_j | a_j`, we have*
```
a_j ≤ m - q_j ≤ a_n + R - q_j.
``

*Proof.* Since `q_j | m` and `q_j | a_j`, we have `m ≡ a_j ≡ 0 (mod q_j)`, so `m - a_j` is a
positive multiple of `q_j` (positive because `m > a_n ≥ a_j`). Hence `m - a_j ≥ q_j`, giving
`a_j ≤ m - q_j`. By Lemma 2, `m < b_n ≤ a_n + R` (as `m ∈ (a_n, b_n)`), so `m ≤ a_n + R - 1 <
a_n + R`, whence `a_j ≤ m - q_j < a_n + R - q_j`, i.e. `a_j ≤ a_n + R - q_j` (integers). ∎

**Corollary 5 (the unkillable value window).** *Let `q_min(m) := min{ q : q | m, q > R }` (`m`'s
smallest large prime; it exists since `m ∉ B_n` forces at least one). Then every `σ*`-term `a_j`
with*
```
a_n + R - q_min(m) < a_j ≤ a_n
```
*is **not** divisible by any large prime of `m` (since every large prime `q` of `m` satisfies
`q ≥ q_min`, giving `a_j > a_n + R - q`, contradicting Lemma 4). Such a `σ*`-term therefore escapes
`m` entirely (`σ(m) ∩ σ* = ∅` gives no small-prime hit; no large-prime hit either), so `m ∉ A_n` —
a shortcut is impossible.*

This is the **genuine, rigorous content** the spacing mechanism extracts: a shortcut `m` missing
`σ*` is possible only if NO `σ*`-term lies in the value window `(a_n + R - q_min(m), a_n]` (whose
length is `q_min(m) - R ≥ 1`), AND every `σ*`-term of smaller value is divisible by an appropriate
large prime of `m`. The spacing fact has localized the obstruction to RECENT `σ*`-terms (within
`q_min(m) - R ≤ R` in value of `a_n`); outside that recent band, further number-theoretic
coincidences (`q_j | a_j`) are required.

---

### 6. [GAP B1' — covering sufficiency] THE HEART, UNPROVED

To close B1' one must prove, for every hypothetical shortcut `m ∈ (a_n, b_n) ∩ (A_n \ B_n)` and
every class `σ*` missed by `σ(m)`:

> **(Cov)** *At least one `σ*`-term `a_j` is NOT divisible by any large prime of `m`.*

Corollary 5 supplies (Cov) for free whenever some `σ*`-term lies in the value window
`(a_n + R - q_min(m), a_n]`. **The unproved step is the case where no `σ*`-term lies in that
window** — one must then argue from the deeper number-theoretic constraint (`q_j | a_j` with `q_j
| m`) that the older `σ*`-terms still escape.

**Why the clean value-window version fails (empirical refutation of the simple mechanism).** I
tested (Cov)-via-value-window on `a_1 ∈ {15, 35, 77, 91, 105, 135, 175, 385}`, `N = 120–300`
terms each, over all candidate/class pairs `m ∈ (a_n, b_n)` missing some `σ*`: the value-window
condition is VIOLATED in `753 – 48153` cases per `a_1` (e.g. `9927` violations at `a_1 = 15`). The
`σ*`-terms are too sparse in a window of length `q_min(m) - R` (often `1–5`) to always supply a
recent term. Moreover the value gap `a_n - a_{j*}` to the most-recent missed term reaches `747`
(`a_1 = 175`) and `763` (`a_1 = 385`), so no uniform "recent-`σ*`-term" bound closes (Cov) either.
The actual obstruction that kills each shortcut is **number-theoretic** (the specific large primes
of `m` do not divide the specific older `σ*`-terms), not capturable by spacing/density alone. This
**confirms** the round-2 outline-reviewer's coupling warning: spacing + covering, in every clean
formulation I could find, does not close B1'.

Honest assessment: I cannot prove (Cov). The crux B1' remains open. The conditional development
below shows that B1' is the ONLY obstruction to periodicity from some index `N_0` onward.

---

### 7. Conditional development: B1' ⟹ periodicity from `N_0`

Assume henceforth **B1' holds**. We derive `a_{n+T} = a_n + L` for all `n ≥ N_0` (some `N_0`,
explicit below), with `L` the kernel product.

**Lemma 6 (stabilization over `P_R`).** *`F'_n` (as a set of distinct supports) is monotone
increasing in `n` and bounded above by `2^{P_R}` (a finite set). Hence there exists an index
`N_0` with `F'_{N_0} = F'_{N_0 + 1} = ⋯`. Consequently `M'_n =: M'_∞` and `B_n =: B` are constant
for `n ≥ N_0`.*

*Proof.* `F'_n ⊆ 2^{P_R}`, `|2^{P_R}| < ∞` (since `P_R` is finite), and `F'_{n+1} = F'_n ∪
{σ_{n+1}} ⊇ F'_n`. A monotone sequence in a finite poset stabilizes: ∃ `N_0` with
`F'_{N_0} = F'_{N_0+1}`. By induction `F'` is constant for `n ≥ N_0`. `M'_n` is a function of
`F'_n` alone (minimal hitting sets of a family depend only on the family), so `M'_n` is constant
for `n ≥ N_0`; call it `M'_∞`. Then `B_n = ∪_{h ∈ M'_n} {mult of m_h}` is constant for `n ≥ N_0`;
call it `B`. ∎

**The modulus `L`.** Set `S := ∪_{h ∈ M'_∞} h ⊆ P_R` and `L := ∏_{p ∈ S} p` (squarefree; the
**kernel product**). Each `m_h` (`h ∈ M'_∞`) divides `L` (since `h ⊆ S`), so each arithmetic
progression `{mult of m_h}` is `L`-periodic; their union `B` is `L`-periodic (`B + L = B`). `L ≥ 2`
(`S` is nonempty: `M'_∞` is nonempty since a hitting set of `F'_{N_0}` always exists —
`primes(a_1) ⊆ P_R` hits every `σ_i` by the universal-small-prime lemma — and minimal ones exist by
finite descent).

> **Empirical confirmation** (Python/sympy, `a_1 ∈ {15,35,77,91,105,135,175,385}`): `L` matches the
> true period's lift exactly — `L = 30` for `a_1 = 15` (NOT `∏_{p ≤ 15} p = 30030`; the extra
> small primes `7,11,13` appear only in REDUNDANT support classes and impose no new constraint),
> `210` for `a_1 = 35, 105, 135`, `154` for `a_1 = 77`, `182` for `a_1 = 91`, `2730` for `a_1 =
> 175`. The over-counting correction (`∏∪M'_∞`, not `∏∪F'_∞`) is essential.

**Lemma 7 (seed is automatic: `a_{N_0} ∈ B`).** *Under B1', `a_{N_0} ∈ B_{N_0} = B`.*

*Proof.* By B1' applied at step `N_0 - 1` (choosing `a_{N_0}`): `a_{N_0} = min(B_{N_0-1} ∩
(a_{N_0-1}, ∞)) ∈ B_{N_0-1}`. Hence `σ(a_{N_0})` hits every `σ_i` for `i ≤ N_0 - 1`. Trivially
`σ(a_{N_0})` also hits `σ_{N_0} = σ(a_{N_0})` itself (a nonempty set meets itself; nonempty because
`a_{N_0}` carries a prime of `a_1` by the universal-small-prime lemma). Hence `σ(a_{N_0})` hits
every `σ_i` for `i ≤ N_0`, i.e. `a_{N_0} ∈ B_{N_0} = B`. ∎

This **dissolves the old sub-gap B1(b)** (round 1 carried "seed `a_N ∈ A`" as a separate concern):
under B1' the seed is free.

**Theorem 8 (periodicity from `N_0`, conditional on B1').** *Assuming B1', for `T := |B ∩ [0, L)| ≥
1` we have `a_{n + T} = a_n + L` for all `n ≥ N_0`.*

*Proof.* For `n ≥ N_0`, `B_n = B` (Lemma 6), so B1' gives `a_{n+1} = min(B ∩ (a_n, ∞)) =: f_B(a_n)`.
By Lemma 7, `a_{N_0} ∈ B`. The orbit `(a_n)_{n ≥ N_0}` is therefore the `f_B`-orbit of `a_{N_0}` in
the nonempty `L`-periodic set `B`. Apply Theorem 1 (`lemmas/periodic-set-iteration.md`): with
`x_0 = a_{N_0} ∈ B`, the orbit satisfies `x_{k+T} = x_k + L` for all `k ≥ 0`, `T = |B ∩ [0,L)|`,
single cycle, no pre-period inside `B`. Translating `k = n - N_0`: `a_{n+T} = a_n + L` for all `n ≥
N_0`. ∎

So **conditional on B1', the theorem holds from `n = N_0` onward.** The remaining gap is to reach
`n = 1`.

---

### 8. [GAP B2 — from-`n = 1`] (secondary)

Theorem 8 gives `a_{n+T} = a_n + L` for `n ≥ N_0`, but `N_0` may exceed `1` (the support family
`F'_n` genuinely grows during the first few terms; e.g. `N_0 = 3` for `a_1 = 15`, `N_0 = 7` for
`a_1 = 175`). To prove the theorem from `n = 1` one must show:

> **(B2)** *For every `n < N_0`, no integer `m ∈ (a_n, f_B(a_n))` that is admissible for `B_n`
> (but would leave the future `B`-orbit) is actually chosen by the greedy — equivalently the
> pre-period `[1, N_0)` already lies on the eventual `B`-cycle: `a_n = f_B^{n - N_0}(a_{N_0})` for
> `n < N_0` as well.*

The single-cycle property of Theorem 1 removes any pre-period INSIDE `B` (once `a_{N_0} ∈ B`), but
for `n < N_0` the governing set is `B_n ⊋ B` (stricter — `B_n ⊇ B` because `B_n` has fewer rows;
wait: `B_{n+1} ⊆ B_n` as `n` grows, so `B_n ⊇ B` for `n < N_0`), so a candidate admissible for
`B_n` need not lie in `B`. Such a "prematurely valid" candidate could, in principle, be smaller
than `f_B(a_n)` and steal the greedy — which would derail the cycle.

**Empirics** (Python/sympy, `a_1 ∈ {15, 35, 45, 77, 91, 105, 135, 175, 187, 221, 385}`): the
pre-period is EMPTY in every tested case (`a_{1+T} = a_1 + L` holds from `n = 1`); the cleanest
stubborn cases `a_1 = 187` (`T = 484`) and `a_1 = 221` (`T = 334`) still satisfy it. But no proof
exists. This is a SEPARATE gap from B1' (the round-1 `bijection-from-n1` route correctly diagnosed
it is not a corollary of injectivity or of Theorem 1). On the small lattice (post-B1') the object
is cleaner — `B_n` rather than the full `A_n` — but the mechanism is still unknown.

**[GAP B2]** remains open.

---

### 9. Summary of rigor

| Component | Status |
|---|---|
| Lemma 1 (`B_n ⊆ A_n`, so `a_{n+1} ≤ b_n`) | proved |
| Lemma 2 (`b_n ≤ a_n + R`, greedy in window) | proved (uses bounded-diff witness + universal-small-prime, imported) |
| B1' (window form / `M_n = M'_n` equivalence) | stated; **[GAP]** |
| Lemma 3 (spacing: `q > R` divides ≤ 1 window integer) | proved |
| Lemma 4 + Cor. 5 (value bound; unkillable value window) | proved (necessary condition only) |
| (Cov) covering sufficiency — the heart | **[GAP B1']**; clean value-window version empirically REFUTED |
| Lemma 6 (stabilization over `P_R`; `B` fixed, `L` kernel product) | proved (conditional on B1') |
| Lemma 7 (seed `a_{N_0} ∈ B` automatic) | proved (conditional on B1') |
| Theorem 8 (`a_{n+T} = a_n + L` for `n ≥ N_0`) | proved conditional on B1' (imports Theorem 1) |
| Trivial cases (`a_1` even; `a_1 = p^k`) | proved (round 1, imported) |
| B2 (from-`n = 1`) | **[GAP]** |

The proof is complete and rigorous for the trivial cases. For the hard case it is complete modulo
the two precisely-located gaps **[GAP B1']** (covering sufficiency) and **[GAP B2]** (from-`n = 1`),
both honestly flagged. ∎ (conditional parts marked)

## Promotable lemmas
- **Spacing fact** (Lemma 3 above): *a prime `q > R` divides at most one integer of any window of
  length `R`.* Proved in `approaches/small-prime-window-lemma.md` §4. Purely the multiplicative
  spacing of multiples; reusable by any spacing-based attack on B1'.
- **Small-prime minimum in window** (Lemma 2 above): *`b_n := min(B_n ∩ (a_n,∞)) ≤ a_n + R` for
  every `n`, witnessed by the next multiple of `R` (which is small-prime-admissible via
  `primes(a_1) ⊆ σ(M)` and universal-small-prime).* Proved in `approaches/small-prime-window-
  lemma.md` §2. Gives `a_{n+1}, b_n ∈ W_n` and localizes the B1' question to the window.
- **Value-bound / unkillable-window lemma** (Lemma 4 + Cor. 5 above): *a shortcut `m ∈ (a_n, b_n) ∩
  (A_n \ B_n)` missing `σ*` hits a `σ*`-term `a_j` via large `q` only if `a_j ≤ a_n + R - q`; hence
  all `σ*`-terms in `(a_n + R - q_min(m), a_n]` escape `m`.* Proved in
  `approaches/small-prime-window-lemma.md` §5. The rigorous content of the spacing mechanism on
  B1' (necessary condition).
