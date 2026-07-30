# Mass-balance lemma (sub-gap (ii) vacuous)

**Source:** `tail-count` §13, round 5 (from the nosaddle-close explorer's lead).

## Statement

Let `M` be a refinement of the dyadic tower `T_n = (2^n, 2^{n-1}, ..., 2, 1)` (tower units, total
`D_n = 2^{n+1} - 1`, ODD) obtained by `≤ n` marks, and suppose the top piece `2^n` has been split
(into `r ≥ 2` fragments of total mass `2^n`). Fix a combinatorial type `σ` whose open PL cell
`C_σ` satisfies the **block condition** of `telescoping-block-lemma` (c): every split's fragments
sit at positions of a single sign (all `+` or all `−`). Then on `C_σ`:

**(i) Algebraic identity.** `D = 2 S_+ - D_n`, where `S_+` is the total mass of pieces sitting at
`+` (odd-index) positions.

**(ii) Characterization of `D = 1`.** `D = 1` on `C_σ` `⟺ S_+ = (D_n + 1)/2 = 2^n` `⟺` every
fragment derived from the top piece `2^n` sits at a `+` position AND every piece derived from a
tower piece below `2^n` (split or unsplit) sits at a `−` position (the **all-top-`+` / all-below-`−`**
sign pattern of `telescoping-block-lemma` (d)).

In particular, **every block-condition cell on which `D = 1` is settled directly by
`telescoping-block-lemma` (d)** (`D = 2^n - (2^n - 1) = 1`); there are NO block-condition cells with
`D = 1` that lack the all-top-`+` / all-below-`−` pattern. This makes **sub-gap (ii) vacuous**.

## Proof

**(i)** For ANY config (block condition not needed here), let `S_+ = Σ_{i odd} a_i` be the mass at
`+` positions and `S_- = Σ_{i even} a_i` the mass at `−` positions. Then
`D = S_+ - S_-` and `S_+ + S_- = D_n` (total mass), so `D = S_+ - (D_n - S_+) = 2 S_+ - D_n`. ∎
(Pure algebra; this is the cell-level instance of the `D = ∫(N mod 2)dt` identity of
`D-equals-parity-integral`.)

**(ii)** Since `D_n = 2^{n+1} - 1` is odd, `(D_n + 1)/2 = 2^n`. By (i), `D = 1 ⟺ 2 S_+ - D_n = 1
⟺ S_+ = (D_n + 1)/2 = 2^n`. So `D = 1` on `C_σ` forces `S_+ = 2^n` exactly.

The top piece `2^n` is split into `r ≥ 2` fragments of total mass `2^n`; by the block condition
(`telescoping-block-lemma` (c)) all `r` fragments sit at positions of a single sign.

- **If all top fragments sit at `−` positions:** they contribute `0` to `S_+`. The remaining mass
  available for `+` positions is the below-top mass `2^n - 1` (the tower pieces `T_{n-1}`), so
  `S_+ ≤ 2^n - 1 < 2^n`. Hence `D = 2 S_+ - D_n ≤ 2(2^n - 1) - (2^{n+1} - 1) = -1 < 1`, in
  particular `D ≠ 1`. So this case CANNOT occur on a `D = 1` cell.

- **If all top fragments sit at `+` positions:** they contribute exactly `2^n` to `S_+`. Then
  `S_+ = 2^n + (below-top mass at +)`. For `S_+ = 2^n` we need (below-top mass at `+`) `= 0`, i.e.
  EVERY piece derived from a tower piece below `2^n` (whether unsplit, or split into fragments that
  by the block condition all share a sign) sits at a `−` position.

Combining: `D = 1` on a block-condition cell forces the **all-top-`+` / all-below-`−`** sign pattern.
By `telescoping-block-lemma` (d), this pattern gives `D = 2^n - (2^n - 1) = 1` directly on the whole
cell, with no dyadic endpoint required. ∎

## Scope and the vacuity of sub-gap (ii)

Sub-gap (ii) of `tail-count` §13 asked whether there exist block-condition cells in the min-level
set `{D = 1}` that (a) lack the all-top-`+` / all-below-`−` sign pattern AND (b) contain no dyadic
endpoint — cells undetermined by `telescoping-block-lemma` alone. This lemma shows (a) is
impossible: every block-condition cell with `D = 1` HAS the sign pattern, hence is settled by
`telescoping-block-lemma` (d). So **sub-gap (ii) is vacuous**: no such cells exist.

**Important caveat (what this lemma does NOT prove).** This lemma CHARACTERIZES the block-condition
cells on which `D = 1` (they have the pattern). It does NOT prove that `D ≥ 1` on every block-condition
cell (a block-condition cell with all top fragments at `−` would have `D ≤ -1`, but whether such a
cell exists as an open cell is not resolved here — at a strong breakpoint the tie structure tends to
force the largest fragment `≥ 2^{n-1}` to pair with the below-top piece `2^{n-1}`, but this is a
separate argument). It also does NOT address non-block-condition cells (V-shape cells, sub-gap (i)),
which remain the genuine open step of GAP-C.

## Verification (not a proof step)

Checked `Fraction`-exact on `T_3` block-condition cells: every cascade spine-3/5/7 cell with `D = 1`
has all top fragments at `+` and all below-top pieces at `−` (the interleaved order), confirming the
characterization. The V-shape cell `{4, 3, 3, 2, 2, 1}` (split `8 → 5+3`, then `5 → 4+1`): the split
of `5` produces fragments `{4, 1}` at positions `2 (−)` and `5 (+)` — opposite signs, block condition
FAILS — this is a V-shape cell, NOT a block-condition cell, and is not covered by this lemma.

**Depends on:** `telescoping-block-lemma` (block condition, part (d)), `D-equals-parity-integral`
(algebraic identity `D = 2 S_+ - D_n`).

**Importable by:** `tower-induction` (spine-level shadow), `gaps-leftover` (mass-balance as the
gaps+leftover telescoping at the cell level), `lp-dual-certificate` (the dual certificate
`y_eq = +1` on top-fragment bins, `−1` on below-top bins is the LP shadow of this sign pattern).
