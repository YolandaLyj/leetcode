import sys
import functools
@functools.lru_cache()
def dfs(i,j):
    res = 0
    if j-i==0: return 0
    for loc in range(i,j):
        left_value = pre[loc]-pre[i]+value[i]
        right_value = pre[j]-pre[loc]
        if left_value>right_value:
            res = max(res, 2*right_value-dfs(loc+1, j))
        elif left_value<right_value:
            res = max(res, 2*left_value-dfs(i,loc))
        else:
            res = max(res, 2*left_value-dfs(i,loc), 2*right_value-dfs(loc+1, j))
    return res
    
N = int(sys.stdin.readline().strip())
value = list(map(int,sys.stdin.readline().strip().split(' ')))
pre = [0 for i in range(len(value)+1)]
n=0
for i in range(len(value)):
    n+=value[i]
    pre[i]+=n
print(dfs(0,len(value)-1))