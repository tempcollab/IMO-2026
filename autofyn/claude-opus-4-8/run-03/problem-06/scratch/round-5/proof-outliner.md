## imo-2026-06

Standing reduction (CERTIFIED, imported by ALL approaches — do NOT re-prove): the whole
theorem `a_{n+T}=a_n+L for all n` follows from **(CSP)**: *no term is bad*, where term `m` is
**bad** iff `S(m):=primes(m)∩[2,P_max]` is non-covering (some term `B` has `primes(B)∩S(m)=∅`);
`P:=primes(a_1)`, `P_max:=max P`, `L_0:=∏_{p≤P_max}p`, `L=L_0`, `T=#(E*∩[a_1,a_1+L_0))`. Imports:
`enumeration-of-E-infinity`, `periodic-set-enumeration`, `csp-implies-theorem`,
`generalized-sole-connector-off-lattice` (GPC), `bad-partner-and-ascent`, `sole-connector-off-lattice`,
`term-density-and-prime-capacity`. Certified sub-fact used below: **S(m) depends only on m mod L_0**
(covering-small-part-descent Step 1a). The open crux is (CSP); Step-5 ascent is symmetric on a mutual
bad pair (one step, no chain). HARD-DEAD (never reopen): pure covering/Helly/sunflower (Prop D barrier);
global Σ_{p>P_max}1/p² capacity; window-CRT assuming a length-a_1 window holds a full residue system mod
L_0 (VERIFIED FALSE this round: a_1<L_0 for a_1∈{15,35,231}); self-dual-clutter-grading as a solve route;
targeting witness P_max-smoothness (237=3·79 good for a_1=231).

---

bad-residue-witness-index: new
Target: `a_{n+T}=a_n+L` for every n — the full periodicity claim, via (CSP).
Technique: residue-class reformulation of badness + fixed witness-index-set + finite-factorization
pigeonhole (KB: Pigeonhole/extremal §108,§188; CRT §59). Distinct route: attacks the crux at the
`Z/L_0Z` level with a FIXED per-class witness set — NON-symmetric, does not order terms by value, so it
sidesteps the symmetric mutual-pair trap that stalls the value-ascent engine.
Skeleton:
  1. (CSP) ⇒ theorem — imported (csp-implies-theorem / descent Step 1). Reduce to: no bad term exists.
  2. Badness is a residue property — by certified "S(m) depends only on m mod L_0", define
     `R_bad ⊆ Z/L_0Z` = residues r with `S(r)` non-covering. `|R_bad| ≤ 2^{|P|}` (finite). Suppose a bad
     term exists; then some inhabited class `r∈R_bad`. — by CRT + finiteness of subsets of {primes≤P_max}.
  3. Fixed witness set — `W(r):={i : primes(a_i)∩S(r)=∅}` depends only on r and the colors, not on which
     term in class r. For ANY term `m≡r (mod L_0)`, `S(m)=S(r)`, so for each `i∈W(r)`, `primes(a_i)∩S(m)=∅`
     yet `gcd(m,a_i)>1` (m is a term): **m shares a LARGE prime with every a_i, i∈W(r).** — by (ENUM)+F1.
  4. W(r) indexes bad terms — for `i∈W(r)`, m witnesses a_i's badness: `primes(m)∩S(a_i)=∅` (a common
     small prime would lie in primes(a_i)∩S(m)=∅). So every a_i (i∈W(r)) is itself bad, hence lies in some
     class of R_bad. — by the small-prime-disjointness computation (mirrors bad-partner lemma).
  5. Dichotomy + pigeonhole (THE CRUX STEP, gap):
     • W(r) infinite ⇒ {a_i:i∈W(r)} is an infinite set of bad terms in finitely many classes (R_bad),
       so one class r* holds infinitely many; the single term m has finitely many prime factors, so ONE
       large prime `p|m` divides infinitely many terms `a_i≡r* (mod L_0)`. These are infinitely many
       off-lattice (bad⇒off-lattice, GPC) terms in the fixed AP `p·k ≡ r* (mod L_0)`. Derive a
       contradiction from "one fixed large prime is the recurring large link across an infinite
       small-disjoint family in a single residue class."
     • W(r) finite ⇒ let `i*=max_{r∈R_bad} max W(r)`; every term a_i, i>i*, small-hits every bad class.
       Turn the finite conjunction "m shares a large prime with each of finitely many a_i (i∈W(r))" into a
       finite CRT object and rule out an inhabiting term directly.
