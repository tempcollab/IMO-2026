from fractions import Fraction as Fr
exec(open('exp4.py').read().split('for pieces')[0])
for pieces in [[Fr(403,1000),Fr(212,1000),Fr(199,1000),Fr(186,1000)],
               [Fr(396,1000),Fr(212,1000),Fr(193,1000),Fr(176,1000),Fr(19,1000),Fr(4,1000)]]:
    k=len(pieces)-1
    r,tr=eval_trace(tuple(pieces),k,{})
    print("pieces=",[float(x) for x in pieces],"k=",k,"residual/u_k=",round(float(r/u(k)),4),"residual=",float(r))
    for mv in tr: print("   ",mv)
