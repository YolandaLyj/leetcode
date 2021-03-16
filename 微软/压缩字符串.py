import json

def func(s, k):
    def del_str(j):
        n=0
        x,y = sorted_m[j][1],sorted_m[j][1]-1
        if len(str(x))>len(str(y)) or y==1 or y==0: n-=1
        sorted_m[j][1]=-1
        return n

    def add_str(j):
        n=0
        x,y = sorted_m[j][1],sorted_m[j][1]+1
        if len(str(x))<len(str(y)) or y==2 or y==1: n+=1
        sorted_m[j][1]=+1
        return n
        
    m = [-1 for i in range(len(s))]
    sorted_m, sorted_m_len = [], 0
    for i in range(len(s)):
        if i!=0 and s[i]==s[i-1]:
            m[i] = len(sorted_m)-1
            a,b = sorted_m[-1]
            sorted_m[-1] = [a, b+1]
            if int(str(b)) > int(str(b+1)) or sorted_m[-1][1]==2:
                sorted_m_len+=1
        else:
            m[i] = len(sorted_m)
            sorted_m.append([s[i],1])
            sorted_m_len+=1

    res, cur = sorted_m_len, sorted_m_len
    for i in range(len(s)-2):
        if i==0: cur += del_str(m[i])+del_str(m[i+1])+del_str(m[i+2])
        else: cur += del_str(m[i+2])+add_str(m[i-1])
        res = min(res, cur)
    return res

print(func('aaabbbcdr',3))