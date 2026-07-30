## Status
partial

## Approaches tried
- (round 1, new) Analytic/growth route: bound which primes can ever be load-bearing by a density + bounded-gap argument, then hand off to a periodicity endgame.
- (round 1, build) **Magnitude reduction (the productive form of the density lane).** Reduced the *entire* problem to a single clean statement — the **Structural Lemma: every two terms share a prime factor `≤ a_1`** — and proved the *whole* endgame around it rigorously (Steps 1–5 below, including periodicity and the `a_{n+T}=a_n+L` conclusion for every `n`). The magnitude flavour is genuine: only primes `≤ a_1` are ever load-bearing, so `L = ∏(small primes present)` is finite. **Verified numerically** on 20 seeds (no disjoint-color pair ever) and the endgame `(T,L)` shift + `enum==seq` confirmed for `a_1∈{15,35}`.
- (round 1, dead end recorded) **Density-on-persistent-primes fails.** The outline's mechanism "only finitely many primes divide infinitely many terms" is FALSE: e.g. for `a_1=35`, `E_∞` is periodic mod `210`, so multiples of any prime `q` (e.g. `q=37`) meet `E_∞` in a positive-density set, hence *infinitely* many primes divide infinitely many terms. Asymptotic density therefore cannot isolate the load-bearing primes. The correct crux is not "persistent" primes but the *magnitude* fact (Structural Lemma), which is a per-pair statement, not an asymptotic one.

## Current best
**The whole problem is reduced, rigorously, to one lemma.** Everything below is proved in full except the **Structural Lemma**. Given the Structural Lemma, the conclusion `a_{n+T}=a_n+L` for *every* `n` follows completely (Step 5). The isolated open gap is:

> **Structural Lemma.** For all `i<j`, `gcd(a_i,a_j)` has a prime factor `≤ a_1`. Equivalently, writing the *color* `c(a_i)=\{p\le a_1 : p\mid a_i\}`, the color family is pairwise intersecting: `c(a_i)∩c(a_j)≠∅` for all `i,j`.

This is equivalent to "no prime `> a_1` is ever load-bearing," and it is the genuine crux of P6. It is a *finite/magnitude* statement (not asymptotic), verified on 20 seeds with no counterexample.

## Target
Prove there exist positive integers `T, L` with `a_{n+T}=a_n+L` for every `n`.

## Full proof
(Not present — Status is `partial`. The complete argument modulo the Structural Lemma is written below in "Reduction"; it becomes a full proof the moment the Structural Lemma is established.)

## Reduction (complete, modulo the Structural Lemma)

Throughout, for an integer `m>1` let `π(m)` denote its set of prime divisors. Let `P_1=π(a_1)` and note every `p∈P_1` satisfies `p≤a_1`. Call a prime `p` **small** if `p≤a_1`, **large** if `p>a_1`. For a term `a_i` let its **color** be `c(a_i)=π(a_i)∩{p:p≤a_1}` (its small prime divisors). A number is **smooth** if all its prime factors are small.

Define the compatible sets
`E_n = {m≥1 : gcd(m,a_i)>1 ∀ i≤n}`, `E_∞ = {m≥1 : gcd(m,a_i)>1 ∀ i≥1}`.
By construction `a_{n+1}=min{m>a_n : m∈E_n}`.

**Step 1 (all terms pairwise non-coprime).** For `i<j`, the defining rule at the `j`-th step required `gcd(a_j,a_i)>1` (the `i≤j-1` instance). Also `gcd(a_i,a_i)=a_i>1`. Hence `gcd(a_i,a_j)>1` for all `i,j`. In particular every term lies in `E_∞`. ∎(Step 1)

**Step 2 (small prime present; colors finite).** For `n≥2`, `gcd(a_n,a_1)>1` (the `i=1` instance), so `a_n` is divisible by some `p∈P_1`, i.e. some small prime; and `a_1` is divisible by its own (small) primes. Thus every color `c(a_i)` is nonempty. Since every color is a subset of the finite set `{p prime : p≤a_1}`, there are only finitely many colors, and the set `R=⋃_i c(a_i)` of small primes that ever appear is finite. ∎(Step 2)

**Step 3 (bounded gaps `a_{n+1}-a_n≤a_1`).** Let `M` be the least multiple of `a_1` exceeding `a_n`; then `a_n<M≤a_n+a_1`. `M` is divisible by every prime of `P_1`; each earlier term `a_i` (`i≤n`) is divisible by some prime of `P_1` (Step 2), so `gcd(M,a_i)>1`. Thus `M∈E_n`, and by minimality `a_{n+1}≤M≤a_n+a_1`. ∎(Step 3)

**Step 4 (the sequence is the increasing enumeration of `E_∞` from `a_1`).** `E_∞⊆E_n` for every `n`. We have `a_{n+1}∈E_∞` (Step 1) and `a_{n+1}=min\{m>a_n:m∈E_n\}`. Suppose some `m∈E_∞` satisfied `a_n<m<a_{n+1}`; then `m∈E_n` (as `E_∞⊆E_n`) and `m>a_n`, contradicting minimality of `a_{n+1}`. Hence there is no element of `E_∞` strictly between consecutive terms. Combined with `a_1∈E_∞` and every term lying in `E_∞`, the terms are exactly the elements of `E_∞∩[a_1,∞)` listed in increasing order. ∎(Step 4)

