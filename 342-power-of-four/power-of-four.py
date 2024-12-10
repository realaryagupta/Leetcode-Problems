class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        pwr_of_4 = []

        for i in range(32):
            num = 4 ** i
            pwr_of_4.append(num)
        
        if n in pwr_of_4:
            return True
        else:
            return False