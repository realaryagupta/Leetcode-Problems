class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(speed):
            total_hours = 0  
            for pile in piles:
                total_hours += (pile - 1) // speed + 1
                if total_hours > h:  
                    return False
            return total_hours <= h  

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left