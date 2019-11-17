from typing import List
from collections import Counter
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        left, right = 0, 0
        res = 0
        cnt = Counter()
        distincnum = 0
        while right < len(tree):
          if cnt[tree[right]] == 0:
            distincnum += 1
          cnt[tree[right]] += 1
          while distincnum > 2 and left <= right:
            cnt[tree[left]] -= 1
            distincnum -= cnt[tree[left]] == 0
            left += 1
          res = max(res, right - left + 1)
          right += 1
        return res

