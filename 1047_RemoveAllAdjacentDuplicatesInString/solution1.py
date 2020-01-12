"""
two pointers
"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        i = 0
        res = [None] * len(S)
        for j in range(len(S)):
            res[i] = S[j]
            if i > 0 and res[i-1] == res[i]:
                i -= 2
            i += 1
        return "".join(res[:i])
