class Solution:
    def isPalindrome(self, x: int) -> bool:
      if x < 0: return False
      revx = 0
      copyx = x
      while x:
        x, m = divmod(x, 10)
        revx = revx * 10 + m
      return revx == copyx
