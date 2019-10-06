from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        if not intervals or not intervals[0]: return res
        left, right = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > right:
                res.append([left, right])
                left, right = intervals[i]
            else:
                right = max(right, intervals[i][1])
        res.append([left, right])
        return res

