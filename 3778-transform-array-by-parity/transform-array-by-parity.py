class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        count_even = 0

        for i in nums:
            if i % 2 == 0:
                count_even = count_even + 1
                

        count_odd = n - count_even
        total = count_even + count_odd

        arr = [0] * count_even

        # dont use append use extend instead
        arr.extend([1] * count_odd)

        return arr