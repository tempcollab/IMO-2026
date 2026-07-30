# proof-reviewer — round 1, imo-2026-06 (IMO 2026 P6)

Problem: `a_1>1`; `a_{n+1}` = smallest integer > `a_n` with `gcd(a_{n+1},a_i)>1` for EVERY `i≤n`. Prove ∃ `T,L>0` with `a_{n+T}=a_n+L` for all `n`. (`task: proof_only`, `answer_type: none`.)

I independently re-derived every "proved" step in Python/sympy and verified small cases. Summary of independent checks:
- Bounded-diff lemma `a_{n+1}-a_n ≤ rad(a_1)`: VERIFIED for `a_1 ∈ {15,35,77,135,175,187,221,6,9,25,33,45,105,385,91}`.
- Cyclic-successor theorem: proof re-derived; the consecutive-residue / wrap-case gap argument is rigorous (interval `(x,y)` of length `< L` ⇒ `z mod L` stays in the open gap between consecutive residues, disjoint from the residue set). Empirically matches `a_1=15` (`L=30, T=8`, residues `{0,6,10,12,15,18,20,24}`, greedy == `f_B` exactly, `x_{k+8}=x_k+30` from `k=0`).
- Trivial cases: VERIFIED (even `a_1` → step 2; `a_1=p^k` → step `p`).
- From-n=1 / empty pre-period: empirically TRUE for `a_1 ∈ {15,35,45,77,91}` (e.g. `a_1=35`: `L=210,T=34`; `a_1=77`: `L=154,T=18`), but UMPROVEN.
- "Periodicity mod `R=rad(a_1)` is false": VERIFIED (`a_1≡a_5≡0 mod 15` but `a_2≡3, a_6≡6 mod 15`).
- Free-rider large primes `> R` occur (`a_1=15`: 17,19,23,29,31,37) but always alongside a kernel prime.

---

## Approach 1: `bounded-diff-finite-state` — verdict: CHANGES REQUESTED (Status: partial)

**Correctness.** Every "proved" layer is valid:
- Lemma 1 (bounded-diff): the candidate `M = R·⌈(a_n+1)/R⌉` (next multiple of `R=rad(a_1)` after `a_n`) is admissible because every past `a_i` shares a prime of `a_1` with `M`. Non-circular (uses greedy rule only on past terms). VERIFIED.
- Lemma 2 (universal small prime): `n≥2` ⟹ `gcd(a_n,a_1)>1` ⟹ `a_n` shares a prime of `a_1` ⟹ that prime ≤ R. Correct.
- Lemma 3 (family stabilization): `S_0 ⊆ {primes ≤ R}` finite ⟹ `2^{S_0}` finite ⟹ `F_n` monotone stabilizes. Correct. The inclusion `A_n ⊇ B` for `n≥N` (with `B = ∩_{σ∈F} ∪_{p∈σ} pZ`, `L_0`-periodic) is correctly justified: each `supp(a_i) ⊇ σ_i ∈ F`, so `∪_{p∈supp(a_i)}pZ ⊇ ∪_{p∈σ_i}pZ`, intersecting gives `A_n ⊇ B`. Hence `a_{n+1} ≤ min(B∩(a_n,∞))` (†). Correct.
- Theorem 1 (cyclic successor): rigorous (see above).
- Trivial Cases A (`a_1` even) and B (`a_1=p^k`): correct. Case A's lower bound uses `gcd(a_n+1,a_n)=1` (consecutive-integer coprimeness) — `a_n` is a past term, so `a_n+1` fails it; upper bound `a_n+2` hits all even past terms. Case B: non-multiples of `p` in `[a_n+1,a_n+p-1]` fail to hit `a_1=p^k` (sole prime `p`); `a_n+p` hits all. VERIFIED.

