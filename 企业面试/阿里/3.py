def func(nums):
    dp = [[0,0] for i in range(len(nums))]
    res = 0
    if nums[0]=='1':
        dp[0][0] = 1
        dp[0][1] = 0
    else:
        dp[0][0] = 0
        dp[0][1] = 0
    for i in range(1,len(nums)):
        if nums[i]=='1':
            dp[i][0] = dp[i-1][0]+1
            dp[i][1] = dp[i-1][1]+1
        else:
            dp[i][0] = 0
            dp[i][1] = dp[i-1][0]+1
        res = max(res, dp[i][1])
    return res

print(func(['0']))