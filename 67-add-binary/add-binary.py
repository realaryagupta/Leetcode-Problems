class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # convert to decimal
        a = int(a,2)
        b = int(b,2)

        # convert sum to binary
        sum = bin(a + b)

        # the output will contain '0b' prefix so removing them 
        sum = sum[2:]
        
        return sum