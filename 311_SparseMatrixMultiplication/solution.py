import numpy as np
class Solution():
    def sparseMatrixMul(self, A, B):
        """
        type A: list
        type B: list
        rtype list
        """
        A = np.asarray(A)
        B = np.asarray(B)
        if len(B.shape) == 1:
            B = np.matrix(B).T
        C = np.zeros((A.shape[0], B.shape[1]))
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                if A[i][j] != 0:
                    for k in range(B.shape[1]):
                        C[i][k] += A[i][j]*B[j][k]
        return C.tolist()

if __name__ == '__main__':
    # A = [[1,2,3], [0,2,1], [0,0,3]]
    # B = [[2,0], [1,2], [0,1]]
    A = [[2.0,	-1.0,	0,	0],
[-1.0,	2.0,	-1.0,	0],
[0,	-1.0,	2.0,	-1.0],
[0,	0,	-1.0,	2.0]]

    B = [1.0, 0.0, -1.0, 0.0]

    print(Solution().sparseMatrixMul(A, B))


