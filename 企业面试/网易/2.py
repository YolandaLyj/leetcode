import sys
N = int(sys.stdin.readline().strip())
nums = []
for _ in range(N):
    nums.append(list(map(int,sys.stdin.readline().strip().split(' '))))
source = []
for i in range(N):
    for j in range(N):
        if nums[i][j]==1:
            source.append([i,j])
if len(source)==0:
    print(0)
elif len(source)==N*N:
    print(0)
else:
    dis = []
    for i in range(N):
        for j in range(N):
            if nums[i][j]!=1:
                temp_res = float('inf')
                for _s in source:
                    temp_res = min(temp_res,abs(i-_s[0])+abs(j-_s[1]))
                dis.append([j,i,temp_res])
            else:
                dis.append([j,i,0])
    dis.sort(key=lambda r: r[1])
    dis.sort(key=lambda r: r[0])
    dis.sort(key=lambda r: r[2], reverse=True)
    for i in range(len(dis)):
        if dis[i][2]!=dis[0][2]:
            break
    temp_res = [str(line[0])+' '+str(line[1]) for line in dis[:i]]
    print(' '.join(temp_res))