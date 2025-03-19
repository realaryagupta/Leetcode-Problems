class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        # any number to power 0 is 1
        if n == 0:
            return 1 

        # if number is negative then make it positive and change power 
        if n < 0:
            x = 1 / x
            n = -n
        
        ans = 1

        while n:

            # is n is odd then we need to multiply ans by the x so that later we can calculate the square of half the power
            # this is done to reduce the time complexity from n to nlogn because we halved the computaitons
            if n % 2:
                ans = (ans * x)
            
            x = x * x
            n = n // 2
        
        return ans