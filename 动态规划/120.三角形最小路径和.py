class Solution:
    def minimumTotal(self, triangle):
        pre = [0 for _ in range(len(triangle[-1]))]
        temp = [0 for _ in range(len(triangle[-1]))]
        pre[0] = triangle[0][0]
        temp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            temp[0] = pre[0]+triangle[i][0]
            for j in range(1,len(triangle[i])-1):
                temp[j] = min(pre[j], pre[j-1])
                temp[j] += triangle[i][j]
            temp[len(triangle[i])-1] = pre[len(triangle[i])-2]+triangle[i][len(triangle[i])-1]
            for j in range(0, len(triangle[i])):
                pre[j] = temp[j]
        return min(pre[:len(triangle)])

s = Solution()
print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))