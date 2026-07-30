## Status
partial

## Approaches tried
- **covering-small-part-descent** (round 10, ADVANCE) — Attacked the outliner's concrete new descent
  variable: **iterated hub-VALUE floor-tightness (Lemma 9) along the ¬(FIN-Q) class-graph walk**, with
  pigeonhole on the ≤L_0 residue nodes, aiming to make the hub value a well-founded monovariant. Delivered
  one gap-free NEW lemma and a crisp, honest pinning of why the mechanism cannot descend:
  * **Lemma 15 (Hub abundance under ¬(FIN-Q), NEW, gap-free).** For an E_∞-inhabited bad class `r_0` with
    `Q(r_0)` infinite: (a) a **finite transversal** `D` of the witness-color family `{Q_i : i∈W(r_0)}`
    exists (take `D = Q(m_1)` for any hub `m_1`); (b) the hub set `H_{r_0} := {m ≥ a_1, m ≡ r_0 (mod L_0) : m∈E_∞}`
    is **infinite** (CRT on `m≡r_0 (mod L_0)`, `∏D | m`, using (★)); (c) every hub `m∈H_{r_0}` is a **bad
    term** with `S(m)=S(r_0)` non-covering and `Q(m)` a transversal of `{Q_i}`. This rigorously constructs
    the infinite family of bad hubs on which the walk was to run — the setup the outline demanded.
  * **The honest GAP (i), now PINNED with two independent structural obstructions (NEW).** The assigned
    descent CANNOT be made a monovariant, for reasons intrinsic to the mechanism, not merely unfinished:
    - **(Obstruction 1 — shed leaves the node set.)** Every Lemma-9 shed step divides out a prime `p`
      (large in case (i), or a small redundant prime in case (ii)); in BOTH cases `p` changes the residue
      `m mod L_0` (a large `p ∤ L_0` shifts it; a small `p | L_0` also shifts it). So a value-descent step
      is *orthogonal* to the class-graph walk (which lives on `ℤ/L_0ℤ`): you cannot shed value while
      staying on the finite node set. The pigeonhole (finite nodes) and the descent (shed) never combine.
    - **(Obstruction 2 — the hub value is a class-function.)** If instead the descent variable is
      `v(r) := min H_r` (smallest hub of the visited class `r`), then `v(r)` is a **function of `r`**:
      revisiting a node returns the SAME value, not a smaller one. Pigeonhole gives a repeated node with
      *equal* `v`, no strict decrease, no contradiction. To force `v(r_k) < v(r_j)` on a revisit `r_k=r_j`
      one would need the smallest hub of a fixed class to depend on the walk history — it does not.
  So the iterated-floor-tightness value-walk **stalls at the same a_1 threshold**: Lemma 9's per-node shed
  only yields a smaller bad term when it stays `≥ a_1` (unproven off the global minimum), and even when it
  does, the shed exits the class, so the ≤L_0-node pigeonhole has nothing to bite on. Honest residual GAP
  unchanged in kind (the wall = "no minimal covering set with a large prime realizes `≥ a_1`"); but the
  advance is genuine: Lemma 15 (infinite bad-hub family) is new and gap-free, and the round now records
  *precisely why* the value-walk descent variable is not well-founded (two structural obstructions), so no
  future round re-fields it blindly. Status: partial (advanced — Lemma 15; value-walk stall pinned).
- **covering-small-part-descent** (round 9, ADVANCE) — Leaned on the essential-witness value pressure
  (each essential witness `B_p` is a term `≥ a_1`) exactly as the reviewer directed. Delivered two
  gap-free items that recast (6b) as a crisp **value/divisibility** statement — the sharpest form yet in
  this lane, genuinely distinct from the set-theoretic ℰ-small-only:
  * **(EC) Essential-connector equivalence (NEW, gap-free).** CSP fails ⟺ some **large** prime `q` is an
    *essential connector* for some non-covering prime set `A` — meaning **every `A`-avoiding term is
    divisible by `q`** (equivalently `A∪{q}` is covering while `A` is not). Both directions proved
    (Lemma 13). This turns the crux from "a minimal cover carries a large prime" into a concrete
    arithmetic assertion about term-divisibility, the value form the outliner asked for.
  * **(Essentiality propagation, NEW, gap-free).** In any essential-connector config `(A,q)`, **every**
    `A`-avoiding term `B` has `q` essential inside it (`primes(B)\{q}` non-covering): otherwise the
    covering set `primes(B)\{q}` realizes (REAL c) an `A`-avoiding term coprime to `q`, contradiction.
    So the config self-reproduces to `(primes(B)\{q}, q)` (Lemma 14). Uses "`N` is a term" (value
    method), Prop-D-compliant.
  Honest residual GAP unchanged in kind: `q` **recurs** under propagation (Lemma 14 gives no descent on
  `q`, `rad`, or `|·|`); the essential-witness value pressure yields the crisp EC reformulation and its
  self-propagation but **no downward monovariant**, so the mechanism stalls at the same wall. Status:
  partial (advanced — EC-equivalence + propagation; crux recast as a value/divisibility statement, not
  closed).
