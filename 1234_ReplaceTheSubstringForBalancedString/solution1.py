from collections import Counter
class Solution:
    def balancedString(self, s: str) -> int:
      cnt = Counter(s)
      if len(cnt) > 4:
        raise RuntimeError
      left, right = 0, 0
      res = len(s)
      while right <= len(s):
        while any(cnt[c] > len(s)//4 for c in 'QWER'):
          if right >= len(s):
            break
          cnt[s[right]] -= 1
          right += 1
        if all(cnt[c] <= len(s)//4 for c in 'QWER'):
          res = min(res, right - left)
        elif right >= len(s): break
        if res == 0:
          break
        cnt[s[left]] += 1
        left += 1
      return res
    
    def balancedString2(self, s: str) -> int:
      cnt = Counter(s)
      if len(cnt) > 4:
        raise RuntimeError
      left, right = 0, 0
      res = len(s)
      while right <= len(s):
        if any(cnt[c] > len(s)//4 for c in 'QWER'):
          if right >= len(s):
            break
          cnt[s[right]] -= 1
          right += 1
          continue
        res = min(res, right - left)
        if res == 0:
          break
        cnt[s[left]] += 1
        left += 1
      return res


if __name__ == "__main__":
    sol = Solution()
    # s = "QQQQ"
    # s = 'WQER'
    s = "WQWRQQQW"
    print(sol.balancedString(s))