import numpy as np
from fractions import Fraction

def D_alt(pieces):
    s = sorted(pieces, reverse=True)
    return sum((-1)**i * s[i] for i in range(len(s)))

def best_xiang_D(config, n_marks, grid=35, memo=None):
    config = tuple(sorted(config, reverse=True))
    if memo is None: memo = {}
    key = (config, n_marks)
    if key in memo: return memo[key]
    best = D_alt(list(config))
    if n_marks == 0:
        memo[key] = best; return best
    for i in range(len(config)):
        piece = config[i]
        if piece < 1e-12: continue
        others = list(config[:i]) + list(config[i+1:])
        for g in range(1, grid):
            p = piece * g / grid
            if p < 1e-12 or p > piece - 1e-12: continue
            new = others + [p, piece - p]
            d = best_xiang_D(new, n_marks - 1, grid, memo)
            if d < best: best = d
    memo[key] = best
    return best

# ---------------------------------------------------------------
# PART 4: Test the PAIRING strategy in the non-dominant case.
# Pairing: split L into (a_2, L - a_2).  Since L < 2*a_2 (non-dominant),
#   L - a_2 < a_2, so fragments are (a_2, L-a_2) with a_2 >= L-a_2.
#   New config: (a_2, a_2, max(L-a_2, a_3), ...) — two a_2's pair & cancel.
#   D(new) = D(rest) where rest = sort({L-a_2} ∪ {a_3,...,a_m}), IF L-a_2 >= a_3
#   (parity clean). rest total = 1 - 2*a_2.
# ---------------------------------------------------------------
def pairing_D(config):
    """One pairing mark: split L into (a_2, L-a_2). Returns D after, or None if parity not clean."""
    a = sorted(config, reverse=True)
    L, a2 = a[0], a[1]
    if L >= 2*a2:
        return None  # not applicable (dominant); use halving instead
    frag_small = L - a2  # = L - a_2, and since L < 2*a_2, frag_small < a_2
    rest = [a2, frag_small] + list(a[2:])  # two a_2's cancel; rest = {frag_small, a_3, ...}
    # Actually new config = {a_2 (orig), a_2 (from split), frag_small, a_3, ...}
    # sorted: a_2, a_2, max(frag_small, a_3), ...
    # D = (a_2 - a_2) + D(rest) where rest = sort({frag_small, a_3, ..., a_m})
    rest_pieces = [frag_small] + list(a[2:])
    # Parity clean iff the two a_2's occupy positions 1,2, i.e. a_2 >= frag_small (yes, since frag_small<a_2)
    #   AND a_2 >= a_3 (yes, sorted). So positions 1,2 = a_2, a_2 always. positions 3+ = rest.
    # rest position 3 = max(frag_small, a_3). Parity: pos 3 = odd = +. rest-local pos 1 = odd = +. SAME. Clean!
    return D_alt(rest_pieces), sum(rest_pieces), rest_pieces

# Test pairing on non-dominant configs
print("=== PAIRING strategy test (split L into a_2, L-a_2) ===")
rng = np.random.default_rng(99)
n = 2
Dn = 2**(n+1)-1
tgt = 1.0/Dn
pairing_close = 0
pairing_fail = 0
pairing_clean_but_overshoot = 0
for _ in range(20000):
    k = rng.integers(3, 5)  # 3 or 4 pieces (n+1 or fewer)
    a = np.sort(rng.dirichlet(np.ones(k)))[::-1]
    L, a2 = a[0], a[1]
    if L >= 2*a2:
        continue  # dominant, skip
    res = pairing_D(a)
    if res is None:
        continue
    d_rest, r_total, rest = res
    # After pairing (1 mark used), rest has <= n pieces, total r_total.
    # Induction (n-1 marks) forces D(rest) <= r_total / D_{n-1}.
    Dn1 = 2**n - 1
    ind_bound = r_total / Dn1
    if d_rest <= tgt + 1e-9:
        pairing_close += 1  # pairing alone (1 mark) already caps it!
    elif ind_bound <= tgt + 1e-9:
        pairing_clean_but_overshoot += 1  # pairing + induction closes
    else:
        pairing_fail += 1
        if pairing_fail <= 3:
            print(f"  PAIRING FAIL: cfg={np.round(a,4)}, D_rest={d_rest:.4f}, R={r_total:.4f}, ind_bound={ind_bound:.4f}, tgt={tgt:.4f}")

