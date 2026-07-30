# Outline review — imo-2026-06, round 10

Context: 4th+ collapse to ONE certified-equivalent wall (CSP = ℰ-small-only = (EC) = ¬(FIN-Q)). The
shared-gap rule required ≥1 genuinely-new *closing mechanism* off those four faces. I judged the three
fielded lanes for wrong technique / circularity / a 5th reformulation in disguise, and ran a small-case
sim (a1∈{15,35,99,231,1155}) confirming: gap ≤ a_1 on every seed, every term shares a prime with a_1
(so a multiple of a_1 is always a small-prime-only compatible successor within the window), 0 large-only
links (CSP holds). That last fact is decisive below.

---

## smallest-essential-prime-descent (NEW) — CHANGES REQUESTED / register + build

Genuinely-new *closing mechanism*: a minimal-counterexample value descent (aimo-0030 "Ana–Banana" Claim-3
transplant). Its TARGET is CSP/(EC) — as every live lane's must be, via the certified reduction — but it
does NOT merely re-state the wall in a new equivalent form: it brings a constructive descent that CHANGES
the object (cofactor B=q^r·y, cofactor-power realization, prime-indexed branch onto a smaller essential
prime q'∈U). That is exactly the shape of the standard "only primes ≤ threshold are load-bearing" proof,
and it is untried in this problem's history (prior value lanes minimize a term value / window index /
linking prime as a *floor*; this minimizes the realization n(T,q) and manufactures a strictly smaller
essential config).

Checks passed:
- Steps 1–4 ride certified lemmas only (enumeration, csp-implies-theorem, essential-connector-equivalence
  EC (a), essentiality propagation Lemma 14). It does NOT smuggle the circular cofactor-peel hypothesis
  ("peeled cofactor compatible with all earlier" — a corollary of the crux): U non-covering & essential
  is derived from certified Lemma 14, not assumed. Clean.
- Distinct well-founded order from the sibling value lane (realization value n(T,q) / prime-indexed
  inversion, vs the hub-value pigeonhole of covering-small-part-descent) — the two are kept apart.

Load-bearing gaps to close while building (do not hand-wave):
- **GAP A** — define the manufactured smaller object z from y with its config again essential AND a term ≥ a_1.
- **GAP B (crux-equivalent)** — the STRICT descent inequality n(new) < n(T,q). This is the whole game. B is
  a real risk of collapse: the T-avoiding witness B is merely *some* term (possibly huge), so the aimo-0030
  guarantee "x < n" is NOT automatic here; the outliner's proposed substitute (floor-tightness m_0 < a_1·p,
  used internally) applies to the global-minimum bad term, not to an arbitrary B. The builder MUST exhibit a
  genuinely smaller, genuinely-changed object — and if GAP B reduces verbatim to "no minimal covering set
  with a large prime realizes ≥ a_1" (the certified a_1-threshold stall), report the collapse honestly
  rather than paper over it. It is not provably circular (the cofactor-power/prime-indexed object is new),
  so the lane is worth one builder — but B is where it lives or dies.
- **GAP C** — the closure (minimality contradiction or iterated Claim-3 + support-monotonicity).
- Cases r=1 vs r≥2, U carrying another large q' (prime-indexed descent — show min large prime or realization
  strictly drops), and z<a_1 termination (small-prime-only support = covering = base-case contradiction).

Verdict: technique is right and genuinely new; the crux gap (B) is expected of any live lane here. Build it.

---

## greedy-successor-jump-monovariant (NEW) — RETHINK / not registered, not built

Fatal flaw — this is a 5th reformulation in a dynamical costume, and its load-bearing horn is unreachable.

1. **"Greedy dynamics" carries no information beyond the static E_∞ picture.** The certified `enumeration-of-
   E-infinity.md` says the sequence IS the increasing enumeration of E_∞ ∩ [a_1,∞). Hence a_{n+1} = min(E_∞ ∩
   (a_n,∞)) is a *function of the fixed set E_∞*; any "process potential" Φ_n is a function of E_∞ and n, with
   no external state. Window Purity ("(a_n,a_{n+1}) ∩ E_∞ = ∅") is literally "a_{n+1} is the next E_∞
   element" — definitional from ENUM. So the claim that this lane is "far from the four static faces" is
   refuted by a certified lemma: greedy minimality's *only* consequence beyond set-membership is the gap
   bound ≤ a_1, which is already certified and used. There is no new dynamical lever to exploit.

