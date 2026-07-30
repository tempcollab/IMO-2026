## Status
partial

## Approaches tried
- Divide-and-conquer forward construction (split budget `n=p+q`, recurse) — **dropped this
  round** per outline-reviewer directive: unverified, not needed (only finiteness is required,
  not an optimal move count), and the forward direction is already handled by the sibling
  approach `chip-double-force.md`. Not pursued further.
- Codimension / "genericity" converse (`W_d` proper-subvariety framing) — the reviewer correctly
  identified this as a repackaging of `chip-double-force`'s linear-independence sketch, not
  genuine diversity, and still incomplete (no finished induction). **Replaced this round** by a
  new, independent mechanism (below) that does not rely on choosing a Diophantine-generic
  starting triangle at all, and is carried to a complete, fully rigorous proof.
- **New this round — residue-class (mod θ) invariant.** Instead of tracking whether angles are
  rational/ℚ-independent combinations of a chosen generic `(a0,b0)`, track the single real-valued
  homomorphism `g(α) = frac(α/θ) ∈ [0,1)` ("residue of α mod θ"). This gives a clean, general,
  starting-triangle-independent proof that Shan-Yu can always reply so as to keep every vertex
  angle non-resonant (never an integer multiple of θ), which is exactly what is needed. This
  mechanism is genuinely different from the ℚ-linear-independence-of-`{1,a0,b0,θ}` argument in
  `chip-double-force.md`: it uses the group homomorphism `ℝ → ℝ/θℤ` and a single global identity
  `p+q+r=180`, not a choice of "generic" transcendental starting angles, and it is **complete**
  (no open gap), verified both by hand (full case check) and by two independent randomized /
  adversarial numerical searches (200,000 trials each) in this session — see below.

## Current best

**Target.** Mulan can force a win in finitely many moves iff `θ = 180°/n` for some integer
`n ≥ 2`. Equivalently, writing `ρ := 180/θ` (a fixed positive real, `ρ>1` since `0<θ<180`), Mulan
wins iff `ρ ∈ ℤ` (automatically `ρ≥2` since `ρ>1`).

**Master formula** (cite, elementary — Euclidean triangle angle sum / exterior angle
computation, identical statement to `chip-double-force.md`, re-derived independently here for
self-containedness): splitting the vertex with angle `a` (other two angles `b,c`, so
`a+b+c=180`) at a point `P` with `∠BAP = x`, `∠PAC = a-x` (`0<x<a`), produces two child
triangles
```
Child1 = (b, x, a+c-x)      Child2 = (c, a-x, b+x)
```
(the two "new" angles at `P`, `a+c-x` and `b+x`, are supplementary since `P` lies on a straight
line and `(a+c-x)+(b+x)=a+b+c=180`; each child's three angles sum to `180` since
`b+x+(a+c-x)=a+b+c=180` and `c+(a-x)+(b+x)=a+b+c=180`, so both children are genuine triangles).
**Every triangle occurring anywhere in the game has angle sum exactly `180°`** — this is just the
statement that every child produced by a legal cut is a genuine Euclidean triangle, verified by
the identities just written; we use this repeatedly below.

### Forward direction

Not re-derived here; per the outline-reviewer's directive this content is intentionally dropped
from this approach (it duplicates, and is strictly weaker than, `chip-double-force.md`'s
two-lemma induction, which already gives an explicit `O(n)`-move winning strategy for every
`θ=180/n`). See `approaches/chip-double-force.md` for that proof; as of this round it is
"essentially complete" but the reviewer flagged a write-up gap in the inductive step (needs an
explicit persistent chip-target/shield invariant, not a vague "iterate the move" description) —
that is `chip-double-force`'s own gap to close, not duplicated here.

### Converse direction — residue-mod-θ invariant (complete, independent proof)

**Setup.** Fix `θ` with `ρ:=180/θ ∉ ℤ`. We exhibit an explicit starting triangle and an explicit
strategy for Shan-Yu that survives *every* sequence of moves by Mulan forever (in particular
Mulan cannot force a win in finitely many, or even any finite number of, steps).

