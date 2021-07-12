'''
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。

请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。

如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[[0] *(n+1) for _ in range(m+1)] for _ in range(len(strs) + 1)]
        for i in range(1, len(strs) + 1):
            ones = strs[i-1].count("1")
            zeros = strs[i-1].count("0")
            for j in range(m+1):
                for k in range(n+1):
                    dp[i][j][k] = dp[i-1][j][k]
                    if j >= zeros and k >= ones and dp[i][j][k] < dp[i-1][j-zeros][k - ones] + 1:
                        dp[i][j][k] = dp[i-1][j-zeros][k - ones] + 1
        return dp[-1][-1][-1]
