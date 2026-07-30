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
    import math
    lg = math.log2(x) if x > 0 else -1
    return abs(lg - round(lg)) < 1e-9 and round(lg) >= -20

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

# T_3 cascade: 8 -> (8-q1)+q1 -> (q1-q2)+q2 -> (q2-q3)+q3
# frags = [8-q1, q1-q2, q2-q3, q3], towers = [4, 2, 1]
N = 8
print("="*70)
print("T_3 cascade: D=1 breakpoints with spine analysis")
print("="*70)

d1_count = 0
examples_with_F = []
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
            d1_count += 1
            origins = ['F']*4 + ['T']*3
            sp = spine_with_origins(all_pieces, origins)
            F_mass = sum(v for v,o in sp if o=='F')
            T_mass = sum(v for v,o in sp if o=='T')
            # Check breakpoint: every fragment ties an adjacent piece
            # (every piece value appears >= 2 times OR is a tower piece)
            counts = Counter(all_pieces)
            is_breakpoint = True
            for v in frags:
                if counts[v] < 2 and not is_pow2(v):
                    is_breakpoint = False
                    break
            if F_mass > 0 and is_breakpoint:
                if len(examples_with_F) < 15:
                    examples_with_F.append({
                        'q': (q1,q2,q3), 'cfg': sorted(all_pieces, reverse=True),
                        'spine': sp, 'F': F_mass, 'T': T_mass,
                        'D_sp': alt_sum([v for v,o in sp]),
                        'breakpoint': is_breakpoint
                    })

print(f"Total D=1 cascade configs: {d1_count}")
print(f"D=1 breakpoints with F>0: {len(examples_with_F)}")
for ex in examples_with_F[:10]:
    sp_str = [(str(v), o) for v,o in ex['spine']]
    print(f"  q={ex['q']} cfg={[str(x) for x in ex['cfg']]}")
    print(f"    spine={sp_str} F={ex['F']} T={ex['T']} D(sp)={ex['D_sp']} bp={ex['breakpoint']}")
    # Check: is 3F <= 8? Is T >= 3F - 1?
    print(f"    3*F={3*ex['F']} <= 8? {3*ex['F'] <= 8}, T={ex['T']} >= 3F-1={3*ex['F']-1}? {ex['T'] >= 3*ex['F']-1}")

# Now check: for D=1 breakpoints with F>0, verify block condition on spine
print("\n" + "="*70)
print("Block condition check on spine for D=1 breakpoints with F>0")
print("="*70)
block_ok = 0
block_fail = 0
for ex in examples_with_F:
    sp = ex['spine']
    frag_positions = [i for i,(v,o) in enumerate(sp) if o=='F']
    all_frag_plus = all(i % 2 == 0 for i in frag_positions)
    if all_frag_plus:
        block_ok += 1
    else:
        block_fail += 1
        print(f"  BLOCK FAIL: q={ex['q']} spine={[(str(v),o) for v,o in sp]} frag_pos={frag_positions}")

print(f"Block OK: {block_ok}, Block FAIL: {block_fail}")

# Key test: the mass budget inequality T >= 3F - 1
print("\n" + "="*70)
print("Mass budget inequality: T >= 3F - 1 (derived from 2^n >= 3F + (2^n-1) - T)")
print("="*70)
violations = 0
for ex in examples_with_F:
    if ex['T'] < 3*ex['F'] - 1:
        violations += 1
        print(f"  VIOLATION: F={ex['F']} T={ex['T']} 3F-1={3*ex['F']-1}")
print(f"Violations: {violations} / {len(examples_with_F)}")

# Also test: for block-holding D=1, D = F - T = 1, so F = T+1.
# Combined with T >= 3F-1: T >= 3(T+1)-1 = 3T+2, so -2T >= 2, T <= -1. CONTRADICTION if F>0.
print("\n" + "="*70)
print("Key test: if block holds (all F at +), D=F-T. D=1 => F=T+1.")
print("Combined with T>=3F-1=3T+2 => T<=-1. Contradiction if F>0!")
print("So: D=1 breakpoint with F>0 CANNOT have all fragments at +.")
print("="*70)
print(f"Among D=1 breakpoints with F>0, how many have all F at +? {block_ok}")
print(f"If 0, then the block condition (all F at +) NEVER holds with F>0.")
print(f"This means: when F>0, the block condition must fail OR all F at -.")
