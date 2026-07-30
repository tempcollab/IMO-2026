## imo-2026-06

### 1. What "minimal realization ≥ a_1" means, and why a_1 (not just P_max) is the right threshold

A **covering set** C is a finite prime set meeting `primes(a_i)` for every term `a_i`. By the certified
Realizability Lemma (`lemmas/realizability-and-self-dual-clutter.md`, clause (c)), every integer
`≥ a_1` whose prime set ⊇ C is a term; in particular the **minimal realization** of C is the least
integer ≥ a_1 with prime set exactly C. If the squarefree product `∏_{p∈C} p ≥ a_1`, that product IS
the minimal realization (any smaller integer with the same prime set is impossible). If
`∏_{p∈C} p < a_1`, you must inflate one prime's exponent to cross the a_1 threshold, and the minimal
realization is whatever that bumped value is.

`a_1` (not merely `P_max`) is the right threshold because it is literally the ONLY place the value
level enters Realizability clause (c) — "covering" is a purely combinatorial (prime-set) notion, and
`a_1` is the sole numeric gatekeeper converting a covering set into an actual term. This is exactly
where Lemma 9 (minimal-bad-term floor-tightness) stalls: the descent `m_0 → m_0/p` is only certified to
produce a smaller bad term when the quotient is `≥ a_1`; below `a_1` clause (c) is silent. So the crux is
inherently about `a_1`'s specific numeric value versus the *squarefree product* of a covering set's
primes, not just about `P_max` (the value threshold, not the color threshold).

### 2. Main finding: a stronger, cleaner, EMPIRICALLY-SUPPORTED reformulation that closes (6b) if true

I tested directly (not just the weaker "no minimal covering set with a large prime realizes ≥ a_1")
whether **any minimal covering set ever contains a large prime at all**. I searched, for
`a_1 ∈ {15, 35, 99, 231, 1001, 105}`, every prime set `C = (subset of small primes, size ≤ 4) ∪ {q}`
for every large prime `q` up to 150–200, using the actual greedy sequence out to 500–1200 terms
(script: generated sequence, built each term's color = its prime factorization, and tested
`is_covering`/minimality against that term list as an approximation to the true infinite covering
condition). **Result: in every case, zero minimal covering sets containing a large prime were found**
— for a_1=15 I pushed to size ≤5, primes ≤200, 1200 terms, still empty. Meanwhile the SMALL-only
minimal covering sets found match exactly the certified Prop-D example (a_1=15: `{2,3},{2,5},{3,5}`,
the self-dual triangle) and analogous small triples for the others.

**Conjecture (ℰ-small-only).** *Every minimal covering set (i.e. every member of the clutter*
`ℰ` *of minimal transversals of the term-color hypergraph, certified self-dual in*
`lemmas/realizability-and-self-dual-clutter.md`*) is a subset of* `[2, P_max]` *— no large prime is ever
load-bearing in a MINIMAL cover, even though large primes freely appear in non-minimal covers and in
term prime sets.*

**Why this would immediately close the whole crux (a one-line argument, given the certified lemmas):**
Let `m_0` be the smallest bad term (if one exists), `C := primes(m_0)`, which is covering (𝒯⊆𝒞). Since
`C` is finite and covering, it contains some `C' ∈ ℰ` (a minimal covering subset — existence is exactly
the self-dual-clutter fact that every covering set contains an edge). If ℰ-small-only holds, `C' ⊆
[2,P_max]`, so `C' ⊆ C ∩ [2,P_max] = S(m_0)`. Since supersets of covering sets are covering, `S(m_0) ⊇
C'` is covering — **directly contradicting** `m_0` bad (`S(m_0)` non-covering by definition). Hence no
bad term exists, CSP holds, and by the already-certified `lemmas/csp-implies-theorem.md` the theorem
follows. **This bypasses Lemma 9's stalled descent entirely** — it needs no induction on `m_0`, no
value-descent, just one existence-of-an-edge fact plus the certified Realizability/self-duality lemmas.

This is a strictly crisper, purely set-theoretic/combinatorial target than the dispatch's stated crux
("no minimal covering set with a large prime has minimal realization ≥a_1") — it says such sets don't
exist AT ALL, not merely that their realization is small. It is logically at least as strong as (implies)
that stated crux, and my numerical search targeted it directly (found nothing, not even below-a_1
witnesses of large-prime minimal covers, which the weaker crux would also forbid from being ≥a_1 but
would allow to exist below a_1 — I found none at any value).

**Caveat — this is a conjecture, not a proof.** My search is necessarily a finite-term truncation of
the (a priori infinite) covering condition; I cannot rule out a minimal covering set requiring
information about term #10000 to fail as "covering" in the truncation but succeed in the limit, or a
minimal cover with a large prime whose size exceeds my search bound (5) or whose large prime exceeds my
search bound (200). But given 6 different `a_1` values, up to 1200 terms, and no single hit, this is
strong evidence, and — crucially — it is a MUCH more tractable-looking statement to actually prove than
the original theorem, because it is now entirely about the clutter `ℰ`, decoupled from "bad term"
minimality/induction.

### 3. Partial mechanism / exchange idea toward ℰ-small-only (a lead, not a proof — do not treat as done)

