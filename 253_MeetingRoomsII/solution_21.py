class Solution():
    def meetingRoomII(self, intervals):
        start = sorted([s[0] for s in intervals])
        end = sorted([s[1] for s in intervals])
        endpos = 0
        res = 0
        for i in range(len(intervals)):
            if start[i] < end[endpos]:
                res += 1
            else:
                endpos += 1
        return res  
            

if __name__ == "__main__":
    # intervals = [[0, 30],[5, 10],[15, 20]]
    intervals = [[15, 20], [5, 10], [0, 30]]
    sol = Solution()
    print(sol.meetingRoomII(intervals))