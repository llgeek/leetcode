# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def insert(self, intervals: List[Interval], newInterval: Interval) -> List[Interval]:
        if not intervals:
            return [newInterval]
        res = []
        i = 0
        while i < len(intervals) and intervals[i].end < newInterval.start:
            res.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval = Interval(min(intervals[i].start, newInterval.start), max(intervals[i].end, newInterval.end))
            i += 1
        res.append(newInterval)
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res
        
            
