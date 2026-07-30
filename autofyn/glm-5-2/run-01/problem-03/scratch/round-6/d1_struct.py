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

# T_3 cascade: frags = [8-q1, q1-q2, q2-q3, q3], towers = [4, 2, 1]
N = 8
print("T_3 cascade D=1 configs (showing first 20):")
d1 = []
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
            all_pieces = frags + towers
            D = alt_sum(all_pieces)
            if D != 1: continue
            origins = ['F']*4 + ['T']*3
            sp = spine_with_origins(all_pieces, origins)
            F_mass = sum(v for v,o in sp if o=='F')
            T_mass = sum(v for v,o in sp if o=='T')
            counts = Counter(all_pieces)
            is_bp = all(counts[v] >= 2 or is_pow2(v) for v in frags)
            d1.append((q1,q2,q3, all_pieces, sp, F_mass, T_mass, is_bp))

print(f"Total D=1 cascade configs: {len(d1)}")
n_bp = sum(1 for x in d1 if x[7])
n_Fpos = sum(1 for x in d1 if x[5] > 0)
print(f"D=1 breakpoints (every frag ties): {n_bp}")
print(f"D=1 with F>0 (non-dyadic spine): {n_Fpos}")

for i,(q1,q2,q3,cfg,sp,Fm,Tm,bp) in enumerate(d1[:25]):
    sp_str = [(str(v),o) for v,o in sp]
    dyad = all(is_pow2(v) for v in cfg)
    print(f"  q=({q1},{q2},{q3}) cfg={[str(x) for x in sorted(cfg,reverse=True)]} "
          f"spine={sp_str} F={Fm} T={Tm} dyad={dyad} bp={bp}")

# T_3 split-larger: frags = [8-q1-q2, q2, q1], towers = [4, 2, 1]
print("\n" + "="*70)
print("T_3 split-larger D=1 configs (showing first 20):")
d1_sl = []
for q1n in range(1, 4*N+1):
    q1 = F(q1n, N)
    if q1 <= 0 or q1 > 4: continue
    for q2n in range(1, int((8-q1)*N/2)+1):
        q2 = F(q2n, N)
        if q2 <= 0 or q2 > (8-q1)/2: break
        frags = [F(8)-q1-q2, q2, q1]
        towers = [F(4), F(2), F(1)]
        all_pieces = frags + towers
        D = alt_sum(all_pieces)
        if D != 1: continue
        origins = ['F']*3 + ['T']*3
        sp = spine_with_origins(all_pieces, origins)
        F_mass = sum(v for v,o in sp if o=='F')
        T_mass = sum(v for v,o in sp if o=='T')
        counts = Counter(all_pieces)
        is_bp = all(counts[v] >= 2 or is_pow2(v) for v in frags)
        d1_sl.append((q1,q2,all_pieces,sp,F_mass,T_mass,is_bp))

print(f"Total D=1 split-larger configs: {len(d1_sl)}")
n_bp = sum(1 for x in d1_sl if x[6])
n_Fpos = sum(1 for x in d1_sl if x[4] > 0)
print(f"D=1 breakpoints: {n_bp}, D=1 with F>0: {n_Fpos}")
for i,(q1,q2,cfg,sp,Fm,Tm,bp) in enumerate(d1_sl[:20]):
    sp_str = [(str(v),o) for v,o in sp]
    dyad = all(is_pow2(v) for v in cfg)
    print(f"  q=({q1},{q2}) cfg={[str(x) for x in sorted(cfg,reverse=True)]} "
          f"spine={sp_str} F={Fm} T={Tm} dyad={dyad} bp={bp}")
