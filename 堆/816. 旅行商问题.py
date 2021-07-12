'''
给 n 个城市(从 1 到 n)，城市和无向道路成本之间的关系为3元组 [A, B, C]

（在城市 A 和城市 B 之间有一条路，成本是 C）

我们需要从1开始找到的旅行所有城市的付出最小的成本。
'''


import heapq 

class Solution:
    """
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """
    def minCost(self, n, roads):
        # Write your code here
        neighbors = {ii: [] for ii in range(1, n + 1)}
        for city1, city2, cost in roads:
            neighbors[city1].append((cost, city2))
            neighbors[city2].append((cost, city1))
        
        hq = [(0, 1, [1])]
        while hq:
            cost_sofar, city, visited = heapq.heappop(hq)
            if len(visited) == n:
                return cost_sofar
            for cost_delta, nbr_city in neighbors[city]:
                if nbr_city not in visited:
                    heapq.heappush(hq, (cost_sofar + cost_delta, nbr_city, visited + [nbr_city]))
        
        return -1