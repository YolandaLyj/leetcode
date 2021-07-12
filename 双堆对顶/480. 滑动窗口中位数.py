# 困难：
# 想到维护两个平衡的堆
# 增加删减时候注意堆的平衡
import heapq
class Solution:
    def medianSlidingWindow(self, nums, k):
        min_heap, max_heap = [], []
        for i in range(k):
            heapq.heappush(min_heap, (nums[i], i))
        for i in range(k//2):
            n,idx = heapq.heappop(min_heap)
            heapq.heappush(max_heap, (-n, idx))
        res = [(min_heap[0][0]-max_heap[0][0])/2 if k % 2 == 0 else min_heap[0][0] * 1.0]
        for i in range(k, len(nums)):
            if nums[i] < min_heap[0][0]:
                # 放入大顶堆
                heapq.heappush(max_heap, (-nums[i],i))
                if nums[i-k] >= min_heap[0][0]:
                    # 如果移除的数在小顶堆，平衡两个堆
                    n, idx = heapq.heappop(max_heap)
                    heapq.heappush(min_heap, (-n, idx))
            else:
                # 放入小顶堆
                heapq.heappush(min_heap, (nums[i], i))
                if nums[i-k] <= min_heap[0][0]:
                    # 如果移除的数在大顶堆，平衡两个堆
                    n,idx = heapq.heappop(min_heap)
                    heapq.heappush(max_heap,(-n,idx))

            while min_heap and min_heap[0][1] <= i-k:
                heapq.heappop(min_heap)
            while max_heap and max_heap[0][1] <= i-k:
                heapq.heappop(max_heap)
            res.append((min_heap[0][0]-max_heap[0][0])/2 if k % 2 == 0 else min_heap[0][0] * 1.0)
            
        return res

