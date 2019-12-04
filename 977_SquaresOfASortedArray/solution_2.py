class Solution:
  def sortedSquares(self, A: List[int]) -> List[int]:
    res = []
    if not A:
      return res
    for i in range(len(A)):
      if A[i] > 0:
        break
    i, j = i-1, i
    while i >= 0 and j < len(A):
      P, Q = A[i] ** 2, A[j] ** 2
      if P <= Q:
        res.append(P)
        i -= 1
      else:
        res.append(Q)
        j += 1
    while i >= 0:
      res.append(A[i] ** 2)
      i -= 1
    while j < len(A):
      res.append(A[j] ** 2)
      j += 1
    return res