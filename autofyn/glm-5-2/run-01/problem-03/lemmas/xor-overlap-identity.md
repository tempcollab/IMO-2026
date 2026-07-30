# Lemma: XOR-overlap identity — `D = D_F + D_R − 2C` (PROPOSED, awaiting certification)

**Source.** Approach `xor-overlap` (round 5). Verified exact: 0 failures over 3000 random
refinements of `T_2,T_3,T_4,T_5` (exact `Fraction` arithmetic) and on the unsplit tower.

## Statement

Let `T_n = (2^n, 2^{n-1}, …, 2, 1)` be the dyadic tower in **tower units** (total
`D_n = 2^{n+1} − 1`). Let `M` be any refinement of `T_n` (a multiset of positive reals
summing to `D_n`), obtained as follows: the **top piece** `2^n` is split (possibly
trivially) into a multiset `F = (f_1, …, f_k)`, `k ≥ 1`, `Σ f_i = 2^n`; the **below-top
tower** `T_{n−1} = (2^{n-1}, …, 2, 1)` (total `D_{n−1} = 2^n − 1`) is refined into a
multiset `R = (r_1, …, r_\ell)`, `Σ r_j = 2^n − 1`. (When the top is unsplit, `F = {2^n}`
is a one-element list; `R` is an arbitrary refinement of `T_{n−1}`, including the unsplit
tower.) Then `M = F ⊎ R` (disjoint union as a multiset).

For a multiset `P = (p_1 ≥ p_2 ≥ … ≥ p_m)` define, as in `D-equals-parity-integral`,

$$N_P(t) \;:=\; \#\{i : p_i \ge t\}, \qquad D(P) \;=\; \int_0^\infty \bigl(N_P(t) \bmod 2\bigr)\, dt \;=\; p_1 - p_2 + p_3 - \cdots.$$

(The equality `D(P) = ∫(N_P \bmod 2)dt` is the certified lemma `D-equals-parity-integral`;
the integral is finite-support since `N_P(t) = 0` for `t > p_1`.)

Set

$$D_F \;:=\; D(F), \qquad D_R \;:=\; D(R), \qquad
C \;:=\; \int_0^\infty \bigl(N_F(t)\bmod 2\bigr)\bigl(N_R(t)\bmod 2\bigr)\,dt,$$

where `N_F, N_R` count pieces of `F`, resp. `R`, that are `≥ t`. Then

$$\boxed{\; D(M) \;=\; D_F \;+\; D_R \;-\; 2\,C. \;}$$

Equivalently, the alternating sum of the merged multiset equals the sum of the two
*standalone* alternating sums minus **twice the overlap** `C` of the two odd-parity
regions `Ω_F = {t : N_F(t) \text{ odd}}` and `Ω_R = {t : N_R(t) \text{ odd}}`
(`C = |Ω_F ∩ Ω_R|`).

## Proof

**Step 1 — the count splits.** The pieces of `M` are exactly the disjoint union of the
pieces of `F` and `R` (every fragment of `F` originated from the top piece `2^n`, every
piece of `R` from `T_{n−1}`; these sources are disjoint). Hence for every threshold `t`,

$$N_M(t) \;=\; \#\{i : m_i \ge t\} \;=\; \#\{i : f_i \ge t\} \;+\; \#\{j : r_j \ge t\}
\;=\; N_F(t) + N_R(t).$$

(Sorting `M` descending and counting how many pieces exceed `t` is identical to counting
the `F`-pieces and `R`-pieces exceeding `t` and adding — sort order does not affect a
count above a threshold.)

**Step 2 — the pointwise parity identity.** For nonnegative integers `a, b`,

$$(a + b) \bmod 2 \;=\; (a \bmod 2) + (b \bmod 2) - 2\,(a \bmod 2)(b \bmod 2). \tag{∗}$$

This is the identity `a ⊕ b = a' + b' - 2 a' b'` for `a' = a mod 2, b' = b mod 2 ∈ {0,1}`
(the parity of a sum is the XOR of the parities; in `{0,1}`, `a' ⊕ b' = a' + b' - 2a'b'`,
since both are `1` exactly when exactly one of `a', b'` is `1`). Direct check of the four
parity cases `(a mod 2, b mod 2) ∈ {(0,0),(1,0),(0,1),(1,1)}` gives `(0,0,0,0)` on both
sides — exact.

