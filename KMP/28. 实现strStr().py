class KMP:
    def kmp(self, pat):
        m = len(pat)
        dp = [[0]*256]
        dp[0][ord(pat[0])] = 1
        X = 0
        for i in range(1, m):
            if len(dp)<i+1: dp.append([])
            for j in range(256):
                if len(dp[i]) >= j+1:
                    dp[i][j] = dp[X][j]
                else:
                    dp[i].append(dp[X][j])
            dp[i][ord(pat[i])] = i+1
            X=dp[X][ord(pat[i])]
        return dp

    def strStr(self, haystack, needle):
        m = len(needle)
        n = len(haystack)
        if m==0: return 0
        dp = self.kmp(needle)
        j = 0
        for i in range(n):
            j = dp[j][ord(haystack[i])]
            if j==m: return i-m+1
        return -1



class Solution:
    def maximumProduct(self, nums):
        if len(nums)==3: return nums[0]*nums[1]*nums[2]
        min1, min2, max1, max2, max3 = float('inf'), float('inf'), float('-inf'), float('-inf'), float('-inf')
        for a in nums:
            if a<min1:
                min1, min2 = a, min1
            elif a<min2:
                min2 = a
            if a>max3:
                max3, max2, max1 = a, max3, max2
            elif a>max2:
                max2, max1=a, max2
            elif a>max1:
                max1 = a
        return min1*min2*max3 if min1*min2*max3 > max1*max2*max3 else max1*max2*max3



s = Solution()
print(s.maximumProduct([-100,-98,-1,2,3,4]))

# s = KMP()
# print(s.strStr('ABABABABC', 'ABABC'))