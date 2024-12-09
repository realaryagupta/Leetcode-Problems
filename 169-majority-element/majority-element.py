class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_count = {}

        # Count occurrences of each number
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        # Check if any number occurs more than n / 2 times
        for num in num_count:
            if num_count[num] > len(nums) / 2:
                return num