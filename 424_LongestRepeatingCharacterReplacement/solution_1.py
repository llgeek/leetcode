class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        maxcnt = 0
        cnt = {}
        while right < len(s):
            cnt[s[right]] = cnt.get(s[right], 0) + 1
            maxcnt = max(maxcnt, cnt[s[right]])
            if maxcnt + k < right - left + 1:
                cnt[s[left]] -= 1
                left += 1
            right += 1
        return right - left + 1
