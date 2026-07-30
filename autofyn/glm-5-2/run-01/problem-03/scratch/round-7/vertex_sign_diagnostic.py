"""
Round 7: Diagnostic — WHY does F>0 at a strong breakpoint force D>1?

Restatement of the crux (cleaner than "balance->block on faces"):
  pl-breakpoint-minimum (certified) => global min of D is at a PL VERTEX (strong breakpoint).
  Exhaustive enumeration (this round, exact Fraction) shows:
    - At every strong breakpoint of T_3, T_4 (all refinement types), D >= 1.
    - D = 1 ONLY at DYADIC vertices (F = 0, no surviving non-dyadic fragments).
    - Every non-dyadic vertex (F > 0) has D > 1 (smallest D = 5/3).
  So the crux reduces to: WHY does F > 0 at a strong breakpoint force D > 1?

This script dumps the full sign/spine structure of EVERY non-dyadic strong breakpoint
of T_3 (cascade r=4, split-larger r=3, split-tower) and looks for the structural reason:
  - the spine's sign assignment (which positions are F vs T)
  - whether the block condition holds on the spine
  - the mass-budget T vs 3F-1
  - the value of D and its decomposition D = (F-T) + 2(t+ - f-)

We also test a CONJECTURED mechanism: at a non-dyadic vertex, the spine CANNOT have the
all-frag-+/all-tower- pattern (block condition) because the mass-budget T >= 3F-1 with
F = T+1 (needed for D=1 under block) gives T <= -1. And WITHOUT the block pattern, D is
pushed above 1 by the sign-mixing term 2(t+ - f-). The question: is 2(t+ - f-) always
large enough (given the sort-order sign assignment) to push D above 1?
"""
from fractions import Fraction as F
from collections import Counter, defaultdict
from itertools import product

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

def set_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first = items[0]
    rest = items[1:]
    for sp in set_partitions(rest):
        yield [[first]] + sp
        for i, g in enumerate(sp):
            new_sp = [list(g2) for g2 in sp]
            new_sp[i] = [first] + list(g)
            yield new_sp

def spine_with_origins(pieces, origins):
    val_count = Counter(pieces)
    val_origins = defaultdict(list)
    for v, o in zip(pieces, origins):
        val_origins[v].append(o)
    sp = []
    for v in sorted(val_count.keys(), reverse=True):
        cnt = val_count[v]
        if cnt % 2 == 1:
            olist = val_origins[v]
            nF = olist.count('F')
            if nF % 2 == 1:
                sp.append((v, 'F'))
            else:
                sp.append((v, 'T'))
    return sp

def analyze_vertex(frags, towers, origins, label=""):
    """Full diagnostic of one strong breakpoint vertex."""
    full = list(frags) + list(towers)
    D = alt_sum(full)
    sp = spine_with_origins(full, origins)
    # Spine sign analysis
    f_pos = [i for i,(v,o) in enumerate(sp) if o == 'F']
    t_pos = [i for i,(v,o) in enumerate(sp) if o == 'T']
    F_mass = sum(sp[i][0] for i in f_pos)
    T_mass = sum(sp[i][0] for i in t_pos)
    f_plus = sum(sp[i][0] for i in f_pos if i % 2 == 0)
    f_minus = sum(sp[i][0] for i in f_pos if i % 2 == 1)
    t_plus = sum(sp[i][0] for i in t_pos if i % 2 == 0)
    t_minus = sum(sp[i][0] for i in t_pos if i % 2 == 1)
    block = (all(i % 2 == 0 for i in f_pos) or all(i % 2 == 1 for i in f_pos))
    pattern = all(i % 2 == 0 for i in f_pos) and all(i % 2 == 1 for i in t_pos)
    return {
        'frags': sorted(frags, reverse=True), 'towers': sorted(towers, reverse=True),
        'D': D, 'spine': sp, 'F_mass': F_mass, 'T_mass': T_mass,
        'f_plus': f_plus, 'f_minus': f_minus, 't_plus': t_plus, 't_minus': t_minus,
        'block': block, 'pattern': pattern,
        'budget': T_mass - (3*F_mass - 1),  # T - (3F-1), should be >= 0
        'Ddecomp': (F_mass - T_mass) + 2*(t_plus - f_minus),  # = D under any sign
        'label': label,
    }

