class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        arr = []

        for i in range(0,32):
            a = 2 ** i 
            arr.append(a)

        for i in arr:
            if n == i:
                return True
            
        return False