- **covering-small-part-descent** (round 8, ADVANCE) — Attacked the crisp value inequality (6b)
  ("no minimal covering set with a large prime realizes ≥ a_1") with the essential-witness value
  pressure the outliner assigned. Delivered three gap-free items, none of which closes (6b), but
  which sharpen the wall decisively:
  * **Equivalence (CSP ⟺ ℰ-small-only), both directions rigorous.** The reverse direction
    (CSP ⟹ ℰ-small-only) is NEW: a minimal covering set with a large prime, power-inflated to
    value ≥ a_1, is *always* a bad term. Consequence: the value-descent target (6b) and the sibling
    approach `minimal-cover-small-only`'s target ℰ-small-only are the **same statement**, not
    independent bets — a rigor correction to the outline's "keep the two independent" premise.
  * **Case-split reduction showing the "crisp value inequality" (VI′) is strictly too weak.** The
    minimal covering skeleton `C'` of a smallest bad term splits into Case I (rad(C′) ≥ a_1, closed
    by VI′) and Case II (rad(C′) < a_1, NOT touched by VI′). Since minimal covers with radical < a_1
    genuinely exist, VI′ cannot close (6b). This corrects the round-7 file's assertion that VI′
    "would close (6b)".
  * **Essential-witness spawning lemma (NEW, value mechanism).** A minimal covering set `C'` with
    large prime `q` forces, via its `q`-witness term `B_q`, a *distinct* minimal covering set `C''`
    with `q ∈ C''` and `C'' ∩ C' = {q}`. A genuine structural constraint on the clutter obtained by
    value methods (uses "`N` is a term", Prop-D-compliant), distinct from the sibling's pure
    transversal argument.
  Honest residual GAP: ℰ-small-only itself (= (6b) = CSP). The spawning lemma yields no downward
  monovariant (q recurs; no descent), so the value mechanism stalls at the same wall. Status:
  partial (advanced — equivalence + reduction + spawning lemma; the crux is re-identified exactly,
  not closed).
- **covering-small-part-descent** (round 7, ADVANCE) — Lemma 7 (Window Purity), Lemma 8 (Local
  Hub-Cover), Lemma 9 (Minimal-bad-term floor-tightness: v_p(m_0)≥2 ⟹ m_0<a_1·p). All certified.
  GAP: (6b) blocked at the a_1 threshold. Status: partial.
- **covering-small-part-descent** (round 5, ADVANCE) — Lemma 6 (bad-signature geometric family),
  closing sub-gap (6a). Status: partial.
- **covering-small-part-descent** (round 4, NEW) — value ascent framing; (CSP)⇒theorem; base case;
  bad-partner + single ascent. GAP: Step 6→7. Status: partial.

## Current best

The whole theorem is reduced, fully rigorously (certified `lemmas/csp-implies-theorem.md`), to

> **(CSP)** — *No term is bad*, where a term `m` is **bad** iff its small part
> `S(m) := primes(m) ∩ [2,P_max]` is non-covering.

**New round 10 (gap-free deliverable + honest pinning).** Attacking the assigned descent variable
(iterated hub-value floor-tightness along the ¬(FIN-Q) class-graph walk), I proved **Lemma 15 (Hub
abundance under ¬(FIN-Q))**: for an inhabited bad class `r_0` with `Q(r_0)` infinite, a finite transversal
`D` of `{Q_i : i∈W(r_0)}` exists, the hub set `H = {m ≥ a_1, m≡r_0 (mod L_0) : m∈E_∞}` is infinite, and every hub is
a bad term with `S(m)=S(r_0)` and `Q(m)` a transversal — the concrete infinite bad-hub family the walk
required. But I then **pinned GAP (i)** (per-node minimality) as a *structural incompatibility*, not a
missing step: **(Obstruction 1)** a single finite transversal `D` already forces infinitely many hubs, so
`Q(r_0)`'s infinitude exerts no value/overflow pressure; **(Obstruction 2)** every Lemma-9 shed step divides
out a prime and so *changes the residue mod `L_0`*, exiting the finite node set — the value-descent is
orthogonal to the class-graph pigeonhole, and the only class-intrinsic value `min H_r` is a function of the
node (constant on revisits, no monovariant). So the iterated value-walk stalls at the same a_1 threshold;
the deliverable is Lemma 15 (gap-free) plus the diagnosis retiring this descent variable.

**New round 9 (all gap-free).** Leaning on the essential-witness value pressure (each essential witness is
a term `≥ a_1`), I recast the crux as a crisp term-divisibility statement:
- **(EC) Essential-connector equivalence (Lemma 13).** CSP fails ⟺ some large prime `q` is an *essential
  connector* for some non-covering set `A` — every `A`-avoiding term divisible by `q` (⟺ `A ∪ {q}`
  covering, `A` not). So CSP ⟺ **(EC):** for every non-covering `A` and large `q`, some `A`-avoiding term
  is not divisible by `q`. This is the value/arithmetic face of the crux, in this lane's spirit.
- **Essentiality propagation (Lemma 14).** In a failing config `(A,q)`, every `A`-avoiding term `B` has
  `primes(B)\{q}` non-covering, so `(primes(B)\{q}, q)` is again a failing config — the SAME `q`. The
  config self-reproduces but `q`, `rad`, size all recur: no downward monovariant, so the mechanism stalls.
  This pins the honest wall in its crispest value form.

**Round-8 items (all gap-free).** I identify the crux exactly and correct the round-7 target:

- **(EQ) CSP ⟺ ℰ-small-only.** No term is bad **iff** every minimal covering set is a subset of
  `[2,P_max]` (no large prime is load-bearing in any minimal cover). Both directions proved below
  (Lemma 10). The reverse direction is new and shows (6b) is *literally* the sibling approach's
  ℰ-small-only target.
- **(VI′ is too weak.)** The round-7 "crisp value inequality" — no minimal covering set with a large
  prime has minimal realization `≥ a_1` — is, read as *radical* `≥ a_1` (VI′), only the Case-I half
  of the skeleton split (Lemma 11); Case II (radical `< a_1`) is untouched and genuinely occurs, so
  VI′ does **not** close (6b). Read as *some* realization `≥ a_1`, it is trivially true (powers of
  any prime of `C'` cross `a_1`) and equivalent to ℰ-small-only. Either reading, the "value
  inequality" framing collapses onto ℰ-small-only.
- **(Spawning, Lemma 12.)** Any minimal covering `C'` with large prime `q` forces a *distinct*
  minimal covering `C''` with `q ∈ C''`, `C'' ∩ C' = {q}`. Partial structural progress toward
  ℰ-small-only through the value mechanism; but it produces no downward well-founded quantity, so
  the descent stalls (the honest gap).

The residual GAP is **(EC) = ℰ-small-only = (6b) = CSP**: equivalently, rule out any large prime being an
essential connector for a non-covering set (Lemma 13), i.e. force some `A`-avoiding term coprime to `q`.
The value/essential-witness mechanism sharpens the structure (Lemmas 12–14) but does not close it: Lemma
14 shows the failing config self-reproduces with `q` fixed, giving no downward monovariant.

