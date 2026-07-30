## Status
partial

## Approaches tried
- **minimal-linking-prime-extremal** (round 5, NEW) — Extremal principle on the *linking prime* q* (min large prime that is a large link of some small-disjoint term pair), not on a term value; local per-window pigeonhole under GPC off-lattice confinement; induction relocated to the window index k. Rigorously established Steps 1–4 (imported certified lemmas + elementary spacing): (i) (CSP)⇒theorem imported; (ii) bad terms are off-lattice, pinned in open windows W_k=(k·a_1,(k+1)·a_1) of length a_1, imported GPC; (iii) **q\*** well-defined by well-ordering (a small-disjoint term pair exists once a bad term is assumed) and **every large link of a small-disjoint term pair is ≥ q\*** (the non-symmetric handle, independent of term value); (iv) **per-window spacing cap**: any window holds ≤ ⌊(a_1−1)/p⌋+1 ≤ a_1/q\*+1 multiples of a fixed prime p≥q\*, and two same-window terms linked by the same p≥q\* are ≥ q\* apart. Reformulated the crux as **"no minimal bad window"** (Step 5). HEEDED the reviewer: DROPPED the false "finitely many bad windows collide with the single ascent" closure (the certified ascent yields a larger partner only for the *smallest* bad term, so it never produces a bad term above *every* bad term). Honest GAP: the descent-on-k step itself — a bad term in W_k forcing a bad term/link in a strictly smaller window — is not established; it is difficulty-equivalent to the crux and I could not produce the downward step without re-assembling an infinite chain the structure does not supply (the relocated 6a trap). Status: partial.

*(Prior-round history for other slugs lives in current.md; this is a new slug.)*

## Current best

The whole theorem is reduced (certified) to **(CSP)**: every term m is *good*, i.e. its small part S(m):=primes(m)∩[2,P_max] meets primes(a_i) for every i (P:=primes(a_1), P_max:=max P). This slug attacks (CSP) by contradiction through a genuinely non-symmetric extremal object — the minimal linking prime q\* — and a strictly *local* per-window count, avoiding both dead barriers (covering/Helly and the global Σ1/p² capacity).

Rigorously in hand this round (Steps 1–4 below): q\* is well-defined and is a floor for every large link; bad terms are confined off-lattice inside length-a_1 windows; each window admits only ≤ a_1/q\*+1 multiples of any fixed p≥q\*. The crux is sharpened to the single statement **(DESC): the set of window indices k with W_k∩{bad terms}≠∅ has no minimum** — equivalently, a bad window forces a bad window of smaller index. (DESC) is the honest open gap and is difficulty-equivalent to (CSP); it is recorded, not papered over.

## Approach: extremal on the minimal linking prime, descent on the window index

Throughout, "term" means an element of the greedy sequence a_1<a_2<…; equivalently (certified `enumeration-of-E-infinity.md`, henceforth **ENUM**) a term is an element of E_∞∩[a_1,∞), where E_∞={m>1 : gcd(m,a_i)>1 ∀i}. Write P:=primes(a_1), P_max:=max P, L_0:=∏_{p≤P_max}p. For m>1 let S(m):=primes(m)∩[2,P_max] (its *small part*); a prime is *small* if ≤P_max, *large* if >P_max. Two terms are **small-disjoint** if S(A)∩S(B)=∅. A term m is **bad** iff S(m) is not covering, i.e. some term B (a *witness*) has primes(B)∩S(m)=∅.

We use the following **certified** facts (imported by reference, NOT re-proved here):

- **(ENUM)** `enumeration-of-E-infinity.md`: the sequence is the increasing enumeration of E_∞∩[a_1,∞).
- **(PER)** `periodic-set-enumeration.md`: a set tail-periodic from a_1 with period L yields a_{n+T}=a_n+L for every n.
- **(CSP⇒THM)** `csp-implies-theorem.md`: if (CSP) holds then a_{n+T}=a_n+L for all n, with L=L_0, T=#(E\*∩[a_1,a_1+L_0)), E\*={m>1:S(m) meets every primes(a_i)}.
- **(F1)** every two terms share a prime; every term is divisible by a prime of P (so S(t)≠∅); every multiple of a_1 is a term with small part ⊇P ("good"). (Used inside the certified lemmas above.)
- **(GPC)** `generalized-sole-connector-off-lattice.md`: if two terms are small-disjoint then a_1 divides neither — both lie strictly inside an open window between consecutive multiples of a_1.
- **(BPA)** `bad-partner-and-ascent.md`: every bad term m has a *bad* partner B≠m that is small-disjoint from m (they share only large primes), both off-lattice; and if any bad term exists, the smallest one m_0 has a strictly larger bad partner. NOTE (certified caveat): the partner relation is symmetric, so this gives only ONE upward step, never an infinite chain, and an infinite bad family is not by itself a contradiction.

