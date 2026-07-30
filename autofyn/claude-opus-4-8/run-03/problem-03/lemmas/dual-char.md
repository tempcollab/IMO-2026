# Lemma DUAL-CHAR (box-free chain-certificate characterization) + Refutations R14a/R14b — CERTIFIED (round 14)

**Certification (round 14).** DUAL-CHAR verified by re-deriving the coefficient-matching /
telescoping identity; it is a correct structural (Farkas) characterization. R14a and R14b
independently reproduced by exact arithmetic (see verification note). Admitted as a **structural
fact + dead-mechanism record** — DUAL-CHAR is LOSS-FREE EQUIVALENT to GAP-EXTR (strong LP duality),
so it does NOT close the lower wall; its value is (i) the two forced identities that make R14a
airtight, (ii) recording the LP-dual/sparse-Farkas vehicle as dead for the LOWER wall.

## Lemma DUAL-CHAR
For a **box-free** combinatorial type `T` (a vertex with all `0 < v_i < 2^{n-1}`), a Farkas
certificate of `L_T ≥ 1` using only the group-sum equalities (E) and the descending order chain (O)
exists iff there are reals `y_g` (one per group `g`, with `rhs_F = 2^n`, `rhs_j = 2^j`) satisfying
```
  (A)  Σ_g y_g · rhs_g   = 1
  (B)  Σ_g y_g · |group g| = [m odd]
  (C)  z_k := Σ_{l≤k} ( s_l − y_{g(l)} ) ≥ 0  for all k,   s_l = (−1)^{l+1}.
```
*Proof.* On `P_T` write `L_T(v) − 1 = Σ_g y_g(eq_g − rhs_g) + Σ_{k=1}^{m-1} z_k(v_{σ(k)} −
v_{σ(k+1)})`. Matching the coefficient of the piece at position `k` gives `s_k = y_{g(k)} + z_k −
z_{k−1}` (`z_0 = z_m := 0`); the constant term gives `−1 = −Σ_g y_g rhs_g`, i.e. (A). Solving the
chain, `z_k = Σ_{l≤k}(s_l − y_{g(l)})`; the position-`m` equation telescopes to
`Σ_k s_k = Σ_g y_g|g|`, i.e. `[m odd] = Σ_g y_g|g|` = (B). Feasibility `z_k ≥ 0` is (C). ∎

## Refutation R14a (±1-equality certificate impossible) — rigorous
For the box-interior `n=4` witness `F={6,6,4}`, tail level-3 split `{3,3,2}`, sorted
`v* = {6,6,4,4,3,3,2,2,1}` (`L_T=1`, all `0<v_i<8`): by complementary slackness every certifying
dual has zero box multipliers, so DUAL-CHAR applies. The `rhs_g` are the distinct powers
`{2^0,…,2^4}`; `Σ ±2^k = 1` has the UNIQUE `±1` solution `y_F=+1, y_tail=−1` (flip subset of
`{16,8,4,2,1}` must sum to `15 = 8+4+2+1`, unique). That `y` gives `Σ y_g|g| = |F|−|B| = 3−6 = −3 ≠
[9 odd] = 1`, violating (B). Hence **no `±1`-equality certificate exists** — the outline's stated
sparse multiplier form is impossible. (The true optimal dual here is `y = e_{value-1 group}` with
four order-slacks ×1: `L_T−1 = (v_9−1) + Σ_{k∈{1,3,5,7}}(v_k−v_{k+1})` — type-specific, not
uniform.)

## Refutation R14b (odd-block collapse impossible) — rigorous
Box-free `L_T=1` vertices with `≥2` odd blocks exist: `n=4`, `F={6,6,4}`, level-3 split `{4,4}`,
sorted `{6,6,4,4,4,4,2,1}`, box-free, `L_T = 6−6+4−4+4−4+2−1 = 1`, block sizes `[2,4,1,1]` — two
odd singleton blocks `{2},{1}`. This refutes both the "≤ 1 odd block" collapse and the "odd
residual pinned to value 1" conjecture (one odd block has value 2).

## Verification note (reviewer, round 14)
Reproduced by exact integer arithmetic: `L_T(v*)=1`, `max v* = 6 < 8` ✓; the signed-power equation
`Σε_k·{16,8,4,2,1}=1` has the unique `±1` solution `(+,−,−,−,−)`; `Σ y_g|g| = +3−6 = −3 ≠ 1` ✓.
R14b: block sizes `[2,4,1,1]`, two odd blocks ✓.

**Consequence.** The LP-dual / sparse-Farkas / exchange-smoothing vehicle joins the dead LOWER
families (scalar-reserve R10, structured-matching R11, prefix/termwise monovariant R8,
f-partition-localisation R12). The Farkas dual is a loss-free reframing of GAP-EXTR with no uniform
provable multiplier pattern — retire it for the LOWER wall. GAP-EXTR (`min L_T ≥ 1` at every
vertex, ⟺ MID-core) remains the open crux, now confirmed by exhaustive computation at `n ≤ 5`.

**Scope.** Structural characterization + two dead-mechanism records. Does NOT prove GAP-EXTR.
