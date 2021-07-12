import sys
# try: 
# 	while True:
# 		line = sys.stdin.readline().strip()
# 		if line == '':
# 			break 
# 		lines = line.split()
# 		print int(lines[0]) + int(lines[1])
# except: 
# 	pass

N = int(sys.stdin.readline().strip())
nums = list(map(int,sys.stdin.readline().strip().split(' ')))

res_dict = {a:0 for a in nums}
nums.sort()
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1, N):
            if nums[i]+nums[j]>nums[k]:
                res_dict[nums[i]]+=1
                res_dict[nums[j]]+=1
                res_dict[nums[k]]+=1
            elif nums[i]+nums[j]<=nums[k]:
                break
res_dict = list(res_dict.items())
res_dict.sort(key=lambda r: r[1], reverse=True)
print(res_dict)
res = []
for line in res_dict:
    if line[1]==res_dict[0][1]:
        res.append(line[0])
    else:
        break
res.sort()
print(' '.join(map(str,res)))