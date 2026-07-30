# imo-2026-06 — proof-outliner field (round 2)

Synthesis of round-2 scouts (three independent reports converge): the round-1
field's "B1 = stabilize kernel S + coincidence + seed" **collapses to ONE clean
claim, B1'**, and once B1' holds the rest is **free** (pigeonhole stabilization
of the small-prime hitting-set family over the fixed finite universe
`P_R = {primes ≤ R}`, then certified Theorem 1). The round-1 monovariant
`(|M_n|, Σ|h|, #disjoint-pairs)` is **FALSE** (non-monotone) — drop it. The
closure lemma (cross-intersecting `M_n` is stable forever) is **VALID** (stress-
tested, 0 violations) and becomes the *early-stabilization* mechanism, not
load-bearing. The König route **collapsed** into bounded-diff-finite-state; the
injectivity route is **exhausted**. Retire both.

Mechanism diversity on the crux B1' is the priority (the round-1 single-gap
trap was really a single-**mechanism** trap). The field below attacks B1' via
four distinct mechanisms: (i) window spacing/density, (ii) transversal-
minimality / matching duality, (iii) `v_p`-multiplicity size counting,
(iv) min-of-failing-set monovariant + reduce-mod-lcm (the `aimo-0678` crux
analog). Two re-advances (bounded-diff, periodic-set) carry the spacing/`v_p`
sub-mechanisms on their existing spines; two new slugs (small-prime-window-
lemma, frozen-invariant-reduce-mod-lcm) are genuinely different framings.

Certified imports (free for every approach): `lemmas/bounded-difference.md`
(`a_{n+1}-a_n ≤ R := rad(a_1)`), `lemmas/universal-small-prime.md` (every `a_n`
carries a prime of `a_1`, hence ≤ R), `lemmas/periodic-set-iteration.md`
(Theorem 1: cyclic successor on a fixed `L`-periodic set ⇒ `x_{k+T}=x_k+L`
from `k=0`, single cycle, lift exactly `L`). Trivial cases `a_1` even
(`T=1,L=2`) and `a_1=p^k` (`T=1,L=p`) are fully proved.

