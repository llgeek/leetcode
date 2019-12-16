from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter(t)
        remainnum = len(cnt)
        left, right = 0, 0
        ans = -1, len(s)
        while right < len(s):
            if s[right] in cnt:
                cnt[s[right]] -= 1
                if cnt[s[right]] == 0:
                    remainnum -= 1
            while remainnum == 0 and left <= right:
                if right - left < ans[1] - ans[0]:
                    ans = left, right
                if s[left] in cnt:
                    if cnt[s[left]] == 0:
                        remainnum += 1
                    cnt[s[left]] += 1
                left += 1
            right += 1
        return '' if ans[0] == -1 else s[ans[0]:ans[1]+1]

if __name__ == "__main__":
    sol = Solution()
    # s = "ADOBECODEBANC"
    # t = "ABC"
    s = "aaaaaaaaaaaabbbbbcdd"
    t = "abcdd"
    print(sol.minWindow(s, t))
            
