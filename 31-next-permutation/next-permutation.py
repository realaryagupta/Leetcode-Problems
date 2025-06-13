class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i == -1:
            nums.reverse()
            return
        
        j = len(nums) - 1

        # Find the first number greater than nums[i] from the end
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        nums[i], nums[j] = nums[j], nums[i]

        # Reverse the suffix
        nums[i+1:] = reversed(nums[i+1:])