**The gaps are honest and precisely the only obstructions:**
- **B1** (equality in (†) + seed `a_N∈B`): the greedy may shortcut below `min(B∩(a_n,∞))` via large primes. The approach correctly diagnoses the skeleton's competing-candidate/Bertrand mechanism as INVALID (a single-kernel-prime multiple is not universally admissible — only the `R`-multiple is, which gives Lemma 1, not B1).
- **B2** (from-n=1): stabilization index `N>1` in general; extending periodicity from `n≥N` to `n≥1` is open.
- One sharpening I flag: B1 bundles the **seed `a_N ∈ B`**, which is NOT automatic — `a_N` hits each past `a_j` via *some* shared prime, but that prime could be a large free-rider (not an `S`-prime), so `a_N` need not lie in `B`. The approach flags this (it is in the B1 hypothesis statement) but slightly under-emphasizes it; it is a genuine sub-gap, not a formality. (Empirically it holds for `a_1=15`: every term shares a prime ≤15 with all past terms.)

**Overclaim check.** Status `partial` is correct; B1/B2 are not presented as established. The invalid Bertrand sub-claim is explicitly recorded as "do not retry." Good.

**Scores.** Correctness 8/10 (proved layers all valid); Completeness 5/10 (B1+B2 open); Progress 7/10 (bounded-diff + cyclic-successor + trivial cases = substantial reusable machinery).

---

## Approach 2: `periodic-set-iteration` — verdict: CHANGES REQUESTED (Status: partial)

**Correctness.**
- Theorem 1 (Part I): rigorously proved (certified canonical). The consecutive-residue gap argument and the telescoping lift to exactly `L` are correct.
- Part II Step 1 (`A_n` decreasing chain of periodic sets, period `M_n=rad(∏_{i≤n}a_i)`): correct. `A_{n+1}⊆A_n`; membership depends only on divisibility by primes in `∪_{i≤n}supp(a_i)`, all dividing `M_n`, so `m∈A_n ⇔ m+M_n∈A_n`. Correct.
- Step 2 (nonempty, bounded-diff): correct (re-proves the shared lemma inline).
- Step 3 (profinite compactness): the setup is correct (`Â_n` clopen, decreasing, nonempty ⟹ `Â_∞≠∅` in `Ẑ` by compactness/FIP). The HONEST diagnosis that this is insufficient is the right call: `Â_∞` is closed-not-open, need not contain a genuine integer (a genuine `m∈∩A_n` would need a single prime hitting ALL `a_n`, false generically), and the orbit `(a_n)` is NOT contained in `Â_∞` (`a_n` drops out of `Â_m` for `m>n` because it need not hit future terms). This is a correct negative result — the distinctive gamble does not bypass B1.
- Step 4 (conditional on B1): `A^{(S)}⊆A_n` for `n≥N_1` is correctly argued (any `m` hitting each `s∈F_∞` via `S`-primes hits each `a_i` via that same prime). The reverse-inequality failure (free-rider shortcuts in `(a_n,a_n+R]`) is the honest sub-gap, shared with bounded-diff's B1.
- Step 5 (from-n=1): correctly flagged as a separate gap.

**Gap.** B1 (finiteness of kernel `S`) + free-rider-shortcuts sub-gap + from-n=1. The approach correctly notes `L = ∏S` (kernel product), NOT `∏_{p≤R}p` and NOT `R` — verified (a_1=15 has L=30, not 30030-with-right-period, not 15). Minor: the seed `a_N ∈ A^{(S)}` is not explicitly flagged here (it is folded into the coincidence), but it is the same sub-gap noted above.

**Overclaim check.** Status `partial` correct. The compactness gamble is honestly diagnosed as insufficient rather than overclaimed.

**Scores.** Correctness 8/10; Completeness 5/10 (B1+free-rider+from-n=1 open); Progress 7/10 (Theorem 1 + clean reduction; compactness escape correctly ruled out).

---

## Approach 3: `bijection-from-n1` — verdict: CHANGES REQUESTED (Status: partial)

**Correctness.** The proved sub-results are all valid:
- Bounded-diff lemma (section A): correct (same as above).
- Theorem 1 (section B): correct (the wrap-counter argument for "lift = L, not c·L, from k=0" is rigorous). This is the SAME theorem as the other two routes' Theorem 1 — the approach honestly says so.
- Common-prime-lock lemma (C.1): correct (if `p|a_n` for all `n`, then `a_{n+1}=a_n+p`).
- Trivial sub-cases C.2 (even) and C.3 (prime power): correct, from `n=1`.

