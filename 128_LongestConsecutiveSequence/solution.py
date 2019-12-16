class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        vals = set(nums)
        res = 0
        firstseen = 0
        for val in vals:
            if val - 1 not in vals:
                firstseen = 1
                while val + 1 in vals:
                    firstseen += 1
                    val += 1
                res = max(res, firstseen)
        return res