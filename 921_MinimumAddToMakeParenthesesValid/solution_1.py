class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left, right = 0, 0
        res = 0
        for c in S:
            if c == '(':
                left += 1
            elif c == ')':
                right += 1
            if right > left:
                res += (right - left)
                left = right
        if left > right:
            res += (left - right)
        return res