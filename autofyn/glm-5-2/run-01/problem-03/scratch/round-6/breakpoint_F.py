from fractions import Fraction as F
from collections import Counter, defaultdict

def alt_sum(pieces):
    s = sorted(pieces, reverse=True)
    return sum(((-1)**i)*s[i] for i in range(len(s)))

def is_pow2(x):
    if x <= 0: return False
    if isinstance(x, F):
        if x.denominator == 1:
            n = int(x); return n > 0 and (n & (n-1)) == 0
        num, den = x.numerator, x.denominator
        return (num & (num-1)) == 0 and (den & (den-1)) == 0
    return False

def spine_with_origins(pieces, origins):
    val_origins = defaultdict(list)
    for v, o in zip(pieces, origins):
        val_origins[v].append(o)
    sp = []
    for v in sorted(val_origins.keys(), reverse=True):
        cnt = len(val_origins[v])
        if cnt % 2 == 1:
            origins_list = val_origins[v]
            nF = origins_list.count('F')
            if nF % 2 == 1:
                sp.append((v, 'F'))
            else:
                sp.append((v, 'T'))
    return sp

def is_breakpoint(frags, all_pieces):
    """Every fragment ties an adjacent piece (value appears >= 2 in config)
    OR is a tower piece value (power of 2, can tie a tower piece)."""
    counts = Counter(all_pieces)
    for v in frags:
        if counts[v] < 2:
            return False
    return True

# ===== T_3 all types =====
N = 8

# Type 1: cascade (3 marks on top)
print("T_3 cascade:")
d1_bp_F0 = 0; d1_bp_Fpos = 0; d1_nonbp_Fpos_block = 0; d1_nonbp_Fpos_noblock = 0
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    if q1 <= 0 or q1 > 4: continue
    for q2n in range(1, int(2*q1*N)+1):
        q2 = F(q2n, N)
        if q2 <= 0 or q2 > q1/2: break
        for q3n in range(1, int(2*q2*N)+1):
            q3 = F(q3n, N)
            if q3 <= 0 or q3 > q2/2: break
            frags = [F(8)-q1, q1-q2, q2-q3, q3]
            towers = [F(4), F(2), F(1)]
            all_p = frags + towers
            if alt_sum(all_p) != 1: continue
            origins = ['F']*4 + ['T']*3
            sp = spine_with_origins(all_p, origins)
            Fm = sum(v for v,o in sp if o=='F')
            bp = is_breakpoint(frags, all_p)
            frag_pos = [i for i,(v,o) in enumerate(sp) if o=='F']
            block = all(i%2==0 for i in frag_pos)
            if bp and Fm == 0: d1_bp_F0 += 1
            if bp and Fm > 0: d1_bp_Fpos += 1
            if not bp and Fm > 0 and block: d1_nonbp_Fpos_block += 1
            if not bp and Fm > 0 and not block: d1_nonbp_Fpos_noblock += 1
print(f"  D=1 breakpoints F=0: {d1_bp_F0}, F>0: {d1_bp_Fpos}")
print(f"  D=1 non-bp F>0 block-OK: {d1_nonbp_Fpos_block}, block-FAIL: {d1_nonbp_Fpos_noblock}")

# Type 2: split-larger (2 marks on top, split larger fragment)
print("T_3 split-larger:")
d1_bp_F0 = 0; d1_bp_Fpos = 0; d1_nonbp_Fpos_block = 0; d1_nonbp_Fpos_noblock = 0
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    if q1 <= 0 or q1 > 4: continue
    for q2n in range(1, int((8-q1)*N/2)+1):
        q2 = F(q2n, N)
        if q2 <= 0 or q2 > (8-q1)/2: break
        frags = [F(8)-q1-q2, q2, q1]
        towers = [F(4), F(2), F(1)]
        all_p = frags + towers
        if alt_sum(all_p) != 1: continue
        origins = ['F']*3 + ['T']*3
        sp = spine_with_origins(all_p, origins)
        Fm = sum(v for v,o in sp if o=='F')
        bp = is_breakpoint(frags, all_p)
        frag_pos = [i for i,(v,o) in enumerate(sp) if o=='F']
        block = all(i%2==0 for i in frag_pos)
        if bp and Fm == 0: d1_bp_F0 += 1
        if bp and Fm > 0: d1_bp_Fpos += 1
        if not bp and Fm > 0 and block: d1_nonbp_Fpos_block += 1
        if not bp and Fm > 0 and not block: d1_nonbp_Fpos_noblock += 1
print(f"  D=1 breakpoints F=0: {d1_bp_F0}, F>0: {d1_bp_Fpos}")
print(f"  D=1 non-bp F>0 block-OK: {d1_nonbp_Fpos_block}, block-FAIL: {d1_nonbp_Fpos_noblock}")