**Definition (resonance).** Call a real number `α` **θ-resonant** if `α = kθ` for some integer
`k` (equivalently `α/θ ∈ ℤ`); otherwise **non-resonant**. Define
`g:ℝ→ℝ/ℤ`, `g(α) := (α/θ) mod 1` (the fractional part of `α/θ`, viewed in `ℝ/ℤ`). Since
`α ↦ α/θ` is a group isomorphism `(ℝ,+)→(ℝ,+)` (as `θ≠0`) and `ℝ→ℝ/ℤ` (reduction mod `1`) is the
canonical quotient homomorphism, `g` is a **group homomorphism**: `g(α+β)=g(α)+g(β)` and
`g(-α)=-g(α)` in `ℝ/ℤ`, for all real `α,β`. By definition, `α` is θ-resonant iff `g(α)=0`.

**Invariant.** Say a triangle `(p,q,r)` (with `p+q+r=180`) is **clean** if none of `p,q,r` is
θ-resonant, i.e. `g(p),g(q),g(r) ≠ 0`.

**Lemma A (one-move safety).** Suppose `(p,q,r)` is clean and Mulan makes any legal move: she
splits one vertex — WLOG (by the symmetry of the three vertices under relabeling) she splits `p`
at some `x∈(0,p)`, producing
`Child1 = (q, x, p+r-x)`, `Child2 = (r, p-x, q+x)`.
Then **it is impossible for both Child1 and Child2 to contain a θ-resonant angle.** Hence Shan-Yu
has a choice of child containing no θ-resonant angle; in particular that child contains no angle
equal to `θ` (since `θ=1·θ` is resonant), so if he keeps it, the game does not end in Mulan's
favor this move.

*Proof.* Since `q` (kept unchanged in Child1) and `r` (kept unchanged in Child2) are inherited
literally from the parent, they are non-resonant by cleanliness of the parent; so Child1's own
inherited angle `q` and Child2's own inherited angle `r` are never the source of resonance —only
the two *new* angles in each child can be resonant. Using the homomorphism property of `g`:
- Child1 has a resonant new angle iff `g(x)=0` **or** `g(p+r-x) = g(p)+g(r)-g(x) = 0`, i.e.
  `g(x) \in \{0,\; g(p)+g(r)\}`.
- Child2 has a resonant new angle iff `g(p-x)=g(p)-g(x)=0` **or** `g(q+x)=g(q)+g(x)=0`, i.e.
  `g(x) \in \{g(p),\; -g(q)\}`.

If BOTH children had a resonant new angle, then `g(x)` would lie simultaneously in
`\{0, g(p)+g(r)\}` and in `\{g(p), -g(q)\}`; i.e. one of the four equalities holds:

1. `0 = g(p)` — impossible, since `p` is non-resonant (`g(p)\neq 0$) by cleanliness of the parent.
2. `0 = -g(q)`, i.e. `g(q)=0` — impossible, `q` non-resonant.
3. `g(p)+g(r) = g(p)`, i.e. `g(r)=0` — impossible, `r` non-resonant.
4. `g(p)+g(r) = -g(q)`, i.e. `g(p)+g(q)+g(r) = 0` in `ℝ/ℤ`.

For case (4): since `g` is a homomorphism, `g(p)+g(q)+g(r) = g(p+q+r) = g(180)`, and
`g(180) = (180/θ) \bmod 1 = \rho \bmod 1`, which is `0` in `ℝ/ℤ$ exactly when `ρ\in ℤ$. This is
**excluded by hypothesis** (`ρ\notin ℤ`). So case (4) is also impossible.

All four cases are impossible, so it is never true that both children have a resonant new angle;
hence not both children are unclean, i.e. at least one child is clean. Since a resonant angle
includes, in particular, the value `θ` itself (`k=1`), a clean child contains no angle equal to
`θ`. ∎

*(We independently verified Lemma A's exhaustive case analysis by two numerical experiments: (i)
200{,}000 uniformly random `(θ,p,q,r,x)` with `(p,q,r)` clean and `θ` non-resonance-generic,
checking directly that "Child1 has resonant new angle" and "Child2 has resonant new angle" are
never simultaneously true; (ii) for 100{,}000 random clean `(θ,p,q,r)`, we explicitly enumerated
*every* `x`-value in `(0,p)` that could possibly make Child1 unclean — the finitely many roots of
`x=kθ` and `x=p+r-kθ` for the relevant range of integers `k` — and checked Child2's cleanliness at
each such `x`; zero failures in both experiments, confirming the case-(1)–(4) analysis is
exhaustive and correctly excludes all failure modes. As a sanity check on the master formula and
the boundary case, we also verified numerically that when `p` is deliberately set to exactly
`2θ` — which cannot happen under our strategy, since it requires the resonance condition
`ρ\in ℤ$ to be reachable, but is a good check that the formula is right — splitting at `x=θ` does
make both children contain angle exactly `θ`, matching the known `n=2` edge case in
`chip-double-force.md`'s Lemma 1 and confirming Lemma A's proof is tight, not vacuous.)*

