# Proof-reviewer — round 5 (imo-2026-06)

Three built approaches, reviewed independently. No solve flip. Two rigorous advances (both
certified), one modest-but-honest new framing. Substantive crux unbroken.

---

## 1. covering-small-part-descent — VERDICT: CHANGES REQUESTED (Status: partial)

**Scores.** Correctness 10/10 · Rigor 10/10 · Progress 6/10.

**Load-bearing step re-derived independently.** Lemma 6 (bad-signature geometric family): if `m` is
bad then `m·r^k` (`r∣m`, `k≥0`) is a bad term with `S(m·r^k)=S(m)` and the same witness. I re-derived
this from scratch:
- `m` term ⇒ `primes(m)` covering (certified `realizability-...` Lemma 1, 𝒯⊆𝒞). ✓
- `r∣m` ⇒ `primes(m·r^k)=primes(m)` (no new prime) — covering; `m·r^k ≥ m ≥ a_1`. By Realizability
  clause (c) ("every integer ≥a_1 whose prime set contains a covering set is a term") `m·r^k` is a
  term. I independently confirmed clause (c) is itself correct: `primes(n)⊇S` covering ⇒ `primes(n)`
  meets every color ⇒ `n∈E_∞`, and `n≥a_1` ⇒ term by ENUM. ✓
- `S(m·r^k)=primes(m)∩[2,P_max]=S(m)` non-covering, same witness `B`
  (`primes(B)∩S(m·r^k)=primes(B)∩S(m)=∅`) ⇒ bad. `r≥2` ⇒ strictly increasing. ✓
- Computationally verified (a_1∈{15,35,231}, 400 terms): `m·r` is always a term. ✓

No hidden gap, no circularity, no `a_1∣m·r^k` trap (a bad term misses a prime of P, so `primes(m·r^k)
=primes(m)⊉P` ⇒ off-lattice, consistent with GPC). **Lemma 6 is CORRECT and CLOSES sub-step (6a).**