**The route's distinctive bet collapsed (honestly).** The setup was to BYPASS B1 via an injectivity argument on residues mod L. The approach correctly self-diagnoses that this is broken: the residue transition `τ` is not well-defined until the admissible set is periodic mod L, and periodicity mod L IS B1. So the route is not genuinely distinct — it repackages the shared Theorem 1 + the shared B1 wall. Its one residual structural contribution is the diagnostic that from-n=1 (D.3: no "prematurely valid" candidate in the gap `(a_n, f(a_n))`) is a SEPARATE gap, not a free corollary of injectivity. This is a useful sharpening of B2, recorded in current.md.

**Overclaim check.** Status `partial` correct; the collapse is documented, not hidden. The approach does NOT claim to have bypassed B1.

**Scores.** Correctness 8/10 (sub-results valid); Completeness 4/10 (distinctive route collapsed; general case open on B1+B2); Progress 6/10 (shared lemmas + trivial cases + the B2 sharpening diagnostic, but no distinct mechanism).

---

## Certified lemmas

- `lemmas/bounded-difference.md` — **CERTIFIED**. Correct, non-circular, verified. Canonical.
- `lemmas/universal-small-prime.md` — **CERTIFIED**. Correct, verified.
- `lemmas/periodic-set-iteration.md` — **CERTIFIED (canonical)**. The cyclic-successor theorem, correct and verified. Designated the canonical version.
- `lemmas/cyclic-successor.md` — **DUPLICATE, marked "merge into periodic-set-iteration.md"**. Same theorem/proof, correct but redundant. Not importable as-is.
- (No standalone file for the common-prime-lock lemma or the family-stabilization lemma; both are proved inline in their approaches and correct. The bijection approach proposed `common-prime-lock` as promotable but wrote no `lemmas/` file — not admitted as a standalone lemma this round, though the statement is correct and reusable.)

## Precise B1 / B2 statement

- **B1 (kernel stabilization / coincidence).** ∃ finite prime set `S ⊇ primes(a_1)` (conjecturally `S ⊆ {p ≤ R=rad(a_1)}`), modulus `L = ∏_{p∈S} p`, index `N`, such that for all `n ≥ N`: (a) `a_{n+1} = min(A ∩ (a_n,∞))` where `A` is the fixed `L`-periodic admissible set built from the stabilized `S`-support family — equivalently, no free-rider prime `> R` yields a shortcut candidate in `(a_n, a_n+R]` lying in `A_n \ A`; AND (b) the seed `a_N ∈ A` (non-automatic: shared primes with past terms may be large free-riders, not `S`-primes). THE crux; Bertrand/competing-candidate attack shown insufficient.
- **B2 (from-n=1 / empty pre-period).** Granting B1 (periodicity from `n=N`), extend to `n ≥ 1`: for `n < N`, no "prematurely valid" candidate `m ∈ (a_n, f_A(a_n))` (valid for `A_n`, failing some future constraint) steals the greedy. Separate from B1 (injectivity does not give it for free). Empirically always true; no proof.

## Goal progress assessment

The reusable infrastructure is now solid and certified (bounded-diff, universal-small-prime, cyclic-successor theorem, trivial cases). The problem is reduced cleanly to two precisely-located gaps (B1 the coincidence/kernel stabilization; B2 the from-n=1 lift). **B1 is the genuine crux** and remains wide open — the one concrete attack (Bertrand/competing-candidate) was correctly refuted, so a genuinely new mechanism is needed. B2 is secondary (the trivial cases handle it for free; in the hard case it is a separate, sharper obstruction). Distance to solved: B1 is the wall; until a mechanism proves the greedy coincides with the cyclic successor on a fixed periodic set (or equivalently bounds the kernel primes and excludes large-prime shortcuts), the hard case stays `partial`. The profinite-compactness bypass was correctly ruled out, and the injectivity bypass collapsed into B1 — so next round needs a framing genuinely different from "stabilize then apply Theorem 1", or a direct attack on the free-rider-shortcut sub-gap with a new invariant.
