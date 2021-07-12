import sys
n = int(sys.stdin.readline().strip())
for _ in range(n):
    n,k = sys.stdin.readline().strip().split()
    n,k = int(n), int(k)
    dp = [[0 for _ in range(2)] for _ in range(n+1)]
    dp[0][0] = 1
    dp[0][1] = 1
    dp[1][0] = k
    dp[1][1] = 0
    dp[2][0] = k*(k-1)
    dp[2][1] = k
    for i in range(3,n+1):
        # dp[i][1] = k*dp[i-2][0]+(k-1)*dp[i-2][1]
        dp[i][1] = (k-1)*(dp[i-2][0]+dp[i-2][1])
        dp[i][0] = (k-1)*(dp[i-1][0]+dp[i-1][1])
    print(dp[-1][1]+dp[-1][0])