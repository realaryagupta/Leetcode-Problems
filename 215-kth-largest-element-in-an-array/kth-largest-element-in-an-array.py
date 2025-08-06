import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        if k <= 0 or k > len(nums):
            return None

        for num in nums:
            heapq.heappush(min_heap, num)

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]