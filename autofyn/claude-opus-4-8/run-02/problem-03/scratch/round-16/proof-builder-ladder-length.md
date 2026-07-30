# Build report — round 16 — ladder-length-deficient-induction (b-lift, cut-top-rung leaf)

Status: **partial** (advanced). File: `results/imo-2026-03/approaches/ladder-length-deficient-induction.md`.

## What I proved (banked this round)

**(1) (L̂B-inherit) — the correct inheritance on the leaf.** On Case II of `(P̂_m)` (top rung cut,
`a₁≥1`), with all reds `≤θ` and `ΣR≤2^m`, the pair `(R,F'')` satisfies `Δ(R,F'') ≥ min(0, θ−ΣR)`.
Proof: `a₁≥1` spends a budget unit ⇒ `a₀+b'' ≤ m−a₁ ≤ m−1`, which with reds `≤θ=2^{m−1}` and
`ΣR≤2^m` is exactly the hypothesis set of `(L̂B_{m−1})` (derived from `(P̂_{m−1})` via the certified
Lipschitz collapse, available in the outer IH). This CORRECTS the round-15 file, which only inherited
`(Q̂_{m−1})`. Verified `0` fails / `~70k` (probe4) and again `fLB=0` (tprobe).

**(2) (ΣR≤θ closure) — Case IIb-1 CLOSED completely.** For the cut-top-rung leaf with all reds `≤θ`
and `ΣR≤θ`: `Δ(R,F') ≥ ½(θ−D̃(ρ₁)) > 0`. Two-line proof: `(L̂B-inherit)` gives `Δ(R,F'')≥0`; `(C)`
gives `Δ(R,F') ≥ ½θ+½D̃(ρ₁)−I_S ≥ ½θ−½D̃(ρ₁)` via `I_S≤λ(O_{ρ₁})=D̃(ρ₁)`; and `D̃(ρ₁)≤p₁<θ`
(alternating sum ≤ largest part; largest part `<θ` because the rung is cut). Boundary `ΣR=θ` safe
(`min(0,0)=0`). Verified `0` fails: `fail_final=0` over the whole `ΣR≤θ` slice, and the explicit
bound chain `bad_b=0` over `119,119` configs, `bad_Dmax=0` (D̃≤max never violated).

Both are stand-alone, certifiable sub-lemmas (see Promotable, below). Together with the certified
engine they leave **exactly one wall**.

## What remains open (the sole gap)

The **cut-top-rung, oversized-red leaf `ΣR>θ`** (Case IIb-2) and its mirror (Case IIa / the `(Q̂)`
cut-top-rung `ΣR>2^m` branch). Sharpened precisely:

- By `(C)`, the target `Δ(R,F')≥0` is `(†) I_S ≤ Δ(R,F'')+½θ+½D̃(ρ₁)`.
- I verified rigorously (algebra + numerics) that `(†)` is **literally equivalent to the target**:
  using `D̃(W)=2Δ(R,F'')+ΣR−(θ−1)` and `λ(E∩O_W)=D̃(W)−I_S`, it rearranges to
  `(‡) λ(O_W∩O_{ρ₁})−λ(O_W∩E) ≤ D̃(ρ₁)+2θ−1−ΣR`, and at `ΣR=2θ` this is exactly
  `λ{parity mismatch of N_{ρ₁},N_W on (0,θ)} ≥ 1`, i.e. `D̃(R⊎F')≥1`. So `(†)` may NOT be assumed —
  it IS the thing to prove (matches the reviewer's caveat exactly).
- The residual is **razor-tight**: true `min Δ(R,F')` over oversized configs `= 0.062 → 0`
  (`/tmp/tprobe3.py`). Any scalar `I_S`-ceiling fails ~34% of oversized configs (`/tmp/tprobe.py`) —
  provably vacuous (the banned R14 estimate). Closure REQUIRES the per-tooth comb geometry.
- I set up the comb: `O_{ρ₁}` = `⌈r/2⌉` disjoint teeth `(p₂,p₁),(p₄,p₃),…(+(0,p_r) if r odd)`,
  `a₁=r−1` controls tooth COUNT not measure (`D̃(ρ₁)→θ⁻` possible for every `r`), `I_S=Σ_teeth
  λ(tooth∩O_W)`, `O_W` has `≤ 2m−a₁` budget-limited breakpoints. The needed closer is a per-tooth
  charge giving `(‡)`. **I did NOT close it** — I do not have the per-tooth lower bound on the
  "saved" measure. Honestly marked open. The mirror (IIa) needs the dual (teeth MEET `O_W`, a LOWER
  bound on `I_S`) and does not follow from the upper-bound side for free.

## Spec concerns

- The b-lift target REQUIRES the budget `Σa_i≤n` (retained from R15; FALSE without it —
  `π₀={2,2},F'={3/2,3/2}` gives `D̃=0`). Unchanged.
- Corrected the file's §4/§6 wording: `(L̂B_{m−1})` (not just `(Q̂_{m−1})`) is inheritable on the
  leaf. This is what makes IIb-1 close.
- Confirmed the `(Q̂_m)` cut-top-rung branch closes for `ΣR≤2^m` via `I_S≥0` (so `(P̂_m)`'s use of
  `(Q̂_m)` in Case IIa, at `ΣR₀<θ`, is fine for the UPPER direction of `(Q̂)`); the missing piece in
  IIa is the STRONGER `(P̂)`-strength upper bound `Δ(R₀,F')≤2^m−1−ΣR₀`, which needs the LOWER bound
  on `I_S₀` = the mirror wall.

## Lemmas I propose to certify

1. **(L̂B-inherit)** — statement + proof above; verified `0`/`~70k`. Clean, reusable.
2. **(ΣR≤θ cut-top-rung closure, IIb-1)** `Δ(R,F') ≥ ½(θ−D̃(ρ₁)) > 0` — statement + 2-line proof
   above; verified `0`/`119,119`. Stand-alone regardless of the residual.

Both depend only on already-certified machinery ((C), (L̂B_m) Lipschitz collapse, Lemma G).

## Assessment / plateau note

Real forward motion (the `ΣR≤θ` half is newly and fully closed, and the wall is now pinned to the
oversized regime with an exact parity-mismatch reformulation), but the core TEETH parity bound
remains open — this is the razor-tight heart of the b-lift, open since R11. Per the outline
reviewer's plateau flag: if TEETH stalls again, next round's explorer should cheap-kill the two
logged speculative directions (discrete run-length/±1-jump recast of `M`; red-side MAXPEEL of the
largest red `≤θ`) on the extremal ladder family before any new slug is seeded.
