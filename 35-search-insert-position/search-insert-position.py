class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        # here len(nums) - 1 is not done because if target is largest number then we need a place to add that last number
        right = len(nums)
        
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                right = mid

            else:
                left = mid + 1
        
        return left 