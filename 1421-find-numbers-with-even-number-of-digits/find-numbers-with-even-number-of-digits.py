class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        if len(nums) == 0:
            return 0

        for i in nums:
            test = 0
            while i > 0:
                test = test + 1
                i = i // 10
            
            if (test % 2) == 0:
                count = count + 1

        return  count