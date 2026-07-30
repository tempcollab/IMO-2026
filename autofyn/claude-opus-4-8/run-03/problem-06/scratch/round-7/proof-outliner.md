## imo-2026-06

Field this round: 2 NEW (one on the mandated GREEDY DYNAMICS surface, one foreign-technique active-rewrite),
2 ADVANCE (the two live crux carriers). All import the certified scaffold — ENUM, PER, F1, GPC, csp-implies-
theorem, finite-witness-periodicity (Reduction Lemma: (FIN-W)⟹theorem), bad-signature-geometric-family
(Lemma 6), bad-partner-and-ascent, minimal-linking-prime-and-window-cap (Lemma A q*/Lemma B window cap),
realizability-and-self-dual-clutter — none re-proved. reduced-process-identity and enum-covering-primes stay
PARKED (import the crux proof once it lands; not built). Shared notation: P_max=max prime factor of a_1;
L_0=∏_{p≤P_max}p; S(m)=primes(m)∩[2,P_max]; a term is bad iff S(m) non-covering; R_bad={bad classes mod L_0},
|R_bad|≤L_0 (finite, certified); W(r)={i: primes(a_i)∩S(r)=∅}; q*=min large linking prime (certified).

---

window-purity-class-cycle: new
Target: the full theorem — ∃ T,L with a_{n+T}=a_n+L for every n. (This is the mandated GREEDY-DYNAMICS
  framing: it is the ONLY approach whose spine uses how a_{n+1} is *chosen* — the open interval (a_n,a_{n+1})
  and the finite walk the witnessing dynamics induce — rather than a static E_∞/covering fact.)
Technique: greedy window-minimality (a new local lemma, "Window Purity") + pigeonhole on a FINITE directed
  class-graph (≤L_0 nodes) whose infinite traversal must revisit a class + q* extremal floor. Reduces the
  whole problem to (FIN-W) (certified sufficient), then attacks (FIN-W)'s failure through the dynamics.
Skeleton:
  1. It suffices to prove (FIN-W) [every term is small-disjoint from only finitely many terms] — by the
     certified Reduction Lemma (finite-witness-periodicity.md), (FIN-W)⟹theorem. IMPORT, gap-free.
  2. **Window Purity (new cheap lemma, certifiable in ~5 lines).** For every n and every integer x with
     a_n<x<a_{n+1}: x∉E_∞, hence S(x) is NON-COVERING (x fails gcd>1 with some term of the WHOLE sequence,
     not merely a predecessor). — by ENUM (the terms ARE E_∞∩[a_1,∞) enumerated, so no E_∞-element lies
     strictly between consecutive terms) + the immediate direction "S(x) covering ⟹ x∈E_∞". This is strictly
     window-wide, sharper than GPC (which only pins the endpoint off-lattice). It is the local, per-window
     texture Prop D says any closing argument must use, and it invokes no dead global count.
  3. Suppose (FIN-W) fails. IMPORT the certified pigeonhole of bad-residue-witness-index Step 5: obtain a
     hub term m (bad, small part s_0) and an infinite family T_p={t_1<t_2<…}, all ≡r* (mod L_0), all divisible
     by one fixed large prime p (with p|m), each small-disjoint from m, each bad (Steps 2–3), all off-lattice
     (GPC), all in one AP mod pL_0.
  4. **Single-sided witnessing is harmless (prune, gap-free).** If class r* needs to clear only the hub m's
     slot, then every x≡r* (mod L_0) divisible by any large prime of the fixed finite set Q(m) already lies
     in E_∞ — this is exactly the finite-Q_rel bookkeeping of the Reduction Lemma and yields NO contradiction.
     Hence the failure of (FIN-W) forces MUTUAL / CYCLIC infinite witnessing: the witness index set W(r*) is
     itself infinite (each t_j is bad, so spawns its own witness structure), recursively.
  5. **Finite class-graph revisit.** Define a directed graph G on R_bad: r→r′ whenever a term in class r is
     small-disjoint from a term in class r′ (a witness link, carrying a large linking prime q≥q* by Lemma A).
     By Step 4 an infinite witnessing process is an infinite walk in G; since |R_bad|≤L_0 is finite (certified),
     the walk revisits some class infinitely often. [GREEDY LEVER + OPEN GAP — see below.]
  6. Contradiction ⟹ (FIN-W) holds ⟹ theorem (Step 1).
Key lemmas (claim + mechanism):
  - Window Purity — because ENUM makes the terms exactly the increasing enumeration of E_∞∩[a_1,∞), so the
    open gap (a_n,a_{n+1}) contains NO element of E_∞; and "small part covering ⟹ in E_∞" is immediate, so
    every interior integer has non-covering small part. (Certifiable now; deliver as a cached lemma even if
    the crux stays open.)
  - Greedy no-smaller-hole — because t_j is the SMALLEST element of E_∞ exceeding its predecessor and m<t_j
    is a predecessor of t_j, any integer x≡r* (mod L_0) with x<t_j that is compatible with all predecessors
    would already be a term; so if a candidate x in class r* were skipped, some predecessor a_i (i∈W(r*))
    is not cleared by x — pinning WHICH witness color blocks each interior candidate. Window Purity supplies
    the same non-covering fact for EVERY x in the gap, so the blocking predecessor varies over W(r*): this is
    the concrete handle that forces W(r*) to be "actively used", i.e. the mutual/cyclic structure of Step 4.
