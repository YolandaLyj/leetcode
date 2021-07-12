import sys

N,V = sys.stdin.readline().strip().split(' ')
N,V = int(N), int(V)
value = list(map(int,sys.stdin.readline().strip().split(' ')))
if sum(value)<V: print('NO')
elif sum(value)==V: print('YES')
else:
    dp = [False for i in range(V+1)]
    dp[0] = True
    for i in range(N):
        for j in range(V,-1,-1):
            if j-value[i]>=0 and dp[j-value[i]]:
                dp[j] = True
    print('YES' if dp[V] else 'NO')

# 5 50
# 0 0 20 10 10