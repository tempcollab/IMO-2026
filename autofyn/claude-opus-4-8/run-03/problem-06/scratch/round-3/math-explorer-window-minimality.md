## imo-2026-06

### Scope of this report
Assigned lens: window-minimality / rejected-integers hitting-set attack on the sole open
crux (Lemma A / Structural Lemma / R finite — every two terms share a prime ≤ P_max).
I did NOT re-derive the E_∞ reduction (certified, `lemmas/enumeration-of-E-infinity.md`,
`lemmas/periodic-set-enumeration.md`) or re-litigate Prop C / Prop D
(`lemmas/sole-connector-off-lattice.md`, `approaches/cofactor-recruitment-smoothness.md`
Steps 4–5) — I verified both hold up on inspection (Prop C's proof is a clean 4-line
contradiction, correct; Prop D's construction G'={{p1,q},{p2,q},{p1,p2}} is a genuine
valid pairwise-intersecting covering family with a large-prime minimal member, correct)
and then traced concrete rejection witnesses to probe exactly the question this lens was
assigned: can "why was x rejected" data be turned into a pigeonhole/hitting-set
contradiction forcing small-prime bridges?

### Method
For several seeds, generated the true greedy sequence (sympy), and for every window
(a_{n-1}, a_n), enumerated integers x in the open window that survive the *trivial*
rejection (share a prime with a_1), and for each such x computed the **full set of
earlier indices j with gcd(x, a_j) = 1** (the blocking witnesses). This directly exposes
the hitting-set structure the lens description asks about.

### Distinct openings surfaced

1. **Blocking is empirically concentrated on very few "hub" terms.** For a_1=99, almost
   every rejected 3·(large prime) candidate (111=3·37, 123=3·41, 129=3·43, 141=3·47,
   153=3·17, 159=3·53, 171=3·19, 177=3·59, 183=3·61, 189=3·7, 201=3·67, ... — dozens of
   cases across 60 windows) is rejected by **exactly one** earlier term: 110 = 2·5·11
   (later also 220 = 2²·5·11). I.e. the whole burden of excluding "3-only, large-cofactor"
   candidates from ever becoming terms is carried by a single hub term per epoch. This
   matches round-2's recruitment-mechanism finding (a_1=99 recruits 5 via witness 110) but
   sharpens it: the blocking is not diffuse, it is a **single witness per rejected
   candidate** in the overwhelming majority of cases (verified: distinct single-blocker
   hub terms are just {110,135} for a_1=99, {42,45} for a_1=35, {156,165,231} for a_1=143,
   {237} for a_1=231, across 400+ terms each).

2. **Mechanistic explanation of hubs (elementary, reusable bookkeeping — NOT new
   leverage on the crux).** If h ∈ E_∞ with primes(h) = S (S covering), then ANY m with
   primes(m) ⊇ S is automatically in E_∞ too (a superset of a covering set is covering).
   So once a "smooth-enough" covering set S is realized by some hub term h, every multiple
   of rad(S) — in particular h, 2h, 3h, ... whenever they preserve primes ⊇ S — re-enters
   E_∞ periodically, re-blocking the same residues forever. This is exactly the mechanism
   underlying the periodicity endgame already certified; it explains WHY the same hub
   (110, then 220=2·110, ...) recurs as blocker across many windows, but it is bookkeeping,
   not a new attack — it presupposes the covering set S is already established, which is
   the content of Lemma A itself.

3. **New, sharper reframing of the crux (the report's main finding): Lemma A is a
   REDUNDANCY statement, not a "witness smoothness" statement.** Tested a_1 = 231 =
   3·7·11 (P_max=11). Its hub term at index 3 is **237 = 3·79**, which genuinely contains
   a prime 79 > P_max = 11. This hub is NOT excluded and IS a legitimate term (matches the
   already-certified fact that large primes divide infinitely many terms — persistence ≠
   necessity, round-2 dead end). Traced its blocking role: candidate x=238=2·7·17 is
   rejected because gcd(238,237)=1 — i.e. 238 would need EITHER 3 or 79 to connect to 237,
   has neither. This shows large primes DO actively participate in the covering
   requirement that rejects candidates. I then searched exhaustively (up to 600 terms) for
   any actual term sharing **only** 79 with 237 (a genuine sole-connector pair for q=79) —
   **found none**: every term that does connect to 237 does so via 3 (its small anchor
   prime), even though nothing in the covering-set structure alone forbids a 79-only
   connector (consistent with Prop D). So the real content of Lemma A is not "hub/witness
   terms are P_max-smooth" (false — 237 itself is a counterexample to that phrasing) but
   **"whenever a large prime q could in principle bridge two terms, a small-prime bridge
   is always the one actually realized / no candidate ever ends up needing q as its ONLY
   option."** This is a materially different (and more accurate) way to state Gap G than
   round 2's "cofactor-smoothness of the witness" phrasing, and may be a cleaner target for
   the outliner: a **redundancy / alternative-bridge lemma**, not a smoothness bound.

4. **Cheap-kill, reconfirmed with a clean proof (not just numeric this time): a_1 a prime
   power makes Lemma A trivial.** If P = primes(a_1) = {p} (a_1 = p^k), every term must be
   divisible by p (its only way to satisfy gcd(·,a_1)>1), so ALL terms pairwise share p
   trivially — R = {p}, done, no large prime ever needed. This matches round-2's
   "single-winner" seeds {25,49,121,169} exactly and gives a rigorous (not just numeric)
   proof for that sub-case, useful as a base case if the outliner wants induction on |P|.

### Attempted pigeonhole/hitting-set closure — did NOT succeed (report honestly)
Tried to leverage finding 1 (concentration on 1–3 hub terms per seed) into a bound: if
only boundedly many hubs are ever needed to explain rejections in the P-lattice, maybe a
counting argument forces those hubs' own prime sets to stay small. This collapses into
exactly Gap G / Prop D's barrier: proving the hubs are themselves built from bounded
primes (equivalently, that IF a hub needs a large prime to be covering, a smaller
small-prime-only competitor would already have been picked by the greedy rule) is not a
generic counting fact — it requires the same greedy-minimality-in-a-window statement the
population has already isolated as irreducibly dynamical (Prop D). I could not find a
hitting-set/CRT argument that closes this without assuming the conclusion; this reconfirms
(does not merely repeat) round 2's finding that generic pigeonhole/CRT fails here (window
length a_1 vs. LCM of relevant primes can be arbitrarily mismatched), now witnessed
concretely on the a_1=231/hub-237 example rather than only asserted abstractly.

