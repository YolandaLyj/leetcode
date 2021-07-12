import sys
n, k = sys.stdin.readline().strip().split()
n, k = int(n), k

def f(x, k):
    res = ''
    yinzi = [0 for i in range(x+1)]
    for i in range(1, int((x+1)/2)):
        if yinzi[i]!=0: continue
        if x%i==0:
            yinzi[x//i] = 1
            yinzi[i] = 1
    for i in range(len(yinzi)):
        if yinzi[i]:
            res+=str(i)
    print(res)
    if k in res:
    #if k in res[-2*len(k):]:
        return False
    return True

nums = sys.stdin.readline().strip().split()
finalres = 0
for _num in nums:
    if not f(int(_num), k):
        finalres+=1
print(finalres)