---

### Imported certified facts (used verbatim, NOT re-proved)

- **(ENUM)** `lemmas/enumeration-of-E-infinity.md` — the sequence is the increasing enumeration of
  `E_∞ ∩ [a_1,∞)`, `E_∞ = {m>1 : gcd(m,a_i)>1 ∀i}`.
- **(REAL)** `lemmas/realizability-and-self-dual-clutter.md` Lemma 1: for a finite prime set `S`,
  (a) `S` covering ⟺ (b) some term has prime set exactly `S` ⟺ (c) every integer `≥ a_1` with prime
  set `⊇ S` is a term. Hence `𝒯 ⊆ 𝒞`.
- **(CLUT)** same file, Lemma 2: `𝒞` is an up-set of finite sets, so every covering set contains a
  minimal covering set (an edge of `ℰ`); `b(ℰ)=ℰ`.
- **(F1 / Lemma 0)** every two terms share a prime; every term meets `P`, so `S(t) ≠ ∅` for every
  term `t`.
- **(GPC)** `lemmas/generalized-sole-connector-off-lattice.md` — two terms sharing no small prime are
  both off the `a_1`-lattice.
- **(CSP⇒thm)** `lemmas/csp-implies-theorem.md`.
- Lemmas 6–9 as certified (`bad-signature-geometric-family.md`, `window-purity.md`,
  `local-hub-cover.md`, `minimal-bad-term-floor-tightness.md`).

Throughout, `P := primes(a_1)`, `P_max := max P`; a prime is *small* if `≤ P_max`, *large* if
`> P_max`; `Q(m) := primes(m) ∩ (P_max,∞)`; `rad(S) := ∏_{p∈S} p` for a prime set `S`. `ℰ` = the
clutter of minimal covering sets. **ℰ-small-only** = "every `C' ∈ ℰ` satisfies `C' ⊆ [2,P_max]`".

Two standing observations used repeatedly:
- **(O1)** `{q}` is never covering for a large prime `q`: `q ∤ a_1` (as `primes(a_1)=P ⊆ [2,P_max]`),
  and `a_1` is a term, so `{q} ∩ primes(a_1) = ∅`. Hence any covering set containing a large prime,
  and in particular any minimal covering set containing a large prime, has size `≥ 2`.
- **(O2)** every minimal covering set `C' ∈ ℰ` meets `P`: `C'` is covering and `a_1` is a term, so
  `C' ∩ primes(a_1) = C' ∩ P ≠ ∅`. Thus a minimal cover containing a large prime also carries a
  small prime of `a_1`'s own factor set (the §3 free fact of the value-inequality explorer).

---

### Lemma 10 (Equivalence CSP ⟺ ℰ-small-only) — COMPLETE

*Statement.* No term is bad ⟺ every minimal covering set is a subset of `[2,P_max]`.

*Proof.*

**(⇐) ℰ-small-only ⟹ CSP.** Suppose every `C' ∈ ℰ` satisfies `C' ⊆ [2,P_max]`, and suppose toward a
contradiction that a bad term `m` exists. Let `C := primes(m)`; by (REAL) `𝒯⊆𝒞`, `C` is covering. By
(CLUT), `C` contains a minimal covering set `C' ∈ ℰ`. By hypothesis `C' ⊆ [2,P_max]`, so
`C' ⊆ C ∩ [2,P_max] = S(m)`. Since `C'` is covering and covering sets are superset-closed within
`primes(·)`, and `S(m) ⊇ C'` with `C'` covering, `S(m)` meets every term (any term met by `C'` is met
by its superset `S(m)`), i.e. `S(m)` is covering. This contradicts `m` bad (`S(m)` non-covering).
Hence no term is bad.

**(⇒) CSP ⟹ ℰ-small-only.** Suppose no term is bad, and suppose toward a contradiction some
`C' ∈ ℰ` contains a large prime `q`. We produce a bad term with prime set exactly `C'`.

Let `R := rad(C') = ∏_{p∈C'} p`. Fix any prime `p_1 ∈ C'` (e.g. `p_1 = q`), and let `k ≥ 0` be the
least integer with `N := R · p_1^{k} ≥ a_1`. Then:
- `primes(N) = C'` exactly: multiplying `R` by copies of `p_1 ∈ C'` adds no new prime and drops none.
- `N ≥ a_1` and `primes(N) = C' ⊇ C'` with `C'` covering, so by (REAL) clause (c), `N` is a term.
- `S(N) = primes(N) ∩ [2,P_max] = C' ∩ [2,P_max]`. Since `C' ∈ ℰ` is a minimal cover and `q ∈ C'` is
  large, `C' \ {q}` is non-covering (minimality); and `C' ∩ [2,P_max] ⊆ C' \ {q}` (as `q` is large,
  `q ∉ [2,P_max]`). A subset of a non-covering set is non-covering (if it missed no color it would be
  covering, hence so would every superset). Therefore `S(N)` is non-covering, i.e. `N` is **bad**.

So `N` is a bad term, contradicting CSP. Hence no `C' ∈ ℰ` contains a large prime, i.e. every
`C' ∈ ℰ` is `⊆ [2,P_max]`. ∎ (Lemma 10)

*Consequence.* The value-descent crux (6b) = CSP is **exactly** the sibling approach's ℰ-small-only.
There is no strictly-weaker "value inequality" separating the two: any minimal cover with a large
prime, once it exists, is *realized as a bad term* (its power-inflation `N`), so its mere existence
already breaks CSP. The two approaches share the SAME target; they differ only in *mechanism*
(value/essential-witness here vs. pure transversal in the sibling).

---

### Lemma 11 (Skeleton case-split; why VI′ handles only Case I) — COMPLETE

