"""Re-run with HARD validation: sum(full) must == D_n = 2^{n+1}-1.
Also re-examine the split-tower origin tracking and the clean restatement."""
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

def analyze(frags, towers, origins, label, D_n):
    full = list(frags) + list(towers)
    if sum(full) != D_n:
        return None  # spurious
    D = alt_sum(full)
    sp = spine_with_origins(full, origins)
    f_pos = [i for i,(v,o) in enumerate(sp) if o == 'F']
    t_pos = [i for i,(v,o) in enumerate(sp) if o == 'T']
    F_mass = sum(sp[i][0] for i in f_pos)
    T_mass = sum(sp[i][0] for i in t_pos)
    f_plus = sum(sp[i][0] for i in f_pos if i % 2 == 0)
    f_minus = sum(sp[i][0] for i in f_pos if i % 2 == 1)
    t_plus = sum(sp[i][0] for i in t_pos if i % 2 == 0)
    t_minus = sum(sp[i][0] for i in t_pos if i % 2 == 1)
    block = (all(i % 2 == 0 for i in f_pos) or all(i % 2 == 1 for i in f_pos)) if f_pos else True
    pattern = all(i % 2 == 0 for i in f_pos) and all(i % 2 == 1 for i in t_pos)
    return {'frags': sorted(frags,reverse=True), 'towers': sorted(towers,reverse=True),
            'D': D, 'spine': sp, 'F_mass': F_mass, 'T_mass': T_mass,
            'f_plus': f_plus, 'f_minus': f_minus, 't_plus': t_plus, 't_minus': t_minus,
            'block': block, 'pattern': pattern,
            'budget': T_mass - (3*F_mass - 1), 'label': label}

def enum_cascade(n, r):
    top = F(2)**n
    D_n = F(2)**(n+1) - 1
    towers = [F(2)**(n-1-k) for k in range(n)]
    tower_vals = sorted(set(towers), reverse=True)
    idx = list(range(r))
    res = []
    for groups in set_partitions(idx):
        ngroups = len(groups)
        choices = [list(tower_vals) + ['free'] for _ in groups]
        for combo in product(*choices):
            if any(combo[gi]=='free' and len(groups[gi])<2 for gi in range(ngroups)): continue
            free_groups = [gi for gi in range(ngroups) if combo[gi]=='free']
            nfree = len(free_groups)
            fv = [None]*r
            for gi,g in enumerate(groups):
                if combo[gi]!='free':
                    for i in g: fv[i] = combo[gi]
            if nfree == 0:
                if sum(fv) != top: continue
                frags = sorted(fv, reverse=True)
            elif nfree == 1:
                g0 = groups[free_groups[0]]
                known = sum(fv[i] for i in range(r) if fv[i] is not None)
                v = (top - known)/len(g0)
                if v <= 0: continue
                for i in g0: fv[i] = v
                frags = sorted(fv, reverse=True)
            else: continue
            if any(f<=0 for f in frags): continue
            if frags != sorted(frags, reverse=True): continue
            origins = ['F']*len(frags) + ['T']*len(towers)
            a = analyze(frags, towers, origins, f"cascade n={n} r={r}", D_n)
            if a: res.append(a)
    return res

def enum_split_tower(n, k):
    """Top 2^n split into 2 frags; tower 2^k split into 2 frags; rest unsplit.
    frags_top (sum top, origin F) + frags_tk (sum tow_k, origin T) + unsplit (origin T)."""
    top = F(2)**n
    tow_k = F(2)**k
    D_n = F(2)**(n+1) - 1
    unsplit = [F(2)**j for j in range(n) if j != k]
    tower_vals = sorted(set([F(2)**j for j in range(n)]), reverse=True)
    idx = [0,1,2,3]  # 0,1 = top frags; 2,3 = tower-k frags
    res = []
    for groups in set_partitions(idx):
        ngroups = len(groups)
        choices = [list(tower_vals) + ['free'] for _ in groups]
        for combo in product(*choices):
            if any(combo[gi]=='free' and len(groups[gi])<2 for gi in range(ngroups)): continue
            free_groups = [gi for gi in range(ngroups) if combo[gi]=='free']
            nfree = len(free_groups)
            fv = [None]*4
            for gi,g in enumerate(groups):
                if combo[gi]!='free':
                    for i in g: fv[i] = combo[gi]
            if nfree == 0:
                if fv[0]+fv[1] != top or fv[2]+fv[3] != tow_k: continue
                frags = list(fv)
            elif nfree == 1:
                g0 = groups[free_groups[0]]
                fit = [i for i in g0 if i in (0,1)]
                fik = [i for i in g0 if i in (2,3)]
                kt = sum(fv[i] for i in (0,1) if fv[i] is not None)
                kk = sum(fv[i] for i in (2,3) if fv[i] is not None)
                vA = (top - kt)/len(fit) if fit else None
                vB = (tow_k - kk)/len(fik) if fik else None
                if fit and fik:
                    if vA != vB: continue
                    v = vA
                elif fit: v = vA
                else: v = vB
                if v is None or v <= 0: continue
                for i in g0: fv[i] = v
                frags = list(fv)
                # VALIDATE sums
                if fv[0]+fv[1] != top or fv[2]+fv[3] != tow_k: continue
            else: continue
            if fv[1] > fv[0]: continue
            if fv[3] > fv[2]: continue
            if any(f<=0 for f in frags): continue
            origins = ['F','F','T','T'] + ['T']*len(unsplit)
            a = analyze(frags, unsplit, origins, f"split-tower n={n} k={k}", D_n)
            if a: res.append(a)
    return res

