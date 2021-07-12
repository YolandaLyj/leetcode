'''
难点：
1、逆序思维
2、并查集
3、增加一个顶部虚拟节点(-1,-1)，顶部的砖块与(-1,-1)相连，父节点为(-1,-1)
'''


class UnionFind:
    def __init__(self):
        self.father = {}
        self.size_of_set = {}

    def get_size_of_set(self, x):
        return self.size_of_set[self.find(x)]

    def find(self, x):
        root = x
        while self.father[root]!=None:
            root = self.father[root]
        while x!=root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father
        return root
    
    def is_connected(self, x, y):
        return self.find(x)==self.find(y)
    
    def merge(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx!=rooty:
            self.father[rootx] = rooty
            self.size_of_set[rooty]+=self.size_of_set[rootx]
            del self.size_of_set[rootx]
    
    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.size_of_set[x] = 1


class Solution:
    def __init__(self):
        self.CEILING = (-1,1)
        self.DIRECTION = ((1,0), (-1,0), (0,1), (0,-1))

    def initialize(self, uf, m, n, grid, hits):
        uf.add(self.CEILING)

        for x,y in hits:
            grid[x][y] -= 1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    uf.add((i, j))
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    self.merge_neighbors(uf, m,n, grid, i, j)
        for j in range(n):
            if grid[0][j]==1:
                uf.merge((0,j), self.CEILING)

    def is_valid(self, x, y, grid, m, n):
        return 0<=x<m and 0<=y<n and grid[x][y]==1

    def merge_neighbors(self, uf, m,n, grid, x, y):
        for dx, dy in self.DIRECTION:
            nx, ny = x+dx, y+dy
            if not self.is_valid(nx, ny, grid, m, n):
                continue
            uf.merge((x,y), (nx, ny))

    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        uf = UnionFind()
        m, n = len(grid), len(grid[0])
        res = [0]*len(hits)

        self.initialize(uf, m, n, grid, hits)

        for i in range(len(hits)-1, -1, -1):
            x,y = hits[i][0], hits[i][1]
            grid[x][y]+=1
            if grid[x][y]!=1:
                continue
            after_hit = uf.get_size_of_set(self.CEILING)

            uf.add((x, y))
            self.merge_neighbors(uf, m, n, grid, x, y)
            if x==0:
                uf.merge((x,y), self.CEILING)
            
            if uf.is_connected((x,y), self.CEILING):
                before_hit = uf.get_size_of_set(self.CEILING)
                res[i] = before_hit - after_hit - 1
        return res