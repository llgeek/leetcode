from typing import List
from collections import defaultdict
class Window():
  def __init__(self):
    self.cnt = defaultdict(lambda: 0)
    self.nonzero = 0
  def add(self, val):
    self.cnt[val] += 1
    self.nonzero += self.cnt[val] == 1
  def remove(self, val):
    self.cnt[val] -= 1
    self.nonzero -= self.cnt[val] == 0

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
      res = 0
      window1 = Window()
      window2 = Window()
      left1, left2 = 0, 0
      for right, val in enumerate(A):
        window1.add(val)
        window2.add(val)
        while window1.nonzero > K:
          window1.remove(A[left1])
          left1 += 1
        while window2.nonzero >= K:
          window2.remove(A[left2])
          left2 += 1
        res += (left2 - left1)
      return res
      