class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        last_char_len = 0

        if s == "":
            return 0
        
        for i in range(len(s)-1 , -1, -1):
            if s[i] == " ":
                if last_char_len > 0:
                    break
            else:
                last_char_len = last_char_len + 1

        return last_char_len
