def solve(T, K):
    l,r = 0,len(T)-1
    while l+1<r:
        m = (l+r)//2
        if T[m]>=K:
            r=m
        else:
            l=m
    return l if K==T[l] else r

print(solve([1,3,3,3,3,3,3,6,7],3))