def enum_cascade_vertices(n, r):
    top = F(2)**n
    towers = [F(2)**(n-1-k) for k in range(n)]
    tower_vals = sorted(set(towers), reverse=True)
    idx = list(range(r))
    results = []
    for groups in set_partitions(idx):
        ngroups = len(groups)
        choices = [list(tower_vals) + ['free'] for _ in groups]
        for combo in product(*choices):
            valid = all(not (combo[gi] == 'free' and len(groups[gi]) < 2)
                       for gi in range(ngroups))
            if not valid: continue
            free_groups = [gi for gi in range(ngroups) if combo[gi] == 'free']
            nfree = len(free_groups)
            frag_val = [None]*r
            for gi, g in enumerate(groups):
                if combo[gi] != 'free':
                    for i in g: frag_val[i] = combo[gi]
            if nfree == 0:
                if sum(frag_val) != top: continue
                frags = sorted(frag_val, reverse=True)
            elif nfree == 1:
                g0 = groups[free_groups[0]]
                known = sum(frag_val[i] for i in range(r) if frag_val[i] is not None)
                v = (top - known) / len(g0)
                if v <= 0: continue
                for i in g0: frag_val[i] = v
                frags = sorted(frag_val, reverse=True)
            else:
                continue
            if any(f <= 0 for f in frags): continue
            if frags != sorted(frags, reverse=True): continue
            origins = ['F']*len(frags) + ['T']*len(towers)
            results.append(analyze_vertex(frags, towers, origins, f"cascade n={n} r={r}"))
    return results

def enum_split_tower_vertices(n, k):
    top = F(2)**n
    tow_k = F(2)**k
    unsplit = [F(2)**j for j in range(n) if j != k]
    tower_vals = sorted(set([F(2)**j for j in range(n)]), reverse=True)
    idx = [0,1,2,3]
    results = []
    for groups in set_partitions(idx):
        ngroups = len(groups)
        choices = [list(tower_vals) + ['free'] for _ in groups]
        for combo in product(*choices):
            valid = all(not (combo[gi] == 'free' and len(groups[gi]) < 2)
                       for gi in range(ngroups))
            if not valid: continue
            free_groups = [gi for gi in range(ngroups) if combo[gi] == 'free']
            nfree = len(free_groups)
            frag_val = [None]*4
            for gi, g in enumerate(groups):
                if combo[gi] != 'free':
                    for i in g: frag_val[i] = combo[gi]
            if nfree == 0:
                if frag_val[0]+frag_val[1] != top or frag_val[2]+frag_val[3] != tow_k: continue
                frags = list(frag_val)
            elif nfree == 1:
                g0 = groups[free_groups[0]]
                free_in_top = [i for i in g0 if i in (0,1)]
                free_in_k = [i for i in g0 if i in (2,3)]
                known_top = sum(frag_val[i] for i in (0,1) if frag_val[i] is not None)
                known_k = sum(frag_val[i] for i in (2,3) if frag_val[i] is not None)
                vA = (top - known_top)/len(free_in_top) if free_in_top else None
                vB = (tow_k - known_k)/len(free_in_k) if free_in_k else None
                if free_in_top and free_in_k:
                    if vA != vB: continue
                    v = vA
                elif free_in_top: v = vA
                else: v = vB
                if v is None or v <= 0: continue
                for i in g0: frag_val[i] = v
                frags = list(frag_val)
            else: continue
            if frag_val[1] > frag_val[0]: continue
            if frag_val[3] > frag_val[2]: continue
            if any(f <= 0 for f in frags): continue
            origins = ['F','F','T','T'] + ['T']*len(unsplit)
            results.append(analyze_vertex(frags, unsplit, origins, f"split-tower n={n} k={k}"))
    return results

# Collect ALL non-dyadic vertices (F_mass > 0) for T_3 and T_4
all_verts = []
all_verts += enum_cascade_vertices(3, 4)
all_verts += enum_cascade_vertices(3, 3)
all_verts += enum_cascade_vertices(3, 2)
all_verts += enum_split_tower_vertices(3, 2)
all_verts += enum_split_tower_vertices(3, 1)
all_verts += enum_cascade_vertices(4, 4)
all_verts += enum_cascade_vertices(4, 3)
all_verts += enum_cascade_vertices(4, 5)
all_verts += enum_split_tower_vertices(4, 3)
all_verts += enum_split_tower_vertices(4, 2)
all_verts += enum_split_tower_vertices(4, 1)

# dedupe by (sorted frags, sorted towers)
seen = set()
uniq = []
for v in all_verts:
    key = (tuple(v['frags']), tuple(v['towers']))
    if key in seen: continue
    seen.add(key)
    uniq.append(v)

