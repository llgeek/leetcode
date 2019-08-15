"""
optimized sliding window
"""
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        MAXINT = (1<<31)-1
        ans = MAXINT, 0, 0
        left, right = 0, 0
        cnt = Counter(t)
        count = len(t)
        filters = [(i, c) for i, c in enumerate(s) if c in cnt]
        while right < len(filters):
            idx, c = filters[right]
            if cnt[c] > 0:
                count -= 1
            cnt[c] -= 1
            while count == 0:
                if idx - filters[left][0] + 1 < ans[0]:
                    ans = idx - filters[left][0] + 1, filters[left][0], idx
                cnt[filters[left][1]] += 1
                if cnt[filters[left][1]] > 0:
                    count += 1
                left += 1
            right += 1
        return '' if ans[0] == MAXINT else s[ans[1]: ans[2]+1]