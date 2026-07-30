from fractions import Fraction as Fr
exec(open('exp1.py').read().split('# random')[0])

def eval_trace(pieces,budget,memo):
    pieces=tuple(sorted(pieces,reverse=True))
    if budget<=0 or len(pieces)==0:
        return sum(pieces,Fr(0)),[]
    best=sum(pieces,Fr(0)); bestmove=[('stop',)]
    m=len(pieces)
    for i in range(m):
        for j in range(i+1,m):
            if pieces[i]==pieces[j]:
                newp=pieces[:i]+pieces[i+1:j]+pieces[j+1:]
                v,tr=eval_trace(newp,budget,memo)
                if v<best: best=v;bestmove=[('free',float(pieces[i]))]+tr
                break
    for i in range(m):
        newp=pieces[:i]+pieces[i+1:]
        v,tr=eval_trace(newp,budget-1,memo)
        if v<best: best=v;bestmove=[('bisect',float(pieces[i]))]+tr
    for i in range(m):
        for j in range(m):
            if i!=j and pieces[i]>pieces[j]:
                rem=pieces[i]-pieces[j]
                newp=tuple(pieces[x] for x in range(m) if x!=i and x!=j)+(rem,)
                v,tr=eval_trace(newp,budget-1,memo)
                if v<best: best=v;bestmove=[('pin',float(pieces[i]),float(pieces[j]),'->',float(rem))]+tr
    return best,bestmove

for pieces in [[Fr(467,1000),Fr(235,1000),Fr(177,1000),Fr(121,1000)],
               [Fr(49,100),Fr(20,100),Fr(18,100),Fr(13,100)],
               [Fr(4,15),Fr(4,15),Fr(4,15),Fr(3,15)]]:
    s=sum(pieces,Fr(0))
    pn=[p/s for p in pieces]
    r,tr=eval_trace(tuple(pn),3,{})
    print("pieces(norm)=",[round(float(x),4) for x in pn],"residual/u3=",round(float(r/u(3)),4))
    for mv in tr: print("   ",mv)
