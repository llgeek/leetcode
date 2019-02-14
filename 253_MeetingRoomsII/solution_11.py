"""
second trial

sort start and end time seperately
"""

class Solution:
    def meetingRoomII(self, intervals):
        start = sorted([inter[0] for inter in intervals])
        end = sorted([inter[1] for inter in intervals])
        res, endpos = 0, 0
        for i in range(len(intervals)):
            if start[i] < end[endpos]:
                res += 1
            else:
                endpos += 1
        return res
        
