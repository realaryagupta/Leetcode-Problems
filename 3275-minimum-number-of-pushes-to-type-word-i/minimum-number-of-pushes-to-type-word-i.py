class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n = len(word)

        if n == 0:
            return 0
        elif n < 8:
            return n
        elif n < 16:
            return 8 + 2 * (n - 8)
        elif n < 24:
            return 8 + 2 * 8 + 3 * (n - 16)
        else:  
            return 8 + 2 * 8 + 3 * 8 + 4 * (n - 24)
