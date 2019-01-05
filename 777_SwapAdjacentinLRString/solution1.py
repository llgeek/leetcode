class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False
        l, r = 0, 0
        for i in range(len(start)):
            if start[i] == 'L': l += 1
            if start[i] == 'R': r += 1
            if end[i] == 'L': l -= 1
            if end[i] == 'R': r-= 1
            if l > 0 or r < 0 or (l < 0 and r != 0) or (r > 0 and l != 0):
                return False 
        return l == 0 and r == 0


if __name__ == "__main__":
    start = "RXXLRXRXL"
    end = "XRLXXRRLX"
    sol = Solution()
    print(sol.canTransform(start, end))