Open gaps: Step 5's closing mechanism. Two candidate closes for the builder, both flagged UNPROVEN:
  (5a) a revisited class, traversed by the greedy dynamics, forces a strictly SMALLER large linking prime on
  each return (feeding an infinite strictly-decreasing sequence of primes ≥q*, impossible by well-ordering) —
  the DESCENT must be produced, it is NOT given by the q* floor alone (q* is only the global minimum);
  (5b) alternatively, along the fixed AP of p-multiples in class r*, take the SMALLEST x that is NOT in E_∞
  ("first hole"); Window Purity + greedy minimality of the surrounding terms should over-constrain which
  witness color W(r*) blocks x versus its neighbours, but the contradiction is not yet extracted.
  The builder should target (5a)/(5b) and, at minimum, land Window Purity as a certified lemma + the Step-4
  mutual/cyclic reduction as a certified sharpening of the wall.
Cases to cover: in Step 5, split (i) one prime p serves the infinite revisit (star/single-prime case →(5b));
  (ii) infinitely many distinct large primes serve the revisited edge (Q(r) infinite → walk/(5a)).
Watch out for: do NOT assume "one hub blocks a whole window" — REFUTED numerically this round (only ~45–100%
  of windows depending on a_1, never reliably universal); multi-hub joint rejection is the norm, so Step 5b
  must allow several blocking predecessors per interior integer. Do NOT route (5a) through the symmetric
  term-value ascent (bad-partner-and-ascent is provably symmetric — no strict descent). Do NOT touch global
  Σ1/p² capacity or pure covering/Helly (both certified dead).

---

lex-rewrite-descent: new
Target: the full theorem, via (CSP)/(FIN-W). Contradiction from a MINIMAL bad configuration.
Technique: foreign-technique transplant — aimo-0960-style ACTIVE local rewrite / exchange operator on a
  lexicographically-minimal bad configuration, replacing the passive symmetric "bad partner exists" (which
  gives no strict descent) with a *designed asymmetric* rewrite that provably lowers a well-order. This is a
  genuinely different route from window-purity-class-cycle (constructive descent, not dynamics/pigeonhole).
