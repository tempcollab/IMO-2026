import random, itertools

def rand_split(total, parts, rng):
    # random composition of `total` into `parts` positive-ish reals (allow 0)
    if parts==1: return [total]
    cuts = sorted(rng.uniform(0,total) for _ in range(parts-1))
    vals=[]
    prev=0
    for c in cuts:
        vals.append(c-prev); prev=c
    vals.append(total-prev)
    return vals

def gen_Z(n1, b, rng):
    # Z: response to dyadic {1,2,...,2^(n1)} with <=b cuts (n1 pieces indices 0..n1-1 sizes 2^0..2^(n1-1))
    pieces = [2**j for j in range(n1)]
    # choose which pieces get cut, distribute b cuts among them (simple: give each chosen piece some cuts)
    cutcounts = [0]*n1
    budget=b
    # randomly assign
    idxs = list(range(n1))
    rng.shuffle(idxs)
    for idx in idxs:
        if budget<=0: break
        c = rng.randint(0, budget)
        cutcounts[idx]=c
        budget-=c
    Z=[]
    anchors=[]
    for j in range(n1):
        if cutcounts[j]==0:
            Z.append(pieces[j])
            anchors.append(pieces[j])
        else:
            frags = rand_split(pieces[j], cutcounts[j]+1, rng)
            Z.extend(frags)
    return Z, anchors, cutcounts

def gen_Y(n, a, rng):
    # top piece 2^n cut into a+1 fragments
    return rand_split(2**n, a+1, rng)

def compute_run_stats(Y,Z):
    merged = sorted([(w,'T') for w in Y]+[(w,'B') for w in Z], key=lambda x:-x[0])
    c=0
    cs=[]
    for w,lab in merged:
        c += 1 if lab=='T' else -1
        cs.append(c)
    maxc = max(cs) if cs else 0
    # D - 1  = sum psi(c_i) dw_i
    ws = [w for w,l in merged]+[0]
    deficit=0.0
    surplus=0.0
    for i,ci in enumerate(cs):
        dw = ws[i]-ws[i+1]
        psi = (1 if ci%2!=0 else 0) - ci
        if psi<0: deficit += -psi*dw
        else: surplus += psi*dw
    Dtilde = 1 + surplus - deficit
    return maxc, deficit, surplus, Dtilde

rng = random.Random(1)
n=5
results=[]
for trial in range(20000):
    a = rng.randint(1, n-1)
    b = rng.randint(0, n-1-a)  # a+b<=n-1? actually a+b<=n, a in [1,n-1], b in [0,n-a]
    b = rng.randint(0, n-a)
    Y = gen_Y(n, a, rng)
    Z, anchors, cutcounts = gen_Z(n-1, b, rng)  # n1 = n (bottom block has n pieces 2^0..2^(n-1)), wait need n pieces
    maxc, deficit, surplus, Dtilde = compute_run_stats(Y,Z)
    num_uncut = sum(1 for c in cutcounts if c==0)
    results.append((maxc, deficit, surplus, Dtilde, num_uncut, a, b))

# focus maxc>=2
bad = [r for r in results if r[0]>=2]
print("n=",n,"total trials",len(results),"maxc>=2 count",len(bad))
minD = min(r[3] for r in bad) if bad else None
print("min Dtilde among maxc>=2:", minD)
# check correlation deficit vs surplus vs num_uncut
import statistics
for r in bad[:20]:
    print(r)

def altsum(vals):
    vals = sorted(vals, reverse=True)
    s=0
    sign=1
    for v in vals:
        s += sign*v
        sign=-sign
    return s

# check IH: does altsum(Z) >= 1 actually hold for these random Z (n-1 level)?
rng2 = random.Random(2)
n1 = n  # bottom block has n pieces (2^0..2^(n-1)), b cuts budget <= n-1
violations=0
tot=0
minDbot=1e9
for trial in range(20000):
    b = rng2.randint(0, n1-1)
    Z, anchors, cutcounts = gen_Z(n1, b, rng2)
    Dbot = altsum(Z)
    tot+=1
    if Dbot < 1 - 1e-9:
        violations+=1
    minDbot = min(minDbot, Dbot)
print("IH check (Z alone, altsum>=1?): violations", violations, "/", tot, "minDbot", minDbot)
