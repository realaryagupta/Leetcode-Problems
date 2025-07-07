from typing import List

class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        arr = []

        for i in nums:
            if i % 2 == 0:
                arr.append(0)

            elif i % 2 != 0:
                arr.append(1)

        arr.sort()
        return arr