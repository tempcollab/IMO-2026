# Lemma: cross-intersecting closure of the minimal-hitting-set family

## Status
CERTIFIED (round 2, proof-reviewer). Proved in `approaches/hitting-set-monovariant.md` §5/Lemma 6. Stress-tested: 0 violations in 1581 random cross-intersecting families with an added hitting-set row. Unconditional (no B1' needed).

## Statement
Let `F_n = {S_1, ..., S_n}` be a family of finite sets, `M_n` its family of inclusion-minimal hitting sets. Suppose `M_n` is **pairwise cross-intersecting** (`h ∩ h' ≠ ∅` for all `h, h' ∈ M_n`) and `S_{n+1}` is a hitting set of `F_n`. Then `M_{n+1} = M_n` (and inductively `M` is fixed forever for any subsequent row whose support is a hitting set of `F_n`).

## Proof
Since `S_{n+1}` is a hitting set of `F_n`, by well-foundedness `S_{n+1} ⊇ h_0` for some `h_0 ∈ M_n`.

**Old sets persist.** Let `h' ∈ M_n`. `h'` is a hitting set of `F_n`; it hits the new row because `h' ∩ S_{n+1} ⊇ h' ∩ h_0 ≠ ∅` (cross-intersecting, `h_0 ⊆ S_{n+1}`). Minimality is preserved: any `h'' ⊂ h'` fails some row of `F_n`, hence fails it in `F_{n+1}`. So `h' ∈ M_{n+1}`; thus `M_n ⊆ M_{n+1}`.

**No new minimal hitting set.** Let `g ∈ M_{n+1}`. Then `g` is a hitting set of `F_{n+1} ⊇ F_n`, hence of `F_n`; by well-foundedness `g ⊇ h_g` for some `h_g ∈ M_n`. Cross-intersecting gives `h_g ∩ h_0 ≠ ∅`, and `h_0 ⊆ S_{n+1}`, so `h_g ∩ S_{n+1} ≠ ∅`: `h_g` hits the new row. Since `h_g` hits all of `F_n`, it hits all of `F_{n+1}`; so `h_g` is a hitting set of `F_{n+1}` with `h_g ⊆ g`. Minimality of `g` for `F_{n+1}` forces `h_g = g`, i.e. `g = h_g ∈ M_n`. So `M_{n+1} ⊆ M_n`.

Hence `M_{n+1} = M_n`. ∎

## Scope / reusability
Reusable by any hitting-set-based approach to `imo-2026-06`. Under B1' (`M_n = M'_n`), the same closure applies to `M'_n` verbatim (the new row's small support `σ(a_{n+1}) ⊇ h_0 ∈ M'_n` because `a_{n+1} ∈ B_n` by the greedy). Gives a sharper EARLY freeze (`M` stabilizes as soon as it is cross-intersecting, often far before `F'` stabilizes as a set) — a shortcut, not load-bearing (the finite-universe pigeonhole backstop closes the theorem regardless).
