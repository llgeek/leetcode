class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        cnt = Counter(t)
        missing = len(cnt)
        left, right = 0, 0
        ans = -1, (1<<21) - 1
        while right < len(s):
            if s[right] in cnt:
                cnt[s[right]] -= 1
                if cnt[s[right]] == 0:
                    missing -= 1
                while missing == 0 and left <= right:
                    if ans[1] > right - left + 1:
                        ans = left, right - left + 1
                    if s[left] in cnt:
                        cnt[s[left]] += 1
                        missing += (cnt[s[left]] > 0)
                    left += 1
            right += 1
        return s[ans[0]:ans[0]+ans[1]] if ans[0] != -1 else ''

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    print(sol.minWindow(s, t))
            
