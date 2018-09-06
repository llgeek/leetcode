# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not len(intervals):
            return []
        intervals = sorted(intervals, key=lambda x: x.start)
        result = []
        start, end = intervals[0].start, intervals[0].end
        for itv in intervals[1:]:
            if itv.start <= end:
                end = max(end,itv.end)
            else:
                result.append(Interval(start, end))
                start = itv.start
                end = itv.end
        result.append(Interval(start, end))
            
            
