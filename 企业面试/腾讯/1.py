import sys
if __name__ == "__main__":
    n,m = list(map(int,sys.stdin.readline().strip().split()))
    f=[]
    for k in range(n):
        f.append(list(map(int,sys.stdin.readline().strip().split())))
    dp = [[[] for i in range(n)]for j in range(m)]
    dp[0][0]=[f[0][0],f[0][0]]
    for j in range(1,n):
        dp[0][j]=[dp[0][j-1][0]*f[0][j],dp[0][j-1][1]*f[0][j]]
    for i in range(1,n):
        dp[i][0]=[dp[i-1][0][0]*f[i][0],dp[i-1][0][1]*f[i][0]]
    for i in range(1,n):
        for j in range(1,m):
            maxx=max(dp[i][j - 1][0] * f[i][j],dp[i][j - 1][1] * f[i][j],dp[i - 1][j][0] * f[i][j],dp[i - 1][j][1] * f[i][j])
            minn=min(dp[i][j - 1][0] * f[i][j],dp[i][j - 1][1] * f[i][j],dp[i - 1][j][0] * f[i][j],dp[i - 1][j][1] * f[i][j])
            dp[i][j]=[maxx,minn]
    result=max(dp[-1][-1])
    if result < 0:
        print(-1)
    else:
        print(result % 10 ** 9 + 7)
    