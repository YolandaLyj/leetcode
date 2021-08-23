#!/usr/bin/env python  
# coding=utf-8  

nums=[]  
n = int(input())
s = input()

for x in s.split():  
    nums.append(int(x))
nums.sort()
res = []
used = [False for _ in range(len(nums))]
def dfs(cur,used):
    if len(cur)==n: 
        res.append(cur)
    else:
        cur_used = set()
        for i,v in enumerate(used):
            if v==True: continue
            if nums[i] in cur_used: continue
            cur_used.add(nums[i])
            used[i] = True
            dfs(cur+[nums[i]],used)
            used[i] = False
dfs([],used)
print(len(res))
for i in res:
    print(' '.join(map(str,i)))