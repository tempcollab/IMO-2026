# Lemma: max-bound-dominant (MB-Dom) — REDUCTION (NOT a standalone certified lemma)

**REVIEWER NOTE (round 3):** This is a *conditional reduction*, NOT a standalone
certifiable lemma. Its proof depends on the Max-bound induction hypothesis `W(n−1)`
(`D* ≤ M'/2^{n−1}` for every config with max `M'`), which is the Max-bound *conjecture*
itself — proved only for the base cases `n = 0, 1, 2` and open (the crux
`a_1 < 2a_2 ∧ a_3 > a_1/2`) for `n ≥ 3`. Per the round-1 reviewer rule (never certify a
lemma as standalone if its proof depends on an unproved IH), this is REJECTED as a
standalone certifiable lemma. It is recorded here as a clean *reduction* (analogous to
the round-2 `U2`/`U3` reductions): IF the Max-bound holds at level `n−1`, THEN it holds
at level `n` for the dominant case `a_1 ≥ 2a_2`. Importers must treat the Max-bound IH as
an unproved assumption.

**Statement.** Let `L = (a_1 ≥ a_2 ≥ … ≥ a_m)` be a multiset of positive reals
summing to 1 (any `m ≥ 2`), with `a_1 ≥ 2 a_2` (the *dominant* case). Let
`M := a_1`. Assuming the Max-bound induction hypothesis `W(n−1)` — "every multiset
of total 1 with max `M'` admits ≤ `n−1` Xiang marks with `D ≤ M'/2^{n−1}`" — Xiang
has ≤ `n` marks with

$$D(\text{refined}) \;\le\; \frac{M}{2^n}.$$

**Proof.** Xiang's first mark splits `a_1` into equal halves `{a_1/2, a_1/2}`.
Since `a_1 ≥ 2 a_2`, `a_1/2 ≥ a_2 ≥ a_3 ≥ …`, so the sorted order is
`a_1/2, a_1/2, a_2, a_3, …, a_m`. The two halves sit at positions 1 (`+`) and 2
(`−`) and cancel: `+a_1/2 − a_1/2 = 0`. The rest `(a_2, …, a_m)` begins at global
position 3 (odd, `+`), same parity as its rest-local position 1, so
`D(total after mark 1) = D(rest)`. The rest has max `a_2 ≤ a_1/2 = M/2` and
`≤ n` pieces. By `W(n−1)` (piece-count-free), `D(rest) ≤ a_2/2^{n−1} ≤ (M/2)/2^{n−1}
= M/2^n`. Parity is preserved under recursive marking: the two halves (value
`a_1/2 ≥ a_2`) remain the largest pieces, so they stay at positions 1, 2 and keep
canceling (rest-fragments stay `≤ a_2 ≤ a_1/2`). Mark budget `1 + (n−1) = n`. ∎

**Base.** `n = 0`: `D(L) = a_1 + Σ_{k≥1}(a_{2k+1} − a_{2k}) ≤ a_1 = M`
(sorted-desc makes each summand `≤ 0`). So `D* ≤ M = M/2^0`. ✓. The certified
bases `n = 1` (`n1-base-both-bounds`) and `n = 2` (`n2-upper-bound-complete`) also
serve.

**Tightness.** Equality requires `a_2 = M/2` (i.e. `a_1 = 2 a_2`) AND the rest
attaining the Max-bound at level `n−1` with max `M/2`, i.e. (by induction) the
rest is the scaled tower `(M/2)·T_{n−1}`. Together: `L` is the tower `T_n` (up to
scale). So the Max-bound is tight **uniquely at the tower** in the dominant case.

**Caveat (conditional).** This is a *reduction*: it closes the dominant case at
level `n` conditional on `W(n−1)`, which itself requires the crux sub-case (see
`max-bound-pairing-small-third` and the open crux `a_3 > a_1/2`) to be resolved at
level `n−1`. The dominant case at level `n` reduces to level `n−1`; if the lower
level's rest happens to be a crux config, the reduction passes the buck. Fully
closed for the tower-attaining chain `T_n → T_{n−1} → … → T_1`.

**Importable by:** `majorization-upper` (the Max-bound dominant case), any
upper-bound approach using the Max-bound `D* ≤ M/2^n`.