*Setup.* Assume a bad term exists; by well-ordering let `m_0` be the smallest, `C := primes(m_0)`
(covering, by (REAL)), `S(m_0) = C ∩ [2,P_max]` non-covering. As `S(m_0) ⊊ C` fails to cover while
`C` covers, `C` contains a large prime, i.e. `Q(m_0) ≠ ∅`. Fix a minimal covering `C' ⊆ C`
(exists by (CLUT)); `C'` contains a large prime, for otherwise `C' ⊆ C ∩ [2,P_max] = S(m_0)` and then
`S(m_0) ⊇ C'` would be covering — contradiction. Write `R := rad(C')`.

*Claim.* Exactly one of:
- **Case I** (`R ≥ a_1`): then `C = C'` is itself a minimal covering set, `m_0 = R = rad(C)` is
  squarefree, and `m_0 ≥ a_1` is a minimal-cover realization at its radical.
- **Case II** (`R < a_1`): then `C' ∈ ℰ` is a minimal cover with a large prime whose radical is
  `< a_1`; nothing further about `m_0` is forced by the descent.

*Proof.* **Case I.** If `R ≥ a_1`, then `R` has prime set exactly `C' ⊇ C'` covering, `R ≥ a_1`, so by
(REAL c) `R` is a term. Its small part is `C' ∩ [2,P_max] ⊆ C' \ {q}` (q the large prime of `C'`),
non-covering (as in Lemma 10); so `R` is bad. By minimality of `m_0`, `R ≥ m_0`. But
`R = rad(C') ≤ rad(C) ≤ m_0` (since `C' ⊆ C` and `m_0` is a multiple of `rad(C)`). Hence
`R = rad(C') = rad(C) = m_0`. `rad(C') = rad(C)` with `C' ⊆ C` forces `C' = C`; `rad(C) = m_0` forces
`m_0` squarefree. So `C = C'` is a minimal cover and `m_0 = rad(C)`.

**Case II.** If `R < a_1`, `C'` is a minimal cover with a large prime and `rad(C') < a_1`. (This case
does occur: minimal covers with radical below `a_1` exist — e.g. for `a_1 = 15`, `{2,3}` is minimal
covering since every term shares a prime with the term `a_2 = 18 = 2·3²`, and `rad{2,3} = 6 < 15`.) ∎
(Lemma 11)

*Why VI′ is too weak.* The round-7 "crisp value inequality" read as **VI′ := no minimal covering set
with a large prime has radical `≥ a_1`** kills exactly Case I (it forbids the `m_0 = rad(C)` of Case I).
It says nothing in Case II, where the skeleton's radical is already `< a_1`. And Case II is not
vacuous: by Lemma 10, a Case-II skeleton `C'` still power-inflates to a bad term `N` (its own witness),
so Case II is a genuine route to a bad term that VI′ cannot block. Concretely, VI′ is *strictly weaker*
than ℰ-small-only, whereas closing (6b) needs the full ℰ-small-only (Lemma 10). The correct target is
therefore ℰ-small-only, not VI′.

---

### Lemma 12 (Essential-witness spawning) — COMPLETE

*Statement.* Let `C' ∈ ℰ` be a minimal covering set containing a large prime `q`. Then there is a
minimal covering set `C'' ∈ ℰ` with `q ∈ C''`, `C'' ∩ C' = {q}`, and `C'' ≠ C'`.

*Proof.* By (O1), `|C'| ≥ 2`. By minimality, `C' \ {q}` is non-covering: there is a term `B` with
`primes(B) ∩ (C' \ {q}) = ∅`. As `B` is a term, `primes(B)` is covering (`𝒯⊆𝒞`), so
`primes(B) ∩ C' ≠ ∅`; being disjoint from `C' \ {q}`, this forces `q ∈ primes(B)` and
`primes(B) ∩ C' = {q}`. Call this witness `B_q := B` (so `q ∣ B_q` and `B_q` shares no other prime of
`C'`).

`primes(B_q)` is covering and finite, so by (CLUT) it contains a minimal covering set
`C'' ∈ ℰ`, `C'' ⊆ primes(B_q)`. Then
`C'' ∩ C' ⊆ primes(B_q) ∩ C' = {q}`.

Now realize `C'` as a term: by Lemma 10's construction, let `N ≥ a_1` be `rad(C')` times a power of a
prime of `C'`, so `primes(N) = C'` exactly and `N` is a term (REAL c). Since `C''` is covering and `N`
is a term, `C'' ∩ primes(N) = C'' ∩ C' ≠ ∅`. Combined with `C'' ∩ C' ⊆ {q}`, this gives
`C'' ∩ C' = {q}`; in particular `q ∈ C''`. Finally `C'' ≠ C'`, since `C'' ∩ C' = {q} ⊊ C'`
(as `|C'| ≥ 2`). ∎ (Lemma 12)

*Remark (value mechanism, and where it stalls).* Lemma 12 is obtained by value methods: it crucially
uses that `N` (a specific integer `≥ a_1` with prime set `C'`) is an actual **term**, i.e.
Realizability's `a_1`-threshold — it is not a pure set-system fact (Prop-D-compliant; the abstract
clutter alone does not force `C''` to meet `C'`). It shows minimal covers with a large prime cannot
occur in isolation: each such `C'` spawns another `C''` sharing exactly `{q}`. But `q` **recurs** in
`C''` and `|C''| ≥ |C'|` is not forced downward, so this produces no well-founded monovariant. The
essential-witness pressure the outliner assigned yields a genuine new structural constraint but **not**
a contradiction. This is the honest wall.

---

### Lemma 13 (Essential-connector equivalence — the value form of the crux) — COMPLETE

*Definition.* For a prime set `A` and a large prime `q`, say **`q` is an essential connector for `A`**
iff `A` is non-covering and every `A`-avoiding term is divisible by `q` (a term `B` is *`A`-avoiding*
iff `primes(B) ∩ A = ∅`). Equivalently — see the proof — `A` is non-covering but `A ∪ {q}` is covering.

*Statement.* CSP fails ⟺ some large prime `q` is an essential connector for some non-covering set `A`.

*Proof.*

