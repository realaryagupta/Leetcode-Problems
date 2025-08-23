class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber > 0:
            columnNumber = columnNumber - 1

            remainder = int((columnNumber % 26) + ord('A'))
            char = chr(remainder)
            res = char + res

            columnNumber //= 26

        return res