Skeleton:
  1. It suffices to prove (CSP) — no bad term ever — by csp-implies-theorem.md (or the weaker (FIN-W) via the
     Reduction Lemma). IMPORT, gap-free.
  2. Suppose a bad term exists. Order bad terms by the pair (q*, k) where q* is the minimal large linking
     prime (Lemma A, certified, well-defined and non-symmetric) and k the window index of the smaller member;
     take the lex-minimal bad configuration {A,B}, A the smaller (off-lattice, in window (k a_1,(k+1)a_1)).
  3. **[Active rewrite — the load-bearing construction, OPEN GAP.]** Construct an explicit integer A′ from A
     by a covering-preserving prime exchange (e.g. divide out the large linking prime and multiply by a
     smaller admissible large prime, or peel q* and substitute a cofactor's own witness prime) such that:
     (i) A′ is a term — by REAL clause (c): primes(A′) must still CONTAIN a covering set;
     (ii) A′ is bad — its small part stays non-covering (rewrite touches only large primes);
     (iii) A′ is strictly (q*,k)-smaller — the new linking prime is <q*, or the window index drops.
     Any of (i)–(iii) contradicts lex-minimality.
  4. Contradiction ⟹ no bad term ⟹ (CSP) ⟹ theorem.
Key lemmas (claim + mechanism):
  - Covering-preservation of the exchange — because REAL clause (c) says any integer ≥a_1 whose prime set
    contains a covering set is a term; the bad term A has primes(A)=S(A)∪Q(A) covering with S(A) alone
    non-covering, so the covering role rests on Q(A) (large primes). The rewrite must keep a covering
    sub-collection while lowering q*.
  - Strict descent asymmetry — because q* is attached to the WHOLE configuration (not a symmetric pair,
    Lemma A), a rewrite that lowers the linking prime below q* contradicts q*'s minimality directly — the
    exact lever the symmetric value-ascent lacked.
Open gaps: Step 3 — EXISTENCE of the covering-preserving, order-lowering rewrite operator. This is the whole
  difficulty; the builder must EXHIBIT it explicitly (small-case search on a_1∈{99,231,1155} to find the
  operator pattern first is advised) or report it cannot be built. Alternative mechanism to try if the direct
  exchange fails: aimo-0009 "shift-and-overshoot" — combine several SHIFTED instances of F1/GPC against the
  known mod-L_0 periodicity of S(·) to exclude a whole RESIDUE BLOCK for the minimal witness's class at once
  (stronger than plain pigeonhole), forcing the witness into a known-covering class.
Cases to cover: whether A has exactly one large prime (=q*) or several (rewrite target differs); the |P|=1
  base case (already certified elsewhere — cite, don't redo).
Watch out for: dividing out a prime is NOT free — primes(A/r) may lose covering and fail REAL clause (c), so
  the rewrite must ADD a compensating covering prime. Do NOT reuse the symmetric bad-partner relation as the
  descent (proven to give only one step). Report honestly if no operator is found — this is an UNVERIFIED
  transplant, expected to spend the round locating the operator, not assuming it.

---

covering-small-part-descent: advance
Target: the full theorem via (CSP)⟹theorem (certified) — value well-ordering / (6b) contradiction.
Technique: infinite-ascent on bad terms; (6a) unbounded family CLOSED (Lemma 6). Advance = attack (6b) with
  two fresh ingredients this round.
Skeleton (only the open tail — everything above (6b) is certified and imported):
  1. IMPORT: (CSP)⟹theorem; bad-partner+ascent; Lemma 6 (a single bad term ⇒ unbounded fixed-signature bad
     family m·r^k, same witness).
  2. **[OPEN (6b) — new ingredients.]** From the unbounded bad family + hub, derive a contradiction using:
     (A) **local hub-cover fact** (new, from star-config lens, certifiable): for the hub/bad term h,
     primes(h) is covering (REAL 𝒯⊆𝒞) but S(h) is not, so h's FINITELY many large primes Q(h) must JOINTLY
     cover W(h mod L_0) = ⋃_{q∈Q(h)}{i:q|a_i}. This is a LOCAL finite-capacity constraint on one hub (never
     sums over all hubs — distinct from the dead global Σ1/p² route).
     (B) **Window Purity** (from window-purity-class-cycle Step 2): every integer in each gap (a_n,a_{n+1})
     is non-covering — sharpens the interior structure of the ascent chain's windows.
  3. Contradiction ⟹ (CSP) ⟹ theorem.
Key lemmas: local hub-cover — because a term's prime set is covering (REAL) while a BAD term's small part is
  not, the deficit is carried by finitely many large primes, giving a finite-capacity handle on the (possibly
  infinite) missed-color set W(h). Combine with the number of colors any bad term MUST miss to seek overflow.
Open gaps: (6b) — turn (A)+(B) into a numeric contradiction. Reviewer flagged (round-5): the family is
  fixed-signature/sparse, so counting leverage is subtle; the missed-color-vs-|Q(h)| count does NOT obviously
  overflow (a bad term may miss ONE color with |Q(h)|=1). The builder must find the overflow or report it
  doesn't close.
Cases to cover: none new (base |P|=1 certified).
Watch out for: do NOT re-attack (6a) — closed. Do NOT invoke the global capacity count. Local hub-cover (A)
  is a candidate LEMMA — if it cannot close (6b) it should still be certified as a reusable local-capacity fact.

---

bad-residue-witness-index: advance
Target: the full theorem via (FIN-W)⟹theorem (certified Reduction Lemma) — attack the star config directly.
Technique: residue-level; rule out the star (hub small-disjoint from an infinite one-prime family). Advance =
  inject the round-7 mutual/cyclic REFINEMENT + Window Purity into the open Step 5.
Skeleton (only the open Step 5):
  1. IMPORT the certified Reduction Lemma and Steps 1–4 (star pigeonhole).
  2. **[OPEN — refined target.]** Replace the flat "rule out any star" with the SHARPER, certified-derivable
     claim (this round's finding): a single-sided infinite witness is HARMLESS (folds into finite Q_rel), so
     the star can only obstruct if witnessing is MUTUAL AND INFINITE on both sides (W(r) and W(r*) both
     infinite), i.e. a self-sustaining bipartite/cyclic infinite witness structure among the ≤L_0 bad classes.
  3. Rule out the mutual/cyclic structure using Window Purity (interior of each t_j's window is non-covering)
     + Lemma B window-spacing cap (multiples of p≥q* are ≥p apart in a length-a_1 window).
Key lemmas: mutual-witness-necessity — because for a class whose only obstruction is one hub, the finite prime
  pool Q(hub) already places every candidate of the class into E_∞ (Reduction-Lemma bookkeeping), giving no
  obstruction; so obstruction requires each side to feed the other infinitely, recursively.
Open gaps: closing the mutual/cyclic case. Same wall face, but the target is genuinely NARROWER than "star
  exists"; the builder should first CERTIFY the "single-sided-witness-is-harmless" reduction (derived by the
  explorer, NOT yet peer-checked — verify independently), which by itself is a strict sharpening of the wall.
Cases to cover: (i) single hub / single-sided (prove harmless — likely certifiable); (ii) mutual/cyclic (the
  residual wall).
Watch out for: the "single-sided harmless" claim is DERIVED-not-certified — the builder must re-derive it
  from the Reduction Lemma before relying on it. Do NOT re-run the Step-5 pigeonhole as if new (it is already
  baked into the star construction). aimo-0421's "coprime 3rd element" branch is PROVEN inapplicable (F1 makes
  the term family pairwise-intersecting) — do not attempt it.
