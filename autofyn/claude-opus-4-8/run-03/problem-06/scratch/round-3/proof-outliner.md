## imo-2026-06

Context locked in. Whole problem is certified-reduced to a single crux with three equivalent
phrasings; endgame + enumeration + periodicity are certified lemmas (import, never re-prove).
Cleanest phrasing of the crux, adopted below:

> **(SL)** Every two terms share a prime ≤ P_max (= largest prime factor of a_1).
> Equivalently **(CSP)** for every term m, its *small part* S(m) := primes(m) ∩ [2,P_max] is
> itself a covering set (i.e. S(m) meets primes(a_i) for every i).

**(SL) ⟸ (CSP) is a two-line win (fold into every approach):** if every term's small part is
covering, then for any two terms A,B the small parts S(A),S(B) are covering sets; any two covering
sets intersect (each term is a covering set, so the family of covering sets is pairwise
intersecting — certified F1); their intersection is a small prime shared by A and B. ∎
So the entire crux is exactly **(CSP): no term has a non-covering small part** ("no bad terms").
This is the single target all approaches below aim at, from different routes.

DEAD (do not field): pure covering/Helly/sunflower (Prop D barrier — the small clutter can be the
self-dual triangle {2,3},{3,5},{2,5}, a1=15, with no Helly centre); global capacity/density
(Σ1/p² — proven insufficient); competitor/minimality in the window (a_n,a_{n+1}) (G3 — window
provably empty of E_n, so "exhibit a smaller compatible integer" can NEVER close it).

Cheap kills to fold as reductions (both cheap, neither closes |P|≥2):
- **|P|=1 (a_1 a prime power p^k):** every term is divisible by p (its only way to meet a_1), so
  all terms pairwise share p; (SL) trivial. Rigorous 3-line base case (explorer-window §4).
- **Generalized Prop C (singleton hypothesis was never used — promote & certify):** if two terms
  A,B share *no* small prime (primes(A)∩primes(B) ⊆ large primes, any size ≥1), then a_1 divides
  neither A nor B. Proof verbatim from lemmas/sole-connector-off-lattice.md: if a_1|A then P ⊆
  primes(A); B meets a_1 in some p∈P (F1); p∈primes(A)∩primes(B) is small — contradiction. This
  patches the reviewer's flagged multi-large-prime gap in (SL)⟺Lemma A at no cost, confining EVERY
  bad term (single- or multi-large-prime) to a length-<a_1 window off the a_1-lattice.

---

### covering-small-part-descent : new  (the required far-from-field framing — well-ordering on term VALUE)
Target: the full theorem, via (CSP) proved by a global well-ordering / infinite-ascent
contradiction on term values — NOT a local window-minimality argument, so it steps around the
dead G3 competitor route.
Technique: minimal-counterexample / infinite descent (well-ordering of ℕ), plus generalized Prop C.
Skeleton:
  1. Import enumeration + periodicity + reduction: it suffices to prove (CSP). — certified lemmas
     + the (SL)⟸(CSP) two-liner above.
  2. Dispose |P|=1 by the prime-power cheap kill; assume |P|≥2. — base case.
  3. Call a term m **bad** if S(m) is non-covering. Suppose bad terms exist; let **m₀ be the
     smallest bad term** (well-ordering). — hypothesis for contradiction.
  4. m₀ bad ⇒ ∃ term B with primes(B) ∩ S(m₀) = ∅, so primes(m₀)∩primes(B) ⊆ large primes; being
     two terms they still share a prime, hence a LARGE prime q>P_max. — F1 (pairwise intersecting)
     + definition of non-covering small part.
  5. **B is itself bad, and B > m₀** (the proven engine of this approach): if S(B) were covering it
     would meet the edge primes(m₀) in a small prime, contradicting primes(m₀)∩primes(B) ⊆ large;
     so B bad. B≠m₀ (distinct terms in a sole/large connection); minimality of m₀ forces B>m₀.
  6. Hence every bad term has all its large-only partners strictly above it ⇒ an infinite strictly
     increasing chain of bad terms m₀<B<… each off the a_1-lattice (generalized Prop C) and each
     lying in its own length-<a_1 window between consecutive multiples of a_1. — GAP closes here.
  7. Contradiction from the chain ⇒ no bad terms ⇒ (CSP) ⇒ (SL) ⇒ theorem.
Key lemmas (claim + mechanism):
  - (CSP)⇒(SL) — two covering small parts are covering sets, which pairwise intersect, in a small
    prime. (proved, two lines.)
  - Smallest-bad-term ascent (Step 5) — a bad term's large-only partner cannot have a covering small
    part (else it would small-hit the bad term), so it is a larger bad term. (proved — new this
    round, clean; this is the concrete opening that makes the framing live.)
  - Generalized Prop C — every bad term is off the a_1-lattice (a_1∤m for any bad m). (promote from
    certified lemma, singleton hypothesis unused.)
