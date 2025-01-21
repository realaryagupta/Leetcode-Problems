class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0

        if len(nums) == 1:
            return result

        else:

            for i in range(len(nums)-1):
                if nums[i] >= nums[i+1]:
                    result += ( nums[i] - nums[i+1] ) + 1
                    nums[i+1] +=  ( nums[i] - nums[i+1] ) + 1
                    
        return result