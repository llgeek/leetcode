"""
second trial

"""

import heapq
class Solution:
    def meetingRoomII(self, intervals):
        intervals.sort(key=lambda x: x[0])
        heap = []
        for intval in intervals:
            if heap and heap[0][0] <= intval[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (intval[1], intval[0]))
            else:
                heapq.heappush(heap, (intval[1], intval[0]))
        return len(heap)

if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    sol = Solution()
    print(sol.meetingRoomII(intervals))
        
