# Lemma CROSS-TIE-AFFINE and the self-meeting-point-is-an-anchor fact

Proved by `geometric-dominance-construction`, round 8, as an independent
route to `recursive-embedding-induction`'s Lemma V'-GEN gap (b)
(cross-piece tied free coordinates). Builds only on already-certified
`lemmas/alternating-sum-toolkit.md` (Lemma D-INSERT) and the geometric
configuration's Lemma S (`t_i = 2t_{i+1}`, certified in
`geometric-configuration-facts.md` / `geometric-dominance-construction.md`).

## Setting

Fix `n≥1`, `t_i:=2^{n-i}` for `i=1,\dots,n`. Xiang Yu splits some subset of
`A_n`'s `n+1` original pieces (the top piece, total `2t_1`, and the `n`
tail pieces, totals `t_1,\dots,t_n`) using his ≤`n` marks. At a vertex-type
configuration where a piece `π` has all but (at most) one of its parts
pinned to fixed anchor values, write `y` for the remaining free part.

## Lemma CROSS-TIE-AFFINE

*Statement.* Let `π_1,\dots,π_k` (`k≥2`) be distinct split pieces, each
contributing exactly one coordinate `y_1,\dots,y_k` currently tied at a
common value `v`, `t_{j+1}<v<t_j` (some `j`, with `t_0:=+\infty`,
`t_{n+1}:=0`), no anchor strictly between the endpoints of the interval
over which `v` can move while every `y_l`'s rank relationship to
everything except the other tied `y_m`'s stays fixed. Then `D`, restricted
to this interval, is **affine** in `v`:
```
D(v) = const + M·v,   M := Σ_{l=1}^k m_l,
m_l = σ_l                     (π_l has ≥3 parts, others pinned),
m_l = σ_l − σ_l'               (π_l has exactly 2 parts, companion
                                 c_l = top_{π_l} − v co-varies),
```
where `σ_l = (-1)^{r_l+1}` (`r_l` = `y_l`'s current global sorted rank) and
`σ_l'` is the analogous sign for the companion `c_l`. Consequently `D(v)`
is minimized, over the whole interval, at one of the two endpoints — the
tie is never a *strict* local minimizer.

*Proof.* Insert each of `y_1,\dots,y_k` and (for 2-part pieces) each
companion `c_1,\dots,c_{k'}` one at a time, in sorted order, into the fixed
background list (everything else), via repeated application of Lemma
D-INSERT (`alternating-sum-toolkit.md`). Each insertion contributes
`(\pm1)\times(\text{its value})` to `D`, with the sign fixed by its rank
within this block (constant on the interval, since crossing a rank
boundary is exactly what defines the interval's edge). Each `y_l=v`
contributes `σ_l v`; each companion `c_l = \mathrm{top}_{π_l}-v`
contributes `σ_l'\mathrm{top}_{π_l} - σ_l' v` (constant plus `-σ_l' v`).
Summing: `D(v) = \text{const} + Mv`. An affine function on a bounded
interval attains its minimum at an endpoint (elementary). ∎

*Independent verification.* The pairwise (`k=2`, no companions) special
case `D(y,y') = D(C_{\rm bg}) + σ|y-y'|` was checked against 5000 random
exact-`Fraction` background-list trials (`/tmp/verify_formula.py`), zero
mismatches. The full formula (with companions) was reproduced exactly on
the round-8 explorer's `n=2` and `n=3` genuine cross-tie examples
(`/tmp/verify_n2.py`, `/tmp/verify_n3.py`): both give `D(v) = -2v + C`,
exactly affine, matching the explorer's reported non-minimizing endpoint
value (`D=3`) and confirming the true minimum (`D=t_n`) sits at the
anchor-snapped endpoint of the interval, not the interior tie.

## Self-meeting-point-is-an-anchor fact

*Statement.* For any piece `π` of `A_n` split by Xiang Yu into exactly 2
parts (`y+c=\mathrm{top}_π`), the point `v=\mathrm{top}_π/2` (where `y=c`)
is itself always an anchor: `\mathrm{top}_π/2 = t_{i+1}` if
`\mathrm{top}_π=t_i`, or `=t_1` if `\mathrm{top}_π=2t_1` (`π=P_1`).

*Proof.* Immediate from Lemma S (`t_i=2t_{i+1}` for `i<n`) and the
definition `\mathrm{top}(P_1)=2t_1`. ∎

*Consequence.* Whenever Lemma CROSS-TIE-AFFINE's D-minimizing endpoint
coincides with a 2-part piece's own self-meeting point (i.e. the tied
coordinate is the *majority*/larger part of that piece, so `v` reaches
`\mathrm{top}_π/2` before any deeper external anchor), the resulting
endpoint configuration has the piece's two parts simultaneously equal to
the *same* anchor — a zero-residue, fully anchor-resolved even-
multiplicity block. Combined with the ≥3-part case (companion already
pinned, no residue at all — this is exactly `recursive-embedding-
induction`'s already-certified well-separated single-free-coordinate case),
this fully closes gap (b) in these two sub-cases.

## Honest remaining gap (NOT closed by this lemma)

When the tied coordinate is the **minority** (strictly smaller) part of a
2-part piece, in a bracket strictly below that piece's own natural halving
level, the D-minimizing endpoint (an *external* anchor) leaves the
companion at a fixed value `\mathrm{top}_π - (\text{anchor})`, which is
generically **not** itself an anchor (e.g. `t_i - t_j` for `j>i+1` is not a
power of 2). This residue sub-case is not resolved here. One numeric probe
at `n=5` found the affine slope `M=0` (non-competitive, `D=21≫t_5=1`) in a
representative instance of this sub-case, but this is not a general proof.

## Status

**Certified** as stated (the affine formula and the self-meeting-point
fact, both fully proved and independently verified). Does **not** close
Lemma V'-GEN or gap (b) in full generality — the minority-part/deep-bracket
residue sub-case remains open, narrower than before this round's work.
