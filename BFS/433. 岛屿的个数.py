'''
给一个 01 矩阵，求不同的岛屿的个数。

0 代表海，1 代表岛，如果两个 1 相邻，那么这两个 1 属于同一个岛。我们只考虑上下左右为相邻。
'''
from collections import deque

class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
            
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
                    
        return islands                    
    
    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.is_valid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))

    def is_valid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in visited:
            return False
        return grid[x][y]