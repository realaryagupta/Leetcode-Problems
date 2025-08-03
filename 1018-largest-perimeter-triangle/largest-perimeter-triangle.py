class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)

        lar = 0

        for i in range(len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                lar = max(lar, (nums[i] + nums[i+1] + nums[i+2]))
            
        return lar