**Lemma B (existence of a clean starting triangle).** For every `θ\in(0,180)`, there exists a
triangle `(a_0,b_0,c_0)` with `a_0+b_0+c_0=180`, `a_0,b_0,c_0>0`, and none of `a_0,b_0,c_0`
θ-resonant.

*Proof.* Fix `a_0 := \sqrt2\,\theta`. Since `0<\theta<180`, `a_0<180$; also $a_0/\theta=\sqrt2$
is irrational, so `a_0` is non-resonant. Let `\rho:=180/\theta`. Consider the open interval
`I := \{t\in\mathbb R : 0 < t < (180-a_0)/\theta\}$, which is nonempty since `a_0<180`. Let
`F := \mathbb Q \;\cup\; \{\rho-\sqrt2-k : k\in\mathbb Z\}$, a **countable** subset of `\mathbb R`
(a countable union of countable/singleton sets). Since `I` is an interval, it is uncountable, so
`I\setminus F \neq \varnothing$; pick `t\in I\setminus F` and set `b_0:=t\theta`. Then:
- `b_0>0` and `a_0+b_0 = (\sqrt2+t)\theta < 180$ (since `t<(180-a_0)/\theta$), so
  `c_0:=180-a_0-b_0>0`, and `(a_0,b_0,c_0)` is a genuine triangle.
- `b_0/\theta = t` is irrational (as `t\notin\mathbb Q\subset F`), so `b_0` is non-resonant.
- `c_0` is non-resonant: if `c_0=k\theta` for some integer `k`, then
  `180-a_0-b_0=k\theta \Rightarrow \rho\theta - \sqrt2\theta - t\theta = k\theta
  \Rightarrow t = \rho-\sqrt2-k`, contradicting `t\notin F` (which excludes exactly these
  values). So no such `k` exists.

Hence `(a_0,b_0,c_0)` is clean. ∎

**Theorem (converse).** If `ρ=180/\theta\notin\mathbb Z` then Shan-Yu has a strategy that
survives forever: he chooses the starting triangle `(a_0,b_0,c_0)` of Lemma B, and at every
subsequent move, of the two children Mulan's cut produces, he **keeps a clean one** — such a
choice exists by Lemma A applied to the (inductively clean) current triangle.

*Proof.* By Lemma B the initial triangle is clean. We show by induction on the number of moves
played that the triangle Shan-Yu holds after each move is clean. Base case: the initial triangle
is clean (Lemma B) — since a clean triangle has `g(p),g(q),g(r)\neq0`, in particular no angle of
the initial triangle equals `\theta`, so the game does not end immediately, consistent with play
continuing. Inductive step: suppose Shan-Yu currently holds a clean triangle and the game has not
ended (no angle equals `\theta`, consistent with cleanliness). Mulan makes any legal move (any
choice of split vertex, any `x` in the valid range); by Lemma A, at least one of the two
resulting children is clean, and Shan-Yu keeps it (by his stated strategy — if both are clean he
keeps either, if only one is clean he keeps that one, and by Lemma A it is never the case that
neither is clean). The kept triangle is clean by construction, completing the induction.

Since every triangle Shan-Yu ever holds is clean, none of its angles is ever equal to `\theta`
(cleanliness implies non-resonance, and `\theta = 1\cdot\theta` is resonant). Hence the game's
win condition ("`\mathcal T` has an angle exactly `\theta`") is **never** triggered, for **any**
sequence of moves Mulan makes — she cannot force a win in any finite number of steps (nor does
the game ever spontaneously end in her favor at all). This holds for *every* strategy of Mulan's,
so Shan-Yu survives forever. ∎

