"""
use min-heap

sort the intervals in ascending order by the start time
then put the finish the time to the heap

compare the next start time with the earliest finish time,
if the start time is larger than finish time, then pop out the finish time and update with current finish time
otherwise, we cannot fit this task into the assigned rooms, so we need to increment one room.

O(nlogn)
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals or len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key = lambda x: x[0])
        queue = []
        # heapq.heappush(queue, intervals[0][1])
        for inter in intervals:
            if queue and queue[0] <= inter[0]:
                heapq.heappop(queue)
            heapq.heappush(queue, inter[1])
        return len(queue)


if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    sol = Solution()
    print(sol.minMeetingRooms(intervals))
