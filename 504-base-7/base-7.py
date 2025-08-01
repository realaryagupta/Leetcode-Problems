class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        base = 7
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        isNegative = False

        if num < 0:
            isNegative = True
            num = -num

        while num > 0:
            remainder = num % base
            num = num // base
            result = digits[remainder] + result

        if isNegative:
            result = "-" + result

        return result
