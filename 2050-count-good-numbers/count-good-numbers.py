class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def expo(x, num):
            if num == 0:
                return 1
            elif num % 2 == 0:
                return expo((x * x) % MOD, num // 2)
            return (x * expo(x, num - 1)) % MOD

        return 5 ** (n % 2) * expo(20, n // 2) % MOD
