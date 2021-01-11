#!usr/bin/env python
# _*_ coding:utf8 _*_
from collections import defaultdict
class bingchaji:
    def __init__(self, n):
        self.n = n
        self.f = list(range(n))
    def find(self, i):
        try:
            if self.f[i]==i:
                return i
            else:
                self.f[i] = self.find(self.f[i])
                return self.f[i]
        except:
            print(1)
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx==fy:
            return
        self.f[fx] = fy
class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        bcj = bingchaji(len(s))
        for (x,y) in pairs:
            bcj.union(x, y)
        mp = defaultdict(list)
        for i in range(len(s)):
            mp[bcj.find(i)].append(s[i])
        for vec in mp.values():
            vec.sort(reverse=False)
        ans = []
        for i in range(len(s)):
            x = bcj.find(i)
            ans.append(mp[x][0])
            mp[x].pop(0)
        return ''.join(ans)

if __name__ == '__main__':
    s = Solution()
    print(s.smallestStringWithSwaps('dcab', [[0,3],[1,2],[0,2]]))