Key lemmas (claim + mechanism):
  - Residue-level badness: `m∈R_bad` iff `S(m mod L_0)` non-covering — because divisibility by each p≤P_max
    is fixed by m mod p, hence by m mod L_0 (certified Step 1a).
  - W(r)-large-link: every term ≡ r shares a large prime with each a_i, i∈W(r) — because S(m)=S(r) misses
    primes(a_i) by definition of W(r), but gcd(m,a_i)>1 forces a shared prime, necessarily large.
  - W(r) points to bad terms — because m and a_i (i∈W(r)) share no small prime, so m witnesses a_i bad.
Open gaps: Step 5 (both branches) — the final contradiction. Everything in Steps 1–4 is imported-certified
+ short computations from certified facts.
Cases to cover: W(r) infinite vs finite (Step 5 branches). Base |P|=1 imported (descent Step 2).
Watch out for: (a) do NOT assume infinitely many terms lie in a fixed bad class — E_∞ is not yet known
periodic; only the SINGLE term m and the a_i∈W(r) are available. (b) Circularity check: Steps 2–4 use only
certified facts; the pigeonhole in 5 must not smuggle in E_∞-periodicity (that is the theorem). (c) "one
prime divides infinitely many terms" is NOT alone a contradiction — the off-lattice + fixed-class +
small-disjoint structure must be used.

---

minimal-linking-prime-extremal: new
Target: `a_{n+T}=a_n+L` for every n, via (CSP).
Technique: extremal principle on the LINKING PRIME (not term value) + local per-window pigeonhole under
GPC confinement + monovariant on window index (KB: Pigeonhole/extremal §108,§188; Invariants/monovariants
§117,§191; infinite descent §184). Distinct route: the minimal object is a prime `q*`, giving a
non-symmetric handle (every large link uses a prime ≥ q*) that the symmetric term-pair well-order lacks;
the induction is relocated from term value to WINDOW INDEX k. Escapes both dead barriers (not covering-set,
not global density — a strictly LOCAL count inside one window of length < a_1).
Skeleton:
  1. (CSP) ⇒ theorem — imported. Assume bad terms exist (toward contradiction).
  2. Every bad pair shares only large primes and both members are off-lattice — imported (bad-partner
     lemma + GPC): each bad term sits strictly inside an open window `(k a_1,(k+1)a_1)`, length < a_1, with
     a good a_1-multiple as each window endpoint.
  3. Extremal prime — `q* := min{ q>P_max : q | A and q | B for some small-disjoint term pair {A,B} }`,
     well-defined by well-ordering of ℤ_{>0} since a bad pair exists. **Every** large link anywhere uses a
     prime ≥ q*. — by minimality; genuinely non-symmetric (independent of term value).
  4. Local window pigeonhole — inside any window `(k a_1,(k+1)a_1)` (length < a_1), the multiples of a fixed
     prime `p≥q*` are ≥ q* apart, so at most `⌈a_1/q*⌉` of them occur; and any two bad terms in the SAME
     window linked by the SAME large prime are ≥ q* apart. — elementary spacing (NOT the dead global sum).
  5. Window-index monovariant (THE CRUX STEP, gap): show only FINITELY many windows `(k a_1,(k+1)a_1)`
     contain a bad term, e.g. by a quantity on k that strictly moves along any bad→partner step and is
     bounded, or by showing a bad window forces a q*-linked bad window at strictly smaller k (descent on k,
     not on value) until k is minimal — contradiction. Then finitely many bad windows + Step-5 single ascent
     already collide (the ascent produces a bad term above every bad term, needing unboundedly many windows).
Key lemmas (claim + mechanism):
  - Minimal-link floor: every large shared prime of a small-disjoint term pair is ≥ q* — because q* is the
    minimum over all such primes (well-ordering).
  - Per-window spacing cap: a window of length < a_1 holds < a_1/q* + 1 multiples of any single p≥q* —
    because consecutive multiples of p are p ≥ q* apart.
  - Off-lattice endpoints: each window's two endpoints are good a_1-multiples (S ⊇ P covering), so bad terms
    are strictly interior — imported (GPC + "every multiple of a_1 is good").
