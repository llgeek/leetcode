import heapq
class Solution:
    def meetingRoomII(self, intervals):
      if len(intervals) < 2:
        return len(intervals)
      intervals.sort(key=lambda x: x[0])
      endheap = [intervals[0][1]]
      res = 1
      for i in range(1, len(intervals)):
        if intervals[i][0] >= endheap[0]:
          heapq.heappop(endheap)
          heapq.heappush(endheap, intervals[i][1])
        else:
          heapq.heappush(endheap, intervals[i][1])
          res += 1
      return res

if __name__ == "__main__":
    # intervals = [[0, 30],[5, 10],[15, 20]]
    intervals = [[7,10],[2,4]]
    sol = Solution()
    print(sol.meetingRoomII(intervals))