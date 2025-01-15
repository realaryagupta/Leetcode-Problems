class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg_counter = 0
        pos_counter = 0

        for i in nums:
            if i < 0:
                neg_counter += 1
            elif i > 0:
                pos_counter += 1

        return max(neg_counter, pos_counter)