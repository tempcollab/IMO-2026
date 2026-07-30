# Lemma U0 (even-multiplicity corrector) — CERTIFIED (round 6, proof-reviewer)

**Certification note (reviewer, round 6).** (a) is a direct consequence of the certified measure
identity: $N_S(t)$ is a sum of even multiplicities off a finite value-set, hence even a.e., so
$\mu\{N_S\text{ odd}\}=0$. (b) bisect-all makes every final value even-multiplicity, and needs
budget $\ge m$ (the "simultaneous, not sequential" caveat is essential — sequential bisection is
refuted). (c) follows. Self-contained on certified M (and P for the strategic wrapper). All three
parts hold as stated; no overclaim.


Source approach: `parity-measure-potential`. Uses only certified Lemma M (parity–measure
identity, `lemmas/measure-identity.md`) and Lemma P (cancelling pair, `lemmas/cancelling-pair.md`).
Imported by `smoothing-majorization` (regime-(i) base) and `breakpoint-vertex` (§4B); it reduces
the upper bound `UB(n)` to the single full-budget case `m = n+1`.

Throughout, for a finite multiset `S` of positive reals sorted descending `b_1 ≥ b_2 ≥ …`,
`D(S) := Σ_i (−1)^{i+1} b_i`, and `N_S(t) := #{pieces of S that are > t}`. Lemma M states
`D(S) = μ{ t > 0 : N_S(t) odd }` (Lebesgue measure). `u_n := 1/(2^{n+1}−1)`.

---

## Lemma U0(a) [even multiplicity ⇒ D = 0]

**Statement.** Let `S` be a finite multiset of positive reals in which every distinct value has
even multiplicity. Then `D(S) = 0`.

**Proof.** Let the distinct values of `S` be `v_1 > v_2 > … > v_r`, with multiplicities
`m_1, …, m_r`, each `m_j` even. Fix `t > 0` with `t ∉ {v_1, …, v_r}`. The pieces exceeding `t`
are exactly the copies of those `v_j` with `v_j > t`, so
```
        N_S(t) = Σ_{ j : v_j > t } m_j .
```
Each `m_j` is even, hence this sum is even, i.e. `N_S(t)` is even for every `t` outside the finite
(hence measure-zero) set `{v_1, …, v_r}`. Therefore `{ t > 0 : N_S(t) odd }` is contained in a
measure-zero set, so `μ{ t : N_S(t) odd } = 0`. By Lemma M, `D(S) = 0`. ∎

(This is exactly the certified Corollary of Lemma M, isolated as a named lemma so the strategic
consequence (b) can cite it directly. Numerically re-checked round 6: 5/5 random even-multiplicity
multisets give `D = 0` exactly.)

---

## Lemma U0(b) [bisect-all: m ≤ budget ⇒ Xiang forces D = 0]

**Statement.** Let `A = {a_1, …, a_m}` be any multiset of `m` positive pieces with total `L`, and
suppose the cutting budget is `≥ m`. Then by making exactly `m` cuts Xiang can force the final
multiset `F` to satisfy `D(F) = 0`. In particular, whenever `m ≤ n`, `D(F) = 0 ≤ u_n L`.

**Proof.** Xiang bisects every piece: for each `i = 1, …, m` he applies the single cut
`a_i → (a_i/2, a_i/2)`. This is `m` cuts, within the budget `≥ m`. The resulting multiset is
```
        F = { a_i/2 (twice) : i = 1, …, m } .
```
Every value `w` occurring in `F` has the form `a_i/2` for one or more indices `i`; its multiplicity
in `F` is `2 · #{ i : a_i/2 = w }`, which is even. By Lemma U0(a), `D(F) = 0`. Since `u_n L ≥ 0`,
the stated bound `D(F) = 0 ≤ u_n L` holds. ∎

---

## Corollary U0(c) [upper bound reduces to full budget m = n+1]

**Statement.** In the master problem (Liu presents `m` pieces of total `L = 1` with `m ≤ n+1`,
Xiang has `≤ n` cuts, target `D ≤ u_n`), every profile with `m ≤ n` pieces is disposed of with
`D = 0`. Hence the upper bound `UB(n)` is nontrivial only for profiles with exactly `m = n+1`
pieces.

**Proof.** If `m ≤ n`, apply Lemma U0(b) with budget `n ≥ m` to get `D = 0 ≤ u_n`. The only
remaining case is `m = n+1`. ∎

**Remark (why simultaneous, not sequential).** U0(b) bisects all `m` pieces in one shot; this is
NOT sequential/cascading single-piece bisection, which is a refuted rule (it overshoots the target
by `4.7×` on the near-uniform `n = 5` profile `(0.2024, 0.1965, 0.1820, 0.1789, 0.1651, 0.0750)`).
U0(b) is immune because simultaneous bisection makes every final value have even multiplicity, and
it only claims `D = 0` when the budget actually suffices to double every piece (`budget ≥ m`).

**Certification note.** Self-contained given certified Lemmas M and P (only M is used in the
proofs above; P is listed as a dependency of the surrounding peel machinery, not of U0 itself).
Numerically re-verified round 6.
