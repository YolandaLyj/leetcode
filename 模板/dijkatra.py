def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    g = [[] for _ in range(n)]
    for x,y,time in times:
        g[x-1].append((y-1, time))
    dist = [float('inf')]*n
    dist[k-1]=0
    q = [(0,k-1)]
    while q:
        time, x = heapq.heappop(q)
        if dist[x]<time: continue
        for y,time in g[x]:
            d = dist[x]+time
            if d<dist[y]:
                dist[y] = d
                heapq.heappush(q, (d,y))
    ans = max(dist)
    return ans if ans<float('inf') else -1

# 输入：【起始节点，终点节点，时间】，节点数量（1-n），起始节点
# 输出：遍历所有节点最长时间