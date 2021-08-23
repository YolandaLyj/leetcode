#!/usr/bin/env python  
# coding=utf-8  

t=[]  
s = input()

for x in s.split():  
    t.append(int(x))
n = t[0]
t.pop(0)
t.sort()
a,b,c = t
res = 0

for i in range(n//a,-1,-1):
    for j in range((n-i*a)//b,-1,-1):
        if (n-i*a+j*b)%c==0:
            pass
            # print(i+j+(n-i*a+j*b)//c)
            # exit()