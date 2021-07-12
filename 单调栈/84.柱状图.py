'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
'''
class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        left, right = [0]*n, [n]*n
        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]]>=heights[i]:
                right[mono_stack[-1]]=i
                mono_stack.pop()
            left[i]=mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)
        ans = max((right[i]-left[i]-1)*heights[i] for i in range(n)) if n>0 else 0
        return ans