**(⟹) CSP fails ⟹ an essential connector exists.** If CSP fails then by Lemma 10 there is a minimal
covering set `C' ∈ ℰ` with a large prime `q ∈ C'`. Put `A := C' \ {q}`. By edge-minimality of `C'`,
`A = C' \ {q}` is non-covering. Now let `B` be any `A`-avoiding term: `primes(B) ∩ A = ∅`. Since `B`
is a term, `primes(B)` is covering (REAL, `𝒯 ⊆ 𝒞`), so `primes(B)` meets the covering set `C'`:
`primes(B) ∩ C' ≠ ∅`. But `primes(B) ∩ C' = primes(B) ∩ (A ∪ {q}) = (primes(B) ∩ A) ∪ (primes(B) ∩
{q}) = ∅ ∪ (primes(B) ∩ {q})`, so `q ∈ primes(B)`, i.e. `q ∣ B`. Thus every `A`-avoiding term is
divisible by `q`, and `A` is non-covering: `q` is an essential connector for `A`.

**(⟸) an essential connector exists ⟹ CSP fails.** Let `q` (large) be an essential connector for a
non-covering `A`. First, `A ∪ {q}` is covering: let `t` be any term; if `primes(t) ∩ A ≠ ∅` then `t`
is met by `A ⊆ A ∪ {q}`; otherwise `t` is `A`-avoiding, hence `q ∣ t` (essential-connector property),
so `t` is met by `{q} ⊆ A ∪ {q}`. So `A ∪ {q}` meets every term, i.e. is covering. By (CLUT) it
contains a minimal covering set `C'' ∈ ℰ` with `C'' ⊆ A ∪ {q}`. We cannot have `C'' ⊆ A`: that would
make its superset `A` covering, contradicting `A` non-covering. Hence `C''` contains an element of
`(A ∪ {q}) \ A = {q}`, i.e. `q ∈ C''`. So `C'' ∈ ℰ` is a minimal covering set containing the large
prime `q`; by Lemma 10, CSP fails. ∎ (Lemma 13)

*Consequence.* (6b)/CSP is equivalent to the crisp arithmetic statement

> **(EC)** for every non-covering prime set `A` and every large prime `q`, some `A`-avoiding term is
> **not** divisible by `q`,

a pure term-divisibility assertion — the value form of the crux this lane targets. It is equivalent to
ℰ-small-only (both `⟺ CSP`) but phrased entirely in terms of *which terms `q` divides*, not in terms of
the abstract clutter; it is the tightest handle for the value/essential-witness mechanism.

*Two standing facts about an essential-connector config `(A,q)`, used below.*
- **(W-inf)** the set `W_A := { A`-avoiding terms `}` is **infinite**. Indeed `A` is non-covering, so
  some term `B_0 ∈ W_A`. Pick any prime `r ∉ A` (primes are infinite, `A` finite). For each `k ≥ 1`,
  `primes(B_0 · r^{k}) = primes(B_0) ∪ {r} ⊇ primes(B_0)`, which is covering, and `B_0 · r^{k} ≥ a_1`,
  so `B_0 · r^{k}` is a term (REAL c); and `primes(B_0 · r^{k}) ∩ A = (primes(B_0) ∩ A) ∪ ({r} ∩ A) =
  ∅`, so `B_0 · r^{k} ∈ W_A`. These are distinct for distinct `k`, so `W_A` is infinite.
- **(q-mult)** every `B ∈ W_A` is `≥ a_1` (it is a term) and divisible by `q`; consecutive members of
  `W_A` therefore differ by a multiple of `q` — the essential witnesses `B_q` each `≥ a_1` all lie in
  the single residue class `0 (mod q)`.

---

### Lemma 14 (Essentiality propagates; the honest non-descent) — COMPLETE

*Statement.* Let `(A, q)` be an essential-connector config (Lemma 13). Then **every** `A`-avoiding term
`B` has `q` essential inside it: `primes(B) \ {q}` is non-covering. Consequently `(primes(B) \ {q}, q)`
is again an essential-connector config with the **same** large prime `q`.

*Proof.* Let `B ∈ W_A`. By (q-mult), `q ∣ B`, so `q ∈ primes(B)` and `T := primes(B) \ {q}` is
well-defined; also `T ≠ ∅`, for otherwise `B` would be a power of `q`, but `gcd(q^j, a_1) = 1`
(`q` large, `q ∤ a_1`) contradicts `B` being a term.

Suppose, for contradiction, that `T` is covering. `T` is a finite covering prime set, so by (REAL c) any
integer `≥ a_1` whose prime set is exactly `T` is a term: e.g. with `p ∈ T` and `k ≥ 0` least such that
`N := rad(T) · p^{k} ≥ a_1`, we have `primes(N) = T` and `N` a term. Now `T = primes(B) \ {q} ⊆
primes(B)` and `primes(B) ∩ A = ∅`, so `primes(N) = T` is disjoint from `A`: `N` is `A`-avoiding. But
`q ∉ T = primes(N)`, so `q ∤ N`. Thus `N` is an `A`-avoiding term not divisible by `q`, contradicting
that `q` is an essential connector for `A`. Hence `T = primes(B) \ {q}` is non-covering.

Finally, `T ∪ {q} = primes(B)` is covering (`B` is a term, REAL `𝒯 ⊆ 𝒞`), and `T` is non-covering, so by
the equivalence in Lemma 13's proof (`A` non-covering, `A ∪ {q}` covering ⟺ `q` essential connector for
`A`) `q` is an essential connector for `T`. ∎ (Lemma 14)

*Remark (why this does not descend — the honest wall).* Lemma 14 is the furthest reach of the
essential-witness value pressure. It shows the failing configuration is **self-reproducing**: from
`(A, q)` and any `A`-avoiding term `B` we obtain `(primes(B) \ {q}, q)`. But the large prime `q` is
**preserved**, not lowered; and `T = primes(B) \ {q}` bears no order relation to `A` (`B` need not be
comparable to a realization of `A`), so none of `q`, `rad`, or set-size is forced downward. There is no
well-founded quantity, hence no contradiction — exactly the stall recorded since round 5, now pinned in
its crispest value form. To close (EC) one still needs a genuinely new lever forcing *some* `A`-avoiding
term coprime to `q`; the propagation shows the naive lever (realize `primes(B) \ {q}`) is precisely what
the failing case blocks.

