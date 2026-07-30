from fractions import Fraction as F

def L2(u,v):
    M,m=(u,v) if u>=v else (v,u)
    return M if M<=2*m else M/2+m

def V3(x,y,z):
    trip=sorted([x,y,z],reverse=True)
    x,y,z=trip
    sigma=x+y+z
    if x>=F(4,7)*sigma:
        return x/2+L2(y,z)
    elif sigma/2<=x:
        return x
    else:
        return min(x+z/2, y+L2(x-y,z))

def strategies(p1,t1,t2,t3):
    A = t1+V3(*sorted([t2,t3,p1-t1],reverse=True))
    B = p1/2+V3(t1,t2,t3)
    C12 = t2+V3(*sorted([p1,t3,t1-t2],reverse=True))
    C13 = t3+V3(*sorted([p1,t2,t1-t3],reverse=True))
    C23 = t3+V3(*sorted([p1,t1,t2-t3],reverse=True))
    return dict(A=A,B=B,C12=C12,C13=C13,C23=C23)

# try t2=t3 exactly, t1 slightly below 4/15, using nice fractions
# Sigma=15, t1=4-eps... let's use t2=t3=k, t1 = 2k (since found t1~2*t2 numerically: 0.2666/0.1533=1.739 hmm not exactly 2)
# let's just use exact rational near the found optimum: t1=4/15 - tiny, t2=t3
Sigma = F(1)
t1 = F(3999999,15000000)  # slightly less than 4/15=4000000/15000000... let's just do exact with denominator
t1 = F(4,15) - F(1,10**6)
t2 = t3 = (Sigma - t1)/2 * F(1)  # need t1+t2+t3 = Sigma - p1, but p1 unknown; let's directly set t2=t3=x and solve for p1 via target margin like optimizer found
t2 = F(15329037,10**8)
t3 = t2
t1 = F(26665588,10**8)
p1 = Sigma - t1 - t2 - t3
print("p1,t1,t2,t3:", p1,t1,t2,t3, float(p1),float(t1),float(t2),float(t3))
print("sorted check p1>=t1>=t2>=t3:", p1>=t1>=t2>=t3)
print("Case C p1<Sigma/2:", p1<Sigma/2)
print("t1<4/15Sigma:", t1<F(4,15)*Sigma)
Stail=t1+t2+t3
print("t1<Stail/2 (tail case C):", t1<Stail/2, float(t1),float(Stail/2))
vals=strategies(p1,t1,t2,t3)
tgt = F(8,15)*Sigma
print("vals:",{k:float(v) for k,v in vals.items()}, "target",float(tgt))
print("min - target:", float(min(vals.values())-tgt))

print()
print("=== candidate exact interior worst point: (p1,t1,t2,t3) = (8,4,3,2)/17 ===")
p1,t1,t2,t3 = F(8,17),F(4,17),F(3,17),F(2,17)
Sigma=p1+t1+t2+t3
print("Sigma:",Sigma)
print("Case C:", p1<Sigma/2)
print("t1<4/15Sigma:", t1<F(4,15)*Sigma, float(t1),float(F(4,15)*Sigma))
Stail=t1+t2+t3
print("tail case C (t1<Stail/2):", t1<Stail/2)
vals=strategies(p1,t1,t2,t3)
print("vals:",vals)
tgt=F(8,15)*Sigma
print("target:",tgt, float(tgt))
print("min:", min(vals.values()), float(min(vals.values())))
print("margin (target-min):", tgt-min(vals.values()))