# Also split-all-tower: top split into 2 frags + TWO tower pieces split.
def enum_split_two_tower(n, k1, k2):
    top = F(2)**n; tk1 = F(2)**k1; tk2 = F(2)**k2
    D_n = F(2)**(n+1)-1
    unsplit = [F(2)**j for j in range(n) if j not in (k1,k2)]
    tower_vals = sorted(set([F(2)**j for j in range(n)]), reverse=True)
    idx = [0,1,2,3,4,5]  # 0,1 top; 2,3 tower-k1; 4,5 tower-k2
    res = []
    for groups in set_partitions(idx):
        ngroups = len(groups)
        choices = [list(tower_vals) + ['free'] for _ in groups]
        for combo in product(*choices):
            if any(combo[gi]=='free' and len(groups[gi])<2 for gi in range(ngroups)): continue
            free_groups = [gi for gi in range(ngroups) if combo[gi]=='free']
            nfree = len(free_groups)
            fv = [None]*6
            for gi,g in enumerate(groups):
                if combo[gi]!='free':
                    for i in g: fv[i] = combo[gi]
            if nfree == 0:
                if fv[0]+fv[1]!=top or fv[2]+fv[3]!=tk1 or fv[4]+fv[5]!=tk2: continue
                frags = list(fv)
            elif nfree == 1:
                g0 = groups[free_groups[0]]
                # three sum constraints
                fit=[i for i in g0 if i in (0,1)]; fi1=[i for i in g0 if i in (2,3)]; fi2=[i for i in g0 if i in (4,5)]
                kt=sum(fv[i] for i in (0,1) if fv[i] is not None)
                k1s=sum(fv[i] for i in (2,3) if fv[i] is not None)
                k2s=sum(fv[i] for i in (4,5) if fv[i] is not None)
                vs=[]
                if fit: vs.append((top-kt)/len(fit))
                if fi1: vs.append((tk1-k1s)/len(fi1))
                if fi2: vs.append((tk2-k2s)/len(fi2))
                if len(set(vs))!=1: continue
                v=vs[0]
                if v<=0: continue
                for i in g0: fv[i]=v
                frags=list(fv)
                if fv[0]+fv[1]!=top or fv[2]+fv[3]!=tk1 or fv[4]+fv[5]!=tk2: continue
            else: continue
            if fv[1]>fv[0] or fv[3]>fv[2] or fv[5]>fv[4]: continue
            if any(f<=0 for f in frags): continue
            origins=['F','F','T','T','T','T']+['T']*len(unsplit)
            a=analyze(frags, unsplit, origins, f"split-2tower n={n} k1={k1} k2={k2}", D_n)
            if a: res.append(a)
    return res

all_verts = []
all_verts += enum_cascade(3,4)+enum_cascade(3,3)+enum_cascade(3,2)
all_verts += enum_split_tower(3,2)+enum_split_tower(3,1)
all_verts += enum_split_two_tower(3,2,1)
all_verts += enum_cascade(4,4)+enum_cascade(4,3)+enum_cascade(4,5)+enum_cascade(4,2)
all_verts += enum_split_tower(4,3)+enum_split_tower(4,2)+enum_split_tower(4,1)
all_verts += enum_split_two_tower(4,3,2)+enum_split_two_tower(4,3,1)+enum_split_two_tower(4,2,1)

seen=set(); uniq=[]
for v in all_verts:
    key=(tuple(v['frags']),tuple(v['towers']),tuple(v['label'].split()[0]+' '+v['label'].split('k')[0]))
    if key in seen: continue
    seen.add(key); uniq.append(v)

print(f"Total valid strong-breakpoint vertices (T_3+T_4, all types): {len(uniq)}")
print(f"  with D < 1: {sum(1 for v in uniq if v['D']<1)}")
print(f"  with D = 1: {sum(1 for v in uniq if v['D']==1)}")
print(f"  min D overall: {min(v['D'] for v in uniq)}")
d1=[v for v in uniq if v['D']==1]
print(f"\nD=1 vertices: {len(d1)}")
print(f"  D=1 with block FAIL: {sum(1 for v in d1 if not v['block'])}")
print(f"  D=1 with block OK: {sum(1 for v in d1 if v['block'])}")
for v in d1:
    sp=[(str(val),o) for val,o in v['spine']]
    print(f"    D={v['D']} frags={v['frags']} towers={v['towers']} F={v['F_mass']} T={v['T_mass']} "
          f"block={v['block']} pattern={v['pattern']} label={v['label']} spine={sp}")
print(f"\nD<1 vertices (COUNTEREXAMPLES?):")
for v in uniq:
    if v['D']<1:
        print(f"  D={v['D']} frags={v['frags']} towers={v['towers']} label={v['label']}")
print("(if none, lower bound D>=1 holds at all strong-breakpoint vertices)")
