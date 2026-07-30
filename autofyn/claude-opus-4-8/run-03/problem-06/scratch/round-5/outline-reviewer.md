# Outline Review — imo-2026-06, Round 5

Standing spine reconfirmed computationally this round: (CSP) holds (0 bad terms on a_1∈{15,35,231}),
and a_1 < L_0 on all three (15<30, 35<210, 231<2310). So every approach must attack (CSP) by
contradiction (assume a bad term exists), and the window-CRT shortcut stays dead. All four candidates do
attack the whole claim end to end via the certified CSP⇒theorem reduction — no fragments, no proof split
across slugs.

The field has sat on ONE shared wall for 3+ rounds (the value-ascent Step 6a: turn the single symmetric
ascent into an unbounded/contradictory family). The diversity mandate is met this round by TWO genuinely
non-symmetric new framings. My job below is to confirm they are not disguised repeats of a proven-dead
route and that their skeletons are sound.

---

## bad-residue-witness-index — APPROVE (new, distinct framing)

Route: reformulate badness at the Z/L_0Z level; `R_bad ⊆ Z/L_0Z` = residues r with S(r) non-covering;
`W(r) = {i : primes(a_i)∩S(r)=∅}` is a FIXED per-class witness set (does not order terms by value →
sidesteps the symmetric mutual-pair trap). Dichotomy on W(r) infinite/finite + finite-factorization
pigeonhole.

Soundness check of Steps 1–4 (I verified each reduces to certified facts + a short computation):
- **Step 2 (badness is a residue property).** Correct: divisibility by each p≤P_max is fixed by m mod p,
  hence by m mod L_0 (CRT, certified descent Step 1a / csp-implies-theorem 1a). `|R_bad|≤2^{|P|}` finite. OK.
- **Step 3 (W(r)-large-link lemma).** For i∈W(r), any prime shared by a term m≡r and a_i must be LARGE:
  a small shared prime s | a_i, s≤P_max would put s∈S(a_i)∩S(m)=S(a_i)∩S(r), but primes(a_i)∩S(r)=∅ by
  definition of W(r) — contradiction. gcd(m,a_i)>1 by F1 forces the shared prime, necessarily large. VALID.
- **Step 4 (W(r) points to bad terms).** For i∈W(r), primes(m)∩S(a_i)=∅ (they share only large primes by
  Step 3), so m witnesses a_i bad. VALID — mirrors the certified bad-partner lemma.

**Gap (Step 5, both branches) is honest and correctly flagged.** The W(r)-infinite branch's pigeonhole
("m has finitely many primes, so one large prime p|m divides infinitely many a_i≡r* mod L_0") is
logically clean and NON-circular (it uses only the single term m and the a_i∈W(r), not E_∞ periodicity).
The builder MUST heed the outliner's own watch-out (c): "p divides infinitely many terms" is NOT by
itself a contradiction (E_∞ can contain infinitely many multiples of p) — the closure must consume the
combined off-lattice (GPC) + fixed-residue-class + pairwise-small-disjoint structure of that infinite
family. This is the real risk of the approach; it is stated as the gap, not hidden. No reliance on any
dead route (not covering/Helly, not global Σ1/p², not window-CRT). Build it.

## minimal-linking-prime-extremal — APPROVE (new, distinct framing) with one correction

Route: extremal prime `q* = min{large primes linking a small-disjoint term pair}` (well-ordering, since a
bad pair is assumed); every large link ≥ q* (non-symmetric handle independent of term value); local
per-window pigeonhole under GPC confinement; descent on WINDOW INDEX k.

Soundness:
- **Step 3 (q* well-defined, every link ≥ q*).** VALID by minimality/well-ordering.
- **Step 4 (per-window spacing cap).** VALID: consecutive multiples of any p≥q* are ≥q* apart, so a
  window of length <a_1 holds ≤ ⌊a_1/q*⌋+1 of them. Holds whether q*<a_1 or q*≥a_1 (cap = 1 in the latter).
- **Step 2 endpoints off-lattice.** Imported GPC + "every multiple of a_1 is good." VALID.

