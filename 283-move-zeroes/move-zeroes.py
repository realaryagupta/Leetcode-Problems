class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_ptr = 0

        for non_zero in range(len(nums)):
            if nums[non_zero] != 0:
                
                # swap
                nums[zero_ptr], nums[non_zero] = nums[non_zero], nums[zero_ptr]

                zero_ptr = zero_ptr + 1