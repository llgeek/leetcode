from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        if len(cnt) > 4:
          raise RuntimeError
        res = len(s)
        left = 0
        for right, c in enumerate(s):
          cnt[c] -= 1
          while left < len(s) and all(cnt[ch] <= len(s)//4 for ch in 'QWER'):
            res = min(res, right - left + 1)
            cnt[s[left]] += 1
            left += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    # s = "QQQQ"
    # s = 'WQER'
    s = "WQWRQQQW"
    print(sol.balancedString(s))