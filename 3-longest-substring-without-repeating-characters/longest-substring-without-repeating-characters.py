class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_length = 0
        hashset = set()

        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1

            hashset.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length