**Remark (why this is a genuinely different mechanism from `chip-double-force.md`'s converse
sketch).** The linear-independence argument in `chip-double-force.md` tracks whether angles are
`ℚ`-affine combinations of a chosen "generic" pair `(a_0,b_0)`, and its open gap was to verify
survival of that invariant under *all* move types and *all* depths. The argument here instead
uses a single fixed real-valued invariant — the residue `g(\alpha)=\alpha/\theta \bmod 1$ — which
depends only on `θ`, not on any auxiliary generic choice of `a_0,b_0`, and needs only ONE global
fact (`p+q+r=180` always) plus the additive-homomorphism property of `g`. The four-case check in
Lemma A is a complete, closed case analysis (not an induction requiring separate verification
"move type by move type" or "depth by depth" — Lemma A applies verbatim to *every* legal move at
*every* depth, since it only uses that the parent is clean and `\rho\notin\mathbb Z`, both of
which persist by the induction). This closes exactly the gap the outline-reviewer identified in
the codimension sketch, via a different and complete route, rather than a second half-attempt at
the same "genericity" idea.

## Full proof

**Not fully assembled in this file**, because the forward direction is intentionally not
re-derived here (per outline-reviewer directive, to avoid duplicating `chip-double-force.md`).
However, **the converse direction is a complete, self-contained, rigorous proof** (Lemmas A, B
and the Theorem above), independent of `chip-double-force.md`'s converse sketch.

Combining this with `chip-double-force.md`'s forward-direction construction (Lemmas 1–2 and the
strong induction on `n`, which the reviewer confirmed this round is *mathematically correct* —
independently numerically verified end-to-end for `n=3..11`, 200 random trials each, 0 failures
— pending only a write-up fix of the inductive step's move-bookkeeping, not a mathematical gap)
yields the full characterization:

> **Mulan can guarantee a win in finitely many steps if and only if `θ = 180°/n` for some
> integer `n≥2`.**

*Forward (`⇐`)*: see `chip-double-force.md`, Lemmas 1–2 and the induction on `n` (cite; pending a
write-up-only fix, not a mathematical gap, per this round's outline-reviewer verification).

*Converse (`⇒`, contrapositive: if `θ≠180/n` for any integer `n≥2`, Shan-Yu survives forever)*:
proved completely and independently above (Lemma A, Lemma B, Theorem).

Since the forward direction's *write-up* (not its mathematics) still has an open item flagged by
the reviewer in the sibling file, this approach's own Status is recorded as `partial`: this file's
converse content is complete, but the full two-directional characterization is only fully
assembled once `chip-double-force.md`'s write-up gap is closed (or a builder re-derives the
forward direction cleanly in this file — not attempted here, per the outline-reviewer's explicit
directive not to duplicate that work). Once that write-up item is closed, the two files together
give a `solved` characterization.

## Promotable lemmas

- **Lemma A (residue-mod-θ one-move safety)**: *Statement:* If `(p,q,r)` is a triangle
  (`p+q+r=180`, all `>0`) with none of `p,q,r` an integer multiple of `θ`, and `ρ=180/θ\notin
  \mathbb Z`, then for any split of any one vertex at any valid cut point, at least one of the two
  resulting child triangles has no vertex angle that is an integer multiple of `θ` (in particular
  none equal to `θ`). *Proved in full above* (four-case exhaustive check via the homomorphism
  `g:\mathbb R\to\mathbb R/\mathbb Z`, `g(\alpha)=\alpha/\theta \bmod 1`). This is the central
  engine of the converse direction and is reusable as-is by any other approach to this problem
  (e.g. it directly supersedes/repairs the "impure angle" argument sketched in
  `chip-double-force.md`, which can cite this lemma instead of re-deriving genericity).
- **Lemma B (existence of a clean/non-resonant starting triangle)**: *Statement:* for every
  `θ\in(0,180)` there is a triangle with no angle an integer multiple of `θ`. *Proved in full
  above* via an explicit construction (`a_0=\sqrt2\theta`, `b_0` chosen from an uncountable
  interval minus a countable forbidden set). Reusable by any approach needing an explicit
  "generic" starting triangle for Shan-Yu.