---

### Lemma 15 (Hub abundance under ¬(FIN-Q)) — COMPLETE (NEW, round 10)

*Context and notation (imported from the certified (FIN-Q) lemma `finite-connector-pool-periodicity.md`).*
`L_0 := ∏_{p ≤ P_max} p`; for `m > 1`, `S(m) = primes(m) ∩ [2,P_max]` depends only on `m mod L_0`
(residue-locality of `S`). For a term `a_i`, `Q_i := primes(a_i) ∩ (P_max,∞)`. For a residue
`r ∈ ℤ/L_0ℤ` the small part `S(r)` is well-defined; `R_bad := {r : S(r) non-covering}`,
`W(r) := {i : primes(a_i) ∩ S(r) = ∅}` (the witness colors of class `r`),
`Q(r) := ⋃_{i∈W(r)} Q_i` (the large connector pool), and `R'_bad := {r ∈ R_bad : E_∞ meets class r}`.
The certified **membership dichotomy** for `r ∈ R'_bad` and `m ≡ r (mod L_0)`, `m > 1`:

> **(★)**  `m ∈ E_∞ ⟺ for every i ∈ W(r), some q ∈ Q_i divides m`.

**Setting.** Assume ¬(FIN-Q): there is a class `r_0 ∈ R'_bad` with `Q(r_0)` **infinite**. Define the hub
set `H := { m ≥ a_1 : m ≡ r_0 (mod L_0),\ m ∈ E_∞ }` (so by (ENUM) every element of `H` is a term).

*Statement.*
- **(a)** A finite transversal exists: there is a finite set `D` of large primes with `D ∩ Q_i ≠ ∅` for
  every `i ∈ W(r_0)`.
- **(b)** `H` is **infinite**; in fact `H` contains all sufficiently large `m` in the arithmetic
  progression `m ≡ r_0 (mod L_0)`, `m ≡ 0 (mod ∏D)`.
- **(c)** Every `m ∈ H` is a **bad term** with `S(m) = S(r_0)` (non-covering) and with `Q(m) := primes(m)
  ∩ (P_max,∞)` a finite transversal of `{Q_i : i ∈ W(r_0)}`.

*Proof.*

**(a).** Since `r_0 ∈ R'_bad`, `E_∞` meets class `r_0`: fix any `m_1 ≡ r_0 (mod L_0)` with `m_1 > 1` and
`m_1 ∈ E_∞` (no size condition is needed). By the forward direction of (★) applied to `m = m_1`: for every
`i ∈ W(r_0)` some `q ∈ Q_i` divides `m_1`, i.e. `q ∈ primes(m_1) ∩ (P_max,∞) = Q(m_1)` (`q ∈ Q_i` is large,
so `q > P_max`). Hence `D := Q(m_1)` (a finite set — `m_1` has finitely many prime factors) meets every
`Q_i`, `i ∈ W(r_0)`. This proves (a).

**(b).** `D ⊆ (P_max,∞)` and `L_0 = ∏_{p ≤ P_max} p`, so `gcd(L_0, ∏D) = 1`. By the Chinese Remainder
Theorem the two congruences `m ≡ r_0 (mod L_0)` and `m ≡ 0 (mod ∏D)` have a common solution class modulo
`L_0 · ∏D`; this class contains infinitely many integers, all `> 1` (indeed `≥ a_1` for all but finitely
many). Fix any such `m ≥ a_1`. For each `i ∈ W(r_0)`, part (a) gives a prime `q ∈ D ∩ Q_i`; then
`q | ∏D | m`, so "`∃ q ∈ Q_i : q | m`" holds. As this holds for every `i ∈ W(r_0)`, (★) gives `m ∈ E_∞`.
Since `m ≥ a_1` and `m ∈ E_∞`, (ENUM) makes `m` a term; and `m ≡ r_0 (mod L_0)`, so `m ∈ H`. There are
infinitely many such `m`, so `H` is infinite. This proves (b).

**(c).** Let `m ∈ H`. Then `m ≥ a_1` and `m ∈ E_∞`, so by (ENUM) `m` is a term. Its small part
`S(m) = S(m mod L_0) = S(r_0)` by residue-locality of `S`, and
`S(r_0)` is non-covering (`r_0 ∈ R_bad`); hence `m` is **bad**. Finally, `m ∈ E_∞` in class `r_0` gives by
(★) that for every `i ∈ W(r_0)` some `q ∈ Q_i` divides `m`, i.e. `q ∈ Q(m)`; so `Q(m)` meets every `Q_i`,
a transversal. `Q(m)` is finite (`m` has finitely many prime factors). This proves (c). ∎ (Lemma 15)

*Consequences and the role in the intended descent.* Lemma 15 rigorously supplies the object the round-10
outline needed: an **infinite family `H` of bad terms** all sharing the same small part `S(r_0)` and the
same residue `r_0 (mod L_0)`, differing only in their large-prime content and value. This is the concrete
population on which the "class-graph walk / hub-value monovariant" was to run.

*Two facts that block the value-walk from descending (the honest content of GAP (i)).*

1. **A single finite transversal `D` handles hub existence, so `Q(r_0)`'s infinitude exerts no hub-existence
   pressure.** By (a)–(b), the *fixed* finite set `D` already forces infinitely many hubs; the infinitely
   many further primes of `Q(r_0) ∖ D` are never needed to *produce* a hub. (They are not inert for
   `E_∞`-*membership* — a large prime `q' ∈ Q_i ∖ D` dividing `m` gives an *alternative* way to satisfy the
   `i`-th clause of (★), which is exactly why ¬(FIN-Q) genuinely obstructs the period argument — but they
   create no lower bound, no overflow, and no forced growth of any candidate monovariant.) There is thus no
   value quantity that ¬(FIN-Q) forces to move.

