import sys
n,m = sys.stdin.readline().strip().split()
n, m=int(n), int(m)
res = {}
finalres = []
def dfs(last_loc, begin_index, end_index, l):
    for i in range(len(res[begin_index])):
        temp = abs(res[begin_index][i][0]-last_loc[0])+abs(res[begin_index][i][1]-last_loc[1])
        if begin_index==end_index: finalres.append(l+temp)
        else:
            dfs(res[begin_index][i], begin_index+1, end_index, l+temp)

for i in range(int(n)):
    nums = sys.stdin.readline().strip().split()
    nums = list(map(int, nums))
    for j in range(len(nums)):
        if nums[j] not in res:
            res[nums[j]]=[]
        res[nums[j]].append((i,j))
for i in range(1,m+1):
    if i not in res:
        print(-1)
        exit()
for i in range(len(res[1])):
    if 1==m: finalres.append(0)
    else:
        dfs(res[1][i], 1, m, 0)
print(min(finalres))


# 4 4
# 1 2 2 1
# 2 4 4 1
# 4 4 4 2
# 1 1 1 2