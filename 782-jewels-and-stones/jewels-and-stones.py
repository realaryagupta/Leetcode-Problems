class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """

        counter = 0

        for i in stones:
            if i in jewels:
                counter = counter + 1

        return counter
        