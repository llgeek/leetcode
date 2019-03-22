# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        if not intervals:
            return intervals
        intervals.sort(key=lambda x: x.start)
        start, end = intervals[0].start, intervals[0].end
        res = []
        for interval in intervals[1:]:
            if interval.start > end:
                res.append(Interval(start, end))
                start = interval.start
                end = interval.end
            else:
                end = max(end, interval.end)
        res.append(Interval(start, end))
        return res
                