Open gaps: Step 5 — the window-index monovariant / descent-on-k that forces finitely many bad windows and
the contradiction. Steps 1–4 rest on imported certified facts + elementary spacing.
Cases to cover: q* linking two terms in the same window vs different windows; base |P|=1 imported.
Watch out for: (a) do NOT relapse into global Σ1/p² capacity — the count must stay inside a bounded band of
windows. (b) q*'s pair is NOT necessarily the value-minimal bad pair — do not conflate the prime-extremal
and value-extremal objects (that conflation is what makes the term well-order symmetric). (c) verify the
descent-on-k does not secretly re-derive an infinite chain it cannot build (the 6a trap in disguise).

---

covering-small-part-descent: advance
Target: `a_{n+T}=a_n+L` for every n, via (CSP) — value well-ordering / infinite-ascent (unchanged spine).
Technique: value-ascent engine (Steps 1–5 certified) + NEW finite-signature pigeonhole and aimo-0016-style
"infinitely-often ⇒ always" upgrade machinery for the gap (6a)+(6b).
Skeleton (Steps 1–5 imported-certified; only 6a/6b are open):
  6a. Unbounded family — upgrade the single symmetric ascent `m_0→m_1` to an unbounded bad-term set. NEW
      lever: finite-signature pigeonhole — `S(m)⊆Q={primes≤P_max}` ranges over ≤ 2^{|Q|} values, so along
      any putative bad family a fixed non-covering signature `s*` recurs; `B_{s*}={m:S(m)=s*}` is periodic
      mod L_0 (certified Step 1a), giving a bounded-gap recurring pattern to seed a fresh larger bad term
      from `q_0` and a P-prime — the non-symmetric increment the mutual pair lacks.
  6b. Contradiction — transplant the aimo-0016 crux ("upgrade an equal-infinitely-often relation on a
      bounded-alphabet windowed sequence to holds-for-all by a one-step downward induction with an auxiliary
      windowed-sum sequence") onto the signature/linking-prime pair to force a term-level conflict.
Key lemmas (claim + mechanism):
  - Finite signature alphabet: infinitely many bad terms ⇒ a fixed non-covering s*⊆Q repeats infinitely —
    because |Q|=π(P_max) is fixed, so only 2^{|Q|} signatures exist (pure pigeonhole, not density).
  - B_{s*} periodicity: {m:S(m)=s*} is a union of classes mod L_0 — certified Step 1a.
Open gaps: (6a) the non-symmetric increment; (6b) the term-level contradiction (the aimo-0016 upgrade's
"transport one index earlier" step is exactly where its hardest work lives — the honest gap).
Cases to cover: signature-repeats-with-same-linking-prime vs linking-prime-changes (persistence dichotomy).
Watch out for: (a) B_{s*} periodic does NOT make its elements terms — the gap is the jump from "integer with
signature s*" to "term in E_∞" (explorer-flagged stall). (b) Do NOT reuse the dead global capacity count.
(c) a_1 < L_0 (verified) ⇒ no window-CRT shortcut.

---

reduced-process-identity: advance
Target: `a_{n+T}=a_n+L` for every n, via (SL)/(CSP) — static set-inclusion / strong-induction form (the
field's Elo leader; keep the induction carrier live and ready to import the eventual crux closure).
Technique: strong induction (RED_n: S_{n+1} meets each S_1,…,S_n). Everything except RED_n certified.
Skeleton: reduction §1–§3a + GPC + easy direction imported; sole gap = RED_n (reverse inequality
β ≤ a_{n+1}).
NEW sub-lever this round (honest, limited): re-express RED_n's failure at the residue level — if a_{n+1} is
bad, its class r∈R_bad and the missed predecessor a_k has k∈W(r); combine with the bad-residue-witness-index
machinery once that approach produces a class-level contradiction. Record explicitly that the residue lever
CANNOT be closed by a window argument here: a_1 < L_0 (VERIFIED this round for a_1∈{15,35,231}), so the
window (a_n,a_{n+1}) need not contain a full residue system mod L_0 — the naive window-CRT is dead (matches
G3). This advance mainly keeps the induction framing alive and imports whichever crux closure lands.
Key lemmas: RED_n ⟺ (CSP) at the value a_{n+1} — certified equivalence (§4). GPC off-lattice — certified.
Open gaps: RED_n (the shared crux) — no independent new closing mechanism this round; value is as the
import target and induction-form witness of the crux.
Cases to cover: none new (base n=1 done; IH pairwise-intersecting family §5(G4)).
Watch out for: this is the shared-wall carrier — the reviewer should weight the two NEW far framings
(bad-residue-witness-index, minimal-linking-prime-extremal) as the diversity, not this advance. Do NOT let
the field collapse to this induction wall.
