from fractions import Fraction as Fr
import random

def u(k): return Fr(1,2**(k+1)-1)
def c(k): return Fr(2**k,2**(k+1)-1)

def free_deletes(p):
    p=sorted(p,reverse=True)
    i=0
    while i<len(p)-1:
        if p[i]==p[i+1]:
            del p[i+1]; del p[i]
            i=0
        else:
            i+=1
    return p

def strat_top2(pieces,budget):
    # deterministic: pin l2 into l1 (l1-l2), free-delete pairs, repeat. bisect if only 1 piece? stop.
    p=free_deletes(list(pieces))
    while budget>0 and len(p)>=2:
        p=sorted(p,reverse=True)
        l1,l2=p[0],p[1]
        rem=l1-l2
        newp=p[2:]+([rem] if rem>0 else [])
        p=free_deletes(newp)
        budget-=1
    return sum(p,Fr(0))

def strat_subtract_all(pieces,budget):
    # pin l2,l3,... into running top (subtract). if running < next, stop / switch.
    p=sorted(pieces,reverse=True)
    top=p[0]; rest=p[1:]; budget2=budget
    for x in rest:
        if budget2<=0: 
            return top+sum(rest[rest.index(x):],Fr(0)) # rough
        if top>x:
            top=top-x; budget2-=1
        elif top==x:
            top=Fr(0); budget2-=0 # free delete
        else:
            # can't subtract; fall back
            return None
    return top

def strat_smallest(pieces,budget):
    # pin smallest into largest repeatedly, free-delete
    p=free_deletes(list(pieces))
    while budget>0 and len(p)>=2:
        p=sorted(p,reverse=True)
        l1=p[0]; lm=p[-1]
        if l1==lm: break
        rem=l1-lm
        newp=p[1:-1]+[rem]
        p=free_deletes(newp)
        budget-=1
    return sum(p,Fr(0))

random.seed(2)
for k in range(2,6):
    uk=u(k);ck=c(k)
    m1=m2=m3=Fr(0); worst=None
    cnt=0
    for _ in range(2000):
        cuts=sorted(Fr(random.randint(1,9999),10000) for _ in range(k))
        pts=[Fr(0)]+cuts+[Fr(1)]
        pieces=sorted([pts[i+1]-pts[i] for i in range(k+1)],reverse=True)
        if any(p==0 for p in pieces):continue
        l1=pieces[0];l2=pieces[1]
        if not(l1<ck and 2*l2<ck):continue
        if not l1<Fr(1,2): continue  # focus beta<1/2
        cnt+=1
        r1=strat_top2(pieces,k)
        r3=strat_smallest(pieces,k)
        m1=max(m1,r1/uk); m3=max(m3,r3/uk)
    print(f"k={k} beta<1/2 cnt={cnt}  top2 maxratio={float(m1):.4f}  smallest maxratio={float(m3):.4f}")
