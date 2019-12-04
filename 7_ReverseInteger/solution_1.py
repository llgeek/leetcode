class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        flag = 1 if x>=0 else -1
        x *= flag
        while x:
          x, val = divmod(x, 10)
          res = res * 10 + val
          if res % 10 != val:
            return 0
        return res * flag if ((res < 1<<31 and flag == 1) or (res <= 1<<31 and flag == -1)) else 0