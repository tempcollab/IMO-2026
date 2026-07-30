from fractions import Fraction as F
import random

def L2(u,v):
    M,m = (u,v) if u>=v else (v,u)
    if M <= 2*m:
        return M
    else:
        return M/2+m

def V3(x,y,z):
    # sorted descending x>=y>=z>0
    assert x>=y>=z, (x,y,z)
    sigma = x+y+z
    if x >= F(4,7)*sigma:
        return x/2 + L2(y,z)
    elif sigma/2 <= x:
        return x
    else:
        # Case C
        return min(x+z/2, y+L2(x-y,z))

def sortdesc(*vals):
    return tuple(sorted(vals, reverse=True))

def StratC23(p1,t1,t2,t3):
    # tie t2,t3, base triple (p1,t1,r), r=t2-t3
    b = t3
    r = t2-t3
    trip = sortdesc(p1,t1,r)
    return b + V3(*trip)

def StratC12(p1,t1,t2,t3):
    b=t2
    r=t1-t2
    trip=sortdesc(p1,t3,r)
    return b+V3(*trip)

def StratC13(p1,t1,t2,t3):
    b=t3
    r=t1-t3
    trip=sortdesc(p1,t2,r)
    return b+V3(*trip)

def StratA(p1,t1,t2,t3):
    r=p1-t1
    trip=sortdesc(t2,t3,r)
    return t1+V3(*trip)

def StratB(p1,t1,t2,t3):
    return p1/2+V3(t1,t2,t3)

def target(p1,t1,t2,t3):
    return F(8,15)*(p1+t1+t2+t3)

def in_region3(p1,t1,t2,t3):
    Sigma=p1+t1+t2+t3
    if not (p1<Sigma/2): return False
    if not (t1 < F(4,15)*Sigma): return False
    Stail=t1+t2+t3
    if not (t1 < Stail/2): return False
    return True

random.seed(1)
N=200000
worst_margin = None
worst_A = None
count=0
c23_wins=0
c23_fails=0
for _ in range(N):
    # random sorted A with rational entries
    p1 = random.randint(1,1000)
    t1 = random.randint(1,p1)
    t2 = random.randint(1,t1)
    t3 = random.randint(1,t2)
    p1,t1,t2,t3 = F(p1),F(t1),F(t2),F(t3)
    if not in_region3(p1,t1,t2,t3):
        continue
    count+=1
    tgt = target(p1,t1,t2,t3)
    c23 = StratC23(p1,t1,t2,t3)
    margin = tgt - c23
    if margin < 0:
        c23_fails+=1
        if worst_margin is None or margin < worst_margin:
            worst_margin = margin
            worst_A = (p1,t1,t2,t3)
    else:
        c23_wins+=1

print("region3 trials found:", count)
print("C23 wins:", c23_wins, "C23 fails:", c23_fails)
if worst_A:
    print("worst margin", worst_margin, "at", worst_A)

print()
print("=== full min-of-5 check, and identify winning strategy where C23 fails ===")
random.seed(2)
N=200000
count=0
viol=0
worst=None
worstA=None
winner_when_c23_fails = {}
for _ in range(N):
    p1 = random.randint(1,2000)
    t1 = random.randint(1,p1)
    t2 = random.randint(1,t1)
    t3 = random.randint(1,t2)
    p1,t1,t2,t3 = F(p1),F(t1),F(t2),F(t3)
    if not in_region3(p1,t1,t2,t3):
        continue
    count+=1
    tgt = target(p1,t1,t2,t3)
    vals = {
        'A': StratA(p1,t1,t2,t3),
        'B': StratB(p1,t1,t2,t3),
        'C12': StratC12(p1,t1,t2,t3),
        'C13': StratC13(p1,t1,t2,t3),
        'C23': StratC23(p1,t1,t2,t3),
    }
    best_strat = min(vals, key=lambda k: vals[k])
    best_val = vals[best_strat]
    margin = tgt - best_val
    if margin < 0:
        viol+=1
        if worst is None or margin<worst:
            worst=margin; worstA=(p1,t1,t2,t3,dict(vals))
    if vals['C23'] > tgt:
        winner_when_c23_fails[best_strat] = winner_when_c23_fails.get(best_strat,0)+1

