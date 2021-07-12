import sys
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
value = list(map(int,sys.stdin.readline().strip().split(' ')))
dp = [False for i in range(sum(value)+5)]
dp[0] = True
for i in range(len(value)):
    for j in range(sum(value),-1,-1):
        try:
            if j-value[i]>=0 and dp[j-value[i]]:
                dp[j] = True
        except:
            print(1)
for i in range(N, sum(value)+1):
    if dp[i]==True:
        print(i-M)
        break