**CORRECTION required (does not block the build).** Step 5 offers two closure mechanisms; the FIRST is
flawed as written. It says finitely many bad windows "+ Step-5 single ascent already collide (the ascent
produces a bad term above every bad term)." That justification is FALSE: the certified bad-partner/ascent
lemma yields a strictly larger partner only for the SMALLEST bad term — it does NOT produce a bad term
above *every* bad term, so "finitely many bad terms" is fully consistent with the ascent and gives no
contradiction (this is precisely the symmetric-pair limitation). The builder must DROP this collision
argument. The SECOND mechanism — a self-contained descent on k (a bad window at k forces a q*-linked bad
window at strictly smaller k, then infinite descent on k≥1 contradicts directly) — is logically valid IN
PRINCIPLE and is the line to pursue. Whether the descent step is establishable is the honest open crux.
Heed the outliner's watch-out (c): the descent-on-k must not secretly re-assemble an infinite ascending
chain it cannot build (the 6a trap relocated to k). No reliance on the dead global capacity count (Step 4
is a strictly local per-window count). Build it, on the pure descent-on-k line only.

## covering-small-part-descent — APPROVE (advance, value-ascent carrier with a new lever)

Steps 1–5 certified (bad-partner + smallest-bad-term ascent, CSP⇒theorem). Only 6a/6b open. The NEW
lever this round is legitimate and non-circular in its stated part: the finite-signature pigeonhole
(S(m)⊆Q, ≤2^{|Q|} signatures, B_{s*} periodic mod L_0) is pure pigeonhole, not density, and the outliner
correctly re-flags the honest gap — "B_{s*} periodic does NOT make its elements terms" (the integer→term
jump) — and the aimo-0016 upgrade's "transport one index earlier" step as where the hard work lives. This
is the strongest-established distinct framing (proven ascent engine). Build it.

## reduced-process-identity — NOT BUILT this round (advance, holding carrier)

APPROVE as an outline (skeleton sound; RED_n ⟺ CSP at a_{n+1} is certified), but the outliner itself
states there is "no independent new closing mechanism this round" — the RED_n gap IS the shared wall and
this advance only keeps the induction framing alive to import the eventual closure. Per role memory
(NEVER build the reduction/induction spine holder unless a crux framing has actually closed for it to
import; keep the redundancy pair from both being built), building it would just re-hold the standing
partial and burn a builder slot that diversity needs elsewhere. It stays LIVE and top-of-Elo, ready to
import whichever crux closure lands, but is off the build set this round.

---

## Diversity assessment

Mandate MET. The build set spans three far-apart framings, none a covering-set/E_∞ variation of the
others:
- bad-residue-witness-index — attacks the crux at the Z/L_0Z residue level with a fixed witness index set
  (non-symmetric; pigeonhole on residue classes + one recurring large prime).
- minimal-linking-prime-extremal — extremal object is a PRIME (q*), induction relocated to WINDOW INDEX;
  strictly local per-window count.
- covering-small-part-descent — value-ascent with finite-signature pigeonhole + aimo-0016 upgrade.

Shared-wall risk remains real: all three still ultimately must convert a "single non-symmetric handle"
into an unboundedness/descent contradiction (the 6a wall in three disguises). Both new framings are AWARE
of this and route around it differently (residue-class recurrence vs window-index descent), so they are
worth running in parallel rather than collapsing to one. If BOTH new framings bottom out next round on
"one recurring object is not yet a contradiction," the orchestrator should treat that as the shared wall
persisting and seed a framing that attacks the greedy DYNAMICS directly (window-minimality of the actual
successor a_{n+1}), which none of the current live approaches exploits.

Ranking (post-update): reduced-process-identity 1630, covering-small-part-descent 1602,
bad-residue-witness-index 1520, minimal-linking-prime-extremal 1492, self-dual-clutter-grading 1475
(dead), large-prime-capacity-counting 1373 (dead).

build set: bad-residue-witness-index, minimal-linking-prime-extremal, covering-small-part-descent
