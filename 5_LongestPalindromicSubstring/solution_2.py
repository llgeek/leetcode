"""
second trial


"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        is_palind = [False] * len(s)
        for l in range(s):
            for i in range(s):
                if l+i > len(s)-1: continue
                if l == 0: is_palind[i] = True