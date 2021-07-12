'''
水平面上有 N 座大楼，每座大楼都是矩阵的形状

可以用一个三元组表示 (start, end, height)

分别代表其在x轴上的起点，终点和高度。

大楼之间从远处看可能会重叠，求出 N 座大楼的外轮廓线。

外轮廓线的表示方法为若干三元组，每个三元组包含三个数字 (start, end, height)，

代表这段轮廓的起始位置，终止位置和高度。

'''




from heapq import heappop, heappush
class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):
        # write your code here
        events = []
        for id, building in enumerate(buildings):
            events.append((building[0], True, building[2], id))
            events.append((building[1], False, building[2], id))
            
        events.sort()
        maxheap = []
        outline = []
        delset = set()
        
        for x, is_start, height, id in events:
            if is_start:
                heappush(maxheap, ((-height, x, id)))
            else:
                delset.add(id)
                
            while maxheap and maxheap[0][2] in delset:
                heappop(maxheap)
            
            if outline and outline[-1][0] == x:
                outline.pop()
                
            if not outline:
                outline.append((x, -maxheap[0][0]))
            elif maxheap and -maxheap[0][0] != outline[-1][1]:
                outline.append((x, -maxheap[0][0]))
            elif not maxheap:
                outline.append((x, 0))
        
        output = []    
        for i in range(len(outline) - 1):
            if outline[i][1] == 0:
                continue
            output.append([outline[i][0], outline[i + 1][0], outline[i][1]])
            
        return output