class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = 0
        temp = nums[0]
        
        for i in nums:
            if i == temp:
                count = count + 1

            else:
                count = count - 1
                if count == 0:
                    temp = i
                    count = 1

        return temp