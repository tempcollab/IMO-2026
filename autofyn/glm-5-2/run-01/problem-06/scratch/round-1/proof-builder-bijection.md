# proof-builder — bijection-from-n1 (round 1)

## What proved
- **Bounded-difference lemma** (clean, non-circular): `a_{n+1} − a_n ≤ rad(a_1)` for all `n`. Proof: next multiple of `rad(a_1)` after `a_n` is divisible by every prime of `a_1`, hence hits every past term; verified numerically (a_1 ∈ {15,35,77,135,175,187,221}).
- **Theorem 1 (periodic-set single cycle)** — the route's intended injectivity/bijection/single-cycle/lift=L mechanism, isolated and proven in full: iterating `f(x)=min(A∩(x,+∞))` on a nonempty `L`-periodic set `A` gives `x_{k+t}=x_k+L` for **every** `k ≥ 0` (no transient) with `t=|A mod L|`; the residue map is the cyclic successor, a single `t`-cycle (hence injective). This is the shared final-step lemma for bounded-diff-finite-state / hitting-set-monovariant / periodic-set-iteration.
- **Two unconditional trivial sub-cases (solved end-to-end, from n=1):**
  - `a_1` even ⟹ `T=1, L=2` (induction + consecutive-integer coprimeness `gcd(k,k+1)=1` kills `a_n+1`; `a_n+2` is the valid even successor).
  - `a_1 = p^k` prime power ⟹ `T=1, L=p` (hitting `p^k` forces `p | a_n` for all `n`; common-prime lock).
  - Plus a common-prime-lock lemma: if a prime `p | a_n` for all `n`, then `a_{n+1}=a_n+p`.

## Exact gaps (the general case — odd a_1 with ≥2 prime factors)
- **[GAP: B1 — kernel stabilization]** The admissible set `A_n = {m : gcd(m,a_i)>1 ∀ i≤n}` stabilizes to a fixed `L`-periodic set `A` with `L = ∏S`, finite kernel `S ⊇ primes(a_1)` (conjecturally `S ⊆ {p ≤ rad(a_1)}`). Unproven; shared with every other route. Verified that periodicity mod `rad(a_1)` is FALSE (a_1=15: a_1≡a_5≡0 mod 15 but a_2≡3, a_6≡6 — different successors), so the modulus must be the kernel product L, which is exactly what B1 must supply. The "transition on residues mod L" is not even well-defined until B1 holds — so the route's injectivity crux cannot bypass B1.
- **[GAP: from-n=1 consistency]** Even given B1 (so `A_n = A` for `n ≥ N`), the greedy's choices for `n < N` must coincide with the eventual cycle: no "premature valid candidate" `m ∈ (a_n, cyclic_successor_A(a_n))` may lie in `A_n`. This is the route's intended "free" payoff; it is NOT free — it is an additional gap. Theorem 1 only yields from-n=N (eventual), not from-n=1.

## Self-assessed status
**partial.** Two unconditional solved sub-cases; two clean promotable lemmas (bounded-difference, periodic-set-single-cycle, common-prime-lock); the general case blocked by B1 and the from-n=1 consistency gap.

## Distinctiveness verdict (sustains outline-reviewer's warning)
The injectivity crux **reduces to Theorem 1**, which is the same "lift=L / from-the-start" mechanism periodic-set-iteration isolates as its Theorem 1 and bounded-diff-finite-state uses for its final steps. The route is therefore **not genuinely distinct** in mechanism: it repackages the shared final-step theorem plus the shared B1 wall. Useful residual structural observation: the from-n=1 surprise is a *separate* gap (D.3), not a free corollary of injectivity — a diagnostic, not a proof.

## Certified/shared lemmas produced
- `bounded-difference` (Lemma A in the approach file) — proposed for `lemmas/`.
- `periodic-set-single-cycle` (Theorem 1 / section B) — proposed for `lemmas/`; this is the shared final-step theorem the outline-reviewer asked to be certified.
- `common-prime-lock` (section C.1) — proposed for `lemmas/`.
