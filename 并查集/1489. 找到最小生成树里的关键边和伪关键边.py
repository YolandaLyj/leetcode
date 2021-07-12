'''
说句实在话,这题思路不难理解,就是有点不好实现,改错改了好久(面向调试编程真是痛苦)
这题主要要搞明白以下几点:
1.关键边:所有MST都有的共同边,这个比较好找
2.伪关键边:所有MST包含的边中除了关键边的边,(可不是题目中edges除了关键边的边)
3.'啥都不是边':MST中不可能会加入的边,就是说如果该边加入了,就无法构成MST

先利用克鲁斯卡尔做出一个MST,记录权重,以及构成该MST的边
    然后遍历每一条edges中的边,重新构建一棵MST,对于每一条边有三种情况:
        1.如果是原MST中的边,那么它一定是伪关键边或者关键边的一种,那么如何判断是哪一种呢?
                将其不加入新的MST,如果构成的新MST权重增加了,或者压根就没有连通所有的点,那么该边是关键边
                                如果构成的新的MST权重不增加,则说明该边是伪关键边
        2.如果不是原MST中的边,那么它只能是伪关键边或者'啥都不是边',那么如何判断是哪一种呢?
                将其第一个加入新的MST,如果最终形成的MST权重不增加,那么它就是伪关键边
                                    如果最终形成的MST权重增加了,他就是所谓的'啥都不是边'
'''
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
        self.n = n
        self.setCount = n
    
    def findset(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]
    
    def union(self,x, y):
        x, y = self.findset(x), self.findset(y)
        if x==y:
            return False
        if self.size[x] < self.size[y]:
            x,y = y,x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True
    
    def connected(x, y):
        x, y = self.findset(x), self.findset(y)
        return x==y

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        m = len(edges)
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda x:x[2])
        uf_std = UnionFind(n)
        value = 0
        for i in range(m):
            if uf_std.union(edges[i][0], edges[i][1]):
                value+=edges[i][2]
        
        ans = [list(), list()]
        for i in range(m):
            uf = UnionFind(n)
            v = 0
            for j in range(m):
                if i!=j and uf.union(edges[j][0], edges[j][1]):
                    v+=edges[j][2]
            if uf.setCount!=1 or (uf.setCount==1 and v>value):
                ans[0].append(edges[i][3])
                continue

            uf = UnionFind(n)
            uf.union(edges[i][0], edges[i][1])
            v = edges[i][2]
            for j in range(m):
                if i!=j and uf.union(edges[j][0], edges[j][1]):
                    v+=edges[j][2]
            if v==value:
                ans[1].append(edges[i][3])
        
        return ans
            