### Candidate technique(s)
- Redundancy/alternative-bridge reformulation (opening 3) — recommend the outliner
  consider restating Gap G as: "for every pair of terms (A,B) and every prime q ∈
  primes(A)∩primes(B) with q > P_max, there is ALSO some prime p ≤ P_max in
  primes(A)∩primes(B)" (i.e. large-prime intersections are always redundant, never
  exclusive) rather than "witness terms/cofactors are P_max-smooth" (falsified as a literal
  reading by the a_1=231/237=3·79 example — the term itself is fine, only *sole* large
  connections are forbidden). This is the same crux but phrased to avoid a wrong mental
  model (that large primes should be absent from factorizations, which is false and already
  flagged false by round 2's density dead-end).
- Minimal-counterexample induction on |P| (number of distinct primes of a_1), using finding
  4 as a clean base case (|P|=1 trivial) — untested for |P|=2 as an inductive step, flagged
  as a possible scaffold, not attempted here.

### Cheap-kill candidates
- **a_1 a prime power ⇒ Lemma A trivial** (finding 4 above, now with a rigorous 3-line
  proof, not just numeric confirmation). Cheap, reusable, but only disposes of a narrow
  sub-case (|P|=1); does not touch the general |P|≥2 crux.
- No other structural pruning found; parity/size-bound/injection ideas did not surface
  anything beyond what's already certified (gaps ≤ a_1, every term hits P).

### Knowledge-base entries to use
- Pigeonhole / extremal principle — tried and found insufficient here (see "Attempted
  pigeonhole" above), consistent with round 2's finding; record as tried-and-insufficient
  rather than re-suggesting it as fresh.
- Modular arithmetic / CRT — supports opening 2's bookkeeping (multiplicative closure of
  E_∞ under prime-superset) but not a lever on the crux itself.
- No new KB entry identified beyond what round 1–2 already flagged (Bertrand's postulate
  as a plausible-but-unconfirmed tool for smoothness of the smallest element of a window,
  still unexploited).

### Analogous past problems (cruxes)
Did not find a new corpus analogue beyond what round 1–2 already surfaced (aimo-0447's
prime-capacity grid, aimo-0678's finite-state monovariant). Neither supplies the
redundancy/alternative-bridge mechanism opening 3 identifies; this still looks like a
genuinely novel argument for the corpus.

### Prior progress
Unchanged from `current.md`: full reduction to Lemma A (three equivalent phrasings),
Prop C (sole-connector terms avoid the a_1-lattice), Prop D (set-level barrier — any proof
needs greedy dynamics), Gap G stated as cofactor-smoothness. This report's opening 3
proposes restating Gap G as a redundancy/alternative-bridge statement, which is logically
equivalent to Lemma A but empirically better matches what actually happens (large primes
appear in terms freely; they are just never the *sole* bridge) — hand this reframing to the
outliner as a phrasing option, not a new proved fact.

### Dead ends (do not retry)
- **Pigeonhole/hitting-set closure from blocking-witness concentration** (this round,
  "Attempted pigeonhole" above) — even though blocking is empirically concentrated on 1–3
  hub terms, closing the crux this way requires knowing the hubs are themselves
  small-prime-built, which is circular (same content as Gap G / Prop D barrier). Do not
  spend a build round trying to convert "few hubs observed" into a proof without a genuinely
  new mechanism for bounding hub smoothness.
- **"Witness/hub terms must be P_max-smooth"** as a literal target — falsified by the
  a_1=231 example (hub 237=3·79 legitimately contains a prime >P_max and is a completely
  valid term). The correct target is redundancy of large-prime bridges, not absence of
  large primes from factorizations. Flagging so no approach wastes effort trying to prove
  the false stronger smoothness claim.

### Small-case / intuition notes (all conjectural — numeric only)
- Single-blocker hub sets stay very small (1–3 distinct terms) across all four seeds tested
  (a_1 ∈ {99,35,143,231}, 400–600 terms each) — consistent with, but not proof of, Lemma A.
- a_1=231/hub-237 case: exhaustive search over 600 terms found zero pairs whose exact
  common-prime intersection is {79} (or any prime >11) — Lemma A holds on this seed with a
  concrete large prime actively "in play" but never load-bearing, the most informative
  single data point produced this round for why the crux is subtle (large primes are
  common and functionally present, yet provably redundant whenever they matter).
