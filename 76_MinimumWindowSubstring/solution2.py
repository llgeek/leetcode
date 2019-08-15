from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = 0
        ans = 0, 0
        for right, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if ans[1] == 0 or ans[1] - ans[0] > right - left:
                    ans = left, right
        return s[ans[0]:ans[1]]



if __name__ == "__main__":
    # s = "ADOBECODEBANC"
    # t = "ABC"
    s = 'ab'
    t = 'a'
    sol = Solution()
    print(sol.minWindow(s, t))