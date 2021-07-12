#!usr/bin/env python
# _*_ coding:utf8 _*_

'''
难点：
1、题目联想并查集
'''

class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(range(n+1))

        def find(index):
            if parent[index]!=index:
                parent[index] = find(parent[index])
            return parent[index]
        def union(index1, index2):
            parent[find(index2)] = find(index1)
        
        for node1, node2 in edges:
            if find(node1)!=find(node2):
                union(node1, node2)
            else:
                return [node1, node2]
        return []