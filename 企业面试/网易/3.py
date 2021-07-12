import sys
M = sys.stdin.readline().strip()
N = sys.stdin.readline().strip()
dp=[[-1 for _ in range(len(N)+1)] for _ in range(len(M)+1)]
dp[0][0]=0
for j in range(1,len(N)+1):
    dp[0][j] = j
for i in range(1, len(M)+1):
    dp[i][0] = i
for i in range(1,len(M)+1):
    for j in range(1,len(N)+1):
        if M[i-1]==N[j-1]:
            dp[i][j]=dp[i-1][j-1]
        else:
            try:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
            except:
                print(1)

res = float(len(M)+len(N)-dp[len(M)][len(N)])/float(len(M)+len(N))
print('%.2f'%res)