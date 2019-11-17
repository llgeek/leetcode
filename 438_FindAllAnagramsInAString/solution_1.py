from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
      left, right = 0, 0
      res = []
      needed = Counter(p)
      missing = len(needed)
      have = {}
      while right < len(s):
        if s[right] in needed:
          have[s[right]] = have.get(s[right], 0) + 1
          if have[s[right]] == needed[s[right]]:
            missing -= 1
          while missing == 0:
            if right - left + 1 == len(p):
              res.append(left)
            if s[left] in needed:
              have[s[left]] -= 1
              if have[s[left]] < needed[s[left]]: 
                missing += 1
            left += 1
        else:
          left = right + 1
          have = {}
          missing = len(needed)
        right += 1
      return res

if __name__ == "__main__":
    s = "cbaebabacd"
    t = "abc"
    sol = Solution()
    print(sol.findAnagrams(s, t))