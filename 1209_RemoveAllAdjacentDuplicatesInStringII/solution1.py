"""
two pointers
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        i = 0
        res = [None] * len(s)
        cnt = [0] * len(s)
        for j in range(len(s)):
            res[i] = s[j]
            cnt[i] = cnt[i-1] + 1 if i > 0 and res[i-1] == res[i] else 1
            if cnt[i] == k:
                i -= k
            i += 1
        return "".join(res[:i])
            