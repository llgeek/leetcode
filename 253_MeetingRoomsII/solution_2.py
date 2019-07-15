class Solution:
    # def meetingRoomII(self, intervals):
    #     intervals.sort(key=lambda x: x[0])
    #     res = 0
    #     # end = (2<<31) - 1
    #     if not intervals:
    #         return res 
    #     end = intervals[0][1]
    #     for intv in intervals:
    #         if intv[0] < end:
    #             res += 1
    #             end = min(end, intv[1])
        
    #     return res

    def meetingRoomII(self, intervals):
        import heapq
        heap = []
        intervals.sort(key=lambda x: x[0])
        for intv in intervals:
            if heap and heap[0] < intv[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intv[1])
        return len(heap)

if __name__ == "__main__":
    intervals = [[0, 30],[5, 10],[15, 20]]
    sol = Solution()
    print(sol.meetingRoomII(intervals))