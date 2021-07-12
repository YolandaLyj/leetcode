'''
给定 n 本书, 每本书具有相同的页数. 现在有 k 个人来复印这些书. 

其中第 i 个人需要 times[i] 分钟来复印一本书. 每个人可以复印任意数量的书. 

怎样分配这 k 个人的任务, 使得这 n 本书能够被尽快复印完?

返回完成复印任务最少需要的分钟数.
'''


class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copyBooksII(self, n, times):
        l = 1 
        r = min(times) * n 
        while l < r:
            mid = (l + r) // 2
            if self.ok(n, times, mid):
                r = mid 
            else:
                l = mid + 1 
        return l 
    
    def ok(self, n, times, tm):
        num = 0
        for i in times:
            num += tm // i
        return n <= num
