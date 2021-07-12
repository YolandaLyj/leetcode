# import sys
# a = sys.stdin.readline().strip()
# if a == '':
#     break
# print(1)

import bisect
data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
data.sort(key=lambda r: r[1])

a=[1,2,3,5,6,8,8,9,9,9,11,25,79]
a.reverse()
x = 26



# python
import sys
try: 
	while True:
		line = sys.stdin.readline().strip()
		if line == '':
			break 
		lines = line.split()
		print int(lines[0]) + int(lines[1])
except: 
	pass

# python3
import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))