Open gaps:
  - STEP 6→7 CLOSURE (the crux, now in a genuinely new form): derive a contradiction from an
    infinite strictly ascending chain of bad terms, pairwise/chain-linked by large primes, each
    squeezed into a length-<a_1 off-lattice window with a good (a_1-multiple, covering-small-part)
    term within distance a_1. Candidate leverage the builder should try, in order:
    (i) a good term M (multiple of a_1) sits within a_1 of each bad m; M is covering-small-part;
        relate m to M via the greedy value (m is the min E_∞-element above the previous term, and
        M∈E_∞ is a competitor ABOVE m — a *legitimate* larger-competitor bound, not the dead
        smaller-competitor one) to bound how "large-prime-heavy" m can be;
    (ii) track the large prime q linking m₀→B→…: does the SAME q persist up the chain, or must new
        large primes appear? If q persists, q divides an infinite ascending set of bad terms all in
        distinct windows — combine with the a_1-lattice being all-good to bound q-multiples that can
        be bad; if q must change each step, exhibit a monovariant that cannot ascend forever.
  This gap is FAR from window-minimality (it is a value-ordering/ascent argument), so it does not
  share the field's dead wall.
Cases to cover: |P|=1 (base); |P|≥2 bad-term chain; single-large-prime vs multi-large-prime
  connection (both handled uniformly by generalized Prop C — no separate case).
Watch out for: do NOT reintroduce a smaller-competitor at Step 6 (dead G3); the only competitors
  allowed are LARGER known terms (a_1-multiples) used as upper bounds on m's value/structure. Do not
  assume the chain uses one fixed q. Ensure "B>m₀" uses only minimality, not any value estimate.

### reduced-process-identity : advance  (re-oriented to the redundancy target + multi-prime patch)
Target: the full theorem via E_∞∩[a_1,∞) ⊆ E* (already certified reduction); the sole open step is
(SL), to be closed as (CSP)/redundancy — NOT via the dead reverse-competitor route.
Technique: strong induction on n for (SL_n), but the inductive step is now a DIRECT value/redundancy
argument on a_{n+1}'s factorization (per the reverse-inequality explorer: the window is empty, so
no competitor argument is permitted).
Skeleton (only the reoriented parts; §1–§3 stay certified):
  1. Keep §1–§4 verbatim (reduction to (SL_n): S_{n+1} meets each S_k). — certified.
  2. **Patch the (SL)⟺Lemma A gap** the reviewer flagged: state and use generalized Prop C so the
     multi-large-prime shared case (|primes(a_{n+1})∩primes(a_k)|≥2, all large) is covered — a_1
     divides neither, both confined to one window. — promoted lemma.
  3. Reframe the inductive step as **redundancy** (explorer-window opening 3, the accurate model):
     do NOT try to show a_{n+1} is P_max-smooth (FALSE — a_1=231 has term 237=3·79). Show instead:
     IF a_{n+1} connects to a predecessor a_k only through large primes, THEN S(a_{n+1}) is
     non-covering, so some earlier term a_j is missed by S(a_{n+1}); use simultaneous compatibility
     of a_{n+1} with BOTH a_k and a_j (the pairwise-but-not-centrally intersecting structure G4) to
     force a small shared prime — a value contradiction on a_{n+1} itself, not a competitor.
Key lemmas:
  - Generalized Prop C (multi-prime) — closes the reviewer's ⟸ gap; mechanism as above.
  - Redundancy target — large primes may divide a_{n+1} freely; they are forbidden only as the SOLE
    bridge, because a_{n+1} must simultaneously bridge every predecessor and the small parts of the
    predecessors form a pairwise-intersecting family a_{n+1} must hit.
Open gaps: the direct-value inductive step (Step 3) — unproved; this is the shared crux in the
  induction phrasing. Explicitly forbidden: any "smaller compatible competitor" move (G3 dead).
Cases to cover: none new beyond the multi-prime patch.
Watch out for: the literal "witness is P_max-smooth" phrasing is FALSE — target redundancy, not
  smoothness. Do not re-derive E* periodicity (certified).

### cofactor-recruitment-smoothness : advance  (Gap G restated as redundancy; fold generalized Prop C)
Target: the full theorem via Lemma A (certified reduction); close Gap G, restated correctly.
Technique: recruitment monovariant + direct structural argument on the witness term's factorization.
Skeleton (reoriented tail only; Steps 1–5 stay):
  1. Keep Steps 1–5 (recruitment bookkeeping, witness structure, Prop C, Prop D). — as written.
  2. **Restate Gap G** away from the false "cofactor is P_max-smooth" toward the true redundancy:
     the witness term a_i (new minimal member, off-lattice by Prop C) carrying large q with partner
     a_j (primes(a_i)∩primes(a_j)={q}) cannot exist because S(a_i) would be non-covering while a_i
     is a term compatible with ALL predecessors — its small part must already reach a_j.
  3. Promote generalized Prop C (drop the singleton assumption) as a certified lemma, so the barrier
     confines multi-large-prime witnesses too.
