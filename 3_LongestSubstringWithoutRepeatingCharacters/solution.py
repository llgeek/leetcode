"""
O(n)

use set
"""



class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, end = 0, 0
        maxlen = 0
        charset = set()
        nowlen = 0
        for end in range(len(s)):
            if s[end] not in charset:
                nowlen += 1
                charset.add(s[end])
            else:
                maxlen = max(maxlen, nowlen)
                while s[start] != s[end]:
                    charset.discard(s[start])
                    start += 1
                    nowlen -= 1
                start += 1
        return max(maxlen, nowlen)


if __name__ == "__main__":
    s = " "
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s))
