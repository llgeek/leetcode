"""
similar idea as solution_21.py

start point +1, end point +1, overlapping will be accumulated and the max value of overlappings will be the number of rooms needed
"""
class Solution():
    def meetingRoomII(self, intervals):
        timemap = dict()
        for val in intervals:
            timemap[val[0]] = 1
            timemap[val[1]] = -1
        res = 0
        accsum = 0
        for key in sorted(timemap.keys()):
            accsum += timemap[key]
            res = max(res, accsum)
        return res  

if __name__ == "__main__":
    intervals = [[0, 30],[5, 10],[15, 20]]
    sol = Solution()
    print(sol.meetingRoomII(intervals))