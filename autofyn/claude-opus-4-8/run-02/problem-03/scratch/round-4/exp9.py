from fractions import Fraction as Fr
import random
exec(open('exp1.py').read().split('# random')[0])
# Verify pivot lemma: residual = l1 - sum(S) via (m-1) ops matches a real op sequence; and subtract-all validity for beta>=1/2.
def pivot_subtract_all(pieces):
    p=sorted(pieces,reverse=True); l1=p[0]; others=p[1:]
    # subtract descending
    run=l1; ops=0; residual_pieces=[]
    for s in sorted(others,reverse=True):
        if run>s: run=run-s; ops+=1
        elif run==s: run=Fr(0); ops+=0 # free delete pair
        else:
            return None,None # invalid
    return run, ops  # plus we bisected none; if run>0 it's a single piece
random.seed(3)
for k in range(2,8):
    uk=u(k); ck=c(k); ok=True; worst=Fr(0); nbeta=0
    for _ in range(5000):
        cuts=sorted(Fr(random.randint(1,9999),10000) for _ in range(k))
        pts=[Fr(0)]+cuts+[Fr(1)]
        pieces=sorted([pts[i+1]-pts[i] for i in range(k+1)],reverse=True)
        if any(p==0 for p in pieces):continue
        l1=pieces[0]
        if not(Fr(1,2)<=l1<ck): continue
        nbeta+=1
        res,ops=pivot_subtract_all(pieces)
        # residual should = 2l1-1, ops<=k
        assert res==2*l1-1, (float(res),float(2*l1-1))
        assert ops<=k
        if res/uk>worst: worst=res/uk
        if res>uk: ok=False
    print(f"k={k}: beta in [1/2,c(k)) n={nbeta} subtract-all closes: worstratio={float(worst):.4f} all<=u_k:{ok}")