**Step 5 (periodicity and conclusion — uses the Structural Lemma).**
Assume the Structural Lemma: the colors are pairwise intersecting. Let `𝒞={c(a_i):i≥1}` be the (finite, Step 2) family of colors, and `L=∏_{p∈R}p` (`R` finite by Step 2), a squarefree integer.

(5a) *Every color is a hitting set.* Fix a color `c∈𝒞`. By the Structural Lemma `c∩c'≠∅` for every `c'∈𝒞`; i.e. `c` meets every color.

(5b) *Smooth terms realize every color.* Fix `c∈𝒞` and let `g_c=∏_{p∈c}p` (smooth, `π(g_c)=c`). For each term `a_i`, `π(g_c)=c` meets `c(a_i)⊆π(a_i)` by (5a), so `gcd(g_c,a_i)>1`; hence `g_c∈E_∞`, and likewise `g_c^{N}∈E_∞` for every `N≥1` (same prime set). These smooth numbers are unbounded, so `E_∞` contains smooth elements of prime set exactly `c` that are `≥a_1`; by Step 4 each such element is a term. Thus for every color `c∈𝒞` there is a smooth term `b` with `π(b)=c`.

(5c) *`E_∞` is periodic mod `L`.* Put `G={m≥1 : π(m)∩c≠∅ for every c∈𝒞}`. Membership in `G` depends only on which primes of `R` divide `m`, i.e. only on `m mod L`; so `G` is a union of residue classes mod `L`, i.e. periodic mod `L`.
 - `G⊆E_∞`: if `m∈G` then `π(m)` meets `c(a_i)⊆π(a_i)` for every `i`, so `gcd(m,a_i)>1`, i.e. `m∈E_∞`.
 - `E_∞⊆G`: let `m∈E_∞` and `c∈𝒞`. By (5b) there is a smooth term `b` with `π(b)=c`; since `m∈E_∞`, `gcd(m,b)>1`, and `π(b)=c`, so `π(m)∩c≠∅`. Thus `m∈G`.
 Hence `E_∞=G` is periodic mod `L`.

(5d) *Enumeration of a periodic set.* Let `T=\#\{r∈[a_1,a_1+L) : r∈E_∞\}` be the number of residues per period (`0<T`, since e.g. every multiple of `a_1` lies in `E_∞`, and `T≤L`). Because `E_∞` is periodic mod `L`, every half-open interval of length `L` contains exactly `T` elements of `E_∞`. Let `e_1<e_2<⋯` enumerate `E_∞∩[a_1,∞)` (these are the terms, Step 4, with `e_n=a_n`). For each `n`, the interval `[e_n,e_n+L)` contains exactly `T` elements of `E_∞`, namely `e_n,e_{n+1},…,e_{n+T-1}`; moreover `e_n+L∈E_∞` (periodicity) and it is the smallest element of `E_∞` that is `≥e_n+L`, hence `e_{n+T}=e_n+L`. Therefore
`a_{n+T}=a_n+L` for every `n≥1`,
with the positive integers `T` and `L` just defined. ∎(Step 5, modulo the Structural Lemma)

## The open gap: the Structural Lemma

**Statement.** For all `i<j`, `gcd(a_i,a_j)` has a prime factor `≤a_1`; equivalently the colors are pairwise intersecting.

**What is proven around it.** Steps 1–4 and Step 5 are complete and rigorous. By Step 1 any two terms *do* share a prime; the Lemma asserts one such shared prime is small. Because a smooth term can only be met through a small prime, any two terms one of which is smooth already share a small prime (immediate). The difficulty is the case where *both* terms carry large primes (e.g. `a_1=35`: `370=2·5·37`, `555=3·5·37` — they share the large prime `37`, yet also the small prime `5`; the Lemma is that the small coincidence is never optional).

**Why the naive density attack does not reach it (recorded dead end).** Density is asymptotic, but the Structural Lemma is a *per-pair* statement; a single disjoint-color pair would not violate any density bound. Moreover infinitely many primes divide infinitely many terms (`E_∞` periodic ⇒ each prime meets it in positive density), so "persistent primes are finite" is false. The correct crux is the magnitude statement above, not a counting statement.

**Numerical status.** No disjoint-color pair occurs for `a_1∈{15,21,35,45,55,65,77,85,91,105,115,119,133,143,165,187,209,215,221,247}` (hundreds of terms each). The reduction's `(T,L)` (with `L=∏(small primes present)`) was verified to satisfy `a_{n+T}=a_n+L` and to reproduce the sequence exactly for `a_1∈{15,35}` (e.g. `a_1=15`: `L=30030`, `T=8008` — a valid, non-minimal period, which is all the problem requires).

## Promotable lemmas
- **All terms pairwise non-coprime (Step 1).** For all `i,j`, `gcd(a_i,a_j)>1`; hence every term lies in `E_∞`. Fully proved.
- **Every term has a prime factor `≤a_1` (Step 2).** From the `i=1` instance of the rule. Fully proved; gives finiteness of the color set.
- **Bounded gaps (Step 3).** `a_{n+1}-a_n≤a_1`. Fully proved.
- **Enumeration lemma (Step 4).** The sequence equals the increasing enumeration of `E_∞∩[a_1,∞)`; hence periodicity of `E_∞` (mod any `L`) yields `a_{n+T}=a_n+L` for every `n` with `T=\#(E_∞ mod L)`. Fully proved.
- **Periodicity from pairwise-intersecting colors (Step 5).** If the colors are pairwise intersecting then `E_∞={m:π(m)` hits every color`}` is periodic mod `L=∏R`, and the conclusion follows. Fully proved (conditional on its hypothesis, the Structural Lemma).
