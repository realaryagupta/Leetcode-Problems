class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""

        while columnNumber > 0:
            #  decrease one to adjust indexes
            columnNumber -= 1

            remainder = columnNumber % 26
            curr_char = chr(remainder + ord("A"))

            # yeah order bhi matter karta hai test case galat hua thaa
            ans = curr_char + ans

            columnNumber = columnNumber // 26

        return ans