'''
给定一个整数数组，找出两个不重叠的子数组A和B，使两个子数组和的差的绝对值|SUM(A) - SUM(B)|最大。

返回这个最大的差值。

子数组最少包含一个数
'''

class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        if not nums:
            return 0
        n = len(nums)
        left_max, left_min, right_max, right_min = [0] * n, [0] * n, [0] * n, [0] * n
        left_min[0], left_max[0], right_min[-1], right_max[-1] = nums[0], nums[0], nums[-1], nums[-1]
        cur_min, cur_max = nums[0], nums[0]
        for i in range(1, n):
            cur_min = min(nums[i], cur_min + nums[i])
            left_min[i] = min(left_min[i - 1], cur_min)
            
            cur_max = max(nums[i], cur_max + nums[i])
            left_max[i] = max(left_max[i - 1], cur_max)
        cur_min, cur_max = nums[-1], nums[-1]
        for i in range(n - 2, -1, -1):
            cur_min = min(nums[i], cur_min + nums[i])
            right_min[i] = min(right_min[i + 1], cur_min)
            
            cur_max = max(nums[i], cur_max + nums[i])
            right_max[i] = max(right_max[i + 1], cur_max)
        ans = float('-inf')
        for i in range(n - 1):
            v = max(abs(left_max[i] - right_min[i + 1]), abs(left_min[i] - right_max[i + 1]))
            ans = max(ans, v)
        return ans