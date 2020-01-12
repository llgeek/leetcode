from typing import List
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        s = set([1,2,3,4,5,6])
        for d in zip(A, B):
            s.intersection_update(set(d))
        if not s or len(s) > 2:
            return -1
        x = s.pop()
        return len(A) - max(A.count(x), B.count(x))


if __name__ == "__main__":
    sol = Solution()
    A = [2,1,2,4,2,2]
    B = [5,2,6,2,3,2]
    print(sol.minDominoRotations(A, B))