Key lemmas:
  - Generalized Prop C — as above (promote to lemmas/, certify).
  - Redundancy form of Gap G — the witness's connectivity to a_j is realizable through S(a_i)
    because S(a_i) is forced covering (this IS (CSP) localized to the witness).
Open gaps: Gap G in redundancy form (= (CSP) at the witness) — unproved; the dynamical crux.
Cases to cover: |S_i|=1 vs ≥2, single vs several large primes — all uniform under generalized Prop C.
Watch out for: NEVER the circular cofactor-peel (a_i/q^α compatibility is a COROLLARY of Lemma A).
  Prop D forbids a pure covering-set proof — the step must use greedy value.

### self-dual-clutter-grading : new  (option-a far framing — multiplicative structure of E_∞ directly; OPTIONAL 2nd new, reviewer's call)
Target: the full theorem, proving (CSP) by exploiting that the family of edge prime-sets is a
self-dual clutter graded by integer value, with a_1 as the minimal realized element.
Technique: clutter/blocker duality + value-grading (size) as the extra axiom Prop D lacks.
Skeleton:
  1. Import reduction: suffices to prove (CSP). — certified + two-liner.
  2. E := up-set {finite prime-sets S : S∩T≠∅ ∀ edges T}; edges = minimal members; show E = its own
     blocker (self-dual clutter): S∈E ⟺ S hits every minimal member, and every finite covering set
     is realized by some integer ≥ a_1, so edges = minimal covering sets = minimal transversals of
     themselves. — set-theoretic (rigorous, Prop-D-consistent).
  3. Small-clutter H_s := minimal covering sets ⊆ [2,P_max]; P=primes(a_1)∈E gives H_s ≠ ∅. (CSP)
     ⟺ every edge contains a member of H_s ⟺ H_s is *covering-dense* (every covering set has a
     covering small subset). — reformulation.
  4. GRADING lever (the new content, where value beats the abstract triangle): a_1 is the smallest
     term; every multiple of a_1 is a term with a covering small part ⊇P; these good terms tile ℕ
     with gap a_1. Use that a large-prime edge {small primes}∪{q} is realized only at value ≥ q ≫
     a_1, whereas its putative small transversal is realized below a_1 — so if H_s were NOT
     covering-dense, a self-dual triangle among small primes (a1=15 type) would have to coexist with
     a large-prime edge that its small transversals fail to hit, contradicting that the small
     transversals already appear as good terms densely. — GAP.
Key lemmas:
  - E self-dual (blocker(E)=E) — up-closure + realizability of every covering set by a large enough
    integer. (provable, rigorous.)
  - (CSP) ⟺ H_s covering-dense — small part covering ⟺ contains a small covering subset. (provable.)
Open gaps: Step 4 grading argument — turn "small transversals appear densely as good terms below
  a_1-scale" into a proof that no edge escapes H_s. This is the crux in clutter-grading language;
  DIFFERENT gap-flavor from the descent (structural/grading vs value-ascent).
Cases to cover: |P|=1 trivial; H_s a chain vs an antichain (triangle) — the antichain (no Helly
  centre, a1=15) is the hard case and must be handled, not assumed away.
Watch out for: Prop D says self-duality ALONE is insufficient — the proof MUST consume the grading
  (value/size), or it collapses to the dead covering-set level. If Step 4 cannot use value, this
  framing is not viable and should be dropped rather than dressed up.

---

### Recommended candidate field for the reviewer
Rank these four; my priority order:
1. **covering-small-part-descent (new)** — carries a concrete NEW proven step (smallest-bad-term
   ascent) and a gap genuinely off the dead window-minimality wall; best diversity bet.
2. **reduced-process-identity (advance)** — top live Elo; reoriented to redundancy + multi-prime
   patch (also promotes generalized Prop C, a certifiable win independent of the crux).
3. **cofactor-recruitment-smoothness (advance)** — second live dynamical route; Gap G corrected to
   redundancy; promotes generalized Prop C.
4. **self-dual-clutter-grading (new, optional)** — furthest reframing (option a); include if the
   reviewer wants a second new framing, drop if Step 4 grading looks unusable (Prop D risk).
enum-covering-primes stays parked to import the crux proof once it lands (no build needed this round).
Build set suggestion: covering-small-part-descent, reduced-process-identity, cofactor-recruitment-
smoothness (+ self-dual-clutter-grading if breadth is wanted). Each promotes/certifies generalized
Prop C as a shared reusable lemma regardless of crux progress.
