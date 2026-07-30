# Proof review — imo-2026-06, round 1

Reviewed three built approaches. All independent computational claims re-verified by me from
scratch in Python (see snippets below); no theorem/lemma statement was taken on trust.

---

## 1. `growth-bound-density.md`

**Claimed Status:** partial. **Confirmed Status: partial.**

- **Lemma 1 (Gap bound, $a_{n+1}-a_n\le L_0=\mathrm{rad}(a_1)$):** Re-derived from scratch
  independently. Correct. Step 1 (every $a_i$ shares a prime with $a_1$, directly from the $i=1$
  instance of the recursive constraint) is valid; Step 2 (the next multiple of $L_0$ above $a_n$ is
  always a valid candidate) is valid; Step 3 (minimality of $a_{n+1}$) closes it. No gap.
- **Lemma 3 (Constraint Domination):** One-line divisibility argument, correct, no gap.
- **Diagnosis that $S=\mathrm{primes}(a_1)$ is too coarse ($a_1=15$, prime 2 load-bearing for
  $a_3=20$):** I reproduced this by direct simulation — confirmed exactly ($a_2=18$, $a_3=20$,
  witness prime 2 ∉ primes(15)).
- **Refutation of "enlarge $S$ to eventually-active primes":** I reproduced this computationally
  for $a_1=15$ out to 3000 terms: the gap sequence is periodic (period 8, sum $L=30$) from index 2
  on, and primes 7,11,...,101 each divide hundreds of terms — confirmed exactly as claimed.
- **Remaining gap** ("antichain stabilizes" / "large primes never the unique witness"): correctly
  and honestly stated as open, with two named partial attempts (magnitude bound, density) that are
  each shown, correctly, not to close it. No overclaiming; Status `partial` is accurate.

**Verdict: CHANGES REQUESTED.** Real, certifiable progress (two lemmas below), but the theorem is
not proved. Exact gap to close next: show the inclusion-minimal antichain of $P$-signatures is
finite-state / show large primes never become the *unique* (non-redundant) witness for validity in
the guaranteed window — this is the same wall identified in the other two files (see cross-cutting
note below).

---

## 2. `core-signature-pigeonhole.md`

**Claimed Status:** partial. **Confirmed Status: partial** (this is the furthest, most complete
reduction in the population).

Checked every lemma:
- Lemma 1 (core-hitting): correct, same argument as above.
- Lemma 2 (growth bound): correct, identical content to growth-bound-density's Lemma 1.
- The fix $P=\{\text{primes}\le L_0\}$: valid, $P$ finite and $\supseteq S$ by construction
  ($p\in S\Rightarrow p\le\mathrm{rad}(a_1)=L_0$).
- Lemma 3 (signature stabilization): the chain $R_n=\{D_1,\ldots,D_n\}$ is monotone non-decreasing
  in a finite universe $2^P\setminus\{\emptyset\}$, so it stabilizes — valid pigeonhole argument, no
  gap.
- Lemma 4 (CRT reduction, $G\ne\emptyset$ via $0\in G$): valid; CRT usage is correct (primes of $P$
  pairwise coprime, so residue mod $L_P=\prod P$ determines residues mod each $p\in P$
  simultaneously).
- Lemma 5 (sufficiency): valid, follows cleanly from Lemma 3+4.
- The one-directional bound $a_{n+1}\le y_{n+1}$: correctly derived.
- **Lemma 6 (No-Escape) — the crux, correctly flagged as open.** The equivalence "$a_{n+1}=y_{n+1}$
  for $n\ge N_1$ $\iff$ no escape ever occurs" is itself proved (it's a tautological unpacking of
  what "not achieving the minimum via $G$" means), but the substantive claim (no escape ever
  occurs) is NOT proved — only checked computationally (25 values of $a_1$, 100–200 terms each, in
  the builder's own log; I independently re-ran a similar check on 8 values out to 1500 terms and
  found zero escapes too — see script below). The three "partial attempt" write-ups (magnitude
  bound, density, "eventually always" strengthening) are honest, correctly self-diagnosed as
  insufficient, and not further exploitable as written.
