#!/usr/bin/env python  
# coding=utf-8  
n = int(input())
s = input()
res = []
if n==1: 
    print(1)
    exit()
d = {'0':0, '1':0}
all_d = {}
def f(p,q):
    _f_res = 1
    if p>q: small = q
    else: small = p
    for i in range(1, small+1):
        if (p%i==0) and (q%i==0):
            _f_res = i
    return _f_res

def find(a,b,begin,end):
    if begin>end: return 0
    _f_res = 1
    for i in range(begin, end+1):
        if begin>0:
            _d0,_d1 = all_d[i]['0']-all_d[begin-1]['0'],all_d[i]['1']-all_d[begin-1]['1']
        else:
            _d0,_d1 = all_d[i]['0'], all_d[i]['1']
        if _d0!=0 and _d1!=0 and a*_d1==b*_d0:
            _f_res += find(a,b,i+1, end)
            break
    return _f_res


for i in range(len(s)):
    d[s[i]]+=1
    all_d[i] = {'0':d['0'], '1':d['1']}
    if d['0']==0 or d['1']==0:
        temp_res = 1
        m = d['0'] if d['0']!=0 else d['1']
        res.append(m)
    else:
        maxgongyueshu = f(d['0'],d['1'])
        if maxgongyueshu==1:
            res.append(1)
        else:
            res.append(find(d['0'],d['1'],0,i))
print(' '.join(map(str,res)))