2. **The contradiction target (window overflow vs the gap bound, GAP 2 horn (b)) is unreachable.** A multiple
   of a_1 is always in E_∞ (every a_i shares a prime — necessarily small, ≤ P_max — with a_1; verified on all
   seeds), so a small-prime-only compatible successor exists in every a_1-window. The greedy successor is
   therefore NEVER forced onto a q_k-multiple, and "the least compatible integer exceeds a_{n_k}+a_1" simply
   contradicts the certified gap bound — i.e. it never happens. Horn (b) is vacuous, so GAP 2's dichotomy
   collapses to horn (a) "q_k is redundant" = "q_k not essential" = CSP itself. Circular.

3. The two load-bearing pieces are both broken for structural (not merely unfinished) reasons: GAP 1's
   monovariant Φ has, by the outliner's own admission, "NO ready-made analog" (aimo-0678's invariant sum s_n
   does not transplant), and by (1) no monovariant beyond the static E_∞ structure can exist; GAP 2's
   overflow horn is provably unreachable by (2). This is not a fixable gap — it is the wrong technique for
   this object.

Direction for the outliner: the dead premise is "the greedy rule gives information beyond E_∞." It does not
(ENUM). Do NOT re-field a process-potential / occupancy / recruitment-counting lane against the a_1-gap
(the round-8 recruitment "one slot per window" was already ruled a relabel of dead mechanisms). A genuinely
different lever must act on the covering CLUTTER or on a constructive descent (as smallest-essential-prime-
descent does), not on the successor-choice dynamics, which are certified-equal to the static picture.

Not registered (a RETHINK new angle never enters the pool), not built.

---

## covering-small-part-descent (ADVANCE) — CHANGES REQUESTED / build

Concrete new descent variable, not a bare re-advance: iterated floor-tightness (Lemma 9) on the HUB VALUE
v_k along the ¬(FIN-Q) class-graph walk (≤L_0 nodes), with a pigeonhole-forced repeat against a value
monovariant. This is a new mechanism attempt (Lemma 9 has only ever been applied ONCE, at the global
minimum); it is not provably circular, so it stays live. It reuses Lemma 9 as a *tool* with the sibling
smallest-essential-prime-descent but differs in well-founded order (value-walk pigeonhole vs prime-indexed
minimal counterexample) — the two are kept apart.

Gaps to close while building:
- **(i) THE gap** — the per-node value bound must actually decrease. Lemma 9 gives m_0 < a_1·p only at the
  GLOBAL smallest bad term; applying the shed-step "at EVERY node" needs a local minimality per node that is
  not yet established. Without it, the walk's value is not a monovariant and the pigeonhole yields no
  contradiction. This is the honest crux — build it or report the a_1-threshold stall honestly.
- **(ii)** Lemma 9 dichotomy Case A (no sheddable prime: C a minimal cover with a large prime) stalls the
  shed and must be absorbed by the walk structure, not a single shed.

Verdict: worth advancing as the value-carrier hedge; keep it honest about (i).

---

## Field / diversity note for the orchestrator

The genuinely-new mechanism this round is the constructive **smallest-essential-prime-descent** (aimo-0030
value descent). The mandated greedy-dynamics lane collapsed (ENUM makes dynamics = statics; the a_1-multiple
makes the overflow horn vacuous) — that avenue is now closed and should not be re-fielded as a successor-
choice potential. Both surviving build lanes are value/prime descents sharing Lemma 9 as a tool but with
distinct well-founded orders; if BOTH stall on the a_1-threshold again next round, the field will still be
one wall, and the outliner should look to a CLUTTER-level lever (a monovariant on ℰ / the essential-connector
configs) rather than another value-descent or FIN-Q reformulation.

Ranking after this round (Elo): covering-small-part-descent 1688 (top live carrier), enum-covering-primes
1597, reduced-process-identity ~1628 (parked spine), window-purity-class-cycle 1534, smallest-essential-
prime-descent 1521 (NEW), bad-residue-witness-index 1514, minimal-cover-small-only 1507 (dead), density-
bounded-recruitment 1511, bounded-window-distinctness 1453 (dead). smallest-essential-prime-descent anchored
below the established top carrier (which has 4 certified lemmas and is advancing), above both self-certified-
dead lanes, drawn with the stalled residue lane.

build set: smallest-essential-prime-descent, covering-small-part-descent
