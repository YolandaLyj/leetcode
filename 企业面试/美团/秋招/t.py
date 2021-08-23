def solve(T, K):
    if K>T[-1]: return len(T)
    l,r = 0,len(T)-1
    while l+1<r:
        m = int((l+r)/2)
        if T[m]>K:
            r=m
        else:
            l=m
    return l if K<=T[l] else r

print(solve([1,1,3,7,8,9],10))

a=[1,1,3,7,8,9]
a.insert(6, 10)
print(a)
