class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        currsum = 0

        for number in nums:
            if currsum < 0:
                currsum = 0
            
            currsum = currsum + number
            maxsub = max(currsum, maxsub)

        return maxsub