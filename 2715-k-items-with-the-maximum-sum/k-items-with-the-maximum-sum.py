class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:

        ones_taken = min(numOnes, k)
        k -= ones_taken

        zeros_taken = min(numZeros, k)
        k -= zeros_taken

        neg_ones_taken = min(numNegOnes, k)

        return ones_taken - neg_ones_taken
