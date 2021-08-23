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



#!/usr/bin/env python  
# coding=utf-8  
# Python使用的是3.4.3，缩进可以使用tab、4个空格或2个空格，但是只能任选其中一种，不能多种混用
while 1:
    a=[]  
    s = input()

    if s != "":
        for x in s.split():  
            a.append(int(x))  

        print(sum(a))
    else:
        break