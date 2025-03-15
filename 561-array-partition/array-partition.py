class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        n = len(nums)

        nums.sort()

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[i]

        for i in range(0,n,2):
            counter = nums[i] + counter
        
        return counter