2. **Value-descent and the class-graph are orthogonal.** The only descent tool available (Lemma 9) sheds a
   prime `p` from a bad term `m` to obtain `m/p`. In case (i) `p` is large (`p ∤ L_0`) and in case (ii) `p`
   is a small redundant prime (`p | L_0`); in *either* case `m/p ≢ m (mod L_0)`, so the shed **exits the
   class** `r_0` and leaves the finite node set `ℤ/L_0ℤ` on which the pigeonhole was to act. Hence the two
   ingredients of the plan — "descend the value by shedding" and "pigeonhole a repeat among ≤ L_0 residue
   nodes" — cannot be run simultaneously.

---

### Round-10 analysis: the iterated hub-value walk does not yield a monovariant — GAP (i) pinned

*Goal of the round-10 descent variable (as assigned).* Model ¬(FIN-Q) as a revisiting walk on the finite
`≤ L_0`-node class-graph; let `v_k` be the value of the `k`-th revisited hub; apply Lemma 9's shed step at
every node to force `v_k` strictly monotone; pigeonhole (`≤ L_0` residues) forces a repeated node, and a
repeated node with a strictly-decreasing value is a contradiction.

*Why per-node minimality (GAP (i)) cannot be established by this mechanism.* Two independent obstructions,
both proved above (Lemma 15, facts 1–2), defeat every way of instantiating `v_k`:

- **If `v_k` is defined by shedding** (apply Lemma 9 at the current hub to get a smaller bad term, take that
  as the next hub): by Obstruction 2 (of Lemma 15) each shed changes the residue mod `L_0`, so the sequence
  of shed results does not return to any node — it is a plain strictly-decreasing sequence of positive
  integers, which already contradicts well-ordering **iff** every shed stays `≥ a_1`. But Lemma 9 certifies
  the shed result is a *term* only when it is `≥ a_1`; off the global minimum this is exactly the unproven
  a_1-threshold, and Lemma 9's dichotomy Case (A) (a squarefree minimal cover with a large prime: **no**
  sheddable prime) halts the shed with no successor at all. So "shed at every node" is not a total operation
  and produces no walk — it is the certified stall, relocated.

- **If `v_k := min H_{r_k}` is the smallest hub of the visited class** (the value is read off the node, not
  produced by shedding): by fact 2 (Obstruction 2) `v(r)` is a *function of the residue* `r`, so a repeated
  node `r_k = r_j` gives `v_k = v_j` — the pigeonhole delivers an equality, never a strict decrease. There
  is no monovariant, hence no contradiction.

- **If `v_k` carries a "running bound" `v_k ≤ a_1 · ∏(\text{primes shed so far})`** (the outline's suggested
  hybrid): the product on the right *grows* with each shed, so the bound is an increasing upper bound, not a
  decreasing quantity; and by the first bullet the shed steps leave the node set, so the bound is not tied to
  any repeated node. No well-founded order emerges.

*Conclusion of the analysis.* The iterated-floor-tightness value-walk **stalls at the same a_1 threshold**
as the single-application of Lemma 9. The obstruction is now pinned to a structural incompatibility, not a
missing computation: **the value-descent (shed) is orthogonal to the residue-class pigeonhole (mod `L_0`),
because every shed changes the residue**, and the only class-intrinsic value (`min H_r`) is a function of
the node and so is constant on revisits. To close (6b)/CSP/(EC) one still needs the wall statement — *no
minimal covering set with a large prime has minimal realization `≥ a_1`* — which no shed/pigeonhole
combination reaches. This is reported honestly as the residual GAP (i); the round's positive deliverable is
Lemma 15 (gap-free) together with this precise diagnosis, which retires the value-walk as a closing route.

---

### Step 7 — GAP (the sole remaining crux): (EC) = ℰ-small-only = (6b) = CSP

**What is now proved.** (i) CSP ⟺ ℰ-small-only (Lemma 10). (ii) VI′ handles only Case I of the skeleton
split (Lemma 11); Case II is genuine (Lemma 11). (iii) Any minimal cover with a large prime spawns a
distinct one sharing exactly its large prime (Lemma 12). (iv) **NEW round 9:** CSP ⟺ **(EC)** — no large
prime is an essential connector for any non-covering set, a crisp term-*divisibility* statement
(Lemma 13); and in any failing config `(A,q)` essentiality **propagates** to every `A`-avoiding term,
preserving `q` (Lemma 14). So the crux now has a fully value/arithmetic face: *for every non-covering `A`
and large `q`, some `A`-avoiding term is not divisible by `q`.*

**Where it stalls (honest GAP).** To close (EC) one must force, for a fixed non-covering `A` and large
`q` with `A ∪ {q}` covering, *some* `A`-avoiding term coprime to `q`. The natural lever — realize the
covering set `primes(B) \ {q}` for an `A`-avoiding term `B` — is **exactly** what the failing case
blocks: Lemma 14 shows `primes(B) \ {q}` is non-covering for *every* `A`-avoiding `B`. The value pressure
(each essential witness a term `≥ a_1`; all of `W_A` in the class `0 mod q`, `W_A` infinite by (W-inf))
constrains the configuration but does not force a contradiction:
- *No local overflow.* A minimal cover may carry a single large prime `q` and small primes covering
  the rest (Lemma 8 gives `|Q|`-capacity, no numeric overflow) — consistent with Lemma 12.
- *Window Purity gives nothing new here.* As flagged by the reviewer, Window Purity (gap interiors are
  `E_∞`-free) is strictly weaker than the `E_∞`-membership facts the descent already uses; the term `N`
  and witness `B_q` are valid terms, so no interior-sweeping contradiction touches them.

**Proven-dead closures stay barred:** global `Σ1/p²` capacity; pure covering/Helly (Prop D barrier);
symmetric bad-partner ascent; the direct `(q*,k)` active rewrite (`lex-rewrite-descent`, pruned round 7).

