class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        nums.sort(reverse = True)

        if len(nums) < 2:
            return 0 

        if len(nums) == 3:
            return sum(nums)

        for i in range(n-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]

        
        return 0