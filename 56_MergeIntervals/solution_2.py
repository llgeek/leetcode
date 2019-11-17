class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) < 2:
          return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
          if intervals[i][0] > res[-1][1]:
            res.append(intervals[i][:])
          else:
            res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
        return res
