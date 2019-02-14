"""
the idea is to find is there any intersections
"""

class Solution:
    def meetingRoom(self, intervals):
        intervals = sorted(intervals, key = lambda x: x[0])
        for i in range(len(intervals)):
            if i + 1 < len(intervals) and intervals[i][1] > intervals[i+1][0]:
                return False
        return True

if __name__ == "__main__":
    intervals = [[0, 30], [5, 10], [15, 20]]
    # intervals = [[7, 10], [2, 4]]
    sol = Solution()
    print(sol.meetingRoom(intervals))

