import heapq
class Solution:
    def meetingRoomII(self, intervals):
        if len(intervals) < 2:
            return len(intervals)
        intervals.sort(key = lambda x: x[0])
        endpoint = [intervals[0][1]]
        for interval in intervals[1:]:
            if interval[0] > endpoint[0]:
                heapq.heappop(endpoint)
                heapq.heappush(endpoint, interval[1])
            else:
                heapq.heappush(endpoint, interval[1])
        return len(endpoint)

if __name__ == "__main__":
    intervals = [[0, 30],[5, 10],[15, 20]]
    # intervals = [[7,10],[2,4]]
    sol = Solution()
    print(sol.meetingRoomII(intervals))