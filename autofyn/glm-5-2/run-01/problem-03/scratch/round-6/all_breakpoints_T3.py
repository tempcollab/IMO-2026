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
    counts = Counter(all_pieces)
    for v in frags:
        if counts[v] < 2:
            return False
    return True

N = 8  # grid resolution
all_bp = []

# Type 1: cascade (3 marks on top)
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
            all_bp.append(('cascade', (q1,q2,q3), all_p, D, sp, Fm, Tm))

# Type 2: split-larger (2 marks on top)
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    if q1 <= 0 or q1 > 4: continue
    for q2n in range(1, int((8-q1)*N/2)+1):
        q2 = F(q2n, N)
        if q2 <= 0 or q2 > (8-q1)/2: break
        frags = [F(8)-q1-q2, q2, q1]
        towers = [F(4), F(2), F(1)]
        all_p = frags + towers
        if not is_breakpoint(frags, all_p): continue
        D = alt_sum(all_p)
        origins = ['F']*3 + ['T']*3
        sp = spine_with_origins(all_p, origins)
        Fm = sum(v for v,o in sp if o=='F')
        Tm = sum(v for v,o in sp if o=='T')
        all_bp.append(('split-larger', (q1,q2), all_p, D, sp, Fm, Tm))

# Type 3: split-tower (1 mark top, 1 mark tower 4)
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
        # breakpoint: every TOP fragment ties
        if not is_breakpoint(frags_top, all_p): continue
        D = alt_sum(all_p)
        origins = ['F','F','T','T','T','T']
        sp = spine_with_origins(all_p, origins)
        Fm = sum(v for v,o in sp if o=='F')
        Tm = sum(v for v,o in sp if o=='T')
        all_bp.append(('split-tower', (q1,q2), all_p, D, sp, Fm, Tm))

# Type 4: 1 on top, 1 on 4, 1 on 2
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
            if not is_breakpoint(frags_top, all_p): continue
            D = alt_sum(all_p)
            origins = ['F','F','T','T','T','T','T']
            sp = spine_with_origins(all_p, origins)
            Fm = sum(v for v,o in sp if o=='F')
            Tm = sum(v for v,o in sp if o=='T')
            all_bp.append(('split-all', (q1,q2,q3), all_p, D, sp, Fm, Tm))

print(f"Total T_3 breakpoints (all types): {len(all_bp)}")
min_D = min(x[3] for x in all_bp)
print(f"Min D at breakpoints: {min_D}")
print()

# Group by F>0 vs F=0
bp_F0 = [x for x in all_bp if x[5] == 0]
bp_Fpos = [x for x in all_bp if x[5] > 0]
print(f"Breakpoints with F=0: {len(bp_F0)}, min D = {min(x[3] for x in bp_F0)}")
print(f"Breakpoints with F>0: {len(bp_Fpos)}, min D = {min(x[3] for x in bp_Fpos) if bp_Fpos else 'N/A'}")
print()

# Check mass-budget inequality T >= 3F - 1 at ALL breakpoints
violations = [x for x in all_bp if x[6] < 3*x[5] - 1]
print(f"Mass-budget violations (T < 3F-1): {len(violations)}")

# Show F>0 breakpoints with smallest D
bp_Fpos_sorted = sorted(bp_Fpos, key=lambda x: x[3])
print(f"\nF>0 breakpoints (smallest D first, up to 15):")
for typ, params, cfg, D, sp, Fm, Tm in bp_Fpos_sorted[:15]:
    # Check block condition on spine
    frag_pos = [i for i,(v,o) in enumerate(sp) if o=='F']
    block = all(i%2==0 for i in frag_pos)
    print(f"  {typ} p={params} D={D} F={Fm} T={Tm} 3F-1={3*Fm-1} T>=3F-1? {Tm>=3*Fm-1} "
          f"spine={[(str(v),o) for v,o in sp]} block={block}")

# Key: is there ANY breakpoint with F>0 and D=1?
bp_d1_Fpos = [x for x in all_bp if x[3] == 1 and x[5] > 0]
print(f"\nD=1 breakpoints with F>0: {len(bp_d1_Fpos)}")
if bp_d1_Fpos:
    print("COUNTEREXAMPLES FOUND!")
    for x in bp_d1_Fpos[:5]:
        print(f"  {x}")
else:
    print("NONE - confirms: D=1 at breakpoint => F=0 (spine dyadic)")
