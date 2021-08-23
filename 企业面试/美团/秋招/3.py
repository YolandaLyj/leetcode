#!/usr/bin/env python  
# coding=utf-8  
s = list(input())
dp={i:{} for i in range(len(s))}

for i in range(len(s)-1):
    if s[i]=='(' and s[i+1]==')': dp[i][i+1]=2
for l in range(4, len(s)+1, 2):
    for begin in range(len(s)):
        if begin+l>len(s): break
        end = begin+l-1
        if s[begin]=='(' and s[end]==')' and end-1 in dp[begin+1]:
            dp[begin][end] = 1+dp[begin+1][end-1]
        else:
            if s[begin]==')' or s[end]=='(': continue
            for index in dp[begin]:
            # for index in range(begin+1, end-2+1):
                if index in dp[begin] and end in dp[index+1]:
                    dp[begin][end] = (dp[begin][index] * dp[index+1][end])%1000000007
                    break
print(dp[0][len(s)-1]%1000000007)
        