- Lemma 7 + Conclusion (periodicity given No-Escape): I checked the pigeonhole-on-residues argument
  (finite $G$, deterministic map $f$, eventual cycle) — correct. The "extend from eventually to all
  $n$" bookkeeping (choosing $T'=TN$) is a bit informally written ("routine... fiddly") but I traced
  it through and it is in fact mechanically valid — every index $<N$ reaches an index $\ge N$ after
  finitely many steps of size $T$, and the accounting closes. This is legitimate, not hand-waving
  hiding a real gap (it is finite case-checking, correctly summarized rather than spelled out digit
  by digit, which is acceptable for a mechanical index-shift argument, not a substantive claim).

**Verdict: CHANGES REQUESTED.** This is the strongest reduction in the field: the entire theorem is
reduced to one crisply-stated open lemma (No-Escape). Not solved — Status `partial` is correct, not
an overclaim. Exact gap: prove No-Escape for $P=\{\text{primes}\le\mathrm{rad}(a_1)\}$ (or find the
right, possibly larger/different, finite $P$ for which it's provable).

---

## 3. `monovariant-telescoping.md`

**Claimed Status:** partial. **My finding: the framing's stated target is FALSE, so I am
downgrading part of the assessment — the two proved lemmas are correct and certified, but the
approach's own "central open gap" ($|Q|<\infty$) is not just hard, it is refuted.**

I verified this by direct simulation (script below), independent of the builder's own numbers:

```
a1=15, seq to 3000 terms: gap-sequence periodic from index 2, period 8, sum L=30.
Counts of terms divisible by p among first 3000: p=7→429, p=11→272, p=13→231, ..., p=101→30.
a1=21, seq to 3000 terms: EVERY term is a multiple of 3, and prime counts: p=2→1500 (50%),
p=7→429, p=11→273, ..., p=53→56 — every prime tested divides hundreds of terms.
```

This directly **contradicts** the approach file's own reported empirical claims — "$Q=\{2,3\}$ for
$a_1=15$" and "$Q=\{3\}$ for $a_1=21$" — which are factually wrong; the true $Q$ for both cases
contains (empirically, up to the primes tested) essentially every prime. This is not a computation
error on the margins; it's off by an entire qualitative category (finite small set vs. cofinite).

More importantly, this is **provable in general, not just empirically observed**: once the
difference sequence is eventually periodic with total shift $L$ over period $T$ (which is exactly
what the theorem asserts), then for any prime $p\nmid L$, the arithmetic progression $a_n+kL$
($k=0,1,2,\dots$) cycles through every residue class mod $p$ (since $\gcd(L,p)=1$), hence hits
$0\bmod p$ infinitely often — so $p\in Q$ automatically. Hence $Q$ is cofinite in the primes (its
complement is contained in the divisors of $L$), i.e. **$|Q|=\infty$ whenever the theorem's own
conclusion holds.** So "$|Q|<\infty$" is not an open lemma en route to the theorem — it is
inconsistent with the theorem itself. Chasing it is chasing a dead end no matter how it's attacked.
(The builder's file does, to its credit, honestly report three failed attack routes and does not
overclaim a proof — the `partial` self-assessment for *those specific lemmas* is fine, but the
framing's headline target cannot be salvaged as stated.)

The two proved lemmas (Q-cover: every term has a prime factor in $Q$; density:
$\sum_{q\in Q}1/q\ge1/L_0$) are independently correct — I re-checked both proofs line by line (the
finite-maximum contradiction for Q-cover, and the union-bound + linear-growth-corollary combination
for the density inequality) and found no gap. They are certified as standalone facts (see
`lemmas/q-cover-and-density.md`), but they do not, and now provably cannot, be extended to
$|Q|<\infty$.

**Verdict: RETHINK.** The approach's central open gap is not "hard," it is false; the framing
(track $Q$ = all recurring primes, hope it's finite) must be abandoned. The two certified lemmas
survive as general facts any future approach may cite, but a fundamentally different finite
invariant is needed if this line is revived (e.g. tracking only primes that recur *and* are ≤ a
fixed bound tied to the gap-bound $L_0$ — which is exactly what `core-signature-pigeonhole`
already does under the name $P$).

---

## Cross-cutting diagnosis (the key structural finding this round)

The dispatch asked whether the three "No-Escape / antichain-stabilization / $|Q|<\infty$" gaps are
the same obstruction restated three ways. **Yes, with one twist:**

- `growth-bound-density`'s gap ("large prime factors of $a_i$ never become the unique witness for a
  live constraint") and `core-signature-pigeonhole`'s No-Escape ("no candidate below the CRT-target
  is ever valid via a prime outside $P$") are **literally the same claim**, just phrased over
  slightly different finite prime sets ($S$-derived antichain vs. $P=\{\text{primes}\le L_0\}$).
- `monovariant-telescoping`'s $|Q|<\infty$ looked like a third independent angle, but I showed it is
  actually **not equivalent** to the other two — it is a strictly stronger and, in fact, **false**
  claim (recurrence at all, vs. recurrence as a *necessary, unique* witness). The correct lesson:
  the invariant to bound is "does a large prime ever become *necessary* for validity," never "does
  a large prime ever divide infinitely many terms" (the latter is true and unavoidable for a
  cofinite set of primes once the sequence is eventually periodic at all). This is a genuine new
  piece of information for the next round: **any new framing must be phrased in terms of necessity/
  uniqueness of witnesses in a bounded window, not in terms of which primes recur.**

Given that three independent framings (constraint domination, CRT-sufficiency/No-Escape, and
recurring-primes) all either hit the identical necessity-of-witness wall or provably cannot work,
next round's outliner should be told explicitly: don't just patch the current $P$/No-Escape
machinery (a 4th variation on the same idea will hit the same wall). A genuinely different
mechanism is needed to bound how far back a "witness debt" can persist — e.g. a direct argument
that within any window of length $L_0$ (or $L_P$), a term with a given signature must recur before
any single leftover unmatched constraint's minimal witness could be forced above $P$; or an
entirely different global monovariant not based on primes recurring but on, e.g., a potential
function measuring "constraint slack" that is proven to decrease/bound the possible escape events
by a counting argument (not density).

---

## Lemmas certified

Written to `results/imo-2026-06/lemmas/`:
- `gap-bound.md` — $a_{n+1}-a_n\le\mathrm{rad}(a_1)$ (+ linear growth corollary). Certified.
- `constraint-domination.md` — redundant-constraint lemma. Certified.
- `signature-stabilization-and-crt-sufficiency.md` — generic (any finite $P\supseteq
  \mathrm{primes}(a_1)$) signature stabilization + CRT sufficiency, with an explicit note that it
  gives only $a_{n+1}\le y_{n+1}$, not equality. Certified.
- `periodicity-given-no-escape.md` — conditional lemma "No-Escape (for some finite $P$) $\Rightarrow$
  full periodicity for all $n$." Certified as a conditional implication only; explicitly flagged
  that its hypothesis is the open crux.
- `q-cover-and-density.md` — Q-cover and density-inequality lemmas, certified as standalone facts,
  with a prominent caveat (added by the reviewer) that $|Q|<\infty$ is false and should not be
  pursued.

---

## Verdicts

- `growth-bound-density`: **CHANGES REQUESTED** (Status: partial — real lemmas certified, antichain-
  stabilization gap open, correctly self-reported, not overclaimed).
- `core-signature-pigeonhole`: **CHANGES REQUESTED** (Status: partial — furthest reduction in the
  field, reduces the whole theorem to the single No-Escape lemma, correctly self-reported, not
  overclaimed).
- `monovariant-telescoping`: **RETHINK** (Status: unsolved as a route to the theorem — its two
  lemmas are correct and certified, but its central target $|Q|<\infty$ is refuted, not merely
  unproven; the framing cannot be salvaged as set up and should not be advanced next round without
  a different finite invariant).
