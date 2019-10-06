from typing import List
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ret = []
        lefta, righta = 0, 0
        leftb, rightb = 0, 0
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i][0] > B[j][1]:
                j += 1
            elif A[i][1] < B[j][0]:
                i += 1
            # elif A[i][0] <= B[j][1] or :
            else:
                ret.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                if A[i][0] <= B[i][0] <= A[i][1] <= B[j][1] or \
                    B[j][0] <= A[i][0] <= A[i][1] <= B[j][1]:
                    i += 1
                else:
                    j += 1
        return ret
        
if __name__ == "__main__":
    A = [[4,6],[7,8],[10,17]]
    B = [[5,10]]
    sol = Solution()
    print(sol.intervalIntersection(A, B))