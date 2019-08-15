"""
sliding window
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        MAXINT = (1<<31)-1
        left, right = 0, 0
        ans = MAXINT, -1, -1    # len, start, end of substring in s
        cnt = {}
        for c in t:
            cnt[c] = cnt.get(c, 0) + 1
        count = len(t)
        while right < len(s):
            if s[right] in cnt:
                if cnt[s[right]] > 0:
                    count -= 1
                cnt[s[right]] -= 1
                
            while count == 0 and left <= right:
                if right - left + 1 < ans[0]:
                    ans = right-left+1, left, right
                if s[left] in cnt:
                    cnt[s[left]] += 1
                    if cnt[s[left]] > 0:
                        count += 1
                left += 1
            right += 1
        return '' if ans[0] == MAXINT else s[ans[1]: ans[2]+1]

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    print(sol.minWindow(s, t))
