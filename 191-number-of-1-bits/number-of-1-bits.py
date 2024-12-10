class Solution:
    def hammingWeight(self, n: int) -> int:

        n = bin(n)
        n = n[2:]

        n = str(n)        

        counter = 0
        for i in n:
            if i == "1":
                counter = counter + 1

        return counter