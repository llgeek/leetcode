class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = 0
        right = -1
        for i, val in enumerate(light):
            right = max(right, val)
            if right == i + 1:
                res += 1
        return res


