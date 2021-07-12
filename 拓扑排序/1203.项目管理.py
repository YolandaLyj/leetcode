#!usr/bin/env python
# _*_ coding:utf8 _*_
'''
难点：
1、拓扑排序存两个值，后向节点列表，前向度
'''
import collections
class Solution:
    def t_sort(self, items, indegree, neighbors):
        queue = collections.deque()
        res = []
        for item in items:
            if not indegree[item]:
                queue.append(item)
        if not queue: return []
        while queue:
            cur = queue.popleft()
            res.append(cur)

            for neighbor in neighbors[cur]:
                indegree[neighbor]-=1
                if not indegree[neighbor]:
                    queue.append(neighbor)
        return res
        
    def sortItems(self, n, m, group, beforeItems):
        max_group_id = m
        for task in range(n):
            if group[task]==-1:
                group[task] = max_group_id
                max_group_id+=1
        task_indegree = [0 for i in range(n)]
        group_indegree = [0 for i in range(max_group_id)]
        task_neighbors = [[] for _ in range(n)]
        group_neighbors = [[] for _ in range(max_group_id)]
        group_to_tasks = [[] for i in range(max_group_id)]
        for task in range(n):
            group_to_tasks[group[task]].append(task)
            for pre in beforeItems[task]:
                if group[pre]==group[task]:
                    task_indegree[task]+=1
                    task_neighbors[pre].append(task)
                else:
                    group_indegree[group[task]]+=1
                    group_neighbors[group[pre]].append(group[task])
        res = []
        group_queue = self.t_sort([i for i in range(max_group_id)], group_indegree, group_neighbors)
        if len(group_queue)!=max_group_id: return []
        for group_id in group_queue:
            task_queue = self.t_sort(group_to_tasks[group_id], task_indegree, task_neighbors)
            if len(task_queue)!=len(group_to_tasks[group_id]):
                return []
            res += task_queue
        return res

s = Solution()
print(s.sortItems(8,2,[-1,-1,1,0,0,1,0,-1],[[],[6],[5],[6],[3,6],[],[],[]]))