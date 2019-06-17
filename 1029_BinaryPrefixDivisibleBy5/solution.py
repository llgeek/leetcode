class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = [False] * len(A)
        val = 0
        for i, num in enumerate(A):
            val = val + num
            if val % 5 == 0:
                res[i] = True
            val <<= 1
        return res
