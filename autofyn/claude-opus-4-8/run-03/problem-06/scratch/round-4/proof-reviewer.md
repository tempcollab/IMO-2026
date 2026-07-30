# Proof-reviewer — imo-2026-06, round 4

Problem: greedy gcd-sequence is everywhere arithmetic-periodic (a_{n+T}=a_n+L ∀n). The whole
theorem is (certified, rounds 1–2) reduced to the finiteness crux (CSP)/(SL): every term's small
part S(m)=primes(m)∩[2,P_max] is covering (meets every term's primes). Crux remains OPEN. I
re-derived the load-bearing new claims from scratch and checked them numerically on
a_1∈{15,35,99,231,1155}: F1, every-term-meets-P, a_1-lattice⊆terms, CSP (no bad terms), and GPC
all hold. CSP=True (no bad terms) is consistent with the crux being true-but-unproven; every file
correctly marks it UNPROVEN, so no approach is a false `solved`.

---

## covering-small-part-descent — CHANGES REQUESTED (partial)

Value well-ordering / infinite-ascent framing on term value. A genuinely NEW framing (not a rerun
of the E_∞ reduction).

Verified gap-free:
- **Step 1 (CSP)⇒theorem, self-contained.** E*={m>1:S(m) meets every color} is periodic mod
  L_0=∏_{p≤P_max}p (S(m) depends on m mod L_0); under (CSP), E*∩[a_1,∞)=E_∞∩[a_1,∞) (⊇ uses CSP, ⊆
  free); a_1,k·a_1∈E*; ENUM+PER give a_{n+T}=a_n+L_0. I re-derived each inclusion independently —
  correct, order-free, does not need (SL). CERTIFIED.
- **Step 2 base |P|=1.** p|every term ⇒ {p} covering. Correct.
- **Step 3 off-lattice.** shared primes of a bad m and its witness are all large; GPC ⇒ a_1∤m, a_1∤B.
  Correct (GPC hypothesis met).
- **Step 4 bad-partner.** B bad (else S(B) meets primes(m) small); B≠m; mutual pair. Re-derived —
  correct. CERTIFIED.
- **Step 5 ascent.** smallest bad m_0 has bad partner B>m_0. Correct (well-ordering). CERTIFIED.

Genuine GAP (honest, correctly flagged): **Step 6→7.** (6a) the partner relation is *symmetric* on
{m_0,B}, so the single ascent step does NOT yield an infinite chain — unbounded family unproven.
(6b) even an infinite chain is not yet a contradiction (global Σ1/p² capacity caps only a positive
fraction — proven dead). The builder does NOT overclaim; Status `partial` is correct. Real progress
over prior best (new framing off the dead window-minimality wall + proven ascent engine).

## reduced-process-identity — CHANGES REQUESTED (partial)

Static process-coincidence / strong-induction framing. This round's advance:
- **GPC (§3a)** — any two terms sharing no small prime are both off the a_1-lattice, ANY number of
  shared large primes. I re-derived: a_1|A ⇒ P⊆primes(A); B shares p∈P with a_1; p∈primes(A)∩primes(B)
  small, contra. Symmetric. Gap-free — this genuinely CLOSES the reviewer-flagged (SL)⟸
  multi-large-prime gap from round 2 (two shared large primes {q1,q2} no longer escape). CERTIFIED.
- Correctly RETIRES the false "a_{n+1} is P_max-smooth" target (237=3·79 is a good term for a_1=231,
  verified) and reframes the step as **redundancy (RED_n)**: S_{n+1} covers the predecessor list.
- E* periodicity, easy direction, reduction-to-inclusion all re-checked — gap-free (as round 2).

Genuine GAP: **(RED_n)** = the reverse inequality β≤a_{n+1} = the crux in induction form. Honestly
flagged; §5(G3) correctly records the empty-window competitor route is structurally blocked. Status
`partial` correct, no overclaim. Advance = the (SL)⟸ patch.

## self-dual-clutter-grading — RETHINK (unsolved as a route)

Clutter/blocker-duality + value-grading framing. Set-theoretic core is rigorously proved:
- **Lemma 0** every term meets P; **Lemma 1** realizability 𝒞=𝒯 (m_k=(∏S)p₀^k realizes S, →∞, ENUM);
  **Lemma 2** self-dual clutter b(ℰ)=ℰ; **Lemma 4** (CSP)⟺H_s covering-dense; **Lemma 5** base |P|=1;
  **Lemma 6** GPC. I re-derived Lemmas 1 and 2 independently — both correct and gap-free. CERTIFIED.

But the distinctive **Step-4 grading lever is not a gap the builder can close** — the builder itself
self-certifies (honestly, no overclaim) that after consuming realizability the residual "H_s
covering-dense" reduces to *exactly* covering-small-part-descent's open Step 6→7 (contradiction from
an infinite ascending bad-term chain), and that the value/size axioms it may legitimately add do NOT
break the self-dual triangle. Per the established role rule (round 2, large-prime-capacity-counting):
when an approach self-certifies its framing adds no distinct route to the crux, route RETHINK — there
is no gap for THIS builder to close, only the same shared wall. Its reformulation lemmas are the
salvage and are certified into the cache. Keeping it as a live solve route would duplicate the descent
gap (single-gap trap). Status truly = unsolved-as-route; builder's `partial` label refers to its
cache byproducts, which is fair, but for routing it is RETHINK.

---

## Lemmas certified this round (5)

1. **generalized-sole-connector-off-lattice.md (GPC)** — supersedes the singleton Prop C; closes the
   round-2 (SL)⟸ multi-large-prime flag. Gap-free.
2. **csp-implies-theorem.md** — order-free (CSP)⇒theorem reduction (covering-small-part Step 1;
   equivalently reduced-process-identity's E*-reduction). Gap-free, conditional on (CSP).
3. **realizability-and-self-dual-clutter.md** — 𝒞=𝒯, b(ℰ)=ℰ, every-term-meets-P (self-dual Lemmas
   0,1,2). Gap-free.
4. **bad-partner-and-ascent.md** — bad-partner lemma + smallest-bad-term ascent (covering-small-part
   Steps 3–5). Gap-free; explicitly notes it is an engine, not a closure (symmetric relation ≠ chain).

Nothing that claims to close the crux was certified — none exists. No false `solved`; all files
honestly mark (CSP)/(SL)/(RED_n)/Step-6→7 UNPROVEN, consistent with the round-1 role rule.

## Verdicts
- covering-small-part-descent: **CHANGES REQUESTED** (partial) — advance a chain/contradiction for Step 6→7.
- reduced-process-identity: **CHANGES REQUESTED** (partial) — RED_n still open; (SL)⟸ gap closed.
- self-dual-clutter-grading: **RETHINK** (unsolved-as-route) — lemmas salvaged; framing collapses to shared wall.
