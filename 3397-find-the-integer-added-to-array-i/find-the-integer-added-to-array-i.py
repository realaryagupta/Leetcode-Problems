class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        
        nums1.sort()
        nums2.sort()

        x = nums2[-1] - nums1[-1]
        
        return x