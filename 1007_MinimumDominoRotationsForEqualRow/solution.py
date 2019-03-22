class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def helper(A, B, cand):
            swap = 0
            for i in range(len(A)):
                if A[i] != cand:
                    if B[i] != cand:
                        return -1
                    else:
                        swap += 1
            return swap

        swap1 = helper(A, B, A[0])
        swap2 = helper(A, B, B[0])
        swap3 = helper(B, A, A[0])
        swap4 = helper(B, A, B[0])
        if swap1 == swap2 == swap3 == swap4 == -1:
            return -1
        else:
            return min(swap for swap in (swap1, swap2, swap3, swap4) if swap != -1)
