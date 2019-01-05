"""
use dict to accelerate processing
O(n) time complexity
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        seechar = dict()
        maxlen = 0
        for idx, char in enumerate(s):
            if char in seechar and seechar[char] >= start:
                start = seechar[char] + 1
                seechar[char] = idx
            else:
                seechar[char] = idx
                maxlen = max(idx - start + 1, maxlen)
        return maxlen
