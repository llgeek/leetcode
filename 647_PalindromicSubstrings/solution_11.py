"""
expand from the center point
"""

class Solution:
    def countSubstrings(self, s: str) -> int:

      def expand(left, right):
        cnt = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
          cnt += 1
          left -= 1
          right += 1
        return cnt

      res = 0
      for i in range(len(s)):
        res += expand(i, i)
        res += expand(i, i+1)
      return res
