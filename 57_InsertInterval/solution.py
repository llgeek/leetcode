# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        if not intervals:
            return [newInterval]
        res = []
        finished = False
        for val in intervals:
            if not finished and val.start > newInterval.end:
                finished = True
                res.append(newInterval)
                res.append(val)
            elif not finished and (newInterval.start <= val.start <= newInterval.end or val.start <= newInterval.start <= val.end):
                # newInterval = [min(val[0], newInterval[0]), max(val[1], newInterval[1])]
                newInterval.start = min(val.start, newInterval.start)
                newInterval.end = max(val.end, newInterval.end)
            elif not finished and val.end < newInterval.start:
                res.append(val)
            elif finished:
                res.append(val)
            else:
                print('unhandled cases')
                print(val.start, val.end, newInterval.start, newInterval.end, finished)
        if not finished:
            res.append(newInterval)
        return res



            

            
