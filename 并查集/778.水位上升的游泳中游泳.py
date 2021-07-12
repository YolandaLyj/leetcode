#难点：
#1、想到并查集
#2、实现并查集，构建数组idx
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, x):
        if x!=self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root!=y_root:
            self.parent[x_root] = y_root
    def connect(self,x,y):
        return self.find(x)==self.find(y)

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n = len(grid)
        idx = [0]*(n*n)
        for i in range(n):
            for j in range(n):
                idx[grid[i][j]] = (i, j)
        uf = UnionFind(n*n)
        for t in range(n*n):
            x,y = idx[t]
            for dx, dy in directions:
                nx = x+dx
                ny = y+dy
                if 0<=nx<n and 0<=ny<n and grid[nx][ny]<=t:
                    uf.union(x * n + y, nx * n + ny)
            if uf.connect(0, n*n-1):
                return t
        return -1