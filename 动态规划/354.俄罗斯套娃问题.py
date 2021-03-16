from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        def find_longest_arr_2(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)

        def find_longest_arr(nums):
            res = [1 for i in range(len(nums))]
            for i in range(len(nums)):
                for j in range(i-1,-1,-1):
                    if nums[i]>nums[j]:
                        res[i] = max(res[i], 1+res[j])
            return max(res) if res else 0
        return find_longest_arr([i[1] for i in envelopes])
s = Solution()
print(s.maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]))