### Step 1 — Reduction to (CSP), and the contradiction hypothesis

By **(CSP⇒THM)** it suffices to prove (CSP): every term is good. Suppose, for contradiction, that a **bad term exists**. All of Steps 2–5 run under this hypothesis; deriving a contradiction proves (CSP) and hence the theorem via the certified reduction. ∎(Step 1)

### Step 2 — Windows and off-lattice confinement

For an integer k≥1 let the **window** W_k:=(k·a_1,(k+1)·a_1) be the open interval between consecutive multiples of a_1; it has length a_1. Its endpoints k·a_1 and (k+1)·a_1 are multiples of a_1, hence terms, hence good (F1).

By **(BPA)** a bad term m has a bad, small-disjoint partner B, and by **(GPC)** both m and B satisfy a_1∤m, a_1∤B. Every integer that is not a multiple of a_1 and is ≥a_1 lies strictly inside exactly one window W_k (k≥1). Hence:

> **(2a)** Every bad term lies strictly inside some window W_k, k≥1. In particular the set K:={k≥1 : W_k contains a bad term} is a nonempty set of positive integers.

We also record a clean consequence of **(GPC)** used later:

> **(2b)** Every term T is small-disjoint from *no* multiple of a_1; i.e. T shares a small prime with every multiple of a_1. Indeed if S(T)∩S(M)=∅ for a multiple M of a_1, then {T,M} is small-disjoint, so by (GPC) a_1∤M — impossible. In particular a bad term B in W_k shares a small prime with each of its two window endpoints k·a_1,(k+1)·a_1.

### Step 3 — The minimal linking prime q\* (the non-symmetric handle)

Since a bad term exists, **(BPA)** gives at least one small-disjoint term pair {m,B}. By **(F1)** m and B share a prime; that prime is not small (S(m)∩S(B)=∅), so it is large. Hence the set

> Q\* := { q prime : q>P_max and ∃ terms A,B with S(A)∩S(B)=∅ and q|A and q|B }

is nonempty. By well-ordering of ℤ_{>0}, define **q\* := min Q\***.

> **(3a) Minimal-link floor.** For *any* small-disjoint term pair {A,B}, every prime they share is large (by the argument above, since S(A)∩S(B)=∅) and hence lies in Q\*, so is ≥ q\*. Thus **every large link of every small-disjoint term pair is ≥ q\***, and by (F1) such a pair shares *at least one* prime, necessarily large and ≥ q\*.

This is the distinctive, genuinely non-symmetric feature: q\* is a fixed prime attached to the whole configuration, not to any single (symmetric) bad pair, and it floors *every* large link uniformly — a handle the value-well-order of terms does not possess. Fix once and for all a witnessing pair {A\*,B\*}: terms, small-disjoint, with q\*|A\* and q\*|B\*, both off-lattice by (GPC).

### Step 4 — Local per-window spacing under q\*-confinement

Fix any prime p≥q\* and any window W_k (length a_1, open).

> **(4a) Per-window spacing cap.** The multiples of p in W_k are p·⌈(k·a_1+1)/p⌉, p·(⌈…⌉+1), …, consecutive ones differing by p≥q\*. An open interval of length a_1 contains at most ⌊(a_1−1)/p⌋+1 ≤ a_1/q\* + 1 of them. In particular, if q\*≥a_1 then W_k contains **at most one** multiple of any fixed p≥q\*.

> **(4b) Same-window linked terms are far apart.** If two distinct terms X,Y lie in the same window W_k and are both divisible by the same prime p≥q\* (e.g. they are a small-disjoint pair linked by p), then p|(Y−X) and 0<|Y−X|<a_1, forcing p<a_1; and |Y−X|≥p≥q\*. Consequently two same-window terms linked by a prime ≥a_1 cannot exist: **a small-disjoint pair linked by a prime ≥a_1 straddles two distinct windows.**

This is a strictly *local* count inside one length-<a_1 band; it never sums 1/p² over all primes, so it does not relapse into the proven-dead global-capacity route.

### Step 5 — The window-index descent (THE CRUX; open gap)

