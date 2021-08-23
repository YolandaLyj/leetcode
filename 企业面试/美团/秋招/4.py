#!/usr/bin/env python  
# coding=utf-8
n = int(input())
temp = input().split()
nums = [int(x) for x in temp]
_n = int(input())

sum_list = [0 for _ in range(n)]
for i,num in enumerate(nums):
    if i==0: sum_list[0] = num
    else:
        sum_list[i] = sum_list[i-1]+num

for _ in range(_n):
    ops, l, r = input().split()
    l,r = int(l)-1, int(r)-1
    if ops == '1':
        if l-1>=0:
            print(sum_list[r]-sum_list[l-1])
        else:
            print(sum_list[r])
    elif ops == '2':
        res = 0
        if l-1>=0:
            _sum = sum_list[r]-sum_list[l-1]
        else:
            _sum = sum_list[r]

        for num in nums[l:r+1]:
            res+= (_sum-num)**2
        print(res)
    elif ops=='3':
        print(max(nums[l:r+1]))