Suppose toward contradiction `C ∈ ℰ` contains a large prime `q`. By minimality, `C∖{q}` is NOT
covering: some witness term `B` has `primes(B) ∩ (C∖{q}) = ∅`; since `C` is covering, `primes(B)∩C≠∅`,
forcing `q | B` (B's *only* connector to C is q). Two free facts fall out immediately (both are
one-line consequences of already-certified material, safe for the outliner to reuse without
re-deriving from scratch):
- `B ≠ a_1`: since `q` is large, `q ∤ a_1` (as `primes(a_1) = P ⊆ [2,P_max]`), but `q | B` is required.
- Hence `a_1` (a term, `≠ B`) must itself meet `C∖{q}` (every two terms share a prime — cert. fact F1,
  and `a_1` is a term not equal to B, so `a_1` meets C via some prime, and it can't be q since q∤a_1).
  So **`C` already contains some prime of `P` (⊆ small)** — i.e. `C∖{q}` is nonempty and intersects `P`.
  This shows every minimal cover with a large prime is forced to ALSO carry a prime of `a_1`'s own factor
  set — a real (if partial) constraint, but not yet the full contradiction; the natural next step (not
  attempted here) is to iterate this "who is B's witness" argument along a chain of terms, or to use
  Local Hub-Cover (Lemma 8) with `h=B` to bound `Q(B)` and try to force `q` itself to be redundant in C
  via B's own structure. I did not push this further — flagging as the likely proof lever, not a result.

### 4. Cheap-kill / structural checks that support the reformulation

- `{q}` alone (a large prime) is NEVER covering: `q ∤ a_1` (large, so not a factor of `a_1`), and `a_1`
  is a term, so `{q}` misses `a_1`'s color — a one-line fact, already implicitly used above. So every
  minimal cover containing `q` has size `≥2`, consistent with all numeric hits being size ≥2 (in fact
  found sets were size-2 SMALL-only, never large-prime-inclusive at any size).
- The certified Prop-D "self-dual triangle" example (`{2,3},{3,5},{2,5}` for a_1=15) that the field has
  been treating as a *barrier* to pure combinatorics is, on inspection, NOT a counterexample to
  ℰ-small-only — it is small-only itself. It illustrates only that ℰ can be self-dual/centerless among
  small primes, a different (and compatible) fact.

### Distinct openings
1. **(New, this report) Attack ℰ-small-only directly** as a standalone combinatorial statement about the
   clutter, using the exchange/witness argument in §3 (forces `C∖{q} ∩ P ≠ ∅`) as the entry lever —
   decoupled from `m_0`-minimality/induction. This is a genuinely different top-level target from Lemma
   9's descent (no induction on term value at all; purely about which primes CAN be load-bearing in a
   minimal cover).
2. Push the exchange argument in §3 further: iterate "which term witnesses C∖{q} fails" using Local
   Hub-Cover (Lemma 8) on the witness B (not on m_0) to try to force q reducible/redundant in C.
3. Try to disprove ℰ-small-only with a more exhaustive/larger search (higher a_1 with more prime
   factors, larger size bound, symbolic/exact covering test instead of finite-truncation) before
   investing further proof effort — see caveat above.

### Candidate technique(s)
Clutter/blocker duality (already in play via `realizability-and-self-dual-clutter.md`) combined with the
witness-exchange argument in §3; this is a hypergraph-transversal minimality argument, not a
number-theoretic descent — a genuinely different mechanism from Lemma 9's induction-on-value.

### Cheap-kill candidates
`{q}` singleton never covering (shown above, one line) — already rules out trivial size-1 large-prime
covers; not by itself decisive but a good sanity check for any builder.

### Knowledge-base entries to use
Realizability / clutter duality already exploited (see `realizability-and-self-dual-clutter.md`); if the
builder wants a named external tool for "every covering set contains a minimal one," that's just the
finite/DCC well-ordering already used — check `knowledge_base.md`'s extremal-principle / pigeonhole
entries (same ones cited in Lemma 8/9) since no new KB entry beyond what's already certified is needed
for the §3 lever.

### Analogous past problems (cruxes)
Not checked this pass in depth (assigned lens was the value inequality itself, and the numerical find
was the priority given the time budget) — the outliner/next explorer should check crux corpus under
number_theory subtopics "covering systems" / "greedy sequences" / "hypergraph transversal" for a
witness-exchange precedent; I did not locate one myself and don't want to force a weak match.

### Prior progress
Unchanged from `current.md`: CSP reduction, Lemmas 6–9 all certified as recorded there. This report adds
a NEW candidate reformulation (ℰ-small-only) that, if proved, closes (6b) in one line via the existing
certified lemmas — it does not yet constitute progress on a proof, only a sharper, better-supported
target plus a partial lever (§3).

### Dead ends (do not retry)
As recorded in current.md: global Σ1/p² capacity, pure covering/Helly (Prop D barrier) as a
COMBINATORICS-ONLY closer (my finding does NOT resurrect pure-Helly — it still needs the §3
value/witness argument using `a_1` being a term, so it is value-dependent, not purely set-theoretic),
symmetric bad-partner ascent, aimo-0016 template, direct (q*,k) rewrite operator.

### Small-case / intuition notes
**Conjecture, backed by exhaustive-within-bounds numerical search across 6 values of a_1, up to 1200
terms, size ≤5, primes ≤200 — zero counterexamples found:** every minimal covering set is entirely
small-prime (⊆[2,P_max]). This is NOT proved. If true it closes the crux in one line via already-
certified lemmas (Realizability, self-dual clutter, csp-implies-theorem). The natural next proof lever
(§3) shows any hypothetical large-prime-containing minimal cover is forced to also contain a prime of
`P = primes(a_1)` — a genuine, cheap, certifiable-looking partial fact that the next builder should
attempt to push into a full contradiction.
