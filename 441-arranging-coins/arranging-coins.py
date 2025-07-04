import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0

        for i in range(1, n+1):
            n = n - i

            if n >= 0:
                count += 1

            elif n < 0:
                break

        return count
