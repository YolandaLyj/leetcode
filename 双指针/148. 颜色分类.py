'''
给定一个包含红，白，蓝且长度为 n 的数组，将数组元素进行分类使相同颜色的元素相邻，

并按照红、白、蓝的顺序进行排序。

我们可以使用整数 0，1 和 2 分别代表红，白，蓝。
'''


'''
使用一次扫描的办法。
设立三根指针，left, index, right。定义如下规则：

left 的左侧都是 0（不含 left）
right 的右侧都是 2（不含 right）
index 从左到右扫描每个数，如果碰到 0 就丢给 left，碰到 2 就丢给 right。碰到 1 就跳过不管。
'''



class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, A):
        left, index, right = 0, 0, len(A) - 1
        # be careful, index < right is not correct
        while index <= right:
            if A[index] == 0:
                A[left], A[index] = A[index], A[left]
                left += 1
                index += 1 # move to next number
            elif A[index] == 2:
                A[right], A[index] = A[index], A[right]
                right -= 1
            else:  # == 1, skip
                index += 1