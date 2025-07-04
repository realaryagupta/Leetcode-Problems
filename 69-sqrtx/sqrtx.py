class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        
        left = 0
        right = x

        while left < right:
            mid = left + (right-left) // 2
            if mid * mid >= x:
                right = mid

            else:
                left = mid + 1
            
        if left * left == x:
            return left
        else:
            return left - 1
