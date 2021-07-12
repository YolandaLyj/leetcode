import sys
from decimal import *
def gen(x, iter):
    x0 = pow(x, 1/3)
    for _  in range(1000*iter):
        x0 = x0+(x/x0**2 - x0)*(1/3)
    return x0

n = int(sys.stdin.readline().strip())
getcontext().prec = 30
for _ in range(n):
    l,r,k = sys.stdin.readline().strip().split()
    l,r,k = int(l), int(r), int(k)
    # res = 0
    # for i in range(l, r+1):
    #     res+= gen(i+pow(10,-k), 2*k)-gen(i,2*k)
    # print("%.5E"%res)
    re = Decimal(0)
    for i in range(l, r+1):
        re += Decimal((i+Decimal(10**(-1*k)))**Decimal(1/3))-Decimal(i**Decimal(1/3))
    re = "%.5E"%re
    re = list(re)
    l_index = re.index('-')
    if len(re[l_index+1:])<3:
        re = re[:l_index+1]+['0']*(3-len(re[l_index+1:]))+re[l_index+1:]
    print(''.join(re))