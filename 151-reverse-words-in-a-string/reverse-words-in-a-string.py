class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip()
        s = s.split()        
        arr = []

        for i in range(len(s) -1, -1, -1):
            arr.append(s[i])

        text = ""

        for char in arr:
            text = text + " " + char

        text = text.strip()
        return text