By (2a) the index set K={k≥1 : W_k has a bad term} is a nonempty subset of ℤ_{>0}; let **k\*:=min K** (well-ordering). Let m be a bad term in W_{k\*}. To reach a contradiction it suffices to establish:

> **(DESC).** If a bad term lies in W_k (k≥1), then a bad term lies in some window W_{k'} with 1 ≤ k' < k.

Granting (DESC), applying it to m∈W_{k\*} produces a bad term in a window of index <k\*, contradicting minimality of k\*. Hence no bad window exists, so no bad term exists, so (CSP) holds, and (CSP⇒THM) finishes the theorem. Thus **the entire remaining problem is (DESC)**.

**Reviewer's correction, heeded (recorded so it is never retried).** An earlier version of this step tried to close via "finitely many bad windows + the single certified ascent collide." That is FALSE: the (BPA) ascent produces a strictly larger bad partner only for the *smallest* bad term; it does not produce a bad term above *every* bad term, so "finitely many bad terms/windows" is entirely consistent with the ascent and yields no contradiction. That collision argument is DROPPED.

**Honest status of (DESC).** (DESC) is difficulty-equivalent to (CSP): a proof of (DESC) is exactly a proof that the bad-window set has no minimum, i.e. is empty. The extremal prime q\* supplies real structure toward it — every large link is ≥ q\* (3a), and the q\*-witness pair {A\*,B\*} together with (4a)/(4b) pins the coarse geometry — but I was **unable to produce the downward step**. Concretely, the natural attempts fail:

- *Descend along the witness pair.* The bad term m in W_{k\*} has a bad partner (BPA) and a q\*-link somewhere, but the partner may sit in a window of *larger* index (the relation is symmetric), and the shared prime being ≥ q\* gives no upper handle on the partner's window. There is no forced smaller-index bad term.
- *Descend along an endpoint.* By (2b), m shares a *small* prime with each window endpoint k\*·a_1, (k\*±1)·a_1; small links do not produce bad (small-disjoint) pairs, so they cannot seed a bad term in a neighbouring window.
- *Descend on the prime instead of k.* Producing a small-disjoint term pair sharing a large prime in (P_max, q\*) would contradict minimality of q\* and finish, but I have no construction of such a pair from {A\*,B\*}.

Each attempted descent either re-assembles an infinite ascending chain the structure does not build (the relocated 6a trap the reviewer warned of) or needs an input equivalent to (CSP). **(DESC) is therefore recorded as the single honest open gap of this approach.** I do not claim it; I claim only Steps 1–4 and the reduction of the crux to (DESC).

### What is rigorously proved vs. open

- Proved (imported certified + elementary): (CSP)⇒theorem; bad terms off-lattice in length-a_1 windows (2a); every term small-hits every a_1-multiple (2b); q\* well-defined and floors every large link (3a); per-window spacing cap (4a); same-window links are <a_1 apart / big links straddle windows (4b); the crux is equivalent to (DESC).
- Open: (DESC), the window-index descent step. This is the crux and remains unproved.

## Full proof
*Not present: Status is partial. The proof is complete through the reduction of the theorem to (DESC) (Steps 1–4), but (DESC) — the window-index descent — is an open gap.*

## Promotable lemmas

- **Minimal linking prime q\* (floor on large links).** *Statement:* Under the hypothesis that a small-disjoint term pair exists, the set Q\*={primes q>P_max : q divides both members of some small-disjoint term pair} is nonempty; set q\*=min Q\*. Then every small-disjoint term pair shares at least one prime, every prime it shares is large, and every such shared prime is ≥ q\*. *Proof:* Step 3 above (well-ordering + (F1) + definition of small-disjoint). Uses only certified (F1). Non-symmetric handle reusable by any extremal/descent attack.
- **Per-window spacing cap (local).** *Statement:* For any prime p≥q\* and any window W_k=(k·a_1,(k+1)·a_1), the number of multiples of p in W_k is ≤ ⌊(a_1−1)/p⌋+1 ≤ a_1/q\*+1 (and =at most 1 when q\*≥a_1); moreover two distinct terms in one window sharing a prime p≥q\* differ by a multiple of p that is <a_1, so p<a_1 (equivalently, a small-disjoint pair linked by a prime ≥a_1 straddles two windows). *Proof:* Step 4 above, elementary. Reusable local count that avoids the dead global Σ1/p² capacity.

*(Both are modest and rest on certified facts; offered for certification. The crux (DESC) is NOT promotable — it is unproved.)*
