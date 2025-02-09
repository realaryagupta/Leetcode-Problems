class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_count = 0
        close_count = 0

        for char in s:
            if char == "(":
                open_count += 1
            elif open_count > 0:
                open_count -= 1
            else:
                close_count += 1

        return open_count + close_count