print(f"n={n} non-dominant: pairing-alone-closes={pairing_close}, pairing+induction-closes={pairing_clean_but_overshoot}, fail={pairing_fail}")

# Now the KEY question: does pairing+induction ALWAYS close in non-dominant case?
# Need: r_total / D_{n-1} <= 1/D_n, i.e. r_total <= D_{n-1}/D_n = (2^n-1)/D_n.
# r_total = 1 - 2*a_2. So need 1 - 2*a_2 <= (2^n-1)/D_n, i.e. a_2 >= (1 - (2^n-1)/D_n)/2 = 2^{n-1}/D_n.
# In non-dominant: a_2 > L/2, and L >= a_2, so a_2 can be as small as... 
# The constraint a_2 >= 2^{n-1}/D_n: is this always true in non-dominant? NO — a_2 can be tiny
# if there are many pieces. E.g. (0.4, 0.2, 0.2, 0.2): L=0.4 < 2*0.2=0.4... boundary.
# (0.39, 0.2, 0.2, 0.21): no. Let me find a counterexample: small a_2 with many pieces.
# (0.5, 0.15, 0.15, 0.1, 0.1): L=0.5, a_2=0.15, L<2*a_2? 0.5<0.3? NO, dominant.
# Need L < 2*a_2 with small a_2: L < 2*a_2 and L >= a_2, so a_2 > L/2 >= ... 
# if L is small (many pieces), a_2 > L/2 but L ~ 1/(n+1). For n=2, 3 pieces, L~1/3, a_2~1/3.
# 2^{n-1}/D_n for n=2 = 2/7 ≈ 0.286. a_2 > L/2, L >= 1/3 (for 3 pieces, L >= 1/3 since sorted).
# Actually L >= 1/(n+1) = 1/3 for 3 pieces. a_2 > L/2 >= 1/6. So a_2 can be < 2/7=0.286!
# Find: L=0.34, a_2=0.18 (> L/2=0.17), a_3=0.48? No, sorted desc: a_3 <= a_2.
# L=0.34, a_2=0.18, a_3=0.48 violates sorted. Need a_3 <= a_2=0.18, sum=1 => rest=0.66, 
# a_3+a_4+... but 3 pieces: a_3 = 1-0.34-0.18 = 0.48 > a_2. Not sorted. 
# For 3 pieces: L + a_2 + a_3 = 1, a_3 <= a_2 => 1-L-a_2 <= a_2 => a_2 >= (1-L)/2.
# Non-dominant: a_2 > L/2. So a_2 in [max((1-L)/2, ...), ...] and a_2 > L/2.
# (1-L)/2 > L/2 iff 1-L > L iff L < 1/2. For 3 pieces L >= 1/3. 
# If L < 1/2: a_2 >= (1-L)/2 > L/2 (auto non-dominant). a_2 >= (1-L)/2.
#   Need a_2 >= 2^{n-1}/D_n = 2/7. (1-L)/2 >= 2/7 iff 1-L >= 4/7 iff L <= 3/7.
#   For 3 pieces L >= 1/3 > 3/7=0.429? No, 1/3 ≈ 0.333 < 0.429. So L in [1/3, 3/7] works.
#   L in (3/7, 1/2): a_2 >= (1-L)/2 < 2/7, so the bound a_2 >= 2/7 might FAIL.
# Find counterexample: L=0.48, 3 pieces, a_2 = (1-0.48)/2 = 0.26, a_3=0.26.
#   a_2=0.26 < 2/7≈0.286. Non-dominant: L=0.48 < 2*0.26=0.52? YES.
#   pairing: r_total = 1-2*0.26 = 0.48. ind_bound = 0.48/3 = 0.16 > 1/7≈0.143. OVERSHOOTS.
cfg = [0.48, 0.26, 0.26]
res = pairing_D(cfg)
print(f"Counterexample cfg={cfg}: pairing D_rest={res[0]:.4f}, R={res[1]:.4f}, ind_bound={res[1]/3:.4f}, tgt={1/7:.4f}")
# Does Xiang still cap it with 2 marks total (1 pairing + 1 more)?
d_opt = best_xiang_D(cfg, 2, grid=40)
print(f"  Xiang optimal with 2 marks: {d_opt:.6f}, target {1/7:.6f}, {'OK' if d_opt<=1/7+1e-9 else 'OVER'}")

print("PART 4 DONE")
