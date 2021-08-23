import sys
s = sys.stdin.readline().strip()
res = [0 for _ in range(len(s)+1)]
loc = {}
for i in range(len(s)):
    if s[i] not in loc: loc[s[i]]=[]
    loc[s[i]].append(i)
tres = 0
for i in range(len(s)):
    temp = tres+1
    for j in loc[s[i]]:
    #for j in range(0,i):
        if j<i and s[j]==s[i]:
            temp-=res[j]
    res[i]=temp
    tres+=res[i]
print((tres+1)%20210101)