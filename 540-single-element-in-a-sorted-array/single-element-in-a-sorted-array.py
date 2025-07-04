class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        total = sum(nums)
        a = set(nums)

        ans = abs(total - (2 * sum(a)))
        return ans