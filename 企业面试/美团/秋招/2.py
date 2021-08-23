#!/usr/bin/env python  
# coding=utf-8  

s = list(input())
n = int(input())
s_index = {}

# def insert(K, T):
#     if K>T[-1]: return len(T)
#     if len(T)<=1: return -1
#     l,r = 0,len(T)-1
#     while l+1<r:
#         m = int((l+r)/2)
#         if T[m]>K:
#             r=m
#         else:
#             l=m
#     return l if K<=T[l] else r

def search(K, T):
    if len(T)<=1: return -1
    l,r = 0,len(T)-1
    while l+1<r:
        m = int((l+r)/2)
        if T[m]>K:
            r=m
        else:
            l=m
    index = l if K==T[l] else r
    if index==0:
        return abs(T[1]-T[0])
    elif index==len(T)-1:
        return abs(T[index]-T[index-1])
    return min(abs(T[index]-T[index-1]), abs(T[index]-T[index+1]))

for i in range(len(s)):
    if s[i] not in s_index: s_index[s[i]] = []
    s_index[s[i]].append(i+1)
for _ in range(n):
    nums = input().split()
    if nums[0]=='2':
        print(search(int(nums[1]),s_index[s[int(nums[1])-1]]))
    elif nums[0]=='1':
        if nums[1] not in s_index: s_index[nums[1]] = []
        s.append(nums[1])
        s_index[nums[1]].append(len(s))