# Type 3: split-tower (1 mark on top, 1 on tower 4)
print("T_3 split-tower (1 on top, 1 on tower 4):")
d1_bp_F0 = 0; d1_bp_Fpos = 0; d1_nonbp_Fpos_block = 0; d1_nonbp_Fpos_noblock = 0
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    if q1 <= 0 or q1 > 4: continue
    for q2n in range(1, 2*N+1):
        q2 = F(q2n, N)
        if q2 <= 0 or q2 > 2: break
        frags_top = [F(8)-q1, q1]
        frags_t4 = [F(4)-q2, q2]
        towers = [F(2), F(1)]
        all_p = frags_top + frags_t4 + towers
        if alt_sum(all_p) != 1: continue
        origins = ['F','F','T','T','T','T']
        sp = spine_with_origins(all_p, origins)
        Fm = sum(v for v,o in sp if o=='F')
        bp = is_breakpoint(frags_top, all_p)
        frag_pos = [i for i,(v,o) in enumerate(sp) if o=='F']
        block = all(i%2==0 for i in frag_pos)
        if bp and Fm == 0: d1_bp_F0 += 1
        if bp and Fm > 0: d1_bp_Fpos += 1
        if not bp and Fm > 0 and block: d1_nonbp_Fpos_block += 1
        if not bp and Fm > 0 and not block: d1_nonbp_Fpos_noblock += 1
print(f"  D=1 breakpoints F=0: {d1_bp_F0}, F>0: {d1_bp_Fpos}")
print(f"  D=1 non-bp F>0 block-OK: {d1_nonbp_Fpos_block}, block-FAIL: {d1_nonbp_Fpos_noblock}")

# Type 4: 3 splits on tower pieces (no top split) -- actually top IS split
# 8->(8-q1)+q1, 4->(4-q2)+q2, 2->(2-q3)+q3
print("T_3 split-all-tower (1 on top, 1 on 4, 1 on 2):")
d1_bp_F0 = 0; d1_bp_Fpos = 0; d1_nonbp_Fpos_block = 0; d1_nonbp_Fpos_noblock = 0
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    if q1 <= 0 or q1 > 4: continue
    for q2n in range(1, 2*N+1):
        q2 = F(q2n, N)
        if q2 <= 0 or q2 > 2: break
        for q3n in range(1, N+1):
            q3 = F(q3n, N)
            if q3 <= 0 or q3 > 1: break
            frags_top = [F(8)-q1, q1]
            frags_t4 = [F(4)-q2, q2]
            frags_t2 = [F(2)-q3, q3]
            towers = [F(1)]
            all_p = frags_top + frags_t4 + frags_t2 + towers
            if alt_sum(all_p) != 1: continue
            origins = ['F','F','T','T','T','T','T']
            sp = spine_with_origins(all_p, origins)
            Fm = sum(v for v,o in sp if o=='F')
            bp = is_breakpoint(frags_top, all_p)
            frag_pos = [i for i,(v,o) in enumerate(sp) if o=='F']
            block = all(i%2==0 for i in frag_pos)
            if bp and Fm == 0: d1_bp_F0 += 1
            if bp and Fm > 0: d1_bp_Fpos += 1
            if not bp and Fm > 0 and block: d1_nonbp_Fpos_block += 1
            if not bp and Fm > 0 and not block: d1_nonbp_Fpos_noblock += 1
print(f"  D=1 breakpoints F=0: {d1_bp_F0}, F>0: {d1_bp_Fpos}")
print(f"  D=1 non-bp F>0 block-OK: {d1_nonbp_Fpos_block}, block-FAIL: {d1_nonbp_Fpos_noblock}")

# ===== KEY: at D=1 breakpoints with F>0, check mass-budget inequality =====
print("\n" + "="*70)
print("KEY: Mass-budget inequality at ALL breakpoints (not just D=1)")
print("At a breakpoint, T >= 3F - 1. If D=1 and block holds (all F at +),")
print("then F=T+1 and T>=3(T+1)-1=3T+2 => T<=-1. CONTRADICTION if F>0.")
print("So D=1 breakpoint with F>0 CANNOT have block (all F at +).")
print("Question: do D=1 breakpoints with F>0 even EXIST?")
print("="*70)

# Check ALL breakpoints of T_3 (not just D=1) and their F values
print("\nAll T_3 cascade breakpoints:")
bp_F_values = []
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    if q1 <= 0 or q1 > 4: continue
    for q2n in range(1, int(2*q1*N)+1):
        q2 = F(q2n, N)
        if q2 <= 0 or q2 > q1/2: break
        for q3n in range(1, int(2*q2*N)+1):
            q3 = F(q3n, N)
            if q3 <= 0 or q3 > q2/2: break
            frags = [F(8)-q1, q1-q2, q2-q3, q3]
            towers = [F(4), F(2), F(1)]
            all_p = frags + towers
            if not is_breakpoint(frags, all_p): continue
            D = alt_sum(all_p)
            origins = ['F']*4 + ['T']*3
            sp = spine_with_origins(all_p, origins)
            Fm = sum(v for v,o in sp if o=='F')
            Tm = sum(v for v,o in sp if o=='T')
            bp_F_values.append((D, Fm, Tm, q1, q2, q3, all_p, sp))

print(f"  Total breakpoints: {len(bp_F_values)}")
D_values = sorted(set(x[0] for x in bp_F_values))
print(f"  Distinct D values: {D_values[:15]}")
min_D = min(x[0] for x in bp_F_values)
print(f"  Min D = {min_D}")
for D_val in sorted(set(x[0] for x in bp_F_values))[:10]:
    configs = [x for x in bp_F_values if x[0] == D_val]
    F_vals = [x[1] for x in configs]
    print(f"  D={D_val}: {len(configs)} configs, F values: {sorted(set(F_vals))[:5]}")
