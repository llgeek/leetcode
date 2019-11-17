class Solution:
    def minWindow(self, s: str, t: str) -> str:
      cnt = {}
      ans = -1, -1, (1<<31)-1

      for c in t:
        cnt[c] = cnt.get(c, 0) + 1
      left, right = 0, 0
      num = len(t)
      while right < len(s):
        if s[right] in cnt:
          if cnt[s[right]] > 0:
            num -= 1
          cnt[s[right]] -= 1
          while num == 0 and left <= right:
            if ans[2] > right - left + 1:
              ans = left, right, right-left+1
            if s[left] in cnt:
              cnt[s[left]] += 1
              if cnt[s[left]] > 0:
                num += 1
            left += 1
        right += 1
      return s[ans[0]:ans[1]+1] if ans[2] != (1<<31)-1 else ""

if __name__ == "__main__":
    # s = "ADOBECODEBANC"
    # t = "ABC"
    s = "bba"
    t = "ab"
    sol = Solution()
    print(sol.minWindow(s, t))