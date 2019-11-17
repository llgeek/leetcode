
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        def helper(A):
          for i in range(1, len(A)):
            if A[i] < A[i-1]:
              return False
          return True
        
        return helper(A) or helper(A[::-1])