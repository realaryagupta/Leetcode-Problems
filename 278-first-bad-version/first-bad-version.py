# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid) == True:
                right = mid
            
            else:
                left = mid + 1
            
        return left