**Sharpest form of the residual crux (round-9 update).** The crux has three certified-equivalent faces —
ℰ-small-only (set-theoretic, Lemma 10), spawning-into-families (structural, Lemma 12), and now **(EC)**
(arithmetic/value, Lemma 13): *for every non-covering prime set `A` and large prime `q`, some
`A`-avoiding term is not divisible by `q`.* The value mechanism's furthest reach is Lemma 14
(essentiality propagation), which is self-reproducing with `q` fixed; closing it requires either a
well-founded monovariant on essential-connector configs `(A,q)` (none found — `q`, `rad`, size all
recur) or an entirely different lever forcing a `q`-coprime `A`-avoiding term.

## Full proof
(Not present: Status is `partial`. Lemmas 10–14 are complete and gap-free and pin the crux to the
crisp value statement (EC) = ℰ-small-only = (6b) = CSP, but (EC) itself is not proved: Lemma 14 yields no
downward monovariant — the large prime `q` is preserved under propagation — so the value/essential-witness
mechanism stalls at the same wall.)

## Promotable lemmas

0. **Hub abundance under ¬(FIN-Q) (Lemma 15) — NEW round 10.** *Statement:* if `r_0 ∈ R'_bad` has `Q(r_0)`
   infinite, then (a) a finite transversal `D` of `{Q_i : i∈W(r_0)}` exists, (b) the hub set
   `H = {m ≥ a_1, m ≡ r_0 (mod L_0) : m∈E_∞}` is infinite, and (c) every hub is a bad term with `S(m)=S(r_0)` and
   `Q(m)` a transversal of `{Q_i}`. *Proof:* Lemma 15 above — (a) from (★) at one hub `m_1` (`D=Q(m_1)`),
   (b) by CRT (`gcd(L_0,∏D)=1`) + (★), (c) by residue-locality of `S` + (★). Imports only the certified
   (FIN-Q) scaffold (`finite-connector-pool-periodicity.md`: (★), `R'_bad`, `W(r)`, `Q(r)`), ENUM, CRT.
   Gap-free. **Recommend certifying** — it is the rigorous "infinite bad-hub family" structure of a
   ¬(FIN-Q) configuration, reusable by any lane that reasons about the ¬(FIN-Q) obstruction (the class-graph
   walk, bad-residue-witness-index, window-purity-class-cycle); and it records the sharp diagnosis that a
   single finite transversal suffices for hub existence (so value/overflow pressure is absent) and that
   value-shed descent is orthogonal to the residue-class pigeonhole (every shed changes `m mod L_0`) — a
   pruning fact barring the iterated-hub-value-walk closer.

1. **Equivalence CSP ⟺ ℰ-small-only (Lemma 10).** *Statement:* no term is bad ⟺ every minimal
   covering set is `⊆ [2,P_max]`. *Proof:* Lemma 10 above; (⇐) via (CLUT) + superset-closure, (⇒) via
   power-inflating a large-prime minimal cover to a bad term `N ≥ a_1` (REAL c). Both directions
   gap-free. **Recommend certifying** — it certifies that the value-descent target (6b) and
   `minimal-cover-small-only`'s ℰ-small-only are the *same* statement (resolving the single-gap-trap
   question with a theorem), and corrects the round-7 claim that VI′ closes (6b).

2. **Essential-witness spawning (Lemma 12).** *Statement:* every minimal covering set `C'` containing
   a large prime `q` yields a distinct minimal covering set `C''` with `q ∈ C''` and `C'' ∩ C' = {q}`.
   *Proof:* Lemma 12 above, from edge-minimality + (CLUT) + Realizability of `C'` as a term `N`.
   Gap-free. **Recommend certifying** — a reusable structural constraint on the clutter obtained by the
   value mechanism (Prop-D-compliant), usable by both `minimal-cover-small-only` (as a transversal
   fact) and any future monovariant attempt on `ℰ`.

3. **Essential-connector equivalence, the value form of the crux (Lemma 13, + (W-inf)).** *Statement:*
   CSP fails ⟺ some large prime `q` is an *essential connector* for some non-covering set `A` (every
   `A`-avoiding term divisible by `q`; equivalently `A` non-covering, `A ∪ {q}` covering). Equivalently
   CSP ⟺ **(EC):** for every non-covering `A` and large `q`, some `A`-avoiding term is not divisible by
   `q`. Companion: the set `W_A` of `A`-avoiding terms is infinite and lies in the class `0 (mod q)`.
   *Proof:* Lemma 13 above; (⟹) via Lemma 10 + REAL `𝒯⊆𝒞`, (⟸) via (CLUT) + `A` non-covering (`C''⊄A`,
   so `q∈C''`), (W-inf) via REAL c. Gap-free. **Recommend certifying** — recasts the crux as a pure term-divisibility statement,
   the sharpest value form; distinct from ℰ-small-only in phrasing though certified-equivalent.

4. **Essentiality propagation (Lemma 14).** *Statement:* in any essential-connector config `(A,q)`,
   every `A`-avoiding term `B` has `primes(B)\{q}` non-covering, and `(primes(B)\{q}, q)` is again an
   essential-connector config with the same `q`. *Proof:* Lemma 14 above, from REAL c (realize
   `primes(B)\{q}` if it were covering, obtaining a `q`-coprime `A`-avoiding term — contradiction).
   Gap-free. **Recommend certifying** — pins why the naive value lever fails and records the honest
   non-descent (`q` preserved); a pruning fact for future monovariant attempts.

3. **Skeleton case-split (Lemma 11).** *Statement:* the minimal covering skeleton `C'` of a smallest
   bad term satisfies either Case I (`rad(C') ≥ a_1`, forcing `C = C'` minimal and `m_0 = rad(C)`
   squarefree) or Case II (`rad(C') < a_1`); VI′ (radical `≥ a_1` forbidden) closes only Case I. *Proof:*
   Lemma 11 above. Records the precise reason the value-inequality framing does not suffice; useful as a
   pruning note (do not re-field VI′ as a sufficient closer).