**Honest caveat (not a flaw, but bounds the progress).** The family Lemma 6 produces is a single
fixed-signature orbit with one fixed witness (density →0). This is exactly the object the certified
Σ1/p² capacity count already cannot exploit. So (6a) is genuinely closed, but the substantive crux
**(6b)** — a value-level contradiction — is entirely untouched. Arguably (6a) was the easier half of
the round-4 decomposition (near-immediate from the certified Realizability "infinitely many
realizers"). Progress is real and rigorous but does not move the field toward a solve.

**Recorded Status accurate** (builder marked partial, not overclaimed). Gap for next round: (6b).

**Certified:** Lemma 6 → `lemmas/bad-signature-geometric-family.md`.
(Promotable #1 "(CSP)⇒theorem self-contained reduction" duplicates certified `csp-implies-theorem.md`;
#3 bad-partner duplicates `bad-partner-and-ascent.md` — no new certification.)

---

## 2. bad-residue-witness-index — VERDICT: CHANGES REQUESTED (Status: partial)

**Scores.** Correctness 10/10 · Rigor 9/10 · Progress 7/10.

**Load-bearing step re-derived: the Reduction Lemma (FIN-W)⟹theorem.** I checked the three-case
residue-determination end to end and it holds:
- Q_rel finite under (FIN-W): W(r) finite (hyp) × Q_i finite × R'_bad finite (≤L_0) ⇒ finite. ✓
- `M=L_0·∏Q_rel`; `m∈E_∞` is a function of `m mod M`:
  - r covering ⇒ `m∈E_∞` always (S(r) meets every color, S(r)⊆primes(m)). ✓
  - r∈R'_bad ⇒ via (★) `m∈E_∞ ⟺ ∀i∈W(r) ∃q∈Q_i: q∣m`; every such `q∈Q_i⊆Q_rel∣M`, and W(r),Q_i
    depend on `r=m mod L_0∣M`, so determined by `m mod M`. ✓
  - r∈R_bad, class missed ⇒ constantly false (if any `m≡r` satisfied (★) the class would be met, so
    this is exactly the complement within R_bad). ✓ (the consistency check is legitimate.)
- ⇒ E_∞ tail-periodic mod M; PER+ENUM ⇒ `a_{n+T}=a_n+M`. ✓

No circularity: (FIN-W) is the hypothesis, not smuggled. This **genuinely weakens the crux**:
(CSP)⟹(FIN-W)⟹theorem, and (FIN-W) is strictly weaker (it permits bad terms with finitely many
witnesses each). Clean, gap-free, and a real generalization of `csp-implies-theorem.md`.

**Gap (honest, correctly recorded).** (FIN-W)'s infinite-witness branch. The Step-5 pigeonhole to the
"star configuration" (one hub term small-disjoint from an infinite family all divisible by one fixed
large prime `p`, one residue class mod L_0) is itself gap-free, but the contradiction from the star is
NOT established — the field's standing wall, honestly not papered over. No dead route used.

**Certified:** Reduction Lemma → `lemmas/finite-witness-periodicity.md`.

---

## 3. minimal-linking-prime-extremal — VERDICT: CHANGES REQUESTED (Status: partial)

**Scores.** Correctness 10/10 · Rigor 9/10 · Progress 4/10.

**Sub-lemmas verified.**
- (3a) q* floor: every small-disjoint pair shares a prime (F1), all large (small shared ⇒ in
  S(A)∩S(B)=∅), each large shared prime ∈Q* ⇒ ≥q*. CORRECT (trivial but valid). ✓
- (4a)/(4b) per-window cap: open interval length a_1 holds ≤⌊(a_1−1)/p⌋+1 multiples of p; same-window
  p-linked terms differ by a nonzero multiple of p that is <a_1. Elementary, CORRECT. ✓

These are correct and rest only on certified F1 + well-ordering, so I certify them — but they are
**modest** and close no gap.

**Gap (honest, correctly recorded).** (DESC) — a bad window forces a smaller-index bad window — is
unproved and, by the builder's own (accurate) assessment, difficulty-equivalent to (CSP). All three
natural descents fail (symmetric partner gives no smaller-index control; endpoint links are small;
no construction of a link in (P_max,q*)). This is the relocated 6a/6b wall. The builder correctly
DROPPED the round-4 false "finitely-many-windows-collide-with-single-ascent" closure and recorded why.

**No overclaim; recorded Status accurate.** This is a genuinely new *non-symmetric* framing (q* is a
configuration-level object, not a symmetric pair), which is valuable for diversity, but it immediately
bottomed out on the shared wall with no path beyond restating it. Outcome recorded `partial` (no gap
closed), distinct from the two `advanced` slugs.

**Certified:** q* floor + per-window cap → `lemmas/minimal-linking-prime-and-window-cap.md`.
(DESC not promotable — unproved.)

---

## Round-5 assessment

The three faces of the crux are now certified-equivalent: **(6b)** ≡ **(FIN-W) infinite branch** ≡
**(DESC)** — *an unbounded fixed-signature / star / bad-window family is not by itself a contradiction.*
The field has re-converged to one object with no *lower pressure*. Real gains: (6a) unconditionally
closed (Lemma 6); crux strictly weakened (CSP)→(FIN-W). But no live static-E_∞ framing supplies the
value/dynamics inequality a minimal bad realizer must violate.

**Recommendation to orchestrator.** Per the diversity mandate (shared-gap plateau, now 5 rounds on one
wall), next round MUST seed ≥1 framing attacking the greedy DYNAMICS of how `a_{n+1}` is *chosen*
(window-minimality of the actual successor) — the one surface no live approach touches. Advancing
covering-small-part-descent or bad-residue-witness-index alone will hit (6b)/(FIN-W) again.

3 lemmas certified this round: `bad-signature-geometric-family.md`, `finite-witness-periodicity.md`,
`minimal-linking-prime-and-window-cap.md`.