print("region3 trials:", count, "violations of min(5)<=target:", viol)
if worstA: print("worst:", worstA)
print("when C23 alone fails, which strategy actually wins (count):", winner_when_c23_fails)

print()
print("=== check the round-16 example A=(10,10,10,9) ===")
p1,t1,t2,t3 = F(10),F(10),F(10),F(9)
print("in region3:", in_region3(p1,t1,t2,t3))
print("target", target(p1,t1,t2,t3))
print("A", StratA(p1,t1,t2,t3), "B", StratB(p1,t1,t2,t3), "C12", StratC12(p1,t1,t2,t3), "C13", StratC13(p1,t1,t2,t3), "C23", StratC23(p1,t1,t2,t3))

print()
print("=== check the specific worst-margin witness for C23 alone, is min(5) still fine? ===")
p1,t1,t2,t3 = F(937),F(457),F(390),F(142)
print("in region3:", in_region3(p1,t1,t2,t3))
print("target", target(p1,t1,t2,t3))
print("A", StratA(p1,t1,t2,t3), "B", StratB(p1,t1,t2,t3), "C12", StratC12(p1,t1,t2,t3), "C13", StratC13(p1,t1,t2,t3), "C23", StratC23(p1,t1,t2,t3))

print()
print("=== is there a Region-3 point where ONLY C23 succeeds (A,B,C12,C13 all fail)? ===")
random.seed(3)
N=300000
count=0
only_c23=0
only_c23_examples=[]
strategy_needed_counts = {'A':0,'B':0,'C12':0,'C13':0,'C23':0}
none_win=0
for _ in range(N):
    p1 = random.randint(1,3000)
    t1 = random.randint(1,p1)
    t2 = random.randint(1,t1)
    t3 = random.randint(1,t2)
    p1,t1,t2,t3 = F(p1),F(t1),F(t2),F(t3)
    if not in_region3(p1,t1,t2,t3):
        continue
    count+=1
    tgt = target(p1,t1,t2,t3)
    vals = {
        'A': StratA(p1,t1,t2,t3),
        'B': StratB(p1,t1,t2,t3),
        'C12': StratC12(p1,t1,t2,t3),
        'C13': StratC13(p1,t1,t2,t3),
        'C23': StratC23(p1,t1,t2,t3),
    }
    winners = [k for k,v in vals.items() if v<=tgt]
    if not winners:
        none_win+=1
    elif len(winners)==1:
        strategy_needed_counts[winners[0]]+=1
        if winners[0]=='C23':
            only_c23+=1
            if len(only_c23_examples)<5:
                only_c23_examples.append((p1,t1,t2,t3,dict(vals),tgt))

print("region3 trials:", count)
print("none win (violation):", none_win)
print("exactly-one-strategy-wins counts:", strategy_needed_counts)
print("examples where ONLY C23 wins:")
for ex in only_c23_examples:
    print(ex)

print()
print("=== examples where ONLY A wins ===")
random.seed(3)
N=300000
only_a_examples=[]
for _ in range(N):
    p1 = random.randint(1,3000)
    t1 = random.randint(1,p1)
    t2 = random.randint(1,t1)
    t3 = random.randint(1,t2)
    p1,t1,t2,t3 = F(p1),F(t1),F(t2),F(t3)
    if not in_region3(p1,t1,t2,t3):
        continue
    tgt = target(p1,t1,t2,t3)
    vals = {
        'A': StratA(p1,t1,t2,t3),
        'B': StratB(p1,t1,t2,t3),
        'C12': StratC12(p1,t1,t2,t3),
        'C13': StratC13(p1,t1,t2,t3),
        'C23': StratC23(p1,t1,t2,t3),
    }
    winners = [k for k,v in vals.items() if v<=tgt]
    if winners==['A']:
        only_a_examples.append((p1,t1,t2,t3,dict(vals),tgt))
        if len(only_a_examples)>=8: break

for ex in only_a_examples:
    p1,t1,t2,t3,vals,tgt = ex
    Sigma=p1+t1+t2+t3
    print(f"A={(p1,t1,t2,t3)} Sigma={Sigma} t1/Sigma={float(t1/Sigma):.4f} 4/15={4/15:.4f} vals={vals} tgt={tgt}")
