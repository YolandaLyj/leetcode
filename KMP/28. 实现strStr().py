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



s = Solution()
print(s.strStr('ABABABABC', 'ABABC'))

s = KMP()
print(s.strStr('ABABABABC', 'ABABC'))