Notation fixed for all slugs: `R := rad(a_1)`; `P_R := {primes p ≤ R}`;
`σ_i := supp(a_i) ∩ P_R` (small-prime support); `F'_n := {σ_i : i ≤ n}`;
`M'_n :=` minimal hitting sets of `F'_n` (⊆ `2^{P_R}`, **automatically** a
finite universe); `M_n :=` minimal hitting sets of the FULL supports
`{supp(a_i) : i ≤ n}`. The crux B1' is `M_n = M'_n` for all `n` (equivalently:
no large prime `q > R` ever enters a minimal hitting set; equivalently: the
true greedy `a_{n+1}=min(A_n∩(a_n,∞))` equals the small-prime greedy
`min(B_n∩(a_n,∞))` where `B_n := ∪_{h∈M'_n}{mult of m_h}`).

---

## imo-2026-06

### small-prime-window-lemma: OPEN (new framing)
Target: the problem's actual claim — ∃ `T,L>0` with `a_{n+T}=a_n+L` for every `n≥1`.
Technique: **reframe B1 as a single window-admissibility lemma and attack it via
the spacing/density fact** (a large prime `q>R` divides ≤1 integer in any window
of length `R`, because multiples of `q` are spaced `q>R` apart). Distinct from
round-1 framings in that (a) the stabilizing object is `M'_n` over the
*definitional* finite universe `P_R` (no "is S finite?" question — it is, by
`universal-small-prime`), (b) the three sub-gaps (stabilize / seed /
coincidence) collapse to the ONE claim B1', (c) the attack mechanism is window-
density (spacing), not Bertrand (dyadic, refuted), profinite (refuted), or
injectivity (refuted).
Skeleton:
  1. **Reduction to the small-prime lattice (clean, certified machinery).**
     `A_n = ∪_{h∈M_n}{mult of m_h}` (definitional). `M'_n ⊆ 2^{P_R}` is
     automatically finite-valued; `M'_n` is a function of `F'_n` alone.
     `B_n := ∪_{h∈M'_n}{mult of m_h}` is the small-prime admissible set.
     `A_n ⊇ B_n` always (a small-prime hit is a hit). [no gap — definition +
     `universal-small-prime`.]
  2. **B1' (THE crux, spacing/density mechanism) [GAP — the heart].** Prove
     `a_{n+1} = min(B_n ∩ (a_n,∞))` for every `n`; equivalently no `m` in the
     window `W_n := (a_n, a_n+R]` lies in `A_n \ B_n`. Attack:
     (a) **Spacing fact (proved).** Every large prime `q>R` divides **at most
     one** integer of `W_n` (length `R < q`). So each large past-prime `q`
     "occupies" ≤1 slot of `W_n`. [mechanism: multiplicative spacing.]
     (b) **Admissibility of `m∈W_n` carrying large primes forces a covering.**
     If `m∈W_n` is admissible but `m∉B_n`, then `σ(m)` small-misses some
     support class `σ*∈F'_n`; let `J* := {i≤n : σ_i=σ*}`. For `m` to hit each
     `a_i` (`i∈J*`) it must use a large prime `q_i | a_i` with `q_i | m`. By
     spacing, each `q_i` divides ≤1 member of `W_n`, and `m` is one fixed
     member, so each `q_i` must divide `m` itself. Hence `m` is divisible by
     one large prime per element of `J*` — but `|J*|` past terms each carry a
     *distinct* large prime dividing `m` is impossible once `|J*|` exceeds
     `ω(m) ≤ log_2(a_n+R)` ... [GAP: the crude count goes the wrong way
     (RHS `~ log a_n`, LHS `~ n`); the builder must refine the count to the
     **last period** of class-`σ*` terms near `a_n` (a bounded, small set),
     where spacing makes each large prime of `m` hit ≤1 of them and the
     covering capacity is `≤ ω(m)` while the demand is the period length `T_*`.
     The unproved step is bounding `T_*` against `ω(m)` using `m ≤ a_n+R`.]
  3. **Stabilization (FREE once B1' holds).** `F'_n` is a growing family over
     the fixed finite set `P_R`, so `F'_n` stabilizes as a set at some `N`
     (`|F'_n| ≤ 2^{|P_R|}`). Then `M'_n =: M'_∞` is fixed for `n≥N`, hence
     `B_n =: B` is a fixed `L`-periodic set, `L = ∏_{p∈∪M'_∞} p` (the KERNEL
     product, e.g. 30 not 30030 — the over-counting correction). [no gap —
     pigeonhole/extremal over a finite universe.]
  4. **Seed is automatic (closes old B1(b) for free).** `a_N ∈ B_N = B` because
     `a_N` is admissible for `F'_{N-1}` (hits all earlier small supports, and
     trivially its own) and B1' makes admissible = small-prime-admissible. [no
     gap, given step 2.]
  5. **Periodicity (Theorem 1, certified).** Greedy = cyclic successor `f_B`
     on the fixed `L`-periodic `B` from index `N`. `lemmas/periodic-set-
     iteration.md` ⇒ `a_{n+T}=a_n+L` for `n≥N`, `T=|B∩[0,L)|`, single cycle.
     [no gap — import certified theorem.]
  6. **B2 / from-`n=1` [GAP — secondary, separate].** Extend to `n<N`: no
     "prematurely valid" small-prime candidate `m∈(a_n, f_B(a_n))` steals the
     greedy for `n<N`. Empirically always true (empty pre-period in every
     tested `a_1`); mechanism still to find. Note B2 lives on the *small*
     lattice once B1' holds — a cleaner object than round-1's B2.
Key lemmas (claim + one-line mechanism):
  - `A_n ⊇ B_n` always — because a small-prime hit is a genuine hit (`σ_i ⊆ supp(a_i)`).
  - **Spacing fact:** a prime `q>R` divides ≤1 integer in any window of length `R` — because multiples of `q` are spaced exactly `q>R` apart.
  - **`F'_n` stabilizes over `P_R`** — because `P_R` is finite (universal-small-prime) and `F'_n` is monotone; pigeonhole.
  - **B1' (the crux):** no large-prime shortcut in `W_n` — spacing makes large primes sparse in `W_n`; a covering bound on the small-missed class near `a_n` shows the demand exceeds the large-prime covering capacity. [UNPROVED.]
Open gaps: step 2 (B1', the covering-bound refinement — the heart); step 6 (B2).
Cases to cover: trivial (`a_1` even / `p^k`, already proved); singleton collapse `M'_∞={{p}}` (`T=1,L=p`); cross-intersecting `(k−1)`-subsets of a `k`-set (the hard case, `T>1`).
Watch out for: the crude covering count `|J*|` vs `ω(m)` goes the wrong way — the refinement MUST restrict to the last period of class-`σ*` terms, not all of them; do not claim `∏∪F'_∞` as the modulus (it over-counts redundant small primes — use `∏∪M'_∞`, the kernel product); do not assert the set of all primes dividing some `a_n` is finite (it is not).

### hitting-set-monovariant: REVISE (clean auto-bounded formulation; drop the false monovariant)
Target: ∃ `T,L>0` with `a_{n+T}=a_n+L` for every `n≥1`.
Technique: **combinatorial transversal theory.** The round-1 skeleton had the
RIGHT object (`M_n`) but a FALSE step-4 monovariant (`(|M_n|,Σ|h|,#disjoint-
pairs)` is non-monotone under the greedy — explorer verified on `a_1=385`:
`|M|` rises `3→9` before falling; `#disjoint-pairs` rises `3→12` on step 1).
REVISE to the clean 7-step chain: the only crux is `M_n=M'_n` (= B1'), and
stabilization is FREE once it holds (finite universe `P_R`); the closure lemma
becomes a clean *early*-stabilization shortcut, not a load-bearing monovariant.
The crux attack uses a **transversal-minimality / matching-duality** mechanism
(different from spacing): if a large prime `q>R` were essential in some minimal
transversal `g∈M_n`, the rows hit only through `q` would form a matching
deficiency in the small-prime part, contradicted by the bounded-diff witness
`R·⌈(a_n+1)/R⌉` which is small-prime-only and admissible.
Skeleton:
  1. **Definitional reduction (clean).** `A_n = ∪_{h∈M_n}{mult of m_h}`;
     `M'_n ⊆ 2^{P_R}`; `B_n := ∪_{h∈M'_n}{mult of m_h}`; `A_n ⊇ B_n`. [no gap.]
  2. **Bounded diff (import `lemmas/bounded-difference.md`).** `a_{n+1}-a_n≤R`.
     [no gap — certified.]
  3. **Cross-intersecting closure lemma (VALID — explorer stress-tested, 0
     violations over 2000 off-greedy families + 7 on-greedy).** If `M'_n` is
     pairwise cross-intersecting, then `M'_{n+1}=M'_n`: every future `σ(a_{n+1})`
     contains some `h_0∈M'_n`, and because `h_0` meets every `h'∈M'_n`, every
     `h'` still hits the new row; and no NEW minimal hitting set `g` can appear
     (it would contain some `h_g∈M'_n`, but `h_g∩h_0≠∅⊆σ(a_{n+1})` makes `h_g`
     hit the new row, strictly inside `g`, contradicting minimality). [no gap —
     load-bearing combinatorial argument, verified.] This is the
     *early-stabilization* mechanism; NOT load-bearing for the theorem
     (finite-universe backstop below suffices) but explains why `M'` freezes
     far before `F'` does.
  4. **B1' = `M_n=M'_n` (THE crux, transversal-minimality mechanism) [GAP —
     the heart].** Prove no minimal transversal of the full support family
     ever uses a large prime `q>R`. Attack (different from spacing): suppose
     `g∈M_n` contains `q>R`. By minimality, ∃ past `a_j` with
     `supp(a_j)∩(g\{q})=∅` and `q|a_j` (a row hit ONLY through `q`). The
     bounded-diff witness `W := R·⌈(a_n+1)/R⌉` is admissible AND
     small-prime-only (divisible by every prime of `a_1`). [GAP (a): show the
     existence of `W` as a small-prime hitting set forces, by a
     matching/transversal-duality argument, that every minimal transversal
     avoids large primes — i.e. the small-prime part of the support family has
     a transversal of bounded product, so no large prime is ever needed for
     minimality. The builder must formulate the duality precisely (Hall/König
     min-transversal = max-matching on the bipartite rows×primes graph, or the
     "minimal transversal of smallest product is small-prime-only" lemma) and
     bridge from "an admissible small-prime candidate exists" to "every minimal
     transversal is small-prime-only" — this bridge is the unproved step.]
  5. **Finite-universe stabilization (FREE once B1' holds).** `F'_n` over
     fixed finite `P_R` stabilizes at `N`; `M'_n=:M'_∞` fixed; `B_n=:B` is
     fixed `L`-periodic, `L=∏∪M'_∞` (kernel product). [no gap — pigeonhole.]
  6. **Seed automatic (closes B1(b) for free).** `a_N∈B`. [no gap, given B1'.]
  7. **Theorem 1 (certified).** Greedy = `f_B` from `N` ⇒ `a_{n+T}=a_n+L` for
     `n≥N`. [no gap — import `lemmas/periodic-set-iteration.md`.]
  8. **B2 / from-`n=1` [GAP — secondary].** Empty pre-period on the small
     lattice. Mechanism TBD.
Key lemmas:
  - **Cross-intersecting closure** — a new term's support contains some `h_0∈M'_n`, which meets every `h'∈M'_n`, so nothing is removed and nothing new is added (minimality contradiction). VERIFIED.
  - **`M_n=M'_n` (B1')** — because the bounded-diff witness `R·⌈(a_n+1)/R⌉` is a small-prime hitting set, so by transversal duality no large prime is ever essential for minimality. [UNPROVED — the bridge is the gap.]
  - **Stable `M'` ⇒ `a_{n+T}=a_n+L`** — Theorem 1 on `B`.
Open gaps: step 4 (B1', transversal-duality bridge); step 8 (B2).
Cases: singleton collapse `{{p}}` (terminal, `T=1,L=p`); cross-intersecting `(k−1)`-subsets (hard case); both terminal states covered by steps 3+5.
Watch out for: do NOT re-raise the false monovariant `(|M_n|,Σ|h|,#disjoint-pairs)` (non-monotone, refuted); the closure lemma is early-stabilization, NOT load-bearing — the finite-universe backstop (step 5) is what closes the theorem; the transversal-duality bridge (step 4) is the genuinely hard step and is NOT a consequence of the closure lemma.

### bounded-diff-finite-state: ADVANCE (free-rider-shortcut sub-gap via `v_p`-multiplicity counting)
Target: ∃ `T,L>0` with `a_{n+T}=a_n+L` for every `n≥1`.
Technique: keep the certified spine (bounded-diff → Lemma 3 family stabilization
→ Theorem 1) intact; replace the REFUTED Bertrand/competing-candidate attack on
the free-rider-shortcut sub-gap (= B1') with a **`v_p`-multiplicity / size
counting** argument (the König explorer's Opening C). Distinct from
`small-prime-window-lemma` in mechanism: spacing bounds the *positions* a large
prime can occupy in the window; `v_p`-counting bounds the *number of past terms*
a free-rider prime of a candidate `m∈W_n` can hit, showing it cannot cover all
the rows that `m` must hit.
Skeleton (only the changed step; rest identical to the round-1 built version):
  1–4. [unchanged, certified] bounded-diff; universal-small-prime; Lemma 3
     (`F_n` over `S_0⊆{p≤R}` stabilizes → fixed `L_0`-periodic `B` with
     `A_n⊇B`, `a_{n+1}≤min(B∩(a_n,∞))`); Theorem 1; trivial cases. [no gap.]
  5. **Free-rider-shortcut sub-gap = B1' [GAP — NEW `v_p` mechanism].** Prove
     equality in `a_{n+1} ≤ min(B∩(a_n,∞))`: no `m∈W_n:=(a_n,a_n+R]` lying in
     `A_n\B` is admissible. New attack: suppose `m∈W_n` is admissible but
     `m∉B`. Then `m` small-misses some `σ*∈F_∞`; let `J*:=\{i≤n:σ_i=σ*\}`
     (rows `m` must hit via large primes only). For each `i∈J*`, some large
     prime `q_i|R`, `q_i|m` (else `m` misses `a_i`). [GAP mechanism — the
     `v_p`-counting move:] a single large prime `q>R` of `m` can hit only the
     past terms divisible by `q`, a set that is NOT cofinal in `F_∞` (it is a
     thin slice of the support family — `q` divides at most one window integer
     by spacing, and divides past terms at most every `q>R`-th term). The
     total covering capacity of `m`'s large-prime divisors is bounded by
     `Σ_{q|m, q>R} (past terms divisible by q)`, while the demand `|J*|`
     grows with `n`. The builder must show the demand exceeds the capacity for
     large `n`, using (a) `ω(m) ≤ log_2(a_n+R)` (few large primes on `m`),
     (b) the bounded-diff constraint `m≤a_n+R` (each large prime `q|m` is
     `≤ a_n+R`, and past terms divisible by `q` are spaced `q` apart ⇒ at
     most `(a_n/q)+1 ≤ a_n/R +1` of them — but the demand `|J*|` is
     proportional to `n` while `a_n` grows roughly linearly in `n`, so the
     count is genuinely tight and may need the *last-period* refinement). [GAP
     — the count is INCONCLUSIVE in the crude form; the builder must refine.]
  6. **B2 / from-`n=1` [GAP — secondary].** Empty pre-period. Mechanism: the
     bounded-diff + Lemma-3 stabilization index `N` vs. Theorem-1 single-cycle
     property; explore whether injectivity of the reachable-residue transition
     (now well-defined once B1' holds) forces `N=1`.
Key lemmas:
  - **B1' via `v_p`-multiplicity:** a free-rider `q>R` of `m∈W_n` covers a thin, non-cofinal slice of `F_∞`; the total covering capacity of `m`'s `O(\log a_n)` large primes is eventually exceeded by the demand `|J*|`. [UNPROVED — count inconclusive in crude form.]
  - rest certified (bounded-diff, Theorem 1, Lemma 3, trivial cases).
Open gaps: step 5 (B1', `v_p`-count refinement); step 6 (B2).
Cases: even / prime-power (proved); hard odd case (the spine + step 5).
Watch out for: do NOT retry Bertrand/competing-candidate (refuted round 1); the crude `v_p` count goes the wrong way (RHS `~ n·log n/R` eventually exceeds LHS `~ n` — wrong direction for contradiction); the refinement must restrict to a bounded "last period" of class-`σ*` terms near `a_n` (where spacing makes each large prime hit ≤1, capacity `≤ω(m)`, demand `T_*`); `L=∏S` (kernel product), NOT `∏_{p≤R}p` (over-counts).

### periodic-set-iteration: ADVANCE (free-rider-shortcut sub-gap via the spacing fact)
Target: ∃ `T,L>0` with `a_{n+T}=a_n+L` for every `n≥1`.
Technique: keep the certified Theorem 1 + the decreasing-chain-of-periodic-sets
reductive frame; replace the refuted profinite-compactness bypass (Step 3,
correctly diagnosed insufficient round 1) with a direct attack on the
free-rider-shortcut sub-gap via the **spacing fact** (window-density). This is
the cleanest bolt-on for this route's existing spine.
Skeleton (only the changed step):
  1–2. [unchanged, certified] `A_n` decreasing chain of `M_n`-periodic sets,
     each a finite union of APs; `A_n≠∅` (bounded-diff). [no gap.]
  3. **DROP the profinite-compactness gamble** (refuted round 1: `Â_∞` is
     closed-not-open, need not contain a genuine integer, orbit not contained).
     Replace with the conditional reduction below.
  4. **Conditional on B1' (spacing mechanism) [GAP — the heart].** Let
     `S = ∪M'_∞ ⊆ P_R`, `L=∏S`. `A^{(S)}:=∪_{h∈M'_∞}{mult of m_h}` is
     `L`-periodic, `A^{(S)}⊆A_n` for `n≥N` (any `S`-hitting `m` hits every
     `a_i`). The danger: a free-rider candidate `m∈W_n:=(a_n,a_n+R]` in
     `A_n\A^{(S)}` smaller than `f_{A^{(S)}}(a_n)` steals the greedy. **Spacing
     attack (NEW, not Bertrand):** each large prime `q>R` divides ≤1 integer of
     `W_n` (length `R<q`). So the large-prime "shortcut threat" is *sparse* in
     `W_n`: at most one window slot per large past-prime. [GAP (a): show this
     sparsity forces `min(A_n∩W_n) = min(A^{(S)}∩W_n)` for `n≥N` — i.e. the
     small-prime candidate `f_{A^{(S)}}(a_n)≤a_n+R` is never beaten by a
     large-prime-bearing candidate in `W_n`. The explorer flagged spacing ALONE
     is insufficient (2 window integers touched at `n=40`, `a_1=15`); the
     builder must combine spacing with a covering bound on the rows a
     large-prime candidate can hit (the same last-period refinement as
     `small-prime-window-lemma` step 2(b), but phrased on the periodic-set
     chain). This is B1' in periodic-set language.] [GAP (b): B2 / from-`n=1`,
     secondary.]
  5. **Theorem 1 (certified).** Once step 4(a) holds, greedy = `f_{A^{(S)}}`
     from `N` ⇒ `a_{n+T}=a_n+L` for `n≥N`. [no gap.]
Key lemmas:
  - **Spacing fact:** `q>R` divides ≤1 integer of any length-`R` window — multiples spaced `q>R` apart.
  - **B1' (spacing + covering):** the small-prime candidate in `W_n` is never beaten by a large-prime candidate — spacing makes the large-prime threat sparse, and a covering bound (last-period of the small-missed class) shows it cannot cover the demand. [UNPROVED.]
  - Theorem 1 (certified).
Open gaps: step 4(a) (B1', spacing+covering); step 4(b) (B2).
Cases: trivial sub-cases (proved); hard case (the spine + step 4).
Watch out for: spacing ALONE is insufficient (verified: 2 window integers touched at `n=40`); do NOT re-raise profinite compactness (refuted); `L=∏S` not `∏_{p≤R}p`; this route's step 4(a) shares the covering-bound refinement with `small-prime-window-lemma` step 2(b) — the two slugs are close in mechanism on B1' (both spacing); their framings differ (periodic-set chain vs. single window-lemma) but if the spacing+covering move is refuted, BOTH die together. The reviewer should note this coupling.

### frozen-invariant-reduce-mod-lcm: OPEN (new framing, `aimo-0678` crux analog — genuinely different mechanism)
Target: ∃ `T,L>0` with `a_{n+T}=a_n+L` for every `n≥1`.
Technique: **adapt the `aimo-0678` crux move (verified in the corpus):
(1) find a frozen invariant / simplifying regime; (2) construct a
min-of-failing-set integer monovariant, prove non-increasing ⇒ boundedness of a
coordinate; (3) once bounded, reduce the OTHER coordinate mod the lcm of
attainable values ⇒ finite-state pair ⇒ eventually periodic.** This is a
DIFFERENT PROOF SHAPE from "stabilize `S` then apply Theorem 1": step (3)
arrives at periodicity via "finite pair `(coordinate, residue mod lcm)` ⇒
eventual periodicity," and the lift `L` comes from bounded-diff (the bounded
coordinate's eventual-constant increment), NOT from exhibiting the periodic
set. The crux B1' is attacked by the monovariant move (2) — bounding the
*state* directly rather than proving large primes never enter minimal
transversals. This is the field's only approach that does NOT route through
`M'_n` stabilization + Theorem 1 as its spine.
Skeleton:
  1. **Bounded coordinate (already certified).** `d_n := a_{n+1}-a_n ≤ R`
     (bounded-diff). This is the `aimo-0678` "bound `a_n`" analog — a coordinate
     is already bounded. [no gap — `lemmas/bounded-difference.md`.]
  2. **Frozen invariant / simplifying regime [GAP — needs identification].**
     `aimo-0678` used `s_n=a_n+b_n` frozen when `a_n|b_n`. Our analog: identify
     an invariant `I_n` of the greedy that is *frozen* (constant) in a
     "simplifying regime" (e.g. when the small-prime support family `F'_n` is
     stable). Candidate: `I_n = a_n mod L_*` for a candidate modulus `L_*`
     (the kernel product) — but periodicity mod `R` is FALSE (verified), so
     `L_*` must be the kernel product, which is unknown a priori. The builder
     must either (a) identify a regime where `a_{n+1}-a_n` is determined by a
     bounded "state" `s_n` (the small-prime support of the last `≤ R` terms,
     which is a finite object), making `(d_n, s_n)` a finite-state pair; or (b)
     find a genuine frozen invariant. [GAP — the genuinely hard conceptual
     step; the builder may conclude this framing does not transfer and flag it
     back.]
  3. **Min-of-failing-set monovariant [GAP — the `aimo-0678` lever for B1'].**
     `aimo-0678` defined `w_n = min{m≥a_n : m∤s_n}` and proved `w_n`
     non-increasing ⇒ `a_n` bounded. Our analog: define
     `w_n := min{m > a_n : m` is NOT small-prime-admissible (i.e.
     `m∉B_n)`}` — the first "failing" candidate. Prove `w_n` is non-increasing
     (or bounded) ⇒ the greedy `a_{n+1} < w_n` always picks a small-prime-
     admissible candidate ⇒ B1'. [GAP: the non-increasing proof. In `aimo-0678`
     it used the frozen invariant; here the mechanism must be supplied. The
     builder must test `w_n` empirically (does it stay above `a_n+R`? does it
     monovariate?) before trusting it. Honest expectation: this is the
     mechanism most likely NOT to transfer, but it is the field's only
     non-`M'_n`-stabilization attack on B1'.]
  4. **Reduce mod lcm ⇒ finite state ⇒ eventually periodic (the `aimo-0678`
     clincher, move 3).** Once the state `s_n` (small-prime support pattern of
     the recent window, or `σ(a_n)`) is bounded to a finite set of attainable
     values, let `M = lcm` of all attainable state-values. The pair
     `(s_n, a_n mod M)` takes finitely many values, and the greedy transition
     `(s_n, a_n mod M) → (s_{n+1}, a_{n+1} mod M)` is deterministic ⇒ the pair
     is eventually periodic. Then `a_n mod M` is eventually periodic, and
     bounded-diff (`d_n≤R`) forces the lift `a_{n+T}-a_n` to be a constant `L`
     among finitely many bounded values. [GAP: the transition must be
     deterministic in `(s_n, a_n mod M)` — this is EXACTLY the König-explorer's
     "finite deterministic state" requirement, which needs B1' to hold (the
     state must be the small-prime support, not the full support). So this step
     DEPENDS on step 3 succeeding; if step 3 fails, this step is circular.]
  5. **From eventual periodicity to `a_{n+T}=a_n+L` (constant lift).**
     `a_n mod M` eventually periodic (period `T`) + `d_n≤R` bounded ⇒
     `a_{n+T}-a_n` is eventually constant among `{0,R,2R,...}`-ish bounded
     values; call it `L`. [GAP: prove the lift is constant, not just
     periodic — needs the single-cycle / injectivity property, which is
     Theorem 1's content; this step may end up importing Theorem 1 anyway,
     partially collapsing the "different shape" claim. Honest flag.]
  6. **B2 / from-`n=1` [GAP — secondary].**
Key lemmas:
  - **Frozen invariant `I_n`** — constant in a simplifying regime of the greedy. [UNIDENTIFIED — the hard conceptual step.]
  - **Min-of-failing-set monovariant `w_n`** — non-increasing ⇒ the greedy always picks a small-prime-admissible candidate ⇒ B1'. [UNPROVED, possibly non-transferring — test empirically first.]
  - **Finite-state pair `(s_n, a_n mod M)` ⇒ eventually periodic** — `aimo-0678` move 3; deterministic transition on a finite set. [Depends on step 3.]
Open gaps: step 2 (frozen invariant identification); step 3 (min-of-failing-set monovariant — the B1' attack, possibly non-transferring); step 4 (deterministic finite-state transition); step 5 (constant lift); step 6 (B2).
Cases: trivial (proved elsewhere); hard case (the whole spine).
Watch out for: this is the highest-risk, highest-reward slug — the `aimo-0678` crux move (2)-(3) may simply NOT transfer to a greedy defined by "smallest admissible" rather than by gcd/lcm recurrence; the builder must test `w_n` empirically before attempting the non-increasing proof; step 4's "deterministic finite state" is the SAME obstruction the König explorer found (residue mod M does not determine the next residue without the small-prime state = B1'), so step 4 is NOT a genuine bypass of B1' — it is a different proof shape that still needs step 3 to supply B1'. If step 3 fails, RETIRE this slug; do not let it become a disguised fifth copy of the B1' wall.

### compactness-konig-branch: RETIRE (folded into bounded-diff-finite-state)
The round-2 König scout verified TWO fatal independent failures: (i) finite
branching (König) holds B1-free but "infinite path ⇒ eventually periodic"
needs a *deterministic finite* state, and the residue mod M is NOT it (same
residue `0 mod 15` yields next residue `10` vs `3` on two greedy-continued
paths); (ii) "unique infinite path" is false in the consistent-prefix tree
(≥20 children at the root, all extending to infinite paths with DIFFERENT
`(T,L)` — `(8,30)`, `(1,3)`, `(1,5)`, long transients). The one salvageable
idea — "finite state ⇒ eventually periodic via the cyclic-successor theorem" —
IS `bounded-diff-finite-state`'s conditional spine. Recommend the reviewer
CUT this slug from the population (or mark `revise-to-dead`); do NOT build it.

### bijection-from-n1: RETIRE (route exhausted)
The distinctive injectivity bypass of B1 was confirmed collapsed in round 1
(the residue transition is not well-defined until the admissible set is
periodic mod L, which IS B1). Its residual contributions — the bounded-diff
lemma, Theorem 1, trivial cases, and the diagnostic that B2 (from-`n=1`) is a
SEPARATE gap — are all recorded in `current.md` and imported by the live
slugs. Recommend the reviewer CUT this slug; do NOT rebuild.

---

## Handoff to the outline-reviewer

Field of 5 live approaches (2 new, 1 revised, 2 re-advanced) + 2 retire
recommendations. Mechanism diversity on the crux B1':

| slug | action | B1' mechanism | notes |
|---|---|---|---|
| `small-prime-window-lemma` | OPEN | spacing/density + covering on last-period class | cleanest single-claim reframing; heart is the covering-bound refinement |
| `hitting-set-monovariant` | REVISE | transversal-minimality / matching duality | drops the FALSE monovariant; closure lemma kept as early-stab shortcut; B1' attack is the duality bridge |
| `bounded-diff-finite-state` | ADVANCE | `v_p`-multiplicity / size counting | replaces refuted Bertrand; crude count inconclusive — needs last-period refinement |
| `periodic-set-iteration` | ADVANCE | spacing (window-density) | drops refuted profinite gamble; shares covering-bound with small-prime-window-lemma (coupling flagged) |
| `frozen-invariant-reduce-mod-lcm` | OPEN | `aimo-0678` monovariant + reduce-mod-lcm | highest-risk; genuinely different proof shape; may not transfer — flag to retire if step 3 fails |
| `compactness-konig-branch` | RETIRE | — | folded into bounded-diff-finite-state |
| `bijection-from-n1` | RETIRE | — | route exhausted |

B2 (from-`n=1`) is flagged as secondary in every live slug. Priority is B1'.

Suggested build set (one builder per slug, the new/revised/advanced four +
the highest-risk new slug as a probe):
`small-prime-window-lemma`, `hitting-set-monovariant`, `bounded-diff-finite-state`,
`periodic-set-iteration`, `frozen-invariant-reduce-mod-lcm`. Reviewer: please
rank, and if population budget is tight, prefer to keep mechanism diversity
(spacing / duality / `v_p` / reduce-mod-lcm) over advancing two spacing-based
slugs in parallel — if the spacing+covering move is refuted, both
`small-prime-window-lemma` and `periodic-set-iteration` die together, so
consider building ONE of them this round and probing the `v_p`/duality/reduce-
mod-lcm alternatives first.