print(f"Total unique strong-breakpoint vertices (T_3 + T_4): {len(uniq)}")
nondy = [v for v in uniq if v['F_mass'] > 0]
print(f"Non-dyadic vertices (F>0): {len(nondy)}")
print(f"Dyadic vertices (F=0): {len(uniq) - len(nondy)}")
print(f"Min D at non-dyadic vertices: {min(v['D'] for v in nondy)}")
print(f"Min D at dyadic vertices: {min(v['D'] for v in uniq if v['F_mass']==0)}")
# D=1 vertices: are they all dyadic?
d1 = [v for v in uniq if v['D'] == 1]
print(f"\nD=1 vertices: {len(d1)}, all with F=0: {all(v['F_mass']==0 for v in d1)}")
# Non-dyadic: what's the min D, and the structure there?
print(f"\n--- Non-dyadic vertices: D distribution ---")
from collections import Counter
ddist = Counter(v['D'] for v in nondy)
for d in sorted(ddist):
    print(f"  D={d} : {ddist[d]}")

print(f"\n--- Non-dyadic vertices with SMALLEST D (the hardest cases) ---")
nondy_sorted = sorted(nondy, key=lambda v: v['D'])
for v in nondy_sorted[:25]:
    sp_str = [(str(val), o, ('+' if i%2==0 else '-')) for i,(val,o) in enumerate(v['spine'])]
    print(f"  D={v['D']} frags={v['frags']} F={v['F_mass']} T={v['T_mass']} "
          f"budget(T-3F+1)={v['budget']} block={v['block']} pattern={v['pattern']} "
          f"f+={v['f_plus']} f-={v['f_minus']} t+={v['t_plus']} t-={v['t_minus']} "
          f"spine={sp_str}")

# Key test: at non-dyadic vertices, does the block condition EVER hold?
print(f"\n--- Non-dyadic vertices: block condition on spine ---")
nondy_block = [v for v in nondy if v['block']]
nondy_noblock = [v for v in nondy if not v['block']]
print(f"  block holds: {len(nondy_block)}")
print(f"  block fails: {len(nondy_noblock)}")
for v in nondy_block:
    sp_str = [(str(val), o) for i,(val,o) in enumerate(v['spine'])]
    print(f"  BLOCK HOLDS (F>0): D={v['D']} frags={v['frags']} F={v['F_mass']} T={v['T_mass']} "
          f"budget={v['budget']} pattern={v['pattern']} spine={sp_str}")

# THE MECHANISM QUESTION: for non-dyadic vertices, D = (F-T) + 2(t+ - f-).
# D=1 requires (F-T) + 2(t+ - f-) = 1. With T >= 3F-1 => F-T <= 1-2F.
# So D <= 1 - 2F + 2(t+ - f-). For D=1: t+ - f- >= F.
# Is t+ - f- always < F when F>0 (which would force D<1... no that's wrong direction)?
# We want D > 1. D > 1 iff (F-T) + 2(t+ - f-) > 1.
# Let's check: at every non-dyadic vertex, is (F-T) + 2(t+ - f-) > 1? (it is, since D>1)
# The structural question: WHY is t+ - f- never big enough to bring D down to 1?
print(f"\n--- Sign-mixing term t+ - f- at non-dyadic vertices ---")
for v in nondy_sorted[:15]:
    print(f"  D={v['D']} F-T={v['F_mass']-v['T_mass']} t+-f-={v['t_plus']-v['f_minus']} "
          f"2(t+-f-)={2*(v['t_plus']-v['f_minus'])} frags={v['frags']}")

# Test the conjectured mechanism: t+ - f- < F whenever F>0 at a vertex?
# (This would give D = (F-T) + 2(t+-f-) < (F-T) + 2F = 3F - T. With T >= 3F-1, 3F-T <= 1.
#  So D < ... no. Let's just check t+ - f- vs F directly.)
print(f"\n--- Is (t+ - f-) < F at non-dyadic vertices? ---")
cnt_lt = sum(1 for v in nondy if v['t_plus'] - v['f_minus'] < v['F_mass'])
cnt_eq = sum(1 for v in nondy if v['t_plus'] - v['f_minus'] == v['F_mass'])
cnt_gt = sum(1 for v in nondy if v['t_plus'] - v['f_minus'] > v['F_mass'])
print(f"  t+-f- < F: {cnt_lt}, == F: {cnt_eq}, > F: {cnt_gt}")