**Step 3 — integrate.** Apply `(∗)` pointwise in `t` with `a = N_F(t), b = N_R(t)`:

$$\bigl(N_M(t) \bmod 2\bigr) \;=\; \bigl(N_F(t)\bmod 2\bigr) \;+\; \bigl(N_R(t)\bmod 2\bigr) \;-\; 2\bigl(N_F(t)\bmod 2\bigr)\bigl(N_R(t)\bmod 2\bigr).$$

All three functions on the right are `{0,1}`-valued, hence bounded and nonnegative, with
finite support (contained in `[0, \max(2^n, 2^{n-1})] = [0, 2^n]` — every piece of `F` is
`< 2^n` unless the top is unsplit, in which case `N_F = 0` for `t ≥ 2^n` and the bound still
holds; every piece of `R` is `≤ 2^{n-1}`). Integrating and using linearity of the integral
(Tonelli for nonnegative simple functions — no convergence issue, finite support):

$$D(M) \;=\; \int_0^\infty (N_M \bmod 2)\,dt \;=\; \int_0^\infty (N_F \bmod 2)\,dt \;+\; \int_0^\infty (N_R \bmod 2)\,dt \;-\; 2\int_0^\infty (N_F \bmod 2)(N_R \bmod 2)\,dt.$$

By the certified lemma `D-equals-parity-integral`, the first two integrals are `D(F) = D_F`
and `D(R) = D_R` (the standalone alternating sums of `F` and `R` *considered as their own
sorted multisets* — the integral representation is intrinsic to the multiset, independent of
any merging). The third integral is `C` by definition. Hence `D(M) = D_F + D_R − 2C`. ∎

## Equivalent reformulation (union form)

Writing `Ω_F = {t : N_F(t) \text{ odd}}`, `Ω_R = {t : N_R(t) \text{ odd}}`, we have
`D_F = |Ω_F|`, `D_R = |Ω_R|`, `C = |Ω_F ∩ Ω_R|`, and `|Ω_F ∪ Ω_R| = D_F + D_R − C`. Thus

$$D(M) \;=\; 2\,|\Omega_F \cup \Omega_R| \;-\; (D_F + D_R) \;=\; 2\,|\Omega_F \cup \Omega_R| \;-\; |\Omega_F| - |\Omega_R|.$$

So `D(M) ≥ 1` is equivalent to `|Ω_F ∪ Ω_R| ≥ (D_F + D_R + 1)/2`, i.e. the two odd-parity
regions are *almost disjoint* (their overlap `C` is at most half of `D_F + D_R` minus `1/2`).

## Consistency check on the unsplit tower

Take `F = {2^n}` (top unsplit), `R = T_{n−1}` unsplit. Then `D_F = 2^n`, `D_R = D(T_{n−1})`,
and `N_F(t) = 1` for `t ∈ [0, 2^n)` (always odd), so `Ω_F = [0, 2^n)` and
`C = |Ω_R ∩ [0,2^n)| = |Ω_R| = D_R` (since `Ω_R ⊂ [0, 2^{n-1}] ⊂ [0, 2^n)`). Hence
`D(M) = 2^n + D_R − 2 D_R = 2^n − D_R = 2^n − D(T_{n−1}) = D(T_n)` (the recurrence
`D(T_n) = 2^n − D(T_{n−1})` certified in `frontier-recursion`). ✓

## Caveat

This identity is an **exact algebraic decomposition** of `D(M)`; it does **not** by itself
prove the lower bound `D(M) ≥ 1`. Closing the bound requires controlling the overlap `C`,
which (see approach `xor-overlap`) is the genuinely open step **GAP-X**, honestly equivalent
in difficulty to the lower-bound wall `G1` itself. The identity's value is structural: it
isolates `C` as a *correlation of two separately-structured parity functions* (one dyadic —
`F`'s odd region, from splitting `2^n`; one — `R`'s odd region, from refining `T_{n−1}`),
decoupled in source from the global-position-parity that drives the four converged framings.

**Depends on:** `D-equals-parity-integral` (certified). Pure algebra otherwise.
