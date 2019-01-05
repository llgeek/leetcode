"""
sort start time and end time in ascending order

compare start time with end time
if start < end time, we need to assign one room,
otherwise, we can skip the current finish time and add endpos by one

O(nlogn)
"""


class Solution:
    def minMeetingRooms(self, intervals):
        starts = sorted([v[0] for v in intervals])
        ends = sorted([v[1] for v in intervals])

        res, endpos = 0, 0
        for i in range(len(starts)):
            if starts[i] < ends[endpos]:
                res += 1
            else:
                endpos += 1
            
        return res


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    sol = Solution()
    print(sol.minMeetingRooms(intervals))
