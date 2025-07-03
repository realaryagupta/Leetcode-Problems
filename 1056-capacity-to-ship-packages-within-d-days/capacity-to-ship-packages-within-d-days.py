from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            our_days = 1
            total = 0

            for weight in weights:
                total += weight

                if total > capacity:
                    our_days += 1       # increment days by 1 (not days + 1)
                    total = weight      # start new day with current weight

                    if our_days > days:  # if days exceed allowed days, return False
                        return False

            return True  # all weights shipped within allowed days

        left = max(weights)  # minimum capacity must be at least the heaviest package
        right = sum(weights) # maximum capacity could be sum of all weights

        while left < right:
            mid = left + (right - left) // 2

            if feasible(mid):
                right = mid  # try smaller capacity
            else:
                left = mid + 1  # increase capacity

        return left
