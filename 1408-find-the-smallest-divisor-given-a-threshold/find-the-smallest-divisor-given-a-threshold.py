import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def count_div(index):
            count = 0
            for i in nums:
                count = count + math.ceil(i/index)
            
            return count

        left = 1
        right = max(nums)

        while left < right:
            mid = (left + right) // 2
            if count_div(mid) <= threshold:
                right = mid
            
            else:
                left = mid + 1
            
        return left