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

# Check: at ALL breakpoints of T_n (all types), is F=0 when D=1?
# And is D >= 1 at all breakpoints?

for n, top_val, tower_list in [(3, F(8), [F(4),F(2),F(1)]),
                                (4, F(16), [F(8),F(4),F(2),F(1)]),
                                (5, F(32), [F(16),F(8),F(4),F(2),F(1)])]:
    N = max(4, 8 if n <= 3 else (4 if n == 4 else 2))
    D_n = sum(tower_list) + top_val  # = 2^{n+1}-1
    
    # Cascade type: top split into n fragments via cascading
    # frags = [top-q1, q1-q2, ..., q_{n-1}-qn, qn], towers unsplit
    # For n=3: 4 frags, 3 towers; n=4: 4 frags, 4 towers; n=5: 5 frags, 5 towers
    # But we use n marks -> n+1 fragments? No, cascade with k marks gives k+1 frags.
    # We use up to n marks. Let's use n marks (full cascade).
    
    # Generate cascade params
    import itertools
    
    n_marks = n  # use all n marks on top (cascade)
    # frags = [top - q1, q1 - q2, ..., q_{n-1} - q_n, q_n]  (n+1 frags? no, n frags)
    # Actually: n marks on top -> n+1 fragments
    # cascade: split top, then split larger frag, etc.
    # frags = [top - q1, q1 - q2, ..., q_{k-1} - qk, qk] for k marks -> k+1 frags
    
    nfrags = n_marks + 1  # n+1 fragments
    # For n=3: 4 frags [8-q1, q1-q2, q2-q3, q3]
    # For n=4: 5 frags [16-q1, q1-q2, q2-q3, q3-q4, q4]
    # For n=5: 6 frags [32-q1, q1-q2, q2-q3, q3-q4, q4-q5, q5]
    
    # Grid search over q1, ..., qn
    # q1 in (0, top/2], qi in (0, q_{i-1}/2]
    
    print(f"\n{'='*70}")
    print(f"T_{n} cascade ({n_marks} marks, {nfrags} frags + {len(tower_list)} towers):")
    print(f"{'='*70}")
    
    bp_count = 0
    bp_d1_count = 0
    bp_d1_F0 = 0
    bp_d1_Fpos = 0
    bp_min_D = None
    bp_d1_Fpos_examples = []
    
    # For efficiency, use coarser grid for larger n
    grid = list(range(1, int(top_val)*N+1))
    
    # Generate cascade params recursively
    def gen_cascade_params(depth, prev_q, params):
        if depth == 0:
            yield tuple(params)
            return
        for qn in grid:
            q = F(qn, N)
            if depth == n_marks:
                max_q = top_val / 2
            else:
                max_q = prev_q / 2
            if q <= 0 or q > max_q:
                continue
            yield from gen_cascade_params(depth-1, q, params + [q])
    
    for params in gen_cascade_params(n_marks, top_val, []):
        qs = list(params)
        # frags = [top - q1, q1-q2, ..., q_{k-1}-qk, qk]
        frags = [top_val - qs[0]]
        for i in range(1, n_marks):
            frags.append(qs[i-1] - qs[i])
        frags.append(qs[-1])
        
        all_p = frags + tower_list
        D = alt_sum(all_p)
        
        bp = is_breakpoint(frags, all_p)
        if not bp:
            continue
        bp_count += 1
        if bp_min_D is None or D < bp_min_D:
            bp_min_D = D
        if D == 1:
            bp_d1_count += 1
            origins = ['F']*nfrags + ['T']*len(tower_list)
            sp = spine_with_origins(all_p, origins)
            Fm = sum(v for v,o in sp if o=='F')
            if Fm == 0:
                bp_d1_F0 += 1
            else:
                bp_d1_Fpos += 1
                if len(bp_d1_Fpos_examples) < 5:
                    bp_d1_Fpos_examples.append((params, sorted(all_p,reverse=True), sp, Fm))
    
    print(f"  Total breakpoints: {bp_count}")
    print(f"  Min D at breakpoints: {bp_min_D}")
    print(f"  D=1 breakpoints: {bp_d1_count}")
    print(f"  D=1 bp with F=0: {bp_d1_F0}")
    print(f"  D=1 bp with F>0: {bp_d1_Fpos}")
    if bp_d1_Fpos_examples:
        print(f"  D=1 bp F>0 examples:")
        for params, cfg, sp, Fm in bp_d1_Fpos_examples:
            print(f"    params={params} cfg={[str(x) for x in cfg]} spine={[(str(v),o) for v,o in sp]} F={Fm}")
    
    if bp_d1_Fpos == 0:
        print(f"  >>> CONFIRMED: all D=1 breakpoints have F=0 (spine dyadic)")
    else:
        print(f"  >>> WARNING: D=1 